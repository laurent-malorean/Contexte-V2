# Entités — ce que sont les objets d'un contexte (V2)

Brouillon. Établi le 2026-09-08, en complément de [skills.md](skills.md), [keyword.md](keyword.md) et [skeleton.md](skeleton.md).

Ce fichier dit **ce que chaque objet est**. Pas comment on le sérialise : ni champ, ni gabarit, ni nom de fichier — ça viendra quand on construira `skeleton/`. Une définition solide doit tenir sans eux.

---

## La chaîne

```text
source  →  note  →  livrable
 le brut    la connaissance neutre    la mise en forme orientée
```

Chaque entité occupe une position dans cette chaîne, et **ne fait pas le travail de sa voisine**. C'est le principe qui gouverne toutes les frontières de ce document : le contexte ne range pas par sujet, il range **selon la place dans la chaîne**.

Les quatre verbes qui séparent les quatre types de notes :

|                       |                                                  |
| --------------------- | ------------------------------------------------ |
| La note atomique      | **stabilise une brique**                         |
| La note thématique    | **organise un ensemble de briques**              |
| L'entrée de glossaire | **stabilise les mots** employés dans ces briques |
| Le decision record    | **conserve un arbitrage**                        |

---

# Source

Une source est **la matière primaire** du contexte. Elle distingue *ce qui a été dit, lu, observé ou importé* de *ce que l'on en a compris*. Sans source, une note devient flottante : elle peut être juste, mais on ne sait plus d'où elle vient ni sur quoi elle repose.

Deux types, séparés par un seul trait : **l'un arrive fini, l'autre grandit pendant qu'on travaille.**

## Document

### Ce que c'est

Une matière produite ailleurs, qui **existe comme objet fini** : article, livre, vidéo, transcription, interview, PDF, page web, document importé. On peut la représenter par un fichier : une source, un contenu, un état stable.

Ce qui fait sa qualité n'est pas son contenu — il ne dépend pas de nous — mais **la fidélité de sa conversion**. Une source qui arrive mal convertie contamine tout ce qui en sortira : « une mauvaise ingestion abîme toute la chaîne. Si la source est incomplète ou mal structurée, les notes deviennent fragiles. Si les notes sont fragiles, les livrables le seront aussi. »

### Ce que ce n'est pas

- **Ce n'est pas une synthèse.** La fiche qui accompagne une source sert à tracer, pas à résumer. Le résumé qu'on ferait à l'entrée serait une sélection faite avant d'avoir lu.
- **Ce n'est pas une note.** La source conserve ; la note comprend.
- **Ce n'est pas un fichier déposé dans un dossier.** Importer, c'est « récupérer, nettoyer, convertir, préserver ce qui porte du sens ».

### L'interprétation est admise, mais mise en quarantaine

Une source documentaire mérite qu'on écrive ce qu'on en pense — pourquoi elle compte pour cette mission, ce qu'elle éclaire, ce qu'on lui reproche. C'est le seul endroit du contexte où l'orientation est permise.

Mais cette lecture est **explicitement séparée de la matière et exclue de l'analyse**. Les notes naissent du texte intégral, **jamais** de ce qu'on a écrit à son propos.

Sans cette séparation, une note hérite d'une sélection faite avant l'analyse, et personne ne peut plus le voir : c'est le défaut classique des « notes fondées sur un résumé ». La règle tient en une phrase : **on a le droit d'interpréter une source, à condition que cette interprétation ne devienne jamais la source.**

### Critères de qualité

**Le texte est intégral.** Pas d'extrait, pas de sélection. Ce qui sera analysé plus tard est le texte complet, jamais un résumé.

**Ce qui porte du sens hors du texte courant est préservé.** Un PDF technique perd beaucoup de valeur si ses schémas disparaissent — le minimum est de signaler leur présence, mieux vaut en produire une description. Une vidéo demande sa transcription intégrale, pas ses moments forts. Une page web demande son texte nettoyé avec titre, auteur, date et URL ; son décor n'a aucun intérêt.

**L'accès ne vaut pas confiance.** Une source peut être fausse, datée, partielle ou contradictoire avec une autre — même une source interne peut être obsolète. Trois choses se distinguent : les sources disent ce que le contexte peut consulter, les connecteurs comment il y accède, **les directives sous quelles conditions il peut utiliser ce qu'il trouve**.

**Une source dont l'extraction a échoué n'est pas exploitable.** Un PDF scanné sans couche texte, un fichier illisible : on garde la trace de la source — elle existe, elle est identifiée — mais **on ne produit aucune note** tant que la matière n'est pas figée. Un fichier vide est plus dangereux qu'un échec déclaré : il laisse croire qu'on a lu.

**Une source garde la trace de ce qu'elle a produit.** Quelles notes en sont nées, quand, et dans quel état on s'est arrêté. C'est ce qui permet de répondre à une question que le lien inverse ne sait pas poser : *cette source a-t-elle servi à quelque chose ?* Sans elle, on ne connaît que le chemin note → source, jamais source → notes.

**Sur une source longue, la lecture complète se prouve.** Une source courte se lit d'un bloc et il n'y a rien à démontrer. Au-delà de quelques milliers de mots, on ne peut plus affirmer « j'ai tout lu » — il faut pouvoir le montrer : quelles zones ont été parcourues, ce que chacune a donné, et **pourquoi une zone n'a rien donné** quand c'est le cas. Une zone sans note et sans justification n'est pas une zone stérile, c'est un trou.

C'est ce qui sépare une lecture d'un survol, et la différence ne se voit pas autrement : les deux produisent des notes qui ont l'air correctes.

### Le test

**Est-ce que je peux revenir à l'origine de ce que le contexte affirme ?** Si la réponse est non, la source n'a pas rempli son rôle, quelle que soit sa qualité apparente.

### Sa place dans la chaîne

Elle est en amont de tout. Elle ne se modifie jamais — elle est figée à l'entrée et le reste. C'est ce qui la rend arbitrable : quand une note se révèle fausse, on revient à la source, et la source n'a pas bougé.

## Session

### Ce que c'est

**Un canal pour verser dans le contexte une connaissance encore informelle.** C'est ce que l'auteur sait, comprend, sent ou relie, mais qui n'existe pas encore comme source stable.

