# Marchés en croissance : cartographie v3 (phase 0)

Date : 2026-10-13. Option A (de zéro). 38 marchés évalués par 4 chercheurs, 149 preuves, 7 lentilles,
plus de 15 secteurs, B2B et B2C, services, produits et logiciels.
Fiches complètes et preuves (ID `X0-pN`) dans `marches/` :
[obligation-transition.md](marches/obligation-transition.md) (A1-A10),
[fragmentation-reseaux.md](marches/fragmentation-reseaux.md) (B1-B9),
[ailleurs-demande.md](marches/ailleurs-demande.md) (C1-C9),
[malservi-b2c.md](marches/malservi-b2c.md) (D1-D10).
Contrôle des chiffres : [verification.md](verification.md).

## Constat général

Aucun des 38 marchés ne prouve une croissance ≥ 8 %/an avec 2 sources dont 1 institutionnelle.
Les marchés français mûrs (obsèques, auto, formation, mariage, animaux) croissent de 0 à 6 %/an.
Les survivants passent le seuil de croissance par la seconde branche de `CLAUDE.md` : **un moteur
structurel daté** (échéance réglementaire 2026-2028) ou un volume qui double (batteries, sans alcool).
Aucune taille n'est publiée par une source fiable pour les survivants : ce sont des calculs bottom-up,
donc confiance « moyenne » au mieux. Cinq des huit marchés gardés touchent à l'énergie ou au bâtiment,
ce qui recoupe le secteur connu de l'équipe (EDF, offres électricité TPE/PME).

## Filtre (seuils éliminatoires de CLAUDE.md)

Croissance = ≥ 8 %/an OU moteur structurel daté. Taille = SAM France ≥ 50 M€. Concentration = 3 premiers
< 40 % sauf angle crédible. Clients ≥ 3 000 (B2B) ou ≥ 100 000 (B2C).

## Score marché (skill market-segment-scanner, étape 3)

Taille 30 %, croissance 30 %, fragmentation 20 %, récurrence de la dépense 10 %, accès aux clients 10 %.
Notes de 0 à 10 attribuées par le coordinateur à partir des synthèses ; elles sont à recalculer après vérification.

| Rang | ID | Marché (qui paie, pour quoi) | Taille France | Croissance / moteur | Conc. | Modèle d'exécution | T | Cr | F | R | A | Score |
|------|----|------------------------------|---------------|---------------------|-------|-------------------|---|----|---|---|---|-------|
| 1 | A6 | Bailleurs privés : mise aux normes des logements classés F avant 2028 | travaux aidés Anah 4,4 Md€ (tous dispositifs) ; 720 000 logements F loués | interdiction de louer un F au 01/01/2028 (puis E en 2034) | très fragmenté | accompagnement outillé ou chantier sous-traité | 8 | 8 | 9 | 3 | 6 | **7,5** |
| 2 | A2 | Propriétaires et occupants de tertiaire > 1 000 m² : OPERAT, GTB/BACS | 170 à 680 M€ [HYPOTHÈSE] | GTB > 70 kW au 01/01/2027 ; déclaration OPERAT chaque 30/09 ; -40 % en 2030 | inconnu | service outillé | 6 | 7 | 6 | 8 | 7 | **6,6** |
| 3 | A1 | TPE/PME : passage à la facturation électronique obligatoire | non publiée ; 10 M d'assujettis TVA | réception 01/09/2026 ; émission PME et micro 01/09/2027 | 108 plateformes agréées | logiciel ou service outillé | 5 | 8 | 5 | 7 | 9 | **6,5** |
| 4 | A5 | Exploitants de parkings > 1 500 m² : ombrières solaires (loi APER) | non calculée ; 21 000 magasins et centres | 07/2026 (> 10 000 m², déjà passée), 07/2028 (1 500 à 10 000 m²) | inconnu | chantier lourd ; angle AMO ou tiers-investisseur | 7 | 8 | 5 | 2 | 6 | **6,3** |
| 5 | C3 | Foyers équipés de panneaux : batterie domestique posée | ≈ 36 à 150 M€ (10 209 × 3 500 à 15 000 €, prix corrigé après vérification) | volume ×2 en 2025 (10 209 installations) ; rachat du surplus à 4 c€/kWh | inconnu | pose technique ; génération de demande | 4 | 9 | 7 | 2 | 6 | **6,1** |
| 6 | D3 | Consommateurs et CHR : bière et boissons sans alcool | 238 M€ (bière) à 330 M€ (avec vin et spiritueux) | +11,5 % en volume 2025 (fédération) | ✘ une marque = 58 % | produit, brassage sous-traité | 6 | 8 | 2 | 7 | 6 | **5,9** |
| 7 | A10 | Copropriétés et syndics : DPE collectif et plan pluriannuel de travaux | 58 à 231 M€/an (plafond théorique) | DPE collectif ≤ 50 lots au 01/01/2026 ; PPPT < 51 lots au 01/01/2025 | probable < 40 % | diagnostic certifié (que l'équipe n'a pas) ou apporteur | 5 | 6 | 7 | 4 | 7 | **5,8** |
| 8 | A9+D6 | Seniors de 70 ans et plus : adaptation du logement (douche, accès) | 230 à 330 M€/an de travaux subventionnés | MaPrimeAdapt' reconduite en 2026 ; +5 à +8 %/an de dossiers (objectif) | fragmenté [HYPOTHÈSE] | pose sous-traitée, accompagnement | 6 | 5 | 8 | 2 | 6 | **5,7** |

