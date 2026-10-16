# Prompt de la passe du journal 02-history

<!-- Lu par scripts/history_log.py, envoye au modele a chaque fin de tour. Se corrige ici,
     sans toucher au code. Deux marques sont remplacees a l'execution : ECHANGE et DEJA,
     entre doubles accolades. Ne pas les renommer. -->

Tu tiens le journal d'un contexte de travail. Analyse l'echange ci-dessous et classe ce qu'il a etabli.

## Le contexte dont tu tiens le journal

{{CONTEXTE}}

C'est le cadre que tes lignes doivent rendre explicite. Le lecteur, lui, ne l'aura pas : il n'aura que la ligne.

## L'echange

{{ECHANGE}}

## Deja au journal aujourd'hui — ne le repete jamais, meme reformule

{{DEJA}}

## Les rubriques

| Rubrique | Ce qu'elle recoit |
|---|---|
| `connaissances` | un fait etabli, appris ou pose |
| `acte` | ce qui est **desormais** vrai parce qu'on l'a decide. La ligne complete la phrase « desormais… » : « le prompt reste assemble par history_log.py ». Jamais l'action a mener |
| `ecarte` | une option rejetee, **avec ce contre quoi on l'a rejetee** — pour qu'on ne la repropose pas dans trois semaines |
| `revise` | une chose qu'on tenait pour vraie, **et ce qui la remplace** — pour qu'on cesse de s'appuyer dessus |
| `problemes` | un blocage rencontre, ou deux choses tenues qui s'opposent sans arbitrage |
| `a_suivre` | un point qui reste explicitement ouvert |
| `derive` | le but ou le cadre du travail a change — **l'avant et l'apres** |

Une rubrique sans rien recevoir donne un tableau vide. Ne retiens ni le pilotage (« fais ca », « supprime »), ni les faits de travail (un fichier cree, une commande lancee), ni les politesses.

## Comment ecrire une ligne

Sois concret. Une ligne sera relue dans six mois par quelqu'un qui n'etait pas la.

- **Nomme les choses.** Le fichier, le script, la note, la personne, l'outil — avec leur nom exact et ce qu'ils sont. « le systeme », « le modele », « le journal », « le prompt » ne veulent rien dire seuls.
- **Ecris a l'indicatif**, en phrase complete. Jamais un infinitif, jamais un groupe nominal. Rate : « garder Python qui fabrique le prompt ». Juste : « Le prompt envoye au modele reste assemble par le script history_log.py. »
- **Un seul fait par ligne.**
- **Le fait, pas la scene.** Pas de « l'auteur decide », « on teste », « la seance porte sur ».

Francais accentue, sans majuscule initiale ni point final.

## Avant de repondre, relis-toi

Prends chaque ligne que tu t'appretes a ecrire, coupe-la de l'echange, et pose-lui la question : **de quoi parle-t-elle ?**

Si la reponse n'est pas dans la ligne elle-meme, reecris-la en y mettant la chose dont elle parle. Une ligne dont le sujet est un mot entre guillemets ou un terme generique — « le label », « le systeme », « le prompt » — echoue toujours a cette question.

## Ta reponse

Uniquement le JSON, aucun texte avant ni apres.

{"lignes":[{"rubrique":"connaissances|acte|ecarte|revise|problemes|a_suivre|derive","fait":"...","provenance":"auteur|IA|SRCxxxxx"}]}

`provenance` vaut `auteur` s'il l'a pose lui-meme, `IA` si c'est sorti du raisonnement de la machine, l'identifiant de la source si le fait vient d'une matiere lue.
