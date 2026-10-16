#!/usr/bin/env python3
"""Régénère tous les README de navigation.

Un README n'est jamais écrit à la main : il est reconstruit à partir des fichiers
présents. C'est la seule façon qu'il ne mente pas.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

from _common import (
    ARCHIVE_ROOT,
    CONTEXTS_ROOT,
    NOTE_KINDS,
    content_files,
    frontmatter_of,
    iter_dirs,
    title_of,
)

GENERATED = "<!-- Généré par scripts/refresh_readmes.py — ne pas écrire à la main. -->"


def write(path: Path, lines: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines + ["", GENERATED, ""]), encoding="utf-8")


def context_goal(context: Path) -> str:
    mission = context / "00-frame" / "mission.md"
    if not mission.exists():
        return "à compléter"
    in_goal = False
    for line in mission.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped.startswith("## "):
            in_goal = stripped == "## Le but"
            continue
        if in_goal and stripped and not stripped.startswith("<!--"):
            return stripped
    return "à compléter"


# --------------------------------------------------------------------------- notes


def note_rows(folder: Path, prefix: str) -> list[str]:
    rows = []
    for path in content_files(folder, "*.md"):
        ident = frontmatter_of(path).get("id") or path.stem.split("-", 1)[0]
        rows.append(f"- [{ident}]({path.name}) — {title_of(path)}")
    return rows


def write_note_readme(folder: Path, kind: str) -> None:
    prefix, _, _, heading, empty = NOTE_KINDS[kind]
    intro = {
        "atomic": "Une idée par note. Le titre est une proposition, pas une étiquette.",
        "thematic": "Un angle qui relie plusieurs notes, et fait apparaître ce qu'aucune ne dit seule.",
        "glossary": "Un terme du domaine, stabilisé. Un mot va ici, une proposition va en note atomique.",
        "decision-record": (
            "Un arbitrage tranché **sur le sujet** du contexte. Une fois acté, il ne se réécrit jamais."
        ),
    }[kind]
    rows = note_rows(folder, prefix)
    lines = [f"# {heading}", "", intro, "", f"`{prefix}00001-…`", ""]
    if kind == "decision-record":
        lines += [
            "À ne pas confondre avec [01-state/decisions.md](../../01-state/decisions.md), qui porte",
            "sur le contexte comme outil. Deux objets différents, pas deux tailles du même objet.",
            "",
        ]
    lines += rows if rows else [f"*{empty}*"]
    write(folder / "README.md", lines)


def write_notes_readme(context: Path) -> None:
    root = context / "04-notes"
    counts = {}
    for kind, (prefix, folder_name, *_rest) in NOTE_KINDS.items():
        counts[kind] = len(content_files(root / folder_name, "*.md"))
    lines = [
        "# 04-notes — la connaissance",
        "",
        "Ce qu'on a compris à partir des sources. Une note est neutre : elle ne se met jamais",
        "en forme pour un livrable.",
        "",
        "| | | |",
        "|---|---|---|",
        f"| [atomic/](atomic/README.md) | `ATO` | {counts['atomic']} |",
        f"| [thematic/](thematic/README.md) | `THM` | {counts['thematic']} |",
        f"| [glossary/](glossary/README.md) | `GLO` | {counts['glossary']} |",
        f"| [decision-records/](decision-records/README.md) | `DRE` | {counts['decision-record']} |",
        "",
        "Trois règles valent pour les quatre types :",
        "",
        "- **toute note a une source identifiable**, y compris quand cette source est la parole de l'auteur ;",
        "- **une note n'est jamais supprimée** : elle est remplacée, reste en place marquée comme telle,",
        "  et pointe vers celle qui prend le relais — qui pointe en retour vers elle ;",
        "- **tout lien est expliqué, bidirectionnel, et sa relation est nommée.**",
    ]
    write(root / "README.md", lines)
    for kind, (_prefix, folder_name, *_rest) in NOTE_KINDS.items():
        write_note_readme(root / folder_name, kind)


# ------------------------------------------------------------------------- sources


def ingestion_state(context: Path) -> dict[str, dict[str, str]]:
    """Lit ingestion-log.md. Le journal est la vérité sur ce qu'une source a produit."""
    log = context / "03-sources" / "ingestion-log.md"
    state: dict[str, dict[str, str]] = {}
    if not log.exists():
        return state
    current = None
    for line in log.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            current = line[3:].strip()
            state[current] = {}
        elif current and line.strip().startswith("- ") and " : " in line:
            key, value = line.strip()[2:].split(" : ", 1)
            state[current][key.strip()] = value.strip()
    return state