## Fiches des 8 marchés gardés

### A6 : Bailleurs privés, mise aux normes des logements F avant 2028
- Taille : 720 000 logements F en location privée (ONRE, A6-p1) ; aides Anah 4,39 Md€ tous dispositifs (secondaire, A6-p3). Pas de taille publiée pour l'accompagnement des bailleurs.
- Croissance : moteur daté, interdiction de louer un logement F au 01/01/2028 (A6-p1), puis E en 2034.
- Acteurs : très fragmenté (artisans RGE, bureaux d'études, Mon Accompagnateur Rénov').
- Modèle : accompagnement outillé (audit, devis, aides, suivi) ou chantier sous-traité.
- **Contre-preuve** : projet de loi d'assouplissement évoqué (non confirmé) ; guichet MaPrimeRénov' fermé du 31/12/2025 au 23/02/2026 ; « Mon Accompagnateur Rénov' » demande un agrément.
- Seuils : taille ✔ | croissance ✔ (moteur) | concentration ✔ | clients ✔. Confiance : moyenne (moteur), faible (taille).

### A2 : Tertiaire > 1 000 m², décret tertiaire et GTB (BACS)
- Taille : 170 à 680 M€ [HYPOTHÈSE illustrative] ; environ 340 000 entités fonctionnelles assujetties (A2-p2, chiffres ≈ non retrouvés à la vérification : à resourcer en phase 1).
- Croissance : moteur daté, GTB obligatoire au 01/01/2027 pour les systèmes > 70 kW, déclaration annuelle OPERAT, -40 % de consommation en 2030 (A2-p2).
- Modèle : service outillé récurrent (déclaration annuelle, suivi des consommations).
- **Contre-preuve** : exemption si le retour sur investissement dépasse 10 ans ; aucun prix public relevé.
- Seuils : taille ? | croissance ✔ | concentration ? | clients ✔. Confiance : moyenne (moteur), faible (taille). Avantage équipe : secteur énergie B2B.

### A1 : TPE/PME, facturation électronique obligatoire
- Taille : non publiée ; environ 10 M d'assujettis à la TVA (A1-p3) ; plateformes agréées souvent gratuites pour les petits volumes (A1-p4).
- Croissance : moteur daté, réception au 01/09/2026, émission pour les PME et micro au 01/09/2027 (A1-p1).
- Acteurs : 108 plateformes agréées (A1-p3), plus les experts-comptables.
- **Contre-preuve** : outils gratuits ; la fenêtre se ferme après septembre 2027 ; les experts-comptables captent l'accompagnement.
- Seuils : taille ? | croissance ✔ | concentration ? | clients ✔. Confiance : moyenne (moteur), faible (taille).

