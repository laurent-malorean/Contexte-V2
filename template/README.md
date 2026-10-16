# Templates — un fichier par entité

Première itération. Chaque fichier est le gabarit d'une entité définie dans [entity.md](../docs/entity.md). Les commentaires HTML disent quoi mettre dans chaque section ; ils sont retirés à la création, sauf ceux qui portent une règle qu'on veut relire.

| Fichier | Entité | Où il atterrit |
|---|---|---|
| [source-document.md](source-document.md) | source documentaire | `03-sources/documents/` |
| [source-session.md](source-session.md) | source de session | `03-sources/sessions/SESSION-YYYY-MM-DD.md` |
| [note-atomic.md](note-atomic.md) | note atomique | `04-notes/atomic/ATO00001-…` |
| [note-thematic.md](note-thematic.md) | note thématique | `04-notes/thematic/THM00001-…` |
| [note-glossary.md](note-glossary.md) | entrée de glossaire | `04-notes/glossary/GLO00001-…` |
| [note-decision-record.md](note-decision-record.md) | decision record | `04-notes/decision-records/DRE00001-…` |

## La règle qui a produit ces frontmatter

**On ne stocke que ce qui n'est pas déductible d'ailleurs.** Un champ recopié peut un jour ne plus correspondre, sans que rien ne le signale.

Sont donc absents, volontairement :

| Champ | Pourquoi il n'y est pas |
|---|---|
| `type` | le dossier le dit — `04-notes/atomic/` ne contient que des atomiques |
| `title`, `term` | le titre `#` du fichier le porte |
| `confidence` | dans les contextes existants, il vaut `medium` partout : un champ qui ne varie jamais n'informe pas |
| `tags` | rien ne les lit ; les liens expliqués font le travail |

Deux exceptions **décidées**, contre la règle : `uuid` et `id` sont dans le frontmatter des quatre types de notes. `id` recopie ce que porte le nom du fichier, mais il rend une note citable et lisible sans dépendre du chemin ; `uuid` la rend identifiable même après un renommage. C'est une duplication assumée, pas un oubli.

Ce qui reste : l'identité, les dates, l'état, les liens de remplacement, et les sources.

## Ce qui est commun aux quatre notes

**`sources: []` est obligatoire, y compris quand la source est ta propre parole** — c'est à ça que sert `SESSION-YYYY-MM-DD`. Une note sans origine identifiable est une opinion, pas une connaissance. Aujourd'hui les deux systèmes divergent : `MINI` met les sources en frontmatter pour les thématiques et le glossaire, et dans le corps pour les atomiques. V2 unifie : frontmatter pour les quatre.

**`status` + `superseded_by`.** Une note n'est jamais supprimée : elle est remplacée, reste en place marquée comme telle, et pointe vers celle qui prend le relais — qui pointe en retour vers elle.

**Aucun template ne contient de section liée au livrable.** Ni « Utilité pour l'article », ni « Accroche », ni « Pour le client ». Le gabarit ne doit pas offrir la case qui fait déraper la note.

## La règle qui gouverne les sections du corps

**On garde toute section que les notes réelles remplissent.** Mesure sur les 313 notes atomiques, 21 thématiques et 4 entrées de glossaire des deux systèmes : aucune section du corps n'est morte. Les taux de remplissage sont de 93 % à 100 %, avec des médianes de 90 à 1 400 caractères.

Une première version de ces gabarits en avait retiré cinq au motif qu'elles seraient décoratives. La mesure a démenti : `Pourquoi c'est important` est remplie 313/313 avec une médiane de 300 caractères, `Questions ouvertes` dans 140 notes, `Rétroliens` dans 300, et les trois sections du glossaire supposées vides le sont 4/4. **La conviction qu'une section est inutile ne vaut rien contre le comptage.**

### Le cas de `## Validation atomique`

Sur 313 notes, **une seule** a une case décochée. Un test qui passe toujours ne teste rien — c'est ce qu'on lit dans l'artefact fini.

Mais la mesure porte sur le mauvais objet. Cette liste n'est pas un contrôle a posteriori, c'est une **contrainte de rédaction** : elle tient la main du rédacteur pendant qu'il écrit. Le taux de 312/313 est tout aussi compatible avec « elle ne sert à rien » qu'avec « elle est la raison pour laquelle ils passent ». L'avant/après a été observé : sans elle, la note dérive. C'est ce constat qui tranche, pas le comptage.

Ce qui reste vrai de la critique : l'unique case décochée n'est pas une note ratée, c'est **une entorse assumée et justifiée en bout de ligne**. Le gabarit le dit maintenant explicitement — une case décochée sans justification est un défaut, avec justification c'est une exception valide.

Une seule ligne a été retirée de la liste : **« aucun nom de personne »**. L'anonymisation dépend du contexte, pas de la note — une recherche bibliographique exige au contraire de citer nommément. Un contexte qui l'impose l'inscrit dans ses directives, et la ligne réapparaît.

## Ce qui reste retiré, et pourquoi

| Retiré | Venait de | Raison |
|---|---|---|
| `## Idées à stabiliser` dans la session | `02-CONTEXT` | contredit la règle « le brut reste brut » : stabiliser est le travail des notes, pas de la source |
| `## Résumé source` de la fiche source | `02-CONTEXT` | la fiche trace, elle ne résume pas — un résumé écrit à l'entrée est une sélection faite avant d'avoir lu |
| `related_terms` avec ses 4 sous-listes | `MINI` | c'est du frontmatter, pas une section ; `À ne pas confondre avec` fait le travail en redéfinissant chaque voisin au lieu de le lister |
| `## Sources` du glossaire | `MINI` | remonté en frontmatter `sources: []`, comme pour les trois autres types de notes |

Le decision record a subi la même correction : sa doctrine en prescrit **onze rubriques**, le premier gabarit n'en avait que sept. `## Hypothèses`, `## Raisons du choix`, `## Conséquences › Positives` et `## Sources et références` sont rétablies. Cette dernière est obligatoire et **strictement séparée** de `## Décisions liées`, qui ne contient que des liens vers d'autres records — c'est cette séparation qui permet de reconstituer le graphe des décisions.

## Tranché

- **`uuid` et `id` sont dans le frontmatter** des quatre types de notes (2026-09-08).
- **Les commentaires restent en français** pour l'instant (2026-09-08).
- **Le decision record garde ses deux dates** (2026-09-08) : `created` date l'écriture du fichier, `decided_on` date le moment où la décision a été prise. Un record naît en `proposed` un jour et devient `accepted` un autre, parfois des semaines plus tard. `updated` ne peut pas faire le travail : il bouge à chaque correction de forme.
- **`ingestion-log.md` est la vérité, la fiche source l'affiche.** Les deux disent ce qu'une source a produit : le journal par ingestion (une source peut être lue en deux fois), la fiche par source, cumulée. Le journal gagne parce qu'il est écrit par un script et porte l'empreinte ; la section `## Ce qu'elle a produit` de la fiche en est générée.
