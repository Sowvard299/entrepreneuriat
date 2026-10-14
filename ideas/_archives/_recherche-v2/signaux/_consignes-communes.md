# Consignes communes aux 6 chercheurs (phase 1)

## Mission générale
Une équipe de 6 étudiants en master marketing (Paris / Île-de-France, budget < 5 000 €, aucun développeur, temps partiel cette année) cherche UNE entreprise à lancer en reprenant un modèle qui existe déjà et qui se vend, et en le faisant mieux (meilleur service, meilleur marketing, cible négligée, meilleur prix ou zone mal servie). L'innovation n'est pas requise : la preuve que des clients paient déjà passe avant l'originalité. Tous secteurs confondus, B2C et B2B, services, produits physiques et logiciels.

Le premier marché est Paris et la petite couronne (75, 92, 93, 94), puis l'Île-de-France, puis la France pour les offres 100 % en ligne.

## Règles de preuve (non négociables)
- Chaque signal : URL, date de la source, citation courte (15 mots maximum, entre « »), type de signal.
- Types de signal, du plus fort au plus faible : **argent dépensé** > **recherche active** (de solution) > **plainte** > **obligation réglementaire** > **tendance**.
- Un modèle « qui marche » se prouve par des clients payants identifiables : chiffre d'affaires publié (Pappers, Societe.com, presse), nombre de clients, avis nombreux et récents, réseau qui ouvre des unités. Une levée de fonds seule ne prouve rien.
- Sources de préférence de moins de 24 mois (après octobre 2024). Indique la date ; si elle est introuvable, écris « date inconnue ».
- AUCUN chiffre inventé. Toute donnée sans source est marquée [HYPOTHÈSE].
- Si une source contredit un modèle, garde-la et dis-le.
- Ne rends jamais une page que tu n'as pas réellement ouverte ou dont tu n'as pas vu l'extrait : pas d'URL devinée.

## Règles de fonctionnement
- Budget : environ 25 recherches web (WebSearch, mode "standard") au maximum. Privilégie l'ouverture directe (WebFetch) des pages utiles : pages Trustpilot, fiches Google, pages de prix, pages Pappers, articles.
- Écris dans TON fichier au fil de l'eau, par lots de 5 signaux (Write puis Edit pour ajouter), pour que le travail survive à une coupure. Si ton fichier existe déjà au démarrage, relis-le et continue sans doublon.
- Reddit, LinkedIn, Malt et Indeed bloquent souvent la lecture automatique. Essaie d'abord WebFetch (pour Reddit, `https://old.reddit.com/...`). Si c'est bloqué et que les outils du navigateur intégré (`mcp__Claude_Browser__*`) sont disponibles : crée TON propre onglet avec `tabs_create`, passe toujours ce `tabId`, lis avec `get_page_text`, ferme l'onglet à la fin. Ne te connecte à aucun compte, n'accepte que les cookies strictement nécessaires, ne remplis aucun formulaire. Liste en fin de fichier toute source qui n'a pas pu être lue.
- Pour compter les entreprises d'un secteur : API Recherche d'entreprises, par exemple
  `https://recherche-entreprises.api.gouv.fr/search?activite_principale=45.20A&departement=75&per_page=1` (le champ `total_results` donne le nombre). Filtres utiles : `activite_principale` (code NAF avec point), `departement`, `tranche_effectif_salarie`, `etat_administratif=A`.
- Ne lis pas les dossiers `ideas/_recherche/` et `ideas/recrutement-garages/` (ancienne itération, on repart de zéro).
- Tu ne poses aucune question : si une info manque, prends une hypothèse raisonnable et note-la.

## Format de chaque signal
```
### <ID> : <titre court>
- Modèle / acteur : <qui vend quoi>
- Secteur : <secteur> | Cible : B2C / B2B
- Type de signal : argent dépensé | recherche active | plainte | obligation réglementaire | tendance
- Source : <URL> (date : AAAA-MM-JJ ou « date inconnue »)
- Citation : « ... »
- Chiffres : <prix, nombre d'avis, note, CA, nombre de clients...>
- Angle d'amélioration : <ce qu'une petite équipe marketing pourrait faire mieux>
```

## Structure du fichier
1. En-tête : famille, date, nombre de recherches utilisées (à mettre à jour), nombre de signaux, nombre de sources distinctes (domaines).
2. Les signaux, numérotés.
3. À la fin : « Synthèse » = les 5 à 8 modèles les plus prometteurs de ta famille (un paragraphe court chacun : qui paie, combien, ce qui ne va pas, signaux qui le prouvent par ID), puis « Sources non lues ».

## Ce que tu rends au coordinateur
Un message court (250 mots maximum) : nombre de signaux, nombre de domaines distincts, secteurs couverts, et ta liste des modèles prometteurs (une ligne chacun). Le détail reste dans ton fichier.
