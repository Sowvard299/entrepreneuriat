# Marchés : lentilles 4 (modèle qui a grossi ailleurs) et 5 (demande en hausse) : fichier de travail

- Mission : Phase 0 de la recherche v3, 9 marchés français (C1 à C9). Lentille 4 : C1 à C5 et C9. Lentille 5 : C6 à C9.
- Date : 2026-10-13
- Recherches web utilisées : 25 / 25 (WebFetch et API gouvernementales en plus)
- Preuves : 39 (voir « Bilan des preuves » en fin de fichier)
- Domaines distincts : 35
- Google Trends : illisible (HTTP 429 en WebFetch). La colonne « demande » s'appuie donc sur Insee, Banque de France, Enedis (open data repris par des tiers), fédérations. Aucune courbe Trends n'a été lue.
- Convention : « ouverte » = page ouverte avec WebFetch ; « extrait de recherche » = résumé fourni par WebSearch, citation non copiée sur la page (le résumé n'est pas toujours verbatim, signalé « résumé »).

---

## C1 : DAF à temps partagé (CFO externalisé) pour PME de 10 à 249 salariés. Lentille 4 (États-Unis)

### Marché : PME de 10 à 249 salariés qui paient un directeur financier à temps partagé (2 à 4 jours par mois)
- Taille France : taille publiée non accessible (étude Xerfi payante, 1 500 € HT, C1-p1). Calcul bottom-up : 172 520 PME hors microentreprises (Insee, Ésane 2023, hors agriculture et finance, C1-p3) × pénétration × 24 000 €/an (2 jours/mois × 12 × 1 000 €, prix public 800 à 1 200 €/jour, C1-p2). À 1 % de pénétration [HYPOTHÈSE] : 41 M€ ; à 5 % [HYPOTHÈSE] : 207 M€. Aucune donnée de pénétration actuelle trouvée. Valeur, France.
- Croissance : non chiffrée. Xerfi parle seulement de « phase de structuration accélérée » (qualitatif). [HYPOTHÈSE] pas de source institutionnelle.
- Moteur de croissance : complexification réglementaire, digitalisation de la fonction finance, besoin d'agilité (cités par Xerfi, C1-p1). Pas de date d'obligation.
- Acteurs : fragmenté (spécialistes 2CFinance, RéférenceDAF, Acting, Bras Droit des Dirigeants ; cabinets d'expertise comptable Baker Tilly, Moore ; Malt, C1-p1). Part des 3 premiers : inconnue [HYPOTHÈSE : < 40 %]. Bras Droit des Dirigeants : plus de 200 cadres toutes fonctions confondues, CA franchisé visé 70 à 120 k€ sur 2 ans (C1-p5).
- Clients identifiables : 172 520 PME (Insee 2023, C1-p3). Sirene : à découper par NAF et tranche d'effectif, non fait.
- Demande : tendance 5 ans sur requêtes « DAF externalisé » : non lue (Trends bloqué). Indice : une franchise de cadres à temps partagé recrute activement en mars 2025 (C1-p5). Hausse probable, non prouvée.
- Modèle d'exécution : service à forte main-d'œuvre qualifiée (sous-traitants seniors, indépendants) ; une version outillée (tableau de bord de trésorerie) est possible.
- Modèle étranger : Pilot.com (États-Unis), comptabilité + CFO pour startups : CA estimé 27 M$ en juin 2024 (estimation Latka) contre 43 M$ fin 2022 (estimation Sacra) ; environ 1 000 clients (non daté) ; 218,3 M$ levés, valorisation 1,2 Md$ (C1-p4). État France : l'équivalent existe déjà (DAF à temps partagé, cabinets, franchise), donc modèle « pas mûr » seulement pour la version forfaitisée à bas prix.
- Contre-preuve (obligatoire) : le seul acteur étranger chiffré aurait vu son CA estimé baisser (43 M$ puis 27 M$, deux estimations de tiers, périmètres non garantis, C1-p4) ; les cabinets d'expertise comptable et les plateformes de freelances entrent sur le marché (C1-p1) ; un DAF crédible demande de l'expérience que l'équipe n'a pas.
- Seuils CLAUDE.md : taille ✔ (sous [HYPOTHÈSE] de pénétration 5 %) | croissance ✘ (non démontrée) | concentration ✔ (non vérifiée) | clients ✔
- Confiance : faible (taille par calcul bottom-up avec pénétration supposée, croissance sans source, preuve étrangère par estimations).

### C1-p1 : Xerfi, le marché de la DAF externalisée
- Acteur / marché : vendeur d'études, France, DAF externalisé
- Type : tendance
- Source : https://www.xerfi.com/presentationetude/Le-marche-des-DAF-externalises_SAE108 (date : 2026-03-04 « dernière mise à jour » ; page ouverte le 2026-10-13)
- Citation : « Le marché entre dans une phase de structuration accélérée. »
- Chiffres : étude 76 pages à 1 500 € HT ; taille 2025 et nombre de DAF externes non affichés ; acteurs cités : 2CFinance, RéférenceDAF, Acting, Bras Droit des Dirigeants, Baker Tilly, Moore France, BlueBirds, Malt
- Ce que ça dit pour nous : le marché existe et se structure, mais aucun chiffre libre ; confiance faible (vendeur de rapports).

### C1-p2 : Companeo, tarif d'un DAF à temps partagé
- Acteur / marché : comparateur de prestataires, DAF à temps partagé pour TPE/PME
- Type : argent dépensé (prix publics)
- Source : https://www.companeo.com/comptabilite-externalisee-expert-comptable/guide/directeur-financier-tpe-pme-temps-partage (date : mise à jour 2026-01-27 ; page ouverte)
- Citation : « entre 800 € et 1 200 € HT par jour »
- Chiffres : 800 à 1 200 € HT/jour en 2026 ; le blog Plateya (extrait de recherche) cite 8 000 à 12 000 €/mois pour 2 jours par semaine
- Ce que ça dit pour nous : panier annuel plausible de 15 à 25 k€ par PME à 2 jours/mois ; prix annoncé par des vendeurs, pas des factures.

### C1-p3 : Insee, nombre de PME en France
- Acteur / marché : statistique officielle, entreprises par catégorie
- Type : tendance (dénombrement)
- Source : https://www.insee.fr/fr/statistiques/2016091 (date : données 2023 ; extrait de recherche, page non ouverte)
- Citation : « 172 520 PME hors microentreprises » (résumé de recherche)
- Chiffres : 172 520 PME hors micro, 4 831 709 microentreprises, 7 296 ETI, 327 grandes entreprises (2023, hors agriculture, finance, assurance)
- Ce que ça dit pour nous : plus de 3 000 clients identifiables ; la catégorie PME de l'Insee ne se confond pas avec 10 à 249 salariés.

### C1-p4 : Pilot.com (États-Unis), compta et CFO pour startups
- Acteur / marché : Pilot, services comptables et CFO à distance, startups et petites entreprises (États-Unis)
- Type : argent dépensé (estimation de tiers, confiance faible) ; la levée seule ne prouve rien
- Source : https://getlatka.com/companies/pilot (date : estimations 2020 à 2026 ; page ouverte)
- Citation : « $1.2B valuation » (mars 2021, série C extension de 100 M$) ; la page ne publie pas de chiffres de l'entreprise
- Chiffres : CA estimé 10,5 M$ (août 2020), 43 M$ (décembre 2022, Sacra), 27 M$ (juin 2024, Latka) ; environ 1 000 clients (sans date) ; 218,3 M$ levés ; 416 salariés (avril 2026)
- Ce que ça dit pour nous : modèle payé à grande échelle aux États-Unis, mais la baisse estimée du CA invite à la prudence ; contre-preuve partielle.

### C1-p5 : Bras Droit des Dirigeants, franchise de cadres à temps partagé (France)
- Acteur / marché : réseau de franchise de DAF, DRH, directeurs commerciaux à temps partagé
- Type : argent dépensé (franchise)
- Source : https://www.observatoiredelafranchise.fr/creation-entreprise/franchise-bras-droit-des-dirigeants-4043.htm (date inconnue ; extrait de recherche)
- Citation : aucune citation verbatim disponible (résumé : droit d'entrée 25 000 € HT, redevance 7 %, CA visé 70 à 120 k€ sur 2 ans)
- Chiffres : plus de 200 cadres selon une fiche (nombres incohérents entre sources : 23, une centaine, 203) ; objectifs de CA, pas résultats audités
- Ce que ça dit pour nous : un franchiseur vit de ce modèle en France ; le CA par cadre (70 à 120 k€) est faible pour notre seuil de 500 k€ sans équipe.

---

## C2 : Assurance santé pour chiens et chats, payée par les propriétaires. Lentille 4 (Royaume-Uni, Suède)

### Marché : propriétaires de chiens et de chats qui paient une mutuelle ou assurance santé animale (environ 340 €/an pour un chien)
- Taille France : fourchette 140 à 600 M€/an de primes (valeur, France). Haut : 600 M€ de primes en 2025 selon HelloSafe, source de ses chiffres non précisée (C2-p2). Bas : bottom-up 1,1 M animaux assurés (C2-p2) × budget moyen 341 € chien / 256 € chat (Meilleurtaux 2024, C2-p3) ≈ 280 à 375 M€ ; l'article de L'Essentiel de l'Éco donne 69 M€ de CA pour SantéVet avec « environ la moitié » du marché, soit ~140 M€ (C2-p4). Les sources se contredisent ; retenir 280 M€ ordre de grandeur, confiance faible.
- Croissance : +8 %/an attendus jusqu'en 2030 (HelloSafe, comparateur, C2-p2) ; rapport de vendeur à 10,5 %/an non retenu (C2-p4) ; pénétration de 3 % à 5,3 % en 5 ans (MoneyVox, extrait, C2-p5). 2 sources, 0 institutionnelle : croissance non validée. Valeur.
- Moteur de croissance : hausse des frais vétérinaires (ONS UK : +9,1 % d'inflation vétérinaire en 2024, C2-p1), humanisation des animaux, rattrapage de pénétration. Pas d'obligation.
- Acteurs : SantéVet « environ la moitié du marché », 189 000 contrats (C2-p4) ; Dalma 65 000 animaux, +100 % en 2024 ; Bulle Bleue, Assur O'Poil, Carrefour Assurance (C2-p2). Part des 3 premiers : probablement > 60 % [HYPOTHÈSE à partir de « la moitié » pour un seul acteur].
- Clients identifiables : 22,6 à 26,5 millions de chiens et chats selon la source (Solly Azar 2024 ; Facco-Odoxa 2024, C2-p5). B2C.
- Demande : tendance 5 ans non lue (Trends bloqué). Pénétration en hausse : 3 % à 5,3 % (C2-p5).
- Modèle d'exécution : produit d'assurance porté par un assureur agréé ; l'équipe ne pourrait faire que du courtage ou de l'affiliation [HYPOTHÈSE : immatriculation Orias requise, article non vérifié].
- Modèle étranger : Royaume-Uni, 4,6 millions de propriétaires assurés en 2024 (+3 %), 1,23 Md£ de sinistres remboursés en 2024 (+4 %), 1,8 million de sinistres (ABI, C2-p1) ; pénétration 25 % UK, 91 % Suède, 20 % Allemagne contre 5 % France (HelloSafe, C2-p2, confiance faible). État France : marché lancé depuis 2005 avec 5 acteurs ou plus.
- Contre-preuve (obligatoire) : sur 5 ans la pénétration reste autour de 5 % ; la presse spécialisée l'appelle « un marché de niche qui peine à faire son trou » (titre Meilleurtaux, C2-p3) ; un leader pèse environ la moitié du marché et a levé 150 M€ (C2-p4) ; les sources donnent de 0,8 à 2,1 millions d'animaux assurés (C2-p5) ; l'inflation vétérinaire (9,1 % UK) pèse sur la rentabilité des assureurs.
- Seuils CLAUDE.md : taille ✔ (≥ 140 M€ dans tous les cas) | croissance ✘ (aucune source institutionnelle) | concentration ✘ (un acteur ~50 %) | clients ✔
- Confiance : faible.

### C2-p1 : ABI (Royaume-Uni), sinistres de l'assurance animaux 2024
- Acteur / marché : Association of British Insurers, assurance santé animale (Royaume-Uni)
- Type : argent dépensé
- Source : https://www.abi.org.uk/news/news-articles/2025/5/insurance-payouts-for-pawly-pets-top-1-billion-for-third-year-in-a-row/ (date : 2025-05 ; extrait de recherche, la page renvoie 403 à l'ouverture)
- Citation : « Insurance payouts for pawly pets top £1 billion for third year in a row » (titre de la page)
- Chiffres : 1,23 Md£ de sinistres payés en 2024 (+4 % sur 2023, +103 % sur 10 ans) ; 4,6 millions de propriétaires assurés (+3 %, +33 % vs 2019) ; 1,8 million de sinistres ; sinistre moyen 685 £ ; inflation vétérinaire ONS 9,1 % (résumé de recherche, données des seuls membres de l'ABI)
- Ce que ça dit pour nous : preuve forte d'un modèle massif ailleurs, source fédération professionnelle.

### C2-p2 : HelloSafe, baromètre de l'assurance animaux
- Acteur / marché : comparateur, assurance animaux France et pays comparés
- Type : tendance (confiance faible)
- Source : https://hellosafe.fr/assurance-animaux/marche (date : données jusqu'en juin 2025 ; page ouverte)
- Citation : « 600 millions € de primes annuelles en 2025 »
- Chiffres : 400 M€ en 2020 ; 1,1 million d'animaux assurés soit 5 % ; +8 %/an jusqu'en 2030 ; UK 25 %, Allemagne 20 %, Suède 91 % ; la page se contredit (80 millions d'animaux vs 22,6 millions) et n'attribue pas ses chiffres français
- Ce que ça dit pour nous : donne l'écart France/UK de pénétration, mais comparateur à intérêt commercial.

### C2-p3 : Meilleurtaux, assurance animaux : « un marché de niche »
- Acteur / marché : courtier-comparateur, assurance animaux France
- Type : contre-preuve
- Source : https://www.meilleurtaux.com/espace-presse/communiques-de-presse/assurance-animaux-un-marche-de-niche-qui-peine-a-faire-son-trou.html (date : 2024-09-25 ; page ouverte)
- Citation : « un taux d'équipement minime »
- Chiffres : 7 % des chiens et 4 % des chats assurés en 2024 (L'Argus de l'assurance) ; budget annuel moyen 341,52 € chien, 256 € chat, 228,48 € NAC
- Ce que ça dit pour nous : prix et pénétration, avec un titre qui contredit l'idée d'un marché en plein boom.

### C2-p4 : L'Essentiel de l'Éco, assurance santé animale
- Acteur / marché : presse économique, acteurs de l'assurance animaux
- Type : tendance
- Source : https://lessentieldeleco.fr/2175-assurance-sante-animale-la-france-a-la-traine-malgre-un-marche-en-plein-boom/ (date : 2025-05-16 ; page ouverte)
- Citation : « à partir de 5,44 euros par mois »
- Chiffres : SantéVet « environ la moitié » du marché, 189 000 contrats, 69 M€ de CA ; Dalma 20 M€ levés en mars 2025, 65 000 animaux, +100 % en 2024 ; marché 1,8 Md$ en 2023 vers 4,9 Md$ en 2033 (CAGR 10,51 %, rapport de vendeur, non retenu) ; l'article indique 35 % de propriétaires assurés, ce qui contredit toutes les autres sources
- Ce que ça dit pour nous : un leader domine ; l'article est peu fiable sur la pénétration.

### C2-p5 : Solly Azar, MoneyVox : nombre d'animaux assurés (sources divergentes)
- Acteur / marché : courtier (Solly Azar) et presse (MoneyVox), parc d'animaux et animaux assurés
- Type : contre-preuve (écarts entre sources)
- Source : https://groupe.sollyazar.com/sites/default/files/2024-06/CP_Solly%20Azar_FAMILY%20VET_GRAND%20PUBLIC_0.pdf (date : 2024-06 ; extrait de recherche) ; MoneyVox : https://www.moneyvox.fr/assurance/actualites/110075/faut-il-assurer-son-animal-de-compagnie-et-a-quel-prix-en-2026 (extrait de recherche, date 2026)
- Citation : aucune citation verbatim disponible (résumé : « moins de 8 % » assurés sur 22,6 millions de chiens et chats)
- Chiffres : 22,6 millions (Solly Azar) ou 26,5 millions (Facco-Odoxa mai 2024) ; assurés : 0,8 million (MoneyVox/Meilleurtaux), 1,1 million (HelloSafe), 2,1 millions (autre comparateur) ; 3 % il y a 5 ans contre 5,3 % (MoneyVox)
- Ce que ça dit pour nous : l'assiette réelle est incertaine à un facteur 2,5.

---

## C3 : Batterie de stockage pour maisons déjà équipées de panneaux solaires. Lentille 4 (Allemagne)

### Marché : propriétaires de maisons avec panneaux photovoltaïques qui achètent une batterie domestique installée (5 500 à 8 500 € pour 10 kWh)
- Taille France : bottom-up : 10 209 installations couplées à un stockage en 2025 (Enedis open data, repris par Hello Watt, C3-p3) × 4 000 à 9 000 € (fourchette de vendeurs, C3-p5) ≈ 41 à 92 M€ de ventes de batteries posées en 2025 [HYPOTHÈSE sur le prix moyen, sans source indépendante]. Valeur, France, une année.
- Croissance : part des installations avec stockage « sous 2 % » sur 2021-2024, 14 % au T4 2025 (Effy, résumé, C3-p4) ; 16 % au T1 2026 (4 922 projets, Hello Watt, résumé). Croissance estimée supérieure à +100 % en 2025-2026 sur une base faible. 2 sources (Hello Watt, Effy) qui reprennent toutes deux l'open data d'Enedis (gestionnaire de réseau, source quasi institutionnelle). Volume (nombre d'installations).
- Moteur de croissance : prix du rachat du surplus figé à 4 c€/kWh depuis 2025 (Effy, résumé), qui pousse à stocker plutôt qu'à revendre ; baisse du prix des batteries [HYPOTHÈSE]. Daté 2025-2026.
- Acteurs : installateurs de panneaux, très fragmentés ; part des 3 premiers inconnue [HYPOTHÈSE : < 40 %]. Non vérifié.
- Clients identifiables : 1 347 232 installations solaires en France fin 2025 (SDES, résumé de recherche, C3-p6), dont 1,7 % équipées d'une batterie (Hello Watt, T3 2025, périmètre Enedis). Soit environ 1,3 million de foyers prospects (B2C).
- Demande : tendance 5 ans non lue (Trends bloqué). Volumes : 10 209 batteries en 2025 (C3-p3).
- Modèle d'exécution : service à main-d'œuvre technique (pose, habilitation électrique, qualification RGE pour les aides) ; l'équipe peut vendre de la génération de contacts ou de la prescription à des installateurs plutôt que poser.
- Modèle étranger : Allemagne, 2 222 454 batteries en service fin 2025 et 526 172 nouvelles en 2025 (registre Marktstammdatenregister, pv magazine, C3-p1) ; France : 10 209 en 2025, soit environ 50 fois moins pour un parc solaire de 1,35 million d'installations (calcul : 526 172 / 10 209 ≈ 51).
- Contre-preuve (obligatoire) : en Allemagne la demande de batteries domestiques a baissé d'environ 8 % en 2025 (BSW-Solar, résumé, C3-p2) : le modèle y arrive à maturité. En France les raccordements ≤ 36 kWc ont chuté de 248 385 (2024) à 185 030 (2025), soit -26 % (C3-p3), et l'autoconsommation résidentielle a reculé de près de 40 à 60 % selon le trimestre (Effy, C3-p4) ; le vivier de nouvelles installations se contracte.
- Seuils CLAUDE.md : taille ✔ (41 à 92 M€, limite basse < 50 M€) | croissance ✔ (volume, source quasi institutionnelle Enedis ; valeur à confirmer) | concentration ✔ (non vérifiée) | clients ✔
- Confiance : moyenne pour les volumes, faible pour la valeur en euros.

### C3-p1 : pv magazine (Allemagne), parc de batteries fin 2025
- Acteur / marché : presse spécialisée, parc allemand de batteries de stockage (registre officiel Bundesnetzagentur)
- Type : argent dépensé (volume installé)
- Source : https://www.pv-magazine.de/2026/01/06/weniger-neue-batteriespeicher-2025-installiert-aber-mit-mehr-kapazitaet/ (date : 2026-01-06 ; page ouverte)
- Citation : « bis zum Jahresende 2.222.454 Speicher als in Betrieb verzeichnet waren »
- Chiffres : 2 222 454 batteries fin 2025 ; 526 172 nouvelles en 2025 ; environ 80 % de la capacité en batteries domestiques ; registre Marktstammdatenregister (erreurs possibles)
- Ce que ça dit pour nous : le marché allemand est 50 fois plus avancé en volume.

### C3-p2 : BSW-Solar via pv magazine : demande de batteries domestiques en baisse
- Acteur / marché : fédération allemande du solaire, batteries domestiques
- Type : contre-preuve
- Source : https://www.pv-magazine.de/2026/01/06/weniger-neue-batteriespeicher-2025-installiert-aber-mit-mehr-kapazitaet/ (date : 2026-01-06 ; extrait de recherche, passage BSW non retrouvé à l'ouverture)
- Citation : aucune citation verbatim disponible (résumé : demande de batteries domestiques en recul d'environ 8 % en 2025)
- Chiffres : BSW : environ 2,4 millions de batteries, près de 600 000 nouvelles en 2025 pour 6,5 GWh
- Ce que ça dit pour nous : l'Allemagne ralentit ; on copie un marché déjà mûr.

### C3-p3 : Hello Watt, chiffres du photovoltaïque T4 2025 (France)
- Acteur / marché : comparateur d'énergie, données Enedis open data, solaire résidentiel
- Type : argent dépensé (volume)
- Source : https://www.hellowatt.fr/blog/chiffres-t4-2025-photovoltaique/ (date : 2026-01-23 ; page ouverte)
- Citation : « 10 209 installations » couplées à un stockage en 2025
- Chiffres : 4 636 au seul T4 2025 ; raccordements ≤ 36 kWc : 248 385 en 2024, 185 030 en 2025 (-26 %) ; puissance +24 % (4 667 à 5 770 MW) ; source Open Data Enedis
- Ce que ça dit pour nous : volume de départ faible mais en accélération ; les installations globales baissent.

### C3-p4 : Effy, autoconsommation : installer moins pour stocker plus
- Acteur / marché : entreprise de rénovation énergétique, solaire résidentiel
- Type : tendance
- Source : https://www.effy.fr/flash-info/autoconsommation-solaire-residentielle-installer-moins-pour-stocker-plus (date : T4 2025 ; extrait de recherche, le résumé attribue les chiffres à Effy sans citer la page exacte parmi trois pages effy.fr listées)
- Citation : « installer moins pour stocker plus » (titre de la page)
- Chiffres : part du stockage sous 2 % en 2021-2024, 14 % des projets T4 2025 ; autoconsommation individuelle 20 000 projets T4 2025 vs 54 000 T4 2024 ; surplus racheté 4 c€/kWh
- Ce que ça dit pour nous : le stockage est le seul segment qui monte dans un marché solaire qui baisse.

### C3-p5 : Ankersolix, prix d'une batterie domestique installée
- Acteur / marché : fabricant de batteries, prix grand public France
- Type : argent dépensé (prix publics de vendeur, confiance faible)
- Source : https://www.ankersolix.com/fr/blogs/batterie-solaire/prix-installation-panneau-solaire-avec-batterie (date : 2026 ; extrait de recherche, page exacte du chiffre non confirmée)
- Citation : « entre 4 000 € et 9 000 € » (batterie de 5 à 10 kWh installée, résumé)
- Chiffres : un autre vendeur donne 5 500 à 8 500 € pour 10 kWh posée ; pas d'aide nationale dédiée aux batteries
- Ce que ça dit pour nous : panier de 4 à 9 k€, fourchette large, aucune source indépendante.

### C3-p6 : SDES, parc solaire français fin 2025
- Acteur / marché : service statistique du ministère de la Transition écologique, parc photovoltaïque
- Type : tendance (dénombrement)
- Source : résumé de recherche citant le SDES (URL SDES non ouverte)
- Citation : « 1 347 232 installations solaires » (résumé)
- Chiffres : 31,3 GW fin 2025 ; Enedis : 1 202 670 installations et 28,3 GW
- Ce que ça dit pour nous : 1,2 à 1,35 million de foyers déjà équipés, liste de prospects mais pas de liste nominative.

---

## C4 : Logiciel de devis, planning et facturation pour TPE de services techniques à domicile (hors gros œuvre). Lentille 4 (États-Unis)

### Marché : paysagistes, chauffagistes-climaticiens, couvreurs (et électriciens) de 1 à 49 salariés qui paient un abonnement de gestion d'interventions (39 à 109 €/mois)
- Taille France : bottom-up. Entreprises employeuses de 1 à 49 salariés, API Recherche d'entreprises le 2026-10-13 (C4-p4) : NAF 81.30Z (paysagistes) 15 541 ; 43.22B (chauffage, climatisation) 12 413 ; 43.91B (couverture) 8 738 ; soit 36 692. Électriciens 43.21A : au moins 20 358 (tranche 20-49 salariés non obtenue). × 828 €/an (offre « Croissance » d'Obat à 69 €/mois en paiement annuel, C4-p3) = 30,4 M€ sans électriciens, au moins 47,2 M€ avec. Exclut les entreprises sans salarié (requête API en échec, non comptées) et les autres métiers. Valeur, France, potentiel total (SAM), pas le marché actuel.
- Croissance : non chiffrée pour la France [HYPOTHÈSE : pas de série trouvée]. Étranger : ServiceTitan +24 % de CA sur son exercice clos le 2026-01-31 (C4-p1).
- Moteur de croissance : numérisation des TPE ; facture électronique obligatoire en France [HYPOTHÈSE : échéances 2026-2027 à vérifier sur economie.gouv.fr, non ouvert].
- Acteurs : Obat revendique plus de 21 000 pros du bâtiment (C4-p3) ; autres éditeurs non chiffrés. Part des 3 premiers : inconnue.
- Clients identifiables : 36 692 à 57 050 entreprises employeuses (Sirene via API, NAF ci-dessus, 1 à 49 salariés, France entière, état actif, 2026-10-13).
- Demande : tendance 5 ans non lue (Trends bloqué).
- Modèle d'exécution : logiciel. Besoin d'un associé tech (ou no-code, ou revente en marque blanche) ; SaaS vertical copié d'un modèle américain, signalé.
- Modèle étranger : ServiceTitan (États-Unis) : 961,0 M$ de CA, +24 %, environ 10 800 clients actifs, 1,11 Md$ visé pour l'exercice 2027 (C4-p1, dépôt SEC). Jobber (Canada) : 150 M$ de CA estimé en 2023, plus de 100 000 entreprises (C4-p2). État France : Obat et d'autres servent déjà le bâtiment ; les métiers non-BTP (paysage, piscine, entretien) restent à vérifier [HYPOTHÈSE].
- Contre-preuve (obligatoire) : Obat a déjà plus de 21 000 clients à 39-109 €/mois (C4-p3) : le modèle n'est pas immature en France pour le bâtiment ; le SAM bottom-up reste autour de 30 à 47 M€, sous le seuil de 50 M€ sans élargissement ; le client moyen de ServiceTitan est grand (~89 k$ de CA par client, calcul 961 M$ / 10 800, périmètre incluant les paiements), pas la TPE française.
- Seuils CLAUDE.md : taille ✘ (30 à 47 M€, élargissable) | croissance ✘ (non sourcée en France) | concentration ✔ (non vérifiée) | clients ✔
- Confiance : moyenne pour les comptages, faible pour la croissance.

### C4-p1 : ServiceTitan, résultats de l'exercice 2026
- Acteur / marché : éditeur de logiciel pour entreprises de services à domicile (États-Unis), société cotée
- Type : argent dépensé
- Source : https://finviz.com/news/337029/servicetitan-announces-fiscal-fourth-quarter-and-full-fiscal-year-2026-financial-results (date : 2026-03-12 ; extrait de recherche) ; pièce SEC 8-K : https://www.sec.gov/Archives/edgar/data/1638826/000163882626000009/ttan-ex99_1.htm (extrait de recherche)
- Citation : aucune citation verbatim disponible (résumé : revenu total 961,0 M$, +24 %)
- Chiffres : 961,0 M$ de CA contre 771,9 M$ ; environ 10 800 clients actifs contre 9 500 ; rétention nette de dollars > 110 % ; volume de transactions 82,1 Md$ ; prévision 2027 : 1 110 à 1 120 M$
- Ce que ça dit pour nous : preuve forte d'un logiciel vertical payé et récurrent aux États-Unis ; cible plus grosse que nos TPE.

### C4-p2 : Jobber, logiciel pour petites entreprises de services
- Acteur / marché : Jobber, gestion d'interventions pour petites entreprises de services à domicile
- Type : argent dépensé (estimation de tiers, confiance faible)
- Source : https://sacra.com/c/jobber (date : estimation 2023 ; extrait de recherche)
- Citation : aucune citation verbatim disponible (résumé : 150 M$ de CA estimé en 2023, +50 %)
- Chiffres : 100 000+ entreprises (revendiqué par Jobber) ; cœur de cible sous 20 salariés ; 237,5 M$ levés
- Ce que ça dit pour nous : le modèle TPE existe ailleurs à grande échelle, mais le CA est une estimation payante.

### C4-p3 : Obat, tarifs et clients (France)
- Acteur / marché : Obat, logiciel de devis et facturation pour artisans du bâtiment
- Type : argent dépensé
- Source : https://www.obat.fr/tarifs (date : consultée le 2026-10-13 ; page ouverte)
- Citation : « Plus de 21 000 pros du bâtiment nous font confiance »
- Chiffres : offre Pro 39 €/mois, Croissance 69 €/mois, Booster 109 €/mois HT en paiement annuel (artisan seul et TPE/PME)
- Ce que ça dit pour nous : le prix et le nombre de payeurs existent en France ; contre-preuve de « marché immature » pour le BTP.

### C4-p4 : API Recherche d'entreprises, comptage des TPE de services techniques
- Acteur / marché : base Sirene, entreprises actives par NAF et tranche d'effectif
- Type : tendance (dénombrement officiel)
- Source : https://recherche-entreprises.api.gouv.fr/search?activite_principale=81.30Z&tranche_effectif_salarie=01&etat_administratif=A&per_page=1 (date : 2026-10-13 ; réponse lue)
- Citation : « "total_results":7215 » (81.30Z, 1-2 salariés)
- Chiffres : 81.30Z : 7 215 (1-2) + 4 379 (3-5) + 2 070 (6-9) + 1 272 (10-19) + 605 (20-49) = 15 541 ; 43.22B : 5 583 + 3 086 + 1 671 + 1 379 + 694 = 12 413 ; 43.91B : 3 758 + 2 526 + 1 285 + 842 + 327 = 8 738 ; 43.21A : 10 000 (plafond, tranche 1-2) + 5 631 + 2 750 + 1 977 = au moins 20 358 ; les requêtes sans salarié ont échoué
- Ce que ça dit pour nous : liste gratuite constructible, plus de 3 000 clients identifiables.

---

## C5 : Programme de santé mentale pour les salariés de PME (accompagnement psychologique payé par l'employeur). Lentille 4 (États-Unis)

### Marché : PME et TPE qui paient un service d'écoute, de consultations et de prévention de la santé mentale pour leurs salariés
- Taille France : non établie. Aucun prix par salarié ni budget employeur trouvé [HYPOTHÈSE à construire : nombre de salariés de PME × prix par salarié/an]. Contexte : 22 % des salariés, soit 6 millions, en mauvaise santé mentale (Qualisocial-Ipsos 2026, C5-p3). Valeur : inconnue.
- Croissance : non chiffrée. 0 source institutionnelle.
- Moteur de croissance : santé mentale « grande cause nationale 2025 » (FrenchWeb, extrait) et Charte « Santé mentale et emploi » d'août 2025, volontaire (C5-p5). Pas d'obligation datée nouvelle trouvée.
- Acteurs : Teale (10 M€ série A, 2023), Moka.care (15 M€ série A, 2022) en France (C5-p2) ; Spring Health, Lyra aux États-Unis (C5-p1). Parts : inconnues.
- Clients identifiables : 172 520 PME hors microentreprises (Insee 2023, C1-p3) ; comptage Sirene non fait.
- Demande : tendance 5 ans non lue. Besoin exprimé : 48 % des dirigeants de TPE/PME veulent des guides pratiques ; plus de 8 sur 10 ont mis en place des temps d'échange mais 41 % des salariés les reconnaissent (AG2R La Mondiale, septembre 2026, C5-p4).
- Modèle d'exécution : service outillé (application) avec des psychologues salariés ou partenaires ; activité réglementée côté praticiens [HYPOTHÈSE : l'équipe ne pourrait être que revendeur ou intégrateur].
- Modèle étranger : Spring Health : « More than 170 million people worldwide have access » (sans date), valorisation 3,3 Md$ (série E 100 M$) ; clients nommés : Microsoft, Target, Pfizer (C5-p1). CA non publié ; les pages de CA de Lyra trouvées sont incohérentes (410 M$ ou 235 M$ selon l'agrégateur, rejetées). État France : Teale et Moka.care vendent surtout à des grands groupes (Sanofi, SNCF, Carrefour), la cible PME paraît moins servie [HYPOTHÈSE].
- Contre-preuve (obligatoire) : l'état de santé mentale s'est amélioré de 3 points en 2026 (C5-p3) ; aucun prix ni budget employeur n'est public ; la preuve étrangère repose sur des levées et des auto-déclarations, sans CA audité.
- Seuils CLAUDE.md : taille ✘ (non démontrée) | croissance ✘ (non démontrée) | concentration ✔ (fragmenté, non vérifié) | clients ✔
- Confiance : faible.

### C5-p1 : Spring Health (États-Unis), page de présentation
- Acteur / marché : plateforme de santé mentale vendue aux employeurs
- Type : argent dépensé (auto-déclaré) ; la levée seule ne prouve rien
- Source : https://www.springhealth.com/about-us (date : pied de page © 2026 ; page ouverte)
- Citation : « More than 170 million people worldwide have access to Spring Health »
- Chiffres : valorisation 3,3 Md$ après une série E de 100 M$ (titre de presse affiché) ; clients cités : Microsoft, Target, Coca-Cola, Pfizer ; CA non publié
- Ce que ça dit pour nous : modèle payé par de grands employeurs aux États-Unis ; pas d'information sur les petites entreprises.

### C5-p2 : Teale et Moka.care (France), levées de fonds et clients
- Acteur / marché : start-ups de santé mentale au travail, clients grands comptes
- Type : argent dépensé (levées, clients cités) ; la levée seule ne prouve rien
- Source : https://www.frenchweb.fr/serie-a-teale-leve-10-millions-deuros-pour-aider-les-entreprises-a-accompagner-leurs-collaborateurs-en-burn-out/444776 (date : 2023 ; extrait de recherche)
- Citation : « Parmi ses premiers clients, TEALE compte Sanofi, SNCF, Carrefour »
- Chiffres : Teale 10 M€ (série A, 2023) ; Moka.care 15 M€ (série A, mai 2022) ; aucun CA
- Ce que ça dit pour nous : l'équivalent français existe déjà et vise les grands groupes.

### C5-p3 : Qualisocial-Ipsos 2026 sur la santé mentale des salariés
- Acteur / marché : baromètre salariés (Qualisocial, Ipsos), via Éditions Tissot
- Type : tendance / contre-preuve
- Source : https://www.editions-tissot.fr/actualite/sante-securite/sante-mentale-des-salaries-en-2026-une-amelioration-globale-mais-des-disparites-persistantes (date : 2026 ; extrait de recherche)
- Citation : aucune citation verbatim disponible (résumé : 22 % des salariés, soit 6 millions, en mauvaise santé mentale)
- Chiffres : -3 points vs 2025 ; 16 à 18 % avant la crise sanitaire ; 83 % des salariés ayant un plan de prévention complet disent leur santé améliorée (édition 2025)
- Ce que ça dit pour nous : besoin large, mais en légère amélioration.

### C5-p4 : AG2R La Mondiale, baromètre des dirigeants de TPE/PME
- Acteur / marché : groupe de protection sociale, dirigeants de petites entreprises
- Type : plainte / recherche active (besoin déclaré)
- Source : https://presse.ag2rlamondiale.fr/download-pdf/6a9fb36d6e107e57a00d84d2 (date : 2026-09 ; extrait de recherche)
- Citation : aucune citation verbatim disponible (résumé : 48 % des dirigeants souhaitent des guides pratiques)
- Chiffres : plus de 300 dirigeants et 1 000 salariés interrogés (Ipsos bva) ; 41 % des salariés reconnaissent les dispositifs
- Ce que ça dit pour nous : un besoin d'outils pratiques existe, aucun budget n'est chiffré.

### C5-p5 : Charte « Santé mentale et emploi » (août 2025)
- Acteur / marché : pouvoirs publics et Alliance pour la santé mentale, employeurs
- Type : tendance (non réglementaire)
- Source : https://pro.apicil.com/sante/sante-mentale-au-travail-charte/ (date : 2025-08 ; extrait de recherche)
- Citation : aucune citation verbatim disponible (résumé : signataires engagés sur quatre piliers en trois ans)
- Chiffres : adhésion volontaire
- Ce que ça dit pour nous : un moteur de sensibilisation, pas une obligation.

---

## C6 : Recouvrement amiable de factures impayées pour TPE/PME. Lentille 5 (demande)

### Marché : TPE/PME qui paient un prestataire pour relancer et recouvrer leurs factures clients (10 à 15 % du montant recouvré)
- Taille France : près de 600 M€ de CA pour plus de 400 spécialistes (Xerfi, recouvrement pour compte de tiers, B2B et B2C mêlés, date inconnue, C6-p2). Valeur, France. Confiance faible.
- Croissance : non démontrée. Défaillances : 68 564 en 2025, +3,5 % après +17,7 % en 2024 (Banque de France via Crédit Agricole) ; Altares 69 957, +3,1 % (C6-p4) ; mais les délais de paiement baissent de 1,5 jour en 2024 et les retards sont de 13,4 jours fin 2025 (Banque de France, C6-p1). 2 sources dont 1 institutionnelle : demande de relance stable à haute, pas de croissance de marché démontrée.
- Moteur de croissance : tension de trésorerie des PME : 13 Md€ de trésorerie supplémentaire sans retards de paiement (Observatoire des délais de paiement, rapport publié le 2026-09-24, C6-p1). Pas d'obligation datée.
- Acteurs : plus de 400 acteurs, mais une dizaine (Intrum, DSO, EOS Credirec, Hoist...) détiendraient plus de 85 % du marché (Que Choisir, date inconnue, C6-p3). Part des 3 premiers : non publiée.
- Clients identifiables : 172 520 PME hors micro et 4,83 millions de microentreprises (Insee 2023, C1-p3).
- Demande : 69 957 défaillances en 2025 (Altares, record), +3,1 %. Requêtes non lues.
- Modèle d'exécution : service outillé (relances automatisées + appels) rémunéré à la commission ; les logiciels de credit management permettent déjà d'internaliser (Xerfi, C6-p2).
- Contre-preuve (obligatoire) : concentration à plus de 85 % pour une dizaine d'acteurs (C6-p3) ; délais de paiement en baisse, part d'entreprises payant sans retard en hausse de 2 points pour la 4e année (C6-p1) ; les clients externalisent « avec parcimonie » (Xerfi, résumé) ; fintech et experts-comptables entrent sur le marché.
- Seuils CLAUDE.md : taille ✔ (600 M€, confiance faible) | croissance ✘ | concentration ✘ | clients ✔
- Confiance : faible.

### C6-p1 : Banque de France, Observatoire des délais de paiement, rapport 2025
- Acteur / marché : institution, délais de paiement des entreprises
- Type : tendance / contre-preuve
- Source : https://www.banque-france.fr/fr/communiques-de-presse/le-rapport-annuel-2025-de-lobservatoire-des-delais-de-paiement-des-resultats-contrastes-selon-les (date : 2026-09-24 ; page ouverte)
- Citation : « les PME et les microentreprises auraient disposé de 13 milliards d’euros de trésorerie supplémentaire »
- Chiffres : délais clients et fournisseurs -1,5 jour (2024) ; retards 13,4 jours fin 2025 ; part payant sans retard +2 points pour la 4e année ; 54,2 % d'anomalies relevées par la DGCCRF ; 1 290 entreprises dégradées par la Banque de France pour comportement de paiement
- Ce que ça dit pour nous : la douleur est réelle (13 Md€) mais elle diminue.

### C6-p2 : Xerfi, le marché du recouvrement
- Acteur / marché : vendeur d'études, recouvrement pour compte de tiers
- Type : tendance (confiance faible)
- Source : https://www.xerfi.com/presentationetude/Le-marche-du-recouvrement_ABF115 (date inconnue ; extrait de recherche)
- Citation : aucune citation verbatim disponible (résumé : plus de 400 spécialistes, près de 600 M€ de CA)
- Chiffres : honoraires 10 à 15 % du montant recouvré ; crédit interentreprises environ 800 Md€ ; près de 60 Md€ de créances perdues par an ; Figec (membres seulement, via data.gouv) : près de 9 millions de créances, 6,5 Md€ de valeur faciale
- Ce que ça dit pour nous : un prix par commission et un secteur déjà consolidé.

### C6-p3 : Que Choisir, enquête sur les sociétés de recouvrement
- Acteur / marché : presse consommateurs, concentration du recouvrement
- Type : contre-preuve
- Source : https://www.quechoisir.org/enquete-societes-de-recouvrement-les-dessous-de-l-industrie-de-la-dette-n25632 (date inconnue ; extrait de recherche)
- Citation : aucune citation verbatim disponible (résumé : une dizaine de poids lourds dominent plus de 85 % du marché)
- Chiffres : Intrum, DSO, EOS Credirec, MCS, Hoist, Nemo, Concilian
- Ce que ça dit pour nous : concentration élevée, mais l'enquête porte surtout sur la dette des particuliers [HYPOTHÈSE].

### C6-p4 : Défaillances d'entreprises 2025 (Altares, Banque de France)
- Acteur / marché : cabinet privé Altares et Banque de France, défaillances en France
- Type : tendance
- Source : https://www.altares.com/wp-content/uploads/CP-ALTARES-DEFAILLANCES-T4-BILAN-2025.pdf (date : début 2026 ; extrait de recherche) ; https://www.journaldeleconomie.fr/entreprises-70000-defaillances-france-2025/ (extrait de recherche)
- Citation : aucune citation verbatim disponible (résumé : 69 957 procédures, +3,1 %, nouveau record)
- Chiffres : Banque de France : 68 564 défaillances (+3,5 %, après +17,7 % en 2024), 92 % de microentreprises ; création record de 1 165 813 entreprises (Insee)
- Ce que ça dit pour nous : plus d'impayés potentiels, mais la hausse se stabilise.

### C6-p5 : Altares, délais de paiement France-Europe 1er semestre 2025
- Acteur / marché : cabinet privé, délais de paiement
- Type : plainte / contre-preuve (écart avec l'observatoire)
- Source : https://www.altares.com/wp-content/uploads/ALTARES_Etude-Delais-de-Paiement-France-Europe_1er-semestre-2025-CP250918.pdf (date : 2025-09-18 ; extrait de recherche)
- Citation : aucune citation verbatim disponible (résumé : retard de 14,1 jours en 2025, +2 jours en 2 ans)
- Chiffres : « pire trajectoire d'Europe » selon Altares ; l'observatoire public indique 13,4 jours et une baisse en 2024
- Ce que ça dit pour nous : les deux sources divergent sur le sens de l'évolution.

---

## C7 : Soutien scolaire (cours particuliers et en ligne) payé par les familles. Lentille 5 (demande)

### Marché : familles de collégiens et lycéens qui paient des cours de soutien (environ 1 500 €/an et par enfant)
- Taille France : plus de 2 Md€ de CA pour plus d'un million d'élèves sur 12 millions (Économie Matin, janvier 2023, C7-p1) ; 2,5 Md€ d'après une étude du Centre d'analyse stratégique (données de 2011-2013, C7-p2). Valeur, France. Environ 80 % non déclaré. Confiance faible (données anciennes).
- Croissance : +2 %/an (Économie Matin) à +4 %/an (prévision Xerfi), et +5 %/an avant 2020 puis -11,5 % en 2020 (Xerfi, C7-p3). 0 source institutionnelle récente. Valeur.
- Moteur de croissance : crédit d'impôt de 50 % pour les cours à domicile ; hors confinement, cours à distance non éligibles (Familles de France, résumé de recherche). Pas d'obligation.
- Acteurs : réseaux de franchise [HYPOTHÈSE, noms non lus] ; Les Sherpas : 40 000 familles et 4 000 professeurs (communiqué, novembre 2025, C7-p4). Part des 3 premiers : inconnue.
- Clients identifiables : plus d'un million d'élèves utilisateurs (C7-p1) ; foyers B2C ≫ 100 000.
- Demande : tendance 5 ans non lue. Marché « parvenu à maturité » (titre Observatoire de la franchise, C7-p2).
- Modèle d'exécution : service à forte main-d'œuvre (professeurs indépendants) ou plateforme de mise en relation (piège : attirer offre et demande en même temps).
- Contre-preuve (obligatoire) : l'Observatoire de la franchise titre « Le soutien scolaire, un marché parvenu à maturité » ; croissance de 2 à 4 % seulement ; chiffres de taille anciens.
- Seuils CLAUDE.md : taille ✔ | croissance ✘ | concentration ✔ (80 % non déclaré, non vérifié) | clients ✔
- Confiance : faible.

### C7-p1 : Économie Matin, état des lieux du soutien scolaire
- Acteur / marché : presse économique, soutien scolaire en France
- Type : tendance
- Source : https://www.economiematin.fr/?p=93356 (date : 2023-01 ; extrait de recherche)
- Citation : aucune citation verbatim disponible (résumé : plus de 2 Md€ de CA, plus d'un million d'élèves)
- Chiffres : +2 %/an ; 12 millions d'élèves au total
- Ce que ça dit pour nous : taille correcte, croissance faible.

### C7-p2 : CAS (via Groupe Réussite) et Observatoire de la franchise : budget des familles et maturité
- Acteur / marché : service du Premier ministre (CAS), observatoire de franchise
- Type : tendance / contre-preuve
- Source : https://groupe-reussite.fr/ressources/cp-france-premier-marche-soutien-scolaire-en-europe/ (date inconnue ; extrait de recherche) ; https://www.observatoiredelafranchise.fr/dossier-franchise/le-soutien-scolaire-un-marche-parvenu-a-maturite-115.htm (date inconnue ; extrait de recherche)
- Citation : « Le soutien scolaire, un marché parvenu à maturité » (titre d'après l'adresse de la page)
- Chiffres : CAS : 40 heures par an et par enfant, 1 500 € par ménage avant crédit d'impôt, 2,5 Md€, environ 80 % non déclaré ; Xerfi : 30 à 40 €/heure
- Ce que ça dit pour nous : budget familial connu, marché mûr.

### C7-p3 : Xerfi, le soutien scolaire et la crise
- Acteur / marché : vendeur d'études, soutien scolaire
- Type : tendance (confiance faible)
- Source : https://www.xerfi.com/blog/le-marche-du-soutien-scolaire-durablement-impacte-par-la-crise-_1155 (date : 2021-05-05 ; extrait de recherche)
- Citation : aucune citation verbatim disponible (résumé : activité -11,5 % en 2020 après plus de 5 %/an depuis 2013)
- Chiffres : voir ci-dessus
- Ce que ça dit pour nous : la croissance passée dépassait 5 %/an, mais ancienne.

### C7-p4 : Les Sherpas, soutien scolaire
- Acteur / marché : Les Sherpas, soutien scolaire à domicile avec professeurs certifiés
- Type : argent dépensé (auto-déclaré)
- Source : https://help.sherpas.com/fr/docs/les-sherpas-reinvente-soutien-scolaire.pdf (date : novembre 2025 selon la recherche ; extrait de recherche)
- Citation : aucune citation verbatim disponible (résumé : 40 000 familles accompagnées, 4 000 professeurs certifiés)
- Chiffres : aucun CA
- Ce que ça dit pour nous : un acteur récent atteint 40 000 familles, donc des familles paient.

---

## C8 : Appareils électroniques reconditionnés (smartphones, ordinateurs). Lentille 5 (demande)

### Marché : consommateurs et petites entreprises qui achètent un smartphone ou un ordinateur reconditionné
- Taille France : non établie en euros. Part : le reconditionné pèse 18,3 % du marché français « global » et environ un quart des ventes de smartphones en 2025 (Back Market, source non indépendante, C8-p1) ; ancien : 2 millions de smartphones reconditionnés vendus en France (GfK, année inconnue, 7 % des ventes, C8-p2). Taille en euros [HYPOTHÈSE à construire].
- Croissance : stable en France en 2025 vs 2024 contre +2 points en Espagne et +2,4 points au Royaume-Uni (Back Market, C8-p1). Monde : volume de transactions de Back Market +32 % (mondial, pas la France).
- Moteur de croissance : prix et sensibilité environnementale (48 % des Français ont déjà acheté du reconditionné, enquête Back Market) ; aides publiques [HYPOTHÈSE, non vérifiées].
- Acteurs : Back Market (CA 440 M€ en 2025 dans le monde, 18 millions de clients, 17 pays, rentable en 2025), Recommerce, reBuy en Allemagne (C8-p1, C8-p2). Part des 3 premiers : inconnue, probablement > 40 % [HYPOTHÈSE].
- Clients identifiables : B2C ≫ 100 000 ; B2B : 172 520 PME (C1-p3).
- Demande : tendance 5 ans non lue.
- Modèle d'exécution : produit (stock, approvisionnement, garantie) ; actifs lourds.
- Contre-preuve (obligatoire) : marché français « mature » et stable en 2025 selon le leader lui-même (C8-p1) ; le leader est déjà rentable.
- Seuils CLAUDE.md : taille ✘ (non établie) | croissance ✘ | concentration ✘ (probable) | clients ✔
- Confiance : faible.

### C8-p1 : Back Market, premier bénéfice 2025
- Acteur / marché : Back Market, place de marché de reconditionné
- Type : argent dépensé
- Source : https://www.maddyness.com/2026/02/04/back-market-devient-a-son-tour-rentable-pour-la-premiere-fois/ (date : 2026-02-04 ; extrait de recherche)
- Citation : aucune citation verbatim disponible (résumé : 18,3 % du marché français, stable vs 2024)
- Chiffres : CA 440 M€, 3 Md€ de transactions (+32 %), 17 pays, 18 millions de clients (mondial)
- Ce que ça dit pour nous : la France est le marché le plus avancé et il ne progresse plus.

### C8-p2 : FrenchWeb, Back Market face à Recommerce et reBuy
- Acteur / marché : presse start-up, reconditionné
- Type : tendance
- Source : https://www.frenchweb.fr/41-millions-deuros-pour-back-market-qui-veut-faire-face-a-recommerce-et-lallemand-lallemand-rebuy/328044 (date inconnue ; extrait de recherche)
- Citation : aucune citation verbatim disponible (résumé : 2 millions de smartphones reconditionnés vendus, 7 % des ventes selon GfK)
- Chiffres : Recommerce 50 M€ levés, reBuy 21 M€
- Ce que ça dit pour nous : chiffre ancien, ordre de grandeur uniquement.

---

## C9 : Séjours en plein air et chez l'habitant en nature (modèle Hipcamp). Lentilles 4 (États-Unis) et 5

### Marché : propriétaires de terrains, fermes et petits campings qui paient une commission ou un abonnement pour être réservés en ligne
- Taille France : non établie en euros. Volume : 147,6 millions de nuitées de camping d'avril à septembre 2025, contre 141,2 millions en 2024 et 126,3 millions en 2019 (Insee, repris par vacances-scolaires.com, C9-p2). Pas de prix moyen ni de CA publiés [HYPOTHÈSE à construire]. Volume.
- Croissance : +4,5 % de nuitées en 2025 vs 2024 et +16,9 % vs 2019 (calculs sur C9-p2) ; Nouvelle-Aquitaine +4,5 %, emplacements équipés +6,6 % (Insee Flash n° 138, C9-p1). 2 sources dont 1 institutionnelle. Volume, pas valeur.
- Moteur de croissance : hausse de la demande de vacances en plein air et des emplacements équipés (mobil-homes, chalets), plus des deux tiers des séjours (Insee, C9-p1).
- Acteurs : campings professionnels dominés par des groupes [HYPOTHÈSE, non lu]. Part des 3 premiers : inconnue.
- Clients identifiables : campings professionnels : comptage Sirene en échec (API en erreur le 2026-10-13) ; [HYPOTHÈSE].
- Demande : tendance 5 ans non lue ; États-Unis : plus de 200 % de hausse des recherches de lieux de camping à l'été 2024 (Hipcamp, auto-déclaré, C9-p3).
- Modèle d'exécution : plateforme de mise en relation (piège connu : attirer l'offre et la demande en même temps, cimetière v2) ; commissions.
- Modèle étranger : Hipcamp : 3,3 millions de nuits réservées sur un an (déclaré, C9-p3) ; aucun CA vérifiable. État France : équivalents éventuels [HYPOTHÈSE, non vérifié].
- Contre-preuve (obligatoire) : pas de prix ni de CA ; la preuve étrangère est auto-déclarée ; plateforme à deux faces sans plan d'acquisition ; saisonnalité forte (64 % des nuitées en juillet-août, titre de C9-p2).
- Seuils CLAUDE.md : taille ✘ (non établie) | croissance ✔ (volume +4,5 %/an, valeur inconnue) | concentration ✔ (non vérifiée) | clients ✘ (non comptés)
- Confiance : faible.

### C9-p1 : Insee Flash n° 138, campings en Nouvelle-Aquitaine
- Acteur / marché : Insee, fréquentation de l'hôtellerie de plein air
- Type : tendance
- Source : https://www.insee.fr/fr/statistiques/8983822 (date : 2026-04-28 ; page ouverte)
- Citation : « Avec 30,3 millions de nuitées en camping entre avril et septembre 2025 »
- Chiffres : +4,5 % sur un an ; emplacements équipés +6,6 % et plus des deux tiers des séjours ; emplacements nus +1,1 %
- Ce que ça dit pour nous : hausse officielle de la fréquentation, portée par les hébergements équipés.

### C9-p2 : vacances-scolaires.com, campings en 2025 d'après l'Insee
- Acteur / marché : site d'information, reprise de données Insee
- Type : tendance
- Source : https://vacances-scolaires.com/actualites/2026/09/25/campings-champions-des-vacances-scolaires-147-millions-de-nuitees-64-en-juillet-aout/ (date : 2026-09-25 ; extrait de recherche)
- Citation : « 147 millions de nuitées, 64 % en juillet-août » (titre)
- Chiffres : 147,6 millions (avril-septembre 2025) vs 141,2 millions (2024) vs 126,3 millions (2019)
- Ce que ça dit pour nous : record de fréquentation, mais saisonnier.

### C9-p3 : Hipcamp acquiert BookOutdoors
- Acteur / marché : Hipcamp, plateforme de réservation de camping sur terrains privés (États-Unis)
- Type : argent dépensé (auto-déclaré)
- Source : https://rv-pro.com/news/hipcamp-acquires-bookoutdoors/ (date : 2024 ; extrait de recherche)
- Citation : « more than 3.3 million individual nights outside » (résumé)
- Chiffres : plus de 200 % de hausse des recherches à l'été 2024 (déclaré) ; revenu par commissions, CA non publié
- Ce que ça dit pour nous : une demande existe aux États-Unis, mais aucun chiffre financier vérifiable.

---

## Sources non lues
- https://trends.google.fr/trends/explore (Google Trends) : HTTP 429, aucune courbe lue.
- https://www.abi.org.uk/news/news-articles/2025/5/insurance-payouts-for-pawly-pets-top-1-billion-for-third-year-in-a-row/ : 403, chiffres lus en extrait de recherche.
- https://www.santeclair.fr/fr/sites/santeclair_prod/files/2026-06/20260615_CP_PreventionEntreprise.pdf : PDF compressé illisible.
- https://fnhpa-pro.fr/wp-content/uploads/2026/04/FNHPA-Dossier-de-presse-2026_Final.pdf : PDF compressé illisible (nombre de campings et CA de la fédération non obtenus).
- Études Xerfi (DAF, recouvrement, soutien scolaire) : payantes, seulement les résumés.
- Pages SDES, rapport complet de l'ODP, Argus et FFA (assurance animaux) : non ouvertes, budget de recherches atteint.
- API Recherche d'entreprises : requêtes sans salarié (00, NN), NAF 55.30Z et tranches manquantes (43.21A 20-49, 43.22A, 43.32A 3-5) en échec ou limitées à 10 000 le 2026-10-13.
- reddit.com, pappers.fr, malt.fr, statista.com : non utilisés (bloqués ou payants).

## Bilan des preuves
- Marchés : 9 (C1 à C9). Preuves : 39 (C1 : 5 ; C2 : 5 ; C3 : 6 ; C4 : 4 ; C5 : 5 ; C6 : 5 ; C7 : 4 ; C8 : 2 ; C9 : 3). Seulement 12 pages ouvertes (C1-p1, C1-p2, C1-p4, C2-p2, C2-p3, C2-p4, C3-p1, C3-p3, C4-p3, C5-p1, C6-p1, C9-p1) ; les autres sont des extraits de recherche.
- Domaines distincts : 35 (xerfi.com, companeo.com, insee.fr, getlatka.com, observatoiredelafranchise.fr, abi.org.uk, hellosafe.fr, meilleurtaux.com, lessentieldeleco.fr, sollyazar.com, moneyvox.fr, pv-magazine.de, hellowatt.fr, effy.fr, ankersolix.com, finviz.com, sec.gov, sacra.com, obat.fr, recherche-entreprises.api.gouv.fr, springhealth.com, frenchweb.fr, editions-tissot.fr, presse.ag2rlamondiale.fr, pro.apicil.com, banque-france.fr, quechoisir.org, altares.com, journaldeleconomie.fr, economiematin.fr, groupe-reussite.fr, maddyness.com, rv-pro.com, vacances-scolaires.com, help.sherpas.com).
- Aucun domaine au-dessus de 40 % des preuves d'un marché ; C3, C5, C8, C9 n'ont qu'une source officielle de seconde main (Enedis, Bundesnetzagentur, Insee via tiers) ou aucune.
