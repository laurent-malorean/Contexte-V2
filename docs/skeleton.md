# Skeleton — la structure d'un contexte vide (V2)

Brouillon. Établi le 2026-09-08, en complément de [skills.md](skills.md) et [keyword.md](keyword.md).

Ce fichier décrit **ce que contient un contexte au moment où on le crée**, avant d'y avoir mis quoi que ce soit. Il sert de spécification pour le dossier `skeleton/`, qui sera un contexte vide, complet, qu'on **copie** à chaque création.

---

## 1. Deux règles qui définissent l'objet

**Le squelette est un vrai dossier, pas une description.** `new` le copie. Personne ne le reproduit d'après un texte. C'est ce qui garantit que deux contextes créés à six mois d'écart sont identiques — et c'est ce qui manque aujourd'hui à `02-CONTEXT`, dont la structure n'existe que décrite dans une commande.

**Chaque fichier arrive avec ses titres de sections et une ligne qui dit ce qu'on y met.** Un contexte vide explique son propre usage : on n'a pas besoin d'aller lire la doctrine pour savoir ce qui va dans `contradictions.md`.

## 2. Les noms sont en anglais

Pour qu'un anglophone puisse ouvrir un contexte et s'en servir sans traduction. Les noms de dossiers et de fichiers sont en anglais, en ASCII, sans accent ni espace. Le contenu, lui, est écrit dans la langue de la mission.

---

## 3. La structure

```text
{context-name}/
  README.md                navigation
  offline.md               boîte aux lettres : on y dépose hors session, `open` la vide

  00-frame/                ce qui bouge peu
    mission.md             le but, la question centrale, ce qui est dans et hors sujet
    directives.md          les règles stables de ce contexte
    loading.md             quoi charger à l'ouverture

  01-state/                ce qui bouge à chaque session
    state.md               ce qu'on sait, ce qui reste incertain, les dettes
    checkpoints.md         la suite des états figés — un bloc par session, le plus récent en tête
    synthesis.md           ce qui est devenu stable et ne bouge plus
    todo.md                le reste-à-faire, par priorité
    decisions.md           ce qu'on a tranché sur le contexte lui-même, et pourquoi
    contradictions.md      ce qui s'oppose et qu'on n'a pas tranché
    handoff.md             comment reprendre sans tout relire
    health.md              verdict du dernier `check`

  02-history/              le log des idées, une section par session
    YYYY-MM-DD.md          un énoncé par ligne, avec son verbe — extrait de la transcription, jamais réécrit

  03-sources/
    README.md              la liste de toutes les sources, tous types confondus
    ingestion-log.md       quelle source a été lue, quand, et ce qu'elle a donné
    documents/             de la matière produite ailleurs, qui arrive finie
      raw/                 le fichier d'origine, tel quel
      fulltext/            son texte, si le format n'était pas lisible
    sessions/              de la parole, produite ici, qui grossit
      SESSION-YYYY-MM-DD.md

  04-notes/
    atomic/                ATO00001-…  une idée par note
    thematic/              THM00001-…  un angle qui relie plusieurs notes
    glossary/              GLO00001-…  un terme du domaine
    decision-records/      DRE00001-…  un arbitrage tranché sur le sujet

  05-outputs/
    _draft/                ce qui n'est pas fini
```

Six dossiers. `02-CONTEXT` en a neuf, `MINI` en a quatre.

L'arbre ci-dessus n'en montre que deux, mais **chaque répertoire porte un `README.md`** — et celui d'un dossier parent pointe vers le `README.md` de chacun de ses dossiers enfants. On parcourt ainsi tout le contexte de proche en proche, sans jamais avoir à déplier l'arborescence. Ces README sont générés, jamais écrits à la main.

### Les sources sont rangées par type, et chaque type a sa forme

Dans `03-sources/`, le premier étage est le **type de source**, jamais l'état d'un fichier. Deux types aujourd'hui, d'autres peuvent venir.

Deux aujourd'hui — `documents/` et `sessions/` — définis dans [entity.md › Source](entity.md#source). Ce qui les sépare tient en un trait : **l'un arrive fini, l'autre grandit pendant qu'on travaille.**