Elle se construit **pendant** le travail, comme un flux continu : ce qu'on formule, corrige, valide, refuse, précise ou découvre dans l'échange avec l'IA. Là où une source documentaire est un objet, une source de session est un mouvement.

Elle existe parce qu'une partie de la connaissance **résiste à la citation**. Elle ne vient pas d'un document unique, elle circule sans URL, sans page, sans date nette — et pourtant elle influence fortement la manière de comprendre un sujet.

C'est aussi simple que ça : **l'humain a quelque chose dans la tête, il le dit à l'IA, et ça entre dans le contexte.** Une source documentaire, il faut aller la chercher, la convertir, vérifier ce qu'on en a tiré. Une source de session, il suffit de parler — et c'est le seul canal par lequel ce que l'humain sait sans l'avoir écrit peut entrer.

**Sa fonction première est la capture.** Elle garde la pensée vivante avant transformation, même désordonnée : oral retranscrit, répétitions, hésitations, reformulations, changements d'avis. Cette matière brute serait gênante dans un livrable ; ici elle est utile, parce qu'elle garde la trace du raisonnement en train de se construire.

### Ce que ce n'est pas

- **Pas un transcript complet.** Si une réunion a été transcrite, le transcript est une source documentaire immuable. La source de session porte plutôt **ce que l'humain comprend autour** de cette source : pourquoi une phrase compte, quelle tension elle révèle, quelle nuance reste hors du document.
- **Pas une note de réunion.** Une réunion a son propre périmètre ; sa note peut alimenter un contexte sans devenir pour autant une source de session.
- **Pas un chat log brut.** Tout l'historique d'une conversation n'a pas vocation à devenir source. Ce qui compte, c'est **la matière volontairement versée**.
- **Pas une base documentaire.** La base conserve les références ; la session capte ce qui est en train de se formuler autour d'elles.
- **Pas une note.** Elle conserve le brut ; les notes portent les idées clarifiées.
- **Pas un document du contexte.** Elle ne prend jamais un identifiant de source documentaire : ceux-là sont réservés à ce qui vient de l'extérieur. Une source de session est identifiée par sa date, et rien d'autre.

### Critères de qualité

**Un but et un focus.** Sans eux, elle devient un fourre-tout. Avec un bon focus, elle capte la matière utile sans décider trop tôt de sa forme finale.

**Le brut reste brut.** On transcrit, on n'interprète pas. L'interprétation naît des notes, pas de la source.

**Elle doit rester compréhensible hors du fil de conversation.** C'est le critère qui commande tous les autres : dans six mois, on lira ce fichier sans avoir la conversation sous les yeux. Un propos qui n'a de sens que dans le fil n'est pas capté, il est perdu.

**La question est gardée quand la réponse en dépend.** Quand l'IA pose une question, propose une reformulation, une hypothèse, une liste de points ou un choix, et que la réponse de l'humain ne se comprend qu'avec, l'intervention de l'IA est notée elle aussi. Sinon elle ne l'est pas — on ne verse pas tout l'historique du chat.

**La parole de l'humain et celle de l'IA sont séparées.** Deux blocs distincts dans le fichier : ce que l'humain a dit, et les interventions de l'IA nécessaires à la compréhension. Mélangées, on ne sait plus des mois après qui a pensé quoi — et une note tirée d'une reformulation de l'IA prise pour la parole de l'auteur est une fausse note.

**Un propos rapporté est signalé comme tel.** Quand l'auteur ne parle pas en son nom mais rapporte ce qu'un client, un collègue ou un tiers a dit, il le dit en le disant — et la source de session garde cette mention. Sans elle, une remarque entendue en réunion prend la même valeur que ce que l'auteur affirme lui-même, et la note qui en naîtra héritera d'une fiabilité qu'elle n'a pas.

**On ne verse pas tout mécaniquement.** Ce qui entre, c'est ce qui servira au contexte. Le pilotage de la conversation n'en fait pas partie.

**Le désordre est admis.** Elle n'a pas à être élégante. Sa fonction n'est pas d'être lisible, c'est de ne rien perdre.

### Quand la créer

Deux mouvements, également légitimes :

- **le micro-signal** — une phrase entendue en fin de call, une remarque qui ne mérite pas un document mais qui mérite de ne pas disparaître. Prise seule, elle semble faible. Mais « des dizaines de petits points accumulés au fil du temps peuvent changer la qualité d'un contexte » : ils font apparaître des motifs, renforcent des intuitions, révèlent des nuances ;
- **le bloc épais** — « voilà ce que j'ai compris après des années sur ce sujet », puis les exemples, les exceptions, les raisons, les limites.

### Quand ne pas la créer

Quand un transcript existe déjà — il devient une source documentaire. Quand la matière relève d'un autre contexte. Et pour tout ce qui est du **pilotage** : une commande, une question à l'assistant, du méta-discours ne sont pas de la matière. En cas de doute entre « dire conceptuel » et « pilotage », on choisit le pilotage : le bac qui ne conserve rien.

### Comment elle grandit

**Elle ne fait que s'allonger, jamais se réécrire.** On ajoute à la fin, on ne corrige pas ce qui est écrit.

**Un fichier par jour et par contexte, jamais un fichier par idée.** Une idée dite le matin et reprise l'après-midi doit se retrouver au même endroit ; découpée par sujet, on perd l'ordre dans lequel la pensée s'est faite, qui est justement ce qu'on voulait garder.

On lit à partir d'un repère posé à la dernière lecture, et on le repose au bout ; ce qui est avant n'est jamais relu. Pas besoin de comparer des empreintes : rien ne bouge derrière le repère, puisqu'on n'ajoute qu'à la fin.

**Ce qui est déposé hors session la rejoint.** Quand l'humain écrit quelque chose sans avoir l'IA sous la main, il le laisse dans la boîte aux lettres du contexte (`offline.md`). À l'ouverture suivante, ce dépôt est versé dans la source de session du jour, horodaté, et la boîte est vidée. Une pensée notée loin de la machine n'est pas une pensée d'un autre genre — elle entre par la même porte.

**Deux états, tous les deux calculés, jamais écrits dans un champ :**

| État | Comment on le sait | Ce que ça veut dire |
|---|---|---|
| fermée à l'écriture | la date du fichier est passée | on n'ajoute plus rien ; la parole du jour va dans le fichier du jour |
| finie d'être lue | le repère est en fin de fichier | tout a été ingéré |

