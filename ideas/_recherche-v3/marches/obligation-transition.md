# Marchés v3, lentilles 1 (obligation datée) et 2 (transition en cours)

- Mission : cartographier 10 marchés français (client qui paie + dépense précise). Phase 0, chercheur A.
- Date : 2026-10-13 (session reprise après coupure API).
- Recherches web utilisées : 21 / 25 (plus WebFetch et API recherche-entreprises).
- Marchés : A1 à A10. Preuves : voir la fin de chaque fiche (IDs A1-p1...). 36 preuves, environ 30 domaines distincts (aucun domaine au-dessus de 40 % ; capeb.fr et avere-france.org sont les plus fréquents, 2 à 3 preuves chacun).
- Avertissement de méthode : certaines citations viennent du résumé que l'outil de recherche renvoie (marqué « ≈ résumé outil ») et pas du texte original de la page. Le vérificateur doit les rouvrir. Les chiffres « calcul » sont mes calculs, montrés. « [HYPOTHÈSE] » = non sourcé.
- Lentille 1 (obligation) : A1 facturation électronique, A2 décret tertiaire/BACS, A3 NIS2, A4 accessibilité numérique, A7 biodéchets pros.
- Lentille 2 (transition) : A5 ombrières de parkings, A6 rénovation énergétique des bailleurs, A8 recharge en copropriété, A9 adaptation du logement, A10 DPE collectif/travaux de copropriété.
- Sources bloquées rencontrées : economie.gouv.fr (403), siecledigital.fr (403), impots.gouv.fr (hôte non résolu), anil.org (connexion refusée sur 1 essai), PDF Anah/DREAL (texte compressé illisible).
- Limite de l'API Sirene : `total_results` plafonné à 10 000, donc comptage par département (somme des 100 départements, 4 DOM inclus, NAF 2008 telle qu'indexée). Les entreprises comptées incluent les micro-entrepreneurs (état administratif actif).

---

## A1. Facturation électronique obligatoire : TPE/PME qui paient une plateforme agréée ou un accompagnement (lentille 1)

- Taille France : non publiée de façon fiable. [HYPOTHÈSE] Les plateformes agréées (PA) étant souvent offertes dans les offres existantes (A1-p4), la dépense directe d'une TPE est proche de 0 € ; l'argent est chez les PME de 10 à 249 salariés (ERP, comptabilité) et chez les cabinets comptables. Aucun prix de PA sourcé : pas de calcul bottom-up possible.
- Croissance : non chiffrée. Moteur structurel daté plutôt que croissance mesurée (A1-p1, A1-p2). Valeur : inconnue.
- Moteur de croissance : réception obligatoire pour toutes les entreprises assujetties à la TVA au 1er septembre 2026 (déjà en vigueur) ; émission et e-reporting obligatoires pour PME, TPE et micro-entreprises au 1er septembre 2027 (A1-p1). Calendrier déjà reporté une fois (1er juillet 2024 puis 2026-2027, loi de finances 2024), mais confirmé et entré en vigueur le 1er septembre 2026.
- Acteurs : 101 plateformes agréées au 16 janvier 2026, 108 plus tard (A1-p3). Top 3 et parts : non établi.
- Clients identifiables : près de 10 M d'acteurs assujettis à la TVA selon Bercy (A1-p3), plus de 7 M selon le règlement d'usage de la marque PA (A1-p3). Seulement 600 000 SIREN avaient enregistré leur point de réception en avril 2026 (A1-p2). Comptage Sirene 69.20Z (experts-comptables, prescripteurs) : voir A1-p5.
- Demande : tendance 5 ans non mesurée (pas de Google Trends). Pic attendu autour de septembre 2027.
- Modèle d'exécution : logiciel (PA) ou service outillé (paramétrage + formation de TPE). La PA elle-même exige un agrément DGFiP : hors de portée de l'équipe. Un revendeur/conseil de PA existante reste possible.
- Contre-preuve (obligatoire) : PA gratuites ou incluses dans des offres existantes (Tiime, B2Brouter annonce une « plateforme gratuite ») ; 108 PA déjà agréées ; pas de sanction avant fin 2026 selon la presse. L'argent à capter est un accompagnement, pas un abonnement logiciel.
- Seuils CLAUDE.md : taille ? (non établie) | croissance ✔ (moteur daté 09/2027) | concentration ? | clients ✔
- Confiance : moyenne pour le moteur et le nombre de clients (source officielle) ; faible pour la taille.

### A1-p1 : calendrier officiel de la réforme
- Acteur / marché : État (DGE/DGFiP) ; toutes entreprises assujetties à la TVA
- Type : obligation
- Source : https://entreprendre.service-public.gouv.fr/actualites/A18953?lang=en (date : 2026-09-02, page ouverte, version anglaise)
- Citation : « all companies must be able to receive electronic invoices » (traduction anglaise de la page, ≈ non copiée du français)
- Chiffres : émission grandes entreprises/ETI au 1er sept 2026 ; PME et micro-entreprises au 1er sept 2027
- Ce que ça dit pour nous : le moteur est confirmé et daté par une source officielle ; la vague PME arrive en septembre 2027.

### A1-p2 : très peu d'entreprises prêtes en avril 2026
- Acteur / marché : Tiime (éditeur et PA), blog comptable
- Type : tendance (preuve d'un besoin non couvert)
- Source : https://blog.tiime.fr/facturation-electronique-la-dgfip-relance-les-entreprises-sans-plateforme-agreee (date : 2026-04-21, mise à jour 2026-08-04, page ouverte)
- Citation : « Dans cet email, l'administration fiscale invite ces structures à se mettre en conformité sans tarder. »
- Chiffres : sur près de 10 M d'entreprises assujetties, 600 000 SIREN avaient enregistré leur point de réception ; près de 6 M d'e-mails de relance envoyés par la DGFiP
- Ce que ça dit pour nous : des millions de TPE n'avaient encore rien fait au printemps 2026 ; reste à prouver qu'elles paieraient.

### A1-p3 : volume et nombre de plateformes
- Acteur / marché : ministère de l'Économie / DGFiP
- Type : tendance
- Source : https://www.economie.gouv.fr/node/3238965 (date : 2026-01-16 environ, extrait de recherche, page 403 à l'ouverture) et https://www.impots.gouv.fr/reglement-dusage-et-charte-dutilisation-de-la-marque-plateforme-agreee (extrait de recherche, date inconnue)
- Citation : « plus de 7 millions d'assujettis avec un volume de 2 milliards de factures » (≈ résumé outil)
- Chiffres : près de 10 M d'acteurs (Bercy) contre plus de 7 M (règlement d'usage) ; 101 PA le 16 janvier 2026, 108 ensuite
- Ce que ça dit pour nous : l'offre de plateformes est déjà saturée en nombre ; l'écart 7 à 10 M montre que le nombre exact de clients n'est pas fiable.

