# Audit : maintenance du froid commercial et des cuisines professionnelles, abonnement préventif à délai garanti
Date : 2026-11-03. Auditeur : agent `auditeur`. Statut : complet sauf les manques listés en fin de fichier.
Recherches web utilisées : 15 sur 15. Appels outil/API (hors budget) : fiche 33.12Z, compter ×5, echecs ×2, marches-publics, API recherche-entreprises, DECP, BODACC.
RÉSUMÉ du vérificateur de citations : OK=8, ABSENT=2 (PDF compressés, retrouvées par pypdf), BLOQUE=0, EXTRAIT=0 ; détail en fin de fichier.
Preuves réutilisées sans les refaire : S1-17 (acteurs 6-20 M€, déclassée en partie : Azur Trucks Froid et Dalkia Froid Solutions perdent de l'argent, voir F-6), S1-20 (pénurie, N3), S1-22 (DECP, N1), S1-23 (BODACC), S1-24 (aucun avis négatif trouvé). Détail dans `ideas/_recherche-v4/porte1/v5/s1-travail.md`.

## 0. Idée et hypothèses
Abonnement annuel pour restaurants, commerces de bouche et cuisines collectives : 1 à 2 visites préventives par an (froid positif et négatif, cuisson) + délai d'intervention garanti en cas de panne (heures, week-end compris). Prix de l'abonnement [HYPOTHÈSE] 900 à 1 200 € HT par an et par site (aucun prix privé publié trouvé, voir F-1 à F-4).

## 1. Preuves (IDs F-)

### F-1 : Contrat préventif d'une commune, avec prix du forfait, de la main d'oeuvre et du déplacement, sans garantie de délai
- Acteur / marché : Allier Froid Clim (Saulcet, 03 ; NAF 33.12Z) pour la ville de Royat ; maintenance préventive du matériel de cuisine d'un restaurant scolaire
- Type : argent dépensé (prix) + contre-preuve (aucune garantie de délai)
- Source : https://www.royat.fr/wp-content/uploads/2025/02/DM2024-178-Ville-de-Royat-Restau-co-Maintenance-des-materiels-de-cuisine-Allier-Froid-Clim.pdf (date : 2024-10 ; niveau N2 ; émetteur : mairie de Royat, texte extrait du PDF avec pypdf, accents dégradés par la police)
- Citation : « Montant H.T 680 »
- Citation 2 : « sans aucune garantie »
- Chiffres : redevance forfaitaire 680 € HT (816 € TTC) par an pour 1 visite préventive par an, fixe 3 ans ; main d'oeuvre dépannage 60,00 € HT/heure ; déplacement 60,00 € HT (tarif 2024) ; interventions du lundi au vendredi de 8 h à 17 h ; « interviendra dans les meilleurs délais » ; le planning est indicatif et son non-respect ne donne droit à aucun dommage-intérêt.
- Ce que ça dit pour nous : 3 prix publics N2 chez un seul émetteur ; l'offre en place est un forfait de visite sans délai garanti ni week-end : l'angle « délai garanti » est vide chez ce vendeur, mais le client y paie 680 € par an, pas 1 200.

### F-2 : Contrat d'entretien « dépannages inclus » d'une commune
- Acteur / marché : Entreprise Mollière (La Chapelle-Saint-Mesmin, 45 ; NAF 43.22B ; 20-49 salariés, résultat net 0,25 M€ en 2025, CA confidentiel) pour la ville d'Ormes ; 2 restaurants scolaires, 1 salle, 1 centre de loisirs
- Type : argent dépensé (prix)
- Source : https://www.ville-ormes.fr/download/94/2025/7095/dc_2025_013_passation-dun-contrat-de-maintenance-du-materiel-de-cuisine-avec-lent-molliere.pdf (date : 2025-01-09 ; niveau N2 ; émetteur : mairie d'Ormes ; texte extrait avec pypdf)
- Citation : « Redevance annuelle : 3 892,00 € hors taxes, soit 4 670,40 € toutes taxes comprises »
- Chiffres : 3 892 € HT par an pour 4 sites, contrat « type P2, dépannages inclus », 1 an renouvelable 2 fois par tacite reconduction ; soit environ 970 € HT par site [calcul : 3 892 / 4].
- Ce que ça dit pour nous : le prix par site d'une cuisine collective, dépannages inclus, est proche de nos 900-1 200 € HT ; une reconduction tacite annuelle est la norme du contrat concurrent.

### F-3 : Diagnostic à distance de pannes de cuisine pro (service freelance)
- Acteur / marché : JulesTech (frigoriste BTS, vendeur depuis mai 2026, 0 vente) sur ComeUp ; diagnostic par photos et vidéos
- Type : recherche active (offre indirecte) ; niveau de preuve faible
- Source : https://comeup.com/fr/service/530999/diagnostiquer-votre-panne-froid-ou-chaud-en-cuisine-pro-a-distance-en-24h (date : 2026-11-03 ; niveau N2 ; émetteur : ComeUp, page du vendeur)
- Citation : « Réponse sous 24h »
- Chiffres : forfait Basique 40,00 € ; 0 vente, aucun avis.
- Ce que ça dit pour nous : une offre de substitution existe (diagnostic distant, 40 €) mais n'a encore aucun client : ne prouve aucune demande.

### F-4 : Prix d'attribution des contrats publics de maintenance de chambres froides et de cuisines (DECP)
- Acteur / marché : collectivités, hôpitaux, établissements
- Type : argent dépensé
- Source : https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/decp-2022-marches-valides/records?where=search(objet,"maintenance chambres froides") and montant>0 and montant<60000 and dureemois>=12 (date : 2026-11-03 ; niveau N1 ; émetteur : DECP, data.economie.gouv.fr)
- Citation : aucune (donnée API)
- Chiffres : « maintenance chambres froides », notifiés 2025-2026, montants maximum sur la durée : 22 234 € / 48 mois (6 offres), 31 000 € / 48 mois (3 offres), 2 280 € / 24 mois (1 offre), 1 388 € / 60 mois (2 offres), 44 837 € / 48 mois (6 offres). « maintenance équipements de cuisine » 2026 : 1 898 € / 24 mois ; 3 995 € / 48 mois ; 5 200 € / 36 mois ; 13 596 € / 12 mois ; 14 000 € / 12 mois ; 32 000 € / 12 mois ; 40 882 € / 48 mois (GHT, parc frigorifique). Nombre d'offres reçues : 1 à 6.
- Limites : montant = valeur maximale pour les accords-cadres, périmètres inconnus ; ces prix sont ceux du secteur public, pas des restaurants.
- Ce que ça dit pour nous : l'argent public dépensé est réel (S1-22 : 144 marchés « maintenance froid » en 2025, 39,5 M€) mais les petits contrats valent 300 à 1 000 € par an : le prix privé d'un abonnement à 1 200 € n'est pas établi.

### F-5 : Nombre de clients potentiels (restaurants et commerces de bouche employeurs)
- Acteur / marché : unités légales actives, API Sirene/RNE via `outils/donnees.py compter`
- Type : tendance (taille)
- Source : https://recherche-entreprises.api.gouv.fr/search?activite_principale=56.10A&etat_administratif=A&per_page=1 (et 56.10C, 47.22Z, 10.71C ; date : 2026-11-03 ; niveau N1 ; émetteur : INSEE/RNE)
- Citation : aucune (donnée API)
- Chiffres : employeuses (1 salarié ou plus) : 56.10A 68 111 ; 56.10C 47 361 ; 47.22Z 8 549 ; 10.71C 22 186 ; total 146 207. Avec 3 salariés ou plus : 56.10A 46 776 ; 56.10C 27 083 ; 47.22Z 5 370 ; 10.71C 18 201 ; total 97 430 [calcul : somme des tranches 3-5 et plus de `compter`]. Limite : unités légales, pas établissements ; un groupe multi-sites compte une fois. Cuisines collectives (56.29A) : 556 unités légales dont 269 employeuses.
- Ce que ça dit pour nous : plus de 3 000 clients identifiables : seuil passé largement.

### F-6 : Acteurs du froid commercial avec CA et résultat (comptes déposés)
- Acteur / marché : NAF 33.12Z et 43.22B, requête « froid » avec CA ≥ 1,5 M€
- Type : argent dépensé
- Source : https://recherche-entreprises.api.gouv.fr/search?q=froid&activite_principale=33.12Z&etat_administratif=A&ca_min=1500000 (date : 2026-11-03 ; niveau N1 ; émetteur : INSEE/RNE)
- Citation : aucune (donnée API)
- Chiffres (dernier exercice déposé, CA / résultat net) : Dalkia Froid Solutions 226,6 M€ / -5,0 M€ (2025) ; Paris Froid Services 20,4 M€ / +0,5 M€ (2025, 91) ; Froid & Services Méditerranée 13,2 M€ / +1,1 M€ (2024, 13) ; Azur Trucks Froid 11,5 M€ / -1,2 M€ (2025, 06) ; BV Services (BV Froid) 7,6 M€ / +0,2 M€ (2024, 60) ; France Froid 7,4 M€ / +0,6 M€ (2025, Martinique) ; Froid Equipement Service 6,3 M€ / +0,1 M€ (2024, 42) ; Gener Froid 5,3 M€ / +0,2 M€ (2025, 13) ; Comaintef 5,3 M€ / +0,6 M€ (2024, 33) ; Applic Froid 4,0 M€ / +0,6 M€ (2025, 33). Allier Froid Clim : CA confidentiel, résultat +0,34 M€ (2025). Savelys (Engie Home Services) : 543,7 M€ / +5,3 M€ (2025, résidentiel).
- Ce que ça dit pour nous : une trentaine d'acteurs régionaux de 1,5 à 20 M€ ; marges nettes de 1 à 12 % ; les deux plus gros sur le froid pur perdent de l'argent : marché fragmenté mais peu rentable. Correction de S1-17 : Azur Trucks Froid -1,2 M€ (résultat net), pas -1,3 M€ de CA.

### F-7 : Saturation des frigoristes et pression des restaurants en canicule (presse)
- Acteur / marché : frigoristes parisiens ; clients restaurants, cafétérias
- Type : plainte
- Source : https://www.linfodurable.fr/cinquante-appels-par-jour-les-frigoristes-satures-en-pleine-canicule-51873 (date : 2025-07-02 ; niveau N3 ; émetteur : L'info durable, reportage)
- Citation : « plus de 50 appels par jour pour des dépannages »
- Citation 2 : « Ils nous harcèlent quand la chambre froide tombe en panne »
- Chiffres : un frigoriste annonce 16 heures par jour ; demandes de devis Engie Home Services 8 374 en juin 2025 contre 2 931 en juin 2024 (climatisation) ; secteur « près de 14 000 entreprises » en 2022.
- Ce que ça dit pour nous : le délai est un vrai point de douleur en pic de chaleur, mais la capacité technique est saturée : garantir un délai suppose des techniciens en réserve.

### F-8 : Obligation de faire intervenir un opérateur titulaire de l'attestation de capacité et de contrôler l'étanchéité (Code de l'environnement)
- Acteur / marché : détenteurs d'équipements frigorifiques (restaurants) ; opérateurs de maintenance
- Type : obligation réglementaire
- Source : https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006074220/LEGISCTA000006188988/ (date : 2026-11-03 ; niveau N1 ; émetteur : Légifrance, articles R543-78 à R543-83)
- Citation : aucune (la lecture a rendu un résumé de page, pas le texte mot à mot ; contenu à recopier avant la porte 2)
- Chiffres : R543-78 : le détenteur fait réaliser les opérations sur le circuit par un opérateur disposant de l'attestation de l'article R543-99 ; R543-79 : contrôle d'étanchéité obligatoire au-delà de 2 kg de HCFC ou 5 tonnes équivalent CO2 de HFC/PFC, par un opérateur titulaire, renouvelé périodiquement selon arrêté ; R543-79-1 : copie du constat à l'État au-delà de 500 t éq. CO2 ; R543-80 : conservation 5 ans des documents au-delà de 5 t éq. CO2 ; R543-82 : fiche d'intervention signée par l'opérateur et le détenteur, conservée 5 ans.
- Ce que ça dit pour nous : le client a une obligation légale de faire contrôler et d'archiver : argument de vente (registre fourni dans l'abonnement), mais l'entreprise doit détenir l'attestation.