Les deux sont **indépendants**. Une source d'hier est fermée à l'écriture dès aujourd'hui, mais reste à lire tant que le repère n'est pas au bout. **Fermer n'interdit que d'ajouter, jamais d'ingérer** — sans quoi on perdrait tout ce qui a été dit après la dernière lecture.

### À l'ingestion : enrichir avant de créer

C'est ici que la règle compte le plus. La même idée revient d'un jour à l'autre, chaque fois un peu plus nette. Dire trois fois la même chose avec trois nuances n'est pas un problème — c'est souvent comme cela qu'une idée mûrit. **Le rôle de l'ingestion n'est pas de produire trois notes, mais d'accréter les nuances dans une connaissance plus fine.**

Une source de session demande donc moins une logique d'archivage qu'une **logique de maturation**.

### Quand l'auteur se contredit

Un dialogue n'est pas cohérent : on peut dire une chose le matin et l'inverse l'après-midi. Trois cas se cachent là-dessous.

**Pendant la session, on demande.** C'est ce qui distingue cette source de toutes les autres : **elle répond**. Un PDF ne peut pas préciser ce qu'il a voulu dire.

| Ce qui s'est passé | Ce qu'on fait |
|---|---|
| il se reformule — il avait mal dit | on affine la note existante |
| il change d'avis | la nouvelle note remplace l'ancienne, qui reste marquée comme remplacée |
| les deux propos tiennent | on ouvre une contradiction, et une note si la tension elle-même est réutilisable |

**Hors session**, quand on ingère des jours plus tard : on ne tranche pas, on ouvre une contradiction. C'est le seul choix qui ne détruit rien.

### Le garde-fou

**Le fourre-tout.** Sans but ni focus, elle avale tout et ne sert plus à rien. Signal d'alerte : on n'arrive plus à dire pourquoi tel propos a été conservé.

### Sa place dans la chaîne

Elle est **le point d'entrée de la pensée humaine dans le contexte**. Elle précède les notes et leur fournit la matière primaire.

**Elle est la seule source qui n'a pas d'étape de conversion.** Un document arrive dans un format à extraire, et cette extraction peut échouer. La source de session naît déjà lisible : elle s'ingère telle quelle.

Elle est essentielle et insuffisante : un humain oublie, simplifie, ignore parfois l'état de l'art, une contrainte réglementaire ou une information récente. C'est pourquoi elle ne remplace pas les sources documentaires.

---

# Notes

## Atomiques

### Ce que c'est

> **Une note atomique est une note autonome, conceptuelle et réutilisable, avec un seul centre de gravité intellectuel.**

Elle capture **une seule unité de pensée** : un concept, une affirmation, une relation entre deux idées, une question précise.

Elle n'est pas forcément courte. Elle peut faire trois lignes ou une page. Elle peut contenir une définition, une explication, un exemple et une nuance — et rester atomique si tous ces éléments servent la même idée. **L'atomicité n'est pas une affaire de taille, c'est une affaire de cohésion.**

Une analogie tient bien : une note atomique suit une logique de *separation of concerns*. Une note = une responsabilité conceptuelle dominante.

> Elle est une unité de pensée assez claire pour être comprise seule, assez complète pour porter son idée, et assez distincte pour entrer en relation avec d'autres. **Une bonne note atomique est un bon voisin dans un réseau de pensée.**

### Ce que ce n'est pas

- **Pas une note courte.** Le mot « atomique » pousse au contresens : on imagine une unité minimale, donc la note la plus brève possible. C'est une erreur de critère.
- **Pas une capture.** Un extrait, un surlignage, une phrase copiée restent attachés à leur contexte d'origine. **Une note atomique commence quand on reformule.**
- **Pas une fiche de lecture.** Une fiche reste prisonnière de son livre : on se souvient vaguement que « tel auteur disait quelque chose sur tel sujet », et il faut rouvrir la source. La connaissance reste classée par origine au lieu d'être classée par concept.
- **Pas un résumé.** Un résumé compresse plusieurs idées ; une note en porte une.
- **Pas une page thématique.** « Tout sur X » n'est pas une idée.
- **Pas une citation recopiée.**
- **Pas de la matière pré-formatée pour le livrable.** Ni accroche, ni angle de pitch, ni punchline, ni slide déguisée.

### Critères de qualité

**La cohésion.** Tout ce que contient la note sert la même idée.

**La reformulation.** L'énoncé est autonome, jamais « l'auteur dit que… » ou « dans le chapitre 3… ».

❌ `Dans tel article, l'auteur dit que les notes doivent être atomiques.`
✅ `L'atomicité sert la réutilisation plus que la concision`

La première reste dépendante de la source. La seconde devient une unité de pensée réutilisable dans plusieurs contextes : écrire un guide, structurer un système, critiquer une méthode, expliquer pourquoi certaines notes deviennent inutilisables.

**Le titre propositionnel.** Le titre n'est pas une étiquette, **c'est déjà une prise de position**. Il affirme quelque chose qui pourrait être vrai ou faux. Lu seul, il communique l'idée entière.

❌ `Atomicité` · `Le prix` · `La maintenance préventive`
✅ `Une note atomique a un centre de gravité conceptuel unique`
✅ `Fragmenter excessivement transforme les liens en bruit`
✅ `Un prix élevé peut augmenter la demande pour les produits de statut`

Un titre comme `Atomicité` classe la note, mais il ne pense pas encore : il dit seulement dans quel dossier mental ranger le contenu.

**L'autonomie.** Compréhensible sans rouvrir la source ni lire une autre note.

**La traçabilité.** L'origine est toujours identifiable, et le fait sourcé se distingue de l'interprétation.

**La bonne granularité.** Une note trop large brouille les liens parce qu'elle parle de trop de choses. Une note trop fragmentée produit l'effet inverse : chaque micro-idée demande un lien, et le réseau devient pénible à lire. L'atomicité cherche le point entre ces deux excès.

**Des liens qui expliquent.** Le but n'est pas d'avoir beaucoup de liens, c'est d'avoir des liens qui nomment une relation : une cause, une conséquence, une objection, un exemple, une tension, une idée voisine.

### Les tests

**Le test principal** — et il est formulé par opposition :

