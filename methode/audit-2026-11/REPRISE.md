# Audit du système (2026-11-03) : état et reprise

Arrêt à 96 % de la fenêtre de 5 heures du forfait (remise à zéro le 2026-11-03 vers 14 h 10, heure de Paris).

## Fait
- `outils/donnees.py` : API publiques testées sans clé (Eurostat SBS, INSEE Melodi DS_ICA, API Recherche
  d'entreprises avec filtre `ca_min`, DECP, BODACC, Wayback) ; commandes `taille`, `croissance`, `compter`,
  `acteurs`, `marches-publics`, `echecs`, `archive`, `fiche`, `ecran` (472 secteurs), `controle`.
- Veille web : `w2-sources-fr-synthese.md`, `w3-preuves-demande-synthese.md`, `w4-notation-synthese.md` (finis, partiels).
- `w1-agents-*` : méthodes de recherche par agents (Anthropic, vérification) : peut-être coupé, relire son statut.

## À faire
1. Relancer W1 s'il est coupé (chercheur : relire `w1-agents-travail.md` et continuer sans doublon).
2. Un `verificateur` : 10 preuves décisives par fichier w1 à w4 (priorité : W2-11 confidentialité 45 %, W2-10 seuil
   DECP 40 000 €, W3 articles du Code de la consommation, W4-1 taux de survie Insee).
3. Écrire `methode/audit-2026-11/audit.md` : constats internes (taux d'erreur 10-70 %, extraits non ouverts,
   références périmées des agents, budgets incohérents, sessions parallèles dans `porte1/`) + veille.
4. Appliquer : CLAUDE.md (niveaux de source, chiffres standard par `outils/donnees.py`, argent dépensé redéfini,
   notation par taux de base Insee + probabilités + niveau de preuve, porte 2 sans entretiens = précommande
   légale), agents (chercheur, verificateur avec WebSearch, auditeur), `methode/sources-fiables.md`,
   `market-segment-scanner` (partir de `ecran`), ranger les vieux guides.

## Prompt à coller
```text
Lis CLAUDE.md puis methode/audit-2026-11/REPRISE.md et reprends l'audit du système à l'étape « À faire » 1.
Lis l'usage (get_usage) avant chaque vague. Ne lis que les fichiers de synthèse (40 lignes).
Commite et pousse sur claude/recherche-idee-v1 après chaque étape.
```
