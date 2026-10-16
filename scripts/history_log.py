#!/usr/bin/env python3
"""Le journal du contexte : ce qu'un tour a etabli, range sous sa rubrique.

Voir docs/history.md. Trois usages :

  history_log.py open <contexte>                pose le repere, cree le fichier du jour
  history_log.py extract --transcript <chemin>  la passe (appelee par le hook, a chaque tour)
  history_log.py catchup [--full]               la meme passe, appelee par save

La passe ne casse jamais une seance : toute panne sort en code 0, sans rien ecrire.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from datetime import date, datetime
from pathlib import Path

from _common import SYSTEM_ROOT, resolve_context

STATE_FILE = SYSTEM_ROOT / ".state" / "history.json"
DEBUG_FILE = SYSTEM_ROOT / ".state" / "history-log-debug.log"
PROMPT_FILE = SYSTEM_ROOT / "prompts" / "history_extract.md"

# Ce qu'on soumet au modele. Court volontairement : devant un mur de texte il resume en
# abstractions, devant un echange il rapporte des faits nommes. C'est la difference
# mesuree avec 02-CONTEXT/memory_sessions, qui tourne sur le meme modele.
MAX_CHARS = 6000
TOOL_CHARS = 400

LINE_RE = re.compile(r"^- (\d{2}:\d{2}) · (\S+) — (.*?)\s*$")
TIME_RE = re.compile(r"^\d{2}:\d{2}$")

# Les sept rubriques, dans l'ordre ou elles apparaissent dans le fichier du jour.
# Une rubrique ne recoit qu'un fait : c'est ce qui empeche la ligne de devenir une
# etiquette qui designe sans rien dire.
RUBRICS = (
    ("connaissances", "Connaissances acquises"),
    ("acte", "Ce qui est désormais acté"),
    ("ecarte", "Écarté — ne pas reproposer"),
    ("revise", "Révisé — ne plus s'appuyer dessus"),
    ("problemes", "Problèmes rencontrés"),
    ("a_suivre", "À suivre"),
    ("derive", "Dérive de la mission"),
)
TITLES = dict(RUBRICS)


# --- etat -------------------------------------------------------------------


def trace(message: str) -> None:
    """Une ligne par passage. Un filet muet ne se repare pas : il faut savoir pourquoi
    il n'a rien fait."""
    try:
        DEBUG_FILE.parent.mkdir(parents=True, exist_ok=True)
        with DEBUG_FILE.open("a", encoding="utf-8") as handle:
            handle.write("{} {}\n".format(datetime.now().isoformat(timespec="seconds"), message))
    except OSError:
        pass


def read_state() -> dict:
    try:
        return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def write_state(state: dict) -> None:
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")


# --- le fichier du jour -----------------------------------------------------


def day_file(context: Path, day: str) -> Path:
    folder = context / "02-history"
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / f"{day}.md"
    if not path.exists():
        path.write_text(f"# Journal — {context.name} — {day}\n", encoding="utf-8")
    return path


def normalise(text: str) -> str:
    """Pour comparer deux faits sans se laisser avoir par la ponctuation."""
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def existing_statements(path: Path) -> list:
    out = []
    try:
        for line in path.read_text(encoding="utf-8").splitlines():
            match = LINE_RE.match(line)
            if match:
                out.append(match.group(3))
    except OSError:
        pass
    return out