> Le bon test n'est pas : « est-ce assez court ? »
> Le bon test est : **« est-ce que tout sert la même idée ? »**

**Le test de granularité.** Si retirer une partie de la note laisse une *autre* idée utile et autonome, elle en contenait deux → la scinder. Autre formulation : puis-je résumer la note en une phrase affirmative sans rien perdre d'essentiel ?

**Le test à six questions**, quand le doute persiste :

1. Puis-je donner un titre net à cette note sans hésiter ?
2. Ce titre décrit-il une seule idée principale ?
3. Le corps soutient-il entièrement ce titre ?
4. Si je supprime un paragraphe, est-ce que j'ouvre en fait une deuxième note possible ?
5. Puis-je comprendre cette note dans six mois sans relire la source ?
6. Puis-je la lier à plusieurs contextes différents ?

**Le test du titre comme diagnostic.** Si l'on n'arrive pas à donner un titre net à une note, ce n'est pas un problème de style : c'est souvent le signe que l'idée n'est pas encore claire.

**Le test inverse, rejoué une fois la note écrite.** Le test de granularité a déjà servi au moment de créer la note ; on le rejoue à la fin, **en confiance zéro envers le jugement initial**. Signal rapide : un titre qui contient « et », qui juxtapose deux propositions affirmatives, ou qui mélange un principe général avec son cas d'application, est une candidate probable à la scission. On relit alors l'idée principale et on vérifie si retirer une partie laisse un reste complet et autonome. Si oui, on scinde, et les deux notes se relient explicitement dans les deux sens.

Pas de relecture systématique pour ce seul motif : sans candidate détectée, il n'y a rien à faire.

### Quand la créer

Quand l'élément est un **fait durable**, une **hypothèse structurante**, une **question importante non résolue**, une **contradiction utile**, une **décision**, une **définition**, un **pattern récurrent** ou un **angle mort** — et seulement si l'idée est distincte, traçable et réutilisable ailleurs que dans son contexte d'origine.

### Quand ne pas la créer

Pour une reformulation mineure. Pour un passage rhétorique. Pour une instruction ultra-locale. Pour un détail sans valeur de réemploi.

**Et les deux motifs qu'il ne faut jamais invoquer pour écarter un passage.** On n'écarte un passage d'une source que s'il **échoue au test atomique** — *ce contenu contient-il une idée exprimable en une proposition, compréhensible hors source, réutilisable ailleurs ?* Si oui, on extrait, y compris au milieu d'un chapitre technique.

Écarter est réservé aux passages purement calculatoires : tables numériques, nomenclatures, index, bibliographies, procédures pas-à-pas sans principe. **Jamais au motif que le passage serait « méthodologique », jamais au motif qu'il serait « déjà couvert ailleurs ».**

Et symétriquement : **pas de quota**. On ne s'arrête pas à un nombre de notes décidé d'avance. On s'arrête quand la source ne contient plus d'idée de qualité à extraire — ce qui peut vouloir dire une note, ou trente. Le premier motif écarte précisément ce qui est le plus réutilisable ; le second remplace une vérification par une impression — si l'idée est vraiment déjà là, la règle qui s'applique est l'accrétion, pas l'omission.

### L'atomicité est un résultat, pas un point de départ

C'est l'erreur la plus fréquente : vouloir écrire directement des notes parfaites. On lit un texte, on ouvre son outil, et on se demande immédiatement si la note est assez atomique, où la ranger, quel titre exact lui donner. **Ce réflexe bloque plus qu'il n'aide.**

La capture peut être brouillonne, incomplète, mal titrée, collée à sa source, encore trop large. C'est normal. L'atomicité vient après, au moment où l'on transforme la matière :

1. capturer librement ;
2. regrouper les fragments par concept ;
3. formuler une idée générale ;
4. scinder si plusieurs idées apparaissent ;
5. ajouter des liens ;
6. revenir plus tard pour améliorer.

