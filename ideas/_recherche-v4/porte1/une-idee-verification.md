# Vérification des preuves chiffrées (porte 1, 2026-11-02)
Vérificateur : contrôle par WebFetch (pages ouvertes) et API Sirene (curl). Fichiers contrôlés : jamais modifiés.
Priorité appliquée : U-ETR-02 à 05 et U-FRA DUERP (10, 11) et biodéchets (03, 04, 05).
Non contrôlé = hors échantillon ou page non rouverte ; ce n'est pas un verdict.

## Fichier 1 : une-idee-etranger-travail.md

| ID | URL | verdict | écart constaté |
|----|-----|---------|----------------|
| U-ETR-01 | starterstory.com/ideas/productized-service-business/success-stories | ✔ | Citation exacte. Design Joy 1,74 M$, Draftss 480 k$, Scribly 444 k$, Thankbox 420 k$ conformes. Date de la page non visible. |
| U-ETR-02 | ibtimes.co.uk/...1728621 | ✔ | Citation exacte. Publié le 30 novembre 2024 (conforme). Plus d'1 M£/an, 4 000 £ (5 000 $)/mois, jusqu'à 20 clients, 140 £ de frais : conformes. |
| U-ETR-03 | designjoy.co | ≈ | Prix $4,995, « One request at a time », « Avg. 48 hour delivery », « PAUSE OR CANCEL ANYTIME » trouvés. Mais le prix est présenté comme offre « Lifetime Discount - Limited Time » (ancien prix barré 5 995 $) : le fichier parle de « prix public actuel ». Date 2026-11-02 non vérifiable (page non datée). |
| U-ETR-04 | penji.co/pricing | ✔ | 995 $, 1 995 $, 4 500 $/mois conformes ; -15 % trimestriel et -20 % annuel affichés. Montants réduits non affichés (calcul seul). |
| U-ETR-05 | comeup.com/fr/service/476358/... | ✔ | Citation exacte, 1 495 € de base, 13 ventes au total, aucun avis sur ce service. Date non visible dans la page. |
| U-ETR-06 | starterstory.com/stories/thankbox | ≈ | « pulls around $25k in revenue », titre 35 k$, prix 5,99 $ / 9,99 $, 2 fondateurs, 3 salariés : conformes. « 140 k$ en 2021 » : le montant 140k est trouvé (« ending with total revenue of $140k ») mais l'année 2021 n'apparaît pas dans l'extrait. |
| U-ETR-07 | kudoboard.com/pricing | ✔ | Citation exacte. Business 39 $/mois (299 $/an), Pro 59 $/mois (449 $/an), Enterprise sur devis : conformes. La page affiche aussi 25 $ et 38 $/mois (formule annuelle), non mentionnés. |
| U-ETR-08 | smith.ai/pricing | ✔ | « Ask about enterprise pricing. » exacte. 300 $ (30 appels), 810 $ (90), 2 100 $ (300) conformes ; dépassements 11,50 / 10,50 / 8,50 $ (fichier : 8,50 à 11,50 $) conformes. |
| U-ETR-09 | ruby.com/pricing/ | ≈ | Prix 250 / 395 / 720 / 1 725 $/mois conformes. La citation « Great for small businesses of all kinds » est présente mais uniquement sous le forfait 200 min à 720 $, pas comme description de l'offre entière. |
| U-ETR-10 | cloudtalk.io/fr/blog/... (MAJ 2026-09-04) | ≈ | « L'IA de réception est disponible dès €99/mois pour 200 minutes » : quasi exact. Aircall 175 €/500 min, Rosie 49 €/250 min, Dialzara 99 €/220 min : chiffres justes mais formulations paraphrasées (« dès €175/mois (500 min) » ; « forfait Professional ... coûte €49 »). Date de mise à jour 4 septembre 2026 : conforme. Page lue sur 100 000 caractères sur 109 545 (le reste non lu). |
| U-ETR-11 | trustmrr.com | non contrôlé | Hors échantillon. |

