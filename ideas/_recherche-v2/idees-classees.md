# Phase 3 : idées « la même chose, en mieux »

Point de départ : les 10 modèles les mieux prouvés de [problemes.md](problemes.md).
Méthode : chaîne du skill `ai-startup-opportunity-generator` (travail réel → douleur → qui paie → solution → concurrents → échecs passés → MVP), sans l'étape 9 (stack Laravel), appliquée à des services plutôt qu'à des logiciels.
Les numéros entre crochets renvoient aux signaux ([1.21] = famille 1, ligne 21).

## Grille de score (sur 10, pondérée)

| Critère | Poids |
|---------|-------|
| A. Argent déjà dépensé sur ce modèle | 25 % |
| F. Faiblesse prouvée des acteurs en place | 15 % |
| D. Douleur prouvée par le web | 15 % |
| M. Avantage d'une équipe marketing (acquisition, contenu, vente) | 15 % |
| V. Vitesse jusqu'au premier client payant (personnes qui doivent dire oui × fréquence de l'occasion) | 15 % |
| T. Testable en moins de 4 semaines, pour moins de 500 €, sans coder | 10 % |
| Taille du marché | 5 % |

## Classement

| Rang | Idée | Modèle amélioré | A | F | D | M | V | T | Taille | **Score** |
|------|------|-----------------|---|---|---|---|---|---|--------|-----------|
| 1 | **I1. Fiche Google gérée, sans engagement, pour artisans du bâtiment** | Visibilité locale TPE | 9 | 7 | 6 | 9 | 8 | 9 | 8 | **8,05** |
| 2 | I2. Même offre pour restaurants et commerces de bouche | Visibilité locale TPE | 8 | 6 | 6 | 9 | 8 | 9 | 7 | **7,60** |
| 3 | I3. « Sortir de PagesJaunes » : audit d'abonnement, résiliation, reprise, payé au succès | Visibilité locale TPE | 8 | 8 | 7 | 7 | 7 | 8 | 6 | **7,45** |
| 4 | **I10. Aide numérique à domicile pour seniors, en abonnement, vendue aux enfants** | Assistance numérique seniors | 7 | 5 | 8 | 8 | 7 | 8 | 8 | **7,15** |
| 5 | **I4. Petits déménagements franciliens à prix fixe, faits par des étudiants** | Déménagement | 7 | 8 | 8 | 6 | 7 | 6 | 7 | **7,05** |
| 6 | **I8. Courtier en énergie transparent pour TPE gourmandes en électricité** | Courtage énergie TPE | 7 | 7 | 7 | 7 | 6 | 7 | 8 | **6,90** |
| 7 | I5. Porteurs à l'heure (main-d'œuvre seule, le client loue son camion) | Déménagement | 7 | 6 | 6 | 6 | 8 | 9 | 5 | **6,80** |
| 8 | **I14. Débarras de marque en Île-de-France, prix affiché en ligne** | Débarras | 8 | 4 | 6 | 8 | 7 | 6 | 7 | **6,70** |
| 9 | I19. Transition résidentielle des seniors (tri, débarras, déménagement, installation) | Débarras + déménagement + seniors | 7 | 6 | 7 | 7 | 5 | 6 | 5 | **6,35** |
| 10 | I9. Audit de factures d'énergie des TPE, payé au pourcentage des économies | Courtage énergie TPE | 6 | 6 | 7 | 6 | 6 | 7 | 7 | **6,30** |
| 11 | I7. Astreinte dépannage pour petits bailleurs (artisans vérifiés, prix plafonnés) | Dépannage urgent | 6 | 8 | 8 | 5 | 5 | 5 | 6 | **6,20** |
| 12 | I15. Débarras de successions vendu via notaires et agents immobiliers | Débarras | 7 | 4 | 6 | 7 | 6 | 6 | 6 | **6,10** |
| 13 | I17. Conciergerie à prix fixe par séjour (au lieu de 20 % de commission) | Conciergerie courte durée | 7 | 5 | 5 | 7 | 6 | 6 | 4 | **6,00** |
| 14 | I13. Montage de cuisines et meubles en kit, avec SAV garanti | Cuisine équipée | 6 | 7 | 6 | 3 | 7 | 6 | 6 | **5,85** |
| 15 | I11. Ateliers numériques vendus aux résidences seniors et aux mairies | Assistance numérique seniors | 5 | 4 | 7 | 6 | 5 | 7 | 5 | **5,50** |

