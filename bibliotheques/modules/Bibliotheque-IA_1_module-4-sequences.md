# Bibliothèque IA 1 — module « Séquences » — v1

Édition du 22 novembre 2026. Extrait généré automatiquement de la Bibliothèque IA 1 intégrale et de sections de la Bibliothèque IA 2 par le script outils/modules.py ; ne pas modifier ce fichier : modifier la bibliothèque intégrale, puis relancer le script. Auteur : Emmanuel Flaction, HEP Vaud (UER MI). Licence : CC BY-NC-SA 4.0. Ce référentiel n'est pas une publication officielle de la HEP Vaud.

> **Ce module** : composer une séquence : fonctions pédagogiques, correspondance avec les huit fonctions du guide, critères de l'écosystème, circulation et régulation.

> **Usage des modules (essai du 21.11.2026).** Joindre toujours le module « Noyau », puis le ou les modules de la tâche (par exemple Noyau + Jeux + Vérification et livraison pour un jeu imprimé). Le module « Code des recettes » ne sert qu'à un outil qui exécute du code Python. Les renvois (§, codes) visent la bibliothèque intégrale : une section absente de ce module se trouve dans un autre module. En cas de doute, ou si l'outil accepte les longs documents, joindre plutôt la Bibliothèque IA 1 intégrale. L'effet de ce découpage sur la fidélité des IA n'est pas encore mesuré.

# ÉTAPE 3 — CHOISIR : DE L'OBJECTIF AU GABARIT

## 3.5 Correspondances patron × gabarit × micro-format

| Patron pédagogique (Livre II, Partie 5) | Gabarits compatibles | Micro-formats compatibles | Gabarits de jeu (J) |
|---|---|---|---|
| P01 Défi initial | G6, G10 | MF01, MF06, MF21 | — |
| P02 Enquête par indices | G8, G9, G12 | MF04, MF05, MF19, MF24, MF54 | — |
| P03 Comparaison contrastée | G9, G12 | MF07, MF08, MF22, MF55 | J3 |
| P04 Erreur à débusquer | G4, G6, G1 | MF14, MF16, MF30, MF33 | — |
| P05 Choix argumenté | G6, G7 | MF11, MF20 | — |
| P06 Exemple guidé puis autonome | G3, G4, G9, G13 | MF13, MF14, MF15, MF57 | — |
| P07 Tri raisonné | G1, G12 | MF08, MF09, MF10 | J3 |
| P08 Associations à justifier | G2, G21 | MF17, MF18 | J2 |
| P09 Prédire, tester, expliquer | G3, G7, G10 | MF06, MF19, MF52, MF53 | — |
| P10 Cas à résoudre | G3, G7, G9 | MF04, MF24, MF49, MF50 | J5 |
| P11 Experts complémentaires | G7, G9 | MF26, MF27, MF29 | — |
| P12 Production sous contraintes | G7, G10 | MF23, MF29, MF56 | — |
| P13 Confrontation des solutions | G6, G7, G9 | MF07, MF25, MF30 | — |
| P14 Rappel actif progressif | G1, G3, G6 | MF17, MF18, MF32 | J1, J2, J4, J5 |
| P15 Ateliers différenciés | G1 à G25, G29 à G31 | MF13, MF15, MF36 | J1 à J6 |
| P16 Transfert de contexte | G7, G10 | MF15, MF34 | — |
| P17 Investigation critique des sources | G8, G9 | MF04, MF07, MF16, MF54 | — |
| P18 Retour sur sa démarche | G6, G7 | MF21, MF31-MF35, MF51, MF58 | — |
| P19 Rallye de postes | G1 à G25 | MF05, MF38, MF43 | J1 à J38 |
| P20 Apprivoiser un outil de référence | G6, G8 | MF04, MF05, MF12 | — |
| P21 Même tâche, plusieurs temps | G10, G15 | MF21, MF35, MF43 | — |
| P22 Les élèves conçoivent l'exercice | G18 | MF23, MF64, MF68 | J4 |
| P23 Du vécu corporel à la trace | G19 | MF38, MF42 | — |
| P24 La dictée réfléchie | G20 | MF33, MF45, MF75 | — |

