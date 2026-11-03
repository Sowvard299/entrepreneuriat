# Agro x énergie : fichier de travail porte 1 (2026-11-02)

Mission : ce que boulangeries, boucheries-charcuteries, fromageries, ateliers < 50 salariés, restaurants indépendants et cuisines collectives paient déjà pour énergie et froid.
Recherches web : 12 sur 12 (budget atteint). Appels API recherche-entreprises : 1 série de comptages. WebFetch : 12.
Preuves : 20 (dont 4 comptages API). Domaines distincts : 17 (opera-energie.com = 5 preuves sur 20, soit 25 %).
Statut : partiel. Manque : aucun prix de contrat de maintenance froid ; aucun prix de frigoriste lu ; aucun prix payé d'audit énergie TPE ; prime CEE en euros pour boulangerie/boucherie ; avis Google ; cuisines collectives (non cherchées, budget) ; Reddit/forums de boulangers non lus.
Codes tranche d'effectif de l'API : 03 = 6-9 salariés, 11 = 10-19, 12 = 20-49 [HYPOTHÈSE : codification Sirene standard, non rouverte en session].

## Clients cibles (API recherche-entreprises, unités actives, 2026-11-02, nombre d'unités, pas de CA)
### A-01 : comptage par NAF
- Source : https://recherche-entreprises.api.gouv.fr/search?activite_principale=<NAF>&etat_administratif=A (appel API réel, 2026-11-02)
- Type : donnée officielle (Sirene). Plafond 10 000.
- Chiffres (total ; 6-9 / 10-19 / 20-49 salariés) : 10.71C boulangerie : ≥ 10 000 ; 5 713 / 4 701 / 1 274. 10.71D pâtisserie : 9 305 ; 469 / 370 / 126. 10.13B charcuterie : 2 962 ; 281 / 223 / 81. 47.22Z boucherie : ≥ 10 000. 47.23Z poissonnerie : 2 772. 10.51C fromagerie : 919 ; 95 / 99 / 99 (+ 35 de 50-99 et 29 de 100-199). 10.51A : 250. 10.85Z plats préparés : 2 869. 56.10A restauration traditionnelle : ≥ 10 000 ; ≥ 10 000 / 9 099 / 3 172. 56.29A restauration collective sous contrat : 556 ; 33 / 49 / 53. 56.29B autres : 4 391 ; 69 / 65 / 57.
- Ce que ça dit : les cibles se comptent par dizaines de milliers (seuil 3 000 B2B largement dépassé), mais la plupart ont moins de 10 salariés ; boulangeries employant ≥ 6 personnes : environ 11 700 (somme 10.71C).

