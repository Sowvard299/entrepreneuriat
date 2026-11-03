# Audit complet du système (2026-11-03)

Périmètre : CLAUDE.md, les 3 agents, `market-segment-scanner`, le guide v4, les runs du 2026-11-02 (11 fichiers de
chercheurs, 4 contrôles), et une veille web de 4 chercheurs (`w1` à `w4`, 154 preuves, 18 preuves décisives
re-vérifiées : 16 ✔, 2 ≈, 0 ✘, voir `verification.md`).

## Verdict
Le système échouait moins par sa méthode que par sa **chaîne de preuve** : il demandait à des agents de trouver
sur le web des chiffres qui existent déjà, gratuits, dans des bases officielles, et il les laissait citer des
extraits de recherche sans ouvrir la page. Résultat : 10 à 70 % d'erreurs au contrôle, et aucune taille de marché
en euros ni part de marché trouvée sur 4 fiches neutres. Ces chiffres sortent maintenant en quelques secondes,
avec leur URL, de `outils/donnees.py`.

## Constats internes (preuves tirées de nos runs)
| # | Défaut | Preuve | Correctif appliqué |
|---|---|---|---|
| 1 | L'extrait de recherche était accepté comme preuve | `chercheur.md` : « ouverte ou vue en extrait » ; fiche B2B : 14 preuves, toutes en extrait ; script : 7 EXTRAIT sur 20 citations (mrr) | niveaux N1-N5, extrait = jamais une preuve ; script `verifier-citations.py` avant rendu |
| 2 | Erreurs fréquentes | contrôles : distribution 60 %, mrr 70 %, reprise 20 %, Acquire 10 %, neutre 6/16 ≈ ou ✘ | contrôle automatique d'abord, vérificateur sur le soutien de l'énoncé |
| 3 | Chiffres standard cherchés sur le web | taille en € et parts « introuvables » dans les 4 fiches neutres ; obtenus par l'outil pour 43.21A : 49,0 Md€, +4,9 %/an, top 3 ≥ 7,1 % | `outils/donnees.py` obligatoire (CLAUDE.md, chercheur, auditeur) |
| 4 | Contre-preuves manquées | procédures collectives « borne de recharge » : 26 (2024), 49 (2025), 52 (2026), absentes de la fiche qui classait la piste 1re | `echecs` dans la fiche et dans l'audit |
| 5 | « Argent dépensé » = prix affichés | grille : « 3 prix publics » | redéfini : CA du secteur + CA déposés d'acteurs ou marchés publics, + prix |
| 6 | Notes faussement précises, poids sans fondement | audit v3 (7,35 contre 7,20) ; W4 : aucune source ne fonde 25/25/20/15/15 | taux de base INSEE + niveau de preuve + 3 probabilités datées |
| 7 | Porte 2 impossible sans entretiens | refus de l'équipe ; score plafonné à 7,5 | précommande légale sur page de test (articles vérifiés) |
| 8 | Idées tirées de la mémoire du modèle | B2C : 7 marques américaines célèbres (Crumbl, Club Pilates…) | porte 0 « écran » : 472 secteurs classés par croissance (Eurostat) |
| 9 | Vérificateur sans recherche, juge la présence | il a tenté de lire Bing et DuckDuckGo ; W1 | WebSearch (2 par preuve), soutien, lecture à l'aveugle, copie archivée |
| 10 | Références périmées, budgets incohérents | auditeur → `_recherche-v3/idees-classees.md`, « ambition chiffrée » ; 20 recherches dans l'agent, 12 dans les missions | corrigé ; 15 recherches par défaut |
| 11 | Sessions parallèles dans `porte1/` | fichiers agro et énergie d'une autre session commités par erreur le 2026-11-02 | une session = un sous-dossier + une ligne dans `etat.md` |
| 12 | Trop de guides | 3 guides et 2 audits à la racine | anciens rangés dans `methode/historique/` |

## Ce que la veille a établi (détail dans les synthèses)
- W1 (agents) : ouvrir avant de citer, citation copiée et retrouvée par script, verdict de soutien, lecture
  latérale, brief complet ; les taux d'erreur de citation publiés (25 à 60 %) rendent les nôtres plausibles.
- W2 (sources FR) : Ésane/Eurostat pour la taille, indices de CA TVA pour la croissance ; ≈ 45 % des comptes
  confidentiels ; DECP = plancher (40 000 € HT) ; Xerfi 990 à 6 200 € HT sans méthode publiée.
- W3 (étranger, demande) : seuls les comptes audités ou lus chez le processeur de paiement sont fiables ;
  aucun signal gratuit ne prouve la rentabilité ; cadre légal d'une précommande test.
- W4 (notation) : survie à 5 ans par secteur (63,9 à 77,3 %), probabilités et score de Brier, pas de bonus
  d'ordre d'entrée.

## Ce qui reste faible
- La demande n'est toujours prouvable que par une précommande payée : aucun outil ne la remplace.
- La concentration calculée est une borne basse (comptes confidentiels, groupes non consolidés).
- Les gains des règles W1 ne sont mesurés par aucune source : à mesurer sur la prochaine vague (taux d'ABSENT).
- Non testé : SEC EDGAR (exige un contact déclaré dans l'agent utilisateur), Companies House, hook SubagentStop.
