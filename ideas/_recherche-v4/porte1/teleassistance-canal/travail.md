# Téléassistance par les canaux prescripteurs : travail
Mission : distribution via départements/CCAS (marchés publics), caisses de retraite, mutuelles/assureurs. Date : 2026-11-03.
Recherches web utilisées : 6 sur 15 (plus 6 ouvertures de pages, 4 échecs de lecture). Appels outil/API : DECP, BODACC, recherche-entreprises.
Preuves : 10. Domaines distincts : data.economie.gouv.fr, bodacc (opendatasoft), recherche-entreprises.api.gouv.fr, matmut.fr, groupama.fr, lassuranceretraite.fr, agirc-arrco.fr, 62.admr.org.

### TC-01 : Volume des marchés publics
- Acteur / marché : collectivités acheteuses de téléassistance
- Type : argent dépensé
- Source : https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/decp-2022-marches-valides/records?where=search%28objet%2C%22t%C3%A9l%C3%A9assistance%22%29&select=count%28%2A%29+as+marches%2C+sum%28montant%29+as+montant&group_by=year%28datenotification%29&limit=30 (date : 2026-11-03 ; N1 ; DECP)
- Citation : « "marches": 25, "montant": 13324847.84 »
- Chiffres : 2024 25 marchés 13,3 M€ ; 2025 30 marchés 9,6 M€ ; 2026 31 marchés 7,9 M€ (valeurs maximales d'accords-cadres, DECP dès 40 000 € HT ; quelques faux positifs : maintenance de logiciels de bibliothèque)
- Ce que ça dit pour nous : canal public réel mais petit (< 15 M€/an notifiés) face aux 112-250 M€ de marché.

### TC-02 : Acheteurs et titulaires, marchés notifiés depuis 2024 (requête API)
- Acteur / marché : départements, CCAS, communes, bailleurs
- Type : argent dépensé
- Source : https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/decp-2022-marches-valides/records?where=search%28objet%2C%22t%C3%A9l%C3%A9assistance%22%29+and+datenotification%3E%3D%222024-01-01%22&select=acheteur_id%2Ctitulaire_id_1%2Cmontant%2Cdatenotification%2Coffresrecues%2Cprocedure%2Cdureemois%2Cobjet&order_by=montant+desc&limit=60 (date : 2026-11-03 ; N1 ; DECP)
- Citation : « Appel d'offres ouvert »
- Chiffres : (86 marchés depuis 2024 selon total_count) Essonne 10 M€/48 mois, Vitaris, 2 offres, procédure adaptée (2024-01) ; Oise 4,4 M€/48 mois, Vitaris, 2 offres, AO ouvert (2025-06) ; Alpes-Maritimes 2 M€, Vitaris (2026-09) ; Val-d'Oise 0,87 M€/12 mois, Vitaris, 2 offres (2026-07) ; Somme 0,55 M€, Vitaris, 3 offres (2024-04). Vitaris titulaire d'environ 25 des 60 plus gros marchés ; Redion environ 10 (Colombes, Rouen, Malakoff, Antony, Ludres, Asnières) ; autres : Technipro Allovie, Co-Assist, Bluelinea, Présence Verte, G.T.S, CDTS, Solem.
- Ce que ça dit pour nous : 1 à 6 offres par marché (souvent 2-3) : concurrence faible mais Vitaris domine ; il faut gagner des contrats de 3-4 ans avec références.

### TC-03 : Mode de choix du prestataire
- Acteur / marché : CCAS, communes, départements
- Type : obligation (procédure)
- Source : https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/decp-2022-marches-valides/records?where=search%28objet%2C%22t%C3%A9l%C3%A9assistance%22%29+and+datenotification%3E%3D%222024-01-01%22&select=acheteur_id%2Ctitulaire_id_1%2Cmontant%2Cdatenotification%2Coffresrecues%2Cprocedure%2Cdureemois%2Cobjet&order_by=montant+desc&limit=60 (même requête que TC-02 ; date : 2026-11-03 ; N1 ; DECP)
- Citation : « "offresrecues": "2" »
- Chiffres : sur les 60 plus gros marchés : majorité en procédure adaptée (3-6 offres), quelques AO ouverts, environ 8 marchés sans publicité ni mise en concurrence (renouvellements, My Keeper). Durées 36 ou 48 mois dominantes. Montants CCAS : 100-440 k€ sur 3-4 ans.
- Ce que ça dit pour nous : accès par appel d'offres, faisable pour une petite structure avec références ; cycle de 3-4 ans.

### TC-04 : CA des titulaires (comptes déposés)
- Acteur / marché : Vitaris, Redion, Bluelinea
- Type : argent dépensé
- Source : https://recherche-entreprises.api.gouv.fr/search?q=343431615 (date : 2026-11-03 ; N1 ; API entreprises, comptes déposés)
- Citation : « VITARIS »
- Chiffres : Vitaris CA 2025 26,62 M€, résultat net 0,03 M€ ; Redion Service Téléassistance (453798647) CA 2025 7,55 M€, résultat 0,09 M€ ; Redion Téléassistance (451833735) CA 2025 9,26 M€, résultat 0,39 M€ ; Bluelinea Services CA 2019 6,31 M€, perte 2,79 M€ ; Co-Assist et My Keeper CA 0 (confidentiel) ; Technipro Allovie : pas de comptes.
- Ce que ça dit pour nous : le leader public gagne environ 0 % de marge nette : ce canal paie mal.

### TC-05 : Assurance retraite (Carsat) finance l'installation
- Acteur / marché : CNAV/Carsat, retraités
- Type : argent dépensé (subvention)
- Source : https://www.lassuranceretraite.fr/portail-info/home/retraite/aide-retraite/aide-quotidien.html (date inconnue ; N2 ; Assurance retraite)
- Citation : « prises en charge à 100 % par l'Assurance retraite, dans la limite des fonds disponibles »
- Chiffres : plafond annuel par bénéficiaire (montant non affiché sur la page ouverte ; un extrait de recherche évoque 500 €/an : [NON OUVERT])
- Ce que ça dit pour nous : la caisse paie ; comment le prestataire est choisi : non établi.

### TC-06 : Matmut, offre Sérélia
- Acteur / marché : Matmut distribue Sérélia (Séréna, Groupe IMA)
- Type : argent dépensé (prix public)
- Source : https://www.matmut.fr/mutuelle/teleassistance-serelia (date inconnue ; N2 ; Matmut)
- Citation : « Sérélia Sérénité est proposée sans engagement au tarif de 34,90 € par mois. »
- Chiffres : 34,90 €/mois, 17,45 € après crédit d'impôt 50 % ; pas de part prise en charge par la mutuelle : elle revend, elle ne subventionne pas.
- Ce que ça dit pour nous : l'assureur distribue un service d'une filiale d'assistance (IMA) déjà intégrée.

### TC-07 : Groupama, tarif
- Acteur / marché : Groupama Loire Bretagne
- Type : argent dépensé (prix public)
- Source : https://www.groupama.fr/tap/ (date : 2026-10 ; N2 ; Groupama)
- Citation : « Tarif de 32,70 € par mois »
- Chiffres : 32,70 €/mois, 16,35 € après crédit d'impôt ; promo 2 mois offerts jusqu'au 30/11/2026
- Ce que ça dit pour nous : même zone de prix que les indépendants (26-43 €) ; promotions = concurrence sur l'acquisition.

### TC-08 : Défaillances (BODACC)
- Acteur / marché : entreprises citant « téléassistance »
- Type : contre-preuve
- Source : https://bodacc-datadila.opendatasoft.com/api/explore/v2.1/catalog/datasets/annonces-commerciales/records?where=familleavis%3D%22collective%22+and+search%28%22t%C3%A9l%C3%A9assistance%22%29+and+dateparution%3E%3D%222025-01-01%22&select=commercant%2Cregistre%2Ctypeavis_lib%2Cjugement%2Cdateparution&limit=40 (date : 2026-11-03 ; N1 ; DILA)
- Citation : « AMA TELEASSISTANCE »
- Chiffres : les 24 annonces de 2025 concernent surtout des sociétés d'aide à domicile ou de sécurité (Dom'Care, Central Sud, Auprès de Vous, Vie Active, Iris Assistance) où le mot figure dans l'activité ; seul nom explicite : AMA Téléassistance, liquidation judiciaire du 2026-02-23.
- Ce que ça dit pour nous : le chiffre de 24 ne mesure pas des échecs de téléassistance ; aucun échec de centrale établi.

