# Audit initial et plan de correction
Révision examinée : b3fe87a192384b760274ab79c21770d62ab96bf6, branche portfolio-cyber. Inventaire récursif de neuf fichiers. La racine contient une licence Apache 2.0, un fichier d’exclusion Git et une présentation de MathsLab. Le dossier portfolio contient deux documents, un CSV de 14 événements, un programme Python, une requête SQL et un module de tests. Aucune dépendance applicative externe déclarée.

| Priorité | Observation et portée | Traitement |
| --- | --- | --- |
| Moyenne, exactitude | SQLite renvoie NULL pour une date illisible dans strftime ; la comparaison SQL écarte alors la ligne. Le lecteur CSV saute la première ligne sans contrôler son nom. | Valider format, date réelle, colonnes, identité et unicité avant calcul. |
| Moyenne, livraison | Aucun workflow dans l’arbre initial. Les tests ne sont pas imposés avant diffusion. | Contrôles automatisés et construction du répertoire publiable après succès. |
| Faible, diagnostic | Les erreurs CSV/SQLite peuvent produire une trace locale. | Message de commande concis, sans contenu de ligne. |
| Fonctionnelle | Aucune interface Web, route HTTP, session, formulaire, politique navigateur, configuration de déploiement, métadonnée SEO ou composant visuel à tester initialement. | Site statique généré avec API JSON de lecture et démonstrations locales au navigateur. |

Le SQL utilise des paramètres à l’insertion. Aucun chemin ne reçoit de requête réseau ou de commande utilisateur. L’évaluation porte sur l’arbre courant, pas sur les anciens commits, les réglages du compte ou une infrastructure de production. Aucune exploitation constatée. Les trois tests initiaux passent ; la commande produit atlas puis boreal. Le volume de 14 événements ne permet aucune conclusion sur la capacité à l’échelle d’un SIEM.