def append_under(path: Path, added: dict) -> None:
    """Range chaque fait sous sa rubrique, en creant les rubriques manquantes dans l'ordre.

    Rien n'est jamais retire ni reecrit : on ajoute a la fin de la rubrique concernee.
    """
    lines = path.read_text(encoding="utf-8").splitlines()
    for key, title in RUBRICS:
        fresh = added.get(key)
        if not fresh:
            continue
        heading = "## " + title
        if heading in lines:
            cut = len(lines)
            for position in range(lines.index(heading) + 1, len(lines)):
                if lines[position].startswith("## "):
                    cut = position
                    break
            while cut > 0 and not lines[cut - 1].strip():
                cut -= 1
            lines[cut:cut] = fresh
        else:
            if lines and lines[-1].strip():
                lines.append("")
            lines += [heading, ""] + fresh
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def open_session(context: Path) -> str:
    """Cree au besoin le fichier du jour, et renvoie sa date.

    Pas de section de seance : une ligne se lit seule, un titre de seance laisserait
    croire qu'on peut s'appuyer dessus.
    """
    day = date.today().isoformat()
    day_file(context, day)
    return day


# --- la transcription -------------------------------------------------------


def text_of(value) -> str:
    if isinstance(value, str):
        return value.strip()
    if isinstance(value, list):
        parts = []
        for item in value:
            if isinstance(item, dict) and item.get("type") == "text":
                parts.append(str(item.get("text", "")))
            elif isinstance(item, str):
                parts.append(item)
        return " ".join(p for p in parts if p.strip()).strip()
    return ""


def tool_of(value) -> str:
    """Ce qu'un tour a lu ou ecrit, resume court.

    Sans ca, la passe ne voit que ce qui a ete *dit* : une note ouverte pendant le tour
    et jamais citee a l'ecran lui reste invisible, et sa ligne ne peut que la designer.
    """
    if not isinstance(value, list):
        return ""
    parts = []
    for item in value:
        if not isinstance(item, dict):
            continue
        kind = item.get("type")
        if kind == "tool_use":
            data = item.get("input") if isinstance(item.get("input"), dict) else {}
            target = ""
            for field in ("file_path", "path", "notebook_path", "pattern", "command", "url"):
                if data.get(field):
                    target = str(data[field])
                    break
            parts.append("{} {}".format(item.get("name") or "outil", target).strip())
        elif kind == "tool_result":
            body = text_of(item.get("content"))
            if body:
                parts.append(body[:TOOL_CHARS])
    return "\n".join(p for p in parts if p.strip()).strip()


def read_transcript(path: Path, start: int) -> tuple:
    """Les echanges depuis la ligne `start`. Tolere Claude Code et Codex.

    Renvoie (echanges, nouveau_repere). Un echange = (heure, role, texte). Le role vaut
    AUTEUR, IA, ou OUTIL pour ce qui a ete lu et ecrit pendant le tour.
    """
    exchanges = []
    index = 0
    try:
        with path.open(encoding="utf-8", errors="replace") as handle:
            for index, raw in enumerate(handle, start=1):
                if index <= start or not raw.strip():
                    continue
                try:
                    record = json.loads(raw)
                except ValueError:
                    continue
                if not isinstance(record, dict):
                    continue
                message = record.get("message")
                message = message if isinstance(message, dict) else {}
                role = record.get("role") or message.get("role") or record.get("type") or ""
                if role not in ("user", "assistant"):
                    continue
                stamp = str(record.get("timestamp") or message.get("timestamp") or "")
                found = re.search(r"T(\d{2}:\d{2})", stamp)
                hhmm = found.group(1) if found else ""
                body = text_of(message.get("content"))
                if not body:
                    body = text_of(record.get("content")) or text_of(record.get("text"))
                if body:
                    exchanges.append((hhmm, "AUTEUR" if role == "user" else "IA", body))
                tools = tool_of(message.get("content")) or tool_of(record.get("content"))
                if tools:
                    exchanges.append((hhmm, "OUTIL", tools))
    except OSError:
        return [], start
    return exchanges, index


# --- l'appel au modele ------------------------------------------------------