### F-9 : Attestation de capacité (R543-99) : durée, établissement, organisme
- Source : https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006839333 (date : 2026-11-03 ; niveau N1 ; émetteur : Légifrance, article R543-99)
- Type : obligation réglementaire
- Citation : aucune (résumé de page, non mot à mot)
- Chiffres : l'opérateur obtient l'attestation délivrée par un organisme agréé ; une attestation par établissement ; durée de 5 ans au plus ; l'organisme vérifie les conditions de capacité professionnelle (R543-106) et l'outillage ; l'attestation précise types d'équipements et d'activités. Un arrêté du 21 novembre 2025 remplace l'arrêté du 30 juin 2008 sur la délivrance (extrait de recherche non ouvert : https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000052993429, N5, piste).
- Ce que ça dit pour nous : licence obligatoire, délivrée par organisme agréé, coût et délai non chiffrés [HYPOTHÈSE : quelques centaines à milliers d'euros par technicien et par entreprise ; non sourcé].

### F-10 : Fréquence des contrôles d'étanchéité selon la charge (arrêté du 29 février 2016, article 4)
- Source : https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000038980393 (date : 2026-11-03 ; niveau N1 ; émetteur : Légifrance)
- Type : obligation réglementaire
- Citation : aucune (tableau rendu par la page ; reproduit ci-dessous)
- Chiffres : HFC/PFC de 5 à moins de 50 t éq. CO2 : tous les 12 mois, 24 mois avec détection de fuites permanente ; de 50 à moins de 500 t : 6 mois, 12 mois avec détection ; 500 t et plus : 3 mois (mobile) ou 6 mois (fixe), 6 mois avec détection. HCFC : 2 à 30 kg 12 mois, 30 à 300 kg 6 mois, plus de 300 kg 3 mois. Le règlement UE 2024/573 article 4 reprend ces seuils (5, 50, 500 t) d'après la FAQ ministère, texte UE non lu (EUR-Lex illisible par l'outil).
- Ce que ça dit pour nous : une chambre froide de restaurant (quelques kg de HFC, souvent en dessous de 5 t éq. CO2) n'est souvent pas soumise au contrôle périodique ; une centrale de supermarché ou de boucherie l'est. À vérifier site par site : [HYPOTHÈSE] charge typique d'un groupe de chambre froide, non sourcée. Ceci réduit le caractère obligatoire de la visite pour la cible restaurants.