def write_sources_readme(context: Path) -> None:
    root = context / "03-sources"
    docs = root / "documents"
    sessions = root / "sessions"
    log = ingestion_state(context)

    groups: dict[str, list[str]] = {}
    for path in content_files(docs, "*.md"):
        fm = frontmatter_of(path)
        ident = path.stem.split("-", 1)[0]
        entry = log.get(path.stem) or log.get(ident) or {}
        etat = entry.get("état", "non ingérée")
        produit = entry.get("a produit", "—")
        if fm.get("extraction") == "failed":
            etat = "**extraction échouée**"
        intention = fm.get("intention") or "sans intention"
        groups.setdefault(intention, []).append(
            f"| [{ident}]({path.relative_to(root).as_posix()}) | {title_of(path)} | {etat} | {produit} |"
        )

    lines = [
        "# 03-sources — la matière",
        "",
        "Ce qui a été dit, lu, observé ou importé — jamais ce qu'on en a compris.",
        "",
        "| | |",
        "|---|---|",
        f"| [documents/](documents/README.md) | de la matière produite ailleurs, qui arrive finie — {len(content_files(docs, '*.md'))} |",
        f"| [sessions/](sessions/README.md) | de la parole, produite ici — {len(content_files(sessions, 'SESSION-*.md'))} |",
        "| [ingestion-log.md](ingestion-log.md) | quelle source a été lue, quand, et ce qu'elle a donné |",
        "",
    ]

    if groups:
        lines.append("## Les documents, par intention")
        lines.append("")
        for intention in sorted(groups):
            lines += [
                f"### {intention}",
                "",
                "| Réf. | Titre | Ingestion | A produit |",
                "|---|---|---|---|",
                *sorted(groups[intention]),
                "",
            ]
    else:
        lines += ["*Aucun document.*", ""]

    session_files = content_files(sessions, "SESSION-*.md")
    lines.append("## Les sessions")
    lines.append("")
    if session_files:
        for path in session_files:
            date = path.stem.removeprefix("SESSION-")
            entry = log.get(path.stem, {})
            etat = entry.get("état", "non ingérée")
            lines.append(f"- [{date}](sessions/{path.name}) — {etat}")
    else:
        lines.append("*Aucune session.*")

    write(root / "README.md", lines)

    write(
        docs / "README.md",
        [
            "# documents — la matière qui arrive finie",
            "",
            "Un article, un livre, une vidéo, un PDF, une page web. Elle existe comme objet fini",
            "et ne bougera plus. Une fiche par source ici ; le fichier reçu et son texte en dessous.",
            "",
            "| | |",
            "|---|---|",
            "| [raw/](raw/README.md) | le fichier d'origine, tel qu'il est arrivé |",
            "| [fulltext/](fulltext/README.md) | son texte, quand le format n'était pas lisible |",
            "",
            "**Ce qui sera analysé est le texte intégral, jamais un résumé.** Une source dont",
            "l'extraction a échoué garde sa fiche mais ne produit aucune note.",
            "",
            *(
                [f"- [{p.stem}]({p.name}) — {title_of(p)}" for p in content_files(docs, "*.md")]
                or ["*Aucun document.*"]
            ),
        ],
    )
    write(
        docs / "raw" / "README.md",
        [
            "# raw — les fichiers d'origine",
            "",
            "Le fichier tel qu'il est arrivé, jamais retouché. C'est le recours : quand une note",
            "se révèle fausse, on revient ici, et rien n'a bougé.",
            "",
            *([f"- [{p.name}]({p.name})" for p in content_files(docs / "raw")] or ["*Aucun fichier.*"]),
        ],
    )
    write(
        docs / "fulltext" / "README.md",
        [
            "# fulltext — les textes extraits",
            "",
            "Le texte d'une source dont le format n'était pas directement lisible. Un fichier ici",
            "est complet et sans mise en forme. Une extraction ratée porte un marqueur visible",
            "plutôt qu'un fichier vide — un fichier vide laisse croire qu'on a lu.",
            "",
            *([f"- [{p.name}]({p.name})" for p in content_files(docs / "fulltext")] or ["*Aucun texte extrait.*"]),
        ],
    )
    write(
        sessions / "README.md",
        [
            "# sessions — la parole de l'auteur",
            "",
            "Un fichier par jour, `SESSION-YYYY-MM-DD.md`. Le seul canal par lequel ce qui n'a",
            "jamais été écrit peut entrer. Le fichier ne fait que s'allonger.",
            "",
            *([f"- [{p.stem}]({p.name})" for p in session_files] or ["*Aucune session.*"]),
        ],
    )