**Colonne J** : correspondances proposées (inférence de conception), sauf P14 → J1, testé le 30.10.2026.

**P04 (erreur à débusquer)** : pleinement utilisable en mathématiques, en sciences et pour un raisonnement ou un fait ; en langue écrite, à partir de formes correctes ou des productions des élèves eux-mêmes, ou, sur décision de l'enseignant·e et dès la 5P, avec des formes fautives marquées et corrigées (exception encadrée du § 3.7).


# ANNEXE I-D — LISTE DES CODES DU LIVRE II (NOMS SEULEMENT)

## Fonctions pédagogiques (F01 à F43)

- F01 — Susciter l'intérêt et motiver
- F02 — Contextualiser et donner du sens
- F03 — Expliciter les objectifs et attentes
- F04 — Problématiser et lancer un défi
- F05 — Réactiver les acquis
- F06 — Faire émerger les représentations
- F07 — Diagnostiquer les acquis et besoins
- F08 — Informer et documenter
- F09 — Expliquer et faire comprendre
- F10 — Illustrer et exemplifier
- F11 — Démontrer et modéliser
- F12 — Faire observer et identifier
- F13 — Comparer, classer et organiser
- F14 — Structurer et institutionnaliser
- F15 — Questionner et formuler des hypothèses
- F16 — Rechercher et enquêter
- F17 — Manipuler et expérimenter
- F18 — Analyser et interpréter
- F19 — Confronter et exercer son esprit critique
- F20 — Donner des consignes
- F21 — Organiser et séquencer
- F22 — Guider et étayer
- F23 — Outiller et fournir des ressources d'aide
- F24 — Différencier et adapter
- F25 — Faciliter l'accessibilité
- F26 — Appliquer et mettre en pratique
- F27 — S'entraîner et développer la maîtrise
- F28 — Automatiser
- F29 — Mémoriser et consolider
- F30 — Résoudre des problèmes et prendre des décisions
- F31 — Produire, créer, exprimer
- F32 — Réinvestir, transférer et généraliser
- F33 — Échanger et argumenter
- F34 — Coopérer et coconstruire
- F35 — Communiquer et valoriser des productions
- F36 — Vérifier la compréhension
- F37 — Recueillir des traces d'apprentissage
- F38 — Fournir une rétroaction
- F39 — Favoriser l'autoévaluation
- F40 — Favoriser l'évaluation entre pairs
- F41 — Évaluer les acquis
- F42 — Réguler et remédier
- F43 — Développer la métacognition et l'autorégulation

## Correspondance avec les huit fonctions du guide (21.11.2026)

Le guide web propose huit fonctions simples pour composer une séquence. Correspondance proposée par l'auteur (inférence de conception) :

| Fonction du guide | Fonctions du Livre II |
|---|---|
| Présenter une information | F08, F09, F10, F14 |
| Faire s'exercer | F26, F27, F28, F29 |
| Enseigner pas à pas, avec un retour | F11, F21, F22, F36, F38 |
| Motiver par le jeu | F01, F04 (le plus souvent avec F27 ou F29) |
| Faire explorer | F15, F16, F19 |
| Faire manipuler et observer | F12, F17, F18 |
| Faire construire | F13, F30, F31 |
| Faire échanger entre élèves | F33, F34, F35, F40 |

Sans équivalent dans les huit : F02, F03, F05, F06, F07, F20, F23, F24, F25, F32, F37, F39, F41, F42, F43. Devant une séquence, l'IA traduit chaque fonction du guide en fonctions F, puis vérifie au regard de l'objectif celles qui manquent, notamment le diagnostic de départ (F07), les aides et la différenciation (F23, F24), les traces et la régulation (F37, F42), l'autoévaluation et la métacognition (F39, F43). Dans ce qu'elle écrit à l'enseignant·e, elle nomme les fonctions en toutes lettres, sans code.