**Chaque type définit sa propre forme interne.** `documents/` a besoin de deux étages — `raw/` pour le fichier reçu, `fulltext/` pour son texte quand le format n'était pas lisible — parce que sa matière demande une conversion. `sessions/` n'en a pas besoin : le fichier *est* la matière. Un type futur aura la sienne, sans avoir à se plier à celle des autres.

Ce qui reste commun à tous les types reste à la racine de `03-sources/` : la liste des sources et le journal d'ingestion.

---

## 4. Qui écrit quoi

C'est la colonne la plus importante du document. Un fichier que personne n'a la charge d'écrire finit vide ; un fichier que tout le monde peut écrire finit faux.

| Fichier | Écrit par | Quand |
|---|---|---|
| `README.md` (**de chaque répertoire**) | **généré** | à chaque ajout ou suppression — jamais à la main |
| `health.md` | **généré** par `check` | à chaque `check` — jamais à la main |
| `offline.md` | **l'humain**, hors session | vidé par `open` |
| `mission.md` | l'humain | à la création, puis rarement |
| `directives.md` | l'humain, ou le mot-clé `directive :` | quand une règle se stabilise |
| `loading.md` | l'humain | quand le contexte change de nature |
| `state.md` | `save` | à chaque point d'étape |
| `checkpoints.md` | `save` | un bloc ajouté en tête, seulement si quelque chose a changé — jamais retouché |
| `synthesis.md` | `save` | quand quelque chose devient stable |
| `todo.md` | le mot-clé `todo :`, et `save` | en continu |
| `decisions.md` | le mot-clé `décision :` | au vol |
| `04-notes/decision-records/` | le mot-clé `decision record :`, puis quelques questions | quand un arbitrage sur le sujet est tranché |
| `contradictions.md` | le mot-clé `contradiction :` | au vol |
| `handoff.md` | `save` | réécrit à chaque fois — donc toujours frais |
| `02-history/YYYY-MM-DD.md` | **une passe automatique**, jamais l'IA en séance | à chaque fin de tour ; `open` ouvre la section, `save` rattrape |
| `03-sources/**` | `source` et `session` | à l'ajout |
| `ingestion-log.md` | `ingest` | à chaque lecture de source |
| `04-notes/**` | `ingest` | quand une source donne une idée |
| `05-outputs/**` | `build` | pendant la rédaction |

Trois choses se lisent dans ce tableau :

- **deux fichiers sont générés** et ne se touchent pas à la main — c'est ce qui les empêche de mentir ;
- **`handoff.md` n'a qu'un seul auteur**, `save`. Personne d'autre n'y écrit, sinon il devient un brouillon de plus ;
- **cinq fichiers se remplissent au vol**, par mots-clés, parce qu'une décision prise à l'oral disparaît si rien ne l'attrape sur le moment.

---

## 5. Les règles que la structure fait respecter

**On n'écrit jamais deux fois la même information.** Une source est décrite dans son propre fichier ; la liste des sources est régénérée en les lisant. Il n'y a pas de catalogue tenu en parallèle. Aujourd'hui `02-CONTEXT` en tient trois, et deux affichent du faux depuis des mois.

**Les identifiants se calculent en regardant les fichiers présents.** Pas de compteur. Le risque habituel — réattribuer un numéro libéré par une suppression — n'existe pas, parce qu'**une note n'est jamais supprimée** : elle est remplacée, et l'ancienne reste en place, marquée comme remplacée, avec un lien vers la nouvelle.

**Une décision sur l'outil et une décision sur le sujet ne vont pas au même endroit.** Ce sont deux objets différents, pas deux tailles du même objet.

`01-state/decisions.md` porte sur **le contexte** — comment on le range, ce qu'on charge, quelle directive on ajoute. `04-notes/decision-records/` porte sur **le sujet** — ce que la mission tranche à propos de la chose étudiée. Le détail est dans [entity.md › Decision record](entity.md#decision-record).

**Il n'y a pas de passage de l'un à l'autre.** Une décision sur l'outil ne deviendra jamais une décision sur le sujet, même très structurante — elles ne sont pas sur la même échelle. Les deux mots-clés sont donc différents : c'est toi qui dis de quoi tu parles, l'IA n'a pas à le deviner.

