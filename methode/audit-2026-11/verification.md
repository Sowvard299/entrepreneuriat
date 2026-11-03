# Vérification de la veille (2026-11-03)

Vérificateur (haiku), 18 preuves décisives, rapport rendu en message et recopié ici par le coordinateur.

| Fichier | ✔ | ≈ | ✘ | ? | Écarts |
|---|---|---|---|---|---|
| w2-sources-fr-travail.md | 4 | 2 | 0 | 0 | W2-10 : « Théoriquement » (pas « théorique »), 40 000 € HT et date justes ; W2-3 : citation abrégée, chiffres justes |
| w3-preuves-demande-travail.md | 6 | 0 | 0 | 0 | L.121-2, L.132-2, L.221-14, L.221-18 lus sur Légifrance ; Unbounce 6,6 % ; NBER w20171 (eBay) |
| w4-notation-travail.md | 6 | 0 | 0 | 0 | survie Insee à 5 ans (12 secteurs), 69,0 / 70,6 / 63,3 %, micro 28 %, défaillances Banque de France 70 766 |

Aucun ≈ ni ✘ ne porte sur un chiffre utilisé. W1 : 105 citations anglaises retrouvées mot pour mot par
`outils/verifier-citations.py` (contrôle du chercheur lui-même).

## Calibrage du contrôle automatique (`outils/verifier-citations.py`)
| Fichier ancien | Vérificateur humain-IA (02/11) | Script (03/11) |
|---|---|---|
| porte1/modeles-mrr-travail.md | 3 ✔ / 7 ≈ ou ✘ | 8 OK / 5 ABSENT / 7 EXTRAIT |
| porte1/neutre-marches-travail.md | — | 14 OK / 1 ABSENT / 0 EXTRAIT |
Le script retrouve les mêmes fichiers faibles que le vérificateur, en quelques secondes et sans modèle.
Il vérifie la présence d'une citation, pas qu'elle soutient l'énoncé : le vérificateur reste nécessaire pour ça.