# EXTRAITS DE LA BIBLIOTHÈQUE IA 2

# PARTIE 1 — RÉFÉRENTIEL DES FONCTIONS PÉDAGOGIQUES (F01 À F43)

La typologie suivante propose un vocabulaire opérationnel pour orienter les décisions de conception. Les fonctions ne sont pas exclusives : une ressource peut en associer plusieurs sans devoir toutes les mobiliser.

**Comment lire ce référentiel**

- Chaque fonction a un **code stable** (F01 à F43) pour y faire référence dans les patrons et les prompts.

- Une ressource mobilise typiquement **1 à 2 fonctions principales** et quelques fonctions secondaires.

- Certaines fonctions forment un **continuum** (F27 → F28).

- Certaines fonctions sont **complémentaires et souvent co-activées** (F13 et F18 par exemple).

---

## Famille A — Mobiliser et donner du sens

Fonctions qui engagent l'élève dans l'activité, suscitent son intérêt et donnent une raison d'apprendre.

| Code | Fonction | Intention |
|---|---|---|
| F01 | Susciter l'intérêt et motiver | Éveiller la curiosité, capter l'attention, engager. |
| F02 | Contextualiser et donner du sens | Relier les apprentissages à des expériences, usages ou situations concrètes. |
| F03 | Expliciter les objectifs et attentes | Clarifier les apprentissages visés et les critères de réussite. |
| F04 | Problématiser et lancer un défi | Faire émerger une question, une énigme ou un problème à résoudre. |

**Exemples d'objectifs mobilisant cette famille** : amorce d'une séquence sur l'eau (F02 + F04 : partir d'un vécu — une fuite à la maison — et poser une énigme — « d'où vient l'eau du robinet ? ») ; introduction à une œuvre d'art (F01 + F03 : capter par le ressenti, puis annoncer ce qu'on va apprendre à voir).

---

## Famille B — Activer et diagnostiquer

Fonctions qui mobilisent les acquis antérieurs, font émerger les représentations et identifient le point de départ de chaque élève.

| Code | Fonction | Intention |
|---|---|---|
| F05 | Réactiver les acquis | Mobiliser des connaissances et compétences antérieures. |
| F06 | Faire émerger les représentations | Faire expliciter les conceptions initiales, intuitions et croyances. |
| F07 | Diagnostiquer les acquis et besoins | Identifier prérequis, difficultés, lacunes et ressources des élèves. |

**Exemples** : rituel de début de séance (F05) ; brainstorm initial sur un sujet SHS (F06) ; mini-test diagnostique avant une nouvelle notion (F07).

---

## Famille C — Informer, expliquer et structurer

Fonctions qui transmettent, rendent intelligible et organisent le savoir.

| Code | Fonction | Intention |
|---|---|---|
| F08 | Informer et documenter | Apporter connaissances, données, faits et sources. |
| F09 | Expliquer et faire comprendre | Rendre intelligible un concept, un phénomène ou un mécanisme. |
| F10 | Illustrer et exemplifier | Fournir exemples, contre-exemples et analogies. |
| F11 | Démontrer et modéliser | Montrer un raisonnement, un geste ou une procédure. |
| F12 | Faire observer et identifier | Repérer caractéristiques, indices et régularités. |
| F13 | Comparer, classer et organiser | Distinguer, catégoriser, ordonner et mettre en relation. |
| F14 | Structurer et institutionnaliser | Synthétiser, formaliser et stabiliser les connaissances construites. |

**Note sur F13 et F18** : *Comparer/classer* (F13, famille C) et *Analyser/interpréter* (F18, famille D) sont souvent co-activées. Un tableau à double entrée qui compare deux textes mobilise les deux : classer les éléments (F13) et interpréter ce que la comparaison révèle (F18).

**Exemples** : fiche de synthèse de leçon (F14) ; capsule vidéo de modélisation d'une démarche de résolution (F11) ; tableau comparatif de deux poésies (F13).

---

## Famille D — Explorer, investiguer et exercer son jugement

Fonctions qui engagent l'élève dans une démarche active de recherche, d'expérimentation et de critique.

