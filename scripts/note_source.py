#!/usr/bin/env python3
"""Ajoute une source à une note existante — le geste de l'accrétion.

Une note atomique grandit au fil de sources hétérogènes : une première fait apparaître
l'idée, une deuxième la confirme, une troisième la nuance. Le corps se densifie, et le
frontmatter doit suivre — sinon la note affiche une seule origine alors qu'elle en a
plusieurs, et personne ne peut plus répondre à « cette source a-t-elle servi ? ».

Le LLM n'écrit jamais un champ de frontmatter : il donne un identifiant de note et un
identifiant de source, le script écrit. `updated` passe au jour de l'accrétion, parce
qu'une note qui se densifie a changé.

  note_source.py <contexte> ATO00042 --add-source SRC00003
  note_source.py <contexte> THM00006 --add-source SRC00003,SESSION-2026-08-07
"""

from __future__ import annotations

import argparse
import re
from datetime import date

from _common import NOTE_KINDS, resolve_context
from refresh_readmes import refresh_context


def main() -> None:
    parser = argparse.ArgumentParser(description="Ajouter une source à une note existante.")
    parser.add_argument("contexte")
    parser.add_argument("note", help="Identifiant de la note, par exemple ATO00042")
    parser.add_argument("--add-source", required=True, help="Identifiants séparés par des virgules")
    args = parser.parse_args()

    context = resolve_context(args.contexte)
    ident = args.note.strip().upper()

    folders = [context / "04-notes" / folder for _prefix, folder, *_rest in NOTE_KINDS.values()]
    matches = [p for folder in folders for p in folder.glob(f"{ident}-*.md")]
    if len(matches) != 1:
        raise SystemExit(f"{ident} : {len(matches)} note(s) trouvée(s)")
    path = matches[0]

    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        raise SystemExit(f"{path.name} : pas de frontmatter")
    end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")

    index = next((i for i in range(1, end) if lines[i].startswith("sources:")), None)
    if index is None:
        raise SystemExit(f"{path.name} : pas de champ sources")

    raw = lines[index].split(":", 1)[1].strip().strip("[]")
    current = [s.strip() for s in raw.split(",") if s.strip()]

    added = []
    for source in (s.strip() for s in args.add_source.split(",") if s.strip()):
        if source in current:
            print(f"déjà présente : {source}")
            continue
        current.append(source)
        added.append(source)

    if not added:
        return

    lines[index] = "sources: [" + ", ".join(current) + "]"
    for i in range(1, end):
        if lines[i].startswith("updated:"):
            lines[i] = f"updated: {date.today().isoformat()}"

    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    refresh_context(context)
    print(f"{ident} — source(s) ajoutée(s) : {', '.join(added)} ({len(current)} au total)")


if __name__ == "__main__":
    main()
