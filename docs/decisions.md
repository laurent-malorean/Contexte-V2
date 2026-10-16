# Décisions — système de contexte V2

Les décisions dont on risque d'oublier la raison. Une décision déjà expliquée dans [skills.md](skills.md), [keyword.md](keyword.md) ou [skeleton.md](skeleton.md) n'est pas répétée ici.

---

## DEC0001 — Le checkpoint reste, mais comme bloc dans une série, pas comme fichier daté

- **Décision** : V2 conserve l'état figé à un instant. Ce n'est plus un fichier par jour dans un dossier dédié, mais **un bloc de trois lignes ajouté en tête de `01-state/checkpoints.md`** — les compteurs et la prochaine action. Écrit par `save`, seulement si quelque chose a changé, et jamais retouché ensuite.
- **Pourquoi garder l'état figé** : sans lui, il n'existe aucun moyen de savoir dans quel état était le contexte à une date passée. La trace donne les événements, mais reconstituer « 28 sources, 60 notes, 13 facettes » à partir d'une liste d'événements est long et faux.
- **Pourquoi pas un fichier par jour** : on ne lit jamais un état figé tout seul, **on parcourt la série**. « Où j'en étais quand j'ai décidé ça ? » demande d'en comparer plusieurs. Éparpillés dans des fichiers datés, ils ne se parcourent pas. Dans un seul fichier, le plus récent en tête, un an de travail se lit d'un coup.
- **Pourquoi pas dans la trace du jour** : deux buts différents dans un même fichier obligent à traverser des dizaines de lignes d'événements pour lire trois lignes d'état.
- **Ce que ça ne suppose pas** : que le contexte soit versionné. **Un contexte n'est pas forcément sous git.** Quand git est là, il donne en plus l'état exact d'un fichier à une date, et c'est confortable — mais aucune règle du système ne doit en dépendre.
- **Ce n'est pas une copie de `state.md`** : `state.md` fait une cinquantaine de lignes — ce qu'on sait, ce qui reste incertain, les dettes. Le bloc figé n'en garde que les compteurs et la prochaine action. Rien à synchroniser.
- **Ce que ça remplace** : le dossier `02_checkpoints/` de `02-CONTEXT` — un fichier daté par jour, réécrit à chaque point d'étape, qui cohabitait avec un journal faisant la moitié du même travail.
- **Date** : 2026-09-08.

## DEC0002 — Le contexte doit être simple à utiliser, pour les humains autant que pour les IA

- **Décision** : à chaque arbitrage, on choisit ce qui rend le contexte le plus simple à utiliser — **pour les deux à la fois**. Ni un système lisible par une machine que personne n'ouvre, ni un dossier agréable à parcourir qu'une IA ne sait pas exploiter.
- **Pourquoi** : c'est le critère qui tranche quand deux solutions se valent techniquement. Il sert à arbitrer tout le reste.
- **Date** : 2026-09-08.

## DEC0003 — Les sources sont rangées à plat, et c'est la liste générée qui les groupe

- **Décision** : `03-sources/` ne contient pas de dossiers par intention. Toutes les sources sont au même niveau. L'intention (recherche, entretien, veille…) est écrite dans la fiche de chaque source, et `03-sources/README.md`, qui est régénéré, groupe les sources par intention pour la lecture.
- **Pourquoi** : ranger par intention oblige à classer une source avant de l'avoir lue, et le classement se fige — `02-CONTEXT` propose quatre dossiers typés, son plus gros contexte en utilise un seul pour ses 29 sources. Une intention écrite dans une fiche se corrige ; un nom de dossier ne se corrige qu'en déplaçant des fichiers.
- **Ce que ça préserve** : la lisibilité pour un humain, qui était le vrai besoin. Elle est rendue par la liste générée, pas par l'arborescence — donc sans coûter un classement à l'entrée (DEC0002).
- **Date** : 2026-09-08.

## DEC0004 — Chaque répertoire a un `README.md`, et les README se chaînent

- **Décision** : tout répertoire du contexte contient un `README.md` à jour. Si un répertoire A contient un répertoire B, le README de A porte une ligne qui pointe vers `B/README.md`. On peut donc parcourir tout le contexte de proche en proche, sans jamais ouvrir l'arborescence.
- **Pourquoi** : pour la navigation d'un humain. Un dossier de fichiers ne se lit pas ; une page qui dit ce qu'il y a dedans et par où continuer, si.
- **La condition qui la rend vraie** : ces README sont **générés**, jamais écrits à la main. La règle existe déjà dans les deux systèmes actuels — `02-CONTEXT` la prescrit en toutes lettres, `MINI` la fait exécuter par un script. Chez `02-CONTEXT` les README ont dérivé, chez `MINI` non. La règle ne vaut rien sans le générateur.
- **Date** : 2026-09-08.

## DEC0005 — Le système est 100 % portable : aucune dépendance hors du `.venv`

- **Décision** : tout ce dont le système a besoin s'installe avec `pip` dans le `.venv` du projet. Un `git clone` suivi d'un `pip install -r requirements.txt` suffit à le faire tourner. Aucun `brew install`, aucun `apt install`, aucun binaire système.
- **Pourquoi** : on change d'ordinateur, on travaille depuis plusieurs machines. Un outil qui manque doit se rattraper par un `pip install`, jamais par une installation système à refaire de mémoire.
- **Ce que ça élimine** : `pdftotext` (poppler) et `tesseract`, sur lesquels reposent les deux systèmes actuels. Ce sont des programmes compilés, que `pip` ne sait pas installer.
- **Ce que ça coûte** : rien de mesurable. Test du 2026-09-08 sur trois articles académiques en deux colonnes du corpus — `PyMuPDF.get_text("text")` donne le même texte que `pdftotext -layout` (identique au mot près sur Dourish, à 0,2 % sur un survey de 70 000 mots), et retrouve les trois marqueurs de contrôle. Pour les PDF scannés, `RapidOCR` à **400 dpi** lit correctement le passage d'Engelbart 1962 sur lequel `tesseract` faisait référence — à 300 dpi il saute une ligne, c'est le réglage qui compte.
- **À vérifier avant de figer** : passer les 144 pages d'Engelbart à RapidOCR et comparer au fulltext tesseract déjà présent au dépôt (46 622 mots). C'est une validation gratuite sur le pire cas du corpus.
- **Date** : 2026-09-08.
