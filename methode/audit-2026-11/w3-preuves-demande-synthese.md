# W3 : synthèse, preuves de CA étranger et signaux de demande en ligne (2026-11-03)
Statut : partiel. 49 preuves (IDs W3-n dans `methode/audit-2026-11/w3-preuves-demande-travail.md`), 32 domaines, 15/15 recherches. Citations lues par WebFetch : à faire re-contrôler. Trous et sources en 403 : fin du fichier de travail.

## A. CA d'entreprises étrangères : source → vérifié ou déclaratif → accès → piège
| Source (preuves) | Vérifié ou déclaratif | Accès (coût, exemple) | Piège |
|---|---|---|---|
| SEC EDGAR 10-K, 10-Q, S-1 (W3-1,2,3,21) | Audité : compte de résultat sur 3 ans (règle S-X 3-02) ; petites cotées : bilan audité sur 2 ans (8-02) | Gratuit, sans clé : `data.sec.gov/api/xbrl/companyfacts/CIK##########.json`, 10 requêtes/s, agent utilisateur déclaré ; plein texte sur 20+ ans : sec.gov/edgar/search/ | Seulement sociétés cotées ou à offre enregistrée, jamais une startup privée classique |
| SEC Form C, financement participatif (W3-4) | Levée ≤ 124 k$ : chiffres fiscaux certifiés par le dirigeant ; 124 à 618 k$ : comptes examinés ; > 618 k$ : audités | Gratuit sur EDGAR | Les petites levées restent déclaratives |
| Companies House, Royaume-Uni (W3-5,6,7,8) | Dépôt légal ; micro-entité (CA ≤ 1 M£) : bilan seul ; petite (CA ≤ 15 M£) : comptes abrégés possibles ; audit non lu | Lot iXBRL gratuit (download.companieshouse.gov.uk/en_accountsdata.html, ~75 % des comptes, fichier gardé 60 jours) ; API : clé, 600 requêtes/5 min, gratuité non confirmée | Le CA d'une petite société rentable est souvent invisible |
| Allemagne : Unternehmensregister, Bundesanzeiger (W3-9,10) | Petite société (2 critères sur 3 : CA ≤ 15 M€, bilan ≤ 7,5 M€, ≤ 50 salariés) : bilan + annexe sans compte de résultat ; micro : bilan seul ; audit seulement au-dessus | Coût non confirmé ; pas de recherche plein texte des comptes sur Bundesanzeiger | Le CA des petites GmbH n'est en général pas public |
| OpenCorporates (W3-15) | Données de registre ; la page tarifs ne cite aucun compte annuel | Payant : 2 250 à 12 000 £/an ; gratuit pour journalistes, ONG, universités | Ne prouve pas le CA |
| FDD américains, franchises (W3-11,16) | Item 19 : facultatif, déclaratif avec justification écrite ; Item 21 : comptes du franchiseur audités | Bases d'États gratuites (Californie, Wisconsin, Minnesota) d'après un cabinet ; sites officiels en 403 | Seulement les franchiseurs enregistrés dans l'État ; lire l'échantillon et les exclusions de l'Item 19 |
| Inc. 5000 (W3-12) | CA 2021 et 2024 sur états financiers signés par le dirigeant et un tiers qualifié : contrôle documentaire, pas audit | Public ; méthode d'Inc. lue en seconde main (403) | Classement de croissance (CA final ≥ 2 M$), rien sur la marge |
| FT 1000 Europe (W3-13) | Formulaire signé par le dirigeant ou le directeur financier : auto-certification | Public ; seuils 100 k€ (2022) et 1,5 M€ (2025) | Croissance « primarily organic » ; aucune pièce comptable exigée sur la page |
| Deloitte Fast 500 (W3-14) | Page : « public company databases » ; pièces justificatives = extrait de recherche non ouvert ; CA non publié | Public ; seuil 5 M$ (FY2025) | Croissance seulement ; technologie propriétaire exigée |
| Revenus lus chez Stripe : Indie Hackers, Baremetrics (W3-17,18) | Encaissements bruts lus chez le processeur : vérifié, mais Stripe seul et sans bénéfice | IH en 403 ; Baremetrics Open Startups = article de 2015 (7 startups), statut actuel inconnu | Sur 937 produits IH vérifiés, plus de 54 % à zéro (2022) ; affichage au choix, comptes partagés (extrait) |