En gras : les idées qui représentent chacune un modèle différent dans le haut du classement.

**Lecture franche** : les trois premières idées sont trois variantes du même modèle (visibilité locale des TPE). C'est cohérent avec les preuves, mais cela concentre le risque sur un seul marché. Le tournoi (phase 4) audite donc les modèles, pas les variantes.

## Fiches des idées retenues

### I1. Fiche Google gérée, sans engagement, pour artisans du bâtiment (Île-de-France)
- **Travail réel** : l'artisan doit être trouvé sur Google Maps, récolter des avis après chaque chantier, y répondre, publier des photos. Il le fait mal ou pas du tout.
- **Douleur** : abonnements subis (12-24 mois, reconduction tacite) [1.25][1.26], résultats invisibles [1.24], 81 % des clients lisent les avis avant de choisir [5.5].
- **Qui paie** : l'artisan (plombier, électricien, couvreur, peintre…), qui paie déjà 33 à 78 € HT/mois à Solocal ou 60 à 240 € HT/mois pour un site [1.25][5.21].
- **Où on bat l'acteur en place** : **contrat** (sans engagement, résiliable en un clic, la fiche reste à l'artisan) et **preuve** (rapport mensuel d'appels et d'itinéraires venus de Google, chiffres que Google fournit gratuitement).
- **Offre** : optimisation de la fiche, collecte d'avis par SMS ou QR code après chantier, réponses aux avis sous 48 h, 4 publications photo par mois, rapport mensuel. Option « avis seuls » à 39 € HT/mois.
- **Prix** : 79 € HT/mois sans engagement, frais de mise en route 149 € HT [HYPOTHÈSE de prix, à tester].
- **Canal** : repérer sur Google Maps les artisans franciliens à fiche faible (moins de 20 avis ou note < 4,2) ; appel puis visite ; audit gratuit de la fiche en 5 minutes ; partenariats avec chambres de métiers et fédérations (la CAPEB le fait déjà pour ses adhérents [5.25]).
- **Concurrents** : Solocal, Simplébo, agences locales, freelances ComeUp et Malt, outils (GMB Briefcase…).
- **Échecs passés** : aucun échec documenté trouvé sur ce créneau précis ; le recul de Solocal est le contre-exemple (modèle à engagement long).
- **MVP** : tableur + outils gratuits (Google Business Profile, générateur de QR code, SMS manuels), 5 artisans pilotes à prix réduit, en 2 semaines.
- **Juridique** : aucune autorisation. Si la vente se fait chez l'artisan (hors établissement) et qu'il a 5 salariés ou moins, il dispose de 14 jours de rétractation [6.30] : à prévoir dans le contrat.

### I2. Même offre pour restaurants et commerces de bouche
- Même mécanique ; les avis et les photos pèsent encore plus pour un restaurant. Prix 89 € HT/mois.
- **Différence avec I1** : concurrence plus forte (outils spécialisés restauration) [HYPOTHÈSE, à auditer] ; décision rapide (un gérant).

### I3. « Sortir de PagesJaunes »
- **Offre** : on lit le contrat Solocal de l'artisan, on calcule la date et le préavis de résiliation [1.26], on envoie la résiliation, on reprend sa fiche et ses avis. Payé 50 % de l'économie de la première année, puis bascule vers I1.
- **Où on bat l'acteur** : on transforme la principale plainte (le contrat) en offre.
- **Risque** : dépend des dates de reconduction ; revenu ponctuel. C'est surtout un **canal d'acquisition pour I1**.