### F-11 : Moteur daté : fin des fluides régénérés à fort PRG en réfrigération (2030)
- Source : https://www.capeb.fr/actualites/fluides-frigorigenes-attestation-de-capacite (date : 2026-03-30 ; niveau N2 ; émetteur : CAPEB, fédération professionnelle ; texte du règlement non lu)
- Type : tendance structurelle
- Citation : « les fluides régénérés ou recyclés avec PRP/GWP ≥ 2500 pour la réfrigération seront interdits »
- Chiffres : au 1er janvier 2030 pour la réfrigération ; 2032 pour la climatisation et les pompes à chaleur ; aucun terme pour les fluides régénérés sous 2500 (R448A, R449A cités). Le règlement 2024/573 est « entré en vigueur le 11 mars 2024 » avec un objectif de réduction de 79 % des HFC entre 2015 et 2030 (https://www.ecologie.gouv.fr/politiques-publiques/substances-impact-climatique-fluides-frigorigenes, 2026-11-03, N2, ministère).
- Ce que ça dit pour nous : un moteur daté existe (renouvellement ou conversion des groupes aux fluides à fort PRG avant 2030) ; quels fluides sont dans les parcs de restaurants n'est pas établi [HYPOTHÈSE]. L'annexe IV (interdictions de mise sur le marché de la réfrigération commerciale) n'a pas pu être lue.

### F-12 : Obligation de température des denrées (HACCP) qui rend la chambre froide critique
- Source : https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000041864893 (date : 2026-11-03 ; niveau N1 ; émetteur : Légifrance, arrêté du 21 décembre 2009, annexe I)
- Type : obligation réglementaire
- Citation : « doivent être conformes en tous points du produit aux températures définies dans le tableau »
- Chiffres : en vente directe et restauration collective : viande hachée +2 °C ; abats +3 °C ; préparations de viande, volaille +4 °C ; poisson frais +2 °C ; autres denrées très périssables +4 °C ; préparations culinaires prêtes +3 °C ; autres denrées périssables +8 °C.
- Ce que ça dit pour nous : une panne de froid expose à la perte de marchandise et à une non-conformité ; justifie un délai garanti (valeur du stock à sauver non chiffrée [HYPOTHÈSE]).

### F-13 : Restaurants en procédure collective (risque de perte de clients)
- Source : https://bodacc-datadila.opendatasoft.com/api/explore/v2.1/catalog/datasets/annonces-commerciales/records?where=familleavis%3D%22collective%22+and+search%28%22restauration+traditionnelle%22%29&select=count%28%2A%29+as+annonces&group_by=year%28dateparution%29&limit=30 (date : 2026-11-03 ; niveau N1 ; émetteur : DILA, BODACC)
- Type : contre-preuve
- Citation : aucune (donnée API)
- Chiffres : annonces « restauration traditionnelle » : 3 309 (2022), 4 523 (2023), 5 221 (2024), 5 682 (2025) ; 2026 : 4 991 à ce jour. Plusieurs annonces par entreprise possibles. « froid commercial » : 168 (2022) à 325 (2025), 301 (2026) : recherche plein texte, mélange restaurants et fournisseurs, non exploitable pour les frigoristes.
- Ce que ça dit pour nous : la clientèle cœur (restaurants) fait de plus en plus faillite : désabonnements et impayés attendus ; le segment cuisines collectives et commerces de bouche est plus stable [HYPOTHÈSE].

### F-14 : Salaire et tarif journalier d'un frigoriste (ordre de grandeur)
- Source : https://travail-industrie.com/fiche-tjm/technicien-frigoriste (date : 2026 ; niveau N4 ; émetteur : travail-industrie.com, méthode non publiée)
- Type : tendance
- Citation : « Le tarif journalier observé se situe entre 400 et 600 € HT »
- Chiffres : même page, corps de texte : 200 à 450 € HT par jour, médiane 310 € ; la page se contredit. Offres France Travail (extrait de recherche, non ouvert car 404 à l'ouverture, N5 donc piste) : 2 300 à 3 000 € brut par mois pour un technicien à Bordeaux.
- Ce que ça dit pour nous : coût du technicien [HYPOTHÈSE] 2 500 € brut mensuel, soit environ 42 000 € chargé par an [calcul : 2 500 × 12 × 1,4].

### F-15 : Concurrent à contre-emploi : « ne rien faire » et dépannage à la demande
- Source : F-1 (60 €/h + 60 € de déplacement) et https://www.linfodurable.fr/cinquante-appels-par-jour-les-frigoristes-satures-en-pleine-canicule-51873 (N3, 2025-07-02)
- Type : contre-preuve
- Citation : « le manque d'entretien est la cause principale des pannes de climatisation et de réfrigération en été »
- Chiffres : coût d'un dépannage à la demande : 60 € de déplacement + 2 h × 60 € = 180 € HT hors pièces [calcul à partir de F-1] ; un abonnement à 1 200 € HT équivaut à 6 dépannages.
- Ce que ça dit pour nous : le restaurateur peut rationnellement ne rien payer et appeler à la panne : l'abonnement doit se justifier par le délai et la perte de stock évitée. (La citation est celle d'un professionnel rapportée par la presse, reprise du résumé de la recherche web, non retrouvée mot à mot dans la page : à retirer si le script la déclare absente.)

## 2. Concurrents réels (nom, offre, prix, taille, avis, faiblesses)
| # | Concurrent | Offre | Prix public | Taille (N1) | Avis | Faiblesse citée |
|---|---|---|---|---|---|---|
| 1 | Dalkia Froid Solutions (ex Cesbron) | froid commercial et industriel, maintenance, national | non publié | 226,6 M€, résultat -5,0 M€ (F-6) | non établi | perte de 5,0 M€ : la taille ne garantit pas la rentabilité |
| 2 | Paris Froid Services | dépannage et maintenance froid, IDF | non publié | 20,4 M€, +0,5 M€, 20-49 salariés (F-6) | non établi (S1-24 couvre Azur Froid, 5 avis, tous 5 étoiles) | non établie |
| 3 | Froid & Services Méditerranée | idem, Sud-Est | non publié | 13,2 M€, +1,1 M€ | non établi | non établie |
| 4 | BV Services (BV Froid), BV, Gener Froid, Comaintef, Applic Froid... | spécialistes régionaux, 4 à 8 M€ | non publié | F-6 | non établi | non établie |
| 5 | Allier Froid Clim | préventif + dépannage cuisines pro, Auvergne | 680 € HT/an, 60 €/h, 60 € déplacement (F-1) | 10-19 salariés, résultat +0,34 M€ | non établi | « sans aucune garantie » de planning ; lundi-vendredi 8-17 h (F-1) |
| 6 | Entreprise Mollière | contrat P2 dépannages inclus, Loiret | 3 892 € HT/an pour 4 sites (F-2) | 20-49 salariés, résultat +0,25 M€ | non établi | non établie |
| 7 | Savelys / Engie Home Services | résidentiel, climatisation, chaudières (indirect) | non publié | 543,7 M€, +5,3 M€ ; devis ×2,9 en juin 2025 (F-7) | non établi | débordé en canicule (F-7) |
| 8 | Diagnostic distant freelance (ComeUp) | diagnostic par vidéo | 40 € (F-3) | 0 vente | aucun | pas d'intervention sur site |
| 9 | Faire soi-même / ne rien faire | dépannage à la demande | 60 €/h + 60 € déplacement (F-1) | | | délai variable ; stock perdu (F-7) |
| 10 | Constructeurs et distributeurs (SAV réseau) | SAV du matériel vendu | non établi | non établi | non établi | non établi |
Avis clients : aucun avis négatif sur un frigoriste n'a pu être lu (Trustpilot, S1-24 : 5 avis tous 5 étoiles ; la recherche d'avis n'a rendu que des annuaires). Faiblesses sourcées réelles : absence de garantie de délai (F-1), saturation en canicule (F-7). « Non établi » pour les avis de 8 concurrents.

## 3. Pourquoi le leader ne fait pas déjà cet angle, et comment il nous écrase en 6 mois
- Ce que le contrat concurrent contient (F-1, F-2) : forfait de visite ou de dépannage inclus, sans garantie de délai. Aucun acteur n'a été trouvé qui affiche un délai garanti en heures sur son site (non établi : recherche non exhaustive, 15 recherches).
- Pourquoi : garantir un délai impose des techniciens d'astreinte, ressource rare (S1-20 : 81 % de recrutements difficiles) ; les régionaux vendent des travaux et des pièces (CA/salarié de Paris Froid Services supérieur à 400 k€ [calcul : 20,4 M€ / 49 salariés au plus] contre environ 180 k€ pour un technicien d'abonnement, voir §5).
- Avocat du diable : Dalkia, Paris Froid Services ou un régional de 5 M€ peut ajouter une option « intervention sous 4 h » à son contrat en moins de 3 mois : c'est un avenant tarifaire sur un parc de techniciens et de clients déjà là. Il a déjà la densité de tournée et l'attestation. Notre seul avantage serait de ne vendre que cela, et il ne résiste pas à une copie : l'avantage est la capacité d'astreinte, que le leader possède déjà. Délai de copie estimé : 3 à 6 mois [HYPOTHÈSE].

