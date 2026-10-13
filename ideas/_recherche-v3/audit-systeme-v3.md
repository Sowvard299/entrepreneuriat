# Audit critique du système v3 (contre moi-même)

Date : 2026-10-13. Auteur : le coordinateur de la v3, qui critique son propre travail après la phase 0 et la
segmentation. Objectif : un système où l'idée est **viable dès le départ, puis confirmée**, et non une idée
trouvée en dernier puis testée au bout de 4 sessions.

## Verdict

La v3 corrige la v2 (marchés trop petits, idées génériques), mais elle a un défaut de fond : **elle cherche la
preuve au mauvais endroit.** Elle passe ses sessions à prouver la taille et la croissance d'un marché sur le web,
choses que les sources ouvertes ne prouvent presque jamais. Pendant ce temps, elle reporte à la phase 5 la seule
preuve qui compte pour une équipe autofinancée : *quelqu'un de précis paie, ou s'engage à payer.*

## Les 10 défauts, avec la preuve tirée de notre propre run

| # | Défaut | Preuve dans le run v3 | Gravité |
|---|--------|------------------------|---------|
| 1 | **Le seuil de croissance est intenable, donc contourné.** Aucun des 38 marchés ne prouve ≥ 8 %/an avec une source institutionnelle. Tout passe par la clause « moteur daté ». | `marches.md`, constat général | forte |
| 2 | **Ce contournement crée un biais vers les marchés de conformité** (obligations réglementaires) : pics ponctuels, outils publics gratuits, intermédiaires installés (experts-comptables, diagnostiqueurs), échéances reportées. | NIS2 reportée le 06/10/2026 pendant le run (A3) ; A1 : « plateformes gratuites » ; A10 : certification requise | forte |
| 3 | **Aucune preuve de prix réellement payé.** 38 marchés, presque aucun prix public pour les services visés. La disposition à payer, critère n°2 de la grille (20 %), est donc notée à l'aveugle. | synthèse A : « aucun prix », « appeler 5 syndics » | forte |
| 4 | **Notes faussement précises.** J'ai classé des segments à 7,35 contre 7,20 à partir de comptages et de paniers [HYPOTHÈSE]. Le critère Valeur sature (> 3 M€ = 10 pour presque tout) et les 10 % de pénétration sont arbitraires : le classement est surtout du bruit. | `segments.md` : 30 lignes sur 40 en [HYPOTHÈSE] | forte |
| 5 | **Le client est consulté en dernier.** Le mom-test arrive en phase 5, après environ 4 sessions et des centaines de milliers de tokens. Un « non » de 10 clients aurait tué une piste en 2 jours. | prompt maître v3, phase 5 | forte |
| 6 | **Coût insoutenable.** La phase 0 seule a consommé une large part d'un forfait Pro hebdomadaire ; un run complet demande plusieurs comptes. | quotas : 94 % de la semaine après la phase 0 | moyenne |
| 7 | **Les agents paraphrasent et n'accèdent pas aux sources officielles.** 43 % des preuves contrôlées sont approchantes ou fausses ; Légifrance, ADEME, ANIL, impots.gouv sont inaccessibles ; Google Trends bloqué. | `verification.md` | moyenne |
| 8 | **Le profil de l'équipe est vide, alors que c'est le levier le plus fort.** Sans réseau nommé, l'« accès » est noté au hasard. Le système ne demande pas « à qui pouvez-vous vendre lundi ? ». | `hypotheses.md` | forte |
| 9 | **Biais du coordinateur.** J'ai recommandé A2 pour l'avantage EDF, puis ma propre grille l'a sorti du Top 12. J'ai aussi retenu les marchés quand l'utilisateur a dit « continue » sans choisir. | `segments.md`, Top 12 ; `etat.md` | faible |
| 10 | **Le canal d'acquisition n'est jamais testé.** Pour 6 étudiants en marketing, la distribution est l'avantage principal ; le système devrait chercher les marchés où *le marketing est le goulot*, et le prouver par un test d'acquisition. | grille : canal noté, jamais mesuré | moyenne |

## Ce qui marche et qu'on garde

- Partir de l'argent déjà dépensé plutôt que des plaintes (ordre de force des preuves).
- Le piège « agence locale de plus » et le cimetière des modèles (v2).
- Les sous-agents moins chers, l'écriture au fil de l'eau, `etat.md`, la reprise après coupure (testée : erreur API, 4 agents repris sans perte).
- Le vérificateur : il a trouvé un prix faux (C3-p5) et une échéance déjà passée (A5).
- Le comptage des clients par l'API recherche-entreprises.

## Principe correctif : « preuve d'achat d'abord, taille ensuite »

1. **Porte 0, accès** (avant toute recherche) : remplir l'équipe et le réseau. Pour chaque piste, nommer
   20 clients joignables. Sans eux, la piste ne rentre pas.
