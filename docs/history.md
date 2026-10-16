# 02-history — le journal de séance

Établi le 2026-09-09, refondu le 2026-09-10 : le classement par rubriques est repris de
`02-CONTEXT/memory_sessions`, qui produit des entrées lisibles sur le même modèle et le même
hook depuis des mois.

---

## 1. Ce que c'est

Un filet de secours. Une journée par fichier, une ligne par fait établi, rangée sous sa
rubrique. On ne le lit pas pour travailler — on le rouvre le jour où `01-state/` a
raté quelque chose, et ce jour-là il faut que ce soit dedans.

Ce qu'il n'est pas :

- **pas un récit** — des puces, aucune phrase de liaison ;
- **pas une synthèse** — il ne condense rien, il n'arbitre rien ; c'est `01-state/synthesis.md` qui condense ;
- **pas une transcription** — les propos de l'auteur vont dans `03-sources/sessions/`.

---

## 2. Le format

Une journée par fichier, sept rubriques, celles qui n'ont rien reçu étant absentes.

```markdown
# Journal — 03-livre-test — 2026-09-10

## Connaissances acquises

- 09:12 · auteur — un contexte contient deux types de sources : les sources figées comme une réunion client ou un PDF, et les sources de session accumulées en direct
- 09:20 · SRC00007 — la promotion vers la mémoire longue du système de contextes V1 s'est arrêtée en juin, et aucune note n'y a été versée depuis

## Écarté — ne pas reproposer

- 09:31 · auteur — un cadre de séance en tête de journal est écarté, parce que chaque ligne doit se comprendre seule sans dépendre de ce qui la surplombe
```

`- HH:MM · <provenance> — <fait>`

### Les sept rubriques

| Rubrique | Ce qu'elle reçoit |
|---|---|
| Connaissances acquises | un fait établi, appris ou posé |
| Ce qui est désormais acté | un choix, écrit comme l'état qu'il établit |
| Écarté — ne pas reproposer | une option rejetée, avec ce contre quoi on l'a rejetée |
| Révisé — ne plus s'appuyer dessus | une chose qu'on tenait pour vraie, et ce qui la remplace |
| Problèmes rencontrés | un blocage, ou deux choses tenues qui s'opposent sans arbitrage |
| À suivre | un point qui reste explicitement ouvert |
| Dérive de la mission | le but a changé : l'avant et l'après |

Les quatre dernières ne sont pas décoratives. `Écarté` empêche de rediscuter une option
morte dans trois semaines ; `Révisé` empêche de s'appuyer sur une note devenue fausse ;
`Dérive` est la seule trace du déplacement du but, `01-state/` ne gardant que la valeur
du jour.

**La provenance** ne répond qu'à une question : d'où ça sort. `auteur`, `IA`, ou
l'identifiant de la source lue.

### La règle d'écriture

**Nommer les choses concrètes** — le fichier, le script, la note, avec leur nom exact et ce
qu'ils sont. « Le système », « le modèle », « le journal » ne veulent rien dire relus dans
six mois. **Écrire à l'indicatif**, en phrase complète : jamais un infinitif, jamais un
groupe nominal. Un fait par ligne.

C'est tout. Le reste est porté par la rubrique, et c'est voulu : une rubrique ne peut
recevoir qu'un fait, et un fait se tient debout seul.

---

## 3. Qui l'écrit

**Une passe, déclenchée par un hook à la fin de chaque tour.** Ni l'auteur, ni l'IA en
séance. Le texte qu'elle envoie au modèle est dans
[`prompts/history_extract.md`](../prompts/history_extract.md), pas dans le script : il se
relit et se corrige sans ouvrir de code.

```bash
.venv/bin/python scripts/history_log.py extract --transcript <chemin>
```

Elle relit la transcription brute : les mots de l'auteur, ceux de l'IA, et ce que le tour a
ouvert — sans ces derniers, une note lue et jamais citée à l'écran lui resterait invisible.

Trois propriétés qui comptent :

- **idempotente** — elle n'ajoute que ce qui manque, on peut la relancer autant qu'on veut ;
- **incrémentale** — elle garde un repère de lecture et ne fait classer que le nouveau ;
- **muette en cas d'échec** — si le modèle ne répond pas, elle sort sans rien écrire et sans
  casser la séance. Le pourquoi se lit dans `.state/history-log-debug.log`.

### Ce qui a été appris le 2026-09-10

Une première version classait chaque énoncé par un **verbe** pris dans une liste de
quatorze — `infirmé`, `écarté`, `contredit`. Elle produisait des lignes du type
« l'indépendance du témoin externe, qui relit la même transcription » : des étiquettes qui
désignent sans rien dire. Quatre défauts de forme différents en une journée, et une règle
ajoutée à chaque fois, sans convergence.

La cause n'était ni le modèle ni l'automatisme : `02-CONTEXT/memory_sessions` tourne sur le
même hook et le même modèle, et produit des lignes lisibles. Elle était dans l'unité
demandée. **Un verbe demande de nommer un mouvement**, c'est-à-dire un rapport à un état
antérieur — et un rapport ne se nomme qu'en désignant ses deux bouts. **Une rubrique demande
un fait**, et un fait doit se tenir debout pour être un fait.

Deux autres différences relevées au passage, toutes deux corrigées : l'ancienne passe
recevait trente mille caractères d'un coup — devant un mur, un modèle résume en
abstractions ; et son prompt avait accumulé soixante lignes de règles d'écriture, là où
celui de `02-CONTEXT` en tient trois.

Le vocabulaire des quatorze verbes est conservé dans la note thématique `THM00011`, au cas
où il servirait ailleurs.

---

## 4. La frontière avec le reste

Trois endroits reçoivent de la matière. Ils ne se recouvrent pas.

| | Contenu | Fonction | Écrit par |
|---|---|---|---|
| `03-sources/sessions/` | les propos de l'auteur **sur le sujet**, verbatim | de la matière, destinée à être ingérée en notes | l'IA, en séance |
| `02-history/` | ce que chaque tour a établi, rangé par rubrique | un filet, jamais ingéré | la passe, hors séance |
| `04-notes/` | une idée par fichier, formulée pour durer | le travail lui-même | `ingest` |

Le journal et les notes restent **indépendants**. Aucun lien de promotion, aucun statut
« déjà versé » à entretenir : c'est exactement l'engrenage qui a tué la promotion en V1.

---

## Points encore ouverts

- Sept rubriques tiennent-elles à l'usage, ou deux ou trois ne servent-elles jamais ?
- La passe coûte un appel de modèle par tour. Acceptable, ou à ralentir ?
- Les fichiers antérieurs au 2026-09-10 ont été purgés. Rien à convertir.
