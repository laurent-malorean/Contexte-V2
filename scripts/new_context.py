#!/usr/bin/env python3
"""Crée un contexte en copiant le squelette.

On copie un vrai dossier, on ne reproduit jamais une structure d'après un texte.
C'est ce qui garantit que deux contextes créés à six mois d'écart sont identiques.
"""

from __future__ import annotations

import argparse
import shutil

from _common import CONTEXTS_ROOT, SKELETON_ROOT, slugify
from refresh_readmes import refresh_context, write_root_readmes


def main() -> None:
    parser = argparse.ArgumentParser(description="Créer un contexte V2.")
    parser.add_argument("nom", help="Nom du contexte, par exemple 2609-test")
    parser.add_argument("--but", default="", help="Le but, en une phrase")
    args = parser.parse_args()

    name = slugify(args.nom, max_words=8)
    target = CONTEXTS_ROOT / name
    if target.exists():
        raise SystemExit(f"Le contexte existe déjà : {target.relative_to(CONTEXTS_ROOT.parent)}")
    if not SKELETON_ROOT.exists():
        raise SystemExit("Squelette introuvable : skeleton/")

    CONTEXTS_ROOT.mkdir(parents=True, exist_ok=True)
    shutil.copytree(SKELETON_ROOT, target, ignore=shutil.ignore_patterns(".DS_Store"))

    if args.but:
        mission = target / "00-frame" / "mission.md"
        text = mission.read_text(encoding="utf-8")
        marker = "## Le but\n\n"
        head, sep, tail = text.partition(marker)
        if sep:
            mission.write_text(f"{head}{marker}{args.but.strip()}\n\n{tail}", encoding="utf-8")

    refresh_context(target)
    write_root_readmes()

    files = sum(1 for p in target.rglob("*") if p.is_file())
    print(f"contexte créé : contexts/{name} ({files} fichiers)")
    print("prochaine étape : compléter 00-frame/mission.md")


if __name__ == "__main__":
    main()
