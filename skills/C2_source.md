---
name: C2_source
description: Ajouter une source documentaire à un contexte — figer son texte intégral et écrire sa fiche.
---

# C2_source

## But

Faire entrer une matière produite ailleurs, et la figer. Ce qui sera analysé plus tard est le texte complet, jamais un résumé.

## Procédure

1. Demander le fichier ou l'URL, et l'intention : pourquoi cette source est cherchée (`recherche`, `entretien`, `veille`, `référence`…). L'intention groupe la liste générée ; elle se corrige, un dossier ne se corrige qu'en déplaçant des fichiers.
2. Ajouter la source :
   ```bash
   .venv/bin/python scripts/source_add.py "<contexte>" "<fichier|url>" \
       --titre "<titre réel>" --intention "<intention>"
   ```
3. **Lire ce que le script annonce.** S'il affiche `extraction: failed`, s'arrêter : dire à l'utilisateur que la source est enregistrée mais inexploitable (PDF scanné sans couche texte, conversion à refaire), et **ne produire aucune note**.
4. Compléter la fiche créée dans `03-sources/documents/` :
   - `## Pourquoi elle est ici` — ce que cette source apporte à cette mission, deux ou trois lignes ;
   - `## Interprétation — non analysée` — ce qu'on en pense, ce qu'on lui reproche, l'écart avec ce qu'on croyait ;
   - ajuster `reliability` dans le frontmatter si `medium` ne convient pas.
5. Si l'utilisateur propose une page web trouvée par l'agent plutôt que par lui, **demander validation avant de l'ajouter**.

## Règles

- **La fiche trace, elle ne résume pas.** Un résumé écrit à l'entrée est une sélection faite avant d'avoir lu.
- **Le bloc d'interprétation est exclu de l'analyse.** Les notes naîtront du texte intégral, jamais de ce qu'on a écrit à propos de la source. On a le droit d'interpréter une source, à condition que cette interprétation ne devienne jamais la source.
- Ne jamais aspirer un site entier : une page, ou une liste courte d'URL validées.
- Une vidéo demande sa transcription intégrale, pas ses moments forts. Un PDF technique perd sa valeur si ses schémas disparaissent : au minimum, signaler leur présence.
- **L'accès ne vaut pas confiance.** Une source peut être fausse, datée, partielle ou contredite par une autre.

## Sortie attendue

L'identifiant attribué, où le brut et le texte ont été rangés, le résultat de l'extraction, et ce qu'il reste à compléter dans la fiche.