| Code | Fonction | Intention |
|---|---|---|
| F15 | Questionner et formuler des hypothèses | Susciter interrogations, anticipations et prédictions. |
| F16 | Rechercher et enquêter | Recueillir des informations, consulter des sources, investiguer. |
| F17 | Manipuler et expérimenter | Explorer par l'action, tester et observer les effets. |
| F18 | Analyser et interpréter | Traiter des informations, situations, données ou résultats. |
| F19 | Confronter et exercer son esprit critique | Examiner différentes interprétations, juger leur pertinence, questionner la fiabilité des sources. |

**Exemples** : compte-rendu d'expérience sur la flottaison (F15 + F17 + F18) ; enquête sur un métier (F16 + F18) ; comparaison critique de deux versions d'un événement historique (F19).

---

## Famille E — Guider et accompagner les apprentissages

Fonctions qui soutiennent la démarche de l'élève par des consignes, un étayage et une différenciation.

| Code | Fonction | Intention |
|---|---|---|
| F20 | Donner des consignes | Préciser la tâche, les règles, les contraintes et les attendus. |
| F21 | Organiser et séquencer | Décomposer une activité, organiser les étapes et la progression. |
| F22 | Guider et étayer | Proposer indices, questions intermédiaires et aides progressives. |
| F23 | Outiller et fournir des ressources d'aide | Mettre à disposition procédures, méthodes, référentiels, outils de consultation. |
| F24 | Différencier et adapter | Proposer variantes, niveaux, parcours, soutiens et approfondissements. |
| F25 | Faciliter l'accessibilité | Lever les obstacles de perception, compréhension, manipulation ou expression (UDL). |

**Rappel UDL** : F25 n'est pas une fonction qu'on « coche en plus » pour certains élèves. C'est un filtre transversal qui s'applique dès la conception de toute ressource.

**Exemples** : fiche de procédure (F20 + F21) ; aide-mémoire mathématique affiché en classe (F23) ; version avec glossaire pictographique pour élève allophone (F25 pensée dès la conception).

---

## Famille F — Exercer, consolider, produire et transférer

Fonctions qui permettent à l'élève de pratiquer, de produire et de mobiliser ses acquis dans des situations nouvelles.

| Code | Fonction | Intention |
|---|---|---|
| F26 | Appliquer et mettre en pratique | Utiliser des connaissances ou procédures dans une situation donnée. |
| F27 | S'entraîner et développer la maîtrise | Multiplier les occasions de pratique avec une progression adaptée. |
| F28 | Automatiser | Développer la fluidité, la rapidité et la fiabilité de certains acquis. |
| F29 | Mémoriser et consolider | Favoriser la récupération en mémoire, la révision et la rétention durable. |
| F30 | Résoudre des problèmes et prendre des décisions | Mobiliser des ressources, choisir et justifier une démarche. |
| F31 | Produire, créer, exprimer | Élaborer des réalisations, représentations, solutions, productions originales ou œuvres personnelles. |
| F32 | Réinvestir, transférer et généraliser | Mobiliser les acquis dans des situations nouvelles ou plus complexes. |

**Note sur F27 et F28** : *S'entraîner* (F27) et *Automatiser* (F28) forment un continuum. L'automatisation est le degré avancé de l'entraînement : fluidité, rapidité, fiabilité. Une même ressource peut couvrir F27 au début puis F28 en phase de consolidation.