2. **Porte 1, argent visible** (desk research courte, 1 agent) : au moins 3 concurrents avec prix publics et
   clients payants identifiables. Pas de taille de marché à ce stade : seulement « l'argent circule ».
3. **Porte 2, signal client** (terrain, 1 à 2 semaines, < 100 €) : 10 conversations Mom Test et un engagement
   concret (rendez-vous de démonstration, lettre d'intention, précommande, acompte).
4. **Porte 3, taille** : seulement pour les pistes qui passent la porte 2, dimensionnement bottom-up à partir
   des prix entendus en entretien, et chemin d'expansion.
5. **Porte 4, confirmation** : pilote payant, économie unitaire réelle, puis décision GO / PIVOT / STOP.

La recherche documentaire lourde (phases 0 et 1 actuelles) devient une **option de la porte 3**, pas le point de départ.

## Seuils à revoir dans CLAUDE.md (proposition, non appliquée)

- Croissance : garder « ≥ 8 % OU moteur daté », mais un moteur réglementaire compte seulement si la dépense
  **continue après l'échéance** (abonnement, contrôle annuel), sinon c'est un pic ponctuel.
- Ajouter un seuil éliminatoire « 3 prix publics payés par le segment » dès la porte 1.
- Ajouter un seuil éliminatoire « 20 clients nommés joignables » (porte 0) à la place de « 10 en une semaine ».
- Remplacer la note de Valeur saturée par le calcul : nombre de clients nécessaires pour 500 k€ ÷ clients
  joignables ; si plus de 5 % de la cible doit signer en 3 ans, la note baisse.

## Méthodes existantes à reprendre plutôt qu'à réinventer

Voir `veille-systeme.md` (veille GitHub, Reddit, Indie Hackers en cours) et la section « Système v4 » ajoutée
ci-dessous une fois la veille finie.

## Système v4 : ce qu'on reprend de l'existant et où (d'après `veille-systeme.md`)

Aucune méthode de praticien trouvée n'impose de seuil de croissance de marché ; toutes exigent un engagement
client avant de construire. On n'écrit rien de neuf : on branche des pièces existantes (licence MIT sauf mention).

| Porte | Ce qu'elle prouve | Pièce existante à reprendre | Source |
|-------|-------------------|-----------------------------|--------|
| 0. Accès | 20 clients nommés joignables par l'équipe | (profil `CLAUDE.md` rempli) | — |
| 1a. Modèle prouvé | le modèle encaisse déjà (France ou étranger) | filtre « modèle prouvé » : TrustMRR, CessionPME, Starter Story, critères Rocket Internet | veille, tableau 3 |
| 1b. Douleurs et argent visible | ≥ 3 prix publics ; douleurs citées ≥ 3 fils, top 3 sur ≥ 2 sources | agent `startup-painpoint-scout` (haiku, 10 tours, peu coûteux), adapté aux sources françaises ; F5Bot gratuit | github.com/vasilyu1983/AI-Agents-public, `agents/claude/startup-painpoint-scout.md` |
| 1c. Croyance la plus fragile | le risque qui tue la piste et le test qui le lève | skill `before-you-build` | github.com/wshobson/agents, `plugins/before-you-build/skills/before-you-build/SKILL.md` |
| 2. Engagement | 10 contacts en 1 semaine ; seuil écrit avant : ≥ 3 engagements d'argent ou ≥ 5 de temps [HYPOTHÈSE] | skills `mom-test` (déjà là), `interview-script`, `summarize-interview` | github.com/phuryn/pm-skills, dossier `pm-product-discovery/skills/` |
| 3. Taille | bottom-up avec les prix entendus en entretien | `market-sizing`, `beachhead-segment` (déjà là) ; faiblesses concurrents par `competitor-analysis`, `sentiment-analysis` | phuryn/pm-skills |
| 4. Confirmation | pilote payant, précommandes, seuils écrits avant | `brainstorm-experiments-new` (fake door, précommande, concierge) | phuryn/pm-skills |

À NE PAS copier : `voice-of-customer-miner` de deanpeters (licence non commerciale CC BY-NC-SA) : reprendre
l'idée (≥ 2 citations avec URL par thème) dans le prompt de l'agent, pas le fichier. Ignorer : GummySearch (fermé),
IdeaBrowser (payant, aucune preuve de paiement), outils Reddit open source (clés, code, Reddit restreint).

### Conséquences pour la recherche en cours
- Les phases 0-1 de la v3 ne sont pas jetées : `marches.md` et `segments.md` deviennent la **liste d'entrée**
  de la porte 1. Les 12 segments du Top 12 passent les portes 1 et 2 avant toute autre recherche documentaire.
- Les phases 2-4 du prompt maître v3 (idées, tournoi, conseil) ne s'appliquent qu'aux segments qui passent la porte 2.