Exemple, sur ce contexte-ci où les deux sont aujourd'hui mélangés dans un seul fichier : « un penseur ne reste dans la section globale de la bibliographie que si son apport est global » range un livrable — **outil**. « La grille passe à 13 facettes » affirme quelque chose sur le concept de Contexte — **sujet**, donc un decision record.

Un decision record obéit à la doctrine des notes : traçable, réutilisable hors du contexte, et **jamais réécrit** — quand il ne tient plus, un nouveau le remplace et l'ancien reste en place, marqué comme remplacé, parce qu'il explique pourquoi ce choix était raisonnable à l'époque.

**Ce qui n'est pas tranché a sa place.** `decisions.md` et `contradictions.md` sont là dès la création, vides. C'est la seule chose que `MINI` n'a nulle part : chez lui, une tension non résolue n'a aucun endroit où aller.

Et ce n'est pas un fichier d'exceptions. Le monde est fait de contradictions : il s'en présentera tout le temps. `contradictions.md` est un **organe principal**, au même rang que les notes. Trois choses en découlent.

- **Une contradiction a un cycle de vie.** Elle s'ouvre, et un jour elle se referme — en tranchant, ou en supprimant un des deux termes. Quand elle se referme, **la façon dont elle a été résolue est écrite dedans**. `02-CONTEXT` le fait déjà bien, on garde son modèle.
- **Ce n'est pas un dépotoir.** Une contradiction, ce sont deux propos qui **tiennent tous les deux**. Un propos et sa correction, non. Si tout ce qu'on n'a pas su trancher y atterrit, le fichier se remplit de fausses contradictions et ne se lit plus.
- **Une contradiction ouverte depuis longtemps n'est pas un défaut.** `check` les liste pour qu'on ne les oublie pas ; il ne les compte jamais comme des erreurs. Garder ouvert ce qui n'est pas résolu est précisément le travail du contexte — un audit qui pousse à les refermer trahirait ce pour quoi le fichier existe.

**Le mode d'emploi de reprise porte sa date.** `handoff.md` affiche en tête la date à laquelle il a été écrit, et `check` le signale dès qu'il est plus vieux que la dernière session. Ici, il a servi un mode d'emploi daté du 12 juillet pendant deux mois sans que rien ne prévienne.

---

## 6. Ce qui a été retiré, et pourquoi

| Retiré | Venait de | Pourquoi |
|---|---|---|
| `08_qa/` | `02-CONTEXT` | créé dans les 9 contextes, utilisé par aucun |
| `risks.md` | `02-CONTEXT` | grille de risques produit, vide et jugée hors sujet dès qu'on ne fait pas de produit — à rajouter au cas par cas |
| `glossary.md` (fichier de mission) | `02-CONTEXT` | un terme s'enrichit au fil des sources : c'est une note, pas une liste |
| `source_catalog.md` + `source_index.json` | `02-CONTEXT` | deux copies de ce que les sources disent déjà d'elles-mêmes |
| `06_index/index.json` | `02-CONTEXT` | un compteur devient inutile si aucune note n'est supprimée |
| `focus.md` séparé | `02-CONTEXT` | resté vide un mois ; le focus tient dans `mission.md` |
| `current_plan.md` séparé | `02-CONTEXT` | faisait double emploi avec `todo.md`, et les deux ont dérivé |
| les 6 modèles de livrables | `02-CONTEXT` | tous des documents de product management ; aucun ne convenait à un livre, donc le livre s'est écrit hors du mécanisme |
| `02_checkpoints/` — le **dossier** et le fichier par jour | `02-CONTEXT` | l'état figé est conservé, mais comme bloc de trois lignes dans `01-state/checkpoints.md`. Ce qui disparaît, c'est un fichier daté par jour, réécrit à chaque point d'étape, qui cohabitait avec un journal faisant la moitié du même travail. Voir §7. |

Et une chose reprise de `02-CONTEXT` contre `MINI` : le préfixe des notes thématiques est **`THM`**, pas `THE`. En anglais, `THE00001` se lit comme l'article « the ».