### TC-09 : Agirc-Arrco, pas d'offre téléassistance sur la page primaire
- Acteur / marché : Agirc-Arrco
- Type : contre-preuve
- Source : https://www.agirc-arrco.fr/thematique_page/action-sociale/ (date : 2026 ; N2 ; Agirc-Arrco)
- Citation : « Votre caisse de retraite vous aide à évaluer la situation »
- Chiffres : la page ouverte ne mentionne pas la téléassistance ; une offre « retraités isolés avec téléassistance » vient d'un site secondaire [NON OUVERT] ; partenaire exclusif Domiserve/ADMR depuis 2023 : extrait [NON OUVERT].
- Ce que ça dit pour nous : Agirc-Arrco non établi comme payeur de téléassistance ; si exclusif ADMR/Domiserve, fermé aux entrants.

### TC-10 : Filien/ADMR cite les financeurs
- Acteur / marché : Filien (ADMR)
- Type : tendance (extrait non ouvert)
- Source : https://www.62.admr.org/system/files/webmaster/pdf/teleassistance/guide_filien_teleassistance.pdf (date inconnue ; N4 ; extrait de recherche [NON OUVERT])
- Citation : « conseil départemental »
- Chiffres : aucun utilisable
- Ce que ça dit pour nous : piste seulement ; aucune mutuelle partenaire de Filien trouvée.

## Sources non lues
- ADMR communiqué Agirc-Arrco/Domiserve 2023 et Filien CP 2025-11 (PDF compressés illisibles) ; services75ans.agirc-arrco.fr et pour-les-personnes-agees.gouv.fr (erreur de certificat) ; bdor.fr (410) ; entreprises.gouv.fr guide téléassistance (404).
