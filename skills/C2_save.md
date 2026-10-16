---
name: C2_save
description: Consolider le contexte — état, synthèse, reprise, checkpoint, et rattrapage de ce qui n'a pas été rangé.
---

# C2_save

## But

Persister ce qui doit l'être. **C'est la seule commande de consolidation**, et elle se lance quand on veut : fenêtre pleine, changement de machine, interruption, fin de journée. Il n'y a pas de commande de fermeture — c'est `open` qui ouvre la session suivante, donc la précédente se termine d'elle-même.

**`save` doit prendre trente secondes.** Si elle coûte cher, elle ne sera pas lancée au moment où on est pressé — c'est-à-dire au moment où elle sert le plus.

## Procédure

1. **Rattraper ce qui n'a pas été rangé.** Relire la session depuis son début et chercher les messages de l'utilisateur commençant par un mot-clé (`décision :`, `todo :`, `contradiction :`, `directive :`, `decision record :`, `session :`). Pour chacun, vérifier que l'écriture a bien eu lieu. Écrire ce qui manque. C'est le filet : rien d'autre ne garantit qu'un mot-clé a été appliqué.
2. Vérifier de même que les propos conceptuels de la session sont dans `03-sources/sessions/SESSION-<date>.md`. Ajouter les manquants :
   ```bash
   .venv/bin/python scripts/session_append.py "<contexte>" --auteur "…"
   ```
3. Mettre à jour `01-state/state.md` : ce qu'on sait, ce qui reste incertain, les dettes. Une cinquantaine de lignes au plus.
4. Promouvoir vers `01-state/synthesis.md` ce qui a cessé d'être discuté. La synthèse ne fait que croître ; l'état se réécrit.
5. Réécrire entièrement `01-state/handoff.md` : où on en est, ce qu'il faut savoir avant de continuer, **une** prochaine action, ce qui reste ouvert.
6. Ajouter un bloc en tête de `01-state/checkpoints.md` — **seulement si quelque chose a changé** depuis le précédent (mêmes compteurs et même prochaine action ⇒ pas de bloc) :
   ```
   ## AAAA-MM-JJ HH:MM
   - sources : 12 (dont 3 non ingérées) · notes : 47 (ATO 38 · THM 4 · GLO 3 · DRE 2) · livrables : 1
   - prochaine action : …
   ```
   Un bloc posé n'est jamais retouché.
7. **Rattraper le journal.** La passe tourne à chaque tour par hook, mais rien ne signale qu'un hook n'a pas tourné. Relancer sur toute la séance — c'est idempotent, donc sans risque de doublon :
   ```bash
   .venv/bin/python scripts/history_log.py catchup --full
   ```
8. Régénérer la navigation :
   ```bash
   .venv/bin/python scripts/refresh_readmes.py "<contexte>"
   ```
9. Si le dépôt est sous git, proposer un commit. Ne pas commiter sans accord, et ne rien faire de plus si le contexte n'est pas versionné : **un contexte n'est pas forcément sous git.**

## Règles

- `handoff.md` n'a qu'un seul auteur : `save`. Personne d'autre n'y écrit, sinon il devient un brouillon de plus.
- Le checkpoint n'est pas une copie de `state.md` : seulement les compteurs et la prochaine action.
- `02-history/` ne se réécrit jamais. On y ajoute — et **jamais à la main** : c'est la passe qui l'écrit. Voir [docs/history.md](../docs/history.md).
- Ne pas cocher une tâche qui a seulement été discutée.

## Sortie attendue

Trois lignes : ce qui a été persisté, ce qui a été rattrapé, ce qui reste ouvert.
