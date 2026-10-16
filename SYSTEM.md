# Système de contextes V2

Ce fichier ne contient que ce qui doit s'appliquer **sans commande**. Tout le reste se charge à la demande.

## Les commandes

Quand l'utilisateur écrit le nom d'une commande — avec ou sans le préfixe `C2_`, avec ou sans `/` — charger et suivre `skills/C2_<nom>.md`.

`C2_new` · `C2_open` · `C2_source` · `C2_session` · `C2_ingest` · `C2_save` · `C2_check` · `C2_archive`

## Le routage de la parole

**Actif seulement quand un contexte est ouvert.** Hors contexte ouvert, ce fichier n'a aucun effet.

### Les mots-clés

Un mot-clé n'est actif que s'il est le **premier mot du message**. Écrit au milieu d'une phrase, il ne déclenche rien.

| Mot-clé | Destination |
|---|---|
| `décision : …` | `01-state/decisions.md` — une décision **sur le contexte** : comment on le range, ce qu'on charge, quelle règle on adopte |
| `decision record : …` | `04-notes/decision-records/` — un arbitrage **sur le sujet** du contexte |
| `contradiction : …` | `01-state/contradictions.md` |
| `todo : …` | `01-state/todo.md` |
| `directive : …` | `00-frame/directives.md` |
| `session : …` | force l'écriture dans la source de session du jour |

Un mot-clé agit **tout de suite**, en plus de la réponse normale. Annoncer en une ligne ce qui a été enregistré et où. Si le propos est ambigu (« décision : on verra »), demander avant d'écrire.

`decision record :` est le seul mot-clé qui pose des questions avant d'écrire : contre quoi on a tranché, ce qu'on accepte de perdre, sur quoi on s'appuie.

### Sans mot-clé

Chaque propos de l'auteur va dans l'un de trois endroits :

| Ce qu'il dit | Où ça va |
|---|---|
| il donne ou pointe une matière (lien, fichier, extrait) | `03-sources/` — proposer `source` |
| il affirme, suppose, définit, tranche ou constate une tension **sur le sujet** | `03-sources/sessions/SESSION-YYYY-MM-DD.md` |
| il pilote (« fais ça », « supprime », « tu en es où ? ») | nulle part — non conservé |

En cas de doute entre les deux derniers, **ne pas conserver**.

### La source de session

Un fichier par jour et par contexte. On ajoute à la fin, on ne corrige jamais ce qui est écrit. Deux sections, jamais mélangées :

- `## Propos de l'auteur` — ce qu'il a dit, transcrit fidèlement, désordre admis. Un propos rapporté (« un client dit que… ») est signalé comme tel.
- `## Interventions de l'IA nécessaires à la compréhension` — seulement quand la réponse de l'auteur ne se comprend pas sans la question, la reformulation ou le choix proposé.

Le fichier doit rester compréhensible **hors du fil de conversation**.

Écriture : `.venv/bin/python scripts/session_append.py <contexte> --auteur "…"` ou `--ia "…"`.

### Le journal du contexte

`02-history/` **ne s'écrit pas en séance**. Une passe automatique relit la transcription à chaque fin de tour et range sous sa rubrique ce que le tour a établi — connaissances, ce qui est acté, ce qu'on écarte, ce qu'on révise, problèmes, à suivre, dérive. Ne jamais y écrire à la main : `save` relance la passe et rattrape ce qu'un hook absent aurait laissé passer. Voir `docs/history.md`.

## Où sont les choses

| | |
|---|---|
| les contextes | `contexts/<nom>/` |
| les procédures | `skills/C2_<nom>.md` |
| les scripts | `.venv/bin/python scripts/<nom>.py` |
| les prompts des scripts | `prompts/<nom>.md` — le texte envoyé aux modèles, hors du code |
| les gabarits | `template/` — jamais recopiés à la main, c'est `new_note.py` qui les pose |

Les sources et les notes d'un contexte ne se chargent jamais par défaut : seulement quand la tâche les demande.

## Deux règles qui ne se négocient pas

- **Le script ne décide jamais d'un contenu. Le LLM n'écrit jamais un identifiant, un chemin, ni un champ de frontmatter.**
- **Les README sont générés.** Ne jamais en écrire un à la main.
