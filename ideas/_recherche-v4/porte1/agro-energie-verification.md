# Vérification : agro-energie-travail.md (2026-11-02)

Contrôle du `verificateur`, recopié par le coordinateur (l'agent n'a pas pu écrire le fichier).

| ID | URL | Verdict | Note |
|----|-----|---------|------|
| E-AE-01 | https://edito.seloger.com/node/19961 | ✔ | Citation exacte, datée du 21 oct. 2025 (le fichier de travail dit « date inconnue »). |
| E-AE-02 | https://www.xerfi.com/presentationetude/le-courtage-d-energie_sco75 | ≈ | « Plus de 70 acteurs », « plus de 40 % » créés depuis 2021 et 1 500 € HT exacts ; « clients surtout PME/ETI/public » : la page dit « quasi exclusivement BtoB », sans part chiffrée. |
| E-AE-03 | opera-energie.com/courtage-en-energie-restaurant/ ; /facture-electricite-boulangerie/ | ✔ | Trustpilot 4,9 sur 523 avis, Google 4,8, 18 villes (plancher). 99 000 kWh attribués à Engie. « Acteur à 38 M€ » non contrôlé. |
| E-AE-04 | fr.trustpilot.com/review/opera-energie.com?stars=1&stars=2 | ✔ | Deux citations exactes (28/01/2025, 07/07/2024). « Moins de 1 % d'avis 1-2 étoiles » non vérifié. |
| E-AE-05 | assemblee-nationale.fr (proposition de loi n° 1845) | ✔ | Déposée le 16/09/2025, renvoyée à la commission des affaires économiques, ni adoptée ni rejetée au 02/11/2026. Contenu (registre, décret après avis CRE) non lu : PDF illisible. |
| E-AE-06 | thecaterer.com/news/hospitality-energy-bill-legal-challenge-hidden-fees | ✔ | Citation exacte ; « more than 1,700 » restaurateurs ; montants formulés comme possibles. |
| E-AE-07 | services.totalenergies.fr/.../boulangerie-comment-economiser-energie | ✔ | 5 % du CA exact ; cuisson 1er poste, froid 2e. Date non vérifiée. |
| E-AE-08 | banquedesterritoires.fr/boulangeries-les-aides-en-place-... | ✔ | Daté du 13/12/2022 ; facture × 3 avant aides. |
| E-AE-09 | opera-energie.com/bat-eq-125/ | ✔ | kWh cumac par mètre exacts. BAT-EQ-134 (489 €) et BAT-EQ-124 non ouverts. |
| A-01 10.71C | API recherche-entreprises | ✔ | 6-9 salariés : 5 713 ; 10-19 : 4 701 ; 20-49 : 1 274 ; total 6-49 = 11 688. |
| A-01 56.10A | API recherche-entreprises | ✔ | 6-9 : ≥ 10 000 (plafond) ; 10-19 : 9 099 ; 20-49 : 3 172. |

Hors fichier : le code 47.24Z (commerce de pain) ne compte que 399 unités de 6 à 49 salariés. Le segment
« boulangeries » repose donc sur 10.71C (boulangerie-pâtisserie artisanale), ce qui est le bon code.

## Bilan

1. 10 contrôles : 9 ✔, 1 ≈ (E-AE-02), 0 ✘. Taux ✘ + ≈ = 10 %, sous le seuil de 20 %.
2. À corriger, pas à déclasser : E-AE-02 (« surtout PME/ETI/public »), date d'E-AE-01, « < 1 % » d'E-AE-04, « 38 M€ » d'E-AE-03.
3. Proposition de loi n° 1845 sur le courtage en énergie : déposée, non votée. Contenu à faire lire par l'`auditeur`.
4. Le fichier de travail annonce 20 preuves mais n'en liste que 15 plus A-01.
