# Porte 1 : agroalimentaire, restauration commerciale indépendante et collective (fichier de travail)

- Mission : argent déjà dépensé autour de l'alimentation (appro local/EGalim, biodéchets, gaspillage, fiches techniques/coût matière/allergènes), 6 à 8 pistes.
- Date : 2026-11-02. Recherches web utilisées : 11 / 12. WebFetch : 7. Appels API recherche-entreprises : 3 lots.
- Preuves : 20. Domaines distincts : 16 (maire-info, agriculture.gouv.fr, lejournaldesentreprises, combak.co, journaldunet, lafabriquedunet, kolonell, grand-senonais, 3rdanjou, agglo-niort, recherche-entreprises.api.gouv.fr, banquedesterritoires, lillemetropole, grandangouleme, appvizer/capterra, tuco.ac.uk).
- Règle : la plupart des prix viennent d'extraits de recherche (indiqué). Le résumé de l'outil de recherche n'est pas une citation : quand je n'ai pas le texte exact, je l'écris « citation non copiable ».
- Vérif archives (Grep mot-clé) : biodéchets pros éliminé en v3 (A7 : « déjà en vigueur depuis 2024, aucun prix, logistique d'employeur »). Rouvert ici avec prix trouvés (E10 à E13), angle nouveau à écrire.

## Piste 1 : fiches techniques / coût matière / allergènes, restauration indépendante (SaaS)

### E01 : Koust, prix publics
- Acteur / marché : Koust (Brest) vend fiches techniques, inventaires, allergènes, HACCP aux restaurateurs
- Type : argent dépensé (prix catalogue, clients payants non comptés)
- Source : https://www.lafabriquedunet.fr/logiciel/koust (date inconnue ; extrait de recherche)
- Citation : citation non copiable (résumé d'outil) : offre Essentiel 80 €/mois/site annuel, 90 € en mensuel
- Chiffres : 80 à 90 €/mois/site ; grille éditeur (koust.net, PDF illisible) citée à 130 € (Professionnel) et 180 € (Entreprise) par mois et par site
- Ce que ça dit pour nous : le prix de marché est de 80 à 180 €/mois/site, soit 1 000 à 2 200 €/an par restaurant.

### E02 : Melba et Inpulse, prix publics
- Acteur / marché : Melba (49 € HT/mois annuel, 99 € Premium) ; Inpulse (gratuit en base, 159 € HT/site/mois)
- Type : argent dépensé (prix catalogue)
- Source : https://www.appvizer.fr/operations/erp/melba et résultats Koust/Inpulse (date inconnue ; extrait de recherche)
- Citation : citation non copiable (résumé d'outil)
- Chiffres : 49 / 99 / 159 € HT par mois ; Appvizer précise « par utilisateur » pour Melba
- Ce que ça dit pour nous : 3 prix publics (E01, E02) confirmés, mais un acteur propose un plan gratuit.

### E03 : contre-preuve, outils gratuits ou à 29 €
- Acteur / marché : Ratatool (dès 29 €/mois), RatioChef (gratuit, fiches illimitées), Resto-Coûts (gratuit à vie)
- Type : contre-preuve
- Source : https://www.capterra.fr/software/196663/ratatool (403 à l'ouverture ; extrait de recherche), getapp.fr/software/2097488/ratiochef (extrait)
- Citation : citation non copiable (résumé d'outil)
- Chiffres : 29 €/mois ; 0 €
- Ce que ça dit pour nous : marché encombré et prix tiré vers le bas ; peu d'espace pour un « pareil mais mieux » sans angle précis.

### E04 : nombre de restaurants cibles
- Acteur / marché : établissements actifs NAF 56.10A (restauration traditionnelle), 56.10C, 56.21Z
- Type : taille
- Source : https://recherche-entreprises.api.gouv.fr/search?activite_principale=56.10A&etat_administratif=A&per_page=1 (ouvert, 2026-11-02)
- Citation : « total_results »:10000 (plafond de l'API atteint pour 56.10A, 56.10C, 56.21Z, 56.30Z)
- Chiffres : > 10 000 par code (micro-entreprises incluses) ; v3 archive : 114 659 pour 56.10A [source archive, non revérifiée]
- Ce que ça dit pour nous : plus de 3 000 clients B2B, seuil largement passé.

## Piste 2 : logiciel pour cuisines centrales / restauration collective de taille moyenne

### E05 : prix du marché restauration collective
- Acteur / marché : éditeurs spécialisés (non nommés) pour cuisines centrales
- Type : argent dépensé (ordre de grandeur, confiance faible)
- Source : https://kolonell.com/fr/blog/logiciel-cuisine-centrale-restauration-collective-lyon-2026 (ouvert, 2026-10-08)
- Citation : « Paramétrage figé, frais par site »
- Chiffres : 200 à 350 € HT/mois (base), 400 à 600 € HT/mois (complet) ; sur mesure 30 000 à 60 000 € HT. L'auteur vend du sur mesure : chiffres non sourcés.
- Ce que ça dit pour nous : faiblesse déclarée des acteurs (paramétrage figé, portail client limité) mais source intéressée.

### E06 : nombre de cuisines collectives
- Acteur / marché : NAF 56.29A (restauration collective sous contrat) 556 ; 56.29B (autres services) 4 391 ; 87.10A (Ehpad médicalisés) 3 195 ; 87.30A 1 895
- Type : taille
- Source : https://recherche-entreprises.api.gouv.fr/search?activite_principale=56.29A&etat_administratif=A&per_page=1 (ouvert, 2026-11-02)
- Citation : « total_results »:556 (56.29A) ; 4391 (56.29B) ; 3195 (87.10A)
- Chiffres : unités légales, pas sites de production ; une société de restauration compte plusieurs sites
- Ce que ça dit pour nous : 556 sociétés sous contrat est un petit nombre de clients (sous 3 000) ; il faut y ajouter Ehpad et 90 000 cantines (E07).

## Piste 3 : pilotage EGalim / télédéclaration « ma cantine » (communes, Ehpad, sociétés de restauration)

### E07 : taux de conformité publié
- Acteur / marché : cantines françaises, ministère de l'Agriculture
- Type : obligation réglementaire
- Source : https://www.maire-info.com/restauration-scolaire/bio-dans-les-cantines-la-ta-la-da-claration-des-achats-progresse-fortement-47-art26-31233 (ouvert, 2026-10-29)
- Citation : « les taux d'approvisionnement s'établissent à 31,1 % de produits durables et de qualité »
- Chiffres : achats 2025 : 31,1 % durables, 12,1 % bio (cibles 50 % et 20 %) ; près de 50 000 cantines télédéclarantes soit 59 % des sites (+47 %) ; « plus de 90 000 cantines » selon le gouvernement
- Ce que ça dit pour nous : la grande majorité est sous l'objectif et 41 % ne déclarent pas, mais rien ne prouve qu'ils paient pour y arriver.

### E08 : achats 2024, double objectif
- Acteur / marché : cantines télédéclarantes (bilan EGalim 2025, ministère)
- Type : obligation
- Source : https://agriculture.gouv.fr/telecharger/152514 (extrait de recherche, bilan EGalim 2025)
- Citation : citation non copiable (résumé d'outil)
- Chiffres : 29,5 % durables, 11,8 % bio ; environ 35 % des cantines atteignent 50 % ; près de 30 % atteignent le double objectif
- Ce que ça dit pour nous : confirme que 70 % des déclarants échouent au double objectif. Croissance : bio stagne (11,8 puis 12,1 %), donc la douleur ne se résorbe pas seule.

### E09 : contre-preuve, outils publics gratuits
- Acteur / marché : Agrilocal (plateforme départementale) et ma cantine (État)
- Type : contre-preuve
- Source : https://www.banquedesterritoires.fr/agrilocal-plateforme-de-mise-en-relation-entre-les-acheteurs-publics-de-la-restauration-collective (extrait de recherche)
- Citation : citation non copiable (résumé d'outil) : outil « simple, gratuit et immédiat », 34 à 38 départements
- Chiffres : 0 € pour l'acheteur ; aucun prix payé trouvé pour un service privé d'aide à l'EGalim
- Ce que ça dit pour nous : l'argent visible manque ; l'État fournit gratuitement la déclaration et la mise en relation.

## Piste 4 : collecte et valorisation des biodéchets des pros (rouverte, v3 A7 avait écarté)

### E10 : forfait 80 € par mois (Grand Senonais)
- Acteur / marché : intercommunalité, collecte hebdo bac 120 L pour les pros
- Type : argent dépensé (tarif public)
- Source : https://www.grand-senonais.fr/wp-content/uploads/2025/10/LA-FAQ-DES-DECHETS-1-1.pdf (ouvert, 2025-10)
- Citation : « 80 par mois pour une collecte hebdomadaire de vos biodéchets (bac de 120L). »
- Chiffres : 80 (€ implicite, HT/TTC non précisé) par mois, soit environ 960 €/an
- Ce que ça dit pour nous : la collecte coûte environ 1 000 €/an par restaurant ; prix fixé par la collectivité, pas par le marché.

### E11 : Les Alchimistes, 23 € l'échange de bac
- Acteur / marché : Les Alchimistes via 3rd'Anjou (collectivité)
- Type : argent dépensé
- Source : https://3rdanjou.fr/media/le-service-pour-les-professionnels-1.pdf (PDF illisible à l'ouverture ; extrait de recherche)
- Citation : citation non copiable (résumé d'outil) : 23 € par échange de bac, inscription minimale 3 mois
- Chiffres : 23 € par enlèvement
- Ce que ça dit pour nous : second prix public payé, au passage.

### E12 : redevance au litre (Niort)
- Acteur / marché : Agglomération de Niort
- Type : argent dépensé (obligation)
- Source : https://www.agglo-niort.fr/fileadmin/CAN/agglo/Conseils_d_Agglo/CA_110422/C70-04-2022-1.pdf (2022-04 ; extrait de recherche)
- Citation : citation non copiable (résumé d'outil)
- Chiffres : 0,0117 €/litre ; forfait 157,33 €/an pour un conteneur 120/140 L (environ 13 €/mois)
- Ce que ça dit pour nous : écart de 1 à 6 entre territoires (13 à 80 € par mois) : prix fixés localement.

### E13 : Hector le Collector (Toulouse), contre-preuve de taille
- Acteur / marché : start-up de collecte, environ 10 restaurants et 6 entreprises clients
- Type : contre-preuve / argent dépensé
- Source : https://www.lejournaldesentreprises.com/article/hector-le-collector-veut-faciliter-la-gestion-des-biodechets-pour-les-professionnels-643854 (ouvert, 2020-12-09)
- Citation : citation non copiable (article en anglais via l'outil) : abonnement de 6 à 24 mois, facturé au nombre de collectes
- Chiffres : une dizaine de restaurants clients
- Ce que ça dit pour nous : modèle ancien et petit ; la logistique est lourde (contre-preuve ; v3 notait « logistique d'employeur »).

### E14 : contre-preuve, contrôle faible
- Acteur / marché : obligation de tri L.541-21-1 depuis 2024
- Type : contre-preuve
- Source : https://www.grandangouleme.fr/wp-content/uploads/2024/07/2403-Dossier-de-presse-Rappel-de-lobligation-de-tri-des-bio-dechets-des-professionnels-2.pdf (extrait de recherche, 2024-03)
- Citation : citation non copiable (résumé d'outil) : bacs non collectés si biodéchets trouvés dans les sacs noirs
- Chiffres : aucun taux de conformité national ni nombre de sanctions trouvé
- Ce que ça dit pour nous : l'obligation existe mais la contrainte reste locale.

## Piste 5 : anti-gaspi invendus pour restaurateurs (paniers, dons)

### E15 : Too Good To Go, commission payée
- Acteur / marché : Too Good To Go vend des paniers de commerçants et restaurants
- Type : argent dépensé
- Source : https://www.journaldunet.com/retail/1511781-lucie-basch-cofondatrice-too-good-to-go/ (extrait de recherche, date inconnue) et https://www.combak.co/blog/toogoodtogo-avis (extrait)
- Citation : citation non copiable (résumé d'outil) : 1,09 € prélevé sur un panier de 5 €
- Chiffres : commission 1,09 €/panier (JDN) ; blog : 25 % avec minimum 1,09 € et abonnement annuel d'environ 39 € (source tierce, confiance faible) ; nombre de partenaires divergent (2 200 vs 30 000)
- Ce que ça dit pour nous : l'argent circule, mais le marché est tenu par un acteur international ; le restaurateur paie peu.

### E16 : contre-preuve, Phenix gratuit pour les associations
- Acteur / marché : Phenix (dons d'invendus)
- Type : contre-preuve
- Source : https://www.reussir.fr/fruits-legumes/phenix-repond-a-la-forte-demande-en-produits-frais-des-associations (extrait de recherche)
- Citation : citation non copiable (résumé d'outil) : « près de 1300 associations » partenaires
- Chiffres : aucun tarif B2B de Phenix ou Comerso publié
- Ce que ça dit pour nous : pas de prix payé vérifié côté cantines ; piste non prouvée.

## Piste 6 : pesée automatisée du gaspillage en cantine (Winnow, Leanpath, Kitro)

### E17 : prix non publiés
- Acteur / marché : Winnow, Leanpath, Kitro (caméra + balance + tablette)
- Type : argent dépensé (non chiffré)
- Source : https://www.ki-syndikat.de/tools/winnow/ (extrait de recherche, date inconnue)
- Citation : « Winnow gibt keine öffentlichen Preise an » (extrait de recherche, texte tel que renvoyé par l'outil)
- Chiffres : Kitro affirme plus de 500 cuisines dans plus de 40 pays (source Journal des Palaces, extrait) ; aucun prix. Revendication Winnow : retour 2 à 10 fois la première année (vendeur).
- Ce que ça dit pour nous : modèle encaissé à l'étranger mais 0 prix public : ne satisfait pas la règle des 3 prix (éliminatoire porte 1 en l'état).

### E18 : coût du gaspillage en restauration collective
- Acteur / marché : restauration collective, 3,8 milliards de repas par an
- Type : tendance (chiffre cité ADEME non recoupé)
- Source : https://lillemetropole.fr/sites/default/files/2025-12/MEL_guide_etablissements_scolaire%20web%281%29.pdf (extrait de recherche, 2025-12)
- Citation : citation non copiable (résumé d'outil)
- Chiffres : environ 120 g par convive, 68 centimes par repas ; 8 % du gaspillage total
- Ce que ça dit pour nous : 68 c par repas fournit le ROI pour un outil de pesée, à recouper avec l'ADEME.

## Piste 7 : voie distribution, représenter en France un outil étranger de pesée ou de coût matière

### E19 : Inpulse (Belgique) entre en France
- Acteur / marché : Inpulse, outil belge de food cost et fiches techniques
- Type : tendance / argent dépensé
- Source : https://www.lafabriquedunet.fr/logiciel/koust (extrait de recherche) et résultats Koust/Inpulse
- Citation : citation non copiable (résumé d'outil) : « gagne du terrain en France, surtout grâce à un tarif d'entrée bas »
- Chiffres : 0 € en base, 159 € HT/site/mois en complet
- Ce que ça dit pour nous : le modèle de revendeur est possible (Inpulse a déjà son équipe), mais l'espace commission est étroit.

### E20 : contre-preuve, Kitro et Winnow vendent en direct
- Acteur / marché : Kitro, Winnow
- Type : contre-preuve
- Source : https://www.journaldespalaces.com/article-78564-suisse-fournisseurs-ia-foodtech-kitro-accelere-sa-croissance-internationale-reduction-du-gaspillage-alimentaire-dans-l-hotellerie-et-la-restauration.html (extrait de recherche)
- Citation : citation non copiable (résumé d'outil)
- Chiffres : aucune trace d'un distributeur ou agent France indépendant
- Ce que ça dit pour nous : à vérifier par un contact direct avant de croire à une voie distribution.

## Sources non lues
- https://koust.net/wp-content/uploads/Forfaits-Koust3.pdf : PDF compressé, prix illisibles
- https://www.capterra.fr/software/196663/ratatool : 403
- https://3rdanjou.fr/media/le-service-pour-les-professionnels-1.pdf : PDF compressé, prix connu seulement par extrait
- ma-cantine.agriculture.gouv.fr (rapport complet) et bilan EGalim 2025 (agriculture.gouv.fr/telecharger/152514) : non ouverts, budget
- Moulinot, Veolia, Phenix, Comerso, Winnow, Leanpath : tarifs non publiés
- Données Agreste / Insee sur le nombre d'Ehpad et cantines : non cherchées, budget
