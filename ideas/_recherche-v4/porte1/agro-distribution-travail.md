# Agro, voie distribution : fichier de travail (porte 1)

- Mission : 8 produits/équipements/logiciels alimentaires qui encaissent à l'étranger et sont absents ou mal servis en France.
- Date : 2026-11-02. Recherches web utilisées : 12/12 (budget atteint). Plus 6 WebFetch (hors budget).
- Note de périmètre : CLAUDE.md (modifié 2026-11-02) limite la recherche à l'énergie ; cette mission agro est explicitement demandée par le coordinateur, donc traitée telle quelle.
- Grep archives : mot-clé « vrac|consign|anti-gaspi|Too Good To Go|kombucha|sans alcool » présent dans _recherche-v3/marches/malservi-b2c.md (11 occurrences) et signaux/05-modeles-etrangers.md ; non lus (limite : un Grep). À vérifier avant de retenir une piste.
- Limite des outils : WebSearch rend un résumé, pas de texte brut ; les « citations » marquées (résumé) NE SONT PAS copiées telles quelles. Seules les citations marquées (verbatim) viennent d'une page ouverte.
- Preuves : 14. Domaines distincts : 13 (localline.co, scottishfinancialnews.com, cookoutnews.com, brasseurs-de-france.com, thegrocer.co.uk, tendancehotellerie.fr, hospitalitynet.org, cdn.paris.fr, hellopro.fr, whisky.fr, retailbrew.com, cagette.net, bahamastradeinfo.gov.bs/nbcnews/beverage-digest). Aucun domaine > 40 %.
- Statut : partiel. Manque : 3 prix publics par piste (sauf Local Line), chiffres de CA vérifiés à la source primaire, marge/commission de distribution (aucune trouvée), présence France confirmée pour Poppi, Olipop, Chomps, Local Line.

## Pistes retenues (8) et verdict rapide
| # | Piste | Argent encaissé ailleurs | Présence FR | Verdict |
|---|-------|--------------------------|-------------|---------|
| 1 | Soda prébiotique US (Poppi, Olipop) | oui, très fort | non trouvée | écart réel, mais barrière réglementaire (allégation) et accès à la marque via PepsiCo |
| 2 | Meat sticks US (Chomps) | oui, fort | non trouvée | import viande US : contraintes sanitaires UE [HYPOTHÈSE, non sourcée] |
| 3 | Bière sans alcool US (Athletic Brewing) | oui | déjà importée (LMDW) | contre-preuve : canal pris |
| 4 | Local Line (commande en ligne producteurs) | prix publics oui, CA non | non trouvée | écart possible mais concurrents FR (Cagette.net) |
| 5 | Winnow (anti-gaspi IA cuisines) | levées + clients | non confirmée | à clarifier ; concurrents FR (Orbisk, Kikléo) |
| 6 | Vytal (emballages réutilisables) | levée 10 M$ | déjà en France | contre-preuve |
| 7 | Ooni (fours à pizza) | 208 M£ en 2021 | déjà vendu en France | contre-preuve |
| 8 | Armoires de maturation Dry Ager | prix en France | distributeurs FR existent | contre-preuve |

## Preuves

### AGRO-01 : Poppi racheté 1,95 Md$ par PepsiCo
- Acteur / marché : Poppi (soda prébiotique, États-Unis), grande distribution
- Type : argent dépensé (acquisition)
- Source : https://www.nbcnews.com/business/business-news/pepsico-buys-prebiotic-soda-brand-poppi-nearly-2-billion-rcna196693 (extrait de recherche, date : 2025-03)
- Citation : (résumé) PepsiCo a accepté d'acheter Poppi pour environ 1,95 Md$ ; clôture mai 2025.
- Chiffres : 1,95 Md$ prix, 1,65 Md$ net d'avantages fiscaux ; CA ~500 M$ en 2024 selon un blog citant Fortune (confiance faible, non vérifié).
- Ce que ça dit pour nous : la demande US est prouvée ; une acquisition seule ne prouve pas un modèle exportable (règle CLAUDE.md).

