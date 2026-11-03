# Registre des sources fiables (testé le 2026-11-03)

Niveaux : N1 donnée officielle ou comptes déposés lus par API ; N2 page primaire ouverte ; N3 presse ou étude à
méthode publiée ; N4 blog, vendeur d'études, annonce non auditée, résumé IA ; N5 extrait de recherche (jamais une preuve).
Un chiffre utilisé dans un score est N1 ou N2. Détails et preuves : `methode/audit-2026-11/` (W2, W3, W4).

## Les chiffres standard : `outils/donnees.py` (gratuit, sans clé, URL affichée à chaque sortie)

| Preuve | Commande | Source | Pièges |
|---|---|---|---|
| Taille du secteur (M€, nb d'entreprises) | `taille 43.21Z` | Eurostat `sbs_ovw_act` (alimenté par l'Ésane de l'INSEE) | plafond, pas un SAM ; retard ~20 mois ; ruptures de séries 2017 et 2021 ; secret statistique sur certains codes |
| Croissance | `croissance 43.21Z` | INSEE Melodi `DS_ICA`, indices mensuels de CA issus de la TVA | indice en valeur (inflation comprise) ; comparer à la médiane des secteurs (`ecran`) |
| 2 sources dont 1 institutionnelle | `taille` + `croissance` | Ésane/Eurostat et TVA/INSEE : deux sources statistiques distinctes | Eurostat et Ésane ne comptent que pour une |
| Nombre de clients B2B | `compter 43.21Z` | API Recherche d'entreprises (Sirene, RNE) | unités légales au répertoire (micro sans activité incluses) : lire « employeuses » et « 10 salariés ou plus » |
| Plus gros acteurs, concentration | `acteurs 43.21Z` | même API, filtre `ca_min`, champ `finances` | ≈ 45 % des dépôts de comptes confidentiels (INPI, 13/05/2025) : part des 3 premiers = borne basse ; entités, pas groupes ; un seul exercice par entité (pas de croissance par acteur) |
| Argent public dépensé | `marches-publics "mots"` | DECP, data.economie.gouv.fr | plancher : déclaration due dès 40 000 € HT, sans sanction ; accords-cadres en montant maximal |
| Échecs du secteur | `echecs "mots"` | BODACC, procédures collectives | plusieurs annonces par entreprise ; plein texte |
| Repérer les marchés en croissance | `ecran --min 50` | Eurostat, 472 secteurs à 4 chiffres en une requête | rebond post-Covid signalé ; taille ≠ marché adressable |
| Page bloquée (403) | `archive <url>` | Internet Archive, API Wayback | citer la copie et sa date |
| Qualité d'un fichier de preuves | `controle <fichier>` puis `python -I outils/verifier-citations.py <fichier>` | — | présence de la citation, pas soutien ; faux ABSENT sur PDF compressés sans pdftotext |

## Autres sources N1-N2 (accès manuel)
- **Survie des entreprises** : INSEE, enquête SINE (taux à 5 ans par secteur, génération 2018 : commerce 63,9 %, finance 77,3 %, ensemble 69,0 % ; sociétés 70,6 %, entreprises individuelles 63,3 % ; micro-entrepreneurs 28 %). insee.fr/fr/statistiques/2015357 et 8634190.
- **Défaillances** : Banque de France, publication mensuelle (nombres, pas de taux par secteur).
- **Consommation des ménages par produit** (B2C) : INSEE Melodi `DD_CNA_CONSO_MENAGES_PRODUITS` (comptes nationaux, grandes catégories).
- **Établissements employeurs** par département × secteur × taille : Open Urssaf.
- **Droit** : Légifrance (articles en vigueur, date) ; entreprendre.service-public.fr.
- **Concentrations** : décisions de l'Autorité de la concurrence (marchés de plus de 80 M€ France).
- **Comptes d'une société étrangère** : SEC EDGAR (`data.sec.gov/api/xbrl/companyfacts/...`, audités, agent utilisateur avec contact exigé) ; Companies House (Royaume-Uni, comptes en masse gratuits, petites sociétés sans CA) ; Unternehmensregister (Allemagne, petites GmbH sans CA) ; Form C au-delà de 618 k$ (audité) ; FDD Item 21 (comptes audités du franchiseur).

## Sources N4 : à étiqueter « déclaré », jamais seules dans un score
Acquire, Flippa, Dotmarket (annonces de vendeurs) ; Item 19 des FDD ; Inc. 5000, FT1000, Deloitte Fast 500,
Champions de la croissance (formulaires signés, pas d'audit) ; TrustMRR et Indie Hackers (encaissements Stripe,
sans marge ; 54 % des produits vérifiés d'IH à zéro en 2022) ; Xerfi (990 à 6 200 € HT, méthode non publiée),
Statista, Businesscoot, Mordor ; Starter Story.

## Signaux de demande en ligne (aucun ne prouve un achat)
Google Trends (relatif) ; Keyword Planner (compte Google Ads) ; Meta Ad Library et Google Ads Transparency
(présence de pubs ; la durée de diffusion ne prouve pas la rentabilité, étude eBay NBER w20171) ; Indeed Hiring
Lab et API France Travail (secteur) ; Codeur, ComeUp (besoins publiés, budgets) ; médiane de conversion des pages
Unbounce 6,6 % (2024, pages sans conversion exclues) : repère, pas seuil.

## Bloqués connus
reddit.com, pappers.fr, societe.com, malt.fr, economie.gouv.fr/dgccrf et /daj, statista.com, sifted.eu,
lelab.bpifrance.fr, data.inpi.fr (compte requis), openai.com, inc.com, bases FDD des États, avis Google Maps et
stores d'applications. Jamais d'imitation de navigateur pour passer un blocage.
