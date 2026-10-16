# Le cycle de vie d'un contexte

Pourquoi ces sept commandes, et pas d'autres. Les procédures elles-mêmes sont dans [../skills/](../skills/).

## Le cycle en une phrase

On **crée** un contexte, on l'**ouvre** pour travailler, on l'**alimente** en matière, on **transforme** cette matière en notes, on **consolide** ce qu'on a compris, on **vérifie** que tout tient, et on **range** le contexte quand il n'est plus actif.

```text
C2_new → C2_open → C2_source / C2_session → C2_ingest → C2_save
                             ↑                              ↓
                             └──────────────────────────────┘
                                       C2_check
                                      C2_archive
```

## 1. Créer

**`C2_new`** crée le contexte en **copiant un gabarit réel** — pas en décrivant une structure à reproduire — et l'inscrit dans la navigation.

Ce que ça garantit : deux contextes créés à six mois d'écart ont exactement la même structure.

## 2. Ouvrir

**`C2_open`** absorbe ce qui a été déposé hors session, charge ce que **ce** contexte demande de charger — la liste lui est propre —, affiche l'état courant et la prochaine action.

Ce que ça garantit : rien de ce qui a été écrit hors session n'est perdu, et on ne charge pas tout le contexte pour rien.

## 3. Alimenter

**`C2_source`** ajoute une source, en fige le texte intégral, la range, et l'inscrit à un seul endroit.

Ce que ça garantit : la matière analysée plus tard est le texte complet, jamais un résumé.

**`C2_session`** verse un bloc de connaissance dans la source de session du jour, ou restitue ce qui a été capté pour que l'auteur le corrige.

La parole ordinaire n'a pas besoin de cette commande : le routage de `SYSTEM.md` la verse à chaque message. Mais deux gestes ne s'obtiennent pas autrement — **dérouler délibérément un bloc épais** (« voilà ce que j'ai compris après des années »), et **relire ce qui a été capté pour corriger un mauvais tri**. Sans un endroit où regarder, on ne sait pas ce que le contexte a retenu de vous.

C'est aussi la seule fonction du système dont l'échec est documenté : dans le système précédent, la règle était écrite et le dossier `sessions/` est resté vide quatre mois. Une règle permanente et une commande ne se remplacent pas, elles se doublent.

## 4. Transformer

**`C2_ingest`** lit les sources non encore traitées, en tire des notes, prouve la couverture, et journalise ce qu'il a produit avec l'empreinte de la source.

Ce que ça garantit : on sait quelles sources ont donné quoi, et une source modifiée est repérée même si la modification est au milieu du fichier.

## 5. Consolider

**`C2_save`** met à jour l'état, promeut vers la synthèse ce qui est devenu stable, réécrit le mode d'emploi de reprise, ajoute un bloc de checkpoint, pose sa ligne dans la trace du jour, et rattrape les mots-clés qui n'ont pas été appliqués.

**Une seule commande, lancée quand on veut. Il n'y a pas de commande de fermeture.**

Pourquoi : les artefacts de reprise sont exactement ce qu'on perd quand on ne ferme pas proprement — et on ne ferme pas proprement précisément quand on en a le plus besoin : fenêtre pleine, machine coupée, interruption. Les mettre derrière une commande de fin, c'est les perdre au pire moment. Et « déclarer la session finie » ne sert à personne : c'est `C2_open` qui ouvre la section suivante, donc la précédente se termine d'elle-même.

Deux conséquences à tenir : **`C2_save` doit prendre trente secondes**, et un bloc de checkpoint n'est posé que si quelque chose a changé — sinon la série se remplit de doublons.

## 6. Vérifier

**`C2_check`** audite le contexte et rend un verdict.

Pourquoi ce skill existe : dans le système précédent, la vérification était écrite partout et déclenchée nulle part ; dix incohérences ont vécu des mois, dont un catalogue affichant « non analysé » pour vingt-quatre sources analysées. Une vérification qui n'a pas de commande ne se fait pas.

## 7. Ranger

**`C2_archive`** sort le contexte des actifs — après avoir signalé ce qui reste ouvert et demandé confirmation.

## Trois principes qui traversent la liste

**Ne jamais écrire deux fois la même information.** Un identifiant se calcule en regardant les fichiers présents ; une liste de navigation se réécrit à partir de ce qui existe. Dès qu'une information est recopiée, elle peut un jour ne plus correspondre sans que rien ne le signale.

**Une règle qui n'est pas déclenchée ne sera pas suivie.** Tout ce qui doit arriver à coup sûr est accroché soit à une commande, soit à `SYSTEM.md`, qui est chargé en permanence.

**Le script ne décide jamais d'un contenu ; le LLM n'écrit jamais un identifiant, un chemin, ni un champ de frontmatter.**
