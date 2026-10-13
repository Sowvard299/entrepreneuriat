# Pré-mortem : « On est en 2028 et c'est un échec. Pourquoi ? »

**Phase:** 8, Validation
**Project:** recrutement-garages
**Date:** 2026-10-12
**Confidence:** Medium

---

Exercice : on se place en octobre 2028, l'entreprise a fermé. On écrit les 5 causes les plus probables, puis la parade qu'on met en place dès maintenant.

| # | Cause probable de l'échec | Signal d'alerte précoce | Parade |
|---|---------------------------|-------------------------|--------|
| 1 | **Les publicités n'ont pas amené de vrais candidats.** Beaucoup de clics, quelques curieux, presque aucun carrossier. Les garages ont payé 490 € pour rien, l'ont dit à la chambre de métiers, et le bouche-à-oreille s'est retourné contre nous. | Moins de 3 candidats présélectionnables par campagne sur les 3 pilotes ; coût par candidature au-dessus de 30 € [HYPOTHÈSE de seuil] | Ne jamais vendre plus de 3 pilotes avant d'avoir mesuré le résultat. Ouvrir chaque annonce aux reconversions et aux sortants de CFA. Garantie écrite : si moins de 3 candidats présélectionnés, la 2e campagne est offerte. Prévoir un plan B : relance des CFA, lycées professionnels et agences de France Travail de la zone. |
| 2 | **Personne n'a voulu payer d'avance.** Les patrons ont dit « c'est intéressant » puis sont restés sur France Travail et Leboncoin, gratuits. Les quelques clients payaient seulement à l'embauche, donc aucune trésorerie. | Moins de 3 signatures sur 15 propositions faites en fin d'entretien | Vendre un résultat chiffré (études de cas des pilotes : candidats, entretiens, embauche) plutôt qu'une prestation. Tester deux prix (490 € d'avance contre 0 € d'avance et 1 480 € à l'embauche) sur des garages différents. Viser d'abord les garages qui paient déjà (cabinet, renfort freelance). |
| 3 | **L'économie ne tenait pas.** Chaque campagne prenait 25 à 30 heures (trajets, tri des appels, entretiens annulés) pour moins de 900 € en moyenne. À 6, on gagnait moins que le SMIC horaire, et les membres sont partis vers des emplois salariés après le diplôme. | Plus de 20 heures par campagne mesurées sur les pilotes ; taux d'embauche inférieur à 30 % | Chronométrer chaque tâche dès le 1er pilote. Standardiser : script de tournage de 30 minutes, modèles de montage, questionnaire de présélection en ligne avant l'appel. Augmenter le prix vers les repères allemands si le résultat est là. Arrêter si le revenu par heure reste sous 30 € après 10 campagnes. |
| 4 | **On a fâché le marché local.** En servant plusieurs garages d'un même bassin, on a déplacé les mêmes carrossiers d'un atelier à l'autre ; deux clients se sont accusés de débauchage, et la chambre de métiers a pris ses distances. Les recrues reparties après 6 à 12 mois ont fait tomber les primes. | Plus de la moitié des candidats retenus sont déjà en poste dans un garage voisin ; départs pendant la période d'essai | Règle d'exclusivité : un seul client par métier et par bassin à la fois. Mesurer l'origine des candidats. Prime versée pour moitié en fin de période d'essai (le risque est partagé). Pousser les profils en reconversion et les apprentis. |
| 5 | **L'équipe s'est dispersée.** Pendant l'année, personne n'était disponible en semaine pour tourner et appeler ; après le diplôme, seuls deux membres sont restés ; aucune décision nette n'a été prise à temps, ni GO ni STOP. | Moins de 8 h par semaine réellement données par membre pendant 3 semaines ; pilotes reportés | Un responsable par fonction (vente, tournage, publicité, présélection, finances, juridique). Créneaux fixes. Critère GO / PIVOT / STOP écrit à l'avance et appliqué à la date prévue (voir [../07-terrain/go-pivot-stop.md](../07-terrain/go-pivot-stop.md)). Décider dès janvier 2027 qui passe à temps plein après le diplôme. |

Autres causes possibles, moins probables : suspension du compte publicitaire Meta (catégorie « emploi » mal déclarée) ; plainte pour discrimination à la présélection ; arrivée d'un acteur financé (job board automobile qui ajoute la vidéo) ; baisse continue des projets de recrutement (-10 à -15 % en un an).

---

## Flags

**Red Flags:**
- Causes 1 et 3 combinées (pas de candidats + trop d'heures) suffisent à tuer le projet ; elles se mesurent dès les 3 pilotes.

**Yellow Flags:**
- Cause 5 (dispersion de l'équipe) : risque classique d'un projet étudiant à 6.

## Sources
- [assumptions.md](assumptions.md), [../05-financial/revenue-model.md](../05-financial/revenue-model.md), [../../_recherche/phase4/B-audit-recrutement-artisans.md](../../_recherche/phase4/B-audit-recrutement-artisans.md).