Trois niveaux à ne pas confondre : la **capture** (surlignages, extraits — utile, pas encore atomique), la **note de travail** (on reformule, on compare, c'est encore flou), la **note atomique** (autonome, claire, réutilisable, connectable).

### Comment elle grandit

**Par accrétion, pas par duplication.** Une note atomique est un point d'accrétion : elle grandit au fil de sources hétérogènes plutôt que d'être recopiée à chaque nouvelle source. Une première source fait apparaître l'idée. Une deuxième la confirme. Une troisième la nuance. Une quatrième en montre la limite. **Tant que le centre reste le même, la note se densifie.**

Nouvelle idée distincte → nouvelle note. Deux notes qui se recouvrent → **on ne fusionne jamais automatiquement** : deux idées proches peuvent diverger sur un point décisif. Scinder est sûr et réversible ; fusionner ne l'est pas.

**Une note doit souvent être scindée** quand son titre est un mot vague, quand elle contient plusieurs « et », « mais », « cependant » qui ouvrent chacun une piste autonome, quand elle juxtapose définition, exemple, objection et conclusion sans les distinguer, ou quand on ne sait pas quel lien faire vers elle parce qu'elle parle de trop de choses.

### Comment elle est remplacée

**Jamais par suppression.** Une note remplacée reste en place, marquée comme remplacée, et pointe vers celle qui prend le relais — qui pointe en retour vers elle. L'ancienne explique pourquoi on pensait cela à l'époque.

### Le garde-fou

**La finalité du livrable ne redéfinit jamais la note.** Même si la mission est de produire des posts, une note ne doit jamais être une accroche ou une punchline. Tant qu'elle est dans les notes, le but final n'a pas son mot à dire sur son contenu ni sur sa structure.

**Signal d'alerte observable** : une section qui justifie son contenu par l'objectif final plutôt que par sa valeur de connaissance en soi — `Utilité pour l'article`, `Pour le client`, `Accroche`. Quand ce signal apparaît, la note est en train de devenir un brouillon de livrable.

La raison est pratique autant que doctrinale : à partir d'un même ensemble de notes neutres, on peut produire un pitch, une documentation, un article, une narration commerciale, un onboarding. Formatées pour le pitch, elles ne serviraient qu'au pitch.

### Deux points arbitrés

**Le sourçage est obligatoire.** Une note peut très bien porter ta pensée plutôt que celle d'un auteur — mais un contexte est borné par une mission et **doit pouvoir prouver d'où vient ce qu'il affirme**. Y compris quand la source est ta propre parole : c'est précisément à cela que sert la source de session. Une note sans origine identifiable est une opinion, pas une connaissance.

**L'anonymisation est une règle de contexte, pas une propriété de la note.** Certains contextes exigent de remplacer les personnes par des rôles ; une recherche bibliographique exige au contraire de citer nommément. La règle vit dans les directives du contexte.

---

## Thématiques

### Ce que c'est

> **Une note thématique est une synthèse légère qui assemble plusieurs notes autour d'un angle utile.**

Elle ne sert pas à tout dire sur un sujet. Elle sert à faire apparaître **un motif, une tension ou une ligne argumentative** à partir de plusieurs unités de pensée. Là où la note atomique stabilise une idée autonome, la thématique organise une petite constellation d'idées.

Elle répond à une question simple : *qu'est-ce que ces notes, prises ensemble, permettent de comprendre ?*

> **Une bonne note thématique est une vue temporairement stable sur un réseau de notes.**

Elle peut assumer plusieurs idées — à condition qu'elles servent toutes le même angle.

### Ce que ce n'est pas

- **Pas un dossier.** C'est le contresens le plus fréquent : on crée une page `Marketing`, `Roadmap`, `Atomicité`, et on y empile tout ce qui semble lié. La note devient un inventaire — trop longue pour guider, trop générale pour penser, trop lourde pour être réutilisée.
- **Pas une encyclopédie.**
- **Pas une grosse note atomique.**
- **Pas une table de navigation.** Si elle devient une liste de liens sans synthèse, ce n'est plus une note thématique.
- **Pas une carte de navigation.** Une carte range et oriente ; une note thématique comprend. Une thématique qui se réduit à orienter a perdu sa fonction.
- **Pas un remplaçant des notes atomiques.** Elle ne les remplace pas, elle **les met en conversation**.

### Critères de qualité

**La sélectivité.** Elle ne rassemble pas toutes les notes possibles : elle choisit un angle.

**Le titre propose une lecture, pas un sujet.**

❌ `Contexte client`
✅ `Le contexte client devient un actif quand il relie signaux, décisions et preuves`

Le titre change tout : il ne nomme pas seulement un sujet, il propose une lecture.

Deuxième exemple, à partir de trois notes atomiques — *les prospects comparent au processus actuel plutôt qu'à un concurrent* · *une objection prix peut cacher une valeur mal contextualisée* · *le messaging doit relier la capacité produit à la situation réelle* — la thèse thématique qui émerge :

✅ `Les objections commerciales révèlent souvent un problème de contexte plutôt qu'un problème d'argumentaire`

C'est exactement son rôle : faire apparaître **un niveau de lecture qui n'existe dans aucune note atomique isolée**.

**Elle explique la relation, elle ne recopie pas.** Elle n'a pas besoin de reprendre le contenu des notes qu'elle relie.

### Ce qu'elle contient

- un sujet ou une question directrice ;
- une synthèse courte ;
- quelques notes atomiques reliées ;
- les tensions ou contradictions importantes ;
- parfois une piste de livrable — article, plan, décision, argumentaire, roadmap.

### Les tests

**Le test principal** : *qu'est-ce que ces notes, prises ensemble, permettent de comprendre ?* Si la réponse est « rien de plus que ce qu'elles disent séparément », il n'y a pas de note thématique à écrire.

**Les deux tests de dérive**, symétriques :

- si elle commence à **développer une idée autonome en profondeur** → extraire cette idée en note atomique ;
- si elle devient une **liste de liens sans synthèse** → ce n'est plus une note thématique.

### La règle qui départage l'atomique de la thématique

Devant une matière dont on ne sait pas quoi tirer, une question tranche : **peut-on la résumer en une phrase sans perdre l'essentiel ?**

Si oui → c'est une note atomique. Si non → c'est une thématique, et les idées qu'elle assemble deviennent des atomiques qu'elle référence.

Les deux ne s'excluent pas : une source riche produit souvent les deux — les atomiques pour les idées, la thématique pour ce qu'elles disent ensemble.

### Quand la créer

Quand plusieurs notes convergent et qu'un niveau de lecture supérieur apparaît. Elle est souvent **le chaînon entre le système de notes et l'écriture** : elle permet de passer de plusieurs idées dispersées à un plan possible.

**Elle est rare.** Sur l'ensemble des contextes existants : 314 notes atomiques pour 21 thématiques, soit environ une pour quinze. Une thématique par poignée de notes serait le signe qu'on fabrique des dossiers.

### Le garde-fou

**Le tableau de bord de production.** Une note thématique peut se transformer en suivi de chantier : des statuts de rédaction, des liens vers chaque texte en cours, des notes de travail brutes. Ce n'est plus une note, c'est un outil de pilotage déguisé — et c'est une dérive fréquente, parce qu'elle se vit comme un progrès.

**Signal d'alerte observable** : des statuts d'avancement, des liens vers des fichiers de livrable, des listes de tâches. Dès qu'une note thématique dit *où en est le travail* plutôt que *ce que les notes permettent de comprendre*, elle a changé de nature.

---

## Glossaire

### Ce que c'est

> **Une entrée de glossaire est une note qui stabilise un terme du domaine pour le rendre utilisable dans les décisions, les liens et les livrables.**

Elle doit être courte, claire, sourcée si possible, reliée aux notes qui l'utilisent, et attentive aux confusions.

> Un bon glossaire n'est pas une collection de définitions scolaires. **C'est un outil de précision collective.**

Le besoin est réel et permanent : **un terme change subtilement de sens d'une session à l'autre**, et d'une fonction à l'autre. Le même mot circule entre produit, marketing, sales, support, direction, design — chacun l'emploie sans lui donner exactement le même sens. Le glossaire évite cette fausse évidence.

Une entrée sert à dire : ce que le terme signifie ici ; ce qu'il ne signifie pas ; comment il est utilisé ; avec quels mots il peut être confondu ; quelles notes ou décisions il éclaire.

### Ce que ce n'est pas

- **Pas un mini-article.** Elle ne doit pas tout raconter sur un concept. Elle doit rendre un terme utilisable.
- **Pas une note atomique déguisée.** C'est la frontière décisive :

> **La première note pense. La seconde définit.**

❌ note atomique : `Une demande client doit rester un signal avant de devenir du travail` — c'est une **proposition**, elle affirme.
✅ entrée de glossaire : `Signal client — information issue d'un client ou d'un marché qui indique un besoin, une friction, une objection, une contrainte ou une opportunité, sans constituer immédiatement une décision ou un ticket.` — c'est un **mot**, elle délimite.

**La règle : un mot → glossaire. Une proposition → note atomique.**

- **Pas une collection de définitions scolaires.**
- **Pas une ontologie.** Une ontologie décrit ce dont un domaine est fait — les objets, leurs propriétés, leurs liens, les règles. Le glossaire définit des mots un par un ; dans une ontologie, **les liens comptent autant que les définitions**.
- **Pas un remplaçant.** Il ne remplace ni les notes atomiques — il leur donne un vocabulaire commun — ni les thématiques — il rend leurs synthèses plus lisibles — ni les sources — il aide à traduire leurs concepts dans le langage du projet.

### Ce qu'une bonne entrée répond

- **Définition courte.** Que veut dire le terme, en une ou deux phrases ?
- **Définition détaillée.** Quelles nuances faut-il connaître pour l'utiliser correctement ?
- **Usage dans le domaine.** Dans quels livrables, décisions ou discussions ce terme intervient-il ?
- **À ne pas confondre avec.** Quels mots proches créent des ambiguïtés ?
- **Liens contextualisés.** Quelles notes utilisent ce terme, **et pourquoi** ?

Deux ajouts que l'usage a validés :

**Un terme a un sens normatif et un usage terrain, souvent différents.** Une bonne entrée porte les deux : ce que dit la norme ou la définition de référence, et comment le mot est réellement employé en pratique.

**Le sens général et le sens local se distinguent explicitement.** La forme qui marche : un premier paragraphe pour le terme dans sa tradition générale, un second pour le sens retenu ici, introduit par une formule d'ancrage — « dans la distinction travaillée ici… », « dans ce contexte… ».

### Critères de qualité

**Elle se définit contre sa voisine.** Le couple `acteur` / `agent` est le modèle : chacune cite l'autre en tête de ses confusions, chacune ouvre son paragraphe local par la même formule, chacune existe par le contraste. **Une entrée isolée définit mal.**

**`À ne pas confondre avec` redéfinit positivement.** On n'écrit pas « ce n'est pas un agent », on écrit « agent : abstraction centrée sur l'action autonome, l'environnement et les objectifs ». Chaque voisin est redéfini brièvement, pas nié.

**Elle délègue l'argumentation.** L'entrée renvoie aux notes atomiques qui portent le raisonnement ; elle ne les recopie pas.

### Le test

**Le mot est-il ambigu, et utilisé ici dans un sens précis ?** Si le mot ne pose aucun problème de compréhension, l'entrée est décorative.

Un second critère, plus opératoire : **est-ce un mot qui porte les décisions ?** Certains mots ont l'air simples jusqu'au moment où l'organisation doit décider. « Client » peut désigner l'utilisateur final, l'acheteur, le prescripteur, le compte stratégique ou le segment prioritaire. « Qualité » peut vouloir dire robustesse technique, perception premium, absence de défauts, richesse fonctionnelle ou simplicité d'usage. « Lancement » peut désigner une mise en production, une annonce, une ouverture commerciale ou une disponibilité réelle.

### Quand la créer

Quand le terme est **central, ambigu, récurrent, ou nécessaire pour comprendre le domaine**. Le glossaire devient important dès qu'un système de notes sert à plusieurs personnes ou plusieurs usages.

Une liste courte de mots qui doivent absolument être stabilisés vaut mieux qu'un grand dictionnaire décoratif.

### Quand ne pas la créer

Quand le terme est transparent. Quand il n'apparaît qu'une fois. Quand ce qu'on veut écrire est en réalité une thèse — dans ce cas c'est une note atomique.

### Le garde-fou

**L'entrée qui devient argumentative.** Si une entrée commence à défendre une position plutôt qu'à délimiter un sens, il faut **extraire les idées dans des notes atomiques** et laisser l'entrée revenir à sa fonction.

**Signal d'alerte observable** : l'entrée contient un « parce que », un « donc », une justification. Un glossaire recense des usages attestés et tranche lequel vaut ici ; il ne démontre pas.

**Le deuxième piège est l'inverse** : le glossaire décoratif, rempli de définitions justes que personne ne consulte parce qu'aucune n'était ambiguë.

### Sa place dans la chaîne

C'est **une infrastructure**. Il ne produit pas de connaissance nouvelle : il rend utilisable celle des autres. Sans lui, les liens deviennent fragiles, parce que les mots qui les soutiennent restent ambigus.

Sa valeur n'est pas de figer le langage pour toujours. Elle est de **faire apparaître rapidement les écarts de définition**. Un langage commun ne supprime pas les conflits ; il évite qu'ils restent cachés sous les mêmes mots.

---

## Decision record

### Ce que c'est

> **Un decision record conserve la trace d'une seule décision structurante** : le contexte qui l'a rendue nécessaire, les options écartées, ce qui a été tranché, les conséquences acceptées.

Il ne répond pas à « qu'est-ce qu'on fait ? » mais à **« pourquoi a-t-on décidé ça, à ce moment-là, contre quelles alternatives ? »** Il répond au *pourquoi*, jamais au *comment*.

Il ne dit pas « voici la fonctionnalité à construire ». Il dit « dans ce type de situation, voici la règle que nous appliquons ».

**Propriété centrale : une fois actée, une décision ne se réécrit jamais.** Elle peut être remplacée, dépréciée, annulée ; jamais modifiée sur le fond, jamais supprimée. C'est la ligne de partage avec la documentation ordinaire : *la documentation décrit un état présent, le registre conserve une histoire.*

**Le problème qu'il résout** : sans trace du pourquoi, celui qui arrive après n'a que deux options face à un choix existant — **l'accepter aveuglément** (on ne touche pas à ce qu'on ne comprend pas) ou **le changer aveuglément** (on démonte une contrainte dont on ignorait la raison).