# -------------------------------------------------------------------- autres blocs


def write_frame_readme(context: Path) -> None:
    write(
        context / "00-frame" / "README.md",
        [
            "# 00-frame — ce qui bouge peu",
            "",
            "Le cadre : ce que le contexte cherche, sous quelles règles, et ce qu'il faut charger.",
            "",
            "| Fichier | Contenu |",
            "|---|---|",
            "| [mission.md](mission.md) | le but, la question centrale, ce qui est dans et hors sujet |",
            "| [directives.md](directives.md) | les règles stables de ce contexte |",
            "| [loading.md](loading.md) | quoi charger à l'ouverture |",
        ],
    )


def write_state_readme(context: Path) -> None:
    write(
        context / "01-state" / "README.md",
        [
            "# 01-state — où on en est",
            "",
            "Ce qui bouge à chaque session.",
            "",
            "| Fichier | Contenu | Écrit par |",
            "|---|---|---|",
            "| [state.md](state.md) | ce qu'on sait, ce qui reste incertain, les dettes | `save` |",
            "| [checkpoints.md](checkpoints.md) | la suite des états figés, le plus récent en tête | `save` |",
            "| [synthesis.md](synthesis.md) | ce qui est devenu stable et ne bouge plus | `save` |",
            "| [todo.md](todo.md) | le reste-à-faire | mot-clé `todo :` |",
            "| [decisions.md](decisions.md) | ce qu'on a tranché sur le contexte lui-même | mot-clé `décision :` |",
            "| [contradictions.md](contradictions.md) | ce qui s'oppose et n'est pas tranché | mot-clé `contradiction :` |",
            "| [handoff.md](handoff.md) | comment reprendre sans tout relire | `save` |",
            "| [health.md](health.md) | verdict du dernier `check` | `check` |",
        ],
    )


def write_history_readme(context: Path) -> None:
    # Seuls les fichiers datés sont des journées.
    days = [p for p in content_files(context / "02-history", "*.md") if re.match(r"^\d{4}-\d{2}-\d{2}$", p.stem)]
    write(
        context / "02-history" / "README.md",
        [
            "# 02-history — le journal de séance",
            "",
            "Une journée par fichier : ce qu'on a visé, produit, appris, et ce qui reste",
            "incertain. Écrit en fin de séance par `save`, jamais réécrit ensuite. On ne le",
            "lit pas pour travailler : on le rouvre quand `01-state/` a raté quelque chose.",
            "Le format est dans `docs/history.md`.",
            "",
            *([f"- [{p.stem}]({p.name})" for p in reversed(days)] or ["*Aucune journée.*"]),
        ],
    )


def outputs_dir_label(folder: Path) -> str:
    """Ce qu'on sait d'un sous-dossier sans rien inventer : ce qu'il contient."""
    if folder.name == "_draft":
        return "ce qui n'est pas fini"
    files = len(content_files(folder, "*.md"))
    subs = len(iter_dirs(folder))
    parts = []
    if files:
        parts.append(f"{files} livrable" + ("s" if files > 1 else ""))
    if subs:
        parts.append(f"{subs} sous-dossier" + ("s" if subs > 1 else ""))
    return ", ".join(parts) or "vide"


def outputs_dir_table(folder: Path) -> list[str]:
    rows = [f"| [{d.name}/]({d.name}/README.md) | {outputs_dir_label(d)} |" for d in iter_dirs(folder)]
    return ["| | |", "|---|---|", *rows, ""] if rows else []