### A5 : Parkings > 1 500 m², ombrières photovoltaïques (loi APER)
- Taille : non calculée ; 21 000 magasins et centres commerciaux (FCD, A5-p2) ; 902 parkings concernés dans la seule Manche (A5-p3).
- Croissance : moteur daté, juillet 2026 pour les parkings > 10 000 m² (échéance déjà passée) et juillet 2028 pour ceux de 1 500 à 10 000 m² (A5-p1, décret 2026-842, source secondaire).
- Modèle : chantier à capital lourd ; l'équipe ne pourrait viser que l'assistance à maîtrise d'ouvrage ou l'apport d'affaires.
- **Contre-preuve** : report possible jusqu'en 2030 ; 10 à 15 % des sites déjà équipés.
- Seuils : taille ✔ probable | croissance ✔ | concentration ? | clients ✔. Confiance : faible à moyenne.

### C3 : Batteries domestiques pour foyers équipés de panneaux
- Taille : ≈ 36 à 150 M€ en 2025 (10 209 installations × 3 500 à 15 000 €). Le prix initial de 4 000 à 9 000 € (C3-p5) est ✘ à la vérification : la page dit 3 500 à 15 000 €. Le parc d'environ 1,3 M de foyers (C3-p6) n'est pas vérifié.
- Croissance : 10 209 installations en 2025, volume doublé, part des installations avec batterie de 2 % à 14 % (C3-p3, C3-p4, donnée Enedis relayée).
- Moteur : rachat du surplus à 4 c€/kWh depuis 2025, qui pousse l'autoconsommation.
- **Contre-preuve** : solaire résidentiel -26 % ; Allemagne -8 % ; taille à la limite du seuil.
- Seuils : taille ✔ limite | croissance ✔ | concentration ✔ | clients ✔. Confiance : moyenne (volumes), faible (euros).

### D3 : Bière et boissons sans alcool
- Taille : environ 238 M€ pour la bière, 330 M€ avec vins et spiritueux (D3-p3, blog : confiance faible).
- Croissance : +11,5 % en volume en 2025 (D3-p1, fédération) ; +5,4 % en valeur en 2024.
- **Contre-preuve** : une marque tient 58 % (D3-p2) ; la bière totale baisse. Passe la concentration seulement avec un angle (CHR, cavistes, région).
- Seuils : taille ✔ | croissance ✔ (volume) | concentration ✘ sauf angle | clients ✔. Confiance : faible à moyenne.

### A10 : Copropriétés, DPE collectif et plan pluriannuel de travaux
- Taille : 58 à 231 M€/an, plafond théorique (578 000 copropriétés × 1 000 à 4 000 € ÷ 10 ans, A10-p2, A10-p3).
- Croissance : DPE collectif obligatoire au 01/01/2026 pour les copropriétés ≤ 50 lots ; PPPT au 01/01/2025 (A10-p1). Vague déjà lancée.
- **Contre-preuve** : le diagnostic demande une certification que l'équipe n'a pas ; décideur = syndic (40 880 entreprises NAF 68.32A).
- Seuils : taille ✔ | croissance ✘ hors moteur | concentration ✔ probable | clients ✔. Confiance : moyenne (moteur), faible (taille).

