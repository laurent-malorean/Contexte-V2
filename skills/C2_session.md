---
name: C2_session
description: Verser un bloc de connaissance dans la source de session du jour, ou relire ce qui a été capté.
---

# C2_session

## But

La parole est déjà versée à chaque message par le routage de `SYSTEM.md`. Cette commande sert aux trois choses que le routage ne fait pas :

- **verser un bloc épais** délibérément — « voilà ce que j'ai compris après des années sur ce sujet », puis les exemples, les exceptions, les limites ;
- **relire ce qui a été capté aujourd'hui**, pour corriger ce qui a été mal trié ;
- **vérifier qu'il ne manque rien** avant d'ingérer.

## Procédure

### Verser un bloc

1. Laisser l'utilisateur dérouler. Ne pas l'interrompre pour ranger.
2. Écrire, un propos par appel :
   ```bash
   .venv/bin/python scripts/session_append.py "<contexte>" --auteur "…"
   ```
3. Si une question posée est nécessaire pour comprendre la réponse, l'écrire aussi :
   ```bash
   .venv/bin/python scripts/session_append.py "<contexte>" --ia "…"
   ```

### Relire

Lire `03-sources/sessions/SESSION-<date>.md` et le restituer tel quel. Demander ce qui manque, ce qui a été mal trié, ce qui n'aurait pas dû être conservé. Corriger dans le fichier, **sans réécrire ce qui est juste**.

### Voir ce qui reste à ingérer

```bash
.venv/bin/python scripts/session_append.py "<contexte>" --a-lire
```

## Règles

- **Le brut reste brut.** On transcrit, on n'interprète pas. Aucune idée n'est stabilisée ici — c'est le travail des notes.
- **Le fichier doit rester compréhensible hors du fil de conversation.** Dans six mois, on le lira sans avoir la discussion sous les yeux.
- **Un propos rapporté est signalé comme tel.** « Un client dit que… » n'a pas la même valeur que ce que l'auteur affirme lui-même, et la note qui en naîtra en hériterait.
- **Deux blocs, jamais mélangés** : les propos de l'auteur, et les interventions de l'IA sans lesquelles ils ne se comprendraient pas. Des mois après, on doit pouvoir dire qui a pensé quoi.
- **On ne verse pas le pilotage** : une commande, une question à l'assistant, du méta-discours ne sont pas de la matière. En cas de doute, ne pas conserver.
- **On ajoute à la fin, on ne réécrit jamais** ce qui est déjà écrit. Une correction se fait par un ajout qui dit ce qui a changé.
- Le désordre est admis : la fonction n'est pas d'être élégant, c'est de ne rien perdre.

## Sortie attendue

Ce qui a été écrit et où. En mode relecture : le contenu du jour, et la question « qu'est-ce qui manque ou a été mal rangé ? ».
