# Mots-clés — ce qui déclenche une action sans commande (V2)

Brouillon. Établi le 2026-09-08, en complément de [skills.md](skills.md).

Un **skill** fait avancer le contexte d'une étape de son cycle de vie. Un **mot-clé** attrape un geste trop fréquent pour mériter une commande : on l'écrit au fil de la conversation, et l'action se fait en plus de la réponse normale.

Les mots-clés ne sont actifs que **quand un contexte est ouvert**.

---

## 1. Ce qui se passe sans aucun mot-clé

Avant de parler des mots-clés, il faut dire ce que le système fait par défaut. Quand Laurent parle, chaque propos va dans l'un de trois endroits :

| Ce qu'il dit | Où ça va |
|---|---|
| Il donne ou pointe une matière (un lien, un fichier, un extrait) | dans les sources |
| Il affirme, suppose, définit, tranche ou constate une tension **sur le sujet** | dans la source de session du jour |
| Il pilote (« fais ça », « supprime », « tu en es où ? ») | **nulle part** — ce n'est pas conservé |

Le tri difficile est entre les deux derniers. En cas de doute, le système ne conserve pas — et il annonce en une ligne ce qu'il a décidé de noter, pour que Laurent puisse corriger tout de suite.

Les mots-clés servent à **forcer** ce tri quand il se trompe, ou à ranger un propos ailleurs que dans la source de session.

---

## 2. Les mots-clés

- **`décision : …`** — enregistre une décision **sur le contexte lui-même** (comment on le range, ce qu'on charge, quelle règle on adopte), avec sa date et ce qui l'a déclenchée. Va dans `01-state/decisions.md`.
- **`decision record : …`** — ouvre un arbitrage **sur le sujet du contexte** : ce que la mission tranche à propos de la chose étudiée. Va dans `04-notes/decision-records/`, un fichier par arbitrage.
- **`contradiction : …`** — enregistre une tension entre deux choses qu'on tient toutes les deux pour vraies, sans la résoudre.
- **`todo : …`** — ajoute une tâche au reste-à-faire.
- **`directive : …`** — ajoute une règle stable, qui vaudra pour toutes les sessions suivantes de ce contexte.
- **`session : …`** — force l'enregistrement du propos dans la source de session du jour, même si le tri par défaut l'aurait jeté.

## 3. Pourquoi ceux-là et pas d'autres

Un geste mérite un mot-clé quand il réunit trois conditions :

1. il revient plusieurs fois par session ;
2. il tient en une phrase ;
3. **il n'a pas d'endroit évident où aller** si personne ne le range tout de suite.

Une décision prise oralement au milieu d'une conversation disparaît si rien ne l'attrape au vol. Ajouter une source, en revanche, est un geste rare et lourd : il mérite une commande (`source`), pas un mot-clé.

## 4. Mots-clés hérités de `02-CONTEXT` qui ne sont pas repris

Ils existaient mais faisaient double emploi avec une commande. Les garder aurait créé deux façons de faire la même chose.

| Mot-clé abandonné | Ce qu'on utilise à la place | Pourquoi |
|---|---|---|
| `source : …` | la commande `source` | ajouter une source suppose de la télécharger, l'extraire, la ranger, l'indexer — ce n'est pas un geste qu'on glisse dans une phrase |
| `checkpoint` | la commande `save` | même action, deux noms |
| `fin de session` | la commande `save` | il n'y a pas de commande de fermeture : on s'arrête, et `open` ouvre la suivante |
| `alpha directive : …` | `directive : …` | le préfixe « alpha » n'apportait rien |

## 5. Règles de fonctionnement

- **Un mot-clé n'est actif que s'il est le premier mot du message.** Écrit au milieu d'une phrase, il ne déclenche rien. C'est ce qui rend la règle vérifiable par une machine plutôt que laissée au jugement de l'IA : `^décision :` se teste, « il y a une décision quelque part dans ce paragraphe » ne se teste pas. C'est aussi ce qui évite qu'une phrase qui *parle* d'une décision en enregistre une.
- Un mot-clé **agit tout de suite**, en plus de la réponse normale — il n'attend pas la fin de session.
- Le système **annonce en une ligne** ce qu'il vient d'enregistrer et où, pour permettre une correction immédiate.
- Si le mot-clé est incomplet ou ambigu (« décision : on verra »), le système **demande** avant d'écrire.
- Un mot-clé n'écrit **jamais** de note — à une exception près, `decision record :`. Une note ordinaire naît d'une source analysée, jamais d'une phrase attrapée en conversation. Un arbitrage, lui, **n'a pas de source externe** : il est pris par l'auteur, dans la conversation. Il n'y a rien à ingérer, il n'y a que la décision elle-même.
- **`decision record :` est le seul mot-clé qui pose des questions.** Un arbitrage sans alternatives écartées ni base de preuve ne vaut rien — c'est même le signe reconnaissable d'une justification écrite après coup. Le système demande donc ce qui manque avant d'écrire : contre quoi on a tranché, ce qu'on accepte de perdre, et sur quoi on s'appuie (une mesure, des retours, une contrainte, une intuition — l'intuition est légitime, à condition d'être nommée).

---

## Points encore ouverts

- Faut-il un mot-clé pour les questions ouvertes (`question : …`), ou est-ce que ça relève du reste-à-faire ?
- Faut-il un moyen de **retirer** au vol ce qu'un mot-clé vient d'enregistrer, ou est-ce qu'on corrige le fichier ?
- Les mots-clés sont en français. Un contexte rédigé en anglais garde-t-il les mêmes, ou faut-il des équivalents ?
