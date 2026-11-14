# N8211 (82.11Z) : travail
Mission : comprendre la croissance du code, trouver 1-3 modèles qui encaissent. Date : 2026-11-03. Recherches web : 1 WebSearch (+ 4 WebFetch). Preuves : 10.

### N82-01 : taille et croissance du code
- Acteur / marché : secteur 82.11 France
- Type : tendance
- Source : https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/sbs_ovw_act?format=JSON&lang=FR&geo=FR&nace_r2=N8211&indic_sbs=NETTUR_MEUR (date : 2026-11-03 ; N1 ; Eurostat)
- Citation : « 2022 : 2 421 M€ ; 26 383 entreprises »
- Chiffres : 2021 3 816 M€ ; 2022 2 421 ; 2023 3 582 ; 2024 5 282 M€ / 38 479 entreprises. Série non monotone (chute de 37 % en 2022 puis rebond) : signe de reclassement. INSEE (ICA_SERV) : +9,7 %/an sur 3 ans, valeur.
- Ce que ça dit pour nous : la croissance Eurostat (+47,7 %/an à l'écran, +11,4 %/an sur 2021-2024) n'est pas une tendance propre.

### N82-02 : concentration, artefact de holdings
- Acteur / marché : 82.11Z
- Type : contre-preuve
- Source : https://recherche-entreprises.api.gouv.fr/search?activite_principale=82.11Z&etat_administratif=A&ca_min=100000000&per_page=25 (date : 2026-11-03 ; N1 ; API Sirene/comptes déposés)
- Citation : « Part des 3 premières entités dans le CA du secteur N8211 (2024) : 87.0 % »
- Chiffres : RCM 2 244 M€ (2024) ; GCC SERVICES 1 175 M€ et DELTA 1 175 M€ (SIREN 922421136 / 922420963, 2025) ; MUREX GROUP 830 M€ ; ALMAVIVA HOLDING 776 M€. Les SIREN 9224... sont récents : sociétés de groupe. Somme des 10 premiers (~8,4 Md€) > CA Eurostat du secteur (5,3 Md€) : périmètres incompatibles.
- Ce que ça dit pour nous : les gros CA du code sont des holdings/groupes multi-activités, pas un marché de services de bureau.

### N82-03 : population réelle
- Acteur / marché : 82.11Z
- Type : tendance
- Source : https://recherche-entreprises.api.gouv.fr/search?activite_principale=82.11Z&etat_administratif=A&per_page=1 (date : 2026-11-03 ; N1 ; Sirene)
- Citation : « Entreprises actives 82.11Z : 61 855 »
- Chiffres : 56 008 non employeurs ou inconnus ; 5 599 employeurs ; 594 de 10 salariés ou plus ; 445 entreprises avec CA 1,5-60 M€.
- Ce que ça dit pour nous : 91 % de micro-entités sans salarié ; la hausse du nombre d'entreprises est surtout de la micro-création.

### N82-04 : acteurs de taille moyenne, domiciliation absente
- Acteur / marché : entreprises 82.11Z CA 1,5-60 M€
- Type : argent dépensé
- Source : https://recherche-entreprises.api.gouv.fr/search?activite_principale=82.11Z&etat_administratif=A&ca_min=1500000&ca_max=60000000&per_page=25 (date : 2026-11-03 ; N1 ; comptes déposés)
- Citation : « 445 »
- Chiffres (sortie API) : INSITU BUSINESS CENTRE 25,2 M€ (2024, résultat 2,1 M€) ; MON EXPERT ADMINISTRATIF 1,65 M€ (2024, résultat -0,71 M€) ; réseau ERGOS (une dizaine d'entités 1,9-3,5 M€, résultats positifs) ; ACTUAL (agences) 1,5-4,2 M€ ; S2EF 8,6 M€.
- Ce que ça dit pour nous : le code mélange centres d'affaires, agences en réseau et assistance admin ; Kandbaz (74.90B, CA 1 150 €), SeDomicilier SAS (70.22Z, CA 0) ne sont pas en 82.11Z : critère « 3 acteurs du modèle avec CA déposé » non rempli pour la domiciliation en ligne.

### N82-05 : prix Kandbaz
- Acteur / marché : Kandbaz, domiciliation
- Type : argent dépensé (prix affiché, pas une dépense)
- Source : https://www.kandbaz.com/tarifs (date : 2026-11-03 ; N2 ; vendeur)
- Citation : « 19€ 1€ / mois »
- Chiffres : 19 €/mois habituel, 1 € en promo ; packs création 499 € HT, transfert 649 € HT.
- Ce que ça dit pour nous : prix d'appel très bas.

### N82-06 : prix SeDomicilier
- Acteur / marché : SeDomicilier
- Type : argent dépensé (prix affiché)
- Source : https://www.sedomicilier.fr/ (date : 2026-11-03 ; N2 ; vendeur)
- Citation : « à partir de 11€/mois »
- Chiffres : remise jusqu'à 45 % sur 2-3 ans.
- Ce que ça dit pour nous : plancher à 11 €/mois.

### N82-07 : prix LegalPlace
- Acteur / marché : LegalPlace
- Type : argent dépensé (prix affiché)
- Source : https://www.legalplace.fr/domiciliation-entreprise/ (date : 2026-11-03 ; N2 ; vendeur)
- Citation : « à partir de 17 €/mois »
- Chiffres : fourchette citée 15 à 60 €/mois.
- Ce que ça dit pour nous : 3 prix publics (11, 17, 19 €) mais revenu annuel par client ~130-230 € : économie unitaire très faible.

### N82-08 : faiblesses (avis)
- Acteur / marché : Kandbaz
- Type : plainte
- Source : https://www.trustpilot.com/review/kandbaz.com?stars=1&stars=2 (date : 2026-11-03 ; N4 ; Trustpilot)
- Citation : « Every letter that arrives means an additional charge »
- Chiffres : note 4,7/5, 1 009 avis, environ 5-6 % de 1-2 étoiles ; plaintes : frais de courrier, pièces refusées, résiliation bloquée.
- Ce que ça dit pour nous : contre-preuve : le leader est bien noté ; faiblesse limitée, canal unique.

### N82-09 : marchés publics
- Acteur / marché : accueil / secrétariat externalisé
- Type : argent dépensé
- Source : https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/decp-2022-marches-valides/records?where=search%28objet%2C%22accueil+standard+t%C3%A9l%C3%A9phonique%22%29&select=count%28%2A%29+as+marches%2C+sum%28montant%29+as+montant&group_by=year%28datenotification%29&limit=30 (date : 2026-11-03 ; N1 ; DECP)
- Citation : « 2025 : 3 marchés  0.3 M€ »
- Chiffres : « secrétariat externalisé » : 1 marché, 0,8 M€ en 2025.
- Ce que ça dit pour nous : demande publique négligeable.

### N82-10 : échecs
- Acteur / marché : domiciliation / secrétariat
- Type : contre-preuve
- Source : https://bodacc-datadila.opendatasoft.com/api/explore/v2.1/catalog/datasets/annonces-commerciales/records (outil `echecs`, date : 2026-11-03 ; N1 ; BODACC)
- Citation : « Annonces de procédures collectives mentionnant « domiciliation » (BODACC) »
- Chiffres : ~1 300-1 500 annonces/an 2008-2019 pour « domiciliation » (bruit : adresses domiciliées) ; « secrétariat » 336 (2008) à 141 (2021).
- Ce que ça dit pour nous : échecs du modèle non établis, mot-clé trop bruité.

## Sources non lues
- Légifrance L123-11-1 (agrément préfectoral de domiciliation) : [NON OUVERT].
- Prix des assistants virtuels : non cherchés.
