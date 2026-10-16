---
name: C2_new
description: Créer un contexte V2 en copiant le squelette, puis rédiger sa mission.
---

# C2_new

## But

Créer un contexte, et lui donner une frontière assez nette pour qu'on sache ce qu'il refuse.

## Procédure

1. Demander le nom du contexte s'il n'est pas donné. L'utilisateur le choisit ; ne rien lui imposer.
2. Créer la structure :
   ```bash
   .venv/bin/python scripts/new_context.py "<nom>" --but "<une phrase>"
   ```
3. Ouvrir `contexts/<nom>/00-frame/mission.md` et le remplir avec l'utilisateur. Quatre blocs, aucun ne se saute :
   - **le but** — ce que le contexte doit produire ou permettre de comprendre ;
   - **la question centrale** — celle qui guidera tous les tris à venir ;
   - **ce qui est dans le sujet** ;
   - **ce qui est hors sujet** — le bloc décisif : sans lui, un contexte devient un fourre-tout.
4. Si l'utilisateur donne des règles propres à ce contexte (langue, anonymisation, niveau de preuve exigé), les écrire dans `00-frame/directives.md` avec leur date.
5. Régénérer la navigation :
   ```bash
   .venv/bin/python scripts/refresh_readmes.py "<nom>"
   ```

## Règles

- **Ne jamais reproduire la structure à la main.** Le script copie un vrai dossier ; c'est ce qui garantit que deux contextes créés à six mois d'écart sont identiques.
- Ne pas inventer le but ni le hors-sujet : ce sont les deux seules choses que l'utilisateur est seul à savoir. Demander.
- « On ne sait pas encore » est une réponse valide pour le livrable attendu — mais elle doit être écrite.

## Sortie attendue

Le nom du contexte, son but en une phrase, et la prochaine action : compléter la mission, ou ajouter la première source.
