---
uuid: 00000000-0000-0000-0000-000000000000
id: DRE00001
created: 2026-09-08
updated: 2026-09-08
status: proposed
decided_by:
decided_on:
supersedes:
superseded_by:
sources: []
---

<!-- status : proposed | accepted | superseded | deprecated | rejected
     Valeurs en anglais : champ lu par des outils, pas de risque d'accent ni d'accord.
     `proposed` est le seul état où le corps peut encore être modifié. Après `accepted`,
     une transition change l'état et pose un lien — jamais une virgule du corps.

     decided_by : un RÔLE, jamais une personne. « direction produit », pas un nom.
     Un registre nominatif devient un registre de responsabilités, et on cesse d'y écrire.

     supersedes / superseded_by : présents même vides. Un champ vide dit « rien ne remplace
     ceci » ; un champ absent ne dit rien.

     Ce fichier naît avec le titre, la Décision en une phrase et status: proposed.
     Le reste se complète après. Un audit signale les records restés incomplets. -->

# La décision en une phrase, à l'affirmatif

<!-- Le titre énonce la décision, pas le sujet. L'affirmatif inclut le négatif.
     ❌ Support navigateur   ✅ Nous ne supportons que les deux dernières versions majeures
     ❌ Support des langues  ✅ Le produit n'est traduit qu'en français et en anglais -->

## Décision

<!-- OBLIGATOIRE. La règle, sans ambiguïté, avec ses bornes : ce qui est inclus, ce qui ne
     l'est pas. Elle dit « dans ce type de situation, voici la règle », pas « voici ce
     qu'on construit ». Le pourquoi, jamais le comment. -->

## Contexte

<!-- OBLIGATOIRE. Des forces en tension, pas une situation. Ce que ça coûte, ce que ça
     rapporte, ce que ça empêche, qui pousse dans quel sens.
     Un lecteur doit pouvoir se dire « effectivement, il fallait choisir ». -->

## Hypothèses

<!-- Ce qu'on tient pour vrai sans l'avoir démontré. C'est souvent ici que se trouve la
     raison pour laquelle la décision sera un jour rouverte. -->

## Alternatives écartées

<!-- La rubrique la plus utile et la plus négligée. Chaque option avec SON motif de rejet,
     pas seulement son nom. C'est aussi le test de sincérité du record : sans alternative
     crédible, c'est presque toujours une justification écrite après coup.

     Cas particulier — une contrainte subie (décision de direction, exigence réglementaire,
     limite contractuelle, refus client) n'a pas d'alternative. On écrit alors PAR QUI
     l'option est fermée et AU TITRE DE QUOI. Une contrainte non tracée est reproposée
     indéfiniment. -->

## Raisons du choix

<!-- L'argument comparatif : pourquoi celle-ci plutôt que celles-là. -->

## Base de la décision

<!-- Le niveau de preuve : mesure, expérimentation, entretiens formels, retours informels,
     intuition. Écrire « intuition » est légitime ; le cacher ne l'est pas. Sans ce niveau,
     tout a la même autorité et on ne sait plus quoi rouvrir en priorité. -->

## Conséquences

### Positives

<!-- Ce que la décision rend possible. -->

### Arbitrages acceptés

<!-- Ce qu'on perd, à coup sûr, et qu'on a consenti à payer. Certain, déjà accepté,
     n'appelle aucune surveillance.
     Ne jamais reformuler un arbitrage en risque : « nous perdrons ces clients » ne
     devient pas « il y a un risque de perdre des clients ». Cela supprime la perte
     de la trace. Un record sans arbitrage explicite est presque toujours complaisant. -->

### Risques

<!-- Incertain et non consenti. Ce qui peut arriver et qu'on surveille. -->

## Conditions de réévaluation

<!-- Écrites d'avance, en événements observables. Elles transforment une question
     subjective (« est-ce encore vrai ? ») en vérification factuelle.
     C'est la seule parade à la caducité silencieuse : un record périmé ne casse rien,
     n'allume aucun indicateur, et reste bien formé et daté. -->

## Décisions liées

<!-- OBLIGATOIRE. UNIQUEMENT des liens vers d'autres decision records. Tout le reste va
     dans la section suivante. Ce n'est pas cosmétique : c'est ce qui permet de
     reconstituer le graphe des décisions sans le confondre avec la documentation autour.

     Le lien descendant (ce record remplace X) se pose spontanément.
     Le lien remontant — aller marquer l'ancien — est celui qu'on oublie, et le seul dont
     l'absence induit en erreur : sans lui, celui qui arrive par l'ancien record n'a aucun
     moyen de savoir qu'il lit une règle morte.
     En remplaçant un record, dire aussi CE QUI A CHANGÉ — et ce qui n'a pas changé.
     Une décision qui change est rarement une erreur corrigée : c'est une nouvelle
     décision dans un nouveau contexte. -->

## Sources et références

<!-- OBLIGATOIRE. Tout ce qui n'est pas un decision record : fils de discussion, tickets,
     documents, mesures, incidents. Le frontmatter `sources:` ne porte que les sources du
     contexte ; cette section porte ce qui vit à l'extérieur. -->
