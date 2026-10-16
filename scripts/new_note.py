#!/usr/bin/env python3
"""Crée le fichier d'une note à partir de son gabarit.

Le LLM ne choisit pas l'identifiant, ne tape pas le chemin et ne recopie pas le
gabarit : il donne un type, un titre et des sources. Le reste est calculé.
"""

from __future__ import annotations

import argparse
import re
import uuid as uuid_module
from datetime import date

from _common import NOTE_KINDS, TEMPLATE_ROOT, next_id, resolve_context, slugify


def fill_frontmatter(text: str, values: dict[str, str]) -> str:
    """Remplace les valeurs du frontmatter du gabarit, sans toucher au corps."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise SystemExit("Gabarit sans frontmatter.")
    end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    for i in range(1, end):
        key = lines[i].split(":", 1)[0].strip()
        if key in values:
            lines[i] = f"{key}: {values[key]}"
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Créer une note dans un contexte V2.")
    parser.add_argument("contexte")
    parser.add_argument("type", choices=sorted(NOTE_KINDS))
    parser.add_argument("titre", help="Le titre de la note, tel qu'il apparaîtra en tête")
    parser.add_argument("--sources", default="", help="Identifiants séparés par des virgules")
    parser.add_argument("--created", default="", help="Date de création, si la note vient d'ailleurs")
    parser.add_argument("--updated", default="", help="Date de dernière modification, si elle vient d'ailleurs")
    args = parser.parse_args()

    context = resolve_context(args.contexte)
    prefix, folder_name, template_name, *_rest = NOTE_KINDS[args.type]
    folder = context / "04-notes" / folder_name
    folder.mkdir(parents=True, exist_ok=True)

    ident = next_id(folder, prefix)
    path = folder / f"{ident}-{slugify(args.titre)}.md"
    if path.exists():
        raise SystemExit(f"Existe déjà : {path.name}")

    template = (TEMPLATE_ROOT / template_name).read_text(encoding="utf-8")
    today = date.today().isoformat()
    sources = [s.strip() for s in args.sources.split(",") if s.strip()]
    text = fill_frontmatter(
        template,
        {
            "uuid": str(uuid_module.uuid4()),
            "id": ident,
            "created": args.created or today,
            "updated": args.updated or args.created or today,
            "sources": "[" + ", ".join(sources) + "]",
        },
    )

    # Le titre du gabarit est un exemple : on le remplace par le vrai.
    text = re.sub(r"^# .*$", f"# {args.titre.strip()}", text, count=1, flags=re.M)
    path.write_text(text, encoding="utf-8")

    if not sources:
        print("ATTENTION : note sans source. Une note sans origine est une opinion.")
    print(f"{ident} créé : {path.relative_to(context)}")
    print(f"chemin complet : {path}")


if __name__ == "__main__":
    main()