## 4. Prédécesseurs qui ont échoué
- Spécialiste de l'abonnement préventif froid à délai garanti ayant échoué : non trouvé (aucune presse ni annonce BODACC nominative lue). Non établi.
- Signal agrégé : annonces « maintenance industrielle » 287 (2020) → 458 (2025) ; « froid commercial » 168 (2022) → 325 (2025) (S1-23, F-13) : plein texte non nominatif, non exploitable.
- Pertes des gros : Dalkia Froid Solutions -5,0 M€, Azur Trucks Froid -1,2 M€ (F-6).

## 5. Cadre juridique (vérifié sur Légifrance sauf mention)
| Règle | Article | Source | Niveau |
|---|---|---|---|
| Opérateur titulaire de l'attestation de capacité pour toute opération sur le circuit frigorifique | R543-78, R543-99 (Code de l'environnement) | F-8, F-9 | N1 |
| Attestation : organisme agréé, 5 ans maximum, une par établissement, outillage vérifié | R543-99, R543-106 | F-9 | N1 |
| Contrôle d'étanchéité à partir de 5 t éq. CO2 de HFC/PFC ; périodicité 12/6/3 mois (24/12/6 avec détection) | R543-79 ; arrêté du 29 février 2016, art. 4 | F-8, F-10 | N1 |
| Fiche d'intervention signée, conservée 5 ans ; registre du détenteur | R543-80, R543-82 | F-8 | N1 |
| Règlement F-gas UE 2024/573 (en vigueur 11 mars 2024) ; certification des personnes (règlement d'exécution UE 2024/2215) ; interdiction des fluides régénérés ≥ 2500 PRG en réfrigération au 1er janvier 2030 | art. 4 (contrôles) ; calendrier : CAPEB | F-10, F-11 | texte UE non lu ; N2 pour le calendrier |
| Températures des denrées (HACCP, vente directe et restauration collective) | arrêté du 21 décembre 2009, annexe I | F-12 | N1 |
| Assurance responsabilité civile professionnelle de l'entreprise de froid ; garantie décennale non applicable à la maintenance | [HYPOTHÈSE JURIDIQUE] non vérifiée : compte comme risque |  |  |
| Démarchage téléphonique B2B, avis d'accord de reconduction tacite, clauses de pénalité de retard (responsabilité en cas de stock perdu) | [HYPOTHÈSE JURIDIQUE] non vérifiée : compte comme risque |  |  |
| Page de précommande (porte 2) | L.121-2, L.121-3, L.221-5, L.221-14, L.221-18 (voir CLAUDE.md) ; la rétractation de 14 jours concerne les consommateurs : pour un restaurateur professionnel, applicabilité de L.221-3 (professionnel de moins de 5 salariés, hors champ de son activité principale) non vérifiée | [HYPOTHÈSE JURIDIQUE] |  |
Bilan juridique : licence obligatoire (attestation) vérifiée ; aucune carte professionnelle ni diplôme exigé par ces articles au-delà de la capacité professionnelle de R543-106 (contenu non lu).

## 6. Économie unitaire
Hypothèses explicites (aucun prix privé publié ne les confirme) :
| Poste | Valeur | Source / calcul |
|---|---|---|
| Prix de l'abonnement avec délai garanti | 1 200 € HT/an/site (fourchette 900 à 1 200) | F-1 : 680 € (1 visite) ; F-2 : environ 970 € par site dépannages inclus ; prime délai [HYPOTHÈSE] |
| Prix dépannage hors contrat | 60 €/h + 60 € déplacement | F-1 |
| Coût technicien chargé | 42 000 €/an + véhicule, outillage, assurance 12 000 €/an = 54 000 € | F-14 N4 et N5 ; coefficient 1,4 [HYPOTHÈSE] |
| Heures facturables par technicien | 1 400 h/an [HYPOTHÈSE] | 1 600 h travaillées dont temps non facturé |
| Heures par client et par an | 2 visites × (2 h + 1 h de trajet) + 1 dépannage de 3 h = 9 h | [HYPOTHÈSE] |
| Clients par technicien | 1 400 / 9 = environ 155 | calcul |
| CA par technicien | 155 × 1 200 = 186 000 € | calcul |
| Coût direct par client | 9 h × (54 000 / 1 400 = 38,6 €/h) = 347 € + pièces | calcul |
| Marge brute avant astreinte et structure | environ 71 % [calcul : (1 200 - 347) / 1 200] | |
| Revenu par heure de travail | 1 200 / 9 = 133 €/h (contre 60 €/h en dépannage F-1) | calcul |
| Astreinte week-end (délai garanti) | au moins 2 techniciens pour une rotation ; coût [HYPOTHÈSE] 6 000 €/an par technicien en prime | non sourcé |
| Coût d'acquisition d'un client | 300 à 500 € [HYPOTHÈSE] : 10 à 12 h de démarchage terrain et téléphone par contrat signé à 35 €/h chargé | non sourcé ; à mesurer à la porte 2 |
| Clients pour 500 k€ de CA | 500 000 / 1 200 = 417 contrats (556 à 900 €) = 3 techniciens | calcul ; 417 / 97 430 = 0,43 % du parc ≥ 3 salariés (F-5) |
| Capital avant le premier client | 1 technicien (fondateur) + véhicule aménagé + outillage froid + attestation + assurance : [HYPOTHÈSE] 40 000 à 80 000 € ; non sourcé | |
| Délai avant le premier client | attestation de capacité (organisme agréé : délai non établi) + 1 à 3 mois de démarchage [HYPOTHÈSE] | |
Recrutement : 2 950 projets en 2026, 81 % jugés difficiles, 84 % en Île-de-France (S1-20, N3). Le deuxième et le troisième technicien sont le goulot : sans eux, plafond d'environ 186 k€ de CA par technicien.
Taille bottom-up : 97 430 employeurs de 3 salariés ou plus × 900 à 1 200 € = 88 à 117 M€ de dépense potentielle si tous achetaient un abonnement [calcul, prix [HYPOTHÈSE]] ; au-dessus du seuil de 50 M€. Sans prix privé confirmé, la taille est un plafond non prouvé.

## 7. Seuils de CLAUDE.md
| Critère | Valeur trouvée | Source | Niveau | Réussi / raté |
|---|---|---|---|---|
| Taille SAM ≥ 50 M€ | 88 à 117 M€ (97 430 × 900-1 200 €), prix [HYPOTHÈSE] ; DECP : 39,5 M€ de marchés « maintenance froid » en 2025 | F-5, F-4, S1-22 | N1 + hypothèse | réussi sous réserve |
| Croissance ≥ 8 %/an ou moteur daté | 33.12 : +5,0 %/an sur 3 ans (INSEE), +6,3 % sur 5 ans ; Eurostat +15,5 %/an 2021-2024 en valeur ; moteur 2030 (fluides régénérés ≥ 2500) | fiche 33.12 (S1), F-11 | N1, N2 | raté en chiffre ; moteur daté partiel (souhaité, pas éliminatoire) |
| Concentration (3 premiers < 40 %) | 11,9 % pour 33.12 (2024) | fiche 33.12 | N1 | réussi |
| Clients ≥ 3 000 (B2B) | 97 430 (≥ 3 salariés) à 146 207 | F-5 | N1 | réussi |
| SOM 3 ans ≥ 500 k€ | 417 contrats à 1 200 €, 3 techniciens ; 0,43 % du parc | F-5 + hypothèses §6 | N1 + hypothèse | non établi : atteignable sur le papier, goulot de recrutement |
| Argent déjà dépensé | CA secteur 12,7 Md€ ; plus de 10 acteurs avec CA déposé (F-6) ; ≥ 3 prix publics : 3 prix chez Allier Froid Clim (F-1), 1 prix chez Mollière (F-2), 1 prix ComeUp (F-3) ; DECP (F-4) | fiche, F-1 à F-6 | N1, N2 | réussi pour les acteurs ; prix : 3 émetteurs, tous publics ou indirects, aucun prix privé d'abonnement restaurant : réussi sous réserve |
| Engagement client | non testé | | | porte 2 à faire |
| Ressources | attestation de capacité ; 40-80 k€ [HYPOTHÈSE] ; 3 techniciens | F-9, §6 | | décrit, non éliminatoire |

## 8. Notation (CLAUDE.md, section « Notation »)
Classe de référence : NAF 33.12Z / 43.22B, sociétés. SINE génération 2018 : industrie 73,4 % à 5 ans, sociétés 70,6 % (`methode/sources-fiables.md`). Taux de base à 3 ans : environ 80 % [HYPOTHÈSE, interpolation non sourcée].
| Probabilité (date 2026-11-03) | Ancienne (pistes-v5) | Nouvelle | Preuves N1-N2 qui écartent du taux de base |
|---|---|---|---|
| P(passer la porte 2) | 30 % | 25 % | F-1, F-2 (N2) : prix public constaté 680 à 970 € par site, pas 1 200 ; F-1 : aucun concurrent vu ne garantit de délai (signal positif, un seul émetteur, contexte public) ; F-10 : contrôle périodique non obligatoire sous 5 t éq. CO2. Aucune action de client. |
| P(être en vie à 3 ans) | 80 % | 75 % | F-6 (N1) : marges nettes de 1 à 12 %, les deux plus gros acteurs du froid perdent de l'argent ; F-13 (N1) : faillites de restaurants 3 309 → 5 682 (2022-2025) : risque d'impayés et de résiliations. Positif : capital faible. |
| P(CA ≥ 500 k€ à 3 ans) | 30 % | 20 % | F-6 (N1) : entreprises créées en 2010 à 1,9 à 2,6 M€ après 12 à 16 ans (RCIM 2,6 M€ en 2025, Froid Champagne-Ardenne 1,9 M€ en 2024, Arras Froid Services 2,4 M€ en 2022), pente d'environ 0,15 à 0,2 M€ par an ; §6 : 417 contrats et 3 techniciens en 3 ans dans un métier à 81 % de recrutements difficiles (S1-20, N3, ne déplace pas seul). |
Les pistes concurrentes du classement v5 étant à 20-35 % : à moins de 10 points d'écart, on teste les deux.

## 9. Test de porte 2 (légal, sans entretien)
- Cible : restaurants traditionnels et rapides, boulangeries-pâtisseries et boucheries, 3 salariés ou plus, dans une seule zone de 60 min de trajet (une agglomération) ; 97 430 unités au total dans la France entière (F-5).
- Page : « abonnement froid : 2 visites par an + intervention sous X heures, 7 jours sur 7 » ; dire que le service ouvre à une date précise (L.121-2, L.121-3) ; dépôt remboursable de 150 € (soit 1 mois d'abonnement) avec bouton « commande avec obligation de paiement » (L.221-14) ; lien RGPD article 13 ; la rétractation consommateur (L.221-18) ne s'applique pas automatiquement à un professionnel : [HYPOTHÈSE JURIDIQUE] à vérifier avant publication.
- Trafic : annonces ciblées « dépannage chambre froide » + démarchage ciblé par courrier postal à 500 établissements de la zone ; budget [HYPOTHÈSE] 1 500 € au total.
- Seuil écrit avant : sur 500 établissements contactés et 1 500 € de trafic, au moins 10 dépôts (2 %), soit un coût par dépôt d'au plus 150 € ; en dessous de 5 dépôts, STOP. Calcul : 10 dépôts × 1 200 € = 12 000 € de CA annuel engagé contre 1 500 € dépensés, payback de 4 mois sur marge de 71 %. Le seuil de 3 sur 10 proposé par S1 est irréaliste pour une page non sollicitée : les entretiens sont exclus, il faut le formuler en pourcentage de visiteurs, pas de contacts.
- Variante à tester en parallèle : cuisines collectives et EHPAD (marchés publics : 144 marchés « maintenance froid » en 2025, F-4) plutôt que restaurants, car moins de faillites.

## 10. Verdict
- Ce qui tient : taille et nombre de clients (97 000 employeurs, ≥ 3 salariés), argent déjà dépensé (acteurs, DECP), obligations légales vérifiées (R543-78, R543-79, R543-99, arrêté 2009), absence de garantie de délai dans le contrat vu (F-1).
- Ce qui casse : aucun prix privé d'abonnement ; ticket public de 680 à 970 € par site, bien sous le prix à 1 200 € supposé ; les gros du froid perdent de l'argent ; le délai garanti repose sur la ressource la plus rare (techniciens) ; le leader copie en 3 à 6 mois ; clientèle restaurants en faillite croissante.
- Meilleure variante : vendre l'abonnement aux cuisines collectives, commerces de bouche et petites chaînes de restauration (moins de faillites, contrats publics notifiés), avec le registre légal et le rapport numérique inclus, plutôt que « le délai garanti » seul ; tester d'abord une zone.

## Sources non lues / bloquées
- https://eur-lex.europa.eu/legal-content/FR/TXT/HTML/?uri=CELEX:02024R0573-20240220 (page vide pour l'outil) ; texte du règlement 2024/573 et annexe IV non lus.
- https://www.ecologie.gouv.fr/sites/default/files/documents/FAQ%20%20vf.pdf (erreur réseau).
- https://candidat.francetravail.fr/offres/recherche/detail/6058735 (404).
- https://www.boamp.fr/telechargements/FILES/PDF/2025/08/25-96103.pdf (PDF illisible).
- https://modelesdebusinessplan.com/blogs/infos/climatisation-rentabilite (429).
- https://mapa.aji-france.com/mapa/file/marche/126140/CCATP%20-%20Maintenance%20des%20installations%20frigorifiques.pdf (404).
- Modèle étranger : non établi (résultats américains = annonces de cession et profils PitchBook, N5, non ouverts) ; CA audité SEC/Companies House non lu.
- Avis clients des frigoristes : non établis (extraits PagesJaunes non ouverts).

## Contrôle
RESUME : OK=8, ABSENT=2, BLOQUE=0, EXTRAIT=0. Les 2 ABSENT (F-1, F-2) sont des PDF de mairies à texte compressé que le script ne sait pas lire ; les deux citations ont été retrouvées par extraction pypdf du PDF le 2026-11-03 (F-1 : « Montant H.T 680 », « sans aucune garantie de » ; F-2 : texte exact de la décision n° 2025-013). F-8, F-9, F-10 n'ont pas de citation mot à mot (résumés de page Légifrance) : à recopier avant la porte 2.