def frame_of(context: Path) -> str:
    """Le nom du contexte et son but, pour que le modele sache de quoi il tient le journal.

    Sans ca il ecrit « le label », « le systeme » : il n'a aucun nom propre a quoi rattacher
    ce qu'il lit.
    """
    goal = ""
    mission = context / "00-frame" / "mission.md"
    if mission.exists():
        in_goal = False
        parts = []
        for line in mission.read_text(encoding="utf-8").splitlines():
            stripped = line.strip()
            if stripped.startswith("## "):
                if in_goal:
                    break
                in_goal = stripped == "## Le but"
                continue
            if in_goal and stripped and not stripped.startswith("<!--"):
                parts.append(stripped)
        goal = " ".join(parts)
    return "Ce contexte s'appelle `{}`.{}".format(
        context.name, " Son but : {}".format(goal) if goal else ""
    )


def build_prompt(exchanges: list, known: list, frame: str = "") -> str:
    """Le texte vit dans prompts/history_extract.md — il se corrige sans toucher au code."""
    kept, budget = {}, MAX_CHARS
    # La conversation d'abord : sinon le contenu des fichiers lus la chasse de la fenetre.
    for position in range(len(exchanges) - 1, -1, -1):
        _, role, text = exchanges[position]
        if role == "OUTIL":
            continue
        if len(text) > budget:
            break
        kept[position] = text
        budget -= len(text)
    for position in range(len(exchanges) - 1, -1, -1):
        _, role, text = exchanges[position]
        if role != "OUTIL" or budget <= 0:
            continue
        piece = text[: min(TOOL_CHARS, budget)]
        kept[position] = piece
        budget -= len(piece)

    body = "\n\n".join(
        "[{}] {}\n{}".format(exchanges[i][0] or "??:??", exchanges[i][1], kept[i])
        for i in sorted(kept)
    )
    already = "\n".join("- {}".format(k) for k in known[-120:]) or "(rien encore)"

    template = re.sub(r"<!--.*?-->\s*", "", PROMPT_FILE.read_text(encoding="utf-8"), flags=re.DOTALL)
    values = {"{{ECHANGE}}": body, "{{DEJA}}": already, "{{CONTEXTE}}": frame or "(inconnu)"}
    # Une seule passe : ce qu'on injecte n'est jamais relu, sinon une transcription qui
    # contient une marque se ferait substituer a son tour.
    return re.sub(r"\{\{(?:ECHANGE|DEJA|CONTEXTE)\}\}", lambda m: values[m.group(0)], template)


def ask_model(prompt: str) -> str:
    """Un appel, au premier CLI disponible. Toute panne renvoie une chaine vide."""
    if shutil.which("claude"):
        command = ["claude", "--print", "--model", "claude-haiku-4-5-20251001"]
        stdin_prompt = True
    elif shutil.which("codex"):
        command = ["codex", "exec", "--skip-git-repo-check", prompt]
        stdin_prompt = False
    else:
        return ""
    try:
        result = subprocess.run(
            command,
            input=prompt if stdin_prompt else None,
            capture_output=True,
            text=True,
            timeout=600,
            cwd="/tmp",
        )
    except (OSError, subprocess.SubprocessError):
        return ""
    return result.stdout or ""


def parse_lines(raw: str) -> list:
    match = re.search(r"\{.*\}", raw, re.DOTALL)
    if not match:
        return []
    try:
        data = json.loads(match.group())
    except ValueError:
        return []
    out = []
    for item in data.get("lignes", []) if isinstance(data, dict) else []:
        if not isinstance(item, dict):
            continue
        rubric = str(item.get("rubrique", "")).strip().lower()
        rubric = re.sub(r"[^a-z_]", "", rubric.replace("é", "e").replace("è", "e"))
        if rubric not in TITLES:
            continue
        statement = " ".join(str(item.get("fait", "")).split())
        if not statement:
            continue
        hhmm = str(item.get("heure", "")).strip()
        if not TIME_RE.match(hhmm):
            hhmm = datetime.now().strftime("%H:%M")
        source = " ".join(str(item.get("provenance", "")).split()) or "IA"
        out.append((hhmm, rubric, statement, source))
    return out