**Note sur F31** : la fonction est élargie à *« exprimer »* pour couvrir les disciplines où la ressource ne vise pas une production tangible mais une expression personnelle (arts visuels, musique, EPS, production d'écrit créatif).

**Exemples** : fiche de calcul mental minute (F27 → F28) ; situation-problème contextualisée (F30 + F32) ; carnet de création en arts visuels (F31) ; répétition espacée de vocabulaire L2 (F29).

---

## Famille G — Interagir, collaborer et communiquer

Fonctions qui développent les capacités sociales et communicationnelles de l'élève.

| Code | Fonction | Intention |
|---|---|---|
| F33 | Échanger et argumenter | Expliciter ses idées, écouter, discuter, justifier. |
| F34 | Coopérer et coconstruire | Réaliser une tâche collective, négocier, construire ensemble. |
| F35 | Communiquer et valoriser des productions | Présenter, partager, expliquer ou diffuser les résultats d'un travail. |

**Exemples** : cercle de parole en philosophie pour enfants (F33) ; projet coopératif de création d'un journal de classe (F34 + F35) ; présentation orale d'un exposé devant la classe (F35).

---

## Famille H — Évaluer, réguler et développer la réflexivité

Fonctions qui recueillent des traces, donnent du feedback, évaluent les acquis et développent la métacognition.

| Code | Fonction | Intention |
|---|---|---|
| F36 | Vérifier la compréhension | Contrôler la compréhension immédiate, identifier des malentendus. |
| F37 | Recueillir des traces d'apprentissage | Rendre observables les démarches, acquis, progrès et difficultés. |
| F38 | Fournir une rétroaction | Informer sur les réussites, erreurs et pistes d'amélioration. |
| F39 | Favoriser l'autoévaluation | Permettre à l'élève de situer ses acquis à partir de critères. |
| F40 | Favoriser l'évaluation entre pairs | Faire observer, commenter et apprécier les productions d'autrui. |
| F41 | Évaluer les acquis | Mesurer ou apprécier les connaissances et compétences atteintes. |
| F42 | Réguler et remédier | Identifier les obstacles, corriger les erreurs, proposer des ajustements. |
| F43 | Développer la métacognition et l'autorégulation | Faire analyser ses stratégies, planifier son travail, suivre et ajuster ses apprentissages. |

**Note sur F43** : la fonction est dense. Trois sous-usages peuvent être distingués dans les patrons associés :

- *Planification* (avant la tâche : « comment vais-je m'y prendre ? »)

- *Monitoring* (pendant : « où en suis-je ? est-ce que ça marche ? »)

- *Bilan* (après : « qu'est-ce que j'ai appris sur ma façon d'apprendre ? »)

**Exemples** : grille d'autoévaluation feu tricolore (F39) ; carte de sortie avec une question clé (F36 + F37) ; mini-test formatif avec correction immédiate et piste de remédiation (F38 + F41 + F42) ; journal d'apprentissage (F43).

---


# PARTIE 10 — DÉPLOIEMENT PROGRESSIF ET RÉFÉRENCES

## Composer un écosystème de ressources

Cette section sert quand l'enseignant·e demande une séquence composée de plusieurs ressources reliées (rubrique « Composer une séquence » du guide), et non une ressource isolée.

**Définition de travail**

Un écosystème de ressources est un ensemble de ressources hétérogènes, choisies et articulées par l'enseignant·e autour d'un objectif d'apprentissage. Chaque ressource y remplit une fonction pédagogique distincte, et la valeur de l'ensemble tient davantage aux relations entre les ressources qu'à chacune prise isolément.

Statut : proposition de l'auteur, à valider. Le terme n'a pas de définition stabilisée dans la recherche en éducation. Il s'appuie sur deux notions établies : le système de ressources de l'enseignant·e (Trouche et al., 2020) et l'écologie d'apprentissage de l'élève (Barron, 2006). Le mot désigne ailleurs les plateformes et outils numériques d'une institution : ici, il s'agit des ressources d'une séquence, dans une classe.

**Cinq critères**

- Diversité fonctionnelle : l'ensemble couvre plusieurs fonctions, et non plusieurs ressources qui ne font que présenter.
- Complémentarité : chaque ressource fait ce que les autres ne font pas ; une redondance est acceptable si elle est voulue (même notion, deux modalités, pour différencier).
- Circulation : ce que produit une ressource alimente la suivante ; c'est le critère qui distingue un écosystème d'une collection.
- Régulation : l'enseignant·e ajuste l'ensemble d'après ce qu'il ou elle observe (retirer, remplacer, adapter).
- Ancrage : l'ensemble puise dans l'existant (moyens d'enseignement romands, médiathèque, banques de ressources), pas seulement dans ses propres productions.

**Huit fonctions proposées dans le guide**

Présenter une information ; faire s'exercer ; enseigner pas à pas, avec un retour ; motiver par le jeu ; faire explorer ; faire manipuler et observer ; faire construire ; faire échanger entre élèves. Ces fonctions sont adaptées de De Vries (2001), qui les a définies pour les logiciels d'apprentissage ; leur transposition aux ressources imprimées est une proposition. Pour une analyse plus fine, utiliser les fonctions F01 à F43 de la Partie 1, selon la correspondance suivante (proposition de l'auteur, 21.11.2026 ; inférence de conception) :

| Fonction du guide | Fonctions de la Partie 1 |
|---|---|
| Présenter une information | F08, F09, F10, F14 |
| Faire s'exercer | F26, F27, F28, F29 |
| Enseigner pas à pas, avec un retour | F11, F21, F22, F36, F38 |
| Motiver par le jeu | F01, F04 (le plus souvent avec F27 ou F29) |
| Faire explorer | F15, F16, F19 |
| Faire manipuler et observer | F12, F17, F18 |
| Faire construire | F13, F30, F31 |
| Faire échanger entre élèves | F33, F34, F35, F40 |

Les huit fonctions restent la porte d'entrée du guide ; elles ne couvrent pas F02, F03, F05, F06, F07, F20, F23, F24, F25, F32, F37, F39, F41, F42 et F43. L'IA traduit chaque fonction choisie en fonctions F, puis signale au regard de l'objectif celles qui manquent, en particulier le diagnostic de départ (F07), les aides et la différenciation (F23, F24), les traces et la régulation (F37, F42), l'autoévaluation et la métacognition (F39, F43). Elle les nomme en toutes lettres dans ce qu'elle écrit à l'enseignant·e.

**Conduite attendue de l'IA devant une demande de séquence**

- Montrer d'abord le plan d'ensemble : les ressources, la fonction de chacune, ce qui passe de l'une à l'autre ; attendre l'accord.
- Signaler toute redondance involontaire et toute fonction qui manque au regard de l'objectif.
- Ne pas produire les ressources que l'enseignant·e possède déjà : les intégrer au plan et s'y raccorder.
- Produire ensuite les ressources une à une ; chacune reprend ce que la précédente a produit (résultats, formulations des élèves, erreurs repérées).
- Rappeler que la régulation revient à l'enseignant·e : proposer ce qu'il ou elle peut observer, et ce qui peut être retiré ou remplacé.

**Où la métaphore trompe**

Un écosystème naturel n'est conçu par personne et se régule seul ; un ensemble de ressources est conçu et régulé par l'enseignant·e. « Système de ressources » est plus exact ; « écosystème » est plus parlant.

**Références de cette section**

Barron, B. (2006). Interest and self-sustained learning as catalysts of development: A learning ecology perspective. *Human Development*, 49, 193-224.

Trouche, L., Gueudet, G., Pepin, B., & Aldon, G. (2020). *L'approche documentaire du didactique*. https://hal.archives-ouvertes.fr/hal-02512596/file/DAD-TGP_Encyclopedie_Francais-v1.pdf

Statut : les huit fonctions de De Vries (2001) ont été vérifiées dans l'article le 21.11.2026 ; les références Barron (2006) et Trouche et al. (2020) sont reprises d'une note de l'auteur, sans nouvelle vérification ; la définition, les critères et la conduite attendue sont des propositions.

## Décider avant de demander, observer après la classe

Ces repères servent quand l'enseignant·e transforme ou crée une ressource. Ils complètent la procédure de conception (Partie 8) : l'IA s'y réfère pour rappeler ce qui n'a pas été décidé, sans décider à la place de l'enseignant·e.

**Les quatre temps d'une demande**

1. Pourquoi : l'intention propre à cette transformation, et le besoin qu'elle sert.
2. Ce que je décide : ce qui ne change pas (objectif, critères de réussite) et ce qui peut varier (guidage, quantité, complexité, contexte).
3. Ce que je demande : le contexte, la tâche précise, la forme attendue.
4. Ce que je contrôle : le risque propre à cette transformation (perdre l'objectif en simplifiant, souffler la réponse en aidant, décorer sans faire apprendre), si la transformation était nécessaire, et si l'IA l'était : une ressource existante convenait-elle ? Chaque demande consomme de l'énergie ; quelques échanges ciblés valent mieux qu'une série de régénérations.

Les deux premiers temps appartiennent à l'enseignant·e. L'IA peut les rendre explicites et poser une question si une information indispensable manque.

**Partir du problème, pas de la forme**

| Départ par la forme | Risque | Départ par le problème |
|---|---|---|
| Transformer en jeu | Amusant mais peu aligné | Les élèves s'engagent peu : quel défi ou quel rôle soutient l'activité ? |
| Rendre plus original | Surcharge, perte de lisibilité | La tâche est trop mécanique : comment provoquer justification et verbalisation ? |
| Numériser la fiche | Numérique sans valeur ajoutée | Besoin de retour rapide ou de collaboration : quel outil apporte une fonction utile ? |
| Ajouter des images | Décor sans aide à la compréhension | Un obstacle de compréhension appelle-t-il un schéma, un exemple ? |
| Créer un escape game | Activité lourde, parfois superficielle | Un besoin d'enquête ou de résolution progressive justifie-t-il ce format ? |

**Profondeur d'une transformation**

| Niveau | Type | Effet sur l'activité |
|---|---|---|
| 1. Surface | Mise en page, reformulation, clarification | Améliore la lisibilité, change peu la nature de la tâche |
| 2. Adaptation | Différenciation, aides progressives, version accessible | Répond à des besoins réels, soutient l'équité d'accès |
| 3. Outillage | Autocorrection, cartes d'aide, grilles, plan de travail | Modifie les conditions de travail, libère l'enseignant·e pour observer |
| 4. Socialisation | Tutorat, débat, correction croisée, production collective | Fait des interactions un levier d'apprentissage |
| 5. Reconfiguration | Fiche → enquête, exercice → situation-problème, réponse → production | Transforme la nature cognitive ou sociale de l'activité |
| 6. Dispositif | Parcours articulé (aides, autoévaluation, corrigés, ajustements) | Forte valeur, mais exige contrôle et faisabilité |

L'échelle décrit, elle ne hiérarchise pas : le bon niveau est celui qui répond au problème identifié, dans les contraintes de la classe.

**Après la classe : effet recherché, observations, traces**

| Effet recherché | Ce qu'on chercherait à observer | Traces envisageables |
|---|---|---|
| Engagement | Persévérance, implication dans les rôles ou les défis | Observation, productions terminées |
| Compréhension | Réponses mieux justifiées, capacité à expliquer | Billet de sortie, mini-quiz, explication orale |
| Autonomie | Moins de demandes d'aide immédiate, autocorrection pertinente | Traces d'autocorrection, tableau de suivi |
| Verbalisation | Échanges sur les stratégies, vocabulaire disciplinaire | Notes d'observation, critères de discussion |
| Différenciation effective | Tous les élèves entrent dans la tâche et progressent | Parcours réalisés, aides utilisées |
| Transfert | Usage de la notion dans une situation nouvelle | Tâche ouverte, production finale |
| Régulation | Obstacles repérés, ajustements pour la suite | Grille enseignant·e, erreurs-types |
| Mémorisation | Rappel correct après un délai, réutilisation spontanée | Mini-quiz différé, cartes de rappel, autotest |

Ces catégories orientent le regard ; elles se lisent au conditionnel (ce que l'on chercherait à observer) et ne prescrivent ni note ni mesure. L'IA peut proposer, dans la partie enseignant·e, l'effet visé, une observation et une trace ; elle ne présume jamais du résultat.

Statut : propositions de conception de l'auteur (22.11.2026), reprises de son travail sur la transformation des ressources ; sans référence propre dans cette section.