**Le symptôme de son absence** : la même discussion revient, à chaque arrivant, à chaque cas limite, à chaque changement de composition d'une réunion. Elle revient avec moins de contexte que la première fois, et aboutit parfois à la décision inverse sans que personne ne sache qu'il y en avait eu une. Le coût réel n'est pas le temps perdu, c'est la **perte de cohérence** : deux équipes appliquent deux règles opposées, chacune persuadée d'appliquer la bonne.

### Ce que ce n'est pas

| Ce n'est pas | La différence |
|---|---|
| Une **spécification** | La spec dit quoi construire ; le record dit pourquoi cette direction |
| Un **ticket** | Le ticket découpe une action ; le record pose une règle qui gouverne beaucoup d'actions |
| Un **compte rendu** | Le compte rendu raconte ce qui s'est dit ; le record ne retient que ce qui a été tranché et pourquoi |
| Une **documentation** | La doc décrit ce qui existe ; le record explique comment on en est arrivé là |
| Une **justification écrite après coup** | Un record rédigé pour couvrir une décision imposée est un artefact politique. **Détectable : aucune alternative écartée crédible** |

Et il ne se confond pas avec le fichier de décisions du contexte : celui-ci porte les décisions **sur le contexte comme outil** — comment on le range, ce qu'on charge, quelle règle on adopte. Le decision record porte les décisions **sur le sujet**. Deux objets différents, pas deux tailles du même objet ; il n'y a pas de passage de l'un à l'autre.