# --- les commandes ----------------------------------------------------------


def cmd_open(args) -> int:
    context = resolve_context(args.contexte)
    day = open_session(context)
    state = read_state()
    state.update({"context": context.name, "opened": datetime.now().isoformat(timespec="seconds")})
    state.pop("cursor", None)
    state.pop("transcript", None)
    write_state(state)
    print("Journal — {} · {}".format(context.name, day))
    return 0


def run_pass(transcript: Path, full: bool) -> int:
    state = read_state()
    name = state.get("context")
    if not name:
        trace("stop : aucun repere dans .state/history.json — lancer `open` sur un contexte")
        return 0
    try:
        context = resolve_context(name)
    except SystemExit:
        trace("stop : contexte du repere introuvable ({})".format(name))
        return 0
    if not transcript or not transcript.is_file():
        trace("stop : transcription absente ({})".format(transcript))
        return 0

    # Le repere appartient a la seance qui a lance `open`. Une autre session, en
    # parallele, ne doit pas verser dans ce contexte.
    bound = state.get("transcript")
    if bound and bound != str(transcript):
        trace("stop : transcription etrangere au repere — relancer `open` pour la lier ({})".format(name))
        return 0

    start = 0 if full or not bound else int(state.get("cursor") or 0)
    exchanges, cursor = read_transcript(transcript, start)
    if not exchanges:
        state.update({"transcript": str(transcript), "cursor": cursor})
        write_state(state)
        trace("rien de neuf — {} · repere {}".format(name, cursor))
        return 0

    path = day_file(context, date.today().isoformat())
    known = existing_statements(path)
    seen = {normalise(k) for k in known}

    raw = ask_model(build_prompt(exchanges, known, frame_of(context)))
    if not raw.strip():
        trace("stop : le modele n'a rien renvoye ({} echange(s) soumis)".format(len(exchanges)))
    lines = parse_lines(raw)

    added, total = {}, 0
    for hhmm, rubric, statement, source in lines:
        key = normalise(statement)
        if not key or key in seen:
            continue
        seen.add(key)
        added.setdefault(rubric, []).append("- {} · {} — {}".format(hhmm, source, statement))
        total += 1

    if added:
        append_under(path, added)

    state.update({"transcript": str(transcript), "cursor": cursor})
    write_state(state)
    trace(
        "{} ligne(s) ajoutee(s) sur {} classee(s) — {} · {} echange(s) lu(s)".format(
            total, len(lines), name, len(exchanges)
        )
    )
    print("{} ligne(s) ajoutee(s) — {}".format(total, path.name))
    return 0


def cmd_extract(args) -> int:
    return run_pass(Path(args.transcript).expanduser(), full=bool(args.full))


def cmd_catchup(args) -> int:
    raw = args.transcript or read_state().get("transcript")
    if not raw:
        return 0
    return run_pass(Path(raw).expanduser(), full=bool(args.full))


def main() -> int:
    parser = argparse.ArgumentParser(description="Le journal d'un contexte V2.")
    sub = parser.add_subparsers(dest="command", required=True)

    p_open = sub.add_parser("open", help="pose le repere et cree le fichier du jour")
    p_open.add_argument("contexte")
    p_open.set_defaults(func=cmd_open)

    p_extract = sub.add_parser("extract", help="la passe, a chaque fin de tour")
    p_extract.add_argument("--transcript", required=True)
    p_extract.add_argument("--full", action="store_true", help="ignorer le repere de lecture")
    p_extract.set_defaults(func=cmd_extract)

    p_catchup = sub.add_parser("catchup", help="la passe, appelee par save")
    p_catchup.add_argument("--transcript", default=None)
    p_catchup.add_argument("--full", action="store_true", help="relire depuis le debut")
    p_catchup.set_defaults(func=cmd_catchup)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except Exception:  # une panne ne doit jamais casser une seance
        sys.exit(0)