def write_outputs_subdir_readme(folder: Path, depth: int) -> None:
    """Un sous-dossier de 05-outputs, à n'importe quelle profondeur."""
    if folder.name == "_draft":
        lines = ["# _draft — ce qui n'est pas fini", "", "Un brouillon monte d'un niveau quand il est fini.", ""]
        empty = "*Aucun brouillon.*"
    else:
        lines = [f"# {folder.name}/ — un regroupement de livrables", ""]
        empty = "*Aucun livrable.*"
    lines += [
        f"Remonter : [05-outputs/]({'../' * depth}README.md)",
        "",
        *outputs_dir_table(folder),
        *([f"- [{p.name}]({p.name})" for p in content_files(folder)] or [empty]),
    ]
    write(folder / "README.md", lines)
    for sub in iter_dirs(folder):
        write_outputs_subdir_readme(sub, depth + 1)


def write_outputs_readme(context: Path) -> None:
    root = context / "05-outputs"
    write(
        root / "README.md",
        [
            "# 05-outputs — les livrables",
            "",
            "Le seul endroit où la mise en forme et l'orientation sont permises. Les livrables se",
            "rangent par **maturité** : un brouillon dans `_draft/`, un livrable fini ici.",
            "",
            "Un livrable fini vit à la racine, ou dans un sous-dossier qui le regroupe avec les",
            "autres pièces du même ouvrage. La profondeur est libre.",
            "",
            "**La finalité d'un livrable ne redéfinit jamais une note.** Rien d'ici ne remonte",
            "dans `04-notes/`.",
            "",
            *outputs_dir_table(root),
            *([f"- [{p.name}]({p.name})" for p in content_files(root)] or ["*Aucun livrable à la racine.*"]),
        ],
    )
    for sub in iter_dirs(root):
        write_outputs_subdir_readme(sub, 1)


def write_context_readme(context: Path) -> None:
    write(
        context / "README.md",
        [
            f"# {context.name}",
            "",
            context_goal(context),
            "",
            "## Par où commencer",
            "",
            "- [00-frame/](00-frame/README.md) — le but, les règles, ce qu'on charge à l'ouverture",
            "- [01-state/](01-state/README.md) — où on en est",
            "- [02-history/](02-history/README.md) — ce qui s'est passé, jour par jour",
            "- [03-sources/](03-sources/README.md) — la matière",
            "- [04-notes/](04-notes/README.md) — la connaissance",
            "- [05-outputs/](05-outputs/README.md) — les livrables",
            "",
            "## Reprendre le travail",
            "",
            "Lire [01-state/handoff.md](01-state/handoff.md). Il est réécrit à chaque `save`.",
        ],
    )


def refresh_context(context: Path) -> None:
    write_context_readme(context)
    write_frame_readme(context)
    write_state_readme(context)
    write_history_readme(context)
    write_sources_readme(context)
    write_notes_readme(context)
    write_outputs_readme(context)


def write_root_readmes() -> None:
    for root, heading, empty in (
        (CONTEXTS_ROOT, "Contextes actifs", "Aucun contexte actif."),
        (ARCHIVE_ROOT, "Contextes archivés", "Aucun contexte archivé."),
    ):
        root.mkdir(parents=True, exist_ok=True)
        rows = [f"- [{p.name}/]({p.name}/README.md) — {context_goal(p)}" for p in iter_dirs(root)]
        write(root / "README.md", [f"# {heading}", "", *(rows or [f"*{empty}*"])])


def refresh_all() -> None:
    for root in (CONTEXTS_ROOT, ARCHIVE_ROOT):
        for context in iter_dirs(root):
            refresh_context(context)
    write_root_readmes()


def main() -> None:
    parser = argparse.ArgumentParser(description="Régénérer les README de navigation.")
    parser.add_argument("context", nargs="?", help="Nom d'un contexte ; sinon tous.")
    args = parser.parse_args()

    if args.context:
        from _common import resolve_context

        refresh_context(resolve_context(args.context))
        write_root_readmes()
        print(f"README régénérés pour {args.context}")
    else:
        refresh_all()
        print("README régénérés pour tous les contextes")


if __name__ == "__main__":
    main()
