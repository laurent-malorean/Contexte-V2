#!/usr/bin/env python3
"""Verse la parole du jour dans la source de session, et gère le repère de lecture.

Un fichier par jour et par contexte. On ajoute à la fin, jamais on ne réécrit.
Deux sections, jamais mélangées : ce que l'auteur a dit, et les interventions de
l'IA sans lesquelles sa réponse ne se comprendrait pas.

  session_append.py <contexte> --auteur "…"
  session_append.py <contexte> --ia "…"
  session_append.py <contexte> --lu-jusquici        (repose le repère de lecture)
  session_append.py <contexte> --a-lire             (ce qui reste après le repère)
"""

from __future__ import annotations

import argparse
from datetime import date, datetime
from pathlib import Path

from _common import resolve_context
from refresh_readmes import refresh_context

AUTHOR = "## Propos de l'auteur"
ASSISTANT = "## Interventions de l'IA nécessaires à la compréhension"
MARKER = "<!-- lu jusqu'ici : "


def session_file(context: Path, day: str) -> Path:
    folder = context / "03-sources" / "sessions"
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / f"SESSION-{day}.md"
    if not path.exists():
        path.write_text(f"# Session — {day}\n\n{AUTHOR}\n\n{ASSISTANT}\n", encoding="utf-8")
    return path


def section_end(lines: list[str], section: str) -> int:
    """Indice de la fin de la section visée : la section suivante, ou le repère."""
    if section not in lines:
        lines += ["", section, ""]
    start = lines.index(section) + 1
    for i in range(start, len(lines)):
        if lines[i].startswith("## ") or lines[i].startswith(MARKER):
            return i
    return len(lines)


def insert(path: Path, section: str, block: list[str]) -> None:
    """Insère à la fin de la section visée, en gardant l'ordre des deux blocs."""
    lines = path.read_text(encoding="utf-8").splitlines()
    end = section_end(lines, section)
    if end > 0 and lines[end - 1].strip():
        block = [""] + block
    lines[end:end] = block + [""]
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def append(path: Path, section: str, text: str) -> None:
    insert(path, section, [f"**{datetime.now().strftime('%H:%M')}** — {text.strip()}"])


def entries(lines: list[str], section: str) -> list[str]:
    """Les propos d'une section, dans l'ordre du fichier."""
    if section not in lines:
        return []
    found = []
    for line in lines[lines.index(section) + 1:]:
        if line.startswith("## ") or line.startswith(MARKER):
            break
        if line.startswith("**"):
            found.append(line)
    return found


def read_counts(marker: str) -> dict[str, int] | None:
    """Le nombre de propos déjà lus par section, tel que le repère l'a noté."""
    counts = {}
    for part in marker.split("·")[1:]:
        key, _, value = part.replace("-->", "").strip().partition(" ")
        if value.strip().isdigit():
            counts[key] = int(value)
    return counts if {"auteur", "ia"} <= counts.keys() else None


def unread(path: Path) -> str:
    """Ce qui a été ajouté depuis le dernier repère de lecture.

    Les propos s'insèrent à la fin de leur section, donc au-dessus du repère :
    la position ne dit rien. Le repère note combien de propos chaque section
    comptait quand il a été posé ; tout ce qui vient après est à lire.
    """
    lines = path.read_text(encoding="utf-8").splitlines()
    marker = next((l for l in lines if l.startswith(MARKER)), None)
    if marker is None:
        return "\n".join(lines).strip()
    counts = read_counts(marker)
    blocks = []
    for key, section in (("auteur", AUTHOR), ("ia", ASSISTANT)):
        found = entries(lines, section)
        if counts is None:
            # Ancien repère sans compteurs : on se fie à l'heure, à la minute près.
            stamp = marker[len(MARKER):].split("-->")[0].strip()[-5:]
            new = [e for e in found if e[2:7] >= stamp]
        else:
            new = found[counts[key]:]
        if new:
            blocks.append("\n\n".join([section] + new))
    return "\n\n".join(blocks)


def place_marker(path: Path) -> None:
    lines = [l for l in path.read_text(encoding="utf-8").splitlines() if not l.startswith(MARKER)]
    text = "\n".join(lines).rstrip()
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    counts = f"auteur {len(entries(lines, AUTHOR))} · ia {len(entries(lines, ASSISTANT))}"
    path.write_text(f"{text}\n\n{MARKER}{stamp} · {counts} -->\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Écrire dans la source de session du jour.")
    parser.add_argument("contexte")
    parser.add_argument("--auteur", help="Un propos de l'auteur")
    parser.add_argument("--ia", help="Une intervention de l'IA nécessaire à la compréhension")
    parser.add_argument("--lu-jusquici", action="store_true", help="Repose le repère de lecture")
    parser.add_argument("--a-lire", action="store_true", help="Affiche ce qui reste à ingérer")
    parser.add_argument("--date", default=date.today().isoformat())
    args = parser.parse_args()

    context = resolve_context(args.contexte)
    path = session_file(context, args.date)

    if args.a_lire:
        print(unread(path) or "(rien de nouveau depuis la dernière lecture)")
        return
    if args.lu_jusquici:
        place_marker(path)
        print(f"repère posé en fin de {path.name}")
        return

    if not (args.auteur or args.ia):
        raise SystemExit("Donner --auteur, --ia, --lu-jusquici ou --a-lire.")
    if args.auteur:
        append(path, AUTHOR, args.auteur)
    if args.ia:
        append(path, ASSISTANT, args.ia)

    refresh_context(context)
    print(f"écrit dans {path.relative_to(context)}")


if __name__ == "__main__":
    main()