### AGRO-02 : Poppi au Royaume-Uni sans allégation « prébiotique »
- Acteur / marché : Poppi, distribué par Carlsberg Britvic au UK, Tesco
- Type : contre-preuve (barrière réglementaire UE/UK)
- Source : https://www.thegrocer.co.uk/news/poppi-ditches-prebiotic-claim-for-uk-soda-launch/715934.article (ouverte, date : 2026-03-03)
- Citation : (résumé) 3 g de fibres par canette, trop peu ; « prébiotique » exige une allégation autorisée (12 g d'inuline de chicorée par portion).
- Chiffres : 4 références lancées ; prix non indiqué.
- Ce que ça dit pour nous : la marque a déjà choisi un grand distributeur en Europe ; en France, positionnement « riche en fibres » seulement, et PepsiCo contrôle l'accès : peu de place pour un agent indépendant.

### AGRO-03 : Olipop valorisé 1,85 Md$
- Acteur / marché : Olipop (US)
- Type : argent dépensé (levée, signal faible)
- Source : https://siliconvalleyinvestclub.com/fr/2025/02/18/olipop-raises-50-million-at-a-1-85-billion-valuation/ (extrait de recherche, date : 2025-02-18)
- Citation : (titre) « Olipop lève 50 millions de dollars pour une valorisation de 1.85 milliard de dollars »
- Chiffres : CA 400-450 M$ estimé début 2025 (source secondaire, confiance faible). Aucune arrivée en France ni en Europe trouvée.
- Ce que ça dit pour nous : une levée seule ne prouve pas le modèle ; présence FR non vérifiée.

### AGRO-04 : Bière sans alcool, France, fédération
- Acteur / marché : Brasseurs de France, marché français (grande distribution)
- Type : tendance (institutionnelle/fédération)
- Source : https://brasseurs-de-france.com/wp-content/uploads/2026/02/CP-eco-marche-bilan-2025-03022026.pdf (ouverte, date : 2026-02-03)
- Citation : « il représente désormais près de 6 % des volumes en grande distribution » (verbatim selon l'outil de lecture)
- Chiffres : +11,5 % en grande distribution en 2025 (volume ou valeur non précisé) ; 40 % des brasseurs interrogés produisent du sans alcool.
- Ce que ça dit pour nous : France seulement. Marché en croissance, mais dominé localement (Kronenbourg 60,4 % hors panachés selon son propre communiqué, extrait de recherche) : fort concentration.

### AGRO-05 : Athletic Brewing déjà importé en France
- Acteur / marché : Athletic Brewing (US), importée par LMDW
- Type : contre-preuve
- Source : https://www.whisky.fr/en/athletic-brewing-company-run-wild-unitaire.html (extrait de recherche, date inconnue)
- Citation : (résumé) « brand imported and distributed in France by LMDW » (formulation rapportée, non vérifiée mot à mot)
- Chiffres : > 90 M$ de CA en 2023 selon son PDG, via Brewbound/Komo (extrait de recherche ; page Brewbound en 403).
- Ce que ça dit pour nous : l'import exclusif est déjà pris par un acteur établi ; piste fermée pour cette marque.

### AGRO-06 : Chomps, snacks de viande
- Acteur / marché : Chomps (US)
- Type : argent dépensé
- Source : https://www.retailbrew.com/stories/2026/03/10/how-chomps-is-pitching-meat-sticks-for-breakfast (extrait de recherche, date : 2026-03-10)
- Citation : (résumé) CA +124 % en 2025 selon un dirigeant ; aucun montant donné.
- Chiffres : « près de 1 Md$ » (Bloomberg Law, titre de mai 2025, extrait) ; ~900 M$ (agrégateur, confiance faible). Aucune donnée Europe.
- Ce que ça dit pour nous : succès US réel, mais aucun signe d'export ; contraintes sanitaires d'import de viande hors UE non vérifiées [HYPOTHÈSE].

### AGRO-07 : Local Line, prix publics pour producteurs
- Acteur / marché : Local Line (Canada), SaaS de vente directe pour fermes
- Type : argent dépensé (prix publics) ; clients payants non chiffrés
- Source : https://localline.co/pricing (ouverte, date : 2026-11-02)
- Citation : (résumé) pas de commissions ni frais d'installation ; essai gratuit de 7 jours.
- Chiffres : Core 109 $/mois (87 $ en annuel), Premium 199 $ (159 $), Ultimate 399 $ (319 $) ; paiement carte 2,5-2,9 % + 0,30 $. Facturation en EUR possible. Nombre de fermes clientes : non indiqué.
- Ce que ça dit pour nous : 3 prix publics OK. Mais un revendeur n'a pas de commission connue [HYPOTHÈSE : à négocier] et la page ne prouve pas de clients payants.

### AGRO-08 : Cagette.net, concurrent français de Local Line
- Acteur / marché : Cagette.net, logiciel de vente directe, France
- Type : contre-preuve
- Source : https://www.cagette.net/wp-content/uploads/2024/03/Presentation-proposition-1.pdf (extrait de recherche, date : 2024-03)
- Citation : (résumé) 1000 producteurs actifs et 6 M€ de ventes prévues en 2024.
- Chiffres : tarif logiciel non trouvé ; formation à 206 € HT (2024).
- Ce que ça dit pour nous : le besoin est déjà servi, probablement à bas prix ; 6 M€ de ventes pour 1000 producteurs = faible revenu par client.

### AGRO-09 : Winnow, clients et levée
- Acteur / marché : Winnow (UK), IA anti-gaspillage en cuisines pro
- Type : argent dépensé (financement, signal faible)
- Source : https://www.hospitalitynet.org/news/4095500/ai-pioneer-winnow-raises-a-combined-20m-to-lead-the-global-fight-against-food-waste (ouverte, date : 2019-10-17)
- Citation : « adopted by more than 1,000 sites globally » (verbatim selon l'outil de lecture)
- Chiffres : 12 M$ série B + 8 M$ prêt BEI ; profil actuel : « 3500+ kitchens » (non daté) ; CA Dealroom 10-50 M$ (confiance faible). Aucune mention de la France.
- Ce que ça dit pour nous : le marché existe, mais le fournisseur vend en direct ; des concurrents français (Orbisk, Kikléo) existent (extrait de recherche, journaldespalaces.com, sudradio.fr).

### AGRO-10 : Vytal, emballages réutilisables en France
- Acteur / marché : Vytal (Allemagne), restauration à emporter
- Type : argent dépensé (levée) + obligation (loi AGEC)
- Source : https://www.tendancehotellerie.fr/articles-breves/communique-de-presse/17204-article/la-solution-d-emballages-reutilisables-vytal-conclut-une-serie-a-de-10-m (ouverte, date : 2022-03-17)
- Citation : « plus de 3 millions d’emballages jetables » remplacés (verbatim selon l'outil de lecture)
- Chiffres : série A 10 M$ ; > 250 000 utilisateurs ; bureau à Paris.
- Ce que ça dit pour nous : déjà en France (contre-preuve pour une voie distribution).

### AGRO-11 : Vytal, prix publics à Paris
- Acteur / marché : Vytal France
- Type : argent dépensé (prix)
- Source : https://cdn.paris.fr/paris/2024/04/12/annexe_2_guide_consigne-SsGS.pdf (extrait de recherche, date : 2024-04-12)
- Citation : (résumé) Formule Liberté 0 € d'abonnement + 0,15 € par contenant et par usage ; 0,10-0,30 € selon contenant.
- Chiffres : formule à 29 €/mois non rattachée sûrement à Vytal (Pyxo possible) : à ne pas utiliser.
- Ce que ça dit pour nous : revenu par client très bas, peu de marge pour un intermédiaire.

### AGRO-12 : Ooni, déjà en France
- Acteur / marché : Ooni (UK), fours à pizza
- Type : contre-preuve
- Source : https://scottishfinancialnews.com/articles/ooni-on-fire-as-it-posts-record-ps208m-turnover (extrait de recherche, date : 2022)
- Citation : (résumé) CA de 57,2 M£ (2020) à 208 M£ (2021), +264 %.
- Chiffres : 2023 : 194 M$, -24 % (cookoutnews.com, source secondaire). Vendu en France (galaxus.fr, Ooni cite la France comme grand marché ; extrait).
- Ce que ça dit pour nous : argent prouvé mais marque déjà distribuée ; fournisseur en direct.

### AGRO-13 : Dry Ager, distributeurs français existants
- Acteur / marché : Dry Ager (Allemagne), armoires de maturation
- Type : contre-preuve
- Source : https://www.hellopro.fr/armoire-de-maturation-ou-de-sechage-2-portes-type-de-porte-pleine-ref-mature2pnew-12-2018997-12515855-produit.html (extrait de recherche, date inconnue)
- Citation : (résumé) armoire 2 portes pleines annoncée 12 200 € HT ; autre guide : usage domestique dès ~2000 €.
- Chiffres : revendeurs cités : Politec, West Equipements Alimentaires. 3 prix publics : non réunis.
- Ce que ça dit pour nous : canal déjà occupé par des revendeurs d'équipement pro.

### AGRO-14 : Kronenbourg sur le sans alcool
- Acteur / marché : Brasseries Kronenbourg, France
- Type : contre-preuve (concentration)
- Source : https://www.kronenbourg.com/media/25jpben3/cp-brasseries-kronenbourg-anime-le-dry-january-janvier-2026.pdf (extrait de recherche, date : 2026-01)
- Citation : (résumé) sans alcool = 5,7 % du marché bière, +12,8 % en volume sur 10 mois 2025 ; part Kronenbourg 60,4 %.
- Chiffres : communiqué d'un acteur, à prendre avec prudence.
- Ce que ça dit pour nous : la concentration dépasse le seuil de 40 % ; seul un angle de niche (marques importées, restauration) serait crédible.

## Sources non lues
- https://www.brewbound.com/news/athletic-brewing-posts-biggest-dollar-growth-year-heading-into-2025-launches-athletic-january-campaign : 403.
- Bloomberg Law (Chomps) : non ouvert, probable mur payant.
- Pages Pappers/Societe.com non tentées : API entreprises non utilisée faute de budget d'étapes ciblées.
- Aucun appel à l'API recherche-entreprises (nombre de cibles : artisans de bouche, épiceries, restaurants) : manque pour la taille du segment.
