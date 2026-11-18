# Rapport de livraison · Taha El Azhar
Branche portfolio-cyber. L’état initial et les priorités figurent dans [l’audit](AUDIT.md). L’architecture finale utilise Python, SQLite, HTML sémantique, CSS, JavaScript et Web Crypto. [Architecture](ARCHITECTURE.md).

| Modification | Fichiers concernés |
| --- | --- |
| Validation des données et traitement des erreurs | analyse.py, test_portfolio.py |
| Présentation, profil, compétences, projets, certifications déclarées et contact | web/index.html, web/style.css, web/app.js |
| Données JSON en lecture seule, en-têtes HTTP, liste des ressources exposées | build.py, preview.py |
| Tests des interactions, responsive et captures | verification/client.test.cjs, verification/navigateur.py |
| CI, manifeste applicatif, configuration sans secret | ../.github/workflows/portfolio.yml, requirements.txt, .env.example |
| Documentation et suivi | README.md, AUDIT.md, ARCHITECTURE.md, SECURITY.md, CONTRIBUTING.md, DEPLOYMENT.md, SECURITY-CHECKLIST.md, CHANGELOG.md, RAPPORT.md |

## État des projets Blue Team
| Projet | État et preuve |
| --- | --- |
| Security Audit Dashboard | Prévu. Le tableau d’alertes existant traite uniquement le journal synthétique. |
| Security Headers Analyzer | Livré. Trois vérifications locales, dont détection de doublons ; test client Node. |
| File Integrity Monitoring | Comparateur ponctuel SHA-256 livré et testé sur référence identique, différente et fichier trop volumineux. La surveillance continue reste à développer. |
| Log Monitoring Dashboard | Livré sur instantané synthétique. Deux alertes issues de la règle SQL ; tests Python et Node. |
| Vulnerability Management Dashboard | Prévu. Première étape proposée : importer un rapport de dépendances fictif et suivre la correction. |
| Secure Authentication Demo | Prévu. Les événements d’authentification sont simulés. |
| Security Configuration Checker | Vérifications HTTP du site et de la sortie de construction livrées. Vérificateur de configuration général prévu. |
| Incident Response Documentation | Note de triage livrée dans TRIAGE.md avec hypothèses, décision et limites. |
| Secure API Demonstration | Ressource JSON publique en lecture seule livrée. Routes de lecture et refus d’écriture testés en local. Une API authentifiée reste à développer. |
| DevSecOps Security Pipeline | Workflow fourni avec tests, Bandit, audit du manifeste applicatif, détection de secrets et génération d’artefacts après succès. Vérifier l’état GitHub du commit avant publication. |

## Résultats locaux
- Six tests Python réussis, dont les trois tests de détection initiaux. Validation des entrées, blocage des fichiers inattendus, routes, méthodes, en-têtes, absence de cookies et de CORS permissif.
- Un test Node réussi sur DOM simulé couvrant le journal, les en-têtes, l’intégrité et l’encodage du brouillon. Syntaxe JavaScript vérifiée. Le formulaire exige une messagerie configurée.
- Contrôle statique local limité aux appels directs eval/exec dans les trois modules applicatifs ; recherche locale de quelques signatures de secrets. Aucun signal sur ce périmètre. Le contrôle CI est plus large.
- 14 événements, 2 alertes. Médiane locale de détection de 0,46 ms (5 séries de 50 exécutions sur le même jeu en mémoire). Environ 10 Kio pour HTML, CSS, JS et JSON non compressés. Ce microbenchmark ne mesure pas le réseau.
- Le test Chromium local a échoué au démarrage du navigateur, avant affichage. Les captures réelles et les vérifications à 360/768/1440 px sont produites par le job navigateur lorsqu’il réussit. La conformité WCAG et le rendu sur appareils physiques restent à examiner.
- Aucune distribution Python tierce dans l’application. Les versions directes de l’outillage sont fixées. Les résultats des scanners de CI et les contrôles de production dépendent de leur exécution effective.

## Risques résiduels et suite
Une règle unique produit des faux positifs et des faux négatifs. La validation des IP et dates garantit la forme des observations, pas leur authenticité. La lecture et la jointure en mémoire conviennent au petit exercice. Les alertes publiées sont publiques ; conserver un jeu synthétique. La sécurité HTTP dépend de l’hébergeur. Après validation visuelle et mise en ligne, prioriser un deuxième cas d’enquête documenté avant de compléter les tableaux de bord prévus.
