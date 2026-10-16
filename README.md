# Système de contextes V2

Un contexte est un dossier borné par une mission, où de la matière devient de la connaissance, puis un livrable. Ce système en crée, en alimente et en vérifie.

Il est **autonome** : rien ici ne pointe hors de ce dossier. On peut le déplacer ou le copier, il tourne.

## Installer

Prérequis : Python 3.9 ou plus, et Claude Code ou Codex.

Depuis ce dossier :

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
chmod +x .claude/hooks/history-log.sh
```

## Démarrer

Ouvrir **ce dossier** comme dossier de travail, puis :

- dans Claude Code : `/C2_new` ;
- dans Codex : écrire `new`.

## Les commandes

| | |
|---|---|
| `C2_new` | créer un contexte |
| `C2_open` | l'ouvrir : absorber la boîte aux lettres, charger l'état, dire la prochaine action |
| `C2_source` | ajouter une source documentaire et figer son texte |
| `C2_session` | verser un bloc de connaissance, ou relire ce qui a été capté aujourd'hui |
| `C2_ingest` | lire les sources non traitées et en tirer des notes |
| `C2_save` | consolider : état, synthèse, reprise, checkpoint, rattrapage |
| `C2_check` | auditer et rendre un verdict |
| `C2_archive` | sortir un contexte des actifs |

Les procédures sont dans [skills/](skills/), écrites une seule fois et lues par les deux hôtes. Huit commandes, pas trente : chacune couvre une étape du cycle de vie, et ce qui n'a pas besoin de déclencheur n'en a pas.

## Ce qui se passe sans commande

Quand un contexte est ouvert, la parole est routée automatiquement : une matière va dans les sources, un propos conceptuel dans la source de session du jour, du pilotage nulle part. Six mots-clés — `décision :`, `decision record :`, `contradiction :`, `todo :`, `directive :`, `session :` — forcent une destination, **à condition d'être le premier mot du message**.

Tout est dans [SYSTEM.md](SYSTEM.md), le seul fichier chargé en permanence.

## Les dossiers

| | |
|---|---|
| [contexts/](contexts/README.md) | les contextes actifs |
| [_ARCHIVE/](_ARCHIVE/README.md) | ceux qu'on a rangés |
| [skills/](skills/) | les 7 procédures |
| [scripts/](scripts/) | ce qui est tenu par du code, pas par de la prose |
| [template/](template/README.md) | un gabarit par entité |
| [skeleton/](skeleton/README.md) | le contexte vide, copié à chaque création |
| [docs/](docs/) | pourquoi le système est fait comme ça |

## Le partage entre le code et le jugement

> **Le script ne décide jamais d'un contenu. Le LLM n'écrit jamais un identifiant, un chemin, ni un champ de frontmatter.**

Créer un contexte, calculer un identifiant, régénérer un README, extraire le texte d'un PDF, vérifier un lien : déterministe, donc tenu par un script. Décider qu'une idée mérite une note, trancher entre atomique et glossaire, écrire une synthèse : du jugement, donc laissé au LLM — avec les garde-fous écrits dans le skill.

C'est le résultat de la comparaison des deux systèmes précédents : **une règle qui n'est pas déclenchée par une commande n'est pas suivie**, et une information écrite à deux endroits finit par diverger.

## Les deux hôtes

`AGENTS.md` et `CLAUDE.md` contiennent la même ligne : `@SYSTEM.md`. Codex lit le premier, Claude Code le second, et la règle n'existe qu'à un seul endroit. Les huit fichiers de `.claude/commands/` ne servent qu'à obtenir l'autocomplétion des slash commands.

Côté Codex comme côté Claude Code, lancer la session avec ce dossier comme dossier de travail.
