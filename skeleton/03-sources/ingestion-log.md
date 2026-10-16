# Journal d'ingestion

<!-- Écrit par `ingest`. Une entrée par lecture de source.

     Il répond à deux questions qu'aucun lien ne sait poser : cette source a-t-elle été
     lue en entier ? et qu'a-t-elle produit ?

     L'empreinte permet de repérer une source modifiée même quand la modification est au
     milieu du fichier. Une source n'est considérée comme entièrement lue que si son
     entrée est `complete` ET que son empreinte correspond au fichier actuel. -->

<!-- Format d'une entrée :

## SRC00001-nom-de-la-source
- chemin : documents/raw/SRC00001-nom-de-la-source.pdf
- état : complete | partial | needs-review
- empreinte : sha256:…
- lu le : 2026-01-01
- a produit : ATO00021, ATO00022, GLO00003

-->
