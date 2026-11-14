# Une idée France : fichier de travail (porte 1, tous secteurs)
Mission : 5 modèles qui encaissent en France, marché daté, acteurs faibles. Date : 2026-11-02.
Recherches web utilisées : 4 / 15 (arrêt anticipé, voir statut). Preuves valides : 5 (pages ouvertes) + 4 mesures API. Domaines : companeo.com, amf.asso.fr, cci-paris-idf.fr, ecologie.gouv.fr, recherche-entreprises.api.gouv.fr, fr.trustpilot.com.
Règle : seules les pages ouvertes en WebFetch servent. Statut : PARTIEL (2 pistes sur 5 partiellement documentées).
Exclus (déjà dans les archives, Grep) : facture électronique, NIS2, Mon Accompagnateur Rénov', DPE/diagnostics.

### U-FRA-01 : DAE, obligation étendue aux ERP de 5e catégorie
- Acteur / marché : vente, installation, maintenance de défibrillateurs aux ERP
- Type : obligation
- Source : https://www.amf.asso.fr/documents-defibrillateurs-automatises-externes--obligations-communes/43369 (date inconnue ; ouverte)
- Citation : « Depuis le 1er janvier 2022, cette obligation concerne également les ERP de catégorie 5 »
- Chiffres : décret du 5 décembre 2025 élargit à d'autres ERP de 5e catégorie ; arrêté sur le seuil de fréquentation non publié ; aucun nombre d'ERP donné.
- Ce que ça dit pour nous : dépense obligatoire en extension, périmètre exact encore flou (risque).

