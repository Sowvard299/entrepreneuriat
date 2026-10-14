# Copilote électricité pour PME : contre-analyse

Date : 2026-10-14. Verdict : **pas viable sous sa forme actuelle (abonnement logiciel pour toutes les PME de 10 à 250 salariés).** Score revu de 7,6 à 5,5.
Niveau de preuve : [Certain] = source vérifiée, [Likely] = déduction solide, [Guessing] = à vérifier.

## Ce qui contredit l'idée

1. **Le décret BACS ne joue pas avant 2030** [Certain]. Le seuil de 70 kW a été reporté du 1er janvier 2027 au 1er janvier 2030 (décret n° 2025-1343 du 26 décembre 2025). Et un logiciel qui lit le compteur ne remplace pas une gestion technique du bâtiment (GTB) : cette obligation profite à ceux qui vendent des GTB, pas à nous.
2. **Le mécanisme de capacité n'est pas une douleur chiffrée** [Likely]. L'ancien mécanisme coûtait environ 0,9 à 2 €/MWh ; Ekwateur estime que la réforme ne devrait pas faire monter la facture des professionnels. Pour une PME qui consomme 200 MWh par an, l'enjeu se compte en centaines d'euros.
3. **La fin de l'ARENH n'a pas créé de choc clair** [Likely]. Les sources ne s'accordent pas sur la hausse ; ce n'est pas la crise de 2022-2023.
4. **Les plus petites entreprises sont protégées** [Certain]. Depuis le 1er février 2025, les entreprises de moins de 10 salariés et de moins de 2 M€ de chiffre d'affaires ont accès au tarif réglementé, quelle que soit leur puissance.
5. **Le gain est ponctuel, l'abonnement est permanent** [Likely]. Une fois la puissance souscrite corrigée et le contrat renégocié, il ne reste plus grand-chose à optimiser : le client résilie. Les courtiers (Opera Énergie) proposent déjà l'optimisation du tarif d'acheminement (TURPE), payée par les fournisseurs, donc gratuite pour le client.
6. **La flexibilité des petits sites est déjà prise et peu rémunératrice** [Likely]. Flexcity revendique plus de 10 000 sites dès 2 kW ; un petit site rapporte peu par an.
7. **L'énergie pèse peu dans les charges d'une PME de bureau ou de commerce** [Guessing]. Hors période de crise, le dirigeant ne s'en occupe pas.
8. **Conflit avec EDF** [Likely]. L'obligation de loyauté pendant le contrat d'alternance et l'usage d'informations internes peuvent bloquer le projet. À vérifier avant tout.

## Ce qui conforte l'idée

1. **Les données existent** [Certain]. La courbe de charge à la demi-heure est disponible avec l'accord du client ; le produit est faisable techniquement.
2. **Les PME de 10 à 250 salariés sont mal servies** [Likely]. Courtiers (vente de contrat) d'un côté, éditeurs pour grands comptes de l'autre (Deepki, Advizeo, Energisme).
3. **La flexibilité est une priorité de l'État** [Certain]. La PPE 3 (février 2026) consacre la flexibilité de la demande ; la France vise près de 10 GW de flexibilité en 2030.
4. **Les dépassements coûtent vraiment** [Certain]. En tarif jaune (36 à 250 kVA), chaque heure de dépassement de la puissance souscrite est facturée (environ 12 € par heure selon Selectra).
5. **L'équipe connaît le métier de l'intérieur** grâce à l'alternance chez EDF.

## La version qui pourrait tenir

Cibler les **PME énergivores**, pour qui l'électricité est un gros poste : industrie agroalimentaire, entrepôts frigorifiques, boulangeries multi-sites, blanchisseries, plasturgie. Se faire payer **sur les économies réalisées ou par commission sur le contrat** (courtier équipé d'un logiciel), pas par abonnement. Ajouter la flexibilité ensuite, en partenariat avec un agrégateur.

Test avant de coder : 10 entretiens (skill `mom-test`) avec des dirigeants de PME énergivores. Questions clés : combien représente l'électricité dans vos charges ? Quand avez-vous renouvelé votre contrat la dernière fois, et comment ? Avez-vous déjà payé quelqu'un pour réduire votre facture ? Si moins de 3 sur 10 ont déjà payé pour ça, abandonner l'idée.

## Sources

- BACS reporté : [Banque des Territoires](https://www.banquedesterritoires.fr/batiments-tertiaires-le-calendrier-de-mise-en-oeuvre-des-systemes-dautomatisation-et-de-controle), [Projet Celsius](https://projetcelsius.com/blog/decret-tertiaire-bacs-obligations/)
- Mécanisme de capacité : [Ekwateur](https://ekwateur.fr/blog/marche-de-lenergie-pour-les-pros/mecanisme-capacite/), [Selectra](https://selectra.info/energie/actualites/marche/cout-mecanisme-capacite-2026-2027-facture), [Opera Énergie](https://opera-energie.com/media/reglementation-marches-energie-2026-changements/), [amendement parlementaire](https://www.assemblee-nationale.fr/dyn/17/amendements/0324A/AN/1961.pdf)
- Tarif réglementé pour les TPE : [Énergie-Info](https://www.energie-info.fr/pro/extension-des-tarifs-reglementes-delectricite-aux-tpe-et-petites-communes-le-1er-fevrier-2025/?pdf=2095)
- TURPE et dépassements : [Selectra](https://entreprises.selectra.info/energie/electricite/compteurs/puissance/depassement), [Opera Énergie](https://opera-energie.com/optimisation-du-turpe/)
- Fin de l'ARENH : [CCI Lyon Métropole](https://www.lyon-metropole.cci.fr/actualite/hausse-prix-electricite-la-fin-de-larenh-pour-les-entreprises)
- Flexibilité : [Voltalis et Siemens](https://press.siemens.com/fr/fr/communiquedepresse/siemens-et-voltalis-sallient-pour-accelerer-lacces-la-flexibilite-energetique), [baromètre RTE](https://assets.rte-france.com/prod/public/2026-04/2026-04-17-barometre-flexibilite-consommation-principaux-enseignements.pdf)
- Données de compteur : [Copeps](https://copeps.fr/actualites/compteur-pme-pmi-notice/)