### Ce qui fait sa valeur

> **Elle ne se mesure pas au nombre de décisions documentées — mais au nombre de discussions qu'il supprime.**

D'où une conséquence de conception directe : **la rareté est une condition de fonctionnement, pas une préférence esthétique.** Un registre pléthorique n'est plus lu, donc ne clôt plus aucun débat, donc ne sert plus à rien. Quelques-uns par an suffisent — cinq, dix, vingt au maximum selon la taille de l'organisation.

Corollaire à retenir : **un registre peut se dégrader en grossissant**, sans qu'aucun indicateur ne s'allume.

### Les quatre rubriques qu'on bâcle

**Le contexte décrit des forces, pas une situation.** Pas « le client demande X ». Ce qui s'oppose : ce que ça coûte, ce que ça rapporte, ce que ça empêche, qui pousse dans quel sens. Un lecteur doit pouvoir se dire *« effectivement, il fallait choisir »*.

**Les alternatives écartées sont la partie la plus utile et la plus négligée.** Sans elles, la même discussion revient : quelqu'un demande « et si on faisait plutôt cela ? », et personne ne sait si l'option a déjà été étudiée ni pourquoi elle a été rejetée. **C'est aussi un test de sincérité : un record sans alternative crédible est presque toujours une justification a posteriori.**

**La base de la décision nomme son niveau de preuve.** Mesure, expérimentation, entretiens formels, retours informels, **intuition**. Écrire « intuition » est parfaitement légitime — **c'est le cacher qui ne l'est pas**. Un registre où l'on ne distingue plus le mesuré du ressenti donne à tout la même autorité, et rend impossible de savoir quoi rouvrir en priorité.

**Les conséquences distinguent l'arbitrage du risque.** Un **arbitrage accepté** est certain et déjà consenti : on sait ce qu'on perd, on le paie, il n'appelle aucune surveillance. Un **risque** est incertain et non consenti. Le glissement se fait toujours dans le même sens — présenter un arbitrage comme un risque, parce qu'un risque peut ne pas se réaliser. Reformuler « nous perdrons ces clients » en « il y a un risque de perdre des clients » supprime la perte de la trace. **Un record sans arbitrage explicite est presque toujours complaisant.**

### Le décideur est un rôle, jamais une personne

Deux raisons, chacune suffisante.

**Durabilité.** Les personnes partent, les rôles restent. Trois ans plus tard, « décidé par la direction produit » informe encore sur le niveau d'autorité et le type de considérations en jeu ; un nom propre n'informe plus sur rien.

**Écrivabilité.** Dès qu'une trace associe un choix à une personne identifiée, le registre devient un registre de responsabilités individuelles — un objet utilisable contre quelqu'un plus tard. L'effet n'est pas un refus explicite mais un **assèchement** : on écrit moins, plus prudemment, et l'on omet d'abord les hypothèses fragiles, les motifs réels et les arbitrages inconfortables. C'est-à-dire exactement ce qui a de la valeur.

> **Un dispositif qui n'est pas politiquement écrivable ne se remplit pas, quelles que soient ses qualités formelles.**

### Le test de création

> **Si la décision n'évitera aucune rediscussion future, elle n'a pas besoin d'un decision record.**

Mérite un record une décision **transverse** (elle gouverne plusieurs équipes ou situations), **structurante** (elle contraint ou libère des décisions futures), **durable**, **coûteuse à inverser**, **susceptible d'être rediscutée**, ou **non évidente** — un tiers informé aurait pu trancher autrement.

N'en mérite pas une décision **locale**, **ponctuelle**, liée à une seule fonctionnalité, **déjà couverte** par un record existant, **sans conséquence** au-delà de son exécution, ou si évidente que personne ne la rediscutera.

**Le meilleur signal disponible** : si une discussion a déjà eu lieu **deux fois**, elle mérite un record.

### Les contraintes subies en font partie

Une décision de direction, une exigence réglementaire, une limite contractuelle, un refus client ne sont pas des choix. Le réflexe est de ne pas les consigner. **C'est une erreur.**

Ce qui rend la trace nécessaire n'est pas la richesse du raisonnement mais le fait qu'**une option est fermée**. L'information à conserver n'est pas *pourquoi c'était le bon choix* mais **par qui** et **au titre de quoi**. Une contrainte non tracée est reproposée indéfiniment, et l'organisation ne peut plus distinguer ce qu'elle a écarté de ce qu'elle n'a pas le droit de faire.

### Les cinq états

| État | En vigueur ? | Ce que ça veut dire |
|---|---|---|
| **proposé** | pas encore | rédigé, soumis, pas tranché. **Seul état où le contenu peut encore être modifié** |
| **acté** | **oui** | **le contenu devient immuable**. C'est la règle en vigueur |
| **remplacé** | non | une décision plus récente a pris le relais, et elle est nommée |
| **déprécié** | non | ne s'applique plus, et **rien ne le remplace** — le sujet a disparu. Une phrase doit dire pourquoi, sinon on ne saura pas si la règle a été abandonnée par choix ou par oubli |
| **rejeté** | non | proposé puis refusé. N'a **jamais** été en vigueur. On le garde : il documente une option explicitement écartée, avec ses raisons |

