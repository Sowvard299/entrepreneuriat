# Kit de la porte 0 : 30 conversations dans vos réseaux (semaine 1)

But : trouver où de l'argent est déjà dépensé pour un problème pénible, chez des gens que vous pouvez joindre.
On ne présente **aucune idée**. On écoute des faits passés. Règles : skill `mom-test` ; script : skill
`interview-script` ; résumé : skill `summarize-interview` ; regroupement : skill `sentiment-analysis`.

## Qui appeler (5 par personne, 30 au total)

Chacun choisit 5 personnes **qui décident d'une dépense** dans leur travail ou leur foyer :
- au moins 2 dirigeants ou indépendants (artisan, commerçant, profession libérale, gérant de TPE/PME) ;
- au moins 1 personne qui achète pour une entreprise (achats, office manager, responsable d'agence) ;
- au plus 2 particuliers (parents, propriétaires, bailleurs, retraités) ;
- l'alternant EDF : 5 contacts côté clients TPE/PME, en dehors de tout cadre EDF et sans données de l'employeur.
Évitez les amis du même âge sans budget : leur avis ne coûte rien, donc ne prouve rien.

## Message d'approche (à adapter, jamais de pitch)

> Bonjour [prénom], je suis en fin de master et on étudie comment les [métier] gèrent leurs dépenses et leurs
> tâches les plus pénibles. Je ne vends rien. Auriez-vous 20 minutes cette semaine pour me raconter comment ça
> se passe chez vous ? Vos réponses restent anonymes.

## Script (20 minutes, faits passés uniquement)

1. Racontez-moi une semaine type. Qu'est-ce qui vous prend le plus de temps sans rien rapporter ?
2. La dernière fois que ça vous a vraiment agacé, que s'est-il passé ? Qu'avez-vous fait ensuite ?
3. Qu'avez-vous déjà essayé pour régler ça ? Combien ça vous a coûté (argent, heures) ?
4. Pour quoi payez-vous aujourd'hui un prestataire, un abonnement ou un logiciel ? Combien par mois ?
   Qu'est-ce qui vous déçoit chez lui ?
5. Avez-vous changé de prestataire ou de solution l'an dernier ? Pourquoi ?
6. Y a-t-il une obligation, une échéance ou un contrôle qui vous inquiète cette année ?
7. Qui d'autre devrais-je interroger ? (demander une mise en relation : c'est votre premier engagement)

Interdits : « Est-ce que vous utiliseriez… ? », « Combien paieriez-vous pour… ? », parler de votre idée.

## Après chaque conversation (10 minutes)

Remplir `entretiens/_modele.md` (copie nommée `AAAA-MM-JJ-<métier>-<prénom-interviewer>.md`). Noter les
**montants payés** et les **citations exactes**. Ne noter ni nom de famille ni coordonnées dans le dépôt.

## Ce que Claude fait ensuite (fin de semaine 1)

Prompt : « Lis les comptes rendus de ideas/_recherche-v4/entretiens/, résume-les avec summarize-interview,
regroupe douleurs et dépenses avec sentiment-analysis, puis classe les 6 pistes où (a) de l'argent est déjà
payé, (b) au moins 3 personnes citent la même douleur, (c) l'équipe peut joindre 20 clients. Ajoute la voie
distribution et les segments de la v3 comme pistes de comparaison. Écris ideas/_recherche-v4/pistes-porte0.md. »

## Seuil de la porte 0 (écrit avant les appels)

La semaine est réussie si : ≥ 25 conversations faites, ≥ 3 douleurs citées par au moins 3 personnes
différentes, et ≥ 2 de ces douleurs où quelqu'un paie déjà. Sinon : 15 conversations de plus, cibles élargies,
avant toute recherche documentaire.
