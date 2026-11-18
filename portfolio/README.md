# Taha El Azhar | Portfolio cybersécurité

Enseignant en mathématiques, titulaire d’un master en mathématiques pures, je souhaite mettre mon expérience en analyse de données et en pédagogie au service d’une équipe de cybersécurité. Ce portfolio présente un laboratoire reproductible de détection et d’investigation.

## Enquête sur des connexions inhabituelles

Deux comptes présentent chacun cinq échecs de connexion suivis d’une réussite. Faut-il ouvrir deux incidents ? Le laboratoire montre comment construire une règle SQL, en mesurer les erreurs sur des cas étiquetés et décider quelle alerte examiner en premier.

| Pour explorer le travail | Pièce à consulter |
| --- | --- |
| Comprendre la décision en deux minutes | [Note de triage et limites](TRIAGE.md) |
| Examiner la logique de détection | [Requête SQLite](detection.sql) |
| Reproduire les résultats | [Programme Python](analyse.py) et [jeu d’essai fictif](evenements.csv) |
| Vérifier le comportement aux limites | [Tests automatisés](test_analyse.py) |

### Reproduire sur son poste

Depuis une copie de cette branche, ouvrir un terminal dans le dossier `portfolio`. Python 3 et sa bibliothèque standard suffisent.

```sh
python analyse.py
python -m unittest -v
```

La première commande affiche deux alertes classées par heure UTC. La seconde vérifie notamment la borne de dix minutes, le regroupement par compte et par adresse, et l’exclusion des échecs postérieurs à une réussite.

Les données, les comptes et le contexte d’enquête sont fictifs. Les étiquettes de scénario servent uniquement à évaluer la règle après son exécution.