### U-FRA-02 : DAE, prix publics
- Acteur / marché : Companeo (comparateur) pour fournisseurs de DAE
- Type : argent dépensé (fourchettes indicatives, pas des prix payés nominatifs)
- Source : https://www.companeo.com/defibrillateur/guide/dae-cout-installation-comparatif (publié 2025-06-02, MAJ 2026-10-26 ; ouverte)
- Citation : « La maintenance périodique et tests de conformité (150 € à 350 €/an) »
- Chiffres : automatique 1 000-1 800 € HT ; semi-auto 850-1 600 € HT ; connecté 1 300-2 800 € HT ; batteries 65-200 € ; électrodes 65-185 €/paire. Aucun prix de location trouvé.
- Ce que ça dit pour nous : maintenance récurrente 150-350 €/an par appareil = revenu récurrent ; reste à prouver qui paie réellement (CA d'acteurs non trouvé).

### U-FRA-03 : Biodéchets, obligation pour tous les professionnels
- Acteur / marché : collecte de biodéchets pour restaurants et commerces alimentaires
- Type : obligation
- Source : https://www.ecologie.gouv.fr/biodechets (publié 2023-09-15, MAJ 2023-12-27 ; ouverte)
- Citation : « le tri des biodéchets a été généralisé et concerne tous les professionnels et particuliers »
- Chiffres : en vigueur depuis 2024-01-01 (date issue d'un extrait, non reprise ici comme chiffre vérifié)
- Ce que ça dit pour nous : dépense obligatoire déjà active, donc paiement réel possible dès maintenant ; pas de croissance chiffrée (aucune source institutionnelle de volume).

### U-FRA-04 : Biodéchets, prix publics des prestataires
- Acteur / marché : Les Joyeux Recycleurs, Moulinot, abonnements de collecte
- Type : argent dépensé
- Source : https://www.entreprises.cci-paris-idf.fr/web/transition-ecologique/transition-ecologique-des-tpe-et-pme-valorisation-des-dechets (2024-11-05 ; ouverte)
- Citation : « un coût mensuel fixe qui commence à 60€ par mois »
- Chiffres : « généralement plafonnés autour de 100€ mensuels » ; Moulinot : tarif variable au volume (prix non publié). Seulement 1 prix public chiffré sur 3 requis.
- Ce que ça dit pour nous : ticket 60-100 €/mois, soit ~720-1 200 €/an par client ; il faut ~420-700 clients pour 500 k€.

### U-FRA-05 : Biodéchets, CA et pertes du leader (CONTRE-PREUVE)
- Acteur / marché : Moulinot Compost & Biogaz (SIREN 798298899) et filiales
- Type : contre-preuve
- Source : https://recherche-entreprises.api.gouv.fr/search?q=moulinot compost biogaz (API ouverte, 2026-11-02)
- Citation : « 'ca': 10866171, 'resultat_net': -2359387 » (exercice 2024, champ finances)
- Chiffres : Moulinot Nouvelle-Aquitaine CA 1 442 288 €, résultat -1 031 268 € ; Moulinot Pays de la Loire CA 266 462 €, résultat -1 003 114 € (2024). P.B. Collector (SIREN 490249570) : CA 814 079 €, résultat -4 531 € (2024) ; lien avec Hector le Collector NON établi.
- Ce que ça dit pour nous : le leader perd 2,4 M€ pour 10,9 M€ de CA : le modèle est difficile à rentabiliser, pas seulement mal servi.

### U-FRA-06 : Nombre de clients identifiables (API Sirene, actifs, 2026-11-02)
- Type : tendance (taille)
- Source : https://recherche-entreprises.api.gouv.fr/search?activite_principale=56.10A&etat_administratif=A&per_page=1 (ouverte)
- Chiffres : 56.10A (restauration traditionnelle) > 10 000 (plafonné) ; 56.10C > 10 000 ; 93.13Z (salles de sport) 5 901 ; 55.10Z (hôtels) > 10 000 ; 85.10Z 218. Établissements actifs de la base, non filtrés par effectif ni par obligation.
- Ce que ça dit pour nous : le seuil de 3 000 clients B2B est largement dépassé pour la restauration (biodéchets).

### U-FRA-07 : Avis clients indisponibles
- Type : contre-preuve (donnée manquante)
- Source : https://fr.trustpilot.com/review/www.lesjoyeuxrecycleurs.com (ouverte)
- Citation : « Cette entreprise n'a pas encore reçu d'avis. »
- Chiffres : 0 avis ; page Moulinot sur Trustpilot : HTTP 404.
- Ce que ça dit pour nous : la faiblesse des acteurs n'est PAS prouvée par les avis ; critère « avis négatifs nombreux » non rempli.

## Sources non lues
- https://chubbfs.com/.../CHUBB_Offre-Defibrillateurs-Cle-en-main.pdf : PDF compressé illisible [NON OUVERT].
- entreprendre.service-public.gouv.fr/vosdroits/F36203 : la page ne traitait pas des biodéchets.
- Toute la section facturation/NIS2/DPE : exclue (archives).

## Lot 2 (session de reprise) - recherches web cumulées : 15 / 15 (12 + 3 ; budget atteint)

### U-FRA-08 : Biodéchets, 2e contre-preuve (Les Alchimistes)
- Acteur / marché : Les Alchimistes SAS (SIREN 824298343), collecte et compost pour pros
- Type : contre-preuve
- Source : https://recherche-entreprises.api.gouv.fr/search?q=les alchimistes (API ouverte, 2026-11-02)
- Citation : « 'ca': 6375821, 'resultat_net': -1946911 » (exercice 2024)
- Chiffres : CA 6,4 M€, résultat -1,9 M€. Deux leaders sur deux déficitaires (avec U-FRA-05).
- Ce que ça dit pour nous : la collecte de biodéchets ne se rentabilise pas à cette échelle ; piste à déclasser.

### U-FRA-09 : Biodéchets, prix et avis : recherche négative
- Type : contre-preuve (donnée manquante)
- Source : recherches web sur Hector le Collector, Cycle Up, Alchimistes ; pages ouvertes : lejournaldesentreprises.com (2021-11-30) sans tarif ni client ; PDF 3rdanjou.fr illisible [NON OUVERT].
- Citation : sans objet
- Chiffres : aucun prix supplémentaire vérifié ; aucun avis Google/Trustpilot trouvé. Le prix de 23 €/échange de bac vu en extrait n'est PAS utilisé.
- Ce que ça dit pour nous : biodéchets reste à 1 prix public sur 3 ; faiblesse des acteurs non prouvée.

### U-FRA-10 : DUERP, prix d'un prestataire (obligatoire dès le 1er salarié)
- Acteur / marché : réalisation du document unique pour TPE/PME
- Type : argent dépensé (prix affichés, aucun paiement constaté)
- Source : https://www.plateya.fr/blog/detail/cout-duerp-2026-et-nouvelles-sanctions-ce-que-dit-la-loi (2026 ; ouverte ; vendeur = confiance faible)
- Citation : « dès l'embauche du premier salarié »
- Chiffres : 1-5 salariés 489-750 € HT ; 6-10 : 750-1 200 € ; 11-25 : 1 200-1 800 € ; 26-50 : 1 800-2 500 €. Amende administrative annoncée jusqu'à 4 000 €/salarié (loi du 11 mai 2026 selon la même page, non vérifiée officiellement).
- Ce que ça dit pour nous : ticket 500-2 500 € ponctuel (mise à jour annuelle dès 11 salariés) ; une seule source de prix.

### U-FRA-11 : DUERP, marketplace : prix bas et zéro vente (CONTRE-PREUVE)
- Type : contre-preuve
- Source : https://comeup.com/en/service/508181/realiser-votre-duerp-conforme-pour-votre-tpe-pme-a-distance et https://comeup.com/fr/service/523525/rediger-votre-duerp-conforme-au-code-du-travail-par-un-expert-hse (ouvertes)
- Citation : « Le DUERP est OBLIGATOIRE pour toute entreprise française dès le 1er salarié. »
- Chiffres : offres à 143,26 € et 71,64 € TTC ; 0 vente affichée sur chacune ; la seconde « n'est actuellement pas disponible ».
- Ce que ça dit pour nous : des freelances vendent à 65-130 € ; le prix TPE de 489 € est tiré vers le bas.

### U-FRA-12 : DUERP, portail de dépôt non disponible (contre-preuve sur le moteur)
- Type : contre-preuve
- Source : https://www.inrs.fr/publications/juridique/focus-juridiques/focus-juridique-document-unique-evaluation-risques.html (MAJ 2024-10-04 ; ouverte)
- Citation : « à ce jour, le portail dématérialisé n'est toujours pas disponible »
- Chiffres : aucune date d'application du dépôt pour les petites entreprises sur la page. Situation actuelle non vérifiée (page de 2024).
- Ce que ça dit pour nous : le moteur « dépôt obligatoire 2025-2028 » n'est pas daté ; ne pas le supposer.

### U-FRA-13 : Ramonage, prix publics (2 sources)
- Acteur / marché : ramoneurs artisans, particuliers
- Type : argent dépensé (prix affichés)
- Source : https://www.groupama.fr/assurance-habitation/conseils/prix-ramonage/ (MAJ 2026-01-06) et https://travaux.obat.fr/guides/prix-ramonage-cheminee/ (MAJ 2024-10-24) ; ouvertes
- Citation : « une amende forfaitaire de 3ᵉ classe pouvant aller jusqu'à 450 € »
- Chiffres : foyer ouvert 40-90 € ; fermé 50-130 € ; gaz 40-85 € ; fioul 50-85 € TTC (Groupama). Classique 60-120 € TTC (Obat). Obligation annuelle, décret 2023-641 cité par Groupama (non vérifié sur Légifrance).
- Ce que ça dit pour nous : ticket 40-130 €/an, B2C local, exactement le type « agence locale » jugé non viable en v2 ; à ne pas retenir.

### U-FRA-14 : Légionelle et assainissement non collectif : prix introuvables
- Type : contre-preuve (donnée manquante)
- Source : 2 recherches web (extraits uniquement, aucune page ouverte) ; analyses sur devis, SPANC = redevances publiques locales.
- Chiffres : aucun prix privé payé prouvé. Non utilisé.
- Ce que ça dit pour nous : ces deux pistes n'atteignent pas ≥ 3 prix payés ; abandonnées pour manque de preuve, pas par contre-preuve.

## Sources non lues (ajout)
- https://www.3rdanjou.fr/media/guide-des-pro-2-plis-roules-a4-v2026.pdf : PDF compressé [NON OUVERT].
- Extraits seuls, non utilisés : Eurofins (légionelle), banquedesterritoires/CLCV (SPANC), Tulle Agglo.