### I10. Aide numérique à domicile pour seniors, en abonnement, vendue aux enfants
- **Travail réel** : faire les démarches en ligne, utiliser le téléphone et la tablette, éviter les arnaques.
- **Douleur** : 53 % des plus de 75 ans sans internet à domicile [2.13], 39 % des usagers ont renoncé à une démarche [2.14], faux support technique en hausse de 119 % [2.36].
- **Qui paie** : l'enfant (40-60 ans) le plus souvent ; le prix est divisé par deux par le crédit d'impôt [2.10].
- **Où on bat l'acteur en place** : **relation** (même intervenant chaque mois, pas un dépannage ponctuel), **confiance** (marque, intervenants formés, compte rendu envoyé à l'enfant après chaque visite), **anti-arnaque** (numéro à appeler « avant de cliquer »).
- **Prix** : 2 h par mois pour 69 € (34,50 € après crédit d'impôt) [HYPOTHÈSE] ; les franchises facturent 79 à 89 €/h à l'acte [2.29].
- **Canal** : publicité ciblée vers les 40-60 ans (Facebook, Instagram), contenus « comment protéger ses parents des arnaques », pharmacies, CCAS, clubs seniors.
- **Concurrents** : Docteur Ordinateur, PC At Home, indépendants, médiation numérique gratuite, La Poste [HYPOTHÈSE, à auditer].
- **Échecs passés** : Ordissimo recule sur le matériel, progresse sur le service [2.33].
- **MVP** : 10 familles du réseau de l'équipe, visites faites par nous, compte rendu par message, encaissement avant la déclaration SAP (crédit d'impôt ensuite).
- **Juridique** : activité libre ; déclaration NOVA nécessaire pour le crédit d'impôt [6.24][6.25].

### I4. Petits déménagements franciliens à prix fixe, faits par des étudiants
- **Où on bat l'acteur en place** : **ponctualité garantie** (remise si retard), **prix fixe en ligne** par type de logement (studio, T2), photos et inventaire avant départ, assurance casse claire. Les reproches au secteur sont précisément le retard, la casse et l'acompte [1.1-1.4].
- **Prix** : studio 290 €, T2 490 € intra-Paris [HYPOTHÈSE].
- **Canal** : résidences étudiantes, écoles, groupes de colocation, Google Ads « petit déménagement Paris ».
- **Limite** : saisonnalité (pic en été, fin de mois) et mobilité en baisse [2.28] ; capacité de transport léger obligatoire si on transporte, formation disponible chaque mois en IDF [6.20][6.26].

### I5. Porteurs à l'heure (main-d'œuvre seule)
- Modèle HireAHelper (racheté par Porch) [3.12][3.13] : le client loue son utilitaire, nous fournissons 2 porteurs. Pas de transport, donc pas de licence.
- **Prix** : 35 €/h par porteur, minimum 2 h [HYPOTHÈSE]. **Canal** : agences de location d'utilitaires, groupes de quartier.
- **Limite** : faible panier, concurrence d'étudiants isolés sur Aladom [2.26].

