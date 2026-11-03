# Pistes v5 : premier passage du système audité (2026-11-03)

Méthode : `outils/donnees.py ecran` (435 secteurs ≥ 200 M€, médiane +3,2 %/an) → 7 secteurs → fiches N1
(`porte1/v5/fiche-*.md`) → 3 écartés sur chiffres → 2 chercheurs (`porte1/v5/s1-*`, `s2-*`) → contrôle des
citations (OK 18, ABSENT 1, BLOQUÉ 5) → vérificateur (`porte1/v5/verification.md` : ✔ 7, ≈ 3, ✘ 0, ? 1 ;
S1-8, S1-17, S2-15 déclassées en partie, S2-6 non vérifiée).

## Écartés sur les chiffres officiels, sans recherche web
| Secteur | Raison (N1) |
|---|---|
| 82.11 Services administratifs de bureau (+9,7 %/an) | 3 entités = 87 % du CA : croissance de centres de services de groupes, pas un marché ouvert |
| 93.19 Autres activités liées au sport (+5,2 %/an) | 3 entités = 47 % (LFP, hospitalité JO 2024, ASO) : effet d'événements |
| 77.39 Location d'autres équipements | secteur hétérogène (pylônes, palettes), 1 266 employeuses |

## Classement en probabilités (pas de 5 points, datées du 2026-11-03)
Taux de base : survie à 5 ans des sociétés, génération 2018 (INSEE SINE) ; à 3 ans, sociétés 83,4 %.

| Piste | Classe (survie 5 ans) | P(porte 2) | P(en vie à 3 ans) | P(CA ≥ 500 k€ à 3 ans) | Ce qui déplace la probabilité (N1-N2) | Contre-preuve |
|---|---|---|---|---|---|---|
| Maintenance du froid commercial et des cuisines pros, abonnement à délai garanti | industrie 73,4 % | 30 % | 80 % | 30 % | 5 acteurs de 6 à 20 M€ (S1-17, N1) ; marchés publics cuisine 7 (2022) → 163 (2025) (S1-22, N1) ; 81 % des recrutements de frigoristes difficiles (S1-20, N3) | aucun prix public N2 ; un acteur cité est déficitaire (S1-17 ≈) ; attestation fluides frigorigènes à citer |
| Rotation de linge pour la location courte durée hors Paris | autres services 69,5 % | 30 % | 70 % | 20 % | 14,95 € HT le jeu (S1-7, N2) ; 16 % d'avis 1-2 étoiles chez un acteur (S1-9) | Laundryheap France : 2,2 M€ de CA, perte (S1-8 ≈) ; croissance du secteur surtout de prix (Elis +3,2 % organique) |
| Aide à domicile, agence privée à équipes de quartier | enseignement-santé 74,1 % | 25 % | 65 % | 35 % | acteurs N1 à 91-298 M€ (S2-2) ; Petits-fils 56 % d'avis 1-2 étoiles (S2-9, N3, canal unique) | marges 0-4 % ; procédures collectives 252 → 436 (2022-2024, S2-4) ; prix 2026 non vérifiés (S2-6 ?) ; autorisation CASF L313-1 |
| Collecte de biodéchets pour petits producteurs | services 69,0 % | 25 % | 55 % | 20 % | obligation depuis le 1er janvier 2024 (L541-21-1, S2-14, N1) ; 248 marchés publics « biodéchets » en 2024 | Moulinot et Les Alchimistes en perte (S2-15 ≈) ; Rubicon : 675 M$ de CA, -282 M$ (SEC, S2-20) ; procédures collectives en hausse |
| Linge des résidents d'EHPAD | autres services 69,5 % | 20 % | 75 % | 30 % | Bulle de Linge 40,1 M€, 950 établissements (S1-2, N1) | aucun prix public ; marchés publics en plafonds |

Lecture : aucune piste ne se détache de plus de 10 points ; aucune ne passe encore la porte 1 au sens strict
(3 prix publics N2 manquent partout sauf, peut-être, l'aide à domicile, dont les prix ne sont pas vérifiés).
La meilleure combinaison de signaux N1 est la maintenance du froid commercial.

## Mise à jour après audit (2026-11-03, `ideas/froid-commercial/`)
Maintenance du froid commercial : 30/80/30 → **25/80/25** (porte 2 / en vie à 3 ans / 500 k€ à 3 ans).
Prix publics N2 : 680 € HT/an (sans garantie de délai) et 970 € par site, sous l'hypothèse de 1 200 € ; droit
cité (R543-78, R543-79, R543-99, arrêté 2016 art. 4) ; interdiction 2030 des fluides régénérés ≥ 2500 PRG.
Vérification : ✔ 6, ≈ 2 ; F-6 nuancé (Quietalis, 83,5 M€, montre qu'un acteur peut grossir, d'où 25 % et non 20 %
sur le CA) ; F-13 = annonces de procédures collectives de restaurants, pas des faillites (3 309 → 5 682).
Variante proposée : abonnement avec registre légal pour cuisines collectives et commerces de bouche.
Test de porte 2 proposé : dépôt remboursable de 150 €, 500 établissements d'une zone + 1 500 € de trafic ;
seuil : ≥ 10 dépôts, STOP sous 5.

## Avant la porte 2 (précommande légale)
- Froid commercial : 3 prix N2 de contrats d'entretien ; texte sur l'attestation de capacité (fluides frigorigènes).
- Linge courte durée : comptes de Laundryheap UK (Companies House) ; densité de tournée nécessaire.
- Aide à domicile : arrêtés de tarifs 2026 lisibles ; délai d'autorisation départementale.

## Limite découverte de l'outil
L'API Recherche d'entreprises ne donne qu'un exercice de comptes par entité : la croissance acteur par acteur
reste à lire dans les comptes déposés (INPI, compte requis).
