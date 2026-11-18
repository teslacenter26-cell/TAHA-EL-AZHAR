# Sécurité et signalement
Signalez en privé un comportement inattendu à tahaelazhar0@gmail.com avec la révision, le composant, le résultat attendu et une observation minimale sur copie locale. Excluez les secrets et données personnelles. Attendez la coordination du correctif avant de rendre les détails publics.

Le modèle de menace couvre la publication accidentelle de fichiers locaux, les erreurs de données et les contenus interprétés par le navigateur. Le déploiement utilise une liste de fichiers autorisés, une politique CSP restrictive, une protection contre l’intégration dans un cadre, une politique de référent et des permissions limitées. HSTS concerne le site HTTPS effectivement déployé. La prévisualisation HTTP locale omet HSTS. Aucun cookie, compte ou endpoint de modification. Les contrôles CSRF de session sont donc hors périmètre.

Le calcul d’empreinte nécessite une référence fiable. Une correspondance atteste de l’identité des octets. L’analyseur d’en-têtes vérifie trois valeurs exactes et signale les doublons. Son résultat ne constitue pas un audit global. Limiter les essais aux données fictives et aux fichiers autorisés.

Les scans automatisés peuvent manquer des secrets et des défauts. En cas de secret publié, révoquer ou renouveler le secret auprès de son émetteur, puis examiner l’historique et les journaux d’accès.

Référence : [OWASP HTTP Headers Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Headers_Cheat_Sheet.html).