## Argent dépensé et prix
### E-AE-01 : Courtage, rémunération par commission fournisseur
- Acteur / marché : courtiers (Opéra Énergie, Selectra...) payés par les fournisseurs, clients TPE/restaurants.
- Type : argent dépensé (indirect : le client ne voit pas le prix)
- Source : https://edito.seloger.com/node/19961 (extrait de recherche, date inconnue)
- Citation : « La commission est alors généralement comprise entre 2 et 5 % du montant du contrat. » (reformulation de l'extrait, pas copie littérale ; à rouvrir)
- Chiffres : 2 à 5 % du contrat. Xerfi (E-AE-02) : plus de 70 acteurs.
- Ce que ça dit pour nous : le modèle encaisse ; le prix payé par le client est caché, donc pas un « prix public » au sens strict.

### E-AE-02 : Marché du courtage : plus de 70 acteurs, surtout PME/ETI/public
- Source : https://www.xerfi.com/presentationetude/le-courtage-d-energie_sco75 (ouverte, mise à jour 2026-03-04)
- Citation : « plus de 70 acteurs » (extrait de la page, vendeur de rapports : confiance faible)
- Chiffres : clients surtout PME, ETI, public ; plus de 40 % des courtiers créés depuis 2021 ; étude à 1 500 € HT.
- Ce que ça dit pour nous : marché fragmenté (concentration non éliminatoire) mais TPE non décrites comme clientes ; contre-preuve partielle.

### E-AE-03 : Opéra Énergie vise explicitement boulangers et restaurateurs
- Source : https://opera-energie.com/courtage-en-energie-restaurant/ (ouverte, mise à jour 2026-07-27) et https://opera-energie.com/facture-electricite-boulangerie/ (ouverte, 2026-10-09)
- Citation : « Comparateur gratuit & sans engagement » ; « Tarifs négociés » (bandeau, rémunération non précisée)
- Chiffres : Trustpilot 4,9 sur 523 avis, Google 4,8 ; 18 agences ; boulangerie : 99 000 kWh/an en moyenne (Engie cité) ; page témoin : « la boulangerie économise 1000 euros par an » (https://opera-energie.com/media/partenariat-temoignage-boulanger/, 2017-06-26, 1 client, Lyon).
- Ce que ça dit pour nous : un acteur à 38 M€ (voir synthèses énergie) fait de ces métiers une cible, mais la gain annoncé est de l'ordre de 1 000 €/an par boulangerie : commission faible par client.

### E-AE-04 : Plaintes sur courtage (durée, taux) : Trustpilot
- Source : https://fr.trustpilot.com/review/opera-energie.com?stars=1&stars=2 (ouverte)
- Citation : « mon contrat a prix 40% au lieu des 15% prévus » (Sandrine, 2025-01-28, 1 étoile) ; « Les conseillers ne sont pas les payeurs » (2024-07-07)
- Chiffres : moins de 1 % d'avis 1-2 étoiles sur 523 ; réponses de l'entreprise à chacun.
- Type : plainte (contre-preuve de faiblesse : le leader est très bien noté)
- Ce que ça dit pour nous : la faiblesse prouvée est la rémunération opaque, pas la qualité perçue.

### E-AE-05 : Cadre juridique du courtage en énergie
- Source : https://www.lemondedudroit.fr/affaires/295-consommation/101227-reguler-les-activites-de-courtage-en-energie-depot-a-l-an.html (extrait de recherche) et https://www.assemblee-nationale.fr/dyn/17/textes/l17b1845_proposition-loi.pdf (extrait de recherche, déposée 2025-09-16)
- Citation : aucune copiée (extrait résumé : registre national obligatoire, décret après avis de la CRE)
- Type : obligation (en projet, non adoptée à ma connaissance ; statut à vérifier, dossier n° 1845)
- Chiffres : Code de bonne conduite du Syndicat des Courtiers en Énergie révisé en avril 2026, audit Bureau Veritas (https://opera-energie.com/media/syndicat-courtiers-energie-nouveau-code-bonne-conduite/, 2026-05-11, auto-déclaré).
- Ce que ça dit pour nous : pas de licence aujourd'hui [à confirmer par l'auditeur, article non cité] ; un registre arrive peut-être. Honoraires affichés = positionnement aligné sur la régulation.

### E-AE-06 : Étranger : action collective sur commissions cachées (restauration, Royaume-Uni)
- Source : https://www.thecaterer.com/news/hospitality-energy-bill-legal-challenge-hidden-fees (ouverte, 2024-02-07)
- Citation : « Catering businesses are often heavy consumers of energy » (Harcus Parker)
- Chiffres : plus de 1 700 entreprises de restauration inscrites ; jusqu'à 2 milliards £ visés ; ~250 M£ ajoutés aux factures sur dix ans (estimations du cabinet).
- Type : plainte (étranger, non transposable en droit français)
- Ce que ça dit pour nous : la transparence des commissions est un sujet porteur pour la restauration ; aucune preuve équivalente en France.

### E-AE-07 : Part de l'énergie dans les charges (boulangerie)
- Source : https://services.totalenergies.fr/professionnels/conseils/transition-energetique/boulangerie-comment-economiser-energie (ouverte, date inconnue ; vendeur d'énergie)
- Citation : « La consommation d'énergie d'une boulangerie représente environ 5 % de son chiffre d'affaires. »
- Chiffres : cuisson 1er poste, froid 2e ; même ordre de grandeur sur l'-expert-comptable.com (extrait de recherche). Restauration : aucun pourcentage trouvé. Seuil d'aide 2023 : énergie ≥ 3 % du CA 2021 (service-public, extrait).
- Ce que ça dit pour nous : 5 % du CA est un enjeu réel mais source commerciale ; chiffre non institutionnel (confiance faible).

### E-AE-08 : Aides 2023 aux boulangers : signal, pas preuve
- Source : https://www.banquedesterritoires.fr/boulangeries-les-aides-en-place-insuffisantes-pour-contrer-la-hausse-des-prix-de-lenergie (ouverte, 2022-12-13)
- Citation : « les aides mises en place par l'Etat n'épongeront qu'une faible part de l'augmentation »
- Chiffres : facture type de 4 000 € ramenée à 2 600 € (exemple ministre) ; boulanger de Blois : 1 000 €/mois l'hiver, triplé à ~3 000 € ; guichet d'aide 2023 désormais limité aux ETI > 250 salariés (extrait de recherche service-public).
- Type : tendance / plainte. Ce que ça dit : la facture d'une boulangerie est de l'ordre de 12 000 à 36 000 €/an selon le prix ; aides terminées, donc pas de moteur réglementaire pérenne.

### E-AE-09 : CEE froid commercial, fiches
- Source : https://opera-energie.com/bat-eq-125/ (ouverte, 2026-04-07) ; extrait de recherche pour BAT-EQ-134 (prime d'environ 489 € pour une supérette) et BAT-EQ-124 (portes vitrées sur meubles positifs).
- Citation : « 8 200 kWh cumac par mètre » (meuble double, couvercles BAT-EQ-125 ; paraphrase de l'extrait)
- Chiffres : BAT-EQ-125 : 6 700 / 8 200 / 4 600 kWh cumac par mètre ; IND-UT-113 (condensation), IND-UT-116, IND-UT-117 (récupération de chaleur sur groupe froid, cité par ademe/DREAL, extrait de recherche). Économie de ~30 % sur vitrines positives avec portes (OFEN suisse, extrait de recherche). Prime en euros pour boucherie/boulangerie : non trouvée.
- Type : obligation (dispositif CEE). Ce que ça dit : le mécanisme existe et la prime est petite par site ; CEE = délégataire/mandataire, rémunéré par la valeur du certificat (déjà écarté en v3 pour les supermarchés).

### E-AE-10 : Prix du matériel froid (chambre froide)
- Source : https://www.prix-pose.com/chambre-froide et https://conseils.hellopro.fr/guide-de-prix-pour-les-chambres-froides-1314.html (extraits de recherche, dates inconnues)
- Citation : aucune copiée.
- Chiffres : chambre froide positive de 1 500 à plus de 20 000 € ; un devis de 9 000 € HT (150 m3, groupe ~11,6 kW) ; moteur positif ≥ 1 500 €, négatif 2 000 à 5 000 € ; dépannage hors contrat 100 à 200 €/h (site grand public, extrait).
- Type : argent dépensé (prix de vendeurs, pas ventes constatées). Ce que ça dit : un remplacement de groupe = 1 500 à 9 000 € ; marge d'intermédiation possible.

### E-AE-11 : Maintenance froid : aucun prix lisible
- Source : recherche « contrat maintenance chambre froide prix » (extrait de recherche)
- Chiffres : visite 1 à 2 fois/an dans les marchés publics (lycée) ; 145 €/an cité sur un forum de particuliers (équipement domestique, non transposable) ; fourchette clim 120 à 350 €/an.
- Type : contre-preuve (aucun prix public de contrat froid pro). Ce que ça dit : le 3e prix de la piste maintenance manque.

### E-AE-12 : Monitoring de température connecté : prix publics
- Source : https://www.lafabriquedunet.fr/logiciel/octopus-haccp (extrait de recherche) ; https://octopus-haccp.com/?p=18863 (extrait)
- Citation : aucune copiée.
- Chiffres : capteur 6 € HT/mois, hub 12 € HT/mois, tablette 12 €, imprimante 20 € ; Testo Smart 3,90 €/mois (extrait lhotellerie-restauration.fr). Suivi de consommation électrique : aucun prix trouvé.
- Type : argent dépensé (prix catalogue). Ce que ça dit : le froid connecté se vend en abonnement (3 prix publics), mais côté HACCP, pas énergie ; le suivi énergie n'est pas prouvé.

### E-AE-13 : Audit énergie TPE : aide, pas de prix
- Source : https://www.laposte.fr/professionnel/mag/audit-energetique-pour-une-TPE (ouverte, 2026-07-09) ; https://agirpourlatransition.ademe.fr/entreprises/aides-financieres/catalogue/2025/audit-energetique-volontaire-en-industrie (extrait)
- Citation : « peut financer jusqu'à 80 % du coût d'un audit volontaire pour les petites entreprises »
- Chiffres : pas de prix d'audit ; tertiaire seul inéligible ; obligation d'audit seulement au-dessus de 2,75 GWh (extrait de recherche, non ouvert) ; gain potentiel 10 à 25 % de la facture (ADEME 2017 via plaquette Nouvelle-Aquitaine, extrait).
- Type : obligation / aide. Ce que ça dit : pas de prix payé constaté ; l'aide rend la prestation presque gratuite pour les ateliers industriels.

### E-AE-14 : Récupération de chaleur : coûts unitaires, seuil d'aide
- Source : https://www.bioenergie-promotion.fr/wp-content/uploads/2018/12/condenseur_fiche-technique-integration-dans-industrie-2018.pdf (extrait de recherche, 2018)
- Chiffres : échangeur sur condenseur ~35 €/kW ; sur désurchauffeur 190 à 380 €/kW ; ballon 2,7 €/L ; site agro du Nord : 60 k€ d'investissement, 18,6 k€ de CEE (30 %), grande usine ; Fonds Chaleur : plus de 1 GWh/an exigé, donc hors de portée d'un commerce.
- Type : argent dépensé (REX industriel, taille supérieure à la cible). Ce que ça dit : pour fromageries et ateliers, la rentabilité dépend du besoin d'eau chaude ; piste d'ingénierie, pas de courtage.

### E-AE-15 : Cadre juridique des aides et CEE
- Source : https://agirpourlatransition.ademe.fr/entreprises/aides-financieres/2026/realisation-dinstallations-recuperation-chaleur-fatale (extrait de recherche)
- Chiffres : si une fiche CEE existe sous 6 GWh/an, pas d'aide ADEME en plus (note ADEME 2020, extrait).
- Ce que ça dit : un projet à petite échelle passe par un obligé CEE ou un délégataire ; le statut de délégataire/mandataire est à faire citer par l'auditeur.

## Sources non lues
- Réponses de l'Assemblée nationale sur l'énergie des boulangers (QANR5L16QE3920, 4154, 4392...) : ouvertes seulement en extrait ; l'énergie à « 30 % du CA du commerce » (non identifié) non utilisée.
- Pappers, Reddit, malt : bloqués, non tentés.
- Avis Google, forums de boulangers : non lus (budget).
- seloger.com (rémunération 2-5 %), prix-pose.com, hellopro.fr, lafabriquedunet.fr, octopus-haccp.com, lhotellerie-restauration.fr, ademe : extraits de recherche, pages non ouvertes (budget).