## B. Signaux de demande : signal → ce qu'il prouve → fiabilité → coût
| Signal (preuves) | Ce qu'il prouve | Fiabilité | Coût |
|---|---|---|---|
| Google Trends (W3-19) | Intérêt relatif 0 à 100 par zone et période ; termes rares à 0 ; pas de volume absolu | Moyenne (tendance) | Gratuit |
| Keyword Planner (W3-20) | Estimations mensuelles de recherches et de coûts ; compte Google Ads avec facturation exigé | Moyenne ; tranches de volume non confirmées | Gratuité non confirmée |
| Meta Ad Library (W3-22) | Pubs commerciales actives et date de début ; dépenses seulement pour pubs politiques | Faible pour la rentabilité | Gratuit |
| Google Ads Transparency Center (W3-23,24) | Annonceur et pubs servies ; conservation contradictoire (365 jours selon un blog, 30 selon des extraits) | Faible | Gratuit |
| Durée de diffusion d'une pub = rentable ? (W3-25) | Aucune étude favorable trouvée ; étude eBay : rendement réduit à une fraction des estimations non expérimentales | Très faible, ne jamais l'utiliser seule | Sans objet |
| Offres d'emploi (W3-26,27) | Hiring Lab : indice Indeed par secteur, France incluse, CC BY 4.0 ; France Travail : compte gratuit, 1 150 offres/requête et 10 appels/s selon un blog | Moyenne pour un secteur, faible pour un modèle | Gratuit |
| Applications : Appfigures, Sensor Tower (W3-28,29) | Estimations modélisées, erreur ±30 à 50 % par app selon un concurrent | Faible à moyenne (ordre de grandeur) | Appfigures gratuit (5 apps) ; Sensor Tower sans offre gratuite (extrait) |
| ComeUp, Codeur (W3-48,49) | ComeUp : note, avis, ventes par vendeur ; Codeur : besoin publié, tranche de budget, nombre d'offres | Moyenne (cumulés, sans définition) | Gratuit |
| Vitesse des avis (W3-30) | La note influence les ventes relatives (livres) ; aucun ratio avis → ventes sourcé | Faible sans calibrage | Gratuit |
| Repères Unbounce 2024 (W3-31,32) | 41 000+ pages, 57 M+ conversions, médiane 6,6 % ; pages sans conversion exclues ; conversion ≠ paiement | Faible comme seuil | Gratuit |
| Force des preuves (W3-33,34,35) | Seuil écrit avant (Test Card) ; ce que les gens font > ce qu'ils disent ; échelle exacte du livre non lue | Moyenne (sources secondaires) | Sans objet |

## Recommandations pour une porte 2 sans entretiens
1. Preuve étrangère : ne retenir comme chiffre fiable qu'un CA audité (SEC, comptes au-dessus des seuils allemands et britanniques, Form C > 618 k$, Item 21) ou lu chez le processeur de paiement ; marquer « déclaré » tout le reste (Item 19, Inc., FT, Deloitte, Stripe-IH).
2. Trier la demande française avec les signaux gratuits (Trends, France Travail, Hiring Lab, Codeur, ComeUp, Keyword Planner si accessible) mais ne jamais les compter comme « engagement » : ni la durée d'une pub ni le nombre d'avis ne prouvent la rentabilité.
3. Engagement = précommande ou dépôt remboursable, pas un clic ni un e-mail ; seuil écrit avant (W3-33), calculé sur ses propres hypothèses de prix et de coût du trafic, pas sur la médiane Unbounce de 6,6 %.
4. Cadre légal d'un test payant : dire que le produit n'existe pas encore et donner la date de livraison (L. 121-2 2° a, L. 121-3, L. 221-5 3°, L. 216-1 : 30 jours par défaut), bouton « commande avec obligation de paiement » (L. 221-14), remboursement possible 14 jours (L. 221-18) ; la pratique trompeuse coûte jusqu'à 2 ans et 300 000 € (L. 132-2) et vaut aussi en B2B (L. 121-5) ; jurisprudence non cherchée : l'auditeur valide.
5. E-mails : liste d'attente = consentement explicite et informations de l'article 13 du RGPD (responsable, finalité, durée, droits) ; prospection B2C par e-mail seulement après consentement, B2B si le message touche leur profession et que l'opposition est gratuite (CNIL, L. 34-5 CPCE).