---

## 7. On travaille par session, pas par journée

On ferme un contexte pour toutes sortes de raisons : la fenêtre de contexte est pleine, on change d'ordinateur, on est interrompu. Il arrive donc de travailler **plusieurs fois dans la même journée** sur le même contexte, en s'arrêtant et en rouvrant entre chaque.

Trois choses en découlent.

**Un fichier par jour, une section par session.** Le fichier s'appelle `2026-09-08.md`. Si on a travaillé trois fois ce jour-là, il contient trois sections : `## Session 1 — 09:12 → 11:40`, et ainsi de suite. La date sert à ranger ; ce qui compte, c'est la session. On ajoute toujours à la fin, on ne corrige jamais ce qui est déjà écrit.

### À quoi sert vraiment ce dossier

Pas à raconter. Un récit de session n'est lu par personne : `02-CONTEXT` en produit depuis juillet, et rien ne s'y réfère jamais. Ce dossier sert à **deux choses précises**, que rien d'autre ne porte :

- **vérifier un fait quand le rangement a échoué.** Le système n'a pas su où mettre quelque chose, ou l'a mal interprété en le rangeant : on remonte et on recoupe. C'est le même rôle que `raw/` pour une source — ce vers quoi on revient quand la transformation s'est mal passée ;
- **ne pas rouvrir une impasse.** Ce qu'on a lu, essayé, ouvert, et qui n'a rien donné.

Deux règles en découlent.

**Il ne doit pas sortir de la couche qu'il sert à arbitrer.** Un résumé ne peut pas arbitrer un résumé : un récit rédigé en fin de session viendrait de la même interprétation que celle qui a fait l'erreur, avec le même angle mort. Ce dossier est donc écrit par **une passe séparée**, qui relit la transcription brute de la séance — les mots de l'auteur compris — et non le souvenir qu'en garde l'IA.

**Il s'écrit au fil de l'eau, pas à la fermeture.** La passe tourne à chaque fin de tour. Tout reconstruire à la fin, c'est refaire précisément l'étape qui a échoué — et perdre le début de la séance quand la fenêtre se compacte.

### Le format

Une ligne par énoncé : l'heure, le verbe qui dit ce que cet énoncé a fait aux idées, l'énoncé, et sa provenance.

```text
02-history/2026-09-08.md

## Session 1 — 09:12
- 09:14  appris     Dourish oppose le contexte représentationnel au contexte interactionnel  · SRC00007
- 09:52  affirmé    un périmètre fermé est un choix de conception, pas une limite subie      · auteur
- 10:31  tranché    les sources vont à plat, sans sous-dossier par type                      · auteur
- 11:02  nommé      « inter-contexte » désigne la circulation, pas la hiérarchie             · auteur
- 11:38  écarté     la piste « mémoire transactive » ne recoupe pas la mission               · IA
```

`open` ouvre la section de la session suivante, ce qui referme la précédente. `save` rattrape ce que le hook n'a pas pu poser. Les quatorze verbes et le mécanisme sont dans [history.md](history.md).

Une même idée peut donc se trouver ici **et** dans une note, formulée autrement. Ce n'est pas une entorse à la règle « on n'écrit jamais deux fois la même information » : ce sont deux usages distincts — on fouille le log pour retrouver, on lit la note pour travailler. Et les deux restent **indépendants** : aucun lien de promotion, aucun statut « déjà versé » à entretenir. C'est exactement l'engrenage qui a fait mourir la consolidation dans `02-CONTEXT`.

**Le checkpoint n'est plus un fichier par jour, c'est un bloc dans une série.** `02-CONTEXT` écrit un fichier daté par jour, qu'il faut réécrire à chaque point d'étape — et qui cohabite avec un journal faisant la moitié du même travail. V2 garde l'état figé, mais autrement : `save` ajoute **un bloc de trois lignes en tête de `01-state/checkpoints.md`**, et ne le retouche plus jamais. Le bloc n'est écrit que si quelque chose a changé depuis le précédent.