### A1-p4 : contre-preuve, la plateforme est offerte
- Acteur / marché : Tiime, B2Brouter
- Type : contre-preuve
- Source : https://blog.tiime.fr/facturation-electronique-la-dgfip-relance-les-entreprises-sans-plateforme-agreee (date : 2026-08-04) et https://www.b2brouter.net/fr/facture-electronique-calendrier/ (date : 2026-06-01, page ouverte)
- Citation : « incluse gratuitement dans toutes nos offres »
- Chiffres : 0 € pour la PA chez Tiime ; B2Brouter promeut une plateforme gratuite pour auto-entrepreneurs et TPE (affirmation du vendeur)
- Ce que ça dit pour nous : vendre « une plateforme » à une TPE est perdant ; seul un service (accompagnement, intégration) peut se facturer.

### A1-p5 : prescripteurs, experts-comptables (comptage Sirene)
- Acteur / marché : experts-comptables (NAF 69.20Z), prescripteurs naturels des TPE
- Type : tendance
- Source : https://recherche-entreprises.api.gouv.fr/search?activite_principale=69.20Z&etat_administratif=A (date : 2026-10-13, API ouverte)
- Citation : « total_results » (champ de l'API)
- Chiffres : 23 827 cabinets actifs (voir « Comptages API » en fin de fichier)
- Ce que ça dit pour nous : un canal indirect existe (les cabinets), mais il est aussi concurrent (ils vendent l'accompagnement).

---

## A2. Décret tertiaire et GTB/BACS : propriétaires et exploitants de bâtiments tertiaires de plus de 1 000 m² (lentille 1)

- Taille France : non publiée. Bottom-up impossible faute de prix sourcé (la page du prestataire Hayot ne publie aucun tarif, A2-p3). Illustration [HYPOTHÈSE] : 340 000 entités fonctionnelles (A2-p2) × 500 à 2 000 €/an de prestation = 170 à 680 M€/an ; fourchette de prix non sourcée, à ne pas utiliser pour décider.
- Croissance : non chiffrée. Moteur daté (A2-p1, A2-p2). Valeur ou volume : inconnu.
- Moteur de croissance : GTB (BACS) obligatoire pour les bâtiments tertiaires existants de plus de 70 kW au 1er janvier 2027 (plus de 290 kW au 1er janvier 2025) ; décret tertiaire : -40 % de consommation en 2030, -50 % en 2040, -60 % en 2050 ; déclaration OPERAT annuelle avant le 30 septembre ; amende de 7 500 € (personne morale) pour omission. Pas de report constaté du 1er janvier 2027 dans les sources trouvées (à confirmer sur Légifrance : non ouvert).
- Acteurs : non établi. Les intégrateurs GTB (industriels) et bureaux d'études sont nombreux ; top 3 inconnu.
- Clients identifiables : près de 340 000 EFA déclarées fin janvier 2026 (A2-p2) ; l'ADEME estime le taux de remplissage d'OPERAT à 50-60 % du parc assujetti. Seuil : 1 000 m² de surface de plancher.
- Demande : tendance 5 ans non mesurée.
- Modèle d'exécution : service outillé (déclaration OPERAT, plan d'actions) ; la GTB elle-même exige des installateurs (employeur/sous-traitance).
- Contre-preuve (obligatoire) : exemption si installation techniquement impossible ou retour sur investissement supérieur à 10 ans (A2-p1) ; sanctions peu visibles ; chiffres du parc contradictoires (surface 343 M m² à l'échéance contre 518 M m² avec déclarations tardives).
- Seuils CLAUDE.md : taille ? | croissance ✔ (moteur daté 01/2027 et trajectoire 2030) | concentration ? | clients ✔
- Confiance : moyenne pour clients et moteur ; faible pour la taille.

### A2-p1 : GTB obligatoire au 1er janvier 2027
- Acteur / marché : propriétaires/exploitants de bâtiments tertiaires avec chauffage/clim de plus de 70 kW
- Type : obligation
- Source : https://www.ffbatiment.fr/actualites-batiment/actualite-ba/batiments-tertiaires-installer-une-gtb-une-obligation-qui-s-etend (date : 2023-05-10, page ouverte, fédération professionnelle)
- Citation : « au 1er janvier 2027, si la puissance de l'équipement est de plus de 70 kW » (≈ résumé outil)
- Chiffres : 70 kW en 2027, 290 kW en 2025 ; exceptions si impossibilité technique ou ROI supérieur à 10 ans ; aucun nombre de bâtiments ni coût sur la page
- Ce que ça dit pour nous : l'échéance 2027 ouvre un parc de bâtiments moyens (70 à 290 kW) souvent exploités par des PME ; source datée de 2023, report possible non vérifié.

### A2-p2 : volume OPERAT et échéance 2026
- Acteur / marché : ADEME (plateforme OPERAT), assujettis au décret tertiaire
- Type : obligation
- Source : résultats de recherche « décret tertiaire OPERAT 2026 » (extrait de recherche, 2026-10-13 ; chiffres rapportés sans pouvoir rattacher la phrase à une des 9 pages listées, dont https://www.construires.fr/operat-declaration-consommations-energie-tertiaire/ et https://atee.fr/system/files/2025-10/251016_ATEE%20Tertiaire.pdf)
- Citation : « avant le 30 septembre 2026 sur la plateforme OPERAT de l'ADEME » (≈ résumé outil)
- Chiffres : 343 M m² déclarés et validés en 2024 ; près de 340 000 EFA, plus de 1,145 M déclarations (janvier 2026) ; remplissage 50-60 % du parc selon l'ADEME ; amende 7 500 €
- Ce que ça dit pour nous : près de la moitié du parc n'a pas encore déclaré, mais l'amende n'est pas prouvée comme appliquée.

### A2-p3 : contre-preuve, prix non publics
- Acteur / marché : Hayot Expertise (prestataire de déclaration OPERAT)
- Type : contre-preuve
- Source : https://hayot-expertise.fr/blog/decret-tertiaire-operat-obligations-echeances (date : 2025-11-20, page ouverte)
- Citation : « 1000 m² » (seuil cité sur la page ; aucun prix publié)
- Chiffres : aucun tarif ; une grille de prix « sur devis »
- Ce que ça dit pour nous : le marché se vend sur devis, on ne peut pas encore prouver l'argent dépensé ; à tester par appels.

---

## A3. Cybersécurité NIS2 : PME et ETI de 18 secteurs qui achètent audit et mise en conformité (lentille 1)

- Taille France : non publiée. Bottom-up [HYPOTHÈSE] : 15 000 entités (A3-p2) × 15 000 € (bas de la fourchette 15 000 à 120 000 € d'un cabinet de conseil, A3-p3) = 225 M€ en une seule fois, pas par an. Confiance faible : le chiffre d'entités est celui de l'ANSSI repris par des blogs, les prix viennent d'un seul cabinet.
- Croissance : non chiffrée. Moteur NON daté (loi bloquée, A3-p1).
- Moteur de croissance : transposition de la directive NIS2 par le projet de loi Résilience. Date limite européenne dépassée (17 octobre 2024) ; Sénat : adoption en première lecture le 12 mars 2025 ; Assemblée : examen prévu le 7 octobre 2026 de nouveau reporté (A3-p1). Les exigences techniques (décrets, référentiel) ne sont pas publiées ; environ 3 ans de mise en conformité après publication (extrait Legiscope).
- Acteurs : cabinets de conseil, prestataires PASSI, ESN ; top 3 non établi.
- Clients identifiables : environ 15 000 entités selon l'ANSSI (secondaire). Comptage Sirene des entreprises de 50 à 249 salariés : le résultat de l'API (94 645) est jugé peu fiable et n'est pas retenu.
- Demande : tendance 5 ans non mesurée.
- Modèle d'exécution : service à forte expertise (RSSI externalisé), non outillable sans compétence cyber que l'équipe n'a pas. Réserve : revente/orchestration.
- Contre-preuve (obligatoire) : loi toujours non adoptée en octobre 2026, texte reporté, saisine de la CJUE, blocage sur le chiffrement (A3-p1) ; le site officiel parle seulement de « milliers d'entités » et d'un référentiel non obligatoire par défaut (A3-p4).
- Seuils CLAUDE.md : taille ? (225 M€ hypothèse ponctuelle) | croissance ✘ (aucun moteur daté) | concentration ? | clients ✔ (15 000 B2B, source secondaire)
- Confiance : faible.

### A3-p1 : le texte est de nouveau reporté
- Acteur / marché : Assemblée nationale, projet de loi Résilience
- Type : contre-preuve
- Source : https://next.ink/brief-article/alleluia-la-transposition-de-nis2-est-enfin-a-lordre-du-jour-de-lassemblee-nationale/ (date : 2026-10-06, page ouverte)
- Citation : « J'ai bon espoir qu'on pourra réinscrire le texte d'ici quinze jours ou trois semaines »
- Chiffres : examen prévu le 7 octobre 2026 reporté le 6 octobre ; aucune date fixée
- Ce que ça dit pour nous : pas de calendrier d'obligation avant 2027-2029 au mieux ; un pari sur le vote.

### A3-p2 : nombre d'entités concernées
- Acteur / marché : ANSSI (via blogs juridiques)
- Type : obligation
- Source : https://www.legiscope.com/blog/transposition-nis2-france.html (date inconnue, extrait de recherche)
- Citation : « 15 000 entités environ concernées en France » (≈ résumé outil)
- Chiffres : 15 000 entités, 18 secteurs ; une source isolée dit 10 000 à 15 000
- Ce que ça dit pour nous : assez de clients pour le seuil de 3 000, mais le chiffre officiel n'est pas ouvert.

### A3-p3 : prix de conformité (confiance faible)
- Acteur / marché : cabinets de conseil cyber
- Type : argent dépensé (estimation vendeur, pas de transaction prouvée)
- Source : https://ayinedjimi-consultants.fr/articles/cout-mise-en-conformite-nis-2-budget-pme-2026 (date inconnue, extrait de recherche)
- Citation : « de 15 000 € à 120 000 € » (≈ résumé outil)
- Chiffres : 15 000 à 120 000 € de mise en conformité ; audit blanc 15 000 à 80 000 € ; audit de sécurité général de petite entreprise 3 000 à 25 000 € (éditeur cloud, Opsio)
- Ce que ça dit pour nous : ordres de grandeur d'un vendeur, pas des prix payés.

### A3-p4 : page officielle de l'ANSSI
- Acteur / marché : ANSSI, cyber.gouv.fr
- Type : contre-preuve
- Source : https://cyber.gouv.fr/la-directive-nis-2 (date : pas de date, dernière référence « Depuis le 17 mars 2026 », page ouverte)
- Citation : « des milliers d'entités qui concernent le quotidien des citoyens »
- Chiffres : aucun nombre d'entités ; référentiel ReCyF publié le 17 mars 2026, non obligatoire par défaut
- Ce que ça dit pour nous : la source officielle ne confirme ni le chiffre de 15 000 ni une échéance.

---

## A4. Accessibilité numérique (European Accessibility Act) : e-commerçants et services de plus de 10 salariés ou 2 M€ de CA qui paient audit et refonte (lentille 1)

- Taille France : non publiée. Aucun prix d'audit trouvé (A4-p1). Pas de calcul bottom-up possible.
- Croissance : non chiffrée. Moteur : obligation déjà en vigueur depuis le 28 juin 2025 (pas d'échéance future).
- Moteur de croissance : directive 2019/882, transposée en France (loi 2023-171 du 9 mars 2023, décret du 24 août 2026 d'après A4-p1, à vérifier sur Légifrance). Contrôles DGCCRF dès l'entrée en vigueur ; amende de 7 500 € par infraction (5e classe) ; Arcom jusqu'à 50 000 €. Décision de justice du 4 juin 2026 contre Carrefour (source unique, A4-p2).
- Acteurs : agences web, spécialistes RGAA/WCAG ; top 3 non établi.
- Clients identifiables : exemption pour les prestataires de services de moins de 10 personnes et de 2 M€ de CA maximum. Comptage Sirene NAF 47.91B (vente à distance sur catalogue spécialisé, proxy e-commerce) : 55 472 entreprises actives (API, 2026-10-13), dont la grande majorité sont des micro-entreprises donc exemptées [HYPOTHÈSE] ; part au-dessus du seuil non comptée.
- Demande : tendance 5 ans non mesurée.
- Modèle d'exécution : service outillé (audit + corrections), avec développement web : besoin d'un associé tech pour corriger les sites.
- Contre-preuve (obligatoire) : micro-entreprises exemptées ; la majorité du e-commerce français est exemptée ; les montants de sanction divergent selon les sources (un chiffre de 250 000 € « sans base en droit français » selon A4-p1) ; peu de contrôles prouvés hors décision Carrefour.
- Seuils CLAUDE.md : taille ? | croissance ✘ (obligation déjà en vigueur, pas de pic daté) | concentration ? | clients ? (55 000 en proxy, part non exemptée inconnue)
- Confiance : faible.

### A4-p1 : champ, seuils et sanctions
- Acteur / marché : agence web (Scroll), avocats
- Type : obligation
- Source : https://agence-scroll.com/blog/accessibilite-numerique-obligations-entreprises (date : décret du 24 août 2026 cité, page ouverte, blog d'agence)
- Citation : « 250 millions » (seuil de CA du régime de l'article 47 de la loi de 2005 ; texte français non copié intégralement)
- Chiffres : directive : exemption si moins de 10 personnes et 2 M€ de CA ; contravention de 5e classe de 7 500 € ; Arcom jusqu'à 50 000 € ; aucun prix d'audit
- Ce que ça dit pour nous : la cible légale existe, mais sans prix et sans date butoir à venir.

### A4-p2 : première décision de justice
- Acteur / marché : Carrefour France, associations apiDV et Droit Pluriel
- Type : obligation
- Source : https://www.degaullefleurance.com/en/actualites/digital-accessibility-new-obligations-for-the-private-sector/ (date inconnue, extrait de recherche)
- Citation : « un site de e-commerce ne peut pas être un peu accessible » (≈ résumé outil, source unique)
- Chiffres : tribunal judiciaire de Caen, 4 juin 2026, mise en conformité sous 6 mois sous astreinte
- Ce que ça dit pour nous : risque juridique réel pour les grands sites ; pas de signal pour les PME.

### A4-p3 : comptage Sirene e-commerce
- Acteur / marché : entreprises NAF 47.91B
- Type : tendance
- Source : https://recherche-entreprises.api.gouv.fr/search?activite_principale=47.91B&etat_administratif=A (date : 2026-10-13, API ouverte)
- Citation : « total_results » (champ API ; somme sur 100 départements = 55 472)
- Chiffres : 55 472 entreprises actives
- Ce que ça dit pour nous : le vivier brut est large, mais l'exemption micro-entreprise le réduit fortement.

---

## A5. Ombrières photovoltaïques obligatoires sur grands parkings (loi APER) : exploitants de parkings extérieurs de plus de 1 500 m² (lentille 2, transition énergétique + obligation)

- Taille France : non publiée. Périmètre : 21 000 magasins et centres commerciaux pour environ 70 M m² de parkings, selon la Fédération du commerce et de la distribution (A5-p2). Aucun prix de projet sourcé : bottom-up impossible.
- Croissance : non chiffrée. Moteur daté mais repoussable (A5-p1).
- Moteur de croissance : loi APER (loi 2023-175 du 10 mars 2023), article 40 : ombrières sur la moitié de la surface des parkings extérieurs de plus de 1 500 m². Décret du 13 novembre 2024 : 1er juillet 2026 pour les parkings de plus de 10 000 m², juillet 2028 pour ceux de 1 500 à 10 000 m². Report possible jusqu'en 2030 sous conditions techniques (loi du 26 novembre 2025, décret 2026-842 du 7 septembre 2026) (A5-p1).
- Acteurs : développeurs solaires nationaux et locaux ; top 3 non établi.
- Clients identifiables : 21 000 magasins/centres (FCD) ; en Manche, 902 parkings concernés sur 2 272 de plus de 1 500 m² (DDTM, A5-p3). Comptage Sirene des grandes surfaces alimentaires : non fait.
- Demande : tendance 5 ans non mesurée.
- Modèle d'exécution : produit/chantier lourd (investissement de plusieurs centaines de milliers d'euros par parking [HYPOTHÈSE]). Une mise en relation propriétaire-développeur serait un service léger, mais les développeurs financent déjà et prospectent.
- Contre-preuve (obligatoire) : report jusqu'en 2030 autorisé, exemption si le projet n'est pas viable économiquement ou si le parking est ombragé à plus de 50 % ; la grande distribution demande une réglementation « réaliste » (A5-p2) ; 10 à 15 % des parkings de plus de 10 000 m² déjà équipés ou en cours (A5-p4).
- Seuils CLAUDE.md : taille ? | croissance ✔ (obligation datée 2028, mais repoussable) | concentration ? | clients ✔ (21 000)
- Confiance : faible à moyenne.

### A5-p1 : calendrier et report
- Acteur / marché : propriétaires/exploitants de parkings
- Type : obligation
- Source : https://cms.law/en/fra/legal-updates/obligation-de-solarisation-des-parkings-exterieurs-les-conditions-du-report-des-echeances-precisees et https://www.weblex.fr/weblex-actualite/panneaux-photovoltaiques-et-equipement-des-parkings-un-delai-supplementaire (extrait de recherche, date 2026-09 environ)
- Citation : « le 1er juillet 2026 pour les parkings de plus de 10 000 m² et juillet 2028 » (≈ résumé outil)
- Chiffres : décret 2026-842 du 7 septembre 2026 ; six conditions cumulatives (rendement supérieur à 22 %, garantie de performance d'au moins 30 ans)
- Ce que ça dit pour nous : l'échéance existe mais se repousse en achetant des panneaux haut de gamme : un levier pour des acheteurs, pas pour un intermédiaire.

### A5-p2 : périmètre côté distribution
- Acteur / marché : Fédération du commerce et de la distribution (FCD)
- Type : tendance
- Source : https://www.connaissancedesenergies.org/afp/ombrieres-photovoltaiques-sur-les-parkings-la-grande-distribution-demande-une-reglementation-realiste-260702 (date : 2026-07-02 d'après l'URL, extrait de recherche)
- Citation : « la grande distribution demande une réglementation réaliste » (≈ titre de l'article)
- Chiffres : 21 000 magasins et centres commerciaux, environ 70 M m² de parkings
- Ce que ça dit pour nous : le secteur s'oppose à l'obligation ; les clients ne sont pas en demande.

### A5-p3 : comptage officiel local (Manche)
- Acteur / marché : DDTM de la Manche (État)
- Type : obligation
- Source : https://www.manche.gouv.fr/contenu/telechargement/58321/451970/file/Focus%20photovolta%C3%AFque.pdf (date inconnue, extrait de recherche)
- Citation : « 2272 parkings de plus de 1500 m² » (≈ résumé outil)
- Chiffres : 902 parkings concernés par l'obligation, environ 335 hectares, dans un seul département
- Ce que ça dit pour nous : source officielle sur l'ordre de grandeur local ; pas de comptage national.

### A5-p4 : équipement déjà engagé
- Acteur / marché : Idex (cabinet), cité par Le Journal des Entreprises
- Type : contre-preuve
- Source : https://www.lejournaldesentreprises.com/article/ombrieres-photovoltaiques-sur-les-parkings-la-grande-distribution-temporise-2146151 (date inconnue, extrait de recherche)
- Citation : « 10 à 15 % des parkings de plus de 10 000 m² seraient déjà équipés » (≈ résumé outil)
- Chiffres : 10 à 15 % équipés ou en cours
- Ce que ça dit pour nous : les gros parkings sont déjà pris par des développeurs ; reste le segment 1 500 à 10 000 m², échéance 2028.

---

## A6. Rénovation énergétique des bailleurs privés (interdiction de louer les logements F au 1er janvier 2028) (lentille 2, transition énergie + obligation)

- Taille France : aides Anah totales de 4,39 Md€ en 2025 (secondaire, A6-p3, tous dispositifs du parc privé, pas seulement les bailleurs) ; objectif 2026 d'au moins 120 000 rénovations d'ampleur (A6-p3). Taille de la dépense des bailleurs seuls : non publiée. Pas de bottom-up (pas de coût moyen de travaux sourcé).
- Croissance : non mesurable (le guichet a fermé du 31 décembre 2025 au 23 février 2026 faute de loi de finances).
- Moteur de croissance : logements classés G interdits à la location depuis le 1er janvier 2025 ; F au 1er janvier 2028 ; E en 2034 (loi Climat et résilience, 2021). 1,4 M de logements F en 2025 dont 720 000 dans le locatif privé (ONRE, A6-p1) ; 4,8 M de F et G au 1er janvier 2023 (ministère). Réforme du coefficient électricité au 1er janvier 2026 : environ 850 000 logements reclassés (A6-p1).
- Acteurs : très nombreux (artisans RGE, accompagnateurs Rénov', Hellio, etc.) ; top 3 non établi. Comptage Sirene NAF 43.29A (travaux d'isolation) : 8 797 entreprises actives.
- Clients identifiables : 720 000 logements F en locatif privé (propriétaires inconnus, un propriétaire peut en avoir plusieurs).
- Demande : tendance 5 ans non mesurée.
- Modèle d'exécution : service d'accompagnement outillé (audit + dossier d'aides) ou chantier (employeur). Marché déjà occupé par des plateformes de leads.
- Contre-preuve (obligatoire) : un projet de loi annoncé en avril 2026 viserait à remettre des passoires thermiques sur le marché locatif sous engagement de travaux (article de juillet 2026, non confirmé par une source institutionnelle) ; l'aide publique dépend de la loi de finances (fermeture de début 2026) ; les baux en cours ne sont pas rompus.
- Seuils CLAUDE.md : taille ✔ (périmètre trop large, à resserrer) | croissance ✔ (moteur daté 01/2028, instable) | concentration ✔ probable (très fragmenté, non prouvé) | clients ✔ (720 000 logements)
- Confiance : moyenne pour le moteur, faible pour la taille.

### A6-p1 : calendrier et volumes de logements F
- Acteur / marché : bailleurs privés ; ONRE (Observatoire national de la rénovation énergétique)
- Type : obligation
- Source : https://www.cpim.fr/dpe-2028-derniere-ligne-droite/ et https://www.construires.fr/dpe-interdiction-location-passoire-thermique/ (extrait de recherche, date 2026, chiffres ONRE rapportés)
- Citation : « 1,4 million de logements F en France en 2025, dont 720 000 » (≈ résumé outil)
- Chiffres : 720 000 F en locatif privé ; 850 000 logements reclassés par le coefficient électricité de 2026
- Ce que ça dit pour nous : un vivier de bailleurs identifiables ; source secondaire, ONRE non ouverte.

### A6-p2 : contre-preuve, assouplissement envisagé
- Acteur / marché : gouvernement, projet de loi annoncé en avril 2026
- Type : contre-preuve
- Source : https://www.manda.fr/ressources/articles/passoire-thermique-et-location-ce-quil-faut-savoir-pour-2025 (date : juillet 2026 d'après la recherche, extrait de recherche)
- Citation : « remettre sur le marché locatif les passoires thermiques » (≈ résumé outil, adoption non confirmée)
- Chiffres : aucun
- Ce que ça dit pour nous : l'échéance 2028 peut être assouplie, ce qui casserait l'urgence.

### A6-p3 : budget Anah et fermeture du guichet
- Acteur / marché : Anah (opérateur public), CAPEB
- Type : argent dépensé (aides publiques)
- Source : https://www.capeb.fr/actualites/budget-de-l-anah-2026-ou-en-sommes-nous (date : 2026-01-05, page ouverte, fédération professionnelle)
- Citation : « au moins 120 000 rénovations en maison individuelle et en copropriété »
- Chiffres : budget initial 2026 de près de 4,4 Md€ d'aides pour environ 350 000 logements ; guichet fermé depuis le 31 décembre 2025
- Ce que ça dit pour nous : l'argent public est massif, mais dépend d'un vote annuel.

---

## A7. Tri des biodéchets : restaurants, commerces alimentaires et cantines qui paient une collecte (lentille 1)

- Taille France : non publiée. Aucun prix mensuel fiable trouvé (A7-p2). Pas de calcul bottom-up.
- Croissance : non chiffrée. Moteur : obligation déjà en vigueur depuis le 1er janvier 2024.
- Moteur de croissance : article L.541-21-1 du code de l'environnement : tous les producteurs de biodéchets, sans seuil, depuis le 1er janvier 2024 (seuil de 5 tonnes/an en 2023) (A7-p1). Un décret n° 2026-433 du 2 juin 2026 aurait renforcé les sanctions (contravention de 3e classe), source unique non officielle (A7-p3).
- Acteurs : opérateurs de collecte et valorisation (groupes de déchets, associations, start-up) ; top 3 non établi.
- Clients identifiables : 114 659 établissements de restauration traditionnelle actifs (NAF 56.10A, API, micro inclus), plus cantines, traiteurs et commerces alimentaires non comptés.
- Demande : tendance 5 ans non mesurée.
- Modèle d'exécution : service à forte logistique (collecte, véhicules) : exclu pour l'équipe ; seule une offre de coordination/abonnement sans flotte est envisageable.
- Contre-preuve (obligatoire) : les collectivités ne sont pas tenues de collecter les biodéchets des professionnels (A7-p2) ; un article indique l'absence d'amende au 1er janvier 2024 ; aucun bilan de contrôle de l'ADEME trouvé.
- Seuils CLAUDE.md : taille ? | croissance ✘ (obligation déjà en vigueur) | concentration ? | clients ✔ (voir comptage)
- Confiance : faible.

### A7-p1 : obligation sans seuil
- Acteur / marché : tous producteurs de biodéchets
- Type : obligation
- Source : https://www.info.gouv.fr/actualite/le-tri-des-dechets-alimentaires-generalise-au-31-decembre-2023 (date inconnue, extrait de recherche, site gouvernemental)
- Citation : « Le tri des déchets alimentaires généralisé au 31 décembre 2023 » (titre de la page)
- Chiffres : l'ADEME estime 2 à 6 heures par semaine de tri par établissement (résumé outil)
- Ce que ça dit pour nous : obligation officielle, mais déjà en vigueur : pas de pic futur.

### A7-p2 : contre-preuve, collecte non garantie, pas de prix
- Acteur / marché : collectivités, restaurateurs
- Type : contre-preuve
- Source : https://coban-atlantique.fr/wp-content/uploads/2025/03/Guide-pratique-de-la-Redevance-Speciale-2025.pdf et https://www.juritravail.com/Actualite/tri-a-la-source-des-biodechets-quelles-obligations-pour-les-entreprises-depuis-janvier-2024/Id/377002 (extrait de recherche, 2025)
- Citation : « La collectivité n'a donc aucune obligation de collecter vos biodéchets » (≈ résumé outil)
- Chiffres : aucun prix mensuel pour un restaurant
- Ce que ça dit pour nous : le client doit acheter à un privé, mais le prix est inconnu.

### A7-p3 : sanctions renforcées en 2026 (source unique)
- Acteur / marché : producteurs de biodéchets
- Type : obligation
- Source : résultat de recherche « biodéchets restaurants obligation » (extrait de recherche, 2026-10-13), site non précisé par l'outil
- Citation : « Décret n° 2026-433 du 2 juin 2026 » (≈ résumé outil, non vérifié)
- Chiffres : contravention de 3e classe
- Ce que ça dit pour nous : à vérifier sur Légifrance avant tout usage.

---

## A8. Recharge de véhicules électriques en copropriété : syndics et copropriétés qui font installer une infrastructure collective (lentille 2)

- Taille France : bottom-up : environ 12 200 nouveaux points de charge par an en résidentiel collectif (44 331 points en T2 2026, +38 % sur un an : 44 331 - 44 331/1,38 = 12 208, calcul) × [HYPOTHÈSE] 1 100 à 2 200 € par point (reste à charge de 1 080 € après prime selon Leocare, A8-p2 ; l'hypothèse double ce reste à charge) = 13 à 27 M€/an. Inférieur à 50 M€ : à confirmer, car l'infrastructure collective et la maintenance ne sont pas comptées.
- Croissance : +45 % d'immeubles équipés et +38 % de points sur un an (T2 2026 contre T2 2025, Avere-France, A8-p1) ; valeur ou volume : volume (immeubles et points). Un seul émetteur ; deuxième source institutionnelle non trouvée.
- Moteur de croissance : droit à la prise, aides Advenir revalorisées au 1er avril 2026 (plafond de 12 500 € par infrastructure collective jusqu'à 100 places, jusqu'à 50 % du coût HT) (A8-p2), objectif de 400 000 points publics fin 2030 (A8-p3).
- Acteurs : opérateurs spécialisés de recharge en copropriété (modèle « zéro avance de frais »), installateurs. Installateurs électriciens (NAF 43.21A) : 69 963 entreprises actives (API) ; top 3 non établi.
- Clients identifiables : 18 289 immeubles équipés = 7,2 % des immeubles collectifs, donc environ 254 000 immeubles collectifs au total (18 289 / 0,072, calcul) ; environ 236 000 non équipés. Syndics (NAF 68.32A) : 40 880 entités actives (API).
- Demande : 39,3 sessions par point public en août 2026 contre environ 31 un an plus tôt (A8-p3) ; recherche Google Trends non faite.
- Modèle d'exécution : service outillé (mise en relation syndic, vote en AG, dossier Advenir) ; l'installation est sous-traitée à des électriciens qualifiés IRVE.
- Contre-preuve (obligatoire) : le rythme de déploiement ralentit (14 544 points publics ajoutés au premier semestre 2026 contre 19 880 un an plus tôt, A8-p3) ; marché inférieur à 50 M€ en bottom-up ; opérateurs déjà installés.
- Seuils CLAUDE.md : taille ✘ (13 à 27 M€, hypothèse) | croissance ✔ (+38 à +45 %/an, une seule source) | concentration ? | clients ✔ (254 000 immeubles)
- Confiance : moyenne pour clients et croissance ; faible pour la taille.

### A8-p1 : baromètre du résidentiel collectif
- Acteur / marché : Avere-France (fédération), immeubles collectifs
- Type : tendance
- Source : https://www.avere-france.org/wp-content/uploads/2026/09/Barometre-des-infrastructures-de-recharge-en-residentiel-collectif_T2_2026-3.pdf (date : T2 2026, publié 2026-09, PDF ouvert)
- Citation : « 18 289 immeubles déjà équipés soit 7,2% des immeubles collectifs »
- Chiffres : 44 331 points de charge ; +45 % d'immeubles et +38 % de points sur un an
- Ce que ça dit pour nous : source de fédération, récente ; 92,8 % des immeubles restent à équiper.

### A8-p2 : primes Advenir revalorisées
- Acteur / marché : syndics, programme Advenir
- Type : argent dépensé (aides publiques)
- Source : https://leocare.eu/fr/blog/primes-bornes-electriques-copropriete/ et https://www.automobile-propre.com/articles/borne-de-recharge-en-copropriete-elle-va-couter-moins-cher-grace-a-laugmentation-de-ces-primes/ (extrait de recherche, 2026-04)
- Citation : « le plafond passe à 12 500 € pour les parkings jusqu'à 100 places » (≈ résumé outil)
- Chiffres : reste à charge d'environ 1 080 € par borne avec un opérateur qui avance les travaux ; primes valables pour les projets votés en AG à partir du 1er avril 2026
- Ce que ça dit pour nous : la dépense par copropriété est subventionnée et faible par point : volume élevé nécessaire.

### A8-p3 : recharge publique, contre-preuve de rythme
- Acteur / marché : Avere-France, recharge publique
- Type : contre-preuve
- Source : https://www.athlon.com/fr/informations-du-secteur/croissance-marquee-des-infrastructures-de-recharge-ouvertes-au-public-en-2026/ (extrait de recherche, 2026-09)
- Citation : « 200 926 » (points publics au 31 août 2026, ≈ résumé outil)
- Chiffres : +13 % sur un an ; 14 544 points ajoutés au premier semestre 2026 contre 19 880 en 2025 ; 39,3 sessions par point en août 2026
- Ce que ça dit pour nous : l'usage monte mais les installations ralentissent.

### A8-p4 : installateurs (comptage Sirene)
- Acteur / marché : installateurs électriques (NAF 43.21A)
- Type : tendance
- Source : https://recherche-entreprises.api.gouv.fr/search?activite_principale=43.21A&etat_administratif=A (date : 2026-10-13, API ouverte)
- Citation : « total_results » (champ API ; somme sur 100 départements = 69 963)
- Chiffres : 69 963 entreprises actives
- Ce que ça dit pour nous : l'exécution est fragmentée et sous-traitable ; l'avantage est dans la vente aux syndics.

---

## A9. Adaptation du logement à la perte d'autonomie (MaPrimeAdapt') : ménages de 70 ans et plus modestes et leurs prescripteurs (lentille 2)

- Taille France : bottom-up : 37 000 logements adaptés en 2024 (A9-p3) × coût moyen de travaux. Coût moyen estimé à partir de la Nouvelle-Aquitaine 2025 : aide de 23,5 M€ pour 4 183 logements = environ 5 600 €/logement (calcul), couvrant 63 % des travaux, donc travaux d'environ 8 900 €/logement (5 600 / 0,63, calcul) ; 37 000 × 8 900 = environ 330 M€/an de travaux subventionnés. Extrapolation d'une région à la France : [HYPOTHÈSE], confiance moyenne à faible. Hors travaux non subventionnés.
- Croissance : 37 000 logements en 2024 contre un objectif de 41 000 en 2026 (A9-p1, A9-p3) = environ +5 %/an en volume si l'objectif est atteint ; l'objectif 2025 de 45 000 n'est pas atteint en 2024. Démographie : seniors en perte d'autonomie de 2,5 M (2015) à 4 M (2050) selon Insee-Drees, soit environ +1,4 %/an (calcul, A9-p4).
- Moteur de croissance : vieillissement structurel (Insee-Drees), aide MaPrimeAdapt' de l'Anah (ménages modestes et très modestes).
- Acteurs : artisans, entreprises de salle de bain, accompagnateurs agréés ; top 3 non établi.
- Clients identifiables : ménages éligibles non comptés (API non applicable). 4 183 bénéficiaires en Nouvelle-Aquitaine en 2025 (A9-p2).
- Demande : tendance 5 ans non mesurée.
- Modèle d'exécution : service à forte main-d'œuvre (travaux) ou accompagnement/assistance à maîtrise d'ouvrage (outillé). Le client final (personne âgée) est difficile à joindre ; le canal passe par les CCAS, SAAD, kinés.
- Contre-preuve (obligatoire) : croissance de 5 %/an en dessous de 8 % ; objectif 2024 manqué (37 000 pour 45 000) ; guichet fermé début 2026 et stock de dossiers 2025 à instruire (A9-p1) ; dépend d'une aide budgétaire annuelle.
- Seuils CLAUDE.md : taille ✔ (330 M€ hypothèse) | croissance ✘ (environ 5 %/an, pas de moteur daté) | concentration ? (fragmenté) | clients ✔ probable (non compté)
- Confiance : faible à moyenne.

### A9-p1 : objectif 2026 et fermeture du guichet
- Acteur / marché : Anah, CAPEB
- Type : argent dépensé (aides publiques)
- Source : https://www.capeb.fr/actualites/budget-de-l-anah-2026-ou-en-sommes-nous (date : 2026-01-05, page ouverte)
- Citation : « avec 41 000 logements adaptés à la perte d'autonomie »
- Chiffres : objectif 2026 de 41 000 logements ; budget Anah 2026 de près de 4,4 Md€
- Ce que ça dit pour nous : volume plafonné par le budget, pas par la demande.

### A9-p2 : bilan régional 2025
- Acteur / marché : DREAL Nouvelle-Aquitaine (État)
- Type : argent dépensé
- Source : https://www.nouvelle-aquitaine.developpement-durable.gouv.fr/IMG/pdf/publication2026_bilan_financieranah2025_v3.pdf (date : 2026, extrait de recherche)
- Citation : « 4 183 logements adaptés pour 23,5 M€ d'aides » (≈ résumé outil)
- Chiffres : aide couvrant 63 % des travaux ; reste à charge moyen de 3 294 € ; cœur de cible 70 ans et plus
- Ce que ça dit pour nous : panier moyen de travaux de l'ordre de 9 000 €, avec un reste à charge de 3 300 € payé par le ménage.

### A9-p3 : bilan national 2024
- Acteur / marché : Anah
- Type : argent dépensé
- Source : https://www.batiweb.com/actualites/renovation-energetique/plus-d-aides-distribuees-mais-moins-de-logements-renoves-pour-l-anah-en-2024-45828 (extrait de recherche, 2025)
- Citation : « plus de 37 000 logements adaptés » (≈ résumé outil)
- Chiffres : objectif 2024 de 45 000 non atteint ; objectif 2025 de 45 000 ; premier trimestre 2025 : plus de 5 000 rénovations, reste à charge moyen de 3 420 €
- Ce que ça dit pour nous : volume national connu, mais inférieur aux objectifs.

### A9-p4 : démographie (Insee-Drees)
- Acteur / marché : Insee, Drees
- Type : tendance
- Source : https://www.previssima.fr/actualite/perte-dautonomie-pres-de-4-millions-de-personnes-seront-dependantes-en-2050-etude-insee.html (date inconnue, extrait de recherche ; étude 2016)
- Citation : « 4 millions de seniors en 2050, soit 16,4 % des seniors » (≈ résumé outil)
- Chiffres : 2,5 M de seniors en perte d'autonomie en 2015 (15,3 %) ; 30,2 % des 75 ans touchés
- Ce que ça dit pour nous : la hausse est lente (environ +1,4 %/an) ; source ancienne de 2016.

---

## A10. DPE collectif et plan pluriannuel de travaux : copropriétés et leurs syndics qui commandent diagnostics et audits (lentille 2, transition énergétique du bâti + obligation)

- Taille France : bottom-up plafond théorique : 578 000 copropriétés immatriculées (Sénat, A10-p2) × 1 000 à 4 000 € par DPE collectif (ADEME, A10-p3) = 0,58 à 2,3 Md€ sur un cycle de 10 ans (validité de 10 ans, ANIL, A10-p1), soit 58 à 231 M€/an en lissé. Hypothèse maximale : toutes les copropriétés sont soumises et aucune n'est déjà faite ; le champ réel (permis déposé avant 2013) est plus étroit. Confiance faible à moyenne.
- Croissance : non chiffrée. Obligation par vagues (A10-p1). La dernière vague (copropriétés de 50 lots maximum) est entrée en vigueur le 1er janvier 2026, donc le pic des commandes est 2026-2027 puis retombe : décroissance probable après la vague.
- Moteur de croissance : loi Climat et résilience : DPE collectif au 1er janvier 2024 (plus de 200 lots), 2025 (50 à 200), 2026 (50 lots maximum) ; plan pluriannuel de travaux pour les copropriétés de moins de 51 lots depuis le 1er janvier 2025 (ANIL).
- Acteurs : diagnostiqueurs certifiés, bureaux d'études, syndics (qui sélectionnent le prestataire). Top 3 non établi. Syndics (NAF 68.32A) : 40 880 entités actives (API).
- Clients identifiables : 578 000 copropriétés immatriculées ; total estimé 778 790 (Filocom 2019) à 887 855 (CoproFF 2023) ; environ un quart à un tiers non immatriculées (Sénat, A10-p2).
- Demande : tendance 5 ans non mesurée.
- Modèle d'exécution : service à main-d'œuvre qualifiée (diagnostiqueur certifié : exigence de certification non vérifiée [HYPOTHÈSE à confirmer], l'équipe n'a pas ce diplôme) ou apporteur d'affaires auprès des syndics.
- Contre-preuve (obligatoire) : échéance de 2026 déjà passée pour les petites copropriétés (la vague est lancée) ; une source (Cafpi) donne 2027 au lieu de 2026 pour les moins de 50 lots, contredite par l'ANIL ; le décideur est le syndic, à convaincre en assemblée générale ; DPE réalisable seulement par un diagnostiqueur certifié [HYPOTHÈSE].
- Seuils CLAUDE.md : taille ✔ (58 à 231 M€/an en plafond théorique) | croissance ✘ (vague en cours, pas de pic futur daté) | concentration ✔ probable (très fragmenté, non prouvé) | clients ✔ (578 000)
- Confiance : moyenne pour le moteur et les clients ; faible pour la taille.

### A10-p1 : calendrier officiel DPE collectif et PPPT
- Acteur / marché : ANIL (agence publique d'information sur le logement), copropriétés
- Type : obligation
- Source : https://www.anil.org/parole-expert-logement/diagnostics-immeuble-dpe-collectif-dtg-pppt-obligatoires/ (extrait de recherche, mise à jour novembre 2025 ; page non ouverte, connexion refusée)
- Citation : « Depuis le 1er janvier 2026, les copropriétés de 50 lots ou moins sont concernées » (≈ résumé outil)
- Chiffres : validité 10 ans ; PPPT : 51 à 200 lots depuis 2024, moins de 51 lots depuis 2025
- Ce que ça dit pour nous : vague 2026 en cours, donc la fenêtre pour un nouvel entrant est courte.

### A10-p2 : nombre de copropriétés (Sénat)
- Acteur / marché : Sénat, rapport sur la paupérisation des copropriétés
- Type : tendance
- Source : https://www.senat.fr/rap/r23-736-1/r23-736-16.html (date : rapport 2023-736, extrait de recherche)
- Citation : « près de 578 000 copropriétés » (≈ résumé outil)
- Chiffres : 578 000 immatriculées ; total estimé 778 790 (Filocom 2019) à 887 855 (CoproFF 2023)
- Ce que ça dit pour nous : vivier national chiffré par une institution ; date du chiffre de 578 000 non précisée.

### A10-p3 : prix du DPE collectif
- Acteur / marché : ADEME, rapporté par Meilleurtaux
- Type : argent dépensé (barème)
- Source : https://www.meilleurtaux.com/credit-immobilier/actualites/2024-decembre/dpe-collectif-incontournable-coproprietes-plus-50lots-compter-2025.html (date : 2024-12, extrait de recherche)
- Citation : « entre 1 000 et 4 000 € » (≈ résumé outil, attribué à l'ADEME)
- Chiffres : prix selon le nombre de lots, le chauffage et la localisation
- Ce que ça dit pour nous : panier bas par client (1 000 à 4 000 €), donc il faut du volume.

---

## Comptages API (recherche-entreprises.api.gouv.fr, état actif, 2026-10-13, somme sur 100 départements)

- NAF 43.21A (installation électrique) : 69 963
- NAF 47.91B (vente à distance sur catalogue spécialisé) : 55 472
- NAF 43.29A (travaux d'isolation) : 8 797
- NAF 56.10A (restauration traditionnelle, tous effectifs, micro inclus) : 114 659 (A7)
- NAF 68.32A (administration d'immeubles, syndics) : 40 880 (A8, A10)
- NAF 69.20Z (experts-comptables) : 23 827 (A1-p5)
- Entreprises de 50 à 249 salariés (tranches 21, 22, 31, tous secteurs) : 94 645 selon l'API, chiffre NON utilisé : trop élevé pour des entreprises (probablement des établissements ou des unités légales multiples), non cohérent avec les ordres de grandeur Insee que je n'ai pas ouverts. À revérifier avant usage pour A3.
- Note : les comptages Sirene comptent les entités actives, micro-entrepreneurs inclus ; une première tentative en parallèle (16 requêtes simultanées) a renvoyé des totaux partiels (limite de débit) et a été écartée ; les chiffres ci-dessus viennent de requêtes séquentielles complètes (100 départements).

## Sources non lues

- https://www.economie.gouv.fr/node/3238965 : 403 à l'ouverture (chiffres vus en extrait de recherche).
- https://siecledigital.fr/2026/08/27/facturation-electronique-face-aux-craintes-de-piratage-le-gouvernement-veut-rassurer/ : 403 (information « pas de sanction avant fin 2026 », « moins de six entreprises sur dix prêtes » vue seulement en résumé).
- https://www.impots.gouv.fr/... : hôte non résolu.
- https://www.anil.org/parole-expert-logement/diagnostics-immeuble-dpe-collectif-dtg-pppt-obligatoires/ : connexion refusée.
- https://www.corse.developpement-durable.gouv.fr/IMG/pdf/note_dreal_anah_bilan_2025_repartition_objectifs_credits_2026.pdf : PDF compressé illisible.
- Légifrance (décret 2020-887 BACS, loi APER art. 40, L.541-21-1, décret 2026-816, décret 2026-842, décret 2026-433) : non ouvert, aucune recherche dédiée. Les textes sont cités via des sources secondaires.
