# Prévisualisation et publication
Depuis portfolio, lancer `python preview.py`, puis ouvrir http://127.0.0.1:8000/. Arrêter avec Ctrl+C.

## Publication statique sous HTTPS
1. Ouvrir GitHub Actions et sélectionner le workflow « Portfolio défensif » pour le commit voulu de portfolio-cyber. Vérifier la réussite du job complet. Télécharger et décompresser l’artefact portfolio-public.
2. Créer un projet Cloudflare Pages en mode Direct Upload ou une nouvelle version du projet dédié. Charger le contenu décompressé. index.html, app.js, style.css, alertes.json et _headers doivent se trouver à la racine. Ne charger aucun autre dossier du dépôt.
3. Sur l’URL HTTPS fournie, vérifier la page, les deux alertes, la comparaison d’empreinte et le brouillon de courriel. Inspecter la réponse avec les outils réseau du navigateur, vérifier les valeurs de _headers, y compris HSTS. Contrôler l’absence d’autorisation CORS générique. Conserver la révision et l’URL validées.
4. En cas d’échec, restaurer la dernière version validée de ce site. Ne pas activer HSTS pour des sous-domaines non maîtrisés.

Sur un autre hébergeur, configurer les en-têtes dans sa configuration HTTP et vérifier la réponse réellement servie. L’outil preview.py est réservé à la machine locale. Le workflow prépare un artefact ; la publication requiert un hébergement configuré.

[Documentation Cloudflare Pages sur les en-têtes](https://developers.cloudflare.com/pages/configuration/headers/)