Taux (≈ + ✘) sur les chiffres de l'échantillon : 4 / 10 = 40 %. Aucun chiffre faux ; les ≈ portent sur le contexte (promo, forfait), une date (2021) et des formulations. U-ETR-03 et U-ETR-06 sont à corriger avant usage dans un score.

## Fichier 2 : une-idee-france-travail.md

| ID | URL | verdict | écart constaté |
|----|-----|---------|----------------|
| U-FRA-03 | ecologie.gouv.fr/biodechets | ✔ | Citation exacte. Publié le 15 septembre 2023, mis à jour le 27 décembre 2023, « Depuis le 1er janvier 2024 » : conformes. |
| U-FRA-04 | entreprises.cci-paris-idf.fr/...valorisation-des-dechets | ✔ | « un coût mensuel fixe qui commence à 60€ par mois » et « généralement plafonnés autour de 100€ mensuels » exactes. Publié le 05 novembre 2024 : conforme. Joyeux Recycleurs et Moulinot cités. |
| U-FRA-05 | API recherche-entreprises.api.gouv.fr (curl, 2026-11-02) | ✔ | Moulinot Compost & Biogaz 2024 : CA 10 866 171 €, résultat -2 359 387 € conformes. Nouvelle-Aquitaine 1 442 288 € / -1 031 268 € et Pays de la Loire 266 462 € / -1 003 114 € conformes. Les Alchimistes (U-FRA-08) : 6 375 821 € / -1 946 911 € conformes. |
| U-FRA-02 | companeo.com/defibrillateur/guide/dae-cout-installation-comparatif | non contrôlé | Chiffres 150-350 €/an non rouverts (hors échantillon). |
| U-FRA-01 | amf.asso.fr | non contrôlé | Hors échantillon. |
| U-FRA-06 | API Sirene (comptes d'établissements) | non contrôlé | Hors échantillon ; pas de requête de comptage faite. |
| U-FRA-07 | fr.trustpilot.com | non contrôlé | Hors échantillon. |
| U-FRA-10 | plateya.fr/blog/detail/cout-duerp-2026-... | ≈ | « dès l'embauche du premier salarié » exacte ; tranches 489-750 / 750-1 200 / 1 200-1 800 / 1 800-2 500 € conformes ; 4 000 €/salarié conforme. « loi du 11 mai 2026 » absent tel quel : la page écrit « loi de lutte contre les fraudes sociales et fiscales, définitivement adoptée par le Parlement le 11 mai 2026 ». |
| U-FRA-11 | comeup.com/fr/service/523525/... (et 508181) | ≈ | Citation « Le DUERP est OBLIGATOIRE... dès le 1er salarié » exacte ; 71,64 € et 0 vente conformes ; « indisponible à la vente » conforme. « 71,64 € TTC » : la page n'indique pas TTC (« vendeur non assujetti à la TVA »). Offre 143,26 € (URL 508181) non rouverte. |
| U-FRA-12 | inrs.fr/...focus-juridique-document-unique-evaluation-risques.html | ✔ | Citation « à ce jour, le portail dématérialisé n'est toujours pas disponible » exacte ; mise à jour 04/10/2024 conforme. |
| U-FRA-13 | groupama.fr/prix-ramonage ; travaux.obat.fr | non contrôlé | Hors échantillon. |

Taux (≈ + ✘) sur les chiffres de l'échantillon : 2 / 7 = 29 %. Aucun chiffre faux ; les ≈ portent sur la formulation et le TTC. U-FRA-02, 06 et 07 restent à contrôler avant un score.

## Bilan
- Fichier etranger : 6 ✔, 4 ≈, 0 ✘, 1 non contrôlé (sur 11).
- Fichier france : 5 ✔, 2 ≈, 0 ✘, 5 non contrôlés (sur 14 preuves, 7 contrôlées).
- Pas de ✘. Aucune preuve n'est à déclasser ; les ≈ U-ETR-03 (promo), U-ETR-06 (année 2021) et U-FRA-10/11 (libellés) sont à reformuler.
