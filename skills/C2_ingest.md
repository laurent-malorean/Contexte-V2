---
name: C2_ingest
description: Lire les sources non traitées d'un contexte et en tirer des notes sourcées.
---

# C2_ingest

## But

Transformer de la matière en connaissance. C'est le seul skill où presque tout est du jugement : le script ne fait que créer les fichiers et tenir le journal.

**Avant de commencer, lire `docs/entity.md`** — les définitions des quatre types de notes, leurs critères, leurs tests et leurs garde-fous. Sans ça, on produit des notes qui ont l'air correctes.

Les deux types de sources ne s'ingèrent pas de la même façon. Un document arrive fini et se lit une fois ; une source de session grossit pendant qu'on travaille, et **elle peut répondre**.

## Commun aux deux

1. Lire `00-frame/mission.md` et `00-frame/directives.md`. Une idée ne se juge utile que par rapport à un but.
2. Lire `03-sources/README.md` : il indique, pour chaque source, si elle a été ingérée et ce qu'elle a produit.
3. Lire les notes déjà présentes — `04-notes/*/README.md` suffit : les titres sont des propositions, ils disent ce que le contexte sait déjà.
4. Créer chaque note par le script, jamais à la main :
   ```bash
   .venv/bin/python scripts/new_note.py "<contexte>" \
       atomic|thematic|glossary|decision-record "<titre>" --sources <SRC00001|SESSION-AAAA-MM-JJ>
   ```
   Puis remplir le corps du fichier créé — **en éditant le fichier directement, jamais par la ligne de commande.** Un corps de note fait plusieurs paragraphes : le faire passer par un shell casse sur les guillemets et les accents, et pousse à écrire un script jetable qui ne sert qu'à contourner le problème. Le fichier existe, il s'ouvre et s'écrit.
5. **Enrichir une note existante plutôt que la dupliquer** quand la source confirme, nuance ou limite une idée déjà là. Le corps se densifie à la main ; la source s'ajoute au frontmatter par le script :
   ```bash
   .venv/bin/python scripts/note_source.py "<contexte>" \
       ATO00042 --add-source SRC00003
   ```
   Sans ça, la note affiche une seule origine alors qu'elle en a plusieurs. Datez l'ajout dans le corps : on doit voir quelle couche vient de quelle source.
6. Poser les liens : chacun explique la relation, et **dans les deux sens**.

---

## Ingérer un document

1. **Refuser une source en `extraction: failed`.** Le signaler et passer à la suivante.
2. Lire le texte intégral dans `03-sources/documents/fulltext/`. Pas la fiche : la fiche trace, elle ne contient pas la matière, et son bloc d'interprétation est **exclu de l'analyse**.
3. Lire **en entier**. Pour une source longue, tenir la trace des zones parcourues : une zone sans note et sans justification n'est pas une zone stérile, c'est un trou.
4. Marquer l'ingestion :
   ```bash
   .venv/bin/python scripts/source_add.py "<contexte>" \
       --mark-ingested SRC00001 --status complete --notes ATO00012,GLO00003
   ```
   `partial` si tout n'a pas été lu, `needs-review` en cas de doute.

---

## Ingérer une source de session

Elle n'a ni conversion ni texte intégral séparé : le fichier **est** la matière.

1. Ne lire que ce qui reste après le repère :
   ```bash
   .venv/bin/python scripts/session_append.py "<contexte>" --a-lire
   ```
   Ce qui est avant le repère a déjà été traité et ne se relit pas. Le fichier ne fait que s'allonger : rien ne bouge derrière le repère.
2. **Enrichir avant de créer.** C'est ici que la règle compte le plus. La même idée revient d'un jour à l'autre, chaque fois un peu plus nette. Dire trois fois la même chose avec trois nuances n'est pas un problème : c'est comme ça qu'une idée mûrit. Le rôle de l'ingestion n'est pas de produire trois notes, mais d'accréter les nuances dans une connaissance plus fine. **Logique de maturation, pas d'archivage.**
3. **Tenir compte de qui parle.** Un propos signalé comme rapporté (« un client dit que… ») n'a pas la fiabilité d'une affirmation de l'auteur : la note doit le dire. Un propos tiré du bloc `## Interventions de l'IA` n'est pas la parole de l'auteur : il ne fonde jamais une note à lui seul.
4. **Quand l'auteur se contredit**, trois cas — et le premier n'existe que pour cette source :

   | Ce qui s'est passé | Ce qu'on fait |
   |---|---|
   | il se reformule — il avait mal dit | affiner la note existante |
   | il change d'avis | la nouvelle note remplace l'ancienne, qui reste marquée `superseded` |
   | les deux propos tiennent | ouvrir une contradiction, et une note si la tension elle-même est réutilisable |

   **Pendant la session, on demande.** C'est la seule source qui répond : un PDF ne peut pas préciser ce qu'il a voulu dire. **Hors session**, en ingérant des jours plus tard, on ne tranche pas : on ouvre une contradiction. C'est le seul choix qui ne détruit rien.
5. Un arbitrage tranché par l'auteur sur le sujet du contexte devient un `decision-record`, pas une note atomique.
6. Marquer l'ingestion, puis reposer le repère :
   ```bash
   .venv/bin/python scripts/source_add.py "<contexte>" \
       --mark-ingested SESSION-AAAA-MM-JJ --status complete --notes ATO00014
   .venv/bin/python scripts/session_append.py "<contexte>" --lu-jusquici
   ```
   **Ne pas reposer le repère si l'ingestion est `partial`** : ce qui n'a pas été traité serait perdu.

Une source de session d'un jour passé reste ingérable : elle est fermée à l'écriture, pas à la lecture. Fermer n'interdit que d'ajouter.

---

## Règles

- **Le titre est une proposition, pas une étiquette.** `Atomicité` classe la note ; `L'atomicité sert la réutilisation plus que la concision` la pense.
- **Un mot → glossaire. Une proposition → note atomique.** La première note pense, la seconde définit.
- **Peut-on résumer la matière en une phrase sans perdre l'essentiel ?** Oui → atomique. Non → thématique, et les idées qu'elle assemble deviennent des atomiques.
- **Aucune note sans source.** Y compris quand la source est la parole de l'auteur : c'est à ça que sert `SESSION-…`.
- **Pas de quota.** On s'arrête quand la source ne contient plus d'idée de qualité — ce qui peut faire une note, ou trente.
- **Deux motifs ne sont jamais recevables** pour écarter un passage : « c'est méthodologique » et « c'est déjà couvert ailleurs ». Le premier écarte précisément ce qui est le plus réutilisable ; le second remplace une vérification par une impression — si l'idée est déjà là, la règle est l'accrétion, pas l'omission.
- **On ne fusionne jamais deux notes automatiquement.** Scinder est sûr et réversible, fusionner ne l'est pas.
- **La finalité du livrable ne redéfinit jamais la note.** Ni accroche, ni angle de pitch, ni punchline.

## Sortie attendue

Pour chaque source traitée : ce qu'elle a produit, **ce qui a été enrichi plutôt que créé**, les contradictions ouvertes, et les zones qui n'ont rien donné avec leur raison.
