# Note de triage | Authentifications du 12 octobre

**Décision proposée dans cet exercice** — Examiner en priorité le compte atlas. Conserver l’alerte boreal pour validation auprès du support. Les deux alertes ont le même score et appellent des décisions différentes.

| Compte | Observation dans le journal (UTC) | Contexte fourni par le scénario |
| --- | --- | --- |
| atlas | 5 échecs entre 08:00 et 08:04, réussite à 08:05 depuis 192.0.2.10 | Le titulaire fictif déclare qu’il était absent. |
| boreal | 5 échecs entre 09:00 et 09:04, réussite à 09:05 depuis 192.0.2.20 | Une demande fictive d’assistance pour un changement de mot de passe est ouverte au même moment. |
| cedre | Réussite à 10:00 sans échec préalable | Le scénario décrit un accès non autorisé avec des identifiants valides. |
| dune | Réussite à 11:00 sans échec préalable | Le scénario décrit une connexion ordinaire. |

**Suite de l’enquête.** Pour atlas, vérifier par un canal connu la déclaration du titulaire, puis corréler la réussite avec le facteur d’authentification, l’appareil et les actions de la session. Pour boreal, rapprocher l’heure et le compte du ticket d’assistance avant de clore l’alerte. Une adresse IP peut être partagée par plusieurs personnes.

## Évaluation sur les quatre réussites

La règle signale atlas et boreal. D’après les étiquettes fictives, atlas est un vrai positif, boreal un faux positif, cedre un faux négatif et dune un vrai négatif. La précision vaut 1/2 et le rappel vaut 1/2. Ces proportions décrivent uniquement les quatre cas construits pour l’exercice.

**Limite à expliquer en entretien.** Abaisser le seuil pourrait produire davantage d’alertes pour les utilisateurs qui se trompent de mot de passe. Cela laisserait toujours passer cedre, dont le journal contient zéro échec. Pour étudier ce cas, il faudrait une autre observation, par exemple la présence d’un appareil inhabituel, et un historique permettant de l’interpréter.
