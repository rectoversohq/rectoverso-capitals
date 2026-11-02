# Capitales

Relier les lieux à leurs capitales, dans les deux sens.

[English](README.md) · [Périmètre et sources](docs/coverage.md) · [Construction et mises à jour](docs/build.md)

**Candidat local pour revue — non publié.** Aucun téléchargement n’est encore publié.

Une source commune produit **488 cartes en français** et **488 en anglais**, dans deux paquets indépendants. Le référentiel comporte 249 pays et territoires ISO ; seules les questions pertinentes sont incluses. Les exclusions sont documentées, sans capitale inventée.

Les rôles des capitales et des sièges du gouvernement sont précisés. Les champs continent et région facilitent la recherche. Dans Anki, **Explorer** ouvre une courte note après la réponse. La compatibilité native RectoVerso reste une vérification distincte.

## Construire pour Anki

Utiliser Python 3.14 et la version d’Anki fixée dans `requirements.txt`. Aucun compte ni service payant n’est nécessaire. Ce jeu ne contient que du texte : les données JSON suivies dans Git suffisent, sans outil graphique ni téléchargement d’images.

```sh
python3.14 -m venv /chemin/hors-du-depot/anki-venv
/chemin/hors-du-depot/anki-venv/bin/python -m pip install -r requirements.txt
/chemin/hors-du-depot/anki-venv/bin/python scripts/ci.py --output /chemin/hors-du-depot/premiere-construction
```

La sortie doit être un **nouveau dossier hors du dépôt**. La commande construit chaque langue deux fois, contrôle les identités et le contenu, importe et affiche les deux faces de chaque carte avec le moteur Anki, effectue une vraie réponse, puis vérifie médias et progression après export/réimport.

Importer `packages/Capitales-fr-488.apkg` dans Anki. Le paquet anglais s’appelle `Capitals-en-488.apkg`. Chacun possède ses propres identités et sa propre progression.

## Modifier et publier

Travailler sur une branche du dépôt du jeu. Modifier les données partagées ou les fichiers de langue, conserver les identités stables et relancer la même commande dans un nouveau dossier. Une revue éditoriale et visuelle native, dans les deux langues et thèmes, reste nécessaire. La réussite de CI n’autorise pas la publication.

Les sources initiales et les corrections sont attribuées dans les données. Les données initiales d’Ultimate Geography sont dans le domaine public ; les noms usuels suivent le référentiel Maps. Les nouvelles créations sont sous CC BY 4.0 ; les licences d’origine des composants sont conservées. Voir [NOTICE](NOTICE.md) et [LICENSE](LICENSE.md).
