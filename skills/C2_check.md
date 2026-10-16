---
name: C2_check
description: Auditer un contexte — liens cassés, notes sans source, rétroliens manquants, sources jamais ingérées.
---

# C2_check

## But

Vérifier ce qui peut l'être mécaniquement, et rendre un verdict. Une vérification qui n'a pas de commande ne se fait pas : c'est le constat le plus net de la comparaison des systèmes précédents, où dix incohérences ont vécu des mois — dont un catalogue affichant « non analysé » pour vingt-quatre sources analysées.

## Procédure

1. Lancer l'audit :
   ```bash
   .venv/bin/python scripts/check.py "<contexte>"
   ```
   Sans argument, il audite tous les contextes.
2. Lire le verdict, désormais écrit dans `01-state/health.md`.
3. **Proposer les corrections**, groupées par gravité, et attendre l'accord avant de corriger quoi que ce soit.
4. Ce qui ne se corrige pas maintenant part dans `01-state/todo.md`.

## Ce que le script contrôle

| Contrôle | Pourquoi il compte |
|---|---|
| liens relatifs cassés | un lien mort fait douter de tout le reste |
| notes sans source | une note sans origine est une opinion, pas une connaissance |
| note `superseded` sans successeur | on ne sait plus quelle version fait foi |
| rétroliens manquants | celui qui arrive par l'autre bout n'a aucun moyen de savoir |
| sources jamais ingérées | une source ajoutée il y a six mois et jamais lue |
| extractions échouées | elles ne doivent produire aucune note |
| fichiers d'état restés vides | un contexte qui ne dit pas où il en est |
| README écrit à la main | un README non généré finit toujours par mentir |

## Règles

- `check` **ne corrige rien** de lui-même. Il constate, classe, propose.
- `health.md` est écrit par le script : ne pas le rédiger à la main.
- Un constat non traité n'est pas un échec de l'audit — mais il doit finir dans le todo, sinon il reviendra à l'identique la fois suivante.

## Sortie attendue

Le verdict — sain, défauts mineurs, défauts bloquants — puis les constats par gravité, et pour chacun la correction proposée.
