# Architecture et frontières de confiance

1. Le traitement hors ligne lit le CSV synthétique. Il valide les colonnes, les comptes, les IP, les dates UTC et les identifiants avant insertion paramétrée dans SQLite en mémoire. La règle existante produit une ligne par réussite signalée.
2. La construction copie trois ressources explicitement nommées et sérialise les résultats en JSON. Un dossier de sortie contenant un fichier inattendu fait échouer la construction.
3. Le navigateur lit ce JSON sur la même origine et utilise des nœuds texte. Le calcul SHA-256 et la lecture des en-têtes collés restent dans le navigateur. Le formulaire ouvre un brouillon auprès de la messagerie du visiteur.
4. Le serveur de prévisualisation écoute sur la boucle locale et expose quatre chemins de lecture. En production, un hébergeur statique sert les fichiers construits sous HTTPS. Python et SQLite ne traitent aucune entrée réseau en production.

## Contrats
Le CSV utilise id, compte, ip, instant et resultat. L’instant suit AAAA-MM-JJTHH:MM:SSZ. Le résultat vaut succes ou echec. Un identifiant est unique et positif. Le traitement rejette le lot entier en cas d’erreur. La ressource alertes.json contient des objets {id, compte, ip, instant, echecs}, triés par réussite. Tous les visiteurs voient les mêmes données fictives.

Aucune base persistante, session, clé API, télémétrie ou soumission de formulaire sur le serveur. Le déploiement d’un service authentifié demanderait une nouvelle analyse de risques.