```text
01-state/checkpoints.md

## 2026-09-08 · session 2 — 14:22
28 sources · 61 notes · 13 facettes · 4 décisions · 2 contradictions ouvertes
Prochaine action : retirer Kant de F13.

## 2026-09-08 · session 1 — 11:40
28 sources · 61 notes · 13 facettes · 4 décisions · 2 contradictions ouvertes
Prochaine action : retirer Kant de F13.

## 2026-09-05 · session 1 — 18:03
27 sources · 48 notes · 13 facettes · 4 décisions · 1 contradiction ouverte
Prochaine action : analyser SRC-027.
```

Pourquoi un fichier à part, et pas dans la trace du jour : **on ne lit jamais un état figé tout seul, on parcourt la série.** « Où j'en étais quand j'ai décidé ça ? » demande d'en comparer plusieurs. Enfouis dans les fichiers de trace, ils ne se parcourent pas — il faudrait ouvrir chaque jour et sauter les lignes d'événements. Ici, un an de travail tient dans un fichier qu'on lit d'un coup.

Pourquoi le plus récent en tête : on ouvre le fichier et on voit où on en est, sans le parcourir. Une IA lit les vingt premières lignes et a les trois dernières sessions. Le coût — réécrire tout le fichier au lieu d'ajouter à la fin — est sans conséquence à cette taille, et une écriture dans un fichier temporaire suivie d'un renommage écarte le risque d'interruption. La règle « on ne réécrit jamais ce qui est écrit » est tenue : aucune ligne passée n'est altérée, elles sont seulement décalées.

**Ce n'est pas une copie de `state.md`.** `state.md` fait une cinquantaine de lignes — ce qu'on sait, ce qui reste incertain, les dettes. Le bloc figé n'en garde que les compteurs et la prochaine action. Deux objets différents, rien à synchroniser.

Le sens de lecture diffère donc d'un fichier à l'autre, et c'est voulu :

| | sens | pourquoi |
|---|---|---|
| `checkpoints.md` | le plus récent **en tête** | petit, lu souvent, on ne veut que le début |
| `02-history/YYYY-MM-DD.md` | ajout **en fin** | écrit dix fois par session, lu rarement, et alors dans l'ordre où les choses se sont passées |

**Un contexte n'est pas forcément sous git.** C'est un dossier ; il peut vivre sans dépôt. Quand git est là, il apporte un confort — l'état exact d'un fichier à une date — mais **aucune règle du système ne doit en dépendre**. `save` commite quand le contexte est versionné, et ne fait rien de plus quand il ne l'est pas.

**`save` doit prendre trente secondes.** Mettre à jour `state.md`, écrire `handoff.md`, ajouter le bloc en tête de `checkpoints.md`, poser sa ligne dans la trace. Rien d'autre. C'est la seule commande de consolidation : si elle coûte cher, on ne la lancera pas au moment où on en a le plus besoin — quand la fenêtre est pleine et qu'on est pressé.

---

## 8. Les sources de session

Une source de session ne ressemble à aucune autre : elle **grossit pendant qu'on travaille**, là où une source documentaire est figée à l'entrée. Elle demande donc un traitement à part — un repère de lecture, deux états calculés plutôt qu'écrits, l'enrichissement des notes plutôt que leur duplication, et une règle pour ce que l'auteur se contredise.

Tout cela est décrit dans [entity.md › Source › Session](entity.md#session), avec la définition de l'entité. Ce document ne garde que sa place dans la structure : `03-sources/sessions/`, un fichier par jour.

---

## 9. Points encore ouverts

- `loading.md` en markdown lisible, ou en `.json` parsable ? Le markdown se corrige à la main, le JSON ne s'interprète pas de travers.
- `00-frame/` est-il le bon nom ? `00-charter/` dit peut-être mieux « le contrat de la mission ».
- Les sources sont-elles rangées par intention (recherche, entretien, veille) à l'intérieur de `raw/` et `fulltext/`, ou à plat ?
- Faut-il un `.gitkeep` dans les dossiers vides du squelette, pour qu'ils survivent à la copie ?
- `synthesis.md` et `state.md` sont voisins : l'un dit ce qui est stable, l'autre ce qui ne l'est pas encore. La frontière tiendra-t-elle à l'usage, ou faut-il les fusionner ?