### A9 + D6 : Seniors, adaptation du logement
- Fusion de A9 (chercheur A) et D6 (chercheur D), même marché.
- Taille : ≈ 330 M€ de travaux subventionnés (37 000 × 8 900 €, extrapolé d'une région, A9-p2, A9-p3) ; ≈ 230 M€ d'aides publiques en 2025 (D6-p1).
- Croissance : 37 000 dossiers en 2024 → objectif 41 000 en 2026, soit 5 à 8 %/an (objectif, non réalisé).
- **Contre-preuve** : guichet bloqué, 83 000 dossiers en attente (D6) ; objectif 2024 manqué ; pas d'échéance datée.
- Seuils : taille ✔ | croissance ✘ limite | concentration ✔ | clients ✔. Confiance : faible à moyenne.

## Marchés éliminés (motif)

| ID | Marché | Motif |
|----|--------|-------|
| B6 | Cédants de TPE : intermédiaire de cession | taille 39 à 111 M€ [HYPOTHÈSE], sous le seuil ; honoraires non prouvés ; 9e au score (5,4) |
| B4 | Organismes de formation (19 Md€) | croissance 6,3 %/an < 8 %, sans moteur daté ; micro-organismes peu solvables |
| D2 | Familles : obsèques (≈ 3 Md€) | croissance ≈ +1 %/an en volume, pas de moteur daté avant 2030 |
| B2 | Cabinets de santé : télésecrétariat | croissance non établie ; Doctolib vend un substitut IA à 99 €/mois |
| C1 | PME : direction financière à temps partagé | croissance non chiffrée, aucun moteur ; taille seulement sous hypothèse de pénétration |
| A3 | PME/ETI : conformité NIS2 | aucun moteur daté : loi reportée le 06/10/2026 |
| A4 | E-commerçants : audit d'accessibilité | déjà en vigueur depuis 06/2025, micro exemptées, aucun prix |
| A7 | Restaurants : collecte des biodéchets | déjà en vigueur depuis 2024, aucun prix, logistique d'employeur |
| A8 | Syndics : bornes de recharge en copropriété | taille 13 à 27 M€/an, sous le seuil |
| B1 | Bailleurs : gestion locative déléguée | croissance non établie ; prix en ligne -30 à -50 % |
| B3 | Candidats au permis : auto-écoles | croissance non établie ; leader en consolidation |
| B5 | Automobilistes : entretien et réparation | volume -8,9 % ; croissance en valeur seulement |
| B7 | Seniors : aide à domicile en réseau | bénéficiaires APA -0,7 % ; métier d'employeur |
| B8 | Abonnés : salles de sport en réseau | croissance ≈ 1 % ; capital lourd |
| B9 | Cliniques vétérinaires | exercice réglementé ; croissance non chiffrée |
| C2 | Assurance santé animale | un acteur ≈ 50 % ; agrément d'assureur |
| C4 | TPE de services techniques : logiciel de gestion | SAM 30 à 47 M€ ; Obat a 21 000 clients ; associé tech requis |
| C5 | PME : santé mentale des salariés | aucun prix, aucun budget, croissance non chiffrée |
| C6 | PME : recouvrement amiable | concentré (> 85 % pour une dizaine) ; délais de paiement en baisse |
| C7 | Familles : soutien scolaire | marché mûr, +2 à +4 %/an |
| C8 | Reconditionné électronique | marché stable ; stock lourd |
| C9 | Campings et terrains : réservation | aucun prix, plateforme à deux faces |
| D1 | Ménages : déménagement | croissance négative (mobilité en baisse) |
| D4 | Compléments alimentaires | volume en baisse |
| D5 | Hôtels indépendants : commissions des OTA | Booking 65 % ; croissance +3 % |
| D7 | Mariage | mariages +1,1 %/an |
| D8 | Alimentation animale premium | 0 % en valeur en 2025 |
| D9 | Cosmétiques de marques indépendantes | taille inconnue, exportations en baisse |
| D10 | Restaurants : commissions de livraison | duopole (Uber 60 %, Deliveroo 32 %) |

## Vérification (vague 0.2, détail dans verification.md)

21 preuves contrôlées : 8 ✔, 8 ≈, 1 ✘, 4 non vérifiables (ADEME, Légifrance, ANIL, impots.gouv inaccessibles).
Le taux de ≈ + ✘ (43 %) dépasse 20 %, mais la plupart des ≈ portent sur des citations paraphrasées dont le chiffre
utilisé est confirmé. Décision : pas de relance ; les preuves fautives sont déclassées et corrigées ici.
- **Confirmés** : échéances de la facturation électronique (A1, service-public) ; 720 000 logements F (A6) ;
  MaPrimeAdapt' 38 000 dossiers et 41 000 visés (D6, A9) ; sans alcool +11,5 % en volume et 238 M€ (D3) ;
  volumes de batteries 10 209 et part 2 % → 14 % (C3).
- **Corrigés** : prix d'une batterie 3 500 à 15 000 € (C3, taille recalculée) ; échéance APER 2028 = parkings
  de 1 500 à 10 000 m² (A5) ; le chiffre de 850 000 logements (A6) n'est pas utilisé.
- **Non vérifiés** (sources officielles inaccessibles) : 340 000 entités OPERAT (A2), échéance DPE collectif
  01/01/2026 (A10), part de marché 58 % (D3-p2), parc de 1,3 M de foyers solaires (C3-p6).
- Les tailles restent des calculs bottom-up : la phase 1 doit trouver des prix réellement payés.