### I8. Courtier en énergie transparent pour TPE gourmandes en électricité
- **Cible** : boulangeries, restaurants, commerces de bouche au-delà de 36 kVA, donc exclus du tarif réglementé [6.6].
- **Où on bat l'acteur en place** : **commission affichée** sur le devis (ce que la proposition de loi veut imposer [1.28][6.23]), comparaison écrite, rappel automatique avant chaque échéance.
- **Prix** : commission fournisseur affichée, ou honoraires fixes de 290 € par dossier [HYPOTHÈSE].
- **Avantage d'équipe** : connaissance du marché de l'électricité des TPE (alternance EDF).
- **Risque majeur** : **conflit d'intérêts** pour le membre de l'équipe salarié en alternance chez EDF (obligation de loyauté envers l'employeur) ; il ne pourrait pas participer tant que son contrat court [HYPOTHÈSE juridique à vérifier avec un juriste].

### I14. Débarras de marque en Île-de-France, prix affiché en ligne
- **Où on bat l'acteur en place** : **prix connu avant la visite** (photos → devis en 1 h), **rapidité** (intervention sous 72 h), **traçabilité** (photos avant/après, reçus des dons aux ressourceries), **marque** reconnaissable. Les acteurs en place sont locaux et sans marque [2.9][2.23], avec des prix opaques [2.7].
- **Prix** : à partir de 290 € le petit volume ; 800 à 2 500 € un logement complet [HYPOTHÈSE calée sur [2.8]].
- **Canal** : notaires, agences immobilières, résidences seniors, Google Ads « débarras Paris ».
- **Modèle étranger** : College Hunks (fondé par deux étudiants, 280 M$ de ventes) [3.1].
- **Limites** : faiblesse des acteurs non prouvée [1.30] ; coûts de déchetterie professionnelle ; capacité de transport léger et déclaration de transport de déchets au-delà de 0,5 t par chargement [6.28] ; collecte municipale gratuite jusqu'à 3 m³ [2.22] ; travail physique.

### I19. Transition résidentielle des seniors
- Combinaison I14 + I4 + I10 pour le passage en résidence ou chez un enfant : tri, débarras, déménagement, installation de la box et de la tablette.
- **Preuve** : plus de 1 000 entreprises spécialisées aux États-Unis, 1 500 à 5 000 $ par déménagement [3.14][3.15][3.16].
- **Limite** : événement rare, plusieurs décideurs (parent, frères et sœurs), donc vente lente.

### I9, I7, I15, I17, I13, I11 (résumé)
| Idée | Point où on bat l'acteur | Pourquoi plus bas |
|------|--------------------------|-------------------|
| I9. Audit de factures d'énergie au succès | Zéro risque pour le client (payé sur économies) | Économies faibles par TPE ; même conflit d'intérêts qu'I8 |
| I7. Astreinte dépannage pour petits bailleurs | Prix plafonnés, artisans vérifiés | Repose sur des artisans qu'on ne contrôle pas [5.18] |
| I15. Débarras via notaires et agents | Prescripteurs qui voient passer les successions | Vente lente (prescripteurs à convaincre) ; même limites qu'I14 |
| I17. Conciergerie à prix fixe par séjour | Prix fixe au lieu de 20 % | Plafond de 90 jours à Paris et copropriétés pouvant interdire [6.31][6.32] |
| I13. Montage de cuisines et meubles | SAV garanti | Compétence technique que l'équipe n'a pas |
| I11. Ateliers en résidences seniors | Un client paie pour 20 seniors | Budgets publics et institutionnels lents |

## Idées éliminées (définitivement)

| Idée | Filtre éliminatoire | Explication |
|------|---------------------|-------------|
| I6. Annuaire francilien d'artisans de dépannage vérifiés, payé par les artisans | Premier euro impossible en moins de 3 mois | Il faut du trafic avant que les artisans paient, face à des fraudeurs qui achètent de la publicité [2.3] |
| I12. Accompagnement des syndics bénévoles | Décision collective (assemblée générale) | Le budget se vote en assemblée ; de plus, proche d'une idée de la première itération |
| I16. Dépôt-vente Vinted pour particuliers pressés | Leader bien financé sans angle crédible | Vinted est gratuit en libre-service ; Sellpy (H&M) fait le service clés en main et perd de l'argent [5.20] |
| Syndic professionnel, expertise comptable, auto-école | Agrément ou diplôme obligatoire | Carte professionnelle, ordre des experts-comptables, agrément préfectoral |
| Soutien scolaire « mieux fait » | Leader bien financé sans angle crédible | Aucune faiblesse prouvée des acteurs ; 80 % du marché au noir [5.10] |

## Idées qui passent au tournoi (phase 4)

Les 8 premières idées couvrent 5 modèles. Un audit par modèle :
- A. Visibilité locale des TPE (I1, I2, I3)
- B. Aide numérique à domicile pour seniors (I10)
- C. Petits déménagements (I4, I5)
- D. Courtage en énergie pour TPE (I8)
- E. Débarras de marque (I14)
