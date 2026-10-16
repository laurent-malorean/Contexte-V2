---
name: C2_open
description: Ouvrir un contexte V2 — absorber la boîte aux lettres, charger l'état, dire la prochaine action.
---

# C2_open

## But

Reprendre le travail sans rien avoir perdu de ce qui a été déposé entre-temps, et sans charger le contexte entier pour rien.

## Procédure

1. **Si aucun contexte n'est nommé**, lire `contexts/README.md` et proposer la liste. S'arrêter là.
2. **Absorber la boîte aux lettres** — toujours, et avant toute autre lecture :
   ```bash
   .venv/bin/python scripts/offline_absorb.py "<nom>"
   ```
   Si elle contenait quelque chose, le traiter comme un propos de session : trier ce qui relève d'un `todo :`, d'une `décision :`, d'une contradiction, et le ranger.
3. Lire `00-frame/loading.md`, puis charger exactement ce qu'il liste sous « Toujours ». Rien de plus.
4. Lire le premier bloc de `01-state/checkpoints.md` et `01-state/handoff.md`.
5. **Ouvrir le journal du jour.** La commande crée le fichier au besoin et pose le repère qui dit à la passe quel contexte est ouvert — sans ce repère, rien ne se journalise :
   ```bash
   .venv/bin/python scripts/history_log.py open "<nom>"
   ```
6. Signaler ce qui bloque : un fichier de `01-state/` resté vide, une source en `extraction: failed`, un verdict `check` non traité.

## Règles

- **Ne pas charger** `03-sources/` ni `04-notes/` par défaut. On les lit à la demande.
- Ne pas résumer tout le contexte : l'utilisateur veut savoir où il en est, pas relire son travail.
- Le routage de la parole (voir `SYSTEM.md`) devient actif à partir de maintenant.

## Sortie attendue

Quatre lignes au plus :

- le contexte ouvert et son but ;
- où on en est ;
- ce qui a été absorbé de la boîte aux lettres, s'il y avait quelque chose ;
- **la prochaine action**, une seule, immédiatement exécutable.
