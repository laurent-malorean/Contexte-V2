#!/usr/bin/env python3
"""Verse la boîte aux lettres du contexte dans la source de session du jour.

Une pensée notée loin de la machine n'est pas d'un autre genre : elle entre par la
même porte. Après absorption, `offline.md` reste présent et vide.
"""

from __future__ import annotations

import argparse
from datetime import date, datetime

from _common import resolve_context
from refresh_readmes import refresh_context
from session_append import AUTHOR, insert, session_file


def main() -> None:
    parser = argparse.ArgumentParser(description="Absorber offline.md dans la session du jour.")
    parser.add_argument("contexte")
    parser.add_argument("--date", default=date.today().isoformat())
    args = parser.parse_args()

    context = resolve_context(args.contexte)
    offline = context / "offline.md"
    offline.touch(exist_ok=True)

    content = "\n".join(
        line for line in offline.read_text(encoding="utf-8").splitlines() if not line.strip().startswith("<!--")
    ).strip()
    if not content:
        print("boîte aux lettres vide")
        return

    # Un dépôt hors session est de la parole de l'auteur : il va dans son bloc,
    # jamais à la fin du fichier ni dans celui des interventions de l'IA.
    path = session_file(context, args.date)
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    insert(path, AUTHOR, [f"**Déposé hors session — {stamp}**", "", content])

    offline.write_text("", encoding="utf-8")
    refresh_context(context)
    print(f"boîte absorbée dans {path.relative_to(context)} ({len(content.split())} mots)")
    print("à ranger : le dépôt est de la parole de session — le trier comme le reste")


if __name__ == "__main__":
    main()
