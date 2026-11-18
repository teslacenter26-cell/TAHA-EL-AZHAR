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

## Portfolio web et laboratoire interactif

[Rapport de livraison et état des dix projets](RAPPORT.md) · [Architecture](ARCHITECTURE.md) · [Audit initial](AUDIT.md)

Depuis la racine du dépôt sur la branche portfolio-cyber, avec Python 3.11+ et Node 20+ pour les tests client :

```sh
cd portfolio
python -m unittest -v
python build.py
node --test verification/client.test.cjs
python preview.py
```

Ouvrir http://127.0.0.1:8000/ pour voir les résultats SQL, comparer une empreinte ou examiner des en-têtes. Aucune installation de paquet applicatif. Le formulaire de contact ouvre un brouillon local.

[Publier la version vérifiée](DEPLOYMENT.md) · [Sécurité et signalement](SECURITY.md) · [Contribuer](CONTRIBUTING.md) · [Checklist de livraison](SECURITY-CHECKLIST.md) · [Historique](CHANGELOG.md)
