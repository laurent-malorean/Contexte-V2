---
name: C2_archive
description: Sortir un contexte des actifs, après avoir signalé ce qui reste ouvert.
---

# C2_archive

## But

Ranger un contexte dont on a fini, sans perdre ce qu'il contenait ni ce qu'il laissait en suspens.

## Procédure

1. Lancer `check` sur le contexte, et lire son verdict.
2. Lire `01-state/todo.md` et `01-state/contradictions.md`.
3. **Dire à l'utilisateur ce qui reste ouvert** : tâches non faites, contradictions non refermées, sources jamais ingérées, notes sans source. Puis demander confirmation explicite.
4. Sur accord, lancer `save` — pour que l'état figé au moment de l'archivage soit juste.
5. Déplacer le dossier de `contexts/` vers `_ARCHIVE/`.
6. Régénérer la navigation :
   ```bash
   .venv/bin/python scripts/refresh_readmes.py
   ```

## Règles

- **Ne jamais archiver sans confirmation.** C'est la seule commande qui déplace un dossier entier.
- **Ne jamais supprimer un contexte.** Archiver, c'est déplacer.
- Un contexte archivé garde ses README et reste lisible : `_ARCHIVE/README.md` le liste avec son but.
- Ne pas archiver pour « faire du rangement ». Un contexte dont on ne se sert plus mais dont les notes servent ailleurs reste actif.

## Sortie attendue

Ce qui a été déplacé, et la liste de ce qui restait ouvert au moment de l'archivage.