**Trois règles absolues.** Aucune transition ne modifie le corps du record — on change l'état, on pose le lien, le fond reste intact pour toujours. Un record hors vigueur n'est jamais supprimé ni sorti du registre. Les transitions ne reviennent pas en arrière : pour revenir à une règle antérieure, on écrit un **nouveau** record qui remplace le remplaçant.

### La supersession, en quatre gestes

C'est le geste central, et le plus mal exécuté. Le réflexe est d'**éditer le record existant** pour le « mettre à jour ». C'est exactement ce qu'il ne faut pas faire : cela efface le fait qu'il y a eu changement, et avec lui la raison du changement.

1. **Écrire le nouveau record, complet et autoportant.** Quelqu'un qui ne lit que lui doit comprendre la règle en vigueur. Il ne dit jamais « comme le précédent mais avec X ».
2. **Expliquer *ce qui a changé*, pas seulement *ce qu'on décide*.** C'est la partie que tout le monde omet et la plus utile deux ans plus tard. **Une décision qui change n'est presque jamais une erreur corrigée : c'est une nouvelle décision dans un nouveau contexte.** Nommer ce qui a bougé — un coût qui a chuté, une contrainte apparue, une hypothèse invalidée — et, symétriquement, **ce qui n'a pas changé**. Sans cela, la substitution est lue comme un désaveu global alors qu'elle est locale.
3. **Poser le lien descendant** dans le nouveau, en motivant le renvoi.
4. **Marquer l'ancien — et rien d'autre.** Son état, le lien remontant, une ligne. **Le corps de l'ancien n'est pas touché. Pas une virgule.**

**Les deux liens ne protègent pas la même chose.** Le lien descendant préserve la généalogie, et on le pose spontanément en rédigeant le remplaçant. Le lien remontant **avertit celui qui arrive par l'ancien** — par une recherche, un lien externe, un signet. Sans lui, celui qui tombe sur la décision périmée n'a aucun moyen de le savoir : le document a l'air complet, daté, valide. **L'échec est asymétrique donc systématique**, parce que le lien remontant exige de retourner modifier un document déjà clos. C'est celui qui manque, et le seul dont l'absence induit en erreur.

Trois cas particuliers : un record peut en remplacer **plusieurs** ; **plusieurs** peuvent en remplacer un seul — signal fréquent que le record d'origine mélangeait deux décisions ; et **on n'élargit jamais silencieusement la portée** d'un record acté, même quand le résultat semble n'être qu'un ajout. L'extension ne se vit pas comme une réécriture, elle se vit comme une mise à jour légitime — c'est ce qui la rend dangereuse. L'interdit porte sur le geste, pas sur l'intention.

### Le garde-fou : la caducité silencieuse

Le vrai risque n'est aucun des trois états hors vigueur du tableau ci-dessus : dans les trois, on a écrit que le record ne s'appliquait plus. C'est **le record qui n'est plus appliqué mais reste marqué comme acté**.

**C'est le pire état possible — pire que ne pas avoir de registre du tout.** Le mécanisme : on ne lit pas un registre pour s'informer, on le **cite pour trancher**. Un élément faussement actif est donc invoqué comme argument d'autorité, puis démenti par le réel — et le démenti ne porte pas sur cet élément seul, il **détruit la confiance dans l'ensemble**. Une seule occurrence suffit : celui qui l'a vécu cesse de consulter le registre.

L'absence de registre est comparativement un état honnête : chacun sait qu'il doit reconstituer. La caducité silencieuse fait payer le coût de la tenue **et** produit de l'erreur.

**Signal d'alerte observable : il n'y en a aucun.** Rien ne se casse, aucun indicateur ne s'allume, le document reste bien formé et daté. Il ne se dégrade pas — c'est le monde autour de lui qui bouge. D'où les deux parades : des **conditions de réévaluation** écrites d'avance en événements observables, qui transforment une question subjective (« est-ce encore vrai ? ») en vérification factuelle ; et une **revue périodique** qui pose sur chaque record actif la seule question qui compte : *est-ce encore appliqué ?*

**Règle de discipline** : un record qu'on n'applique plus change d'état **le jour où on s'en aperçoit**. Reporter, c'est produire un registre menteur.

### Le coût d'entrée : capturer vite, instruire après

Un registre ne fonctionne que si **le coût d'entrée est proche de zéro**. Si écrire une décision suppose d'ouvrir un formulaire de deux pages, **on n'en écrit aucune** — et le registre reste vide en donnant l'illusion d'exister.

Face à un registre pauvre, le réflexe est d'exiger plus de champs. **C'est la mesure qui l'aggrave** : alourdir le format ne produit pas des traces plus riches, il produit moins de traces.

D'où la règle retenue : **le record naît immédiatement, avec la décision en une phrase et l'état « proposé »**. Les alternatives, les conséquences et la base de preuve se complètent ensuite. Un audit signale les records restés incomplets.

### Une tension à ne pas harmoniser

Les exigences de **rareté** et de **retrait d'autorité au périmé** tirent en sens inverse de la **conservation de l'instable** — garder ouvert ce qui n'est pas tranché. Les deux positions sont fondées et ne se résolvent pas l'une dans l'autre. C'est probablement le point où la doctrine du registre et celle du contexte divergent : à instruire, pas à lisser.

---

# Une règle qui vaut pour toutes les notes

Sur les liens, chaque système existant ne tient qu'une part de la règle. L'un exige d'**expliquer** chaque lien mais jamais de le poser dans les deux sens. L'autre exige la **bidirectionnalité** — déclarer un voisin oblige à mettre à jour la fiche citée — mais jamais l'explication. Un troisième fournit une **liste fermée de relations nommées** (définit, utilise, clarifie, contraste avec, nuance, contredit, remplace, dépend de, cause de…) et la règle « un lien ne doit jamais être décoratif ».

**V2 prend les trois : tout lien est expliqué, bidirectionnel, et sa relation est nommée.**

❌ `- [[Bon de travail]]`
✅ `- [[Bon de travail]] — une demande d'intervention peut être transformée en bon de travail après qualification.`

