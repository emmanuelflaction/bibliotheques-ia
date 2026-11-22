# Bibliothèque IA 2 — pédagogique (à joindre à l'IA) — v1

Concevoir et transformer des ressources pédagogiques avec l'assistance de l'IA, de la 1P à la 11S (exemples situés surtout aux cycles 1 et 2) — Suisse romande.

Édition du 22 novembre 2026. Le nom du fichier (« _v1 ») reste stable pour ne pas casser les liens ; l'édition (sa date) identifie la version, la même pour les bibliothèques, le guide web et les modèles. Historique détaillé : fichier NOUVEAUTES.md du dépôt https://github.com/emmanuelflaction/bibliotheques-ia. Auteur : Emmanuel Flaction, HEP Vaud (UER MI) – emmanuel.flaction@hepl.ch. Licence : CC BY-NC-SA 4.0. Ce référentiel n'est pas une publication officielle de la HEP Vaud.

> **Les documents de l'ensemble.** Bibliothèque IA 1 — technique : contrat de production des ressources imprimées, appelé « Livre I » dans le texte. Bibliothèque IA 2 — pédagogique : référentiels de décision pédagogique, appelés « Livre II ». Bibliothèque IA 4 — personnelle : les préférences de l'enseignant·e, à remplir une fois (modèle .docx). Banque d'icônes : un fichier pour l'IA et les images. Le guide pour les enseignant·e·s est une page web (https://emmanuelflaction.github.io/bibliotheques-ia/) ; l'ancienne Bibliothèque IA 3 qui le contenait n'existe plus et son numéro n'est pas réattribué. Pour une ressource imprimée, la Bibliothèque 1 suffit : elle contient la liste des codes du Livre II (Annexe I-D). Joindre aussi la Bibliothèque 2 quand l'outil accepte les longs documents, ou pour une ressource non imprimée.

> **Format de ce fichier.** Version Markdown destinée aux IA (fichier à joindre ou à déposer dans un projet). Ce fichier contient le **Livre II seul** : fonctions pédagogiques, processus cognitifs, familles de ressources, patrons, micro-formats, règles de combinaison, procédure pour les ressources non imprimées, prompts, et l'Annexe II-A (Catalogue Ressources au primaire : 71 types de ressources, TR01 à TR71). Les tableaux et les blocs de code sont conservés tels quels.

# LIVRE II — RÉFÉRENTIELS DE DÉCISION PÉDAGOGIQUE

Ce livre reprend les Parties 1 à 10 de la version 5, sans modification de fond, complétées par l'Annexe II-A (Catalogue Ressources au primaire, mise à jour du 2 novembre 2026). Il sert à décider **quoi faire et pourquoi** : intention (fonctions), opération mentale (processus cognitifs), support (familles de ressources), organisation de l'activité (patrons) et briques d'engagement (micro-formats).

**Articulation avec le Livre I.** Pour toute ressource imprimée destinée aux élèves (fiches et jeux imprimés), la procédure applicable est celle du Livre I ; le présent livre est consulté à son Étape 3. Pour les ressources non imprimées, la procédure de la Partie 8 reste la référence.

## Finalité

Ce référentiel fournit à une intelligence artificielle le cadre structuré qui lui permet d'aider les enseignant·e·s à concevoir des ressources d'enseignement pertinentes, engageantes, diversifiées, éventuellement originales et réellement exploitables en classe.

Il est pensé pour être **joint directement aux prompts** adressés à une IA générative (Copilot, Claude, ChatGPT, Gemini ou tout autre outil équivalent) ou intégré comme instructions système d'un assistant personnalisé.

L'enseignant·e précise son besoin et son contexte ; l'IA sélectionne, combine et adapte des structures d'activité ; l'enseignant·e conserve la responsabilité du jugement professionnel et de la validation de la ressource.

---

## Posture et principes structurants

**Principe fondamental**

> ***Objectif d’apprentissage → indices de réussite attendus → fonction(s) pédagogique(s) → patron(s) → micro-format(s) → ressource → vérification et ajustement.***

Cette chaîne constitue le fil conducteur du référentiel. Les traces ou indices de réussite sont définis avant les formats afin de mieux aligner objectifs, activités et observation des apprentissages. Le support n’est sélectionné qu’après la clarification de la tâche.

La taxonomie de Bloom révisée, les modalités d'engagement cognitif, les principes d'accessibilité universelle et les cadres de l'évaluation formative constituent des **dimensions de contrôle transversales** à chaque étape.

**Trois éléments complémentaires**

| Élément | Rôle |
|---|---|
| Référentiel | Réunit les fonctions, patrons, micro-formats, règles de combinaison, exemples et critères de vérification. |
| Prompt de l'enseignant·e | Précise l'objectif, le public, la durée et les contraintes sans exiger la maîtrise préalable des formats. |
| Procédure de conception de l'IA | Analyse la demande, explore des solutions, choisit une organisation pédagogique, réalise et vérifie la ressource. |

**Vocabulaire stabilisé**

| Notion | Définition | Exemple |
|---|---|---|
| Fonction pédagogique | Finalité poursuivie par la ressource ou l'activité. | Faire comparer ; diagnostiquer ; consolider. |
| Patron pédagogique | Organisation d'activité réutilisable dans plusieurs contenus ou disciplines. | Enquête par indices ; confrontation de solutions. |
| Micro-format | Brique concrète d'activité, combinable avec d'autres. | Cartes d'indices ; tableau comparatif ; justification courte. |
| Support / livrable | Matérialisation finale accessible à l'enseignant·e et aux élèves. | Fiche, jeu de cartes, diaporama, oral, manipulation. |

Une même ressource peut remplir plusieurs fonctions. Un même micro-format peut soutenir des processus cognitifs différents selon la consigne, les contenus mobilisés et les connaissances antérieures des élèves.

Posture : concevoir l’accessibilité et préserver la possibilité d’adaptations individuelles

La conception universelle de l’apprentissage (CUA ; CAST, 2024) invite à anticiper les obstacles et à proposer, lorsque cela est utile, plusieurs moyens d’engagement, de représentation, d’action et d’expression. Elle vise l’accessibilité au plus grand nombre, sans dispenser des adaptations individuelles qui resteraient nécessaires. La différenciation reste complémentaire à cette conception anticipatrice.

Une image illustrative est celle d'une rampe d'accès : un aménagement conçu pour réduire un obstacle peut bénéficier à de nombreuses personnes, sans répondre à tous les besoins.

Appliqué à une ressource pédagogique, ce principe oriente dès la conception :

- des modalités de représentation et d’action pertinentes (texte, image, oral, geste, manipulation), lorsque leur combinaison sert l’objectif

- des consignes claires et lisibles pour toutes et tous ;

- des codes couleur non exclusifs, complétés par des textes, motifs ou formes lorsque la distinction est nécessaire

- un vocabulaire explicité, une structure stable, des repères visuels constants.

F25 – Faciliter l’accessibilité doit être envisagée comme un principe transversal, sans masquer les besoins spécifiques qui peuvent subsister

**Posture : les patrons sont des possibilités, pas des limitations**

Les patrons et micro-formats rassemblés ici sont des **points de départ**. Ils représentent les structures qui fonctionnent bien dans la plupart des cas. Toute situation d'enseignement peut appeler une structure différente, hybride ou inédite.

Les prompts fournis dans ce référentiel invitent systématiquement l'IA à proposer une alternative lorsqu'elle juge qu'une structure non répertoriée serait mieux adaptée. L'enseignant·e reste décideur·euse.

**Priorités générales**

- Donner la priorité à **l'alignement** entre objectifs, tâches proposées et indices d'apprentissage.

- Favoriser l'**engagement cognitif** réel, sans assimiler nouveauté, jeu et efficacité.

- Préserver l'**exactitude des contenus**, l'**accessibilité**, la **clarté** et la **faisabilité**.

- Chercher une **originalité utile** : renouveler l'expérience d'apprentissage sans compliquer inutilement le travail.

- Produire les éléments **complets** de la ressource, pas seulement des idées d'activités.

---

## Architecture générale du référentiel

| Partie | Contenu | Utilité principale |
|---|---|---|
| 1 | Référentiel des 43 fonctions pédagogiques (F01-F43) | Clarifier ce que la ressource doit permettre à l'élève. |
| 2 | 11 fonctions pour les ressources et le travail enseignant (E01–E11) | Couvrir les méta-ressources (planification, pilotage, communication). |
| 3 | Processus cognitifs de Bloom révisé et types de connaissances | Préciser les opérations mentales attendues et contrôler la pertinence didactique. |
| 4 | Panorama des 5 familles de supports et 2 dimensions transversales et 3 catégories transversales | Dépasser « ressource = fiche », couvrir tout l'écosystème pédagogique. |
| 5 | Bibliothèque de 24 patrons génériques (P01-P24) | Orienter la structure de l'activité. |
| 6 | Bibliothèque de 72 micro-formats en 10 familles (MF01-MF76) | Matérialiser les activités avec des briques réutilisables. |
| 7 | Règles d'originalité, de diversité et de combinaison | Éviter le choix mécanique de formats. |
| 8 | Procédure de conception en 7 étapes + grille de contrôle qualité + trames de contenu | Permettre une révision avant livraison. |
| 9 | Instructions d'assistant + prompts prêts à l'emploi | Rendre le référentiel immédiatement exploitable. |
| 10 | Déploiement, références, bibliographie APA | Documenter la portée scientifique et la mise en œuvre. |

**Choix éditorial** : conserver un niveau de description suffisant pour que les catégories guident réellement la conception. Des listes de noms seules ne suffisent pas ; les conditions de réussite, les points de vigilance et les contre-indications sont essentiels pour que l'IA et l'enseignant·e puissent arbitrer.

---

# PARTIE 1 — RÉFÉRENTIEL DES FONCTIONS PÉDAGOGIQUES (F01 À F43)
<!-- modules : sequences -->

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

# PARTIE 2 — FONCTIONS POUR LES RESSOURCES ET LE TRAVAIL DE L’ENSEIGNANT·E (E01 À E11)

Ces fonctions décrivent les usages de l’IA au service du travail de préparation, d’adaptation, d’analyse, de communication et de suivi de l’enseignant·e. Elles peuvent accompagner une ressource destinée aux élèves ou produire des méta-ressources autonomes.

| Code | Fonction | Finalité |
|---|---|---|
| E01 | Planifier | Concevoir une progression, une séance ou une séquence. |
| E02 | Piloter | Organiser le déroulement, les transitions, les groupes, le temps. |
| E03 | Observer | Identifier les éléments à relever dans l'activité des élèves. |
| E04 | Analyser | Interpréter les productions, difficultés et apprentissages. |
| E05 | Adapter | Préparer des variantes, différenciations et remédiations. |
| E06 | Communiquer et assurer le suivi | Transmettre des informations, conserver les traces, coordonner les interventions. |
| E07 | Renouveler et générer des variantes | Créer plusieurs versions équivalentes ou graduées sans dériver de l’objectif visé. |
| E08 | Transformer les modalités pédagogiques | Passer du papier à l’oral, à la manipulation, à la coopération ou au numérique selon l’objectif et les contraintes. |
| E09 | Créer des supports complémentaires | Produire aide-mémoire, consignes, corrigés, cartes, affiches, documents d’appui ou supports pour les familles. |
| E10 | Analyser et auditer une ressource | Repérer alignement, erreurs, charge cognitive, accessibilité, qualité des consignes et améliorations possibles. |
| E11 | Personnaliser avec discernement | Ajuster exemples, aides, progression ou modalités à partir de besoins pédagogiques décrits sans données identifiantes ni étiquetage des élèves. |

Exemples : trame de séquence alignée au PER (E01) ; grille d’observation d’ateliers (E03) ; message aux familles expliquant un dispositif (E06) ; banque d’erreurs typiques accompagnée de pistes de remédiation (E04 + E05).

---

Les fonctions E07 à E11 complètent le noyau initial : elles permettent de demander à l’IA non seulement de concevoir, mais aussi de renouveler, transformer, enrichir et examiner les ressources. La personnalisation porte sur des besoins d’apprentissage observables, et non sur des profils psychologiques supposés.

Note sur la distinction fonction / micro-format : E07 « Renouveler et générer des variantes » et MF46 « Variantes équivalentes d'une même tâche » décrivent le même geste à deux niveaux. E07 nomme l'intention de l'enseignant·e (le pourquoi) ; MF46 en désigne la brique concrète (le comment). On retrouve la même logique pour E08 « Transformer les modalités pédagogiques » et MF47 « Transposition de modalité ».

## Vérification des 16 usages attendus

Les 16 usages ci-dessous couvrent les attentes typiques formulées dans un descriptif de formation continue à l'usage pédagogique de l'IA au primaire. La table vérifie explicitement leur présence dans le référentiel et indique comment les mobiliser. Un usage peut être principal ou transversal ; il n'est pas nécessaire de l'activer pour chaque production.

| **N°** | **Usage** | **Repères** | **Instruction pour l’IA** |
|---|---|---|---|
| 01 | Correction et régulation | F36, F38, F42 · E04–E05 | Identifier l’erreur, expliquer la correction, proposer une nouvelle tâche ciblée et vérifier le progrès. |
| 02 | Différenciation pédagogique | F24 · P15 · E05 | Moduler guidage, difficulté, rythme, étendue ou soutien en maintenant l’objectif commun lorsque possible. |
| 03 | Inclusion et besoins particuliers (CUA/UDL) | F25 · E05, E11 | Anticiper les obstacles ; proposer des accès alternatifs et prévoir les ajustements individuels nécessaires. |
| 04 | Variantes et renouvellement | E07 · MF46 | Produire versions isomorphes, variations de contextes ou de supports sans fausser le niveau. |
| 05 | Explicitation et compréhension | F09–F11, F14 · P06 | Présenter exemples et contre-exemples, démontrer, guider puis faire reformuler ou expliquer. |
| 06 | Enrichissement métacognitif | F43 · P18 · MF31–MF35 | Faire planifier, surveiller et réviser une stratégie ; éviter les bilans vagues. |
| 07 | Évaluation formative et suivi | F36–F42 · E03–E04 · MF43–MF45 | Recueillir indices, interpréter, rétroagir, adapter l’enseignement et vérifier l’effet. |
| 08 | Motivation et gamification | F01, F04 · P01, P10 | Introduire défi, choix, fiction ou règles de jeu seulement si cela soutient l’apprentissage. |
| 09 | Transfert et interdisciplinarité | F32 · P16 | Changer de contexte, expliciter la connaissance transférée et nommer les liens disciplinaires pertinents. |
| 10 | Autonomie des élèves | F22, F23, F39, F43 | Outiller l’initiative, l’autocontrôle et le choix raisonné avec étayage dégressif. |
| 11 | Soutien à la préparation | E01–E05 | Produire planifications, déroulés, observations, corrigés et pistes d’adaptation. |
| 12 | Communication élèves et familles | E06, E09 · F35 | Rédiger bilans descriptifs, consignes et informations compréhensibles sans données sensibles. |
| 13 | Transformation des modalités | E08 · MF47 | Transposer une même intention vers oral, manipulation, jeu, collectif ou numérique. |
| 14 | Supports complémentaires | E09 | Créer affiches, synthèses, aides, corrigés, lexiques, cartes et variantes cohérentes. |
| 15 | Analyse pédagogique des ressources | E10 | Diagnostiquer forces, limites, erreurs, accessibilité et priorités de révision. |
| 16 | Personnalisation pédagogique | E11 · F24–F25 | Adapter à des besoins explicités, conserver des attentes ambitieuses et éviter toute inférence diagnostique. |

Distinction utile : différenciation = ajustements anticipés pour plusieurs besoins ; personnalisation = ajustements ciblés à partir d’informations pédagogiques pertinentes ; CUA/UDL = conception de départ visant la réduction des obstacles. Ces approches se complètent sans se confondre.

# PARTIE 3 — PROCESSUS COGNITIFS ET TYPES DE CONNAISSANCES

Les 43 fonctions disent **l'intention pédagogique**. La taxonomie révisée de Bloom (Anderson & Krathwohl, 2001) dit **l'opération mentale** que l'élève met en œuvre et **sur quel type de connaissances** elle porte. Les deux dimensions sont **complémentaires** et doivent être croisées pour contrôler la pertinence didactique d'une ressource.

## Les 6 processus cognitifs de Bloom révisé

| Processus | Opérations indicatives | Exemple de tâche élève |
|---|---|---|
| 1\. Mémoriser | Reconnaître, rappeler, restituer. | Réciter la table de 7. |
| 2\. Comprendre | Reformuler, interpréter, illustrer, classer, inférer, expliquer. | Expliquer avec ses mots le cycle de l'eau. |
| 3\. Appliquer | Exécuter, utiliser une procédure. | Résoudre un problème en utilisant une procédure connue. |
| 4\. Analyser | Différencier, organiser, mettre en relation, attribuer. | Décomposer un texte argumentatif. |
| 5\. Évaluer | Vérifier, juger, critiquer selon des critères. | Choisir la meilleure solution parmi trois, justifier. |
| 6\. Créer | Générer, planifier, produire. | Rédiger un récit original avec contraintes. |

## Les 4 types de connaissances

| Type | Exemples |
|---|---|
| Factuelles | Termes, données, définitions, éléments spécifiques. |
| Conceptuelles | Catégories, modèles, relations, principes et théories. |
| Procédurales | Méthodes, techniques, algorithmes et critères d'usage. |
| Métacognitives | Connaissance de ses stratégies, difficultés et modes d'apprentissage. |

**Correspondances typiques fonctions ↔ processus cognitifs**

Les processus **typiquement sollicités** par chaque famille de fonctions. Il ne s'agit pas d'une correspondance mécanique : une même fonction peut mobiliser différents processus selon le niveau de guidage et la complexité de la tâche.

| Famille | Processus cognitifs typiques |
|---|---|
| A. Mobiliser et donner du sens | Comprendre (saisir l'enjeu) |
| B. Activer et diagnostiquer | Mémoriser, Comprendre |
| C. Informer, expliquer, structurer | Comprendre, Analyser |
| D. Explorer, investiguer, exercer son jugement | Analyser, Évaluer, Créer |
| E. Guider et accompagner | (tous processus — fonction d'étayage) |
| F. Exercer, consolider, produire, transférer | Appliquer, Analyser, Créer |
| G. Interagir, collaborer, communiquer | Comprendre, Analyser, Évaluer, Créer |
| H. Évaluer, réguler, réfléchir | Évaluer, Analyser (métacognition : tous) |

**Point de vigilance majeur**

**Un verbe ne suffit pas à classer une tâche.** Sa complexité cognitive réelle dépend des contenus, de la consigne, des connaissances antérieures et du guidage proposé.

Une « analyse de texte » qui se résume à retrouver des informations littérales dans un texte court est en réalité un exercice de prélèvement (Comprendre au plus, souvent Mémoriser). Elle ne mobilise pas Analyser au sens strict.

**Le double regard fonction / processus cognitif est un contrôle qualité** : il permet de vérifier qu'une ressource active réellement l'opération mentale qu'elle prétend solliciter. Cette vérification est intégrée dans la procédure de conception (Partie 8) et dans la grille de contrôle qualité.

**Les six catégories ne constituent pas une progression obligatoire** à imposer à toutes les activités. Mémoriser et Comprendre ne sont pas « inférieurs » à Analyser et Créer ; ce sont des opérations différentes, mobilisées selon les besoins de l'apprentissage.

# PARTIE 4 — PANORAMA DES FAMILLES DE RESSOURCES

*Complément : l'Annexe II-A décrit les 71 types concrets de ressources du Catalogue Ressources au primaire (TR01 à TR71 ; TRnn = carte Rnn du catalogue), reconnaissables à leur structure, avec le verso de chaque carte (fonctions dominantes, conditions d'usage), leurs correspondances (classe, fonctions, patrons, micro-formats, gabarits) et des prompts d'image. Toute ressource imprimée destinée aux élèves, y compris les jeux de la Classe IV, se produit avec le Livre I (gabarits de jeu J1 à J6, § 3.8).*

**Au-delà de la fiche d'exercices**

Dans la pratique courante, le mot « ressource pédagogique » est spontanément réduit à la fiche photocopiée : un support écrit, individuel, papier, souvent centré sur l'exercice. Cette réduction appauvrit la réflexion didactique et masque l'immense éventail des supports mobilisables.

**Une ressource pédagogique est tout artefact — texte, image, son, objet, logiciel, environnement — mobilisé intentionnellement au service d'un apprentissage.** La fiche n'en est qu'un cas particulier.

Les patrons et micro-formats de ce référentiel portent surtout sur ce que l'IA peut aider à produire. Mais une ressource n'est pas qu'un artefact IA-générable. Les classes transversales mentionnées en fin de partie — matériel manipulable, dispositif humain, aménagement de l'espace, sorties — sont souvent les plus déterminantes au cycle 1, et précisément celles où l'IA apporte le moins. Les ignorer biaise la définition même de « ressource ».

## Les 5 familles de supports et 2 dimensions transversales

Les familles I à V décrivent principalement des supports ou environnements. Les rubriques VI et VII décrivent plutôt des dimensions transversales (accessibilité et évaluation), susceptibles de traverser toutes les familles. Le support se choisit après l’objectif et les indices de réussite.

Pour chaque classe, l'apport de l'IA est codé :

- **●** apport fort — création/modification largement déléguable

- **◐** apport partiel ou de niche — l'IA aide sur un sous-ensemble seulement

- **○** apport faible ou problématique — l'IA n'apporte pas, voire dégrade

**Classe I — Documents et supports écrits**

Fiches (découverte / théorique / guide / entraînement / synthèse / autoévaluation), affiches de référence, étiquettes et cartes-mots, cahiers thématiques, cartes mentales, manuels officiels CIIP, documents authentiques (notice, article, menu), infographies, BD pédagogiques, livres et albums, dossiers documentaires.

Fonctions typiquement servies : F08, F09, F10, F14, F23, F26, F27, F28, F29.

Apport IA : **●** pour la génération et l'adaptation ; vigilance sur la mise en page et le respect des standards graphiques.

**Classe II — Audiovisuel et médias**

Capsules vidéo pédagogiques (talking head, écran animé type Powtoon, écriture filmée, screencast, incrustation, cours dialogué), tutoriels vidéo, documentaires et extraits de films, podcasts et capsules audio, enregistrements langues 2 (dialogues, comptines, chansons), images et œuvres d'art, diaporamas projetés (Keynote, PowerPoint, Genially).

Fonctions typiquement servies : F01, F08, F09, F10, F11, F12, F27.

Apport IA : **◐** — script, storyboard, voix off TTS oui ; montage didactique et choix esthétiques, non.

**Classe III — Numérique interactif**

Exerciseurs en ligne (Gomaths, Ortholud, LogicielÉducatif), quiz gamifiés (Kahoot, Wooclap, Plickers, LearningApps, Blooket), flashcards à répétition espacée (Quizlet, Anki), activités interactives (H5P/Lumi, Genially), simulations (PhET, edumedia), micromondes (Scratch, GeoGebra), hypermédias et webquests, TBI et écrans tactiles, applications tutorielles adaptatives, réalité augmentée/virtuelle, robots programmables (Thymio, Beebot, micro:bit), IA générative, outils de création (traitement de texte, Canva).

Fonctions typiquement servies : F17, F26, F27, F28, F30, F36, F38, F41.

Apport IA : **●** pour les contenus (items, textes, images) ; **◐** pour le scénario d'interaction.

**Classe IV — Tangible et manipulable**

Jeux de cartes pédagogiques (memory évolutif, bataille de nombres, Dobble phonologique), jeux de plateau (parcours à contraintes, défis progressifs, plateau modulable), dominos pédagogiques (addition, lecture), dés pédagogiques (dé-conjugaison, dé-histoire), matériel de manipulation maths (réglettes Cuisenaire, base 10, jetons, abaques), matériel Montessori (lettres rugueuses, tour rose), solides géométriques, objets fabriqués en FabLearn (impression 3D, découpe laser : montres en bois, boîtes à compter, fidgets), escape games physiques, maquettes, kits scientifiques, cartes autocorrectives.

Fonctions typiquement servies : F01, F17, F26, F27, F30, F34.

Apport IA : variable. **●** pour la conception des contenus (règles, cartes, défis) ; **○** pour la fabrication physique ; nul pour la sensation tactile elle-même.

**Classe V — Environnements et banques**

Plateformes LMS (Moodle), banques romandes (BDPER / plandetudes.ch, friportail, educlasse, BDRP, RTS Découverte, EpRoCom/IRDP), banques francophones (Éduscol, Réseau Canopé/BRNE, La Digitale), murs collaboratifs (Padlet), portfolios numériques.

Fonctions typiquement servies : F23, F35, F37, E01, E06.

Apport IA : utile pour orienter dans ces banques, pas pour s'y substituer.

**Dimension transversale VI — Accessibilité et besoins particuliers**

Règles et guides de lecture, fidgets, versions adaptées (gros caractères, lecture facile, pictogrammes), outils d'aide technologique (synthèse vocale, correcteur, dictée vocale), formats alternatifs (audio, Braille, langue des signes).

Fonctions typiquement servies : F25 (filtre universel) + toute fonction mise en accessibilité.

Apport IA : **●** pour l'adaptation typographique, la simplification linguistique, la traduction, les versions audio.

**Dimension transversale VII — Évaluation côté élève**

Grilles d'autoévaluation (feu tricolore, smileys, critères gradués), quiz formatifs, sondages interactifs, carnets de bord, journaux d'apprentissage, portfolios de productions.

Fonctions typiquement servies : F36, F37, F39, F40, F41, F42, F43.

Apport IA : **●** pour la génération de critères, descripteurs par niveaux, questions de métacognition.

**Ressources non-artefactuelles complémentaires**

Les trois rubriques ci-dessous décrivent des ressources qui ne sont pas des artefacts générables par l'IA, mais qui demeurent constitutives de l'écosystème pédagogique. À distinguer des dimensions transversales VI (accessibilité) et VII (évaluation côté élève), qui qualifient toute ressource. Les mentionner évite le piège « ressource = artefact IA-générable ».

**Ressources humaines et sociales**

Dispositifs de tutorat entre élèves, ateliers coopératifs, intervenant·e·s extérieur·e·s, parents partenaires de certaines activités.

Fonctions typiquement servies : F22, F33, F34, F35.

Apport IA : nul pour le dispositif humain lui-même, utile en préparation (fiches de tutorat, chartes coopératives, briefings, communication aux parents).

**Aménagement de l'espace**

Coins thématiques (coin lecture, coin maths, coin sciences), ateliers rotatifs, affichage organisationnel, plans de classe.

Fonctions typiquement servies : F21, F22, F23, F25.

Apport IA : **◐** — l'IA aide à concevoir l'étiquetage, systémiser un coin, proposer un plan ; la sensation spatiale reste hors champ.

**Sorties, expériences hors classe, outdoor education**

Visites, musées, classes vertes, camps, école en plein air.

Fonctions typiquement servies : F01, F02, F16, F17, F31, F33.

Apport IA : **◐** — préparation (fiches-traces, questionnaires d'enquête), restitutions ; l'expérience elle-même reste hors champ.

**Les Axes de caractérisation complémentaires**

Au-delà de la classe de ressource, chaque ressource peut être caractérisée sur plusieurs axes croisés. Ces axes servent à affiner le choix et à éviter les choix par défaut.

| Axe | Valeurs (continuum) |
|---|---|
| Fonction pédagogique | parmi F01 à F43 |
| Processus cognitif | mémoriser · comprendre · appliquer · analyser · évaluer · créer |
| Support | tangible (papier, objet) · numérique · hybride |
| Modalité sensorielle | texte · image · oral/audio · geste · manipulation · multimodal, selon les contenus ; sans assigner de styles d’apprentissage aux élèves |
| Interactivité | statique · manipulable · interactif · adaptatif |
| Modalité sociale | individuel · duo · petit groupe · collectif |
| Destinataire | pour l'élève · pour l'enseignant·e (méta-ressource) |

Une fiche d’entraînement papier et un exerciseur en ligne peuvent partager une fonction d’entraînement (F27) tout en différant par le support, l’interactivité et les possibilités de rétroaction

---

# PARTIE 5 — BIBLIOTHÈQUE DE PATRONS PÉDAGOGIQUES (P01 À P24)

**Qu'est-ce qu'un patron pédagogique**

Un **patron pédagogique** est une **organisation d'activité réutilisable dans plusieurs contenus et plusieurs disciplines**. Contrairement à un type de document (fiche, affiche, jeu), un patron décrit **une structure d'engagement cognitif et didactique** indépendante du support.

Un patron est donc **transversal aux disciplines** : le patron « enquête par indices » peut servir en français (reconstituer qui a écrit une lettre), en sciences (identifier une cause à partir d'observations), en SHS (élucider les motifs d'un événement historique), en mathématiques (reconstituer le raisonnement caché derrière un résultat).

Les 24 patrons rassemblés constituent un **noyau opérationnel** que l'IA et l'enseignant·e peuvent sélectionner, combiner et adapter. Ils ne constituent pas une liste exhaustive. L'IA est explicitement invitée, dans chaque prompt, à proposer une structure différente si elle la juge mieux adaptée.

**Fiche-type standard d'un patron**

Chaque patron est documenté selon la structure suivante :

- **Identifiant stable et nom court**

- **Principe de fonctionnement** et valeur ajoutée pédagogique

- **Fonctions compatibles** (principales et secondaires parmi F01-F43)

- **Processus cognitifs** et **types de connaissances** susceptibles d'être mobilisés

- **Déroulement type**, durée indicative et modalités de travail

- **Micro-formats compatibles** et exemples de combinaisons

- **Conditions d'utilisation**, prérequis et points de vigilance

- **Variantes** et adaptations

- **Indices observables de réussite**

- **Contre-indications** : situations où ce patron serait moins pertinent

**Catalogue des 24 patrons**

### P01 — Le défi initial

**Principe** : entrer dans un apprentissage par une question intrigante, une énigme, un phénomène inattendu, une situation surprenante. L'élève se trouve embarqué·e dans une recherche avant d'avoir reçu l'exposition formelle de la notion.

**Fonctions compatibles** : F01 Susciter l'intérêt ; F04 Problématiser ; F06 Faire émerger les représentations.

**Secondaires** : F15 Formuler des hypothèses.

**Processus cognitifs** : Comprendre, Analyser (saisir l'enjeu, formuler une hypothèse).

**Types de connaissances** : conceptuelles principalement.

**Déroulement type**

1\. Présenter le défi (image intrigante, phénomène étonnant, situation réelle).

2\. Laisser émerger les hypothèses des élèves.

3\. Noter la diversité des réponses sans trancher immédiatement.

4\. Annoncer que l'apprentissage à venir permettra de trancher.

**Durée** : 5 à 15 minutes.

**Modalité** : collectif ou duo.

**Micro-formats compatibles** : image à annoter ; informations progressivement dévoilées ; prédiction à vérifier.

**Conditions / variantes** : fonctionne mieux si le défi touche à un intérêt réel ou crée une dissonance cognitive. Variantes : situation-problème (maths), fait divers (SHS), objet mystère (sciences).

**Indices de réussite** : les élèves formulent spontanément des hypothèses, demandent à poursuivre.

**Contre-indication** : à éviter pour une pure consolidation ou une évaluation certificative.

---

### P02 — L'enquête par indices

**Principe** : examiner progressivement des informations pour résoudre une question. L'élève reçoit (ou cherche) des indices qu'il doit interpréter, croiser et confronter pour parvenir à une réponse justifiée.

**Fonctions compatibles** : F16 Rechercher ; F18 Analyser ; F19 Esprit critique.

**Secondaires** : F02 Contextualiser ; F15 Formuler des hypothèses.

**Processus cognitifs** : Analyser, Évaluer.

**Types de connaissances** : conceptuelles, procédurales (méthode d'enquête).

**Déroulement type**

1\. Poser la question d'enquête.

2\. Mettre à disposition (ou faire chercher) les indices.

3\. L'élève note ce qu'il observe, infère, exclut.

4\. Formulation d'une conclusion argumentée.

5\. Confrontation collective.

**Durée** : 30 à 60 minutes.

**Modalité** : individuel ou petit groupe.

**Micro-formats compatibles** : document avec indices à relever ; tableau de confrontation ; conclusion argumentée ; carnet d'enquête.

**Conditions / variantes** : les indices doivent être réellement interprétables (ni évidence directe, ni devinette impossible). Variantes : enquête historique, enquête scientifique, enquête littéraire.

**Indices de réussite** : l'élève justifie sa conclusion en nommant les indices qu'il a mobilisés.

**Contre-indication** : à éviter si les élèves n'ont pas les prérequis pour interpréter les indices (sinon l'enquête tourne à l'arbitraire).

---

### P03 — La comparaison contrastée

**Principe** : comparer deux ou plusieurs exemples, procédures, situations ou productions pour en dégager des propriétés, des différences, des régularités. La comparaison force l'identification de ce qui est essentiel vs accessoire.

**Fonctions compatibles** : F13 Comparer, classer ; F18 Analyser ; F09 Faire comprendre.

**Secondaires** : F10 Illustrer (par contre-exemples) ; F14 Structurer (ce que la comparaison révèle).

**Processus cognitifs** : Analyser, Évaluer.

**Types de connaissances** : conceptuelles (propriétés, principes).

**Déroulement type**

1\. Présentation des éléments à comparer (2 à 4, pas plus pour cycle 1-2).

2\. Identification des critères de comparaison (donnés ou à construire).

3\. Remplissage d'un tableau comparatif.

4\. Formulation des conclusions.

**Durée** : 20 à 40 minutes.

**Modalité** : individuel ou duo.

**Micro-formats compatibles** : tableau à double entrée ; éléments à comparer ; exemples et contre-exemples à distinguer ; conclusion argumentée.

**Conditions / variantes** : les éléments doivent être réellement comparables (même nature, différences significatives). Variantes : comparer deux textes, deux procédures de calcul, deux versions d'un événement, deux productions d'élèves.

**Indices de réussite** : l'élève nomme explicitement les différences et formule ce qu'elles permettent de comprendre.

**Contre-indication** : à éviter si les éléments sont trop proches (différences invisibles) ou trop éloignés (comparaison artificielle).

---

### P04 — L'erreur à débusquer

*Restriction (v6.1, règle MP-CC-11 du Livre I) : par défaut, un support destiné à l'élève ne montre aucune forme écrite fautive ou inexistante. En langue écrite, ce patron s'applique à partir de formes correctes (justifier, comparer, choisir la règle) ou des productions des élèves eux-mêmes ; sur décision de l'enseignant·e, dès la 5P et pour une notion déjà enseignée, il peut aussi montrer des formes fautives marquées comme erreurs, corrigées et justifiées, une seule fois chacune (exception encadrée du Livre I, § 3.7, décision du 21.11.2026) ; il reste pleinement utilisable en mathématiques, en sciences et pour un raisonnement ou un fait.*

**Principe** : présenter une réponse ou une démarche comportant une erreur plausible. L'élève la repère, explique son origine ou sa nature, et propose une correction justifiée. Travaille la posture critique et renverse la dynamique habituelle.

**Fonctions compatibles** : F07 Diagnostiquer ; F18 Analyser ; F38 Fournir une rétroaction ; F42 Réguler.

**Secondaires** : F19 Esprit critique ; F14 Structurer (reformuler la règle).

**Processus cognitifs** : Comprendre, Appliquer, Analyser ou Évaluer selon la consigne.

**Types de connaissances** : procédurales (ce qui a été mal fait), conceptuelles (pourquoi c'est une erreur).

**Déroulement type**

1\. Découvrir la production.

2\. Examiner sa validité.

3\. Localiser et expliquer l'erreur.

4\. Corriger.

5\. Formaliser une règle ou un critère.

**Durée** : 15 à 30 minutes.

**Modalité** : individuel ou duo.

**Micro-formats compatibles** : annotation d'erreur ; comparaison de solutions ; vrai/faux justifié ; correction commentée ; diagnostic court.

**Conditions / variantes** : l'erreur doit être significative (révéler un vrai malentendu) et plausible (que les élèves pourraient faire). Variantes : erreur dans une rédaction, un calcul, un raisonnement, une affirmation médiatique, une réponse fictive d'IA.

**Indices de réussite** : l'élève caractérise l'erreur, justifie son diagnostic, produit une correction adéquate.

**Contre-indication** : éviter les pièges artificiels, les erreurs trop grossières ou purement typographiques.

---

### P05 — Le choix argumenté

**Principe** : proposer plusieurs solutions, procédures ou interprétations possibles. L'élève choisit la plus adaptée et justifie son choix. Travaille le raisonnement et le discernement.

**Fonctions compatibles** : F30 Résoudre et décider ; F19 Esprit critique ; F18 Analyser.

**Secondaires** : F33 Argumenter.

**Processus cognitifs** : Évaluer (juger selon des critères).

**Types de connaissances** : conceptuelles, procédurales, parfois métacognitives.

**Déroulement type**

1\. Présentation de la situation et des options.

2\. Analyse des options (points forts, points faibles).

3\. Choix personnel.

4\. Justification écrite ou orale.

5\. Confrontation collective.

**Durée** : 15 à 30 minutes.

**Modalité** : individuel puis collectif.

**Micro-formats compatibles** : choix entre solutions ; argument à compléter ; classement à défendre ; affirmation à justifier.

**Conditions / variantes** : les options doivent être réellement défendables (pas d'option évidente ni d'option absurde). Variantes : choix de méthode mathématique, choix d'une fin pour un récit, choix d'un angle pour une enquête.

**Indices de réussite** : l'élève justifie son choix en mobilisant des critères explicites.

**Contre-indication** : à éviter quand une seule bonne réponse existe réellement (le patron devient une devinette).

---

### P06 — L'exemple guidé puis autonome

**Principe** : observer une résolution entièrement commentée (exemple travaillé), compléter progressivement les étapes manquantes, puis réussir seul·e une tâche analogue. Patron central pour l'apprentissage de procédures complexes.

**Fonctions compatibles** : F11 Démontrer, modéliser ; F22 Guider et étayer ; F26 Appliquer ; F27 S'entraîner.

**Secondaires** : F10 Illustrer ; F23 Outiller.

**Processus cognitifs** : Comprendre puis Appliquer.

**Types de connaissances** : procédurales.

**Déroulement type**

1\. Observation de l'exemple entièrement résolu, avec commentaires explicites.

2\. Résolution d'un exemple partiellement complété (étapes manquantes).

3\. Résolution autonome d'une tâche analogue.

4\. Vérification et retour si nécessaire.

**Durée** : 30 à 45 minutes.

**Modalité** : individuel.

**Micro-formats compatibles** : procédure partiellement complétée ; exercice à difficulté progressive ; comparaison avant/après.

**Conditions / variantes** : l'exemple doit être représentatif, les commentaires explicites. La transition entre guidage et autonomie doit être progressive. Variantes : worked example pur, fading (effacement progressif des aides), modeling vidéo.

**Indices de réussite** : l'élève réussit la tâche autonome en nommant les étapes.

**Contre-indication** : à éviter en phase d'évaluation certificative, ou si les élèves maîtrisent déjà la procédure (effet d'inversion de l'expertise).

---

### P07 — Le tri raisonné

**Principe** : classer des éléments selon des critères — soit donnés, soit à identifier, soit à expliciter. Travaille la catégorisation, la hiérarchisation et la justification des choix.

**Fonctions compatibles** : F13 Comparer, classer ; F12 Observer ; F18 Analyser.

**Secondaires** : F14 Structurer.

**Processus cognitifs** : Analyser (différencier, organiser).

**Types de connaissances** : conceptuelles.

**Déroulement type**

1\. Présentation des éléments à trier (cartes, images, mots, phrases).

2\. Identification ou formulation du critère.

3\. Tri effectif.

4\. Justification des choix.

**Durée** : 15 à 30 minutes.

**Modalité** : individuel, duo ou petit groupe.

**Micro-formats compatibles** : classement multicritère ; tableau à compléter ; cartes à associer.

**Conditions / variantes** : les éléments doivent permettre un tri non trivial. Variantes : tri sans critère donné (l'élève construit sa catégorisation), tri avec critère caché (à retrouver), tri par couches (plusieurs critères successifs).

**Indices de réussite** : l'élève justifie son tri par le ou les critères mobilisés.

**Contre-indication** : à éviter si tous les éléments relèvent manifestement d'une seule catégorie.

---

### P08 — Les associations à justifier

**Principe** : associer des éléments entre eux (concepts et exemples, images et mots, questions et réponses, arguments et conclusions) en justifiant brièvement chaque association.

**Fonctions compatibles** : F13 Comparer, classer ; F26 Appliquer ; F29 Mémoriser.

**Secondaires** : F18 Analyser.

**Processus cognitifs** : Comprendre, Appliquer.

**Types de connaissances** : factuelles, conceptuelles.

**Déroulement type**

1\. Présentation de deux ensembles à associer.

2\. Association effective (relier, numéroter, placer).

3\. Justification orale ou écrite de chaque association.

**Durée** : 10 à 25 minutes.

**Modalité** : individuel ou duo.

**Micro-formats compatibles** : cartes à associer ; appariement avec distracteurs ; schéma à légender.

**Conditions / variantes** : prévoir des distracteurs pour éviter l'association mécanique par élimination. Variantes : avec un seul distracteur, avec plusieurs, avec associations multiples (un élément peut s'associer à plusieurs).

**Indices de réussite** : l'élève justifie au moins une association non triviale.

**Contre-indication** : à éviter si les associations relèvent de la pure mémorisation sans compréhension.

---

### P09 — Prédire, tester, expliquer

**Principe** : formuler une hypothèse, l'éprouver par une manipulation ou une observation, interpréter les résultats et éventuellement réviser l'hypothèse. Patron central pour les sciences et toute démarche d'investigation.

**Fonctions compatibles** : F15 Formuler des hypothèses ; F17 Manipuler, expérimenter ; F18 Analyser.

**Secondaires** : F19 Esprit critique ; F43 Métacognition.

**Processus cognitifs** : Analyser, Évaluer, Créer (dans la formulation de l'hypothèse).

**Types de connaissances** : conceptuelles, procédurales (démarche expérimentale).

**Déroulement type**

1\. Formulation d'une hypothèse (« Je pense que… parce que… »).

2\. Mise en œuvre d'un test (manipulation, observation, calcul).

3\. Confrontation hypothèse / résultat.

4\. Interprétation et éventuelle révision.

**Durée** : 45 à 90 minutes.

**Modalité** : individuel ou duo.

**Micro-formats compatibles** : prédiction à vérifier ; carnet d'expérience ; comparaison avant/après ; conclusion argumentée.

**Conditions / variantes** : matériel réel à prévoir si expérimentation. Veiller à ce que l'élève écrive son hypothèse *avant* le test. Variantes : expérimentation physique, manipulation numérique (simulation), prédiction mathématique.

**Indices de réussite** : l'élève confronte explicitement son hypothèse initiale au résultat.

**Contre-indication** : à éviter si l'issue de l'expérience est connue par les élèves (pas de réelle anticipation).

---

### P10 — Le cas à résoudre

**Principe** : analyser une situation concrète comportant un problème ou une décision à prendre. L'élève mobilise des ressources pour comprendre, décider et argumenter.

**Fonctions compatibles** : F30 Résoudre et décider ; F18 Analyser ; F02 Contextualiser.

**Secondaires** : F32 Transférer.

**Processus cognitifs** : Analyser, Évaluer, Créer.

**Types de connaissances** : procédurales, conceptuelles.

**Déroulement type**

1\. Lecture du cas (situation réelle ou plausible).

2\. Identification des enjeux et données utiles.

3\. Formulation d'une démarche.

4\. Résolution ou décision.

5\. Justification.

**Durée** : 30 à 60 minutes.

**Modalité** : individuel ou duo.

**Micro-formats compatibles** : document avec indices à relever ; tableau de données ; argument à compléter ; conclusion argumentée.

**Conditions / variantes** : le cas doit être réellement contextualisé (pas un énoncé mathématique habillé). Variantes : cas mathématique, cas littéraire, cas citoyenneté, cas écologique.

**Indices de réussite** : l'élève mobilise les données utiles et justifie sa démarche.

**Contre-indication** : à éviter si le cas est trop simple (devient un exercice d'application pure) ou trop complexe (bloque l'entrée dans la tâche).

---

### P11 — Les experts complémentaires

**Principe** : chaque groupe d'élèves (ou chaque élève) détient une partie des informations ou une spécialité. La résolution exige la mise en commun. Travaille l'interdépendance positive et la coopération.

**Fonctions compatibles** : F34 Coopérer, coconstruire ; F16 Rechercher ; F35 Communiquer.

**Secondaires** : F18 Analyser ; F33 Argumenter.

**Processus cognitifs** : Comprendre, Analyser, Créer.

**Types de connaissances** : conceptuelles, procédurales.

**Déroulement type**

1\. Formation de « groupes experts » (chacun étudie une partie).

2\. Travail dans le groupe expert.

3\. Reconfiguration en « groupes de synthèse » (un expert de chaque spécialité).

4\. Mise en commun et production collective.

**Durée** : 60 à 90 minutes.

**Modalité** : collectif structuré en petits groupes (type Jigsaw).

**Micro-formats compatibles** : fiche expert ; grille de restitution ; production collaborative.

**Conditions / variantes** : chaque partie doit être réellement différente et nécessaire. Variantes : parties disciplinaires (chaque groupe un auteur / un pays / une période), parties procédurales (chaque groupe une méthode à présenter).

**Indices de réussite** : la synthèse finale mobilise réellement les contributions de chaque expert.

**Contre-indication** : à éviter avec des groupes trop jeunes (cycle 1 début) où la coordination est trop coûteuse, ou si une seule des parties suffit en pratique.

---

### P12 — La production sous contraintes

**Principe** : concevoir une réponse, un objet, un texte, une image qui respecte plusieurs contraintes explicites. Les contraintes stimulent la créativité et évitent la paralysie face à une consigne trop ouverte.

**Fonctions compatibles** : F31 Produire, créer, exprimer ; F30 Résoudre ; F26 Appliquer.

**Secondaires** : F32 Transférer ; F34 Coopérer (si collectif).

**Processus cognitifs** : Créer (générer, planifier, produire).

**Types de connaissances** : conceptuelles, procédurales.

**Déroulement type**

1\. Énoncé de la production attendue.

2\. Énoncé des contraintes (3 à 6 contraintes claires et vérifiables).

3\. Phase de production.

4\. Vérification du respect des contraintes.

5\. Partage éventuel.

**Durée** : 30 à 60 minutes.

**Modalité** : individuel, duo ou groupe.

**Micro-formats compatibles** : défi de production ; checklist de contraintes ; critères d'autoévaluation ; comparaison avant/après.

**Conditions / variantes** : les contraintes doivent être explicites, vérifiables et de nature différente (pas 5 contraintes de longueur). Variantes : écriture sous contraintes (Oulipo), construction géométrique sous contraintes, invention d'un jeu avec contraintes de règles.

**Indices de réussite** : la production respecte les contraintes et manifeste une recherche personnelle.

**Contre-indication** : à éviter si les contraintes sont tellement nombreuses qu'elles bloquent la production.

---

### P13 — La confrontation des solutions

**Principe** : plusieurs élèves ou groupes produisent une solution à un même problème, puis confrontent leurs démarches. Fait apparaître la pluralité des chemins et la fécondité des erreurs.

**Fonctions compatibles** : F33 Échanger, argumenter ; F18 Analyser ; F42 Réguler.

**Secondaires** : F19 Esprit critique ; F43 Métacognition.

**Processus cognitifs** : Analyser, Évaluer.

**Types de connaissances** : procédurales, métacognitives.

**Déroulement type**

1\. Résolution individuelle ou par petits groupes.

2\. Présentation des démarches par 2 ou 3 solutions choisies.

3\. Analyse collective (ce qui fonctionne, ce qui bloque, ce qui est élégant).

4\. Formulation d'un apprentissage sur les démarches.

**Durée** : 45 à 60 minutes.

**Modalité** : individuel puis collectif.

**Micro-formats compatibles** : tableau de confrontation ; annotation de productions ; justification courte.

**Conditions / variantes** : prévoir au moins deux démarches réellement différentes à confronter. Variantes : avec démarches réelles d'élèves, avec démarches fictives préparées par l'enseignant·e, avec démarches générées par l'IA à analyser.

**Indices de réussite** : les élèves nomment ce que les différentes démarches ont de spécifique.

**Contre-indication** : à éviter si une seule démarche efficace est enseignée et attendue.

---

### P14 — Le rappel actif progressif

**Principe** : retrouver des acquis **sans consultation immédiate**, puis obtenir une rétroaction. Fondé sur les effets scientifiquement établis du testing effect et du spacing effect.

**Fonctions compatibles** : F29 Mémoriser, consolider ; F27 S'entraîner ; F36 Vérifier la compréhension.

**Secondaires** : F38 Fournir une rétroaction.

**Processus cognitifs** : Mémoriser, Comprendre, Appliquer.

**Types de connaissances** : factuelles, conceptuelles, procédurales.

**Déroulement type**

1\. L'élève tente de récupérer en mémoire ce qu'il sait (sans regarder ses notes).

2\. Il écrit, dit ou coche sa réponse.

3\. Il consulte le corrigé ou la source pour vérifier.

4\. Il repère ce qu'il a oublié et refait l'exercice un peu plus tard (répétition espacée).

**Durée** : 10 à 20 minutes par séance, répété dans le temps.

**Modalité** : individuel.

**Micro-formats compatibles** : cartes de rappel ; mini-test de récupération ; appariement avec distracteurs.

**Conditions / variantes** : la rétroaction doit être rapide et claire. Variantes : flashcards (Quizlet, Anki), quiz auto-corrigé, test oral entre pairs.

**Indices de réussite** : l'élève améliore ses taux de récupération au fil des séances.

**Contre-indication** : à éviter si les connaissances n'ont pas encore été initialement enseignées et comprises.

---

### P15 — Les ateliers différenciés

**Principe** : proposer plusieurs parcours, tâches ou niveaux adaptés à différents besoins, se déroulant en parallèle ou en rotation. Permet de personnaliser l'étayage et le défi.

**Fonctions compatibles** : F24 Différencier ; F22 Guider ; F25 Faciliter l'accessibilité.

**Secondaires** : F21 Organiser ; F27 S'entraîner.

**Processus cognitifs** : (tous selon les ateliers).

**Types de connaissances** : (toutes selon les ateliers).

**Déroulement type**

1\. Diagnostic initial (ou choix libre).

2\. Répartition en ateliers (par niveau, par modalité, par intérêt).

3\. Travail en atelier (chacun à son rythme).

4\. Mise en commun ou travail enseignant·e avec un sous-groupe.

**Durée** : 45 à 90 minutes.

**Modalité** : individuel, duo ou petit groupe par atelier.

**Micro-formats compatibles** : exercice à difficulté progressive ; situation d'application variée ; procédure partiellement complétée ; cartes de rappel.

**Conditions / variantes** : les ateliers doivent être réellement différenciés (pas seulement « plus facile / plus difficile »). Variantes : différenciation par le contenu, par le processus, par la production, par l'environnement.

**Indices de réussite** : chaque élève travaille à un niveau de défi adapté.

**Contre-indication** : à éviter si on ne dispose pas d'un diagnostic préalable ou d'une connaissance suffisante des élèves.

**Variante v7.2 — atelier autocorrectif autonome** (BDRP-G5) : la vérification est portée par le matériel (cartes à pince J10, roues J11, plateaux G12-b, feuille de route GF-G), selon MP-J-04 étendu.

---

### P16 — Le transfert de contexte

**Principe** : réutiliser un acquis dans une situation nouvelle, d'une autre discipline ou d'un contexte différent. Vérifie que l'apprentissage n'est pas limité au contexte initial.

**Fonctions compatibles** : F32 Réinvestir, transférer ; F30 Résoudre ; F02 Contextualiser.

**Secondaires** : F26 Appliquer.

**Processus cognitifs** : Analyser, Appliquer, Créer.

**Types de connaissances** : procédurales, conceptuelles.

**Déroulement type**

1\. Rappel bref de la notion ou procédure apprise.

2\. Présentation du nouveau contexte.

3\. Mise en relation (en quoi la notion s'applique ici).

4\. Résolution.

**Durée** : 20 à 40 minutes.

**Modalité** : individuel.

**Micro-formats compatibles** : situation d'application variée ; cas à transférer ; question de transfert.

**Conditions / variantes** : le nouveau contexte doit être suffisamment différent pour tester le transfert, suffisamment proche pour que le transfert reste faisable. Variantes : transfert disciplinaire (maths → sciences), transfert contextuel (classe → quotidien), transfert d'échelle.

**Indices de réussite** : l'élève identifie la notion applicable et l'utilise correctement.

**Contre-indication** : à éviter trop tôt dans l'apprentissage (le transfert est une opération coûteuse qui suppose une maîtrise initiale).

---

### P17 — L'investigation critique des sources

**Principe** : apprécier la fiabilité, la pertinence et les limites d'informations ou de sources. Patron central pour l'éducation aux médias et à l'IA.

**Fonctions compatibles** : F19 Esprit critique ; F16 Rechercher ; F18 Analyser.

**Secondaires** : F43 Métacognition.

**Processus cognitifs** : Analyser, Évaluer.

**Types de connaissances** : conceptuelles (ce qu'est une source fiable), procédurales (comment vérifier), métacognitives.

**Déroulement type**

1\. Présentation de plusieurs sources (ou productions) sur un même sujet.

2\. Analyse des sources (qui parle, pour qui, avec quelle intention, avec quelles preuves).

3\. Confrontation des contenus.

4\. Formulation d'un jugement argumenté.

**Durée** : 45 à 60 minutes.

**Modalité** : individuel ou duo.

**Micro-formats compatibles** : document avec indices à relever ; tableau de confrontation ; grille d'analyse de source ; conclusion argumentée.

**Conditions / variantes** : prévoir des sources de fiabilité réellement contrastée. Variantes : analyse d'une image de presse, comparaison de deux articles, confrontation d'une production humaine et d'une production IA.

**Indices de réussite** : l'élève justifie son jugement en mobilisant des critères explicites.

**Contre-indication** : à éviter si les élèves n'ont pas les prérequis thématiques pour juger du contenu (sinon le jugement devient formel).

---

### P18 — Le retour sur sa démarche

**Principe** : examiner après coup ses stratégies, ses décisions, ses difficultés et les possibilités d'amélioration. Patron central pour le développement de la métacognition.

**Fonctions compatibles** : F43 Métacognition, autorégulation ; F39 Autoévaluation ; F42 Réguler.

**Secondaires** : F33 Argumenter (si collectif).

**Processus cognitifs** : Analyser, Évaluer (sur sa propre démarche).

**Types de connaissances** : métacognitives.

**Déroulement type**

1\. Rappel de la tâche réalisée.

2\. Analyse des choix opérés (« pourquoi j'ai fait ça ? »).

3\. Identification des difficultés (« qu'est-ce qui a été dur ? »).

4\. Formulation d'un apprentissage (« que ferai-je différemment ? »).

**Durée** : 10 à 20 minutes.

**Modalité** : individuel, parfois en duo.

**Micro-formats compatibles** : autoévaluation critériée ; bilan d'erreur ; échelle de confiance ; question de transfert.

**Conditions / variantes** : les questions doivent inviter à nommer des stratégies précises, pas à produire des généralités (« j'ai bien travaillé »). Variantes : trois sous-usages — planification (avant), monitoring (pendant), bilan (après).

**Indices de réussite** : l'élève nomme une stratégie précise qu'il mobilisera à l'avenir.

**Contre-indication** : à éviter si l'élève n'a pas eu l'occasion de prendre des décisions dans la tâche (une procédure imposée pas à pas offre peu de prise à la métacognition).

### P19 — Le rallye de postes

**Principe** : tous les élèves parcourent tous les postes d'un même thème, avec un document par poste, sur une ou plusieurs séances. Il se distingue de P15, où les ateliers se choisissent ou se différencient.

**Fonctions compatibles** : F17 Manipuler, expérimenter ; F21 Organiser ; F27 S'entraîner.

**Secondaires** : F34 Coopérer.

**Processus cognitifs** : Comprendre, Appliquer.

**Types de connaissances** : factuelles, procédurales.

**Déroulement type**

1\. Présentation du parcours et de la fiche de suivi.

2\. Passage à chaque poste, avec consigne compréhensible sans l'enseignant·e.

3\. Trace à chaque poste.

4\. Mise en commun de ce qui a été découvert.

**Durée** : une à trois séances.

**Modalité** : petits groupes en rotation.

**Micro-formats compatibles** : tableau de suivi de progrès ; observation guidée ; séquence gestuelle ou motrice.

**Conditions / variantes** : prévoir un poste de réserve pour absorber les écarts de temps.

**Indices de réussite** : chaque élève a laissé une trace à chaque poste.

**Contre-indication** : à éviter si les postes dépendent l'un de l'autre dans un ordre strict.

*Origine : BDRP-G1. Durée et déroulement : inférence de conception.*

### P20 — Apprivoiser un outil de référence

**Principe** : des questions servent de prétexte pour faire chercher dans un aide-mémoire, un sous-main ou un glossaire. Le but est l'usage de l'outil, pas la réponse.

**Fonctions compatibles** : F23 Outiller ; F22 Guider.

**Secondaires** : F16 Rechercher.

**Processus cognitifs** : Appliquer.

**Types de connaissances** : procédurales.

**Déroulement type**

1\. Présentation de l'outil et de sa structure.

2\. Questions dont la réponse se trouve dans l'outil.

3\. Mise en commun des chemins de recherche.

4\. Renvoi à l'outil pendant les tâches suivantes.

**Durée** : 15 à 25 minutes.

**Modalité** : individuel ou duo.

**Micro-formats compatibles** : observation guidée ; document avec indices à relever ; fiche-synthèse structurée.

**Conditions / variantes** : à reprendre à chaque nouvel outil, puis à espacer.

**Indices de réussite** : l'élève retrouve seul·e une information dans l'outil.

**Contre-indication** : inutile si l'outil n'est pas utilisé ensuite.

*Origine : BDRP-G2. Durée et déroulement : inférence de conception.*

### P21 — Même tâche, plusieurs temps

**Principe** : une tâche identique revient à intervalles réguliers pour rendre le progrès visible par l'élève et les familles (évaluation ipsative).

**Fonctions compatibles** : F37 Recueillir des traces ; F43 Métacognition.

**Secondaires** : F35 Communiquer.

**Processus cognitifs** : Se rappeler, Évaluer.

**Types de connaissances** : procédurales, métacognitives.

**Déroulement type**

1\. Première réalisation datée.

2\. Rangement de la trace.

3\. Reprise de la même tâche après plusieurs semaines.

4\. Comparaison avec ses traces antérieures.

**Durée** : quelques minutes à chaque reprise, sur l'année.

**Modalité** : individuel.

**Micro-formats compatibles** : carnet d'apprentissage ; comparaison avant / après ; tableau de suivi de progrès.

**Conditions / variantes** : gabarit vierge seulement avec l'IA : aucune production nominative n'est transmise (nLPD).

**Indices de réussite** : l'élève nomme un progrès observé entre deux traces.

**Contre-indication** : à éviter comme comparaison entre élèves.

*Origine : BDRP-G3. Durée et déroulement : inférence de conception.*

### P22 — Les élèves conçoivent l'exercice

**Principe** : les élèves inventent une tâche destinée à d'autres, ce qui les oblige à maîtriser la notion et à prévoir la réponse.

**Fonctions compatibles** : F31 Produire ; F35 Communiquer.

**Secondaires** : F36 Vérifier la compréhension.

**Processus cognitifs** : Créer, Évaluer.

**Types de connaissances** : conceptuelles, procédurales.

**Déroulement type**

1\. Analyse d'un modèle de tâche.

2\. Conception d'une tâche avec son corrigé.

3\. Essai par une autre personne.

4\. Révision.

**Durée** : 30 à 45 minutes.

**Modalité** : duo.

**Micro-formats compatibles** : rubrique « pour mes camarades » ; message codé autovalidant ; défi de production.

**Conditions / variantes** : l'enseignant·e relit tout ce qui circule : aucune forme fautive ne doit être vue par les autres élèves (MP-CC-11).

**Indices de réussite** : la tâche produite vise bien la notion et son corrigé est juste.

**Contre-indication** : à éviter sur une notion encore fragile.

*Origine : BDRP-G4. Durée et déroulement : inférence de conception.*

### P23 — Du vécu corporel à la trace

**Principe** : un parcours vécu avec le corps est observé, puis reproduit, et reparaît plus tard sous forme de trace sur papier.

**Fonctions compatibles** : F17 Manipuler, expérimenter ; F14 Structurer.

**Secondaires** : F12 Observer.

**Processus cognitifs** : Appliquer, Comprendre.

**Types de connaissances** : procédurales.

**Déroulement type**

1\. Parcours tracé au sol et parcouru.

2\. Observation et reproduction.

3\. Reprise après deux à trois semaines sur une fiche du même parcours.

4\. Verbalisation du trajet.

**Durée** : plusieurs séances réparties sur quelques semaines.

**Modalité** : collectif, puis individuel.

**Micro-formats compatibles** : parcours spatial ou manipulation située ; séquence gestuelle ou motrice.

**Conditions / variantes** : l'IA ne produit que la trace finale (G19) ; la ressource n'existe que par la séquence vécue.

**Indices de réussite** : l'élève décrit ou suit le parcours sur papier.

**Contre-indication** : à éviter si le parcours vécu n'a pas eu lieu.

*Origine : BDRP-G6. Durée et déroulement : inférence de conception.*

### P24 — La dictée réfléchie

**Principe** : un texte court cible une ou deux notions ; la dictée sert à raisonner sur l'orthographe plutôt qu'à la contrôler : formes à trous, à choix ou négociées à plusieurs.

**Fonctions compatibles** : F27 S'entraîner ; F33 Argumenter ; F38 Rétroaction.

**Secondaires** : F42 Réguler.

**Processus cognitifs** : Appliquer, Analyser.

**Types de connaissances** : procédurales, conceptuelles.

**Déroulement type**

1\. Annonce des notions ciblées.

2\. Dictée sous une des trois formes (G20).

3\. Justification ou négociation des choix.

4\. Correction expliquée.

5\. Reprise sur un texte proche.

**Durée** : 20 à 30 minutes.

**Modalité** : individuel, puis duo ou trio.

**Micro-formats compatibles** : dictée réfléchie ; bilan d'erreur ; boucle rétroaction–révision–nouvel essai.

**Conditions / variantes** : le texte reste dans la partie enseignant·e ; aucune forme fautive n'est imprimée (MP-CC-11).

**Indices de réussite** : l'élève justifie une graphie par une règle ou une analogie.

**Contre-indication** : à éviter comme note unique d'orthographe.

*Origine : verso de la carte TR70 ; BDRP-I3. Durée et déroulement : inférence de conception.*

---

---

**Vue d'ensemble des 24 patrons par famille de fonctions**

Tableau de compatibilité patrons × familles de fonctions. Un patron peut servir plusieurs familles ; le tableau indique les familles principales.

| Patron | A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|---|
| P01 Défi initial | ● | ○ | · | ● | · | · | · | · |
| P02 Enquête par indices | · | · | · | ● | · | · | · | · |
| P03 Comparaison contrastée | · | · | ● | ● | · | · | · | · |
| P04 Erreur à débusquer | · | ● | · | ● | · | · | · | ● |
| P05 Choix argumenté | · | · | · | ● | · | ● | ● | ● |
| P06 Exemple guidé puis autonome | · | · | ● | · | ● | ● | · | · |
| P07 Tri raisonné | · | · | ● | ● | · | · | · | · |
| P08 Associations à justifier | · | · | ● | · | · | ● | · | · |
| P09 Prédire, tester, expliquer | · | · | · | ● | · | · | · | ● |
| P10 Cas à résoudre | · | · | · | ● | · | ● | · | · |
| P11 Experts complémentaires | · | · | · | ● | · | · | ● | · |
| P12 Production sous contraintes | · | · | · | · | · | ● | · | · |
| P13 Confrontation des solutions | · | · | · | ● | · | · | ● | ● |
| P14 Rappel actif progressif | · | · | · | · | · | ● | · | ● |
| P15 Ateliers différenciés | · | · | · | · | ● | ● | · | · |
| P16 Transfert de contexte | · | · | · | · | · | ● | · | · |
| P17 Investigation critique des sources | · | · | · | ● | · | · | · | ● |
| P18 Retour sur sa démarche | · | · | · | · | · | · | · | ● |
| P19 Rallye de postes | · | · | · | ● | ● | ● | · | · |
| P20 Apprivoiser un outil de référence | · | · | · | · | ● | · | · | · |
| P21 Même tâche, plusieurs temps | · | · | · | · | · | · | · | ● |
| P22 Les élèves conçoivent l'exercice | · | · | · | · | · | ● | ● | · |
| P23 Du vécu corporel à la trace | · | · | ● | ● | · | · | · | · |
| P24 La dictée réfléchie | · | · | · | · | · | ● | ● | ● |

● = famille principalement servie, · = secondaire ou possible selon la mise en œuvre.

# PARTIE 6 — BIBLIOTHÈQUE DE MICRO-FORMATS (MF01 À MF76)

**Qu'est-ce qu'un micro-format**

Un **micro-format** est une **brique d'activité élémentaire**, courte, autonome, reconnaissable, qui s'insère dans un patron et dans un support. Là où le patron décrit l'architecture d'une activité, le micro-format décrit la **forme concrète que prend un item individuel**.

Un patron « Comparaison contrastée » (P03) peut être servi par un ou plusieurs micro-formats : *tableau à double entrée*, *exemples et contre-exemples*, *appariement avec distracteurs*…

Les 72 micro-formats du référentiel sont regroupés en dix familles complémentaires, couvrant également les pratiques orales, corporelles et manipulatoires. Ils constituent des briques adaptables et combinables, sans quota d’utilisation.

**Principe de non-limitation** : ces formats sont des **ressources éprouvées**, non des contraintes. L'IA est invitée dans chaque prompt à en proposer d'autres si elle en identifie de mieux adaptés.

**Fiche-type standard d'un micro-format**

Pour chaque micro-format, le référentiel précise :

- **Nom** et **famille** d'appartenance

- **Description** et **engagement cognitif** typique

- **Patrons compatibles** (sélection des plus fréquents)

- **Fonctions typiquement servies**

- **Points de vigilance** et conditions d'efficacité

- **Variantes** et déclinaisons

## Famille 1 — Micro-formats de perception et de représentation

Supports pour entrer dans la tâche, observer, se représenter mentalement une situation ou un objet.

### MF01 — Image à annoter

Image, schéma ou photo sur laquelle l'élève pose des légendes, des flèches, des commentaires ou des questions.

Patrons : P01, P02, P09, P12.

Fonctions : F12, F06, F15.

Vigilance : laisser des espaces suffisants ; prévoir une légende guide pour les élèves non lecteurs/éviter la saturation visuelle.

### MF02 — Schéma à compléter

Représentation partielle (schéma scientifique, carte, plan, diagramme) dont certains éléments doivent être retrouvés et placés.

Patrons : P03, P07, P16.

Fonctions : F08, F14, F26.

Vigilance : équilibrer éléments donnés et éléments à compléter.

Variante v7.2 — **gabarit vide d'un outil de référence** (BDRP-F14) : version vide d'une affiche, à compléter par l'élève (SP6).

### MF03 — Carte mentale ou carte conceptuelle à enrichir

Carte avec concept central et branches partielles à compléter avec exemples, propriétés, relations.

Patrons : P03, P07, P14.

Fonctions : F14, F29, F43.

Vigilance : rester à 2 ou 3 niveaux de hiérarchie au primaire ; différencier mots-clés et liens.

### MF04 — Document avec indices à relever

Texte, image, document source dans lequel l'élève doit identifier et surligner des éléments précis.

Patrons : P02, P10, P17.

Fonctions : F16, F18, F19.

Vigilance : indices distinguables sans être évidents.

### MF05 — Observation guidée

Grille d'observation avec critères précis à cocher ou à annoter devant un objet, une image ou une vidéo.

Patrons : P02, P09, P17.

Fonctions : F12, F17, F43.

Vigilance : nombre de critères limité (4 à 7) pour maintenir l'attention.

### MF06 — Prédiction à vérifier

Case « Je prédis que… » suivie, après manipulation ou lecture, de « J'ai observé que… ».

Patrons : P01, P09.

Fonctions : F15, F17, F43.

Vigilance : la prédiction doit être écrite *avant* le test ; prévoir espace pour la révision éventuelle.

## Famille 2 — Micro-formats de structuration

Supports pour organiser, hiérarchiser, catégoriser.

### MF07 — Tableau à double entrée

Grille croisant deux dimensions, à remplir, compléter ou analyser.

Patrons : P03, P07, P13, P17.

Fonctions : F13, F14, F18.

Vigilance : titres de lignes et colonnes explicites ; ne pas dépasser 6×6 au primaire.

### MF08 — Classement multicritère

Éléments à ranger selon un ou plusieurs critères donnés ou à identifier.

Patrons : P07, P03.

Fonctions : F13, F18.

Vigilance : prévoir une case « autre » pour les éléments ambigus.

### MF09 — Frise ou ligne du temps

Dispositif linéaire chronologique ou séquentiel à compléter, enrichir ou interpréter.

Patrons : P03, P07, P16.

Fonctions : F02, F14, F29.

Vigilance : échelle proportionnée aux événements.

### MF10 — Carte à légender

Carte géographique, plan ou représentation spatiale sur laquelle placer des éléments nommés.

Patrons : P02, P07, P16.

Fonctions : F02, F14, F29.

Vigilance : symboles cohérents ; légende claire.

### MF11 — Arbre de décision

Suite de choix binaires ou ternaires menant à une conclusion.

Patrons : P05, P07, P10.

Fonctions : F30, F18, F42.

Vigilance : chaque branche doit mener à une conclusion claire.

### MF12 — Fiche-synthèse structurée

Document court avec rubriques fixes (titre, essentiel, exemple, à retenir) à produire ou à compléter.

Patrons : P03, P18.

Fonctions : F14, F29, F32.

Vigilance : rubriques régulières pour favoriser la mémorisation.

## Famille 3 — Micro-formats d'application et d'entraînement

Supports pour mobiliser ce qu'on sait, s'entraîner, consolider.

Variante v7.2 — **référent de graphème à quatre entrées** (BDRP-F11) : geste, graphème, mot-repère, image. La méthode gestuelle n'a pas été identifiée : à vérifier avant usage.

### MF13 — Exercice à difficulté progressive

Suite de 3 à 6 items du plus simple au plus complexe, parfois par paliers.

Patrons : P06, P15, P14.

Fonctions : F27, F28, F24.

Vigilance : la progression doit être réelle, pas cosmétique.

### MF14 — Procédure partiellement complétée

Résolution déjà commencée dont il faut compléter certaines étapes.

Patrons : P06, P04.

Fonctions : F11, F22, F26.

Vigilance : variété des étapes manquantes (début, milieu, fin).

### MF15 — Situation d'application variée

Mêmes notion ou procédure appliquées à plusieurs contextes différents.

Patrons : P16, P15.

Fonctions : F27, F32, F26.

Vigilance : la variation doit tester la robustesse de l'apprentissage.

### MF16 — Vrai / faux justifié

*Restriction (v6.1, règle MP-CC-11 du Livre I) : par défaut, un support destiné à l'élève ne montre aucune forme écrite fautive ou inexistante (seule exception : l'analyse d'erreurs encadrée du Livre I, § 3.7). Une affirmation fausse porte sur le sens, un fait ou une règle, jamais sur une forme mal orthographiée.*

Affirmations à juger, avec justification obligatoire quand la réponse est « faux ».

Patrons : P04, P17.

Fonctions : F18, F19, F36.

Vigilance : affirmations plausibles ; interdire le simple cochage sans justification.

### MF17 — Appariement avec distracteurs

*Restriction (v6.1, règle MP-CC-11 du Livre I) : par défaut, un support destiné à l'élève ne montre aucune forme écrite fautive ou inexistante (seule exception : l'analyse d'erreurs encadrée du Livre I, § 3.7). Les distracteurs sont toujours des mots ou des formes correctement orthographiés.*

Deux listes à associer, avec distracteurs plausibles pour éviter l'élimination mécanique.

Patrons : P08, P14.

Fonctions : F13, F29, F26.

Vigilance : au moins un distracteur par item.

### MF18 — Carte de rappel

Flashcard recto question / verso réponse, à utiliser en rappel actif.

Patrons : P14.

Fonctions : F29, F36.

Vigilance : question suffisamment précise pour exiger une réponse non triviale.

## Famille 4 — Micro-formats de raisonnement et de production

Supports pour analyser, argumenter, produire.

### MF19 — Dispositif « JE / JE PENSE / JE CONCLUS »

Trois cases successives pour poser un fait, formuler une hypothèse, conclure.

Patrons : P02, P09, P18.

Fonctions : F15, F18, F43.

Vigilance : trois cases séparées évitent l'amalgame.

### MF20 — Argument à compléter

Début d'argument (prémisse, exemple) à prolonger pour aboutir à une conclusion justifiée.

Patrons : P05, P17.

Fonctions : F33, F18.

Vigilance : fournir un connecteur logique de départ.

### MF21 — Comparaison avant / après

Deux cases pour saisir ce qu'on pensait au départ et ce qu'on en pense après l'activité.

Patrons : P01, P09, P18.

Fonctions : F43, F18.

Vigilance : utiliser cette brique à la fin de la séquence.

### MF22 — Reformulation ciblée

Reformuler un passage « avec tes mots », « pour un élève plus jeune », « en 10 mots maximum ».

Patrons : P03, P18.

Fonctions : F09, F14, F32.

Vigilance : préciser la contrainte de reformulation.

### MF23 — Défi de production

Produire un objet (court texte, dessin, schéma, règle de jeu) répondant à une consigne précise avec contraintes.

Patrons : P12.

Fonctions : F31, F32, F30.

Vigilance : 3 à 5 contraintes vérifiables ; viser une production réalisable.

### MF24 — Conclusion argumentée

Rédiger la fin d'une démarche en précisant ce qu'on a trouvé et sur quelle base.

Patrons : P02, P09, P10.

Fonctions : F33, F18.

Vigilance : fournir des amorces (« Je conclus que… parce que… »).

## Famille 5 — Micro-formats collaboratifs et dialogiques

Supports pour échanger, confronter, coopérer.

### MF25 — Think / pair / share écrit

Trois cases : « ma réponse », « réponse de mon camarade », « notre réponse commune ».

Patrons : P13, P11.

Fonctions : F33, F34.

Vigilance : les trois cases ne doivent pas être redondantes.

### MF26 — Fiche expert

Dossier court pour qu'un groupe maîtrise une partie du contenu et puisse l'expliquer aux autres.

Patrons : P11.

Fonctions : F09, F14, F35.

Vigilance : densité calibrée pour le temps imparti.

### MF27 — Grille de restitution

Grille à remplir en écoutant les autres groupes, pour garder trace de leurs apports.

Patrons : P11, P13.

Fonctions : F14, F18, F43.

Vigilance : laisser suffisamment d'espace par rubrique.

### MF28 — Débat structuré (fiche)

Trame pour un échange avec rôles (défenseur / opposant / neutre), questions guides, critères.

Patrons : P05, P13, P17.

Fonctions : F33, F19.

Vigilance : règles d'écoute explicites ; temps limités.

### MF29 — Production collaborative à rôles

Document unique à produire à plusieurs, avec rôles explicites (gardien du temps, rédacteur, relecteur, animateur).

Patrons : P11, P12.

Fonctions : F34, F31.

Vigilance : rôles tournants d'une séance à l'autre.

### MF30 — Annotation croisée

Les élèves annotent la production d'un pair selon une consigne précise.

Patrons : P13, P04.

Fonctions : F38, F42, F39.

Vigilance : critères explicites de bienveillance et de précision.

## Famille 6 — Micro-formats d'autoévaluation et de métacognition

Supports pour prendre du recul, s'auto-réguler, dialoguer avec son propre apprentissage.

### MF31 — Autoévaluation critériée

Grille avec 3 à 5 critères à cocher ou à graduer sur une échelle (feu tricolore, smileys, 1-2-3-4).

Patrons : P18.

Fonctions : F39, F43.

Vigilance : critères formulés positivement, en « je ».

### MF32 — Échelle de confiance

Avant et après la tâche : « À quel point je me sens à l'aise avec cela ? » sur une échelle visuelle.

Patrons : P14, P18.

Fonctions : F39, F43.

Vigilance : même échelle avant / après pour permettre la comparaison.

Variante v7.2 — **jauge affective** (BDRP-F4) : trois phrases décrivant comment l'élève s'est senti·e pendant la tâche. Ce ressenti n'est ni noté ni exposé.

### MF33 — Bilan d'erreur

*Restriction (v6.1, règle MP-CC-11 du Livre I) : par défaut, un support destiné à l'élève ne montre aucune forme écrite fautive ou inexistante (seule exception : l'analyse d'erreurs encadrée du Livre I, § 3.7). Le bilan part d'une erreur figurant dans la production de l'élève ; le support n'en recopie pas la forme fautive et l'élève écrit la forme correcte.*

Analyse courte d'une erreur commise : nature, cause, correction, règle à retenir.

Patrons : P04, P18.

Fonctions : F38, F42, F43.

Vigilance : posture bienveillante, l'erreur comme information.

### MF34 — Question de transfert

« Dans quelle autre situation pourrais-je utiliser ce que j'ai appris ? »

Patrons : P16, P18.

Fonctions : F32, F43.

Vigilance : prévoir au moins deux exemples en modèle.

### MF35 — Carnet d'apprentissage

Trace libre, régulière, de ce qu'on a appris, cherché, compris, pas compris.

Patrons : P18, P09.

Fonctions : F43, F31.

Vigilance : amorces variées pour éviter la répétition formelle.

### MF36 — Diagnostic court

Avant la séquence : 3 à 5 items pour établir ce que l'élève sait déjà.

Patrons : P15, P18.

Fonctions : F07, F36, F42.

Vigilance : items courts, résultats exploitables rapidement.

**Vue d'ensemble : micro-formats × patrons**

Chaque patron mobilise typiquement 3 à 8 micro-formats combinables.

| Patron | Micro-formats typiques |
|---|---|
| P01 Défi initial | MF01, MF06, MF21 |
| P02 Enquête par indices | MF04, MF05, MF19, MF24 |
| P03 Comparaison contrastée | MF07, MF08, MF22 |
| P04 Erreur à débusquer | MF14, MF16, MF30, MF33 |
| P05 Choix argumenté | MF11, MF20, MF28 |
| P06 Exemple guidé puis autonome | MF13, MF14, MF15 |
| P07 Tri raisonné | MF08, MF09, MF10 |
| P08 Associations à justifier | MF17, MF18 |
| P09 Prédire, tester, expliquer | MF06, MF19, MF21, MF24 |
| P10 Cas à résoudre | MF04, MF07, MF24 |
| P11 Experts complémentaires | MF26, MF27, MF29 |
| P12 Production sous contraintes | MF23, MF29 |
| P13 Confrontation des solutions | MF07, MF25, MF30 |
| P14 Rappel actif progressif | MF17, MF18, MF32 |
| P15 Ateliers différenciés | MF13, MF15, MF36 |
| P16 Transfert de contexte | MF15, MF34 |
| P17 Investigation critique des sources | MF04, MF07, MF16, MF28 |
| P18 Retour sur sa démarche | MF21, MF31, MF32, MF33, MF34, MF35 |
| P19 Rallye de postes | MF05, MF38, MF43 |
| P20 Apprivoiser un outil de référence | MF04, MF05, MF12, MF71 |
| P21 Même tâche, plusieurs temps | MF21, MF35, MF43 |
| P22 Les élèves conçoivent l'exercice | MF23, MF64, MF68 |
| P23 Du vécu corporel à la trace | MF38, MF42 |
| P24 La dictée réfléchie | MF33, MF45, MF75 |
| Exactitude et provenance | Réponses et corrigés vérifiés ? Citations, codes PER et sources authentiques ou explicitement non vérifiés ? |
| Indices d’apprentissage | La tâche produit-elle des indices exploitables en lien direct avec les objectifs annoncés ? |
| Régulation après retour | Quand un obstacle est repéré, une nouvelle action de l’élève ou de l’enseignant est-elle prévue ? |
| Données et sobriété | Aucune donnée personnelle superflue ? Fichier et support réalisables avec les outils disponibles ? |

---

## Famille 7 — Micro-formats oraux, corporels et manipulatoires (particulièrement utiles au cycle 1)

### MF37 — Tri matériel d’objets

Trier réellement des objets, formes, images ou quantités, puis expliciter un critère.

Patrons : P07, P03. Fonctions : F12, F13, F17.

Vigilance : Prévoir matériel, conditions de sécurité et possibilités de verbalisation.

### MF38 — Séquence gestuelle ou motrice

Reproduire, modifier ou construire une séquence de gestes en lien avec un apprentissage.

Patrons : P06, P12. Fonctions : F17, F26, F31.

Vigilance : Ne pas supposer une habileté motrice identique ; prévoir une alternative.

### MF39 — Association son–image–objet

Associer un son, un mot oral ou un signal à une image ou un objet.

Patrons : P08, P07. Fonctions : F09, F12, F26.

Vigilance : Vérifier qualité audio, clarté du contraste et accessibilité auditive.

### MF40 — Récit construit avec images

Ordonner des images, raconter oralement, justifier la chronologie et enrichir le récit.

Patrons : P12, P03. Fonctions : F14, F31, F35.

Vigilance : Séparer expression orale, compréhension et exigences de décodage.

### MF41 — Dictée à l’adulte ou transcription accompagnée

Faire produire oralement une idée ou un texte, puis le fixer dans un écrit médiatisé.

Patrons : P12, P18. Fonctions : F22, F31, F35.

Vigilance : Préserver les formulations et les intentions de l’élève ; distinguer dictée et reformulation.

### MF42 — Parcours spatial ou manipulation située

Apprendre en déplaçant, positionnant, mesurant, construisant ou observant dans l’espace.

Patrons : P09, P10. Fonctions : F17, F26, F30.

Vigilance : Préciser espace, sécurité, matériel, accessibilité et critères observables.

## Famille 8 — Micro-formats de suivi, de transformation et de communication

### MF43 — Tableau de suivi de progrès

Relever quelques indices datés, des réussites et la prochaine étape d’apprentissage.

Patrons : P14, P18. Fonctions : F37, F38, F42.

Vigilance : Ne pas confondre suivi pédagogique et profil automatisé de l’élève.

### MF44 — Ticket de sortie et décision pédagogique

Recueillir une réponse diagnostique courte et associer chaque profil de réponse à une suite.

Patrons : P14, P18. Fonctions : F36, F37, F42.

Vigilance : Prévoir de vraies décisions d’ajustement, pas seulement un score.

### MF45 — Boucle rétroaction–révision–nouvel essai

Commenter un résultat avec critères, laisser réviser puis vérifier une seconde production.

Patrons : P04, P06. Fonctions : F38, F42, F43.

Vigilance : Rendre la rétroaction actionnable ; conserver une occasion de réessayer.

### MF46 — Variantes équivalentes d’une même tâche

Générer plusieurs versions comparables avec données, ordre, contexte ou distracteurs différents.

Patrons : P06, P14. Fonctions : F24, F27, F41.

Vigilance : Vérifier l’équivalence de difficulté et les corrigés de chaque version.

### MF47 — Transposition de modalité

Convertir une activité écrite en oral, manipulation, affichage ou numérique, en conservant sa fonction.

Patrons : P07, P10, P13. Fonctions : F25, F26, F34.

Vigilance : Contrôler que la transposition ne change pas les apprentissages évalués.

### MF48 — Fiche de communication simplifiée

Informer élèves ou familles sur objectif, démarche, aides possibles et suite, en langage accessible.

Patrons : P18. Fonctions : F03, F35, F43.

Vigilance : Pas de diagnostics, de données d’élèves ou de promesses sur les résultats.

## Famille 9 — Micro-formats à ancrage disciplinaire (sélection)

Ces dix micro-formats complètent les familles 1 à 8 par des gabarits qui portent une **spécificité disciplinaire** forte et qui ne sont pas réductibles à une brique transversale déjà listée. Ils s'articulent avec les patrons P01-P18 et peuvent être servis par les gabarits d'exercice G1-G14 (Livre I, Étape 3).

### MF49 — Problème en 3 étapes (mathématiques)

Structure : **Données → Opération → Réponse en phrase**. Impose à l'élève de rendre explicite sa démarche de résolution.

Patrons : P10 Cas à résoudre, P06 Exemple guidé puis autonome. Fonctions : F30 Résoudre et décider, F18 Analyser, F31 Produire.

Vigilance : la phrase de réponse DOIT reprendre les termes de l'énoncé pour éviter la mécanisation.

### MF50 — Schéma en barres / \*bar model\* (mathématiques)

Dessiner un modèle de barres avant de calculer : représentation visuelle des parties et du tout, utile dès 3P-4P.

Patrons : P03 Comparaison contrastée, P10 Cas à résoudre. Fonctions : F11 Démontrer modéliser, F30 Résoudre.

Vigilance : réserver aux situations où la représentation éclaire effectivement la structure du problème ; ne pas en faire un exercice formel.

### MF51 — Procédure en deux lignes (mathématiques, autoexplicitation)

« J'ai fait \_\_\_ parce que \_\_\_. » Court dispositif de verbalisation d'une démarche de calcul ou de résolution.

Patrons : P18 Retour sur sa démarche. Fonctions : F43 Métacognition, F33 Argumenter.

Vigilance : à utiliser sur un petit nombre d'items (2-3 par séance) sans quoi la verbalisation devient routinière.

### MF52 — Observe → Décris → Explique (sciences)

Trois cases successives, 2-3 lignes chacune. L'élève sépare ce qu'il observe, ce qu'il nomme et ce qu'il infère.

Patrons : P09 Prédire tester expliquer, P02 Enquête par indices. Fonctions : F12 Observer, F15 Formuler hypothèses, F09 Expliquer.

Vigilance : vérifier que l'élève ne saute pas directement à l'explication sans observation ni description.

### MF53 — Expérience « recette » (sciences)

Structure : **Matériel → Étapes numérotées → Résultat observé**. Format reproductible pour les expérimentations courtes.

Patrons : P09 Prédire tester expliquer, P06 Exemple guidé puis autonome. Fonctions : F17 Manipuler expérimenter, F15 Formuler hypothèses.

Vigilance : nommer la variable manipulée et la variable observée ; éviter la succession de « petites manipulations » sans question directrice.

### MF54 — Analyse d'un document source (SHS)

« Que montre ce document ? Quel indice ? Qui parle, pour qui, pourquoi ? »

Patrons : P17 Investigation critique des sources, P02 Enquête par indices. Fonctions : F16 Rechercher, F18 Analyser, F19 Esprit critique.

Vigilance : adapter le questionnement au degré ; distinguer source primaire et commentaire secondaire dès 5P-6P.

### MF55 — Avant / Après (histoire, SHS)

Deux colonnes : état initial, état après l'événement ou le processus. L'élève identifie ce qui change et ce qui demeure.

Patrons : P03 Comparaison contrastée. Fonctions : F13 Comparer classer, F18 Analyser, F14 Structurer.

Vigilance : la question « qu'est-ce qui change ? » doit être explicitée dans la consigne.

### MF56 — Analyse sensible (arts visuels, musique)

« Je vois / Je ressens / Je pense. » Trois accroches pour structurer la rencontre avec une œuvre sans réduire à l'une des trois dimensions.

Patrons : P01 Défi initial, P18 Retour sur sa démarche. Fonctions : F01 Susciter l'intérêt, F31 Exprimer, F43 Métacognition.

Vigilance : ne pas transformer en questionnaire à bonne réponse ; respecter les trois registres.

### MF57 — Mini-dialogue à trous (langues étrangères)

Dialogue court (4-6 répliques) avec des zones à compléter sur une structure langagière ciblée (salutation, question-réponse, forme verbale).

Patrons : P06 Exemple guidé puis autonome. Fonctions : F26 Appliquer, F29 Mémoriser.

Vigilance : contextualiser (qui parle à qui, pour quoi) ; éviter les suites de phrases décontextualisées.

### MF58 — Résumé 3-2-1 (toutes disciplines, bilan)

**Trois** choses apprises, **deux** questions qui restent, **une** surprise. Dispositif de clôture qui engage la métacognition sans questionnaire long.

Patrons : P18 Retour sur sa démarche. Fonctions : F43 Métacognition, F36 Vérifier la compréhension, F37 Recueillir des traces.

Vigilance : laisser suffisamment de place (6 lignes au total minimum) ; accepter des formulations courtes.

## Famille 10 — Micro-formats ajoutés en v7.2

Ces micro-formats viennent du balayage BDRP du 31.10.2026 (MF59 à MF74), complétés de MF75 et MF76. Leurs noms ont été comparés à ceux de MF01 à MF58, MF37 à MF45 compris (contrôle de non-redondance sur les noms seulement). Les numéros MF62, MF65, MF69 et MF72 ne sont pas attribués : ces candidats sont devenus des variantes de MF32, de la règle MP-J-04, de MF12 et de MF02.

### MF59 — Triple codage du nombre

Même quantité en chiffre, en constellation de dé et en doigts.

Patrons : P14, P20. Fonctions : F12, F29.

Vigilance : Trois représentations alignées : l'une sert à vérifier l'autre (SP1).

### MF60 — Arcs syllabiques

Nombre de syllabes représenté par une suite d'arcs à choisir (icônes IC-SYL).

Patrons : P07, P14. Fonctions : F12, F27.

Vigilance : Prononciation de référence de la classe, à vérifier.

### MF61 — Compteur de progression illustré

Figure dont une partie se complète à chaque réussite.

Patrons : P14, P18. Fonctions : F37, F43.

Vigilance : Compare l'élève à lui-même ou à elle-même, jamais aux autres.

### MF63 — Record personnel

Case « temps » et case « mon record ».

Patrons : P14. Fonctions : F28, F43.

Vigilance : Seulement avec G17, sur des faits compris ; temps gardés par l'élève.

### MF64 — Message codé autovalidant

Les réponses donnent des lettres qui forment un message.

Patrons : P14, P10. Fonctions : F27, F38.

Vigilance : Message peu prévisible, sinon il se devine sans faire la tâche (G18, G11-c, GF-X).

### MF66 — Double modèle script / cursif

Même mot présenté en script et en écriture liée.

Patrons : P06, P14. Fonctions : F12, F27.

Vigilance : Écriture liée composée avec R10, jamais dessinée (GF-J, SP2, SP3).

### MF67 — Repère de latéralité

Main gauche et main droite aux extrémités d'un support, chacune doublée du mot.

Patrons : P20. Fonctions : F23, F25.

Vigilance : Repère placé sur le bord correspondant (SP2).

### MF68 — Rubrique « pour mes camarades »

Case où l'élève prépare quelque chose destiné aux autres.

Patrons : P22. Fonctions : F31, F35.

Vigilance : Relecture de l'enseignant·e avant circulation (GF-I).

### MF70 — Geste mnémotechnique

Un geste du corps associé à une forme ou à une règle.

Patrons : P14. Fonctions : F29.

Vigilance : Le geste se montre : l'IA n'en dessine pas (SP8).

### MF71 — Acronyme de stratégie

Initiales formant un mot-repère pour une suite d'actions.

Patrons : P20, P18. Fonctions : F23, F29, F43.

Vigilance : Chaque action est d'abord enseignée (SP7).

### MF73 — Cases d'aménagements accordés

Liste à cocher des aménagements en tête d'une évaluation.

Patrons : P15. Fonctions : F24, F25.

Vigilance : Visibles des pairs : version individuelle seulement (GF-B3).

### MF74 — Piège nommé, avec origine et autotest

L'erreur classique est décrite en mots, son origine expliquée, et un test permet de s'en apercevoir seul·e.

Patrons : P04, P18. Fonctions : F42, F43.

Vigilance : L'erreur est décrite, jamais montrée sous une forme fautive (MP-CC-11).

### MF75 — Dictée réfléchie (trous, choix, négociation)

Forme de dictée qui fait justifier un choix graphique : mots à écrire dans des lacunes, formes existantes à choisir, phrase commune à négocier.

Patrons : P24. Fonctions : F27, F33, F38.

Vigilance : Texte dicté dans la partie enseignant·e ; aucune phrase fautive imprimée (G20).

### MF76 — Rotation des rôles

Tableau qui répartit les rôles d'un groupe et les fait tourner d'une séance à l'autre. MF29 nomme les rôles sans outiller leur répartition : ce micro-format la rend explicite.

Patrons : P11, P12. Fonctions : F21, F34.

Vigilance : Rôle tiré ou tournant, jamais attribué selon le niveau ou le genre (J13).

---

# PARTIE 7 — ORIGINALITÉ, DIVERSITÉ, RÈGLES DE COMBINAISON

**Pourquoi parler d'originalité**

L'IA tend, par défaut, à produire des ressources **standardisées** : fiche d'exercices à colonnes, questionnaire à choix multiples, texte à trous. Rien n'est faux dans ces formats, mais leur usage systématique :

- lasse les élèves et affaiblit l'engagement ;

- appauvrit la palette didactique mobilisée ;

- renforce l'impression (chez les enseignant·e·s comme chez les élèves) que l'IA ne fait que « des fiches » ;

- ne tire pas parti de la richesse réelle des ressources pédagogiques disponibles.

Faire de l'originalité **un critère de conception assumé** change l'exigence posée à l'IA. Non pour « surprendre » gratuitement, mais pour que la ressource corresponde réellement à la fonction visée, pas à l'habitude du modèle.

**Les trois degrés d'originalité**

Chaque ressource produite peut viser trois niveaux d'originalité, cumulatifs.

**Degré 1 — Originalité du contenu**

Le contenu est **sur mesure** : il parle du contexte réel des élèves, mobilise leur langue, leurs intérêts, le canton, l'école, l'actualité, les prénoms de la classe (avec accord), des exemples locaux, des objets familiers.

Un texte lacunaire sur « Léon et sa trottinette qui part du préau » engage davantage qu'un énoncé générique.

**Degré 2 — Originalité du format**

Le format n'est pas toujours une fiche. Un même objectif peut passer par un plateau de jeu, un memory, une bande dessinée, un podcast, une carte à voyager, un escape game en salle de classe, un dépliant à distribuer, une affiche collective, un parcours photographique. **Le choix du format est une décision didactique à part entière.**

**Degré 3 — Originalité de la combinaison**

Deux ressources connues peuvent être combinées de manière inattendue. Un jeu de cartes qui sert à la fois d'exerciseur et de carnet de métacognition. Une affiche qui devient un terrain de défi. Une BD dont les cases servent de support à une prédiction scientifique. **La combinaison inattendue produit souvent plus d'engagement cognitif que l'addition des deux usages séparés.**

**Les 7 règles de combinaison**

Pour concevoir une ressource riche sans tomber dans l'empilement, le référentiel propose 7 règles.

### Règle 1 — Une intention dominante, des fonctions secondaires si utiles

Une ressource gagne à avoir une intention dominante identifiable. D’autres fonctions peuvent être associées lorsque l’activité et la durée le justifient ; leur nombre n’est pas plafonné mécaniquement.

### Règle 2 — Une organisation cohérente, le nombre minimal de micro-formats utiles

Choisir un patron principal lorsque cela facilite l’organisation, et un ou plusieurs micro-formats seulement si chacun apporte une valeur identifiable. Un seul micro-format peut suffire ; plusieurs patrons peuvent aussi s’articuler dans une séquence.

### Règle 3 — Variété raisonnée des représentations et des actions

Sur une séquence, diversifier lorsque c’est utile les supports, représentations, actions et interactions (texte, oral, image, manipulation, papier, écran, groupe). La diversité ne dépend pas de prétendus profils visuel/auditif/kinesthésique des élèves.

### Règle 4 — Progressivité et étayage lorsque l’objectif le justifie

Pour les exercices et apprentissages procéduraux, prévoir si pertinent une gradation de difficulté et des aides décroissantes. Une image d’amorce, une affiche ou un document de référence n’exigent pas nécessairement cette progression.

### Règle 5 — Prévoir une information de retour au bon niveau du dispositif

À l’échelle de l’activité ou de la séquence, prévoir comment l’élève et l’enseignant sauront ce qui a été compris et quelle suite donner. Chaque objet isolé ne requiert pas son propre corrigé ou outil d’autoévaluation.

### Règle 6 — Réduire les obstacles dès la conception, adapter si nécessaire

Anticiper les obstacles de langage, perception, manipulation, attention et expression. Utiliser des modalités alternatives si elles apportent un bénéfice, puis prévoir les adaptations individuelles qui resteraient nécessaires.

### Règle 7 — Conserver des traces lorsque cela éclaire les apprentissages

Prévoir des traces réutilisables quand elles soutiennent mémorisation, suivi, communication ou régulation. Une expérience orale ou corporelle peut être féconde sans laisser d’écrit individuel.

### Règle complémentaire — Gamification utile et motivation

Un défi, des rôles, des points ou un scénario peuvent soutenir le choix, l’engagement et la coopération ; ils ne constituent pas des garanties d’apprentissage. Vérifier que les règles de jeu rendent nécessaire l’activité cognitive visée, éviter les récompenses qui détournent de la compréhension et prévoir des alternatives à la compétition. (Voir Sailer & Homner, 2020.)

### Règle complémentaire — Transfert, interdisciplinarité et autonomie

Pour un transfert, préciser ce qui doit être réutilisé, ce qui change dans le nouveau contexte et quels critères permettront de vérifier la réutilisation. Pour une activité interdisciplinaire, identifier les objectifs de chaque discipline sans inventer d’alignement PER. Pour l’autonomie, donner des aides consultables, des critères et des occasions de choix, puis ajuster progressivement l’étayage.

**Dialogue avec l'IA : la posture non-limitative**

À chaque étape de la conception, l'IA doit être **explicitement autorisée à proposer autre chose**. Les patrons et micro-formats sont des ressources, pas des contraintes. Un prompt bien construit se termine par :

> *« Si tu identifies un patron ou un micro-format mieux adapté que ceux que je t'indique, propose-le-moi en justifiant brièvement pourquoi. »*

C'est à l'enseignant·e, en dernier ressort, de trancher. L'IA propose, l'enseignant·e dispose.

---

# PARTIE 8 — PROCÉDURE DE CONCEPTION EN 7 ÉTAPES

*Pour toute ressource imprimée destinée aux élèves (fiches, jeux de cartes, dominos, plateaux, dés à monter), la procédure applicable est celle du Livre I (Étapes 0 à 6). La présente Partie reste la référence pour les ressources non imprimées. La question de l'Étape 6 ci-dessous (un jeu sert-il mieux l'objectif qu'une fiche ?) est reprise au § 1.1 du Livre I.*

Cette procédure est la **chaîne de décision** opérationnelle que suit l'enseignant·e (seul·e ou avec l'IA) pour transformer une intention en ressource. Chaque étape pose une question précise ; les réponses successives contraignent naturellement les étapes suivantes.

### Étape 1 — Clarifier l’objectif et les indices de réussite

**Question : Que doit apprendre l’élève, et quelles productions, démarches ou réponses permettront raisonnablement de l’observer ?**

Formuler l'objectif en termes **observables** : *« identifier le verbe conjugué dans une phrase simple »*, *« utiliser la soustraction pour résoudre un problème de reste »*, *« expliquer pourquoi un objet flotte ou coule »*. Préciser le **niveau de maîtrise** attendu (découverte, consolidation, maîtrise, transfert).

Relier l’objectif au PER lorsque la référence est disponible et vérifiable ; ne jamais inventer un code ou une attente officielle.

### Étape 2 — Identifier la fonction pédagogique dominante

**Question** : *Dans quelle intention didactique s'inscrit l'activité ?*

Choisir une fonction principale parmi F01-F43 (ou proposer une autre). Éventuellement une ou deux fonctions secondaires. Vérifier la cohérence avec l'objectif : *appliquer* une procédure (F26) et *la découvrir* (F08) ne se font pas avec les mêmes ressources.

### Étape 3 — Identifier les processus cognitifs mobilisés

**Question** : *Quelles opérations mentales l'élève doit-il réaliser ?*

Positionner la tâche sur la taxonomie révisée (mémoriser, comprendre, appliquer, analyser, évaluer, créer) et préciser le ou les types de connaissances concernés (factuelles, conceptuelles, procédurales, métacognitives). Cette double lecture évite la confusion entre « connaître une règle » et « savoir l'appliquer ».

### Étape 4 — Choisir un patron adapté

**Question** : *Quelle architecture d'activité correspond le mieux ?*

Parcourir les patrons P01-P24 compatibles avec la fonction identifiée. Prendre celui qui correspond le mieux au moment pédagogique (découverte, structuration, entraînement, évaluation) et au niveau d'autonomie des élèves. L'IA peut proposer un autre patron si elle le juge mieux adapté.

### Étape 5 — Choisir les micro-formats

**Question** : *Quelles briques concrètes vais-je combiner ?*

Sélectionner le nombre minimal de micro-formats nécessaires (un seul peut suffire), adaptés au patron et à la durée.

### Étape 6 — Choisir la classe de ressource et le support

**Question** : *Quel type de ressource vais-je produire ?*

Parcourir les 5 familles de supports et 2 dimensions transversales (I à VII) et retenir celle qui sert le mieux l'activité. Ne pas céder au réflexe « fiche d'exercices » si une autre forme serait plus pertinente.

### Étape 7 — Vérifier la qualité globale

**Question** : *La ressource respecte-t-elle les critères de qualité attendus ?*

Appliquer la grille de contrôle qualité ci-dessous.

**Grille de contrôle qualité**

| Critère | Vérification |
|---|---|
| Alignement didactique | L'activité sert bien l'objectif visé ? |
| Cohérence fonction × patron × micro-formats | Les choix s'articulent et ne se contrarient pas ? |
| Accessibilité universelle | Lisible, consignes claires, aides prévues, couleurs non discriminantes ? |
| Différenciation possible | Au moins une variante prévue (facile / difficile, individuel / collectif, papier / numérique) ? |
| Rétroaction intégrée | Corrigé, autoévaluation ou critère explicite ? |
| Originalité raisonnée | La ressource dépasse le format standard quand c'est utile ? |
| Faisabilité réelle | Durée, matériel, préparation, exploitation : tout est tenable en classe ? |
| Trace exploitable | Reste-t-il quelque chose à archiver, à afficher, à réutiliser ? |
| /analyser-ressource | Examiner l’alignement, la difficulté, les erreurs, l’accessibilité et proposer trois priorités de révision. |
| /variante-equivalente | Produire une variante comparable et vérifier systématiquement son corrigé. |
| /reguler | Proposer une rétroaction, une tâche de reprise et un indicateur de progrès. |
| /suivi | Créer un suivi descriptif simple à partir de données strictement anonymisées. |
| /interdisciplinaire | Proposer un transfert avec des liens disciplinaires explicites, sans inventer de correspondances PER. |
| /communication-familles | Préparer une explication accessible des objectifs et des aides, sans information d’élève. |
| /mode-explicatif | Afficher les variantes envisagées et les justifications pédagogiques avant production. |

L’absence d’un élément n’est problématique que lorsqu’il est pertinent pour ce type de ressource. En revanche, toute erreur factuelle, toute référence inventée ou tout désalignement didactique appelle une correction avant livraison.

## Trames de contenu et documents d'accompagnement (v7.2)

Ces trames disent **ce que l'IA produit** pour les types non imprimés. Le code TCnn correspond au type TRnn. Elles complètent les sept étapes ci-dessus ; les outils cités au verso des cartes restent des exemples, sans recommandation institutionnelle. Aucun élève n'utilise l'IA (§ 1.5 du Livre I). Durées et quantités : inférence de conception. Les trames ne se testent pas sur un rendu imprimé : elles ont été relues, sans essai en classe.

| Code | Type | L'IA produit | Trame | Reste à l'enseignant·e |
|---|---|---|---|---|
| TC15 | Album ou livre de lecture | texte et questions | titre ; 6 à 10 doubles pages (texte court, intention de l'image) ; arrêts de prédiction ; questions de compréhension | relire les stéréotypes, choisir les images |
| TC41 | Comptine ou chanson | texte original et gestes | 4 à 8 vers rythmés ; geste par vers ; refrain ; répartition sur plusieurs jours | vérifier le rythme à voix haute, enregistrer |
| TC42 | Capsule audio | script segmenté | tâche d'écoute ; segments de 30 à 60 secondes ; pauses ; question de fin | enregistrer ou contrôler la voix de synthèse |
| TC43 | Capsule vidéo ou tutoriel | script et storyboard | but ; plans numérotés (image, commentaire oral, durée) ; tâche pendant le visionnage | filmer, monter, vérifier le geste |
| TC44 | Diaporama projeté | plan de diapositives | une idée par diapositive : mot-clé, intention d'image, commentaire oral, activité des élèves | composer les diapositives, retirer le décoratif |
| TC45 | Tableau interactif | scénario de manipulation | objets à déplacer ; actions des élèves ; question ; capture à garder | préparer le fichier, alterner avec le matériel réel |
| TC46 | Quiz interactif | banque d'items | 6 à 10 questions ; une bonne réponse ; distracteurs fondés sur des erreurs ; explication après chaque réponse | saisir dans l'outil, vérifier ce qui est retenu |
| TC47 | Exerciseur numérique | banque d'items gradués | série courte ; réponse attendue ; rétroaction par erreur ; seuil de reprise | saisir, fixer la durée, suivre les résultats |
| TC48 | Activité interactive à l'écran | scénario d'interaction | zones actives ; information apportée par chacune ; retour immédiat ; suite prévue | construire l'activité |
| TC49 | Récit interactif à embranchements | structure de récit | carte des nœuds ; choix ; conséquence ; fins ; trace du chemin | saisir dans l'outil, discuter des choix |
| TC50 | Parcours numérique | plan d'étapes | objectif par étape ; activité ; point de contrôle avec l'enseignant·e | choisir les ressources, suivre |
| TC51 | Mur collaboratif numérique | consigne de dépôt | question ; format de la vignette ; groupes ; critère de commentaire ; synthèse | créer le mur, modérer |
| TC52 | Simulation numérique | fiche d'exploration (GF-Q) | question à tester ; paramètre à varier ; tableau d'essais ; conclusion | choisir le logiciel validé |
| TC53 | Robot ou programmation | suite de défis | activité débranchée ; défis courts et progressifs ; instruction attendue | tester sur le robot |
| TC55 | Contenu IA relu | texte relu et rapport | prompt ; contenu ; relevé des contrôles (faits, niveau de langue, stéréotypes) ; mention de l'IA | relire, corriger, porter la responsabilité |
| TC68 | Sondage ou vote en direct | questions et cartons | question ; réponses plausibles révélant des conceptions ; explication ; second vote ; cartons J16 | animer, garder les réponses anonymes |

#### Types « hors production » : documents d'accompagnement

| Type | Non produit par l'IA | Document d'accompagnement | Gabarit |
|---|---|---|---|
| TR12 Manuel ou moyen d'enseignement | le manuel | corrigé expliqué, exercices complémentaires | GF-A |
| TR13 Document authentique | le document | questionnaire d'usage | GF-Q |
| TR24 Image ou œuvre à analyser | l'œuvre | fiche d'analyse (je vois, je pense, je me demande) | GF-Q, variante image |
| TR38 Matériel de manipulation mathématique | le matériel | tapis de tri | G12-b |
| TR39 Objet fabriqué | l'objet | fiche d'accompagnement | GF-O |
| TR40 Matériel d'expérimentation | le matériel | protocole et relevé | GF-O, GF-S |
| TR46 Tableau interactif ou écran tactile | l'équipement | scénario de manipulation | TC45 |
| TR53 Simulation numérique | le logiciel | fiche d'exploration | GF-Q, TC52 |
| TR55 Banque de ressources en ligne | le service | chemin de recherche | GF-O |
| TR58 Outil d'aide technologique | l'outil | fiche d'usage | GF-O |
| TR65 Coin de classe | l'aménagement | étiquettes, règles d'usage | SP5, SP9 |
| TR68 Grille d'évaluation (enseignant·e) | le jugement de l'enseignant·e | grille et version élève | GF-AA |

# PARTIE 9 — PROMPTS ET INSTRUCTIONS D'ASSISTANT

*Pour les ressources imprimées (fiches et jeux), utiliser en priorité l'instruction système et les prompts de l'Étape 6 du Livre I.*

**Pourquoi des prompts cadrés**

Un prompt libre produit, avec une IA générative, des ressources très inégales : parfois pertinentes, souvent génériques, parfois à côté de l'objectif. Un prompt cadré selon la **chaîne de décision** du référentiel oriente l'IA vers une ressource ancrée dans la didactique.

Trois niveaux de prompts sont proposés :

- **Instructions d'assistant** — à placer en tête de projet (Claude Projects, Copilot Pages, GPT personnalisé) pour que l'IA adopte durablement la posture et les repères du référentiel ;

- **Prompts prêts à l'emploi** — à copier-coller selon la fonction visée ;

- **Commandes complémentaires** — pour adapter, varier, différencier une ressource existante.

**Instructions d'assistant (à mettre en tête de projet)**

Ces instructions peuvent être placées dans les consignes persistantes d’un projet ou d’un assistant, ou jointes à une demande selon les capacités de l’outil. Un document joint n’équivaut pas automatiquement à une instruction système et sa consultation effective dépend du produit.

> MISSION
> Assister les enseignant·e·s des cycles 1 et 2 (Suisse romande) pour créer, transformer, analyser et adapter des ressources d’enseignement. Le PER sert de repère lorsque le texte officiel est accessible et vérifiable. L’enseignant·e conserve les décisions pédagogiques et la validation.
>
> RÉFÉRENTIEL DISPONIBLE
> 43 fonctions (F01–F43) ; 11 fonctions pour le travail enseignant (E01–E11) ; 24 patrons (P01–P24) ; 72 micro-formats (MF01–MF76) ; cinq familles de supports (I–V) ; accessibilité et évaluation comme dimensions transversales (VI–VII).
>
> DÉMARCHE
> 1. Identifier objectif, prérequis, moment de séquence, contraintes et indices observables d’apprentissage.
> 2. Choisir fonctions dominantes, processus cognitifs et types de connaissances réellement sollicités ; ne pas déduire le processus d’un verbe isolé.
> 3. Envisager plusieurs organisations si la demande le justifie, et sélectionner la plus pertinente. Les patrons ne sont pas exhaustifs.
> 4. Retenir un ou plusieurs micro-formats, sans quota arbitraire, puis le support adapté (oral, papier, manipulation, numérique, collectif, etc.).
> 5. Produire des contenus complets et corriger les erreurs détectées. Ne pas ajouter systématiquement jeu, narration, autoévaluation, variante, grille ou trace si ces éléments n’aident pas.
> 6. Vérifier exactitude, alignement, accessibilité, faisabilité, indices d’apprentissage et possibilités de régulation.
>
> LES SEIZE USAGES
> Savoir : corriger et réguler ; différencier ; inclure et anticiper les obstacles (CUA) ; renouveler les variantes ; expliciter ; soutenir la métacognition ; évaluer formativement et suivre ; motiver ou ludifier à bon escient ; transférer et articuler les disciplines ; développer l’autonomie ; préparer l’enseignement ; communiquer aux élèves/familles ; transformer les modalités ; créer des supports complémentaires ; analyser les ressources ; personnaliser sans profiler.
>
> PROTECTION ET FIABILITÉ
> Ne jamais présenter un document créé comme authentique s’il est fictif. Ne pas inventer de citation, de code PER ou de source. Signaler une vérification impossible. Ne demander aucune donnée personnelle d’élève non nécessaire ; privilégier une description anonyme des besoins. Ne poser aucune inférence clinique ou psychologique à partir de résultats scolaires. Ne pas présumer qu’une ressource est scientifiquement validée. Distinguer un matériel effectivement fourni d’une réalisation seulement décrite. Une évaluation à enjeu peut être préparée, mais sa validité, son barème et ses décisions demeurent sous responsabilité humaine.
>
> SORTIE PAR DÉFAUT
> A. Note courte : objectif, indices observables, fonction et principe pédagogique, durée, matériel.
> B. Ressource complète destinée aux élèves, dans une forme exploitable.
> C. Corrigé ou critères de réussite lorsque pertinent ; conduite et suites pour l’enseignant ; adaptations utiles si nécessaires.
> Par défaut, ne pas afficher tout le raisonnement de sélection. Sur demande (« mode explicatif »), présenter les alternatives et les justifications. Si la demande porte sur des idées, ne pas créer d’emblée tous les supports.
>
> TON
> Clair, précis, adapté à l’âge, engagé sans surcharge. L’originalité est un moyen au service de l’apprentissage, jamais un objectif isolé.

**Prompts prêts à l'emploi**

Les prompts suivants peuvent être utilisés en complément des instructions ci-dessus, pour cibler une fonction précise. Les variables \[entre crochets\] sont à remplir.

### Prompt A — Créer une ressource à partir d'un objectif PER

> OBJECTIF D’APPRENTISSAGE : \[objectif ou formulation PER authentique\]
> DEGRÉ : \[1P–8P\]
> DISCIPLINE / SUJET : \[préciser\]
> MOMENT : \[découverte / structuration / entraînement / consolidation / transfert / évaluation\]
> DURÉE ET MATÉRIEL : \[préciser\]
> CONTEXTE UTILE : \[acquis, besoins pédagogiques anonymisés, modalité souhaitée ou liberté de choix\]
>
> À partir du référentiel joint, concevoir une ressource intéressante, adaptée aux apprentissages et réalisable. Choisir les fonctions, patrons, micro-formats et supports les plus pertinents sans chercher à remplir toutes les catégories. Fournir la ressource complète, les indices de réussite et les éléments d’accompagnement nécessaires. Présenter les choix pédagogiques en cinq lignes maximum ; développer les alternatives uniquement sur demande.

### Prompt B — Transformer un exercice existant

> RESSOURCE EXISTANTE
> \[Coller le texte, décrire la fiche, joindre le fichier\]
>
> ÉLÉMENTS À CONSERVER
> \[Objectif, type d'exercice, contenus clés\]
>
> ASPECTS À FAIRE ÉVOLUER
> \[Format trop répétitif / consignes peu claires / pas de différenciation /
> pas d'autoévaluation / etc.\]
>
> TRANSFORMATION SOUHAITÉE
> \[Plus manipulable / plus collaboratif / plus accessible aux lecteurs
> débutants / etc.\]
>
> Analyse d'abord brièvement la ressource (forces, obstacles prioritaires),
> puis propose 2 ou 3 transformations possibles, numérotées, en précisant
> pour chacune la fonction visée, le patron, les micro-formats et ce qui
> change par rapport à l'original. Attends mon choix avant de transformer.

### Prompt C — Différencier une ressource

> RESSOURCE DE BASE
> \[Décrire ou joindre\]
>
> OBJECTIF
> \[Rappeler l'objectif d'apprentissage visé\]
>
> ÉLÈVES CIBLES
> Variante 1 : \[profil + besoins\]
> Variante 2 : \[profil + besoins\]
> Variante 3 (optionnelle) : \[profil + besoins\]
>
> Produis une variante pour chaque profil, en conservant la même fonction
> pédagogique mais en adaptant le patron et/ou les micro-formats.
> Précise ce qui change et pourquoi.

### Prompt D — Produire une variante dans une autre classe de ressource

> OBJECTIF D'APPRENTISSAGE
> \[Formuler\]
>
> RESSOURCE DÉJÀ EXISTANTE
> \[Décrire ou joindre : par exemple une fiche d'exercices sur les
> conjugaisons\]
>
> NOUVELLE MODALITÉ SOUHAITÉE
> Classe visée : \[II audiovisuel / III numérique interactif / IV tangible
> manipulable / V environnement / VI accessibilité / VII évaluation côté
> élève\]
> Exemples souhaités : \[jeu de cartes / plateau / affiche / capsule
> vidéo / quiz interactif / etc.\]
>
> Propose la ressource complète, en justifiant brièvement pourquoi
> cette autre forme peut servir le même objectif différemment.

### Prompt E — Produire une ressource d'évaluation formative

> OBJECTIF VISÉ
> \[Formuler\]
>
> APPRENTISSAGES À VÉRIFIER
> \[Mémoriser / Comprendre / Appliquer / Analyser / Évaluer / Créer\]
>
> TYPE DE RÉTROACTION SOUHAITÉE
> Autocorrection par l'élève / Grille d'autoévaluation / Correction
> collective / Pair-feedback / Enseignant·e
>
> DURÉE
> \[X minutes\]
>
> Produis une évaluation formative courte (10-20 minutes) qui respecte
> les principes de Black & Wiliam (feedback utilisable immédiatement,
> critères de réussite explicites, régulation possible).

### Prompt F — Produire un dispositif collaboratif

> OBJECTIF
> \[Formuler\]
>
> NOMBRE D'ÉLÈVES
> Par groupe : \[X\]
> Nombre de groupes : \[Y\]
>
> MATÉRIEL DISPONIBLE
> \[À préciser\]
>
> TYPE DE COOPÉRATION VISÉE
> \[Interdépendance d'informations / interdépendance de tâches /
> interdépendance de rôles / collaboration ouverte\]
>
> Propose un dispositif coopératif complet : consignes aux groupes,
> documents à produire, rôles éventuels, modalités de restitution,
> critères de réussite collective.

### Prompt G — Analyser et améliorer une ressource

> RESSOURCE : \[joindre ou coller\] ; OBJECTIF : \[préciser\] ; DEGRÉ : \[préciser\].
> Analyser l’alignement, les processus cognitifs, la clarté, les erreurs éventuelles, l’accessibilité, les possibilités d’évaluation formative et la faisabilité. Identifier d’abord 3 forces et 3 priorités de révision, puis proposer 2 ou 3 transformations numérotées et attendre le choix de l’enseignant·e ; produire ensuite seulement la version améliorée complète, en explicitant ce qui a changé. Ne pas inventer les informations manquantes.

### Prompt H — Générer des variantes comparables

> OBJECTIF ET DEGRÉ : \[préciser\] ; RESSOURCE INITIALE : \[joindre\] ; NOMBRE : \[indiquer\].
> Générer des versions différentes qui ciblent le même apprentissage et un niveau de difficulté comparable. Varier données, exemples ou supports sans modifier l’objectif. Vérifier chaque corrigé, signaler les différences de difficulté et fournir, si utile, une version avec guidage supplémentaire.

### Prompt I — Réguler les apprentissages à partir de traces

> OBJECTIF : \[préciser\] ; TRACES ANONYMISÉES : \[réponses types ou erreurs fréquentes\].
> Classer les erreurs possibles avec prudence, formuler des hypothèses pédagogiques (sans diagnostic de l’élève), proposer une rétroaction actionnable, puis une tâche de reprise et un indicateur permettant de vérifier si la difficulté est dépassée. Présenter une courte aide pour l’enseignant.

### Prompt J — Transformer et communiquer

> RESSOURCE INITIALE : \[joindre\] ; OBJECTIF À CONSERVER : \[préciser\].
> Proposer deux transpositions pertinentes vers des modalités différentes (oral, manipulation, coopération, papier ou numérique), en précisant ce qui change et ce qui doit rester équivalent. Produire la version retenue et, si utile, un court message aux élèves ou aux familles expliquant les apprentissages, sans informations personnelles.

**Commandes complémentaires**

Ces commandes courtes peuvent être enchaînées sur une ressource déjà produite.

| Commande | Effet attendu |
|---|---|
| /plus-simple | Reformuler ou simplifier pour un élève plus jeune ou en difficulté. |
| /plus-complexe | Ajouter un défi, une consigne de transfert, une contrainte supplémentaire. |
| /accessible | Appliquer les critères UDL : typographie, consignes, pictogrammes, couleurs. |
| /en-jeu | Transformer en jeu (plateau, cartes, dominos, enquête). |
| /en-affiche | Transformer en support collectif à afficher. |
| /en-manipulable | Transformer en support tangible à manipuler. |
| /en-numérique | Transformer en activité interactive (Learningapps, Genially, H5P). |
| /ajouter-autoévaluation | Ajouter un dispositif d'autoévaluation ou de métacognition. |
| /ajouter-corrigé | Produire le corrigé explicite. |
| /vérifier-PER | Vérifier l'ancrage dans le PER et proposer la référence précise. |
| /vérifier-qualité | Appliquer la grille de contrôle qualité (étape 7). |

**Ce que l'IA ne doit pas faire**

Pour la clarté, le référentiel énonce aussi ce qui est **hors de son champ** :

- Produire une ressource sans objectif d'apprentissage explicite.

- Prétendre garantir seule l’exactitude scientifique ou disciplinaire : vérifier autant que possible et signaler les éléments à contrôler par l’enseignant·e.

- Décider seule d’une évaluation à enjeu : elle peut aider à préparer des items, mais validité, équité, notation et décisions relèvent de l’enseignant·e.

- Proposer un accès autonome des élèves à une IA sans cadre institutionnel et pédagogique approprié : l’usage doit rester adapté à l’âge, autorisé et supervisé selon les règles applicables.

- Remplacer la connaissance que l'enseignant·e a de ses élèves.

---

# PARTIE 10 — DÉPLOIEMENT PROGRESSIF ET RÉFÉRENCES

## Déploiement progressif de l'usage

Ce référentiel est dense ; son appropriation progressive s'organise en 4 paliers.

**Palier 1 — Première approche**

**Visée** : prendre contact, dédramatiser, obtenir rapidement une ressource utile.

Point d'entrée : partir d'un besoin ponctuel (différencier une fiche existante, adapter un texte à un niveau de lecture), utiliser le prompt B (transformer) ou C (différencier).

À ce stade, pas d'enjeu d'exhaustivité : l'important est que l'enseignant·e constate que l'IA assistée par le référentiel produit une ressource plus pertinente qu'une IA sans cadrage.

**Palier 2 — Appropriation de la chaîne de décision**

**Visée** : apprendre à nommer la fonction, le patron, les micro-formats mobilisés.

Point d'entrée : utiliser le prompt A (créer à partir d'un objectif PER) et prendre le temps de lire la chaîne de décision proposée par l'IA avant de regarder la ressource. Discuter avec un·e collègue des choix opérés.

C'est à ce stade que la métacognition professionnelle s'installe : *pourquoi ce patron et pas un autre ?*

**Palier 3 — Élargissement des formats**

**Visée** : sortir du réflexe « fiche d'exercices » et explorer les 5 familles de supports et 2 dimensions transversales.

Point d'entrée : utiliser le prompt D (variante dans une autre classe). Produire volontairement une variante jeu manipulable d'une fiche, puis une variante affiche d'un dispositif habituellement individuel.

À ce stade, l'enseignant·e découvre souvent que certaines fonctions pédagogiques sont beaucoup mieux servies par des classes de ressources sous-utilisées jusque-là.

**Palier 4 — Conception écosystémique**

**Visée** : concevoir des **écosystèmes de ressources** cohérents sur une séquence d'apprentissage, où plusieurs ressources de classes différentes se complètent et se répondent.

Point d'entrée : partir d'une séquence complète (3-5 séances) et demander à l'IA de proposer, pour chaque séance, 1-2 ressources de classes différentes articulées entre elles.

C'est à ce palier que la pleine valeur du référentiel apparaît : l'IA cesse d'être un générateur de fiches pour devenir un partenaire de conception didactique.

## Validation du référentiel et limites de l’assistance par IA

Les catégories et les correspondances F–P–MF constituent une proposition opérationnelle : elles ne sont pas une taxonomie académique validée telle quelle. Un usage institutionnel devrait être précédé d’essais sur plusieurs disciplines et degrés. Comparer, pour les mêmes objectifs, des ressources générées avec et sans ce référentiel, puis les faire apprécier par des enseignant·e·s selon l’alignement, la diversité, l’accessibilité, la faisabilité, l’exactitude et le temps de révision.

Le dispositif ne doit jamais inférer un diagnostic, un style d’apprentissage ou une caractéristique personnelle à partir de quelques réponses. Les productions d’élèves doivent être anonymisées, et le traitement de données personnelles respecter les exigences institutionnelles. Les contrôles de qualité automatisés ne remplacent pas l’expertise de l’enseignant·e.

## Repères pour les jeux, la coopération et la différenciation
<!-- modules : jeux, differenciation -->

Ces repères complètent les règles de la Bibliothèque IA 1 (MP-J-07, MP-D-02, § 4.3). Ils servent à conseiller l'enseignant·e avant la production et à justifier les choix dans la partie enseignant·e.

**Évaluer une ressource : utile, utilisable, acceptable**

Le triptyque utilité, utilisabilité, acceptabilité (Tricot et al., 2003) donne trois questions : la ressource fait-elle apprendre ce qui est visé ? Est-elle facile à utiliser ? Les élèves et l'enseignant·e ont-ils envie de s'en servir, et le peuvent-ils dans leur contexte ? L'acceptabilité (ce que les utilisateurs pensent de la ressource) ne se confond pas avec l'accessibilité (la possibilité d'y accéder). La mise en page réduit la charge extrinsèque, celle qui vient de la présentation ; la charge intrinsèque dépend du contenu lui-même (Maitre, 2020).

- Utile : l'objectif d'apprentissage tient en une phrase et se relie au plan d'études ; chaque carte ou chaque case fait travailler cet objectif, sans tâche décorative ; le temps passé à apprendre dépasse le temps passé à attendre ou à gérer le matériel ; tous les élèves du groupe répondent ; quand l'exactitude ne s'entend pas (orthographe, accords), la réponse est écrite ou épelée ; l'erreur est exploitée (vérification, explication, nouvelle tentative) ; un moyen permet de savoir ce que les élèves ont appris ; les contenus sont relus.
- Utilisable : une marche à suivre écrite accompagne le jeu et dit aussi qui commence, comment disposer le matériel, qui vérifie et ce que fait celui qui s'est trompé ; un élève peut expliquer la règle après une partie modèle ; les textes se lisent à la distance d'utilisation et la mise en page est la même sur toutes les cartes ; les images sont de style homogène ; la réponse n'est pas visible par celui qui doit la trouver et un corrigé est disponible ; le matériel est solide, facile à distribuer et à ranger ; la taille des groupes et la durée d'une partie sont définies ; des niveaux ou des variantes permettent à chacun de réussir.
- Acceptable : les élèves ont envie de rejouer ; la règle favorise l'entraide et ne met personne en échec devant les autres ; aucun élève n'est désigné comme « différent » par le matériel qu'il reçoit ; le niveau sonore et l'organisation conviennent à la classe ; les rôles, les situations et les récompenses véhiculent des valeurs compatibles avec celles de l'école (pas de rôle de voleur pour s'exercer à la soustraction) ; le temps de préparation reste raisonnable, et le matériel sobre (pages, couleur, plastification) et réutilisable ; un·e collègue pourrait reprendre le jeu sans explications ; les images sont libres de droits ou sourcées, et aucune donnée d'élève n'apparaît.

**Un jeu pour apprendre, pas pour occuper**

Un jeu prend du temps de classe : préparation, explication, partie, rangement. Il vaut ce temps s'il fait apprendre au moins autant qu'une autre activité de même durée (fiche, travail à l'ardoise). Ce qui compte n'est pas la durée de l'activité, mais le temps pendant lequel l'élève travaille réellement la notion, avec réussite : le temps d'apprentissage scolaire (*academic learning time*, Berliner, 1990).

- Compter les réponses : combien de fois chaque élève répond-il en une partie, et combien de temps attend-il ? Si tout le groupe répond à chaque question, chacun travaille à chaque tour.
- Compter la mise en route (distribuer, expliquer, ranger) : une règle déjà connue, reprise avec d'autres contenus, la réduit.
- Compter la préparation : elle se rentabilise si le jeu sert plusieurs fois, à plusieurs groupes ou d'une année à l'autre.
- Comparer : si une fiche ou dix minutes d'ardoise font travailler la notion aussi bien et plus vite, les préférer ; garder le jeu pour ce qu'il apporte en plus (répéter sans lassitude, échanger, se corriger tout de suite).
- Pour tous, pas seulement pour ceux qui ont fini : réservé aux plus rapides, le jeu entraîne surtout ceux qui en ont le moins besoin.
- Pour s'exercer et se rappeler une notion déjà travaillée, par des reprises espacées : se tester et espacer les reprises comptent parmi les techniques d'apprentissage les mieux étayées (Dunlosky et al., 2013). Le jeu ne remplace pas l'enseignement de la notion.

Chaque jeu de la Bibliothèque IA 1 porte une ligne « Fait apprendre si… / N'apprend rien si… » ; l'IA la reprend dans la partie enseignant·e.

**Des règles du jeu qui font travailler tous les élèves**

Un jeu remis sans mode d'emploi laisse chaque groupe inventer ses règles. Une marche à suivre d'une demi-page répond à cinq questions : le but et ce qu'on apprend en jouant ; le matériel et le nombre de joueurs ; ce qu'on fait à son tour, étape par étape ; ce qui se passe en cas d'erreur et la façon de vérifier la réponse ; la fin de la partie.

- Groupes de trois ou quatre : au-delà, l'attente entre deux tours est longue.
- Tout le monde répond : chaque élève note sa réponse, celui dont c'est le tour la dit à voix haute.
- Un vérificateur ou une vérificatrice dispose du corrigé et change à chaque tour.
- Assez de cartes pour éviter les répétitions, numérotées et rangées par lots.
- Une partie modèle jouée devant la classe, et un but annoncé avant de jouer : « à la fin, vous saurez… ».

La règle précise aussi ce qui, sinon, se négocie à chaque partie : qui commence ; la disposition du matériel au départ (pioche face cachée, cartes étalées, domino de départ posé au centre) ; qui vérifie, et avec quoi ; ce que fait l'élève qui s'est trompé (il lit la bonne réponse, la redit ou la récrit ; la carte repart sous la pioche) ; ce qu'on peut consulter pendant la partie ; la conduite en cas de désaccord. Quand l'exactitude ne s'entend pas (orthographe, homophones, accords : *il chante*, *ils chantent*), la réponse est écrite ou épelée, pas seulement dite (Bibliothèque IA 1, MP-J-07).

**De la compétition à la coopération**

Dans un jeu de l'oie classique, le premier arrivé gagne : la compétition vient de la règle, pas des élèves. Pour obtenir de la coopération, il faut changer la condition de victoire. Le principe central est l'interdépendance positive : chacun ne réussit que si les autres réussissent aussi ; elle va de pair avec la responsabilité individuelle (Johnson & Johnson, 2009). La fiche pratique du CTREQ (2023) y ajoute trois autres conditions : la promotion des interactions, les habiletés sociales et coopératives, et le retour du groupe sur son fonctionnement.

- Un seul pion pour le groupe, contre le sablier ou contre un pion adverse qui avance tout seul.
- Un but commun chiffré : tous les pions arrivés en moins de dix tours, ou vingt cartes réussies.
- Des rôles tournants : lecteur ou lectrice, vérificateur ou vérificatrice, secrétaire, gardien ou gardienne du temps.
- L'aide qui rapporte : si l'explication d'un camarade permet de répondre, les deux avancent.
- L'erreur sans recul : le groupe explique, puis l'élève rejoue.
- Des binômes par pion, qui se mettent d'accord avant de répondre, et un bilan de fin de partie.

Si un élève décide de tout à la place des autres, renforcer les rôles. Si l'intérêt retombe sans enjeu, garder un défi : battre le score de la partie précédente, ou jouer équipe contre équipe.

**Différencier sans faire trois versions de chaque fiche**

La différenciation peut porter sur les contenus, les processus, les productions ou les structures (Forget, 2018). Tripler une fiche ne joue que sur les contenus, le levier le plus coûteux à préparer ; les autres se règlent autour d'une fiche unique.

- Difficulté croissante, avec un repère neutre : chacun choisit son point de départ.
- Noyau commun en haut de la fiche, prolongements facultatifs en bas.
- Aides détachées en libre accès : exemple résolu, rappel de la règle, pictogramme de la démarche.
- Quantité plutôt qu'objectif : « au moins quatre exercices sur huit, dont le numéro 5 ».
- Forme de la réponse au choix : écrire, entourer, relier, manipuler puis dessiner, expliquer oralement.
- Organisation : seul, en binôme d'entraide, ou en petit groupe avec l'enseignant·e.
- Trame stable : objectif, exemple, exercices gradués, défi.

Une fiche identique pour tous, avec des aides en libre accès, ne désigne personne comme « différent ». Le libre choix a une limite : certains élèves choisissent toujours trop facile ou trop difficile, et il faut alors orienter leur point de départ.

**Adapter selon l'obstacle, pas selon une étiquette**

Une adaptation part d'un obstacle observé dans la tâche, non d'un diagnostic ni d'une catégorie d'élèves. Trois obstacles fréquents, et des réponses qui gardent la notion intacte :

- Lecture : consigne courte, une action par phrase, consigne lue à voix haute ou illustrée, mots difficiles expliqués.
- Mémoire de travail : une étape à la fois, données visibles pendant toute la tâche, exemple résolu en tête, moins d'éléments à retenir en même temps.
- Planification : étapes numérotées, case « je vérifie » après chaque étape, temps indicatif.

La demande décrit un besoin de la tâche (« des élèves encore fragiles en lecture ») ; l'IA ne reçoit ni nom, ni diagnostic, ni historique d'élève, et l'aide reste en libre accès pour toute la classe.

**« Si je bloque, je… »**

Un encadré court sur les fiches de travail autonome rend visible une stratégie de régulation : relire la consigne et l'exemple, utiliser une aide en libre accès, demander à un·e camarade, puis seulement à l'enseignant·e (Bibliothèque IA 1, MP-D-06). Il soutient la métacognition (F43) s'il est expliqué en classe et repris lors de la mise en commun ; affiché sans être travaillé, il reste un décor.

**Classe multi-âges**

Deux degrés dans la même classe sont la règle en 1P-2P ; la situation se présente aussi à d'autres degrés, dans les petits établissements ou dans les classes spécialisées qui travaillent avec des programmes adaptés. Plutôt que deux ressources séparées, un matériel commun avec une entrée par degré ou par niveau permet de travailler ensemble (Bibliothèque IA 1, MP-D-05) :

- même jeu, deux lots : collection jusqu'à 5 ou jusqu'à 10, images seules ou images et mots ;
- même fiche, deux parcours : tâche de base et prolongement, sans repère de degré visible ;
- même activité, des rôles qui tournent : manipuler, expliquer, vérifier ; le tutorat entre âges reste un choix de l'enseignant·e ;
- un moment commun pour toute la classe : lancement et mise en commun, chacun·e avec son entrée.

L'objectif du plan d'études est indiqué pour chaque degré ou niveau ; la ressource ne désigne aucun élève par son âge ou par son niveau.

**Montrer que les élèves ont appris**

- Trois ou quatre questions identiques avant et après l'activité.
- Une fiche de suivi où l'élève note ce qui est réussi et ce qui reste difficile.
- Trois productions d'élèves commentées : une réussie, une moyenne, une en difficulté.
- Une courte observation ciblée : qui répond, qui attend, qui aide.

**Références de cette section**

Berliner, D. C. (1990). What's all the fuss about instructional time? In M. Ben-Peretz & R. Bromme (Eds.), *The nature of time in schools: Theoretical concepts, practitioner perceptions*. Teachers College Press.

Centre de transfert pour la réussite éducative du Québec. (2023, août). *Approche coopérative : les premiers pas vers la rétroaction par les pairs* [Fiche pratique]. https://www.ctreq.qc.ca/wp-content/uploads/2023/10/CTREQ-D232-Preparation-a-la-REPAIR-Guide-14x85-44329-V9.pdf#page=1

Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. (2013). Improving students' learning with effective learning techniques: Promising directions from cognitive and educational psychology. *Psychological Science in the Public Interest*, 14(1), 4-58. https://doi.org/10.1177/1529100612453266

Forget, A. (2018). *Penser la différenciation pédagogique* (Carnets des sciences de l'éducation). Université de Genève. https://unige.ch/fapse/editions/index.php/download_file/view/544/492

Maitre, J.-P. (2020). *La théorie de la charge cognitive*. Centre de soutien à l'enseignement, Université de Lausanne. https://enseigner.unil.ch/ressources/wp-content/uploads/20CSE_IN_A_NUTSHELL_01_la_theorie_de_la_charge_cognitive.pdf

Tricot, A., et al. (2003). Utilité, utilisabilité, acceptabilité : interpréter les relations entre trois dimensions de l'évaluation des EIAH. Dans *Environnements informatiques pour l'apprentissage humain* (Strasbourg).

Statut des repères ajoutés le 22.11.2026 (adapter selon l'obstacle, « Si je bloque, je… », classe multi-âges) : propositions de conception de l'auteur, sans référence propre. Statut : existence des références citées vérifiée le 21.11.2026 (CTREQ, 2023 ; Forget, 2018 ; Johnson & Johnson, 2009 ; Maitre, 2020 ; Tricot et al., 2003 ; Bastien & Scapin, 1993, rapport INRIA RT-0156) ; les repères pratiques (astuces, variantes de règles) sont issus de l'enseignement de l'auteur et restent des inférences de conception, non testées à large échelle.

Statut des repères ajoutés le 22.11.2026, suite (un jeu pour apprendre, précision de la règle, réponse écrite ou épelée, valeurs véhiculées, sobriété) : propositions de conception de l'auteur. Berliner (1990) : ouvrage, éditeurs, éditeur commercial et définition du temps d'apprentissage scolaire vérifiés le 22.11.2026 ; pages du chapitre non vérifiées. Dunlosky et al. (2013) : référence et conclusion (rappel actif et reprises espacées jugés les plus utiles) vérifiées le 22.11.2026.

## Composer un écosystème de ressources
<!-- modules : sequences -->

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
<!-- modules : sequences, verification -->

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

## Références scientifiques (APA 7)

**Taxonomies et processus cognitifs**

Anderson, L. W., & Krathwohl, D. R. (Eds.). (2001). *A taxonomy for learning, teaching, and assessing: A revision of Bloom's taxonomy of educational objectives*. Longman.

Bloom, B. S. (Ed.). (1956). *Taxonomy of educational objectives: The classification of educational goals. Handbook I: Cognitive domain*. David McKay.

Krathwohl, D. R. (2002). A revision of Bloom's taxonomy: An overview. *Theory Into Practice*, 41(4), 212-218. https://doi.org/10.1207/s15430421tip4104_2

**Design pédagogique et fonctions**

De Vries, E. (2001). Les logiciels d'apprentissage : panoplie ou éventail ? *Revue Française de Pédagogie*, 137, 105-116. https://doi.org/10.3406/rfp.2001.2851

Laurillard, D. (2012). Teaching as a design science: Building pedagogy for learning technology. Routledge.

Merrill, M. D. (2002). First principles of instruction. *Educational Technology Research and Development*, 50(3), 43-59. https://doi.org/10.1007/BF02505024

Tricot, A. (2020). Quelles fonctions pédagogiques bénéficient des apports du numérique ? Cnesco. https://www.cnesco.fr/fr/ressources/fonctions-pedagogiques-apports-numerique/

Tricot, A., Plégat-Soutjis, F., Camps, J.-F., Amiel, A., Lutz, G., & Morcillo, A. (2003). Utilité, utilisabilité, acceptabilité : interpréter les relations entre trois dimensions de l'évaluation des EIAH. In C. Desmoulins, P. Marquet, & D. Bouhineau (Eds.), *Environnements informatiques pour l'apprentissage humain* (pp. 391-402). INRP.

**Accessibilité et conception universelle**

CAST. (2024). *Universal Design for Learning Guidelines version 3.0*. CAST. https://udlguidelines.cast.org

Meyer, A., Rose, D. H., & Gordon, D. (2014). *Universal design for learning: Theory and practice*. CAST.

**Charge cognitive et multimédia**

Mayer, R. E. (2021). *Multimedia learning* (3rd ed.). Cambridge University Press.

Sweller, J., Ayres, P., & Kalyuga, S. (2011). *Cognitive load theory*. Springer.

**Évaluation et feedback**

Black, P., & Wiliam, D. (2009). Developing the theory of formative assessment. Educational Assessment, Evaluation and Accountability, 21, 5–31. https://doi.org/10.1007/s11092-008-9068-5

Black, P., & Wiliam, D. (1998). Assessment and classroom learning. *Assessment in Education: Principles, Policy & Practice*, 5(1), 7-74. https://doi.org/10.1080/0969595980050102

Hattie, J., & Timperley, H. (2007). The power of feedback. *Review of Educational Research*, 77(1), 81-112. https://doi.org/10.3102/003465430298487

Wiliam, D. (2011). *Embedded formative assessment*. Solution Tree Press.

**Mémoire et rappel actif**

Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. (2013). Improving students' learning with effective learning techniques: Promising directions from cognitive and educational psychology. *Psychological Science in the Public Interest*, 14(1), 4-58. https://doi.org/10.1177/1529100612453266

Roediger, H. L., & Butler, A. C. (2011). The critical role of retrieval practice in long-term retention. *Trends in Cognitive Sciences*, 15(1), 20-27. https://doi.org/10.1016/j.tics.2010.09.003

## Gamification, styles d’apprentissage et différenciation
<!-- modules : differenciation -->

Pashler, H., McDaniel, M., Rohrer, D., & Bjork, R. (2008). Learning styles: Concepts and evidence. Psychological Science in the Public Interest, 9(3), 105–119. https://doi.org/10.1111/j.1539-6053.2009.01038.x

**Ergonomie des documents pédagogiques**

Bastien, J. M. C., & Scapin, D. L. (1993). *Ergonomic criteria for the evaluation of human-computer interfaces* (Rapport technique n° 156). INRIA.

**Didactique disciplinaire (références romandes)**

CIIP. (2010-2024). Plan d'études romand (PER), cycles 1 et 2. Conférence intercantonale de l'instruction publique de la Suisse romande et du Tessin. https://www.plandetudes.ch

**Coopération et apprentissage collaboratif**

Johnson, D. W., & Johnson, R. T. (2009). An educational psychology success story: Social interdependence theory and cooperative learning. *Educational Researcher*, 38(5), 365-379. https://doi.org/10.3102/0013189X09339057

**IA en éducation (références récentes)**

Holmes, W., & Tuomi, I. (2022). State of the art and practice in AI in education. *European Journal of Education*, 57(4), 542-570. https://doi.org/10.1111/ejed.12533

Mollick, E., & Mollick, L. (2024). *Instructors as innovators: A future-focused approach to new AI learning opportunities, with prompts*. SSRN. https://doi.org/10.2139/ssrn.4802463

UNESCO. (2023). *Guidance for generative AI in education and research*. UNESCO Publishing. https://doi.org/10.54675/EWZM9535

**Références romandes et suisses**

CIIP. (2025). Intelligence artificielle générative (IAG) : Recommandations pour une utilisation réfléchie et mesurée dans l’enseignement (19 mars 2025). https://www.ciip.ch/files/1050/Documents/IRDP/Recommandations_IAG_19-03-2025_V10.pdf

Sailer, M., & Homner, L. (2020). The gamification of learning: A meta-analysis. Educational Psychology Review, 32, 77–112. https://doi.org/10.1007/s10648-019-09498-w

---

Statut des références : les cadres de recherche étayent les principes généraux de conception ; ils ne valident pas individuellement les 43 fonctions, 24 patrons et 72 micro-formats de cette typologie de travail. Les références CIIP (2024, 2025) ont été vérifiées sur les sites officiels. D’autres entrées historiques conservées gagneront à faire l’objet d’une vérification bibliographique exhaustive avant publication institutionnelle. Toute information PER précise doit être contrôlée dans le texte officiel.

---

**Fin du référentiel.**

*Document conçu comme ressource de travail pour l'enseignant·e. Il peut être joint comme base de connaissances à une IA générative, consulté en appui à la préparation, ou utilisé comme support de formation continue. Il est destiné à être enrichi par l'usage.*

# ANNEXE II-A — CATALOGUE RESSOURCES AU PRIMAIRE : 71 TYPES DE RESSOURCES (TR01 À TR71)

Cette annexe intègre au référentiel le **Catalogue Ressources au primaire** du dispositif « Cartes de design pédagogique avec IA » : 70 cartes A5, une par type de ressource, classées en huit familles et illustrées par des exemples situés aux cycles 1 et 2, complétées par la carte légende R00 (version du 2 novembre 2026). Elle complète la Partie 4 : la Partie 4 décrit des **classes** de ressources ; le catalogue décrit des **types** concrets, chacun reconnaissable à sa **structure** (sa signature visuelle), sans qu'il soit nécessaire de lire son texte.

**Deux usages.**

- **Choisir et construire** : reconnaître un type de ressource, lire au verso de sa carte ses fonctions dominantes et ses conditions d'usage, le relier aux fonctions, patrons, micro-formats et gabarits du référentiel (A.4), puis le produire avec la procédure applicable : Livre I pour toute ressource imprimée destinée aux élèves (fiches et jeux), Partie 8 pour les ressources non imprimées. Certains types ne se produisent pas avec l'IA (manuel officiel, document authentique, objet, matériel, équipement, service en ligne, aménagement de l'espace) : seuls leurs documents d'accompagnement relèvent du référentiel.

- **Illustrer** : produire avec un générateur d'images une série homogène de visuels A5 montrant chaque type, par exemple pour des cartes de formation. Chaque fiche (A.6) fournit pour cela un texte à placer en surimpression et un prompt d'image.

**Codes.** Le numéro TR est celui de la carte : **TRnn = carte Rnn du catalogue** (TR02 = carte R02, Fiche d'exercices). Le préfixe TR évite toute confusion avec les recettes de construction R1 à R8 du Livre I. La numérotation est celle du catalogue renuméroté le 1er novembre 2026 ; les documents antérieurs, dont la version du 31 octobre 2026 de cette annexe (TR01 à TR49), suivent l'ancienne numérotation : correspondance en A.8.

**Statut des contenus.**

- **Verso de la carte** (description, fonctions, conditions d'usage, outils cités) : texte des cartes du catalogue, repris tel quel. La mention (T) signale une condition tirée de Tricot (2020) ; les autres relèvent de la pratique de classe. Les outils cités ne constituent pas une recommandation institutionnelle.

- **Signature visuelle, texte à intégrer, prompt d'image, vigilance** : textes préparés pour les illustrations des cartes. Les textes à intégrer sont des exemples fictifs : ils ne remplacent pas une fiche conçue avec le Livre I. Pour les 21 types ajoutés le 1er novembre 2026 et les 10 fiches passées en version primaire (liste en A.7), les prompts sont ceux des propositions v0 du 1er novembre 2026 ; leur ajustement éventuel lors de la génération des illustrations n'est pas consigné ici.

- **Correspondances (A.4 et rubrique « Référentiel » des fiches)** : un même type peut servir d'autres fonctions selon l'usage qu'on en fait. Les lignes des 21 types ajoutés ont été tranchées le 2 novembre 2026 selon trois critères (cohérence avec les fonctions et les conditions d'usage au verso de la carte, avec la classe de la Partie 4, avec les codes disponibles) : décision automatique du 2 novembre 2026, réversible.

## A.1 Les huit familles du catalogue

Les familles du catalogue (I à VIII) ne se confondent pas avec les classes de ressources de la Partie 4 (classes I à V et dimensions transversales VI et VII) : la colonne « Classe » de A.4 renvoie toujours à la Partie 4.

| **Famille** | **Cartes** | **Types** |
|---|---|---|
| I. Fiches et documents écrits | TR01 à TR16 | Fiche de découverte · Fiche d'exercices · Fiche autocorrective · Fiche théorique · Fiche guide (marche à suivre) · Fiche de synthèse (révision) · Fiche diagnostique · Page d'étude d'un graphème (page-son) · Tracé de chemin orienté · Support effaçable sous pochette · Sous-main de l'élève · Manuel ou moyen d'enseignement · Document authentique · Dossier thématique documentaire · Album ou livre de lecture |
| II. Affiches, référentiels et visuels | TR17 à TR24 | Affiche de stratégies · Affiche-procédure en « je » · Référentiel collectif · Glossaire de classe · Carte mentale · Infographie · BD pédagogique · Image ou œuvre à analyser |
| III. Cartes et jeux | TR25 à TR37 | Cartes à pince · Domino pédagogique · Memory pédagogique · Cartes à classer · Cartes d'erreurs · Cartes d'aide graduée · Cartes de rappel et reprises espacées · Roue à fenêtre et rabat · Loto · Dé pédagogique · Jeu de l'oie pédagogique · Jeu de plateau pédagogique · Escape game pédagogique |
| IV. Matériel, objets et terrain | TR38 à TR41 | Matériel de manipulation mathématique · Objet fabriqué (FabLearn, 3D) · Matériel d'expérimentation · Fiche-trace de sortie |
| V. Audio, vidéo et numérique | TR42 à TR56 | Comptine ou chanson · Capsule audio · Capsule vidéo ou tutoriel · Diaporama projeté · Tableau interactif ou écran tactile · Quiz interactif · Exerciseur numérique · Activité interactive à l'écran · Récit interactif à embranchements · Parcours numérique · Mur collaboratif numérique · Simulation numérique · Robot ou programmation · Banque de ressources en ligne · Contenu IA relu par l'enseignant·e |
| VI. Accessibilité | TR57 à TR58 | Version adaptée du support · Outil d'aide technologique |
| VII. Dispositifs et organisation de la classe | TR59 à TR65 | Atelier à stations autocorrectif · Feuille de route par niveaux et brevet · Menu à choix · Débat à partir de productions fictives · Galerie de productions · Cartes de rôle (travail de groupe) · Coin de classe |
| VIII. Évaluation et traces | TR66 à TR71 | Billet de sortie · Grille d'autoévaluation (élève) · Grille d'évaluation (enseignant·e) · Sondage ou vote en direct · Dictée réfléchie · Carnet de bord ou portfolio |

## A.2 Les 24 fonctions pédagogiques des cartes (Tricot, 2020)

Au verso, chaque carte indique une à trois fonctions dominantes, numérotées d'après les 24 fonctions pédagogiques étudiées par Tricot (2020). Elles ne remplacent pas les fonctions F01 à F43 de la Partie 1, qui servent à la conception : A.4 donne les deux.

| **N°** | **Fonction** | **Cartes** |
|---|---|---|
| 1 | Présenter de l'information | TR01, TR04, TR05, TR12, TR16, TR17, TR18, TR19, TR20, TR21, TR22, TR45, TR56 |
| 2 | Lire et comprendre un texte, apprendre à lire | TR08, TR13, TR15, TR17, TR23, TR50, TR57 |
| 3 | Écouter un document sonore | TR33, TR42, TR43 |
| 4 | Regarder, lire un document multimédia | TR22, TR23, TR24, TR45, TR49 |
| 5 | Regarder une vidéo, une animation | TR44 |
| 6 | Prendre des notes | TR21 |
| 7 | Poser des questions, demander de l'aide | TR11, TR30 |
| 8 | Rechercher de l'information | TR01, TR13, TR14, TR41, TR55, TR65 |
| 9 | Résoudre des problèmes et calculer | TR05, TR29, TR30, TR37, TR38, TR40, TR46 |
| 10 | S'entraîner | TR02, TR03, TR09, TR10, TR12, TR16, TR25, TR26, TR31, TR32, TR34, TR35, TR39, TR48, TR49, TR51, TR59, TR61, TR70 |
| 11 | Jouer | TR26, TR27, TR33, TR34, TR35, TR36, TR37 |
| 12 | Motiver | TR42, TR47, TR50, TR60, TR61, TR65, TR69 |
| 13 | Coopérer | TR28, TR36, TR37, TR46, TR52, TR59, TR62, TR64 |
| 14 | Apprendre à distance | TR51, TR55 |
| 15 | Évaluer, s'autoévaluer, suivre les progrès | TR02, TR03, TR06, TR07, TR25, TR29, TR32, TR47, TR48, TR59, TR60, TR63, TR66, TR67, TR68, TR69, TR70, TR71 |
| 16 | Faciliter l'accès (besoins éducatifs particuliers) | TR11, TR56, TR57, TR58 |
| 17 | Créer un objet technique, une œuvre | TR18, TR63 |
| 18 | Produire un texte, un document | TR14, TR58, TR62, TR71 |
| 19 | Programmer | TR54 |
| 20 | Découvrir des concepts abstraits | TR28, TR38, TR39 |
| 21 | Faire émerger des idées, créativité | TR24, TR52 |
| 22 | Expérimenter | TR40, TR41, TR53 |
| 23 | Apprendre à faire sur simulateur, en réalité virtuelle | TR53 |
| 24 | Mémoriser, apprendre par cœur | TR04, TR06, TR08, TR16, TR19, TR20, TR27, TR31, TR33, TR42 |

Tricot, A. (2020). *Quelles fonctions pédagogiques bénéficient des apports du numérique ?* Cnesco.

## A.3 Degrés et disciplines des exemples

Le degré et la discipline indiqués sont ceux de l'exemple illustré : la plupart des types se transposent à d'autres degrés et à d'autres disciplines. Tous les exemples sont situés aux cycles 1 et 2, couverts par la table 2.1 du Livre I (1P à 8P).

| **Degré** | **Types** |
|---|---|
| 1P (cycle 1) | TR09 |
| 2P (cycle 1) | TR11, TR27, TR42, TR65 |
| 3P (cycle 1) | TR08, TR15, TR25, TR32, TR38, TR39, TR46 |
| 4P (cycle 1) | TR02, TR05, TR10, TR19, TR34, TR54, TR57 |
| 5P (cycle 2) | TR04, TR07, TR24, TR26, TR33, TR35, TR41, TR43, TR56, TR60, TR70 |
| 6P (cycle 2) | TR01, TR03, TR12, TR18, TR20, TR23, TR28, TR29, TR36, TR40, TR44, TR45, TR47, TR49, TR50, TR59, TR63, TR64, TR67, TR68 |
| 7P (cycle 2) | TR13, TR16, TR17, TR21, TR30, TR31, TR37, TR48, TR52, TR58, TR61, TR69 |
| 8P (cycle 2) | TR06, TR14, TR22, TR51, TR53, TR55, TR62, TR66, TR71 |

Total : 19 types illustrés au cycle 1, 52 au cycle 2 (TR16 compris).

| **Discipline** | **Types** |
|---|---|
| Français | TR04, TR07, TR08, TR09, TR13, TR15, TR17, TR19, TR25, TR34, TR35, TR42, TR50, TR56, TR57, TR58, TR67, TR70, TR71 |
| Mathématiques | TR02, TR05, TR10, TR11, TR12, TR13, TR20, TR26, TR29, TR30, TR37, TR38, TR39, TR44, TR46, TR51, TR66, TR69 |
| Allemand | TR03, TR16, TR31, TR33, TR43, TR49 |
| Anglais | TR48, TR61 |
| Sciences de la nature | TR21, TR22, TR27, TR28, TR32, TR36, TR40, TR41, TR45, TR52, TR53, TR68 |
| Géographie | TR01, TR06, TR47, TR55 |
| Histoire | TR14, TR23 |
| Arts visuels | TR24, TR63 |
| Musique | TR42 |
| Activités créatrices et manuelles | TR18 |
| Corps et mouvement | TR59, TR60 |
| Formation générale | TR22, TR62, TR71 |
| Éducation numérique | TR54 |
| Transversal | TR64, TR65 |

Un exemple qui associe deux disciplines (par exemple « français et mathématiques ») figure dans les deux lignes.

## A.4 Correspondances avec les codes du référentiel

| **TR** | **Type** | **Fonctions de la carte (Tricot)** | **Classe (Partie 4)** | **Fonctions (Partie 1)** | **Patrons, micro-formats, gabarits** | **Procédure** |
|---|---|---|---|---|---|---|
| TR01 | Fiche de découverte | 1, 8 | I | F02, F12, F16 | MF04, MF05, MF10 ; G10 | Livre I |
| TR02 | Fiche d'exercices | 10, 15 | I | F26, F27, F28 | MF13 ; G3 ; G15, G16, G17 | Livre I (GF-A) |
| TR03 | Fiche autocorrective | 10, 15 | I | F27, F38, F39 | MF13, MF64 ; G3 ou G9 ; G11-c, G18 | Livre I |
| TR04 | Fiche théorique | 1, 24 | I | F14, F10, F29 | MF12 ; GF-N | Livre I (GF-N) ; décision automatique du 2 novembre 2026, réversible |
| TR05 | Fiche guide (marche à suivre) | 1, 9 | I | F11, F23, F30 | P06, MF14 ; GF-O | Livre I (GF-O) ; décision automatique du 2 novembre 2026, réversible |
| TR06 | Fiche de synthèse (révision) | 24, 15 | I | F14, F29, F39 | MF12, MF02, MF58 ; G3 ; GF-P | Livre I (GF-P) ; décision automatique du 2 novembre 2026, réversible |
| TR07 | Fiche diagnostique | 15 | I et VII | F05, F07 | MF36, MF16 ; G1, G3, G6 | Livre I |
| TR08 | Page d'étude d'un graphème (page-son) | 2, 24 | I | F14, F27 | MF39, MF66 ; GF-J | Livre I (GF-J, R10) |
| TR09 | Tracé de chemin orienté | 10 | I | F27 | P23 ; G19 | Livre I (G19, R11) |
| TR10 | Support effaçable sous pochette | 10 | conditionnement (I ou IV) | F27 | MF13 ; G9 | Livre I |
| TR11 | Sous-main de l'élève | 7, 16 | I ou IV | F23, F25 | MF12, MF59, MF66, MF67 ; SP1 à SP3 | Livre I (§ 3.9) |
| TR12 | Manuel ou moyen d'enseignement | 1, 10 | I | F08, F26, F27 | MF13 ; GF-A | manuel : hors production ; compléments (corrigé expliqué, exercices) : Livre I ; décision automatique du 2 novembre 2026, réversible |
| TR13 | Document authentique | 8, 2 | I | F02, F16, F18 | MF04, MF54 ; GF-Q | document : hors production (jamais généré) ; questionnaire : Livre I (GF-Q) ; décision automatique du 2 novembre 2026, réversible |
| TR14 | Dossier thématique documentaire | 8, 18 | I | F16, F18, F19, F31 | P17, MF54 ; grille de croisement : G9 ; GF-R | Livre I (GF-R ; documents réels, non générés) ; décision automatique du 2 novembre 2026, réversible |
| TR15 | Album ou livre de lecture | 2 | I | F01, F15 | MF06, MF40 ; TC15 | Partie 8 |
| TR16 | Imagier et scène à légender | 24, 10, 1 | I | F12, F27, F29 | P08, MF01, MF17, MF39 ; G21 ; J2, J7, SP11 | Livre I (G21, R11) ; ajouté le 3 novembre 2026 (renumérotation) |
| TR17 | Affiche de stratégies | 1, 2 | I | F14, F23, F43 | MF12, MF71 ; GF-V ; SP9, SP6 à SP8 | Livre I (GF-V, § 2.5) |
| TR18 | Affiche-procédure en « je » | 1, 17 | I | F11, F23 | MF38 ; GF-V ; SP4 | Livre I (GF-V, § 2.5) |
| TR19 | Référentiel collectif | 1, 24 | I | F14, F23, F29 | MF12, MF39 ; GF-V ; SP10, SP6, SP8 | Livre I (GF-V, § 2.5) |
| TR20 | Glossaire de classe | 1, 24 | I | F10, F14, F23 | MF12 ; GF-V ; SP11 | Livre I (GF-V, § 2.5) |
| TR21 | Carte mentale | 6, 1 | I | F13, F14 | MF03 ; GF-V ; SP12 | Livre I (GF-V, § 2.5) |
| TR22 | Infographie | 4, 1 | I | F08, F14 | MF12 ; GF-V ; SP13 | Livre I (GF-V, § 2.5) |
| TR23 | BD pédagogique | 4, 2 | I | F08, F10 | MF40, MF54 ; GF-W | Livre I (GF-W) |
| TR24 | Image ou œuvre à analyser | 4, 21 | II | F06, F12, F18 | MF19, MF56, MF01 ; GF-Q | œuvre : hors production ; fiche d'analyse : Livre I (GF-Q) ; décision automatique du 2 novembre 2026, réversible |
| TR25 | Cartes à pince | 10, 15 | IV | F12, F27 | MF17, MF39 ; J10 | Livre I (J10) |
| TR26 | Domino pédagogique | 10, 11 | IV | F27, F28 | MF17 ; version fiche : G2 | Livre I (J1) |
| TR27 | Memory pédagogique | 24, 11 | IV | F13, F29 | P08 | Livre I (J2) |
| TR28 | Cartes à classer | 20, 13 | IV | F13 | P07, MF08, MF37 ; version fiche : G12 | Livre I (J3) |
| TR29 | Cartes d'erreurs | 9, 15 | IV | F18, F19, F42 | P04 (mathématiques) ; J14 | Livre I (J14) |
| TR30 | Cartes d'aide graduée | 7, 9 | I ou IV | F22, F23, F24 | P15 ; MP-D (§ 3.6) ; J15 | Livre I (J15) |
| TR31 | Cartes de rappel et reprises espacées | 24, 10 | IV | F28, F29 | P14, MF18, MF43 | Livre I (J4) |
| TR32 | Roue à fenêtre et rabat | 10, 15 | IV | F27, F29 | MF39 ; J11 | Livre I (J11, R11) |
| TR33 | Loto | 11, 3, 24 | IV | F27, F29 | MF39 ; J7 | Livre I (J7) |
| TR34 | Dé pédagogique | 11, 10 | IV | F31, F33 | J6 | Livre I (J6) |
| TR35 | Jeu de l'oie pédagogique | 11, 10 | IV | F01, F27, F28 | P14 | Livre I (J5) |
| TR36 | Jeu de plateau pédagogique | 11, 13 | IV | F29, F30, F34 | P08 | Livre I (J5) |
| TR37 | Escape game pédagogique | 11, 13, 9 | IV | F04, F30, F34 | P10, MF64 ; GF-X ; J13 | Livre I (GF-X) |
| TR38 | Matériel de manipulation mathématique | 9, 20 | IV | F09, F17 | MF37 ; G12-b | tapis : Livre I (G12-b) ; matériel : hors production |
| TR39 | Objet fabriqué (FabLearn, 3D) | 20, 10 | IV | F09, F17, F27 | MF37 ; GF-O | objet : hors production ; fiche d'accompagnement : Livre I (GF-O) ; décision automatique du 2 novembre 2026, réversible |
| TR40 | Matériel d'expérimentation | 22, 9 | IV | F15, F17, F18 | P09, MF06, MF53 ; GF-O, GF-S | matériel : hors production ; protocole : Livre I (GF-O, GF-S) ; décision automatique du 2 novembre 2026, réversible |
| TR41 | Fiche-trace de sortie | 8, 22 | sorties, hors classe | F12, F37 | MF05, MF52 ; GF-S | Livre I (GF-S) |
| TR42 | Comptine ou chanson | 24, 12, 3 | II | F01, F29 | MF38, MF39 ; TC41 ; carte imprimée : G10 | Partie 8 ; carte imprimée : Livre I |
| TR43 | Capsule audio | 3 | II | F08, F09, F12 | MF05, MF56 ; TC42 | Partie 8 |
| TR44 | Capsule vidéo ou tutoriel | 5 | II | F09, F11 | TC43 | Partie 8 |
| TR45 | Diaporama projeté | 1, 4 | II | F08, F09, F10 | MF02 ; TC44 | Partie 8 ; décision automatique du 2 novembre 2026, réversible |
| TR46 | Tableau interactif ou écran tactile | 13, 9 | III | F17, F30, F34 | TC45 | équipement : hors production ; contenus : Partie 8 ; décision automatique du 2 novembre 2026, réversible |
| TR47 | Quiz interactif | 15, 12 | III | F01, F29, F36 | MF16, MF17 ; version papier : G6 ; TC46 | Partie 8 |
| TR48 | Exerciseur numérique | 10, 15 | III | F27, F28, F38 | MF57 ; TC47 | Partie 8 |
| TR49 | Activité interactive à l'écran | 4, 10 | III | F27, F36, F38 | MF16, MF17 ; TC48 | Partie 8 ; décision automatique du 2 novembre 2026, réversible |
| TR50 | Récit interactif à embranchements | 2, 12 | I (papier) ou III | F01, F16, F30 | P02, MF11 ; TC49 | Livre I (papier) ou Partie 8 (numérique) |
| TR51 | Parcours numérique | 14, 10 | III ou V | F21, F22, F43 | MF43 ; TC50 | Partie 8 |
| TR52 | Mur collaboratif numérique | 13, 21 | V | F33, F34, F35 | MF29 ; TC51 | Partie 8 |
| TR53 | Simulation numérique | 23, 22 | III | F15, F17, F18 | P09, MF06 ; GF-Q ; TC52 | logiciel : hors production ; fiche d'exploration : Livre I (GF-Q) ; décision automatique du 2 novembre 2026, réversible |
| TR54 | Robot ou programmation | 19 | III | F17, F30 | TC53 | Partie 8 |
| TR55 | Banque de ressources en ligne | 8, 14 | V | F16, F23 | GF-O | hors production ; chemin de recherche : Livre I (GF-O) ; décision automatique du 2 novembre 2026, réversible |
| TR56 | Contenu IA relu par l'enseignant·e | 1, 16 | III | F08, F24, F25 | Partie 9 (prompts) ; contrôles V1 à V19 ; TC55 | Livre I (imprimé) ou Partie 8 ; décision automatique du 2 novembre 2026, réversible |
| TR57 | Version adaptée du support | 16, 2 | VI | F24, F25 | MF47, MF48 ; MP-D (§ 3.6) | Livre I ; décision automatique du 2 novembre 2026, réversible |
| TR58 | Outil d'aide technologique | 16, 18 | VI | F25, F31 | GF-O | hors production ; fiche d'usage : Livre I (GF-O) ; décision automatique du 2 novembre 2026, réversible |
| TR59 | Atelier à stations autocorrectif | 10, 15, 13 | IV ; aménagement de l'espace | F17, F21, F27, F39 | P15, P19, MF38, MF43 ; GF-E | Livre I (GF-E) |
| TR60 | Feuille de route par niveaux et brevet | 15, 12 | I et VII | F21, F43 | MF43, MF61 ; GF-G, GF-L, GF-M | Livre I (GF-G, GF-M) |
| TR61 | Menu à choix | 12, 10 | I | F21, F24 | MF46, MF68 ; GF-I | Livre I (GF-I) |
| TR62 | Débat à partir de productions fictives | 13, 18 | I ; ressources humaines | F18, F19, F33 | P05, P13, MF28, MF30 ; GF-Y | Livre I (GF-Y) |
| TR63 | Galerie de productions | 17, 15 | aménagement de l'espace | F35, F40 | MF56 ; GF-Z | Partie 8 ; fiche de commentaire : Livre I (GF-Z) |
| TR64 | Cartes de rôle (travail de groupe) | 13 | IV ; ressources humaines et sociales | F21, F33, F34 | P11, MF26, MF29, MF76 ; J13 | Livre I (J13) ; décision automatique du 2 novembre 2026, réversible |
| TR65 | Coin de classe | 12, 8 | aménagement de l'espace | F01, F16, F23 | SP5, SP9 | hors production ; étiquettes et règles d'usage : Livre I (SP5, SP9) ; décision automatique du 2 novembre 2026, réversible |
| TR66 | Billet de sortie | 15 | VII | F36, F37, F43 | MF44, MF32 ; GF-T | Livre I (GF-T) |
| TR67 | Grille d'autoévaluation (élève) | 15 | VII | F39, F43 | MF31 ; G9 ; GF-AA (version élève) | Livre I |
| TR68 | Grille d'évaluation (enseignant·e) | 15 | méta-ressource pour l'enseignant·e | F41 ; E03, E04 | GF-AA, GF-B2 | hors support élève ; Livre I (GF-AA) |
| TR69 | Sondage ou vote en direct | 15, 12 | VII | F01, F06, F33, F36 | MF16, MF32 ; TC68 ; J16 | Partie 8 ; cartons-réponses : Livre I (J16) ; décision automatique du 2 novembre 2026, réversible |
| TR70 | Dictée réfléchie | 10, 15 | I et VII | F27, F33, F38 | P24, MF33, MF45, MF75 ; G3, G6 ; G20 | Livre I (G20) ; décision automatique du 2 novembre 2026, réversible |
| TR71 | Carnet de bord ou portfolio | 15, 18 | VII | F37, F43 | P21, MF35 ; GF-H, GF-K, GF-U | Livre I (GF-H, GF-K, GF-U) |

Les lignes TR04, TR05, TR06, TR12, TR13, TR14, TR24, TR39, TR40, TR45, TR46, TR49, TR53, TR55, TR56, TR57, TR58, TR64, TR65, TR69 et TR70 portent la mention de leur décision. Les codes TCnn renvoient aux trames de la Partie 8.

Toute ressource imprimée destinée aux élèves suit le Livre I, y compris les cartes, dominos, plateaux et dés (gabarits de jeu J1 à J38, § 3.8, avec les règles MP-J et les contrôles V11 à V13) et les affiches (GF-V, § 2.5). La Partie 8 reste la référence pour les ressources non imprimées (TR15, TR42, TR43, TR44, TR45, TR46, TR47, TR48, TR49, TR50, TR51, TR52, TR54, TR56, TR63, TR69) ; leurs trames TC y figurent. Les types TR12, TR13, TR24, TR38, TR39, TR40, TR46, TR53, TR55, TR58, TR65 ne sont pas produits par l'IA (« hors production ») : seuls leurs documents d'accompagnement le sont (tableau de la Partie 8). Les gabarits J2 à J6 restent des correspondances non testées. Tous les codes cités sont définis dans le Livre I ou la Partie 8. La Bibliothèque IA 1 décrit aussi les gabarits d'exercice et de support G1 à G31, propose de la 1P à la 4P le choix entre lignes simples et lignes d'écriture romandes, et offre la couleur en option pour les dessins et les modèles de jeux.

## A.5 Socle commun des visuels (à respecter pour les 71 visuels)

- Visuels **originaux à rendu photographique**, **format A5 vertical**, cadre clair, lumière douce, rendu homogène.

- Ressources **plausibles mais fictives** ; contenus originaux et non identifiants ; **aucune donnée d'élève**.

- **Aucun logo, marque, capture d'écran ni interface reconnaissable** ; outils numériques **génériques** (écran neutre inventé).

- **Texte de la fiche non fiable en génération** : le laisser discret ou flou ; **titre et contenus lisibles ajoutés ensuite en surimpression** (voir « Texte à intégrer »).

- **Distinction des types par la structure**, pas par le texte : respecter la signature visuelle.

**Ajouts v6.2 (conformité au référentiel).**

- Les textes en surimpression respectent le Livre I : aucune forme fautive ou inexistante (MP-CC-11, § 3.7) ; ni émojis, ni couleur seule porteuse d'information (X-08) ; si l'en-tête d'une fiche élève est visible, Prénom et Date figurent tout en haut (MP-O-12).

- Une image générée destinée à un support élève ne contient aucun texte produit par le générateur : le texte est ajouté dans le document, puis relu (MP-I-05, V10).

- Si le générateur produit malgré tout des mots lisibles, ajouter au prompt : « les textes imprimés restent flous et illisibles ».

**Ajouts du 1er novembre 2026.**

- Pour ce que la génération dessine mal, utiliser les icônes de la banque IC ; aucune main générée quand le geste n'est pas le sujet ; aucune représentation anthropomorphe de l'IA (TR56, TR58).

- Écarts assumés : TR46 est vue de face (écran mural) et TR65 en plongée sur un espace de la classe ; TR45, TR49, TR53, TR55 et TR58 montrent, comme TR44, un écran avec une interface inventée ; TR62 garde trois pastilles de couleur.

## A.6 Les 71 fiches

### TR01 — Fiche de découverte

*Carte R01 · famille I (Fiches et documents écrits) · exemple illustré : 6P · cycle 2 · ~10 ans · géographie (SHS).*

**Verso de la carte.** Document ou schéma à observer, avec des questions ouvertes pour explorer une notion nouvelle. Fonctions (Tricot, 2020) : 1 Présenter de l'information ; 8 Rechercher de l'information.

**Pour une bonne utilisation.**

- Placer les légendes au bon endroit sur le document, sans détail décoratif (T).

- Guider l'observation par deux ou trois questions, pas par un questionnaire fermé.

- Prévoir une mise en commun qui fixe ce qu'il fallait découvrir.

**Référentiel.** Classe I ; fonctions F02, F12, F16 ; patrons, micro-formats, gabarits : MF04, MF05, MF10 ; G10 ; procédure : Livre I.

**Signature visuelle.** Mise en page ouverte et hétérogène : un document ou un schéma à observer occupe le haut, de larges zones d'observation et de notes, très peu de cases de réponse. Au premier regard : « on observe, on explore ».

**Texte à intégrer (surimpression).** Titre : « À la découverte de mon village ». Sous-titre : « Observe le plan, puis réponds. » Étiquettes du plan : « école », « rivière », « forêt », « gare ». Encadré : « Ce que je remarque : \_\_\_\_\_\_\_\_ ».

**Prompt d'image.** Vue de dessus d'une fiche de découverte en géographie (~10 ans) sur table claire. En haut, un plan ou une carte simplifiée fictive d'un village (rues, école, rivière, forêt) ; en dessous, de larges espaces de notes lignés et un encadré d'observation. Peu de cases de réponse. Une boussole et une petite règle posées à côté. Style sobre, éducatif, lumière douce. Rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

### TR02 — Fiche d'exercices

*Carte R02 · famille I (Fiches et documents écrits) · exemple illustré : 4P · cycle 1 · ~8 ans · mathématiques.*

**Verso de la carte.** Série d'items de même type pour exercer une notion déjà travaillée. Fonctions (Tricot, 2020) : 10 S'entraîner ; 15 Évaluer, s'autoévaluer, suivre les progrès.

**Pour une bonne utilisation.**

- Proposer surtout des items déjà presque maîtrisés : l'entraînement profite le plus à ce stade (T).

- Donner un retour rapide qui explique l'erreur, pas seulement juste ou faux (T).

- Une notion par série, du plus simple au plus complexe, avec la place pour écrire.

**Référentiel.** Classe I ; fonctions F26, F27, F28 ; patrons, micro-formats, gabarits : MF13 ; G3 ; G15, G16, G17 ; procédure : Livre I (GF-A).

**Signature visuelle.** Mise en page répétitive et régulière : une colonne d'items numérotés identiques, nombreuses lignes ou cases de réponse vides, blocs uniformes. Au premier regard : « une série de tâches à faire ».

**Texte à intégrer (surimpression).** En haut : « Prénom : \_\_\_\_\_\_\_\_ Date : \_\_\_\_\_\_\_\_ ». Titre centré : « Additions jusqu'à 20 ». Phrase d'objectif, sans étiquette : « Je calcule des additions jusqu'à 20. » Items visibles : « 1) 7 + 5 = \_\_\_\_ 2) 9 + 8 = \_\_\_\_ 3) 6 + 6 = \_\_\_\_ 4) 4 + 9 = \_\_\_\_ ».

**Prompt d'image.** Vue de dessus, à plat, d'une fiche d'exercices de mathématiques pour jeunes élèves (~8 ans) sur une table claire en bois pâle. Structure très régulière : en haut une ligne « Prénom / Date », puis un titre centré, puis une liste d'additions numérotées, grandes cases de réponse vides, typographie simple et lisible, généreuse. Un crayon HB posé en biais, une gomme. Ambiance de classe primaire, couleurs neutres, lumière douce et homogène. Rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

**Ajustement v6.2.** Prénom et Date déplacés du bas vers le haut de la fiche ; titre centré et objectif ajoutés (MP-O-12, R7).

### TR03 — Fiche autocorrective

*Carte R03 · famille I (Fiches et documents écrits) · exemple illustré : 6P · cycle 2 · ~10 ans · allemand (langue étrangère).*

**Verso de la carte.** Exercices avec un corrigé intégré (rabat, verso) pour vérifier seul·e. Fonctions (Tricot, 2020) : 10 S'entraîner ; 15 Évaluer, s'autoévaluer, suivre les progrès.

**Pour une bonne utilisation.**

- Rédiger un corrigé qui explique : un retour limité à juste ou faux aide peu (T).

- Faire corriger juste après chaque série : un retour immédiat est crucial pour s'entraîner (T).

- Apprendre la démarche : essayer, vérifier, corriger, sans recopier le corrigé.

**Référentiel.** Classe I ; fonctions F27, F38, F39 ; patrons, micro-formats, gabarits : MF13, MF64 ; G3 ou G9 ; G11-c, G18 ; procédure : Livre I.

**Signature visuelle.** Fiche recto-verso ou pliée : partie « exercices » d'un côté, bande « réponses » repliée ou au dos, avec un pictogramme de retournement (flèche ou loupe). Au premier regard : « je fais, puis je vérifie seul ».

**Texte à intégrer (surimpression).** Titre : « Wortschatz — je m'entraîne et je vérifie ». Recto : « der Apfel = \_\_\_\_ · das Haus = \_\_\_\_ · die Katze = \_\_\_\_ ». Verso replié : « la pomme · la maison · le chat ». Pictogramme : « ↻ retourne pour vérifier ».

**Prompt d'image.** Vue de dessus d'une fiche autocorrective d'allemand (~10 ans) sur table claire, légèrement pliée pour montrer un rabat « réponses » au dos. Recto : quelques mots de vocabulaire à traduire avec cases ; le rabat laisse deviner les réponses. Une petite flèche circulaire suggère de retourner. Crayon posé. Style sobre, lumière douce. Rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

### TR04 — Fiche théorique

*Carte R04 · famille I (Fiches et documents écrits) · exemple illustré : 5P · cycle 2 · ~9 ans · français (grammaire).*

**Verso de la carte.** Page de référence qui fixe une règle ou une notion après l'avoir travaillée, avec des exemples. Fonctions (Tricot, 2020) : 1 Présenter de l'information ; 24 Mémoriser, apprendre par cœur.

**Pour une bonne utilisation.**

- La rédiger après la phase de découverte, avec les mots des élèves puis les mots justes.

- Une règle, deux ou trois exemples, un contre-exemple ; aucun détail décoratif (T).

- La ranger dans le classeur de référence et y renvoyer pendant les exercices.

**Référentiel.** Classe I ; fonctions F14, F10, F29 ; patrons, micro-formats, gabarits : MF12 ; GF-N ; procédure : Livre I (GF-N) ; décision automatique du 2 novembre 2026, réversible.

**Signature visuelle.** Page imprimée au cadre « Règle » bien visible, suivie d'un bloc d'exemples et d'un encadré « Attention ». Elle se distingue de la fiche d'exercices (TR02) par l'absence d'items à résoudre et de la fiche de découverte (TR01) par son statut : elle clôt, elle ne fait pas chercher. Au premier regard : « c'est ce qu'il faut retenir ».

**Texte à intégrer (surimpression).** Titre : « Le pluriel des noms ». Cadre : « Règle : la plupart des noms prennent un -s au pluriel. » Exemples : « un chat → des chats · une table → des tables ». Encadré : « Attention : un nez → des nez ». Pied : « Fiche à ranger dans mon classeur ».

**Prompt d'image.** Vue de dessus d'une fiche A4 imprimée posée sur une table claire en bois pâle, pour élèves de ~9 ans : un titre, un grand cadre arrondi contenant une ligne de texte flou, un bloc de trois exemples courts, un petit encadré en bas marqué d'un pictogramme d'attention. Un surligneur et un classeur fermé posés à côté. Mise en page aérée, texte discret ou flou. Couleurs neutres avec un seul accent coloré. Lumière douce et homogène, rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

**Vigilance.** Le texte réel est posé en surimpression ; le texte généré serait fautif. Un seul cadre « règle » : la génération tend à multiplier les encadrés. Pas de police fantaisie.

### TR05 — Fiche guide (marche à suivre)

*Carte R05 · famille I (Fiches et documents écrits) · exemple illustré : 4P · cycle 1 · ~8 ans · mathématiques.*

**Verso de la carte.** Étapes numérotées pour réaliser une procédure, gardées sous les yeux pendant la tâche. Fonctions (Tricot, 2020) : 1 Présenter de l'information ; 9 Résoudre des problèmes et calculer.

**Pour une bonne utilisation.**

- Six étapes au plus, une action par étape, et un exemple résolu à côté : étudier un problème résolu apprend beaucoup (T).

- Le texte de chaque étape placé juste à côté de son illustration (T).

- La retirer progressivement quand la procédure est acquise.

**Référentiel.** Classe I ; fonctions F11, F23, F30 ; patrons, micro-formats, gabarits : P06, MF14 ; GF-O ; procédure : Livre I (GF-O) ; décision automatique du 2 novembre 2026, réversible.

**Signature visuelle.** Bande verticale d'étapes numérotées, chacune avec un mini-schéma, posée à côté du cahier où l'élève applique la procédure. Elle se distingue de l'affiche-procédure (TR18, collective, geste manuel) par son usage individuel sur le pupitre et son contenu : un calcul. Au premier regard : « je suis les étapes pendant que je fais ».

**Texte à intégrer (surimpression).** Titre : « Je pose une addition en colonnes ». Étapes : « 1. J'aligne les unités sous les unités · 2. J'additionne les unités · 3. S'il y a une retenue, je l'écris en haut · 4. J'additionne les dizaines ». Exemple résolu : « 47 + 25 = 72 » avec la retenue.

**Prompt d'image.** Vue de dessus, sur une table claire en bois pâle, d'une fiche guide étroite et verticale pour élèves de ~8 ans : quatre étapes numérotées, chacune avec un petit schéma de colonnes de chiffres, texte flou ; à droite, un cahier quadrillé ouvert où une addition en colonnes est posée au crayon, avec un petit chiffre de retenue. Un crayon et une gomme. Aucune main. Couleurs neutres avec un seul accent coloré. Lumière douce et homogène, rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

**Vigilance.** Les chiffres du cahier doivent être alignés en colonnes et cohérents (47 + 25 = 72) ; faire corriger ou poser en surimpression. Exactement quatre étapes, numérotées dans l'ordre.

### TR06 — Fiche de synthèse (révision)

*Carte R06 · famille I (Fiches et documents écrits) · exemple illustré : 8P · cycle 2 · ~12 ans · géographie (SHS).*

**Verso de la carte.** Résumé d'une séquence sur une page : mots-clés, schéma à légender et questions pour se tester. Fonctions (Tricot, 2020) : 24 Mémoriser, apprendre par cœur ; 15 Évaluer, s'autoévaluer, suivre les progrès.

**Pour une bonne utilisation.**

- La faire compléter par les élèves (trous, schéma à légender) plutôt que la donner finie.

- Terminer par trois questions d'auto-test, réponses cachées au verso.

- Une seule page ; mots et schéma intégrés, sans détail décoratif (T).

**Référentiel.** Classe I ; fonctions F14, F29, F39 ; patrons, micro-formats, gabarits : MF12, MF02, MF58 ; G3 ; GF-P ; procédure : Livre I (GF-P) ; décision automatique du 2 novembre 2026, réversible.

**Signature visuelle.** Page unique très structurée : un schéma central à légender, des mots-clés en marge, trois questions numérotées en bas. Elle se distingue de la fiche théorique (TR04, une règle) par son échelle : toute une séquence. Au premier regard : « tout le chapitre tient sur une page, et je me teste ».

**Texte à intégrer (surimpression).** Titre : « Ma synthèse — Le relief de la Suisse ». Schéma : coupe simplifiée avec trois zones à légender « Jura · Plateau · Alpes ». Mots-clés : « altitude · versant · vallée · col ». Questions : « 1. Dans quelle zone vit la majorité de la population ? · 2. Cite un col. · 3. Quelle zone est la plus haute ? » Mention : « Réponses au verso ».

**Prompt d'image.** Vue de dessus d'une feuille A4 imprimée sur une table claire en bois pâle, pour élèves de ~12 ans : au centre, une coupe de relief stylisée en trois zones de hauteurs différentes avec trois lignes de légende vides ; dans la marge, quatre mots-clés avec pictogrammes simples ; en bas, trois lignes numérotées. Un crayon et un petit cache en carton posés sur le bas de la page. Texte discret ou flou. Couleurs neutres avec un seul accent coloré. Lumière douce et homogène, rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

**Vigilance.** La coupe doit rester schématique et non géographiquement reconnaissable (pas de carte réelle de la Suisse générée, souvent fausse). Trois zones, pas plus.

### TR07 — Fiche diagnostique

*Carte R07 · famille I (Fiches et documents écrits) · exemple illustré : 5P · cycle 2 · ~9 ans · français.*

**Verso de la carte.** Courte série d'items variés pour situer les acquis avant une séquence. Fonctions (Tricot, 2020) : 15 Évaluer, s'autoévaluer, suivre les progrès.

**Pour une bonne utilisation.**

- Cibler les prérequis réellement nécessaires à la séquence, en peu d'items.

- Ne pas noter : annoncer que le but est de savoir d'où chacun·e part.

- Exploiter les réponses pour former des groupes ou ajuster la séquence.

**Référentiel.** Classe I et VII ; fonctions F05, F07 ; patrons, micro-formats, gabarits : MF36, MF16 ; G1, G3, G6 ; procédure : Livre I.

**Signature visuelle.** Fiche courte, aérée, items brefs et variés, cases de réponse petites, une bande « ce que je sais déjà » bien visible. Au premier regard : « petit bilan rapide ».

**Texte à intégrer (surimpression).** Titre : « Où en suis-je ? — Le groupe du nom ». Bandeau : « Ce que je sais déjà ». Items : « Entoure le nom : le petit chat gris. » « Accorde l'adjectif grand : les \_\_\_\_\_\_\_\_ arbres. » « Vrai ou faux : « chien » est un verbe. ☐ V ☐ F ».

**Prompt d'image.** Vue de dessus d'une courte fiche diagnostique de français (~9 ans), aérée, sur table claire. Quelques items brefs et variés, petites cases à cocher, un bandeau coloré discret « ce que je sais déjà » en haut. Peu de contenu, beaucoup d'espace. Un stylo posé. Rendu net, sobre, lumière douce. Rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

**Ajustement v6.2.** L'adjectif à accorder est sorti de la phrase : la suite « les grand arbres » n'apparaît plus (MP-CC-11).

### TR08 — Page d'étude d'un graphème (page-son)

*Carte R08 · famille I (Fiches et documents écrits) · exemple illustré : 3P · cycle 1 · ~7 ans · français.*

**Verso de la carte.** Écritures du graphème, image-clé, syllabes, mots et phrase sur une seule page. Fonctions (Tricot, 2020) : 2 Lire et comprendre un texte, apprendre à lire ; 24 Mémoriser, apprendre par cœur.

**Pour une bonne utilisation.**

- Un seul graphème par page.

- Syllabes, mots et phrase construits avec des graphèmes déjà étudiés.

- Écriture liée en police scolaire, jamais dessinée par l'IA.

**Référentiel.** Classe I ; fonctions F14, F27 ; patrons, micro-formats, gabarits : MF39, MF66 ; GF-J ; procédure : Livre I (GF-J, R10).

**Signature visuelle.** Page de cahier de lecture structurée autour d'un seul son : en haut, le graphème en grand dans ses quatre écritures avec une image-clé ; au milieu, un tableau de syllabes ; en bas, quelques mots puis une courte phrase à lire. Au premier regard : « une page pour apprendre un son ».

**Texte à intégrer (surimpression).** Titre : « J'entends \[ʃ\], j'écris ch ». Écritures : « ch · CH » en script, et les deux mêmes en cursive (police cursive scolaire). Image-clé : « le chat ». Syllabes : « cha · che · chi · cho · chu ». Mots : « la vache · un chemin · la niche ». Phrase : « Le chat dort dans la niche. »

**Prompt d'image.** Vue de dessus, à plat, d'une page de cahier de lecture pour élèves de ~7 ans sur une table claire en bois pâle : en haut un grand encadré avec une lettre géante et une petite illustration de chat, au milieu un tableau régulier de cinq cases, en bas trois lignes de mots et une ligne de phrase sur papier à lignes d'écriture scolaire. Texte discret ou flou. Un gros crayon et un petit cache de lecture en carton posés à côté. Couleurs neutres avec un seul accent coloré. Lumière douce et homogène, rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

**Vigilance.** La cursive ne doit jamais être générée : une lettre déformée est une forme orthographique fausse. Elle est composée en surimpression avec GE Typo Libre (contrôle du 31.10.2026 : « ch » et « CH » corrects, É, œ et guillemets présents). TrueRomande est à éviter pour tout texte composé automatiquement : œ et Œ s'y affichent comme un « q », le point médian comme un « h », et É, À, Ê, « » manquent.

### TR09 — Tracé de chemin orienté

*Carte R09 · famille I (Fiches et documents écrits) · exemple illustré : 1P · cycle 1 · ~5 ans · français (graphisme).*

**Verso de la carte.** Chemins à suivre au crayon, du plus simple au plus complexe. Fonctions (Tricot, 2020) : 10 S'entraîner.

**Pour une bonne utilisation.**

- Progresser du droit au courbe, puis au zigzag et au labyrinthe.

- Commencer avec des couloirs larges.

- Observer la tenue du crayon et la posture.

**Référentiel.** Classe I ; fonctions F27 ; patrons, micro-formats, gabarits : P23 ; G19 ; procédure : Livre I (G19, R11).

**Signature visuelle.** Fiche de chemins à suivre au crayon entre un départ et une arrivée illustrés, en quatre cadres de difficulté croissante (droit, ondulé, en zigzag, labyrinthe simple) ; couloirs larges bordés d'un trait épais, point vert au départ. Au premier regard : « je suis le chemin sans déborder ».

**Texte à intégrer (surimpression).** Consigne : « Aide la souris à rejoindre le fromage. » Repères : « départ ● » dans chaque cadre ; numéros « 1 · 2 · 3 · 4 ». Pictogramme de consigne : icône IC-CON-RELIE.

**Prompt d'image.** Vue de dessus d'une fiche de graphisme pour enfants de ~5 ans sur une table claire en bois pâle : quatre cadres disposés en deux rangées, chacun avec une petite souris d'un côté et un morceau de fromage de l'autre, reliés par un couloir à suivre (droit, ondulé, en zigzag, puis petit labyrinthe), couloirs larges bordés d'un trait noir épais, un point vert au départ. Le premier chemin est déjà tracé au crayon de couleur, en débordant légèrement. Un gros crayon de couleur triangulaire posé à côté. Graphisme très épuré, beaucoup de blanc. Lumière douce et homogène, rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

**Vigilance.** Vérifier que chaque labyrinthe a bien une seule sortie qui mène au fromage ; la génération produit volontiers des couloirs sans issue ou qui se croisent.

### TR10 — Support effaçable sous pochette

*Carte R10 · famille I (Fiches et documents écrits) · exemple illustré : 4P · cycle 1 · ~8 ans · mathématiques.*

**Verso de la carte.** Fiche glissée sous pochette, complétée au feutre effaçable pour recommencer. Fonctions (Tricot, 2020) : 10 S'entraîner.

**Pour une bonne utilisation.**

- Réserver à l'entraînement répété, pas à une trace à garder.

- Vérifier les réponses avant d'effacer.

- Prévoir des feutres fins et un chiffon.

**Référentiel.** Classe conditionnement (I ou IV) ; fonctions F27 ; patrons, micro-formats, gabarits : MF13 ; G9 ; procédure : Livre I.

**Signature visuelle.** Fiche glissée dans une pochette transparente rigide, complétée au feutre effaçable ; feutre et chiffon posés à côté ; reflets du plastique et bord de la pochette visibles. Au premier regard : « j'écris, j'efface, je recommence ».

**Texte à intégrer (surimpression).** Titre : « Le tableau des nombres ». Lignes visibles : « 41 42 __ 44 __ 46 47 __ 49 50 » et « 51 __ 53 54 __ 56 __ 58 59 __ ». Mention : « J'efface et je recommence ».

**Prompt d'image.** Vue de dessus, sur une table claire en bois pâle, d'une fiche de mathématiques pour élèves de ~8 ans glissée dans une pochette transparente rigide : un tableau de nombres à cases régulières, dont quelques cases vides sont complétées à l'encre de feutre effaçable bleue ; une légère trace d'effacement reste visible dans une case. Un feutre effaçable à capuchon et un petit chiffon en microfibre posés à côté. Reflets discrets de la pochette, bord de la pochette visible. Couleurs neutres avec un seul accent coloré. Lumière douce et homogène, rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

**Vigilance.** Carte retenue (validation du 31.10.2026) : elle montre un mode de conditionnement applicable à toute fiche. Les reflets de la pochette ne doivent pas masquer le tableau ; l'encre doit paraître effaçable (trait de feutre, pas de stylo).

### TR11 — Sous-main de l'élève

*Carte R11 · famille I (Fiches et documents écrits) · exemple illustré : 2P · cycle 1 · ~6 ans · mathématiques.*

**Verso de la carte.** Support plastifié posé sur le pupitre, avec les outils de référence de l'élève. Fonctions (Tricot, 2020) : 7 Poser des questions, demander de l'aide ; 16 Faciliter l'accès (besoins éducatifs particuliers).

**Pour une bonne utilisation.**

- N'y mettre que les outils réellement utilisés.

- L'adapter aux besoins de l'élève (repères, codages).

- Placer les repères gauche et droite sur les bords correspondants du sous-main.

**Référentiel.** Classe I ou IV ; fonctions F23, F25 ; patrons, micro-formats, gabarits : MF12, MF59, MF66, MF67 ; SP1 à SP3 ; procédure : Livre I (§ 3.9).

**Signature visuelle.** Grand support plastifié couvrant le plateau d'un pupitre : en haut une bande numérique de 0 à 10 où chaque nombre est codé trois fois (chiffre, points, doigts) ; sur un bord, une réglette avec un repère de main gauche et de main droite ; en bas, l'alphabet en écriture scripte. Au premier regard : « mes outils, toujours sous la main ».

**Texte à intégrer (surimpression).** Titre : « Mon sous-main ». Bande : « 0 1 2 3 4 5 6 7 8 9 10 », sous chaque nombre sa constellation de points et sa main de comptage (icônes IC-MAIN-0 à IC-MAIN-10, convention « pouce d'abord »). Réglette : « main gauche · main droite » (icônes IC-LAT-G et IC-LAT-D). Alphabet : « a b c d e f g h i j k l m n o p q r s t u v w x y z ». Champ : « Prénom : ________ ».

**Prompt d'image.** Vue en plongée d'un pupitre d'élève de ~6 ans dans une classe claire : un grand sous-main plastifié couvre le plateau, avec en haut une longue bande numérique à cases régulières, sur le côté une réglette colorée, en bas une rangée de lettres. Les cases restent simples et peu détaillées. Une trousse ouverte, un gros crayon et une gomme posés sur le sous-main, reflets discrets de la plastification. Couleurs douces, un seul accent coloré. Lumière douce et homogène, rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

**Vigilance.** Ne pas faire générer de mains ni de doigts : le nombre de doigts dessinés est souvent faux [connaissance non vérifiée ici]. Les mains de comptage viennent de la banque IC, en surimpression.

### TR12 — Manuel ou moyen d'enseignement

*Carte R12 · famille I (Fiches et documents écrits) · exemple illustré : 6P · cycle 2 · ~10 ans · mathématiques.*

**Verso de la carte.** Livre ou fichier officiel de la discipline, organisé en chapitres et exercices, lié au plan d'études. Fonctions (Tricot, 2020) : 1 Présenter de l'information ; 10 S'entraîner.

**Pour une bonne utilisation.**

- Choisir les exercices selon l'objectif, pas suivre la page dans l'ordre.

- Compléter le corrigé par un retour qui explique l'erreur : juste ou faux aide peu (T).

- Apprendre aux élèves à s'y repérer : sommaire, pictogrammes, numéros d'exercices.

**Référentiel.** Classe I ; fonctions F08, F26, F27 ; patrons, micro-formats, gabarits : MF13 ; GF-A ; procédure : manuel : hors production ; compléments (corrigé expliqué, exercices) : Livre I ; décision automatique du 2 novembre 2026, réversible.

**Signature visuelle.** Manuel ouvert sur une double page avec un bandeau de chapitre, un encadré de cours et une colonne d'exercices numérotés ; un cahier à côté. La ressource la plus utilisée et la moins analysée. Au premier regard : « le livre de la classe, ouvert au bon chapitre ».

**Texte à intégrer (surimpression).** Bandeau : « Chapitre 4 — Les fractions ». Encadré : « Une fraction désigne une ou plusieurs parts égales d'un tout. » Exercices : « 12. Colorie 3/4 de chaque figure · 13. Écris la fraction coloriée ». Pied de page : « Mathématiques 6 · p. 48 ».

**Prompt d'image.** Vue de dessus d'un manuel scolaire cartonné ouvert sur une table claire en bois pâle, pour élèves de ~10 ans : double page avec un bandeau de chapitre coloré, un encadré de cours, de petites figures géométriques partiellement coloriées et une colonne d'exercices numérotés, texte flou. Un cahier fermé et un crayon posés à côté. Couverture et maquette entièrement inventées, aucune collection reconnaissable. Couleurs neutres avec un seul accent coloré. Lumière douce et homogène, rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

**Vigilance.** Aucun moyen d'enseignement romand réel ni logo d'éditeur : couverture et maquette inventées. Figures de fractions cohérentes (parts égales) ; sinon, poser en surimpression. Titre du manuel fictif (« Mathématiques 6 » sans éditeur).

### TR13 — Document authentique

*Carte R13 · famille I (Fiches et documents écrits) · exemple illustré : 7P · cycle 2 · ~11 ans · français et mathématiques.*

**Verso de la carte.** Document de la vie réelle (horaire, ticket, notice, affiche) utilisé tel quel comme support de tâche. Fonctions (Tricot, 2020) : 8 Rechercher de l'information ; 2 Lire et comprendre un texte, apprendre à lire.

**Pour une bonne utilisation.**

- Choisir un document local et lisible, sans donnée personnelle (horaire, menu, notice).

- Poser une vraie question d'usage : « à quelle heure dois-je partir ? ».

- Guider la recherche d'information par étapes : chercher dans un document est difficile sans aide.

**Référentiel.** Classe I ; fonctions F02, F16, F18 ; patrons, micro-formats, gabarits : MF04, MF54 ; GF-Q ; procédure : document : hors production (jamais généré) ; questionnaire : Livre I (GF-Q) ; décision automatique du 2 novembre 2026, réversible.

**Signature visuelle.** Horaire de bus imprimé, tel qu'affiché à un arrêt, avec une fiche de questions posée dessus et un surligneur. Le document n'a pas été fait pour l'école : c'est ce qui fait sa valeur. Au premier regard : « un vrai document, une vraie question ».

**Texte à intégrer (surimpression).** Horaire : « Ligne 12 — Arrêt Gare → Collège · 7:42 · 7:57 · 8:12 · 8:27 ». Fiche : « L'école commence à 8:15. Le trajet dure 10 minutes. Quel bus dois-tu prendre ? Entoure-le. »

**Prompt d'image.** Vue de dessus, sur une table claire en bois pâle, d'un horaire de transport imprimé au format affichette pour élèves de ~11 ans : un tableau d'horaires fictif à quelques colonnes et lignes, texte flou, en-tête neutre sans logo ; posée en partie dessus, une petite fiche de questions avec deux lignes d'écriture et un surligneur ouvert. Aucune main. Couleurs neutres avec un seul accent coloré. Lumière douce et homogène, rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

**Vigilance.** Aucun logo ni nom de compagnie de transport réelle, aucun nom d'arrêt réel : horaire entièrement fictif. Les heures doivent être posées en surimpression pour que l'exercice soit juste.

### TR14 — Dossier thématique documentaire

*Carte R14 · famille I (Fiches et documents écrits) · exemple illustré : 8P · cycle 2 · ~12 ans · histoire (SHS).*

**Verso de la carte.** Ensemble de documents variés (textes, images, cartes) réunis sur un thème, pour enquêter. Fonctions (Tricot, 2020) : 8 Rechercher de l'information ; 18 Produire un texte, un document.

**Pour une bonne utilisation.**

- Quatre à six documents courts, de natures différentes, numérotés.

- Une question d'enquête et une grille pour croiser les documents.

- Terminer par une production qui cite les documents (affiche, texte).

**Référentiel.** Classe I ; fonctions F16, F18, F19, F31 ; patrons, micro-formats, gabarits : P17, MF54 ; grille de croisement : G9 ; GF-R ; procédure : Livre I (GF-R ; documents réels, non générés) ; décision automatique du 2 novembre 2026, réversible.

**Signature visuelle.** Chemise cartonnée ouverte d'où dépassent des documents de natures différentes, numérotés, et une grille d'enquête. Elle se distingue de la fiche de découverte (TR01, un document) par la pluralité des sources. Au premier regard : « plusieurs documents, une question ».

**Texte à intégrer (surimpression).** Couverture : « Dossier 3 — Vivre au bord du lac il y a 100 ans ». Étiquettes : « Doc 1 : photographie · Doc 2 : carte · Doc 3 : témoignage · Doc 4 : objet ». Grille : « Question : comment se déplaçait-on ? · Ce que dit le doc 1… le doc 2… ».

**Prompt d'image.** Vue de dessus, sur une table claire en bois pâle, d'une chemise cartonnée ouverte pour élèves de ~12 ans contenant quatre documents en partie superposés : une photographie ancienne fictive en noir et blanc d'une rive de lac avec une barque, une carte dessinée stylisée, une feuille de texte flou, une petite image d'objet ; chaque document porte une étiquette numérotée ; à côté, une grille d'enquête vide et un crayon. Aucune main. Couleurs neutres avec un seul accent coloré. Lumière douce et homogène, rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

**Vigilance.** Photographie et carte entièrement inventées, aucun lieu ni archive réels identifiables ; aucune personne reconnaissable sur la photo. Quatre étiquettes numérotées, ordre lisible.

### TR15 — Album ou livre de lecture

*Carte R15 · famille I (Fiches et documents écrits) · exemple illustré : 3P · cycle 1 · ~7 ans · français (lecture).*

**Verso de la carte.** Livre lu ou partagé pour comprendre une histoire ou découvrir une notion. Fonctions (Tricot, 2020) : 2 Lire et comprendre un texte, apprendre à lire.

**Pour une bonne utilisation.**

- Accompagner la lecture et vérifier la compréhension par des questions.

- Choisir des illustrations au service du texte.

- Pour un texte généré par IA, relire et vérifier les stéréotypes.

**Référentiel.** Classe I ; fonctions F01, F15 ; patrons, micro-formats, gabarits : MF06, MF40 ; TC15 ; procédure : Partie 8.

**Signature visuelle.** Album ouvert sur une double page illustrée, avec un marque-page à questions glissé dans le livre et un petit carnet de prédictions. La ressource est un livre entier, accompagné d'un geste de lecture. Au premier regard : « je lis, je m'arrête, j'imagine la suite ».

**Texte à intégrer (surimpression).** Sur la double page : « Lila et le grand vent » et une phrase courte : « Le vent emporte le chapeau de Lila. » Marque-page : « Stop ! Que va-t-il se passer ? ». Carnet : « Je pense que… ________ ».

**Prompt d'image.** Vue de dessus d'un album jeunesse cartonné ouvert sur une table claire en bois pâle, pour élèves de ~7 ans : double page avec une grande illustration douce d'une fillette sur une colline, un chapeau emporté dans le ciel, et une courte ligne de texte. Un marque-page en carton coloré dépasse du haut du livre, un petit carnet ouvert et un crayon à côté. Personnage original, aucune couverture ni personnage existant. Couleurs douces, un seul accent coloré. Lumière douce et homogène, rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

**Vigilance.** L'album doit rester fictif : aucun style, personnage ou titre reconnaissable (le balayage BDRP signale ce risque pour les albums sous licence). Un visage d'enfant de loin ou de dos évite les défauts de génération.

### TR16 — Imagier et scène à légender

*Carte R16 · famille I (Fiches et documents écrits) · exemple illustré : 7P · cycle 2 · ~11 ans · allemand (langue étrangère). Carte ajoutée le 3 novembre 2026 ; les cartes R16 à R70 du 2 novembre deviennent R17 à R71 (A.8).*

**Verso de la carte.** Une scène ou une planche d'images dont l'élève nomme les éléments : il ou elle relie, écrit ou colle le mot sous chaque numéro. Fonctions (Tricot, 2020) : 24 Mémoriser, apprendre par cœur ; 10 S'entraîner ; 1 Présenter de l'information.

**Pour une bonne utilisation.**

- Des images à dénomination univoque, sans texte dedans ; le mot se place dans le document (T).

- Une entrée pour chaque élève : étiquettes à relier ou à coller pour les non-lecteurs, mot à écrire pour les autres ; en langue étrangère, l'article fait partie du mot.

- La fiche complétée devient un référentiel : la relire, la réutiliser en jeu (loto, memory).

**Référentiel.** Classe I ; fonctions F12, F27, F29 ; patrons, micro-formats, gabarits : P08, MF01, MF17, MF39 ; G21 ; variantes J2 (cartes en double version), J7 (loto), SP11 (glossaire) ; procédure : Livre I (G21, R11).

**Signature visuelle.** Une scène riche et colorée (place de petite ville) occupant les deux tiers de la page, parsemée de pastilles blanches numérotées sur des éléments bien séparés ; en dessous, douze courtes lignes numérotées sur deux colonnes. Elle se distingue de la page-son (TR08, un graphème) par le vocabulaire d'un thème entier, du glossaire (TR20, définitions) par l'image qui précède le mot, et de l'activité interactive (TR49, à l'écran) par le support papier. Au premier regard : « je nomme ce que je vois ».

**Texte à intégrer (surimpression).** Titre : « In der Stadt ». Consigne : « Schreibe das Wort mit dem Artikel. » Lignes 1 à 12 vides. Corrigé (partie enseignant·e, hors visuel) : 1 die Bäckerei · 2 die Apotheke · 3 der Bahnhof · 4 der Bus · 5 der Brunnen · 6 der Markt · 7 die Kirche · 8 das Fahrrad · 9 der Hund · 10 die Bank · 11 der Abfalleimer · 12 das Schild.

**Prompt d'image.** Vue de dessus d'une feuille A4 imprimée posée sur une table claire en bois pâle, pour élèves de ~11 ans apprenant l'allemand : les deux tiers supérieurs sont occupés par une scène riche et colorée d'une place de petite ville, illustration plate et nette aux couleurs douces : une boulangerie, une pharmacie, une gare avec un train, un arrêt de bus avec un bus, une fontaine, un marché avec un étal de fruits, une église, un vélo, un chien, un banc, une poubelle, un panneau de rue vierge ; une douzaine d'éléments bien séparés, chacun marqué d'une petite pastille ronde blanche numérotée de 1 à 12 ; quelques personnages vus de loin, sans visage détaillé. Le tiers inférieur de la feuille porte douze courtes lignes d'écriture numérotées, vides, sur deux colonnes. Aucun mot imprimé sur la feuille, enseignes vierges. Un crayon posé en biais, un surligneur fermé dans un coin. Lumière douce et homogène, rendu photographique, format vertical 2:3, matériel fictif et original, sans logo ni marque.

**Vigilance.** Mots allemands posés en surimpression (le texte généré est faux) ; la scène reste sans texte (MP-I-05), la croix verte de la pharmacie est un symbole admis. Les numéros des pastilles sont à vérifier un à un sur le visuel généré (1 à 12, chacun une fois) ; les reposer en surimpression s'ils sont déformés. Aucun dessin tiers reconnaissable ; personnages lointains, sans visage. Visuel généré le 3.11.2026 (ChatGPT) : conforme, recadré au format A5 des autres cartes ; le « panneau » est un simple rectangle bleu, acceptable pour « das Schild ».

### TR17 — Affiche de stratégies

*Carte R17 · famille II (Affiches, référentiels et visuels) · exemple illustré : 7P · cycle 2 · ~11 ans · français.*

**Verso de la carte.** Affiche qui rend visibles les étapes ou les stratégies d'une tâche (lire, résoudre…). Fonctions (Tricot, 2020) : 1 Présenter de l'information ; 2 Lire et comprendre un texte, apprendre à lire.

**Pour une bonne utilisation.**

- La construire avec les élèves plutôt que l'afficher toute faite.

- Six étapes au plus, numérotées, chacune avec un pictogramme.

- Y renvoyer explicitement pendant les tâches.

**Référentiel.** Classe I ; fonctions F14, F23, F43 ; patrons, micro-formats, gabarits : MF12, MF71 ; GF-V ; SP9, SP6 à SP8 ; procédure : Livre I (GF-V, § 2.5).

**Signature visuelle.** Grand format vertical affiché ou posé, titre en haut, étapes ou stratégies listées avec pictogrammes, mise en page synthétique. Au premier regard : « un mémo collectif au mur ».

**Texte à intégrer (surimpression).** Titre : « Bien comprendre un texte ». Étapes : « 1. Je survole le texte · 2. Je repère les mots importants · 3. Je me fais un film dans la tête · 4. Je résume · 5. Je vérifie ce que j'ai compris ». Pictogrammes simples.

**Prompt d'image.** Photographie d'une affiche pédagogique verticale (~10-11 ans) posée sur un chevalet ou fixée sur un mur clair : titre en haut, cinq stratégies de lecture listées avec de petits pictogrammes, mise en page synthétique et colorée mais sobre. Cadrage droit, lumière douce, rendu net. Rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

### TR18 — Affiche-procédure en « je »

*Carte R18 · famille II (Affiches, référentiels et visuels) · exemple illustré : 6P · cycle 2 · ~10 ans · activités créatrices et manuelles.*

**Verso de la carte.** Étapes illustrées, formulées en « je », pour réaliser un geste ou un objet. Fonctions (Tricot, 2020) : 1 Présenter de l'information ; 17 Créer un objet technique, une œuvre.

**Pour une bonne utilisation.**

- Six étapes au plus, dans l'ordre, chacune avec son image.

- Montrer le geste avant d'afficher la procédure.

- Montrer le résultat attendu.

**Référentiel.** Classe I ; fonctions F11, F23 ; patrons, micro-formats, gabarits : MF38 ; GF-V ; SP4 ; procédure : Livre I (GF-V, § 2.5).

**Signature visuelle.** Affiche verticale de cinq étapes numérotées, chacune avec une vignette du geste et une phrase courte en « je », l'objet terminé en bas. Elle se distingue de l'affiche de stratégies (TR17) par la suite de gestes illustrés et le résultat montré. Au premier regard : « je suis les étapes pour fabriquer ».

**Texte à intégrer (surimpression).** Titre : « Je couds un bouton ». Étapes : « 1. J'enfile le fil dans l'aiguille. · 2. Je fais un nœud au bout du fil. · 3. Je pique de l'envers vers l'endroit, à travers un trou du bouton. · 4. Je pique dans le trou d'à côté, puis je recommence quatre fois. · 5. Je termine par un nœud sur l'envers. » En bas : « Résultat ».

**Prompt d'image.** Photographie d'une affiche verticale fixée au mur clair d'un atelier d'activités créatrices : cinq vignettes dessinées en colonne, chacune montrant un geste de couture simple avec un numéro, et en bas la photo d'un bouton cousu sur un carré de tissu. Sous l'affiche, sur une table, une bobine de fil, une pelote à épingles et un carré de tissu. Cadrage droit, couleurs douces, un seul accent coloré. Lumière douce et homogène, rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

**Vigilance.** Carte retenue (validation du 31.10.2026) pour couvrir les activités créatrices et manuelles ; vérifier qu'elle ne se confond pas avec TR17. Aiguille et mains : à contrôler de près, ou montrer les gestes par des vignettes dessinées sans mains.

### TR19 — Référentiel collectif

*Carte R19 · famille II (Affiches, référentiels et visuels) · exemple illustré : 4P · cycle 1 · ~8 ans · français.*

**Verso de la carte.** Panneau de référence durable, organisé en rubriques avec des exemples. Fonctions (Tricot, 2020) : 1 Présenter de l'information ; 24 Mémoriser, apprendre par cœur.

**Pour une bonne utilisation.**

- Le compléter progressivement, au fil des apprentissages.

- Le placer à la vue de tous et y renvoyer souvent.

- Garder des exemples courts et sans erreur.

**Référentiel.** Classe I ; fonctions F14, F23, F29 ; patrons, micro-formats, gabarits : MF12, MF39 ; GF-V ; SP10, SP6, SP8 ; procédure : Livre I (GF-V, § 2.5).

**Signature visuelle.** Panneau ou grande fiche de référence structurée en rubriques (encadrés, exemples types), destiné à rester affiché. Au premier regard : « une référence de classe stable ».

**Texte à intégrer (surimpression).** Titre : « Nos sons ». Rubriques : « \[o\] : bateau, moto », « \[ou\] : loup, roue », « \[an\] : maman, dent ». Petites images à côté de chaque son.

**Prompt d'image.** Photographie d'un référentiel collectif de français (~8 ans) affiché sur un mur clair : grand panneau structuré en rubriques encadrées, chaque rubrique associant un son, des mots-exemples et une petite image. Mise en page ordonnée, couleurs douces, aspect « affichage de classe » durable. Cadrage droit, lumière douce. Rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

### TR20 — Glossaire de classe

*Carte R20 · famille II (Affiches, référentiels et visuels) · exemple illustré : 6P · cycle 2 · ~10 ans · mathématiques (géométrie).*

**Verso de la carte.** Mots de la discipline avec une définition courte et un croquis. Fonctions (Tricot, 2020) : 1 Présenter de l'information ; 24 Mémoriser, apprendre par cœur.

**Pour une bonne utilisation.**

- Une définition courte, un exemple et un croquis par mot.

- Le construire avec la classe et le compléter au fil des leçons.

- Y faire recourir pendant les exercices.

**Référentiel.** Classe I ; fonctions F10, F14, F23 ; patrons, micro-formats, gabarits : MF12 ; GF-V ; SP11 ; procédure : Livre I (GF-V, § 2.5).

**Signature visuelle.** Entrées courtes alignées, chacune associant un mot, une définition brève et un petit croquis ; encadrés réguliers, marges généreuses, quelques termes soulignés. Au premier regard : « les mots dont j'ai besoin, expliqués et illustrés ».

**Texte à intégrer (surimpression).** Titre : « Les mots de la géométrie ». Entrées visibles : « Sommet — le point où des côtés ou des arêtes se rejoignent », « Arête — le segment où deux faces d'un solide se rejoignent », « Droites perpendiculaires — deux droites qui se coupent en formant un angle droit ». Mention en bas : « à compléter ensemble ».

**Prompt d'image.** Vue de dessus, à plat, d'un glossaire de classe en géométrie pour élèves de ~10 ans, posé sur une table claire en bois pâle. Trois ou quatre entrées encadrées, chacune avec un mot en gras, une définition courte et un petit croquis géométrique tracé à la main. Typographie simple et lisible, beaucoup d'air, couleurs neutres avec un seul accent coloré. Un crayon et une règle posés en biais. Lumière douce et homogène, rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

**Ajustement v6.2.** La définition source de l'arête (« le segment entre deux sommets ») désigne aussi une diagonale ; elle est précisée. « Sommet » couvre désormais polygones et solides ; « perpendiculaire » devient « droites perpendiculaires ». Vocabulaire à confronter aux moyens d'enseignement romands du degré (non vérifié).

### TR21 — Carte mentale

*Carte R21 · famille II (Affiches, référentiels et visuels) · exemple illustré : 7P · cycle 2 · ~11 ans · sciences de la nature.*

**Verso de la carte.** Notion au centre, branches et mots-clés pour organiser des idées. Fonctions (Tricot, 2020) : 6 Prendre des notes ; 1 Présenter de l'information.

**Pour une bonne utilisation.**

- Fournir une structure de départ : branches principales déjà posées.

- Peu de branches au cycle 1, davantage ensuite.

- La construire avec les élèves.

**Par exemple avec.** Digimindmap (ladigitale.dev).

**Référentiel.** Classe I ; fonctions F13, F14 ; patrons, micro-formats, gabarits : MF03 ; GF-V ; SP12 ; procédure : Livre I (GF-V, § 2.5).

**Signature visuelle.** Feuille couverte d'une structure rayonnante : une idée centrale, trois branches colorées, des mots courts et de petits dessins ; le tout tracé à la main, avec des feutres posés autour. Au premier regard : « tout part du centre, je vois les liens ».

**Texte à intégrer (surimpression).** Centre : « L'eau ». Branches : « États : glace · eau · vapeur », « Cycle : évaporation · condensation · précipitations », « Usages : boire · cultiver · produire de l'électricité ».

**Prompt d'image.** Vue de dessus d'une feuille posée sur une table claire en bois pâle : carte mentale dessinée au feutre par un élève de ~11 ans, un cercle central avec une goutte d'eau, trois grosses branches courbes de couleurs différentes se divisant en branches fines, chacune terminée par un mot court et un petit dessin simple (glaçon, nuage, robinet). Trois feutres posés à côté. Tracé spontané mais soigné. Lumière douce et homogène, rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

**Vigilance.** Chaque mot doit être sur sa propre branche, reliée au centre sans branche flottante. Trois couleurs servent ici à distinguer les branches : c'est une exception assumée au « seul accent coloré » du socle.

### TR22 — Infographie

*Carte R22 · famille II (Affiches, référentiels et visuels) · exemple illustré : 8P · cycle 2 · ~12 ans · sciences de la nature et formation générale (environnement).*

**Verso de la carte.** Document qui combine chiffres, pictogrammes et textes courts. Fonctions (Tricot, 2020) : 4 Regarder, lire un document multimédia ; 1 Présenter de l'information.

**Pour une bonne utilisation.**

- Intégrer mots et images, sans détail décoratif (T).

- Une idée par bloc et un ordre de lecture clair.

- Guider la lecture par des questions.

**Par exemple avec.** Digidesign et Digicard (ladigitale.dev) · Canva (canva.com).

**Référentiel.** Classe I ; fonctions F08, F14 ; patrons, micro-formats, gabarits : MF12 ; GF-V ; SP13 ; procédure : Livre I (GF-V, § 2.5).

**Signature visuelle.** Affichette verticale où l'information tient dans un parcours visuel : étapes numérotées reliées par une flèche, un pictogramme et quelques mots par étape, sans paragraphe. Elle se distingue de l'affiche de stratégies (TR17) parce qu'elle informe sur un phénomène au lieu de guider une démarche. Au premier regard : « je comprends tout le trajet d'un coup d'œil ».

**Texte à intégrer (surimpression).** Titre : « Que devient ma bouteille en PET ? ». Étapes : « 1. Je la dépose au point de collecte · 2. Elle est triée par couleur · 3. Elle est broyée en paillettes · 4. Les paillettes deviennent une nouvelle bouteille ». Mention : « Exemple fictif simplifié ».

**Prompt d'image.** Vue de dessus d'une affichette imprimée sur une table claire en bois pâle, pour élèves de ~12 ans : mise en page d'infographie verticale, quatre étapes numérotées reliées par une large flèche sinueuse, un pictogramme simple pour chaque étape (bouteille, petit conteneur gris ou brun de collecte PET portant le logo PET, comme en Suisse, paillettes, bouteille neuve), très peu de texte. Aucune marque de boisson. Une paire de ciseaux ou un crayon posé dans un coin. Style plat et propre, couleurs neutres avec un seul accent coloré. Lumière douce et homogène, rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

**Vigilance.** Contexte suisse : le conteneur jaune généré d'abord évoquait la France ; garder un petit conteneur gris ou brun avec le logo PET (correction du 31.10.2026). Marques de boissons à exclure. Pas de chiffres : un pourcentage généré paraîtrait factuel sans source. Le contenu est à vérifier auprès d'une source romande si la carte sert au-delà de l'illustration.

### TR23 — BD pédagogique

*Carte R23 · famille II (Affiches, référentiels et visuels) · exemple illustré : 6P · cycle 2 · ~10 ans · histoire.*

**Verso de la carte.** Récit en cases et en bulles pour présenter une notion ou un événement. Fonctions (Tricot, 2020) : 4 Regarder, lire un document multimédia ; 2 Lire et comprendre un texte, apprendre à lire.

**Pour une bonne utilisation.**

- Placer le texte dans l'image, au bon endroit (T).

- Des bulles courtes, une idée par case.

- Si la BD est générée par IA, vérifier les stéréotypes et les anachronismes.

**Par exemple avec.** Digistrip (ladigitale.dev) · Book Creator (bookcreator.com).

**Référentiel.** Classe I ; fonctions F08, F10 ; patrons, micro-formats, gabarits : MF40, MF54 ; GF-W ; procédure : Livre I (GF-W).

**Signature visuelle.** Planche de quatre cases avec bulles, qui met un contenu en récit ; une question de lecture en dessous renvoie à ce que la BD enseigne. Au premier regard : « je lis une histoire et j'apprends quelque chose ».

**Texte à intégrer (surimpression).** Titre : « Au marché, il y a 700 ans ». Case 1 : « Combien pour ce pain ? ». Case 2 : « Deux deniers. ». Case 3 : « Trop cher ! Un denier et un œuf ? ». Case 4 : « C'est d'accord ! ». Sous la planche : « Comment paie-t-on dans cette BD ? ».

**Prompt d'image.** Vue de dessus d'une planche de bande dessinée imprimée sur une table claire en bois pâle, pour élèves de ~10 ans : quatre cases régulières, deux par rangée, scène de marché médiéval dessinée simplement avec deux personnages originaux (une marchande de pain, un paysan), bulles blanches de forme simple avec texte court, légère ligne de question sous les cases. Un crayon à côté. Dessin clair et lisible, couleurs douces. Lumière douce et homogène, rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

**Vigilance.** Les bulles doivent suivre l'ordre de lecture et pointer vers le bon personnage. Mêmes vêtements et mêmes visages d'une case à l'autre : c'est le défaut le plus probable. Dialogue fictif : le prix ne vaut pas donnée historique, à signaler si la carte sert en classe.

### TR24 — Image ou œuvre à analyser

*Carte R24 · famille II (Affiches, référentiels et visuels) · exemple illustré : 5P · cycle 2 · ~9 ans · arts visuels.*

**Verso de la carte.** Reproduction d'une image ou d'une œuvre, à observer, décrire puis interpréter. Fonctions (Tricot, 2020) : 4 Regarder, lire un document multimédia ; 21 Faire émerger des idées, créativité.

**Pour une bonne utilisation.**

- Trois temps écrits au tableau : je vois · je pense · je me demande.

- Choisir une œuvre libre de droits ou une image originale ; citer l'auteur·e.

- Afficher en grand ; cacher puis dévoiler des parties pour relancer l'observation.

**Référentiel.** Classe II ; fonctions F06, F12, F18 ; patrons, micro-formats, gabarits : MF19, MF56, MF01 ; GF-Q ; procédure : œuvre : hors production ; fiche d'analyse : Livre I (GF-Q) ; décision automatique du 2 novembre 2026, réversible.

**Signature visuelle.** Reproduction d'un tableau original posée à plat, avec un cache en carton qui en masque un coin et une fiche à trois colonnes. L'image n'illustre pas : elle est l'objet d'étude. Au premier regard : « je regarde longtemps avant de parler ».

**Texte à intégrer (surimpression).** Fiche : « Je vois… · Je pense que… · Je me demande… ». Étiquette sous la reproduction : « Paysage au lac, peinture, artiste fictif·ve ».

**Prompt d'image.** Vue de dessus, sur une table claire en bois pâle, d'une reproduction imprimée d'une peinture originale et inventée : paysage calme avec un lac, des collines et une barque, touche picturale simple, style non attribuable à aucun artiste connu ; un cache en carton gris recouvre un coin de l'image ; à côté, une fiche à trois colonnes vides et un crayon. Aucune main. Couleurs douces, un seul accent coloré sur la fiche. Lumière douce et homogène, rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

**Vigilance.** Aucune œuvre, aucun style ni signature reconnaissables ; refuser toute consigne « à la manière de ». Le cache doit masquer réellement une partie (pas un rectangle flottant). L'étiquette reste fictive.

### TR25 — Cartes à pince

*Carte R25 · famille III (Cartes et jeux) · exemple illustré : 3P · cycle 1 · ~7 ans · français.*

**Verso de la carte.** Petites cartes avec une question et plusieurs réponses : l'élève pince la bonne. Fonctions (Tricot, 2020) : 10 S'entraîner ; 15 Évaluer, s'autoévaluer, suivre les progrès.

**Pour une bonne utilisation.**

- Une seule bonne réponse par carte, avec des distracteurs plausibles.

- Prévoir une marque d'autocorrection au verso.

- Proposer des séries courtes et plastifier les cartes pour qu'elles durent.

**Référentiel.** Classe IV ; fonctions F12, F27 ; patrons, micro-formats, gabarits : MF17, MF39 ; J10 ; procédure : Livre I (J10).

**Signature visuelle.** Petites cartes cartonnées avec une question et plusieurs réponses sur les bords ; des pinces à linge en bois posées sur les bords. Au premier regard : « on pince la bonne réponse ».

**Texte à intégrer (surimpression).** Sur les cartes : image d'un « lapin » avec sur les bords « l · r · m » ; image d'un « soleil » avec « s · f · p ». Étiquette du set : « Cartes à pince — le son du début ».

**Prompt d'image.** Gros plan de petites cartes à pince plastifiées pour élèves de ~7 ans, sur table claire. Chaque carte montre une image simple (lapin, soleil) et trois lettres sur le bord (le son initial à trouver) ; deux ou trois pinces à linge en bois posées sur les bords. Couleurs vives et enfantines, coins arrondis. Lumière douce, rendu net. Rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

**Ajustement v6.2.** Distracteur « c » remplacé par « p » : la lettre c peut noter le son \[s\] (cerise), ce qui rendait l'item ambigu (inférence didactique, à valider).

### TR26 — Domino pédagogique

*Carte R26 · famille III (Cartes et jeux) · exemple illustré : 5P · cycle 2 · ~9 ans · mathématiques.*

**Verso de la carte.** Pièces qui associent une question et une réponse, à raccorder en chaîne ou en boucle. Fonctions (Tricot, 2020) : 10 S'entraîner ; 11 Jouer.

**Pour une bonne utilisation.**

- Vérifier avant d'imprimer que chaque réponse ne convient qu'à une seule question.

- Contrôler que la boucle se referme : le jeu se corrige alors de lui-même.

- Terminer par un court débriefing sur les associations difficiles (T).

**Référentiel.** Classe IV ; fonctions F27, F28 ; patrons, micro-formats, gabarits : MF17 ; version fiche : G2 ; procédure : Livre I (J1).

**Signature visuelle.** Pièces rectangulaires de type domino, chaque pièce coupée en deux (un calcul d'un côté, un résultat de l'autre), disposées en chaîne qui se raccorde. Au premier regard : « on relie calcul et résultat ».

**Texte à intégrer (surimpression).** Sur les pièces, dans l'ordre de la chaîne : « 6 × 4 \| 42 », « 7 × 6 \| 32 », « 4 × 8 \| 45 », « 9 × 5 \| 24 ». Étiquette : « Dominos des livrets ».

**Prompt d'image.** Vue de dessus de pièces de domino pédagogique en carton épais (~9 ans) disposées en chaîne sur table claire. Chaque pièce est divisée en deux : à gauche une multiplication, à droite un résultat, si bien que les pièces se raccordent. Quelques pièces alignées, d'autres en attente. Couleurs sobres et lisibles, lumière douce, rendu net. Rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

### TR27 — Memory pédagogique

*Carte R27 · famille III (Cartes et jeux) · exemple illustré : 2P · cycle 1 · ~6 ans · sciences de la nature (découverte du monde).*

**Verso de la carte.** Paires de cartes à retrouver face cachée (image et mot, notion et exemple). Fonctions (Tricot, 2020) : 24 Mémoriser, apprendre par cœur ; 11 Jouer.

**Pour une bonne utilisation.**

- Construire des paires sans ambiguïté : une seule correspondance possible par carte.

- Commencer avec peu de paires, puis en ajouter.

- Faire nommer la paire à voix haute à chaque découverte.

**Référentiel.** Classe IV ; fonctions F13, F29 ; patrons, micro-formats, gabarits : P08 ; procédure : Livre I (J2).

**Signature visuelle.** Grille de cartes carrées retournées face cachée (dos identique) avec deux ou trois paires révélées face visible (une image et un mot ou une lettre). Au premier regard : « jeu de paires à retrouver ».

**Texte à intégrer (surimpression).** Sur les paires révélées : image d'un poisson ↔ image d'un étang ; image d'un oiseau ↔ image d'un nid dans un arbre ; image d'une taupe ↔ image de la terre. Étiquette : « Memory — chaque animal chez lui ».

**Prompt d'image.** Vue de dessus d'un jeu de memory pour jeunes élèves (~6 ans) sur table claire : une grille de cartes carrées face cachée au dos coloré uniforme, et deux ou trois paires retournées associant chacune un animal et son milieu de vie (images simples). Graphisme enfantin, grandes illustrations, couleurs vives. Lumière douce, rendu net. Rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

### TR28 — Cartes à classer

*Carte R28 · famille III (Cartes et jeux) · exemple illustré : 6P · cycle 2 · ~10 ans · sciences de la nature.*

**Verso de la carte.** Étiquettes à répartir dans des catégories, pour construire ou vérifier un concept. Fonctions (Tricot, 2020) : 20 Découvrir des concepts abstraits ; 13 Coopérer.

**Pour une bonne utilisation.**

- Annoncer les critères de tri, ou les faire émerger puis les formuler.

- Inclure quelques cas limites et les discuter.

- Demander de justifier chaque classement, de préférence à deux.

**Référentiel.** Classe IV ; fonctions F13 ; patrons, micro-formats, gabarits : P07, MF08, MF37 ; version fiche : G12 ; procédure : Livre I (J3).

**Signature visuelle.** Étiquettes-cartes réparties en colonnes ou en tas sous des en-têtes de catégories ; flèches ou zones de tri visibles. Au premier regard : « on trie en catégories ».

**Texte à intégrer (surimpression).** En-têtes : « Vivant » / « Non-vivant ». Cartes : « chat », « rocher », « arbre », « vélo », « champignon », « nuage ». Étiquette : « Trie les éléments ».

**Prompt d'image.** Vue de dessus de petites cartes-étiquettes à classer (~10 ans) sur table claire, réparties en deux colonnes sous deux en-têtes de catégories. Chaque carte porte un mot court et une petite icône. Certaines cartes encore en tas au centre, en attente de tri. Style sobre et clair, lumière douce, rendu net. Rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

### TR29 — Cartes d'erreurs

*Carte R29 · famille III (Cartes et jeux) · exemple illustré : 6P · cycle 2 · ~10 ans · mathématiques.*

**Verso de la carte.** Résolutions erronées à analyser pour comprendre une erreur fréquente. Fonctions (Tricot, 2020) : 9 Résoudre des problèmes et calculer ; 15 Évaluer, s'autoévaluer, suivre les progrès.

**Pour une bonne utilisation.**

- Partir d'erreurs réellement fréquentes, puis montrer la démarche correcte.

- Réserver ce format aux calculs et raisonnements : jamais de forme orthographique fautive.

- Faire expliquer l'erreur, pas seulement la corriger.

**Référentiel.** Classe IV ; fonctions F18, F19, F42 ; patrons, micro-formats, gabarits : P04 (mathématiques) ; J14 ; procédure : Livre I (J14).

**Signature visuelle.** Trois cartes rigides portant chacune une soustraction en colonnes fausse, avec la question « Où est l'erreur ? » ; une carte retournée montre la démarche correcte. L'erreur est le matériau d'étude. Au premier regard : « ce calcul est faux, je cherche pourquoi ».

**Texte à intégrer (surimpression).** Carte 1 : « 52 − 17 = 45 » (erreur : 7 − 2 au lieu d'emprunter). Carte 2 : « 300 − 48 = 352 » (erreur : addition). Carte 3 : « 64 − 29 = 45 » (erreur : retenue oubliée). Sur chaque carte : « Où est l'erreur ? Explique-la. » Verso visible : « La bonne démarche : … ».

**Prompt d'image.** Vue de dessus, sur une table claire en bois pâle, de trois cartes rigides de même format pour élèves de ~10 ans, chacune portant une soustraction posée en colonnes au feutre, chiffres flous, et une petite ligne de question ; une quatrième carte retournée montre une résolution en colonnes avec une retenue entourée. Un crayon et une loupe d'écolier posés à côté. Aucune main. Couleurs neutres avec un seul accent coloré. Lumière douce et homogène, rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

**Vigilance.** Les calculs sont posés en surimpression : la génération ne produit jamais une erreur « contrôlée ». Règle de la carte R29 : jamais de forme orthographique fautive, uniquement des calculs. Trois cartes, une seule retournée.

**Version primaire.** Illustration et exemple remplacés le 1er novembre 2026 pour situer la carte au primaire ; la version secondaire est conservée hors de cette bibliothèque, pour le futur Catalogue Ressources au secondaire.

### TR30 — Cartes d'aide graduée

*Carte R30 · famille III (Cartes et jeux) · exemple illustré : 7P · cycle 2 · ~11 ans · mathématiques.*

**Verso de la carte.** Coups de pouce numérotés, du plus ouvert au plus guidé, pour avancer seul·e. Fonctions (Tricot, 2020) : 7 Poser des questions, demander de l'aide ; 9 Résoudre des problèmes et calculer.

**Pour une bonne utilisation.**

- Graduer de l'indice le plus ouvert au plus fermé.

- Rendre l'aide facile à prendre : les élèves qui en ont le plus besoin la demandent le moins bien (T).

- Noter quelle aide a été utilisée, pour suivre les progrès.

**Référentiel.** Classe I ou IV ; fonctions F22, F23, F24 ; patrons, micro-formats, gabarits : P15 ; MP-D (§ 3.6) ; J15 ; procédure : Livre I (J15).

**Signature visuelle.** Petites cartes numérotées « coup de pouce 1 / 2 / 3 » empilées ou en éventail, de la plus ouverte à la plus fermée. Au premier regard : « des aides progressives ».

**Texte à intégrer (surimpression).** Sur les cartes : « Coup de pouce 1 : que cherche-t-on ? » « Coup de pouce 2 : fais un schéma. » « Coup de pouce 3 : quelle opération ? ». Étiquette : « Aides — problèmes ».

**Prompt d'image.** Vue de dessus de petites cartes d'aide graduée (~10-11 ans) disposées en éventail sur table claire, numérotées « coup de pouce 1, 2, 3 » avec des amorces courtes. Codes couleur du plus clair au plus foncé qui doublent la gradation portée par les numéros. À côté, une fiche de problème générique. Style sobre, lumière douce, rendu net. Rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

**Ajustement v6.2.** Les numéros portent la gradation ; la couleur ne fait que la doubler (X-08).

### TR31 — Cartes de rappel et reprises espacées

*Carte R31 · famille III (Cartes et jeux) · exemple illustré : 7P · cycle 2 · ~11 ans · allemand.*

**Verso de la carte.** Cartes question-réponse pour se tester et revenir plus tard sur les mêmes notions. Fonctions (Tricot, 2020) : 24 Mémoriser, apprendre par cœur ; 10 S'entraîner.

**Pour une bonne utilisation.**

- Se tester avant de retourner la carte.

- Planifier les reprises dans le temps, sur un calendrier.

- Travailler par petites séries.

**Par exemple avec.** Digiflashcards (ladigitale.dev) · Anki (apps.ankiweb.net) · Quizlet (quizlet.com).

**Référentiel.** Classe IV ; fonctions F28, F29 ; patrons, micro-formats, gabarits : P14, MF18, MF43 ; procédure : Livre I (J4).

**Signature visuelle.** Petit paquet de cartes recto-verso, une carte retournée montrant la réponse, les autres empilées ou étalées ; à côté, un calendrier de reprises avec quelques cases cochées. Au premier regard : « je me teste, puis je reviens plus tard ».

**Texte à intégrer (surimpression).** Sur la carte visible, recto : « der Schlüssel » ; verso de la carte retournée : « la clé ». Sur le calendrier : « reprise 1 · reprise 2 · reprise 3 » avec deux cases cochées. Mention discrète : « essaie de retrouver avant de retourner ».

**Prompt d'image.** Vue de dessus, à plat, d'un petit jeu de cartes de rappel de vocabulaire allemand pour élèves de ~11 ans, sur une table claire en bois pâle. Une dizaine de cartes rectangulaires de format carte de visite, une retournée montrant sa réponse, les autres légèrement étalées ; à droite, une petite fiche de suivi avec des cases de reprise, dont deux cochées au crayon. Typographie simple et lisible, couleurs neutres avec un seul accent coloré. Lumière douce et homogène, rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

### TR32 — Roue à fenêtre et rabat

*Carte R32 · famille III (Cartes et jeux) · exemple illustré : 3P · cycle 1 · ~7 ans · sciences de la nature.*

**Verso de la carte.** Deux disques superposés : on tourne, on répond, on soulève le rabat pour vérifier. Fonctions (Tricot, 2020) : 10 S'entraîner ; 15 Évaluer, s'autoévaluer, suivre les progrès.

**Pour une bonne utilisation.**

- Placer la réponse sous le rabat pour une correction immédiate.

- Choisir un contenu cyclique ou séquentiel, qui se prête à la roue.

- Montrer la manipulation et tester le montage avant la classe.

**Référentiel.** Classe IV ; fonctions F27, F29 ; patrons, micro-formats, gabarits : MF39 ; J11 ; procédure : Livre I (J11, R11).

**Signature visuelle.** Deux disques en carton superposés, réunis au centre par une attache parisienne ; le disque du dessus porte une fenêtre découpée et un petit rabat soulevable. En tournant, une nouvelle étape apparaît dans la fenêtre ; la réponse se cache sous le rabat. Au premier regard : « je tourne, je réponds, je soulève pour vérifier ».

**Texte à intégrer (surimpression).** Titre sur le disque du dessus : « La roue de la grenouille ». Question : « Qu'est-ce qui vient après ? ». Dans la fenêtre : « le têtard ». Sous le rabat soulevé : « le têtard avec des pattes ». Sur la couronne visible : « 1 · 2 · 3 · 4 ». Mention : « Soulève pour vérifier ».

**Prompt d'image.** Vue de dessus d'une roue pédagogique en carton fort pour élèves de ~7 ans, posée sur une table claire en bois pâle : deux disques superposés, le plus grand dépassant en couronne divisée en quatre secteurs numérotés, réunis au centre par une attache parisienne métallique. Le disque du dessus présente une fenêtre rectangulaire découpée près du bord, avec une petite illustration simple de têtard visible à travers, et à côté un petit rabat en carton légèrement soulevé. Une paire de ciseaux à bouts ronds et quelques chutes de carton posées à côté. Couleurs sobres, un seul accent vert. Lumière douce et homogène, rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

**Vigilance.** La génération représente mal les mécanismes : vérifier que l'attache est au centre commun des deux disques et que la fenêtre se trouve au-dessus du disque inférieur. Le cycle (œufs → têtard → têtard avec des pattes → grenouille) se referme : un bon exemple d'affinité entre une roue et un contenu cyclique.

### TR33 — Loto

*Carte R33 · famille III (Cartes et jeux) · exemple illustré : 5P · cycle 2 · ~9 ans · allemand (langue étrangère).*

**Verso de la carte.** Cartons illustrés : on entend un mot, on couvre l'image. Fonctions (Tricot, 2020) : 11 Jouer ; 3 Écouter un document sonore ; 24 Mémoriser, apprendre par cœur.

**Pour une bonne utilisation.**

- Répartir chaque élément sur un nombre défini de cartons.

- Annoncer clairement et répéter.

- Réutiliser le vocabulaire après la partie.

**Référentiel.** Classe IV ; fonctions F27, F29 ; patrons, micro-formats, gabarits : MF39 ; J7 ; procédure : Livre I (J7).

**Signature visuelle.** Cartons de jeu quadrillés (3 × 3) illustrés, une pile de cartes d'appel portant les mots, des jetons posés sur certaines cases. Au premier regard : « j'entends un mot, je couvre l'image ».

**Texte à intégrer (surimpression).** Titre : « Tier-Lotto ». Cartes d'appel visibles : « der Hund », « die Katze », « das Pferd », « die Kuh », « der Vogel », « das Schwein ». Mention : « Hör gut zu! ».

**Prompt d'image.** Vue de dessus de deux cartons de loto en carton épais pour élèves de ~9 ans sur une table claire en bois pâle : grilles de 3 × 3 cases avec des illustrations simples d'animaux de la ferme et de compagnie, quelques jetons ronds colorés posés sur des cases ; au-dessus, une petite pile de cartes d'appel, dont une retournée porte un mot. Graphisme simple et lisible, couleurs vives mais sobres. Lumière douce et homogène, rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

**Vigilance.** Un même animal ne doit pas figurer deux fois sur un carton ; les deux cartons ne doivent pas être identiques.

### TR34 — Dé pédagogique

*Carte R34 · famille III (Cartes et jeux) · exemple illustré : 4P · cycle 1 · ~8 ans · français (production orale).*

**Verso de la carte.** Dé dont chaque face porte une consigne ou un élément à utiliser. Fonctions (Tricot, 2020) : 11 Jouer ; 10 S'entraîner.

**Pour une bonne utilisation.**

- Lier chaque face à l'objectif.

- Une règle simple, expliquée par l'exemple.

- Tester le patron et le montage avant la classe.

**Référentiel.** Classe IV ; fonctions F31, F33 ; patrons, micro-formats, gabarits : J6 ; procédure : Livre I (J6).

**Signature visuelle.** Un dé en carton monté, posé à côté de son patron en croix et d'une consigne courte ; une illustration différente sur chaque face. Au premier regard : « je lance, je raconte ».

**Texte à intégrer (surimpression).** Titre : « Le dé des histoires ». Faces : « un renard · une fée · un pirate · une souris · un robot · une sorcière ». Consigne : « Lance le dé et commence ton histoire ! ».

**Prompt d'image.** Vue de dessus, sur une table claire en bois pâle, d'un grand dé en carton monté pour élèves de ~8 ans, montrant trois faces illustrées simplement (un renard, une fée, un pirate) ; à côté, une feuille portant le patron du dé à plat en forme de croix, six carrés illustrés avec languettes de collage, et une paire de ciseaux à bouts ronds avec de petites chutes de papier. Aucune main. Couleurs sobres, un seul accent coloré. Lumière douce et homogène, rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

**Vigilance.** Le patron doit compter exactement six faces en croix, sans doublon. Trois faces visibles au maximum sur le dé monté, et elles doivent correspondre à celles du patron.

### TR35 — Jeu de l'oie pédagogique

*Carte R35 · famille III (Cartes et jeux) · exemple illustré : 5P · cycle 2 · ~9 ans · français.*

**Verso de la carte.** Parcours de cases numérotées, dont certaines posent une question ou une consigne. Fonctions (Tricot, 2020) : 11 Jouer ; 10 S'entraîner.

**Pour une bonne utilisation.**

- Lier les cases-questions à l'objectif, pas seulement au hasard du dé.

- Prévoir une fiche-réponses pour trancher sans l'enseignant·e (retour immédiat) (T).

- Terminer par un débriefing sur les questions ratées (T).

**Référentiel.** Classe IV ; fonctions F01, F27, F28 ; patrons, micro-formats, gabarits : P14 ; procédure : Livre I (J5).

**Signature visuelle.** Plateau en spirale à cases numérotées, un dé et des pions ; certaines cases portent une petite question ou consigne. Au premier regard : « on avance de case en case ».

**Texte à intégrer (surimpression).** Titre du plateau : « La course des verbes ». Cases : « Conjugue « aller » au présent », « Avance de 2 », « Passé composé de « faire » ? », « Rejoue ». Départ et Arrivée marqués.

**Prompt d'image.** Vue de dessus d'un plateau de jeu de l'oie pédagogique (~9 ans) sur table claire : parcours en spirale de cases numérotées, quelques cases avec une consigne courte de conjugaison, un dé en bois et deux ou trois pions colorés. Graphisme ludique et lisible, couleurs vives mais sobres, lumière douce, rendu net. Rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

### TR36 — Jeu de plateau pédagogique

*Carte R36 · famille III (Cartes et jeux) · exemple illustré : 6P · cycle 2 · ~10 ans · sciences de la nature.*

**Verso de la carte.** Plateau thématique avec chemins, zones et cartes-défis à piocher. Fonctions (Tricot, 2020) : 11 Jouer ; 13 Coopérer.

**Pour une bonne utilisation.**

- Faire en sorte que la stratégie gagnante mobilise la notion.

- Limiter les règles qui n'apportent rien à l'apprentissage (T).

- Prévoir un débriefing : il fait partie des conditions d'efficacité du jeu (T).

**Référentiel.** Classe IV ; fonctions F29, F30, F34 ; patrons, micro-formats, gabarits : P08 ; procédure : Livre I (J5).

**Signature visuelle.** Plateau thématique « le voyage d'une goutte d'eau » : chemin qui monte vers un nuage, redescend en pluie sur une montagne, suit une rivière jusqu'au lac ; cases-défis et paquet de cartes. Au premier regard : « on avance en suivant le cycle de l'eau ».

**Texte à intégrer (surimpression).** Titre du plateau : « Le voyage de la goutte ». Zones : « Lac · Nuage · Montagne · Rivière ». Cases-défis : « Défi : explique l'évaporation » · « Défi : nomme un état de l'eau ». Cartes : « DÉFI ». Pions : goutte en bois.

**Prompt d'image.** Vue de dessus d'un plateau de jeu en carton épais posé sur une table claire en bois pâle, pour élèves de ~10 ans : parcours de cases qui dessine une boucle entre un lac en bas, un nuage en haut, une montagne et une rivière, quelques cases marquées d'un pictogramme de défi, un paquet de cartes posé dans un coin, deux pions en bois en forme de goutte et un dé. Illustration plate et simple. Aucune main. Couleurs douces, un seul accent coloré. Lumière douce et homogène, rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

**Vigilance.** Le parcours doit former une boucle fermée et lisible ; textes posés en surimpression. Pas de personnages ni de mascotte. Deux pions, un dé à six faces cohérent.

**Version primaire.** Illustration et exemple remplacés le 1er novembre 2026 pour situer la carte au primaire ; la version secondaire est conservée hors de cette bibliothèque, pour le futur Catalogue Ressources au secondaire.

### TR37 — Escape game pédagogique

*Carte R37 · famille III (Cartes et jeux) · exemple illustré : 7P · cycle 2 · ~11 ans · mathématiques.*

**Verso de la carte.** Suite d'énigmes à résoudre en équipe pour « sortir » ou ouvrir un coffre. Fonctions (Tricot, 2020) : 11 Jouer ; 13 Coopérer ; 9 Résoudre des problèmes et calculer.

**Pour une bonne utilisation.**

- Lier chaque énigme à l'objectif d'apprentissage.

- De petits groupes, avec des rôles (T).

- Un débriefing obligatoire : il fait partie des conditions d'efficacité (T).

**Référentiel.** Classe IV ; fonctions F04, F30, F34 ; patrons, micro-formats, gabarits : P10, MF64 ; GF-X ; J13 ; procédure : Livre I (GF-X).

**Signature visuelle.** Coffret fermé par un cadenas à trois chiffres, enveloppes numérotées et feuille de mission ; chaque énigme réussie livre un chiffre du code. Au premier regard : « on résout, on trouve le code, on ouvre ».

**Texte à intégrer (surimpression).** Titre : « Le coffre du professeur Tic ». Enveloppes : « Énigme 1 : 8 × 3 − 20 = ? · Énigme 2 : la moitié de 14 = ? · Énigme 3 : 40 % de 5 = ? ». Feuille : « Code : _ _ _ » et « 20 minutes ». Solution pour l'enseignant·e : 4 – 7 – 2.

**Prompt d'image.** Vue de dessus, sur une table claire en bois pâle, d'un petit coffret en bois fermé par un cadenas à trois molettes, pour élèves de ~11 ans ; autour, trois enveloppes kraft numérotées 1, 2, 3, une feuille de mission avec trois cases vides pour le code, un petit sablier et un crayon. Ambiance de jeu sobre, sans décor de film. Aucune main. Couleurs neutres avec un seul accent coloré. Lumière douce et homogène, rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

**Vigilance.** Le code ne doit apparaître nulle part sur l'image, et les molettes ne doivent pas afficher 4-7-2. Cadenas sans marque. Une seule solution par énigme, pour que le code soit unique.

### TR38 — Matériel de manipulation mathématique

*Carte R38 · famille IV (Matériel, objets et terrain) · exemple illustré : 3P · cycle 1 · ~7 ans · mathématiques.*

**Verso de la carte.** Objets à manipuler (cubes, réglettes, jetons) pour comprendre une notion mathématique. Fonctions (Tricot, 2020) : 9 Résoudre des problèmes et calculer ; 20 Découvrir des concepts abstraits.

**Pour une bonne utilisation.**

- Manipuler, puis représenter, puis écrire avec des symboles.

- Faire verbaliser ce que l'on fait.

- Retirer progressivement le matériel.

**Référentiel.** Classe IV ; fonctions F09, F17 ; patrons, micro-formats, gabarits : MF37 ; G12-b ; procédure : tapis : Livre I (G12-b) ; matériel : hors production.

**Signature visuelle.** Tapis de numération à deux colonnes, barres de dix et petits cubes réellement disposés dessus, avec une étiquette-nombre. Le nombre se construit par la main avant de s'écrire. Au premier regard : « je construis le nombre ».

**Texte à intégrer (surimpression).** Titre : « Je construis 34 ». Colonnes : « dizaines · unités ». Sous les colonnes : « 3 · 4 ». Phrase : « 34, c'est 3 dizaines et 4 unités. »

**Prompt d'image.** Vue de dessus d'un tapis de numération en carton sur une table claire en bois pâle, pour élèves de ~7 ans : deux colonnes bien séparées ; dans la colonne de gauche, exactement trois barres en bois de dix cubes soudés, dans la colonne de droite, exactement quatre petits cubes isolés. Une étiquette portant un nombre posée en haut. Une petite boîte de cubes supplémentaires dans un coin. Aucune main. Couleurs neutres avec un seul accent coloré. Lumière douce et homogène, rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

**Vigilance.** À compter sur l'image : trois barres, dix segments par barre, quatre cubes, et aucun cube isolé dans la mauvaise colonne. Constat du 31.10.2026 : la génération a produit des barres de neuf segments, malgré la consigne ; le dixième a été ajouté par retouche.

### TR39 — Objet fabriqué (FabLearn, 3D)

*Carte R39 · famille IV (Matériel, objets et terrain) · exemple illustré : 3P · cycle 1 · ~7 ans · mathématiques.*

**Verso de la carte.** Objet conçu et fabriqué par l'enseignant·e (découpe laser, impression 3D) pour manipuler une notion. Fonctions (Tricot, 2020) : 20 Découvrir des concepts abstraits ; 10 S'entraîner.

**Pour une bonne utilisation.**

- Partir du besoin d'apprentissage, prototyper, tester avec des élèves, ajuster.

- Robuste, manipulable à deux mains, sans petite pièce détachable.

- Faire verbaliser ce que l'objet montre, puis passer à l'écriture symbolique.

**Référentiel.** Classe IV ; fonctions F09, F17, F27 ; patrons, micro-formats, gabarits : MF37 ; GF-O ; procédure : objet : hors production ; fiche d'accompagnement : Livre I (GF-O) ; décision automatique du 2 novembre 2026, réversible.

**Signature visuelle.** Horloge d'apprentissage en bois clair découpée au laser, aiguilles mobiles, posée à côté d'une petite fiche « Il est \_\_ h \_\_ » et d'une chute de bois gravée. L'objet porte encore la trace de sa fabrication. Au premier regard : « un objet fait pour nous, qu'on peut toucher ».

**Texte à intégrer (surimpression).** Sur l'horloge : chiffres 1 à 12 gravés, repères des minutes « 5 · 10 · 15… » en petit sur le pourtour. Fiche : « Il est \_\_\_ h \_\_\_ » et « Place les aiguilles sur 7 h 30 ».

**Prompt d'image.** Vue de dessus, sur une table claire en bois pâle, d'une horloge d'apprentissage ronde en contreplaqué clair découpé au laser pour élèves de ~7 ans : chiffres de 1 à 12 gravés, deux aiguilles en bois de longueurs différentes fixées par un rivet central, bord légèrement bruni par la découpe ; à côté, une petite fiche avec une ligne à compléter et une chute de bois portant la même gravure. Aucune main. Couleurs naturelles du bois avec un seul accent coloré. Lumière douce et homogène, rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

**Vigilance.** Douze chiffres dans l'ordre, deux aiguilles seulement, de longueurs différentes : à compter sur l'image (les cadrans générés sont souvent faux). Inspiré des productions d'étudiantes 2025-26 (montres en bois), sans reproduire une production identifiable.

### TR40 — Matériel d'expérimentation

*Carte R40 · famille IV (Matériel, objets et terrain) · exemple illustré : 6P · cycle 2 · ~10 ans · sciences de la nature.*

**Verso de la carte.** Kit de matériel simple pour mener une expérience, observer et conclure. Fonctions (Tricot, 2020) : 22 Expérimenter ; 9 Résoudre des problèmes et calculer.

**Pour une bonne utilisation.**

- Faire écrire une hypothèse avant de manipuler.

- Un protocole illustré en étapes ; matériel sûr et en quantité pour de petits groupes.

- Noter les observations, les comparer à l'hypothèse, conclure ensemble.

**Référentiel.** Classe IV ; fonctions F15, F17, F18 ; patrons, micro-formats, gabarits : P09, MF06, MF53 ; GF-O, GF-S ; procédure : matériel : hors production ; protocole : Livre I (GF-O, GF-S) ; décision automatique du 2 novembre 2026, réversible.

**Signature visuelle.** Bac transparent d'eau, objets du quotidien à tester et fiche de résultats à deux colonnes. Elle se distingue de la simulation (TR53) par le réel : on se mouille. Au premier regard : « je prédis, je teste, je note ».

**Texte à intégrer (surimpression).** Fiche : « Flotte ou coule ? » ; colonnes « Mon hypothèse · Ce que j'observe » ; lignes « bouchon · clé · bille · crayon ». Bas : « Ma conclusion : \_\_\_ ».

**Prompt d'image.** Vue de dessus, sur une table claire en bois pâle protégée d'un petit plateau, d'un bac transparent rempli d'eau pour élèves de ~10 ans, où un bouchon de liège flotte et une clé repose au fond ; à côté, une bille, un crayon, un chiffon et une fiche de résultats à deux colonnes avec quelques cases cochées (texte flou). Aucune main. Couleurs neutres avec un seul accent coloré. Lumière douce et homogène, rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

**Vigilance.** Cohérence physique : le bouchon flotte, la clé coule. Pas de verrerie de laboratoire ni de produit chimique : matériel de classe ordinaire. Résultats posés en surimpression.

### TR41 — Fiche-trace de sortie

*Carte R41 · famille IV (Matériel, objets et terrain) · exemple illustré : 5P · cycle 2 · ~9 ans · sciences de la nature.*

**Verso de la carte.** Fiche d'observation utilisée sur le terrain (sortie, visite). Fonctions (Tricot, 2020) : 8 Rechercher de l'information ; 22 Expérimenter.

**Pour une bonne utilisation.**

- Des rubriques d'observation précises.

- Une place pour le dessin d'observation.

- Exploiter la fiche en classe au retour.

**Référentiel.** Classe sorties, hors classe ; fonctions F12, F37 ; patrons, micro-formats, gabarits : MF05, MF52 ; GF-S ; procédure : Livre I (GF-S).

**Signature visuelle.** Fiche fixée sur une planchette, posée dehors avec une loupe et quelques éléments ramassés. Elle prépare et garde la trace d'une expérience que l'IA ne remplace pas. Au premier regard : « je suis dehors, j'observe, je note ».

**Texte à intégrer (surimpression).** Titre : « Ma sortie en forêt ». Champs : « Lieu : ________ Date : ________ ». Rubriques : « Je dessine ce que j'observe · Ce que j'ai trouvé : ________ · Une question que je me pose : ________ ».

**Prompt d'image.** Vue de dessus d'une planchette à pince posée sur un banc de bois clair en forêt, lumière douce de sous-bois, pour élèves de ~9 ans : une fiche d'observation à deux zones (grand cadre de dessin, lignes d'écriture), une loupe d'écolier, un crayon, deux feuilles d'arbre et une pomme de pin. Fond de mousse et de feuilles légèrement flou. Aucune personne. Couleurs naturelles, un seul accent coloré sur la fiche. Lumière douce et homogène, rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

**Vigilance.** Seule carte en extérieur de la série : garder le cadre clair et la vue de dessus pour rester cohérent. Feuilles d'espèces locales plausibles, à vérifier si la carte sert à identifier.

### TR42 — Comptine ou chanson

*Carte R42 · famille V (Audio, vidéo et numérique) · exemple illustré : 2P · cycle 1 · ~6 ans · musique et français (oral).*

**Verso de la carte.** Texte rythmé à dire ou à chanter, souvent avec des gestes. Fonctions (Tricot, 2020) : 24 Mémoriser, apprendre par cœur ; 12 Motiver ; 3 Écouter un document sonore.

**Pour une bonne utilisation.**

- Choisir un texte traditionnel ou original (droits d'auteur).

- Associer des gestes au texte.

- Répéter sur plusieurs jours.

**Référentiel.** Classe II ; fonctions F01, F29 ; patrons, micro-formats, gabarits : MF38, MF39 ; TC41 ; carte imprimée : G10 ; procédure : Partie 8 ; carte imprimée : Livre I.

**Signature visuelle.** Grande carte plastifiée portant une comptine courte, une image par vers et un petit picto de geste à faire ; à côté, un lecteur audio simple pour écouter le modèle. La mémorisation passe par la voix, l'image et le geste. Au premier regard : « j'écoute, je chante, je montre ».

**Texte à intégrer (surimpression).** Titre : « Je compte en chantant ». Texte de la comptine (écrite pour cette carte) : « Un, deux, trois, un petit pois. · Quatre, cinq, six, une cerise. · Sept, huit, neuf, un gros œuf. · Dix, c'est fini, je dis merci ! ». Mention : « Écoute · Chante · Montre ».

**Prompt d'image.** Vue de dessus d'une grande carte plastifiée sur une table claire en bois pâle, pour enfants de ~6 ans : quatre bandes horizontales de même hauteur, chacune avec une illustration simple à gauche (un pois vert, une cerise, un œuf, une étoile) et une zone de texte à droite. Texte discret ou flou. À côté de la carte, un petit lecteur audio sans marque, à gros bouton, et deux bâtonnets de rythme en bois. Graphisme épuré, couleurs douces, un seul accent coloré. Lumière douce et homogène, rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

**Vigilance.** Le texte est original pour éviter tout droit sur une comptine publiée ; il s'inspire seulement du schéma traditionnel des comptines à compter. À faire relire pour le rythme et à tester à voix haute. Pas de partition générée : la notation musicale est presque toujours fausse. Les gestes viennent en surimpression (banque IC), pas de la génération.

### TR43 — Capsule audio

*Carte R43 · famille V (Audio, vidéo et numérique) · exemple illustré : 5P · cycle 2 · ~9 ans · allemand (compréhension orale).*

**Verso de la carte.** Enregistrement court à écouter à son rythme. Fonctions (Tricot, 2020) : 3 Écouter un document sonore.

**Pour une bonne utilisation.**

- Garder la capsule courte et segmentée : un long audio complexe se comprend mal (T).

- Permettre de mettre en pause et de réécouter.

- Donner une tâche d'écoute précise avant l'écoute.

**Par exemple avec.** Digirecord (ladigitale.dev) · Audacity (audacityteam.org) · Dictaphone de l'iPad.

**Référentiel.** Classe II ; fonctions F08, F09, F12 ; patrons, micro-formats, gabarits : MF05, MF56 ; TC42 ; procédure : Partie 8.

**Signature visuelle.** Petit lecteur audio sans marque à gros boutons, casque d'enfant, et fiche d'écoute illustrée où l'on coche les animaux entendus. L'audio est court et la tâche d'écoute est donnée avant. Au premier regard : « j'écoute, je coche ».

**Texte à intégrer (surimpression).** Lecteur : « Im Zoo — 1:30 » ; chapitres « 1 · 2 · 3 ». Fiche : « Ich höre… » suivi de six pictogrammes d'animaux avec cases à cocher : « der Elefant · der Löwe · der Affe · die Giraffe · das Zebra · der Vogel ». Consigne : « Écoute deux fois. Coche ce que tu entends. »

**Prompt d'image.** Vue de dessus, sur une table claire en bois pâle, d'un petit lecteur audio sans marque à gros boutons et écran minimal, d'un casque audio filaire pour enfant, et d'une fiche A5 avec six pictogrammes simples d'animaux alignés en deux rangées, chacun avec une case à cocher ; un crayon. Aucune main. Couleurs neutres avec un seul accent coloré. Lumière douce et homogène, rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

**Vigilance.** Mots allemands posés en surimpression. Six animaux distincts et reconnaissables (banque IC si la génération hésite). Pas de smartphone de marque.

**Version primaire.** Illustration et exemple remplacés le 1er novembre 2026 pour situer la carte au primaire ; la version secondaire est conservée hors de cette bibliothèque, pour le futur Catalogue Ressources au secondaire.

### TR44 — Capsule vidéo ou tutoriel

*Carte R44 · famille V (Audio, vidéo et numérique) · exemple illustré : 6P · cycle 2 · ~10 ans · mathématiques (géométrie).*

**Verso de la carte.** Vidéo courte qui montre une procédure, un geste ou une notion. Fonctions (Tricot, 2020) : 5 Regarder une vidéo, une animation.

**Pour une bonne utilisation.**

- Courte et segmentée, avec un commentaire oral plutôt qu'écrit (T).

- La réserver à ce qui se montre mieux en mouvement : gestes, procédures (T).

- Donner une tâche pendant le visionnage : regarder passivement apprend peu (T).

**Par exemple avec.** Digiview et Digicut (ladigitale.dev) · Keynote ou PowerPoint · Enregistrement d'écran de l'iPad ou du Mac.

**Référentiel.** Classe II ; fonctions F09, F11 ; patrons, micro-formats, gabarits : TC43 ; procédure : Partie 8.

**Signature visuelle.** Tablette affichant un lecteur vidéo générique au format paysage : une image de démonstration, une barre de lecture découpée en trois chapitres et un point de pause marqué ; à côté, le matériel pour refaire le geste. Elle se distingue de la capsule audio (TR43) par l'image animée, les chapitres et l'invitation à s'arrêter pour essayer. Au premier regard : « je regarde, je mets en pause, j'essaie ».

**Texte à intégrer (surimpression).** À l'écran : titre « Comment tracer un cercle au compas (3 min) ». Chapitres : « 1. J'observe · 2. J'essaie · 3. Je vérifie ». Repère de pause à 1:20 avec la mention : « Mets en pause et essaie ! ». Barre de lecture à 1:20 sur 3:00.

**Prompt d'image.** Vue de dessus d'une tablette posée à plat sur une table claire en bois pâle, affichant un lecteur vidéo générique pour élèves de ~10 ans : image de démonstration montrant un compas ouvert et un cercle tracé sur une feuille, barre de lecture à trois segments et petit repère de pause. À côté de la tablette, un compas d'écolier, un crayon et une feuille portant un cercle tracé. Interface neutre et inventée, aucune main visible. Couleurs neutres avec un seul accent coloré. Lumière douce et homogène, rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

**Vigilance.** Aucune interface reconnaissable (pas de plateforme vidéo ni de bouton copié). Le compas doit avoir une pointe et une mine cohérentes ; le cercle doit être fermé. Ne pas faire générer de main tenant le compas.

### TR45 — Diaporama projeté

*Carte R45 · famille V (Audio, vidéo et numérique) · exemple illustré : 6P · cycle 2 · ~10 ans · sciences de la nature.*

**Verso de la carte.** Suite de diapositives projetées, une idée par écran, pour présenter ou structurer une leçon. Fonctions (Tricot, 2020) : 1 Présenter de l'information ; 4 Regarder, lire un document multimédia.

**Pour une bonne utilisation.**

- Une idée par diapositive, mot-clé et image proches, aucun détail décoratif (T).

- Commenter à l'oral plutôt que faire lire du texte à l'écran (T).

- Prévoir ce que font les élèves pendant la projection : question, schéma à compléter.

**Par exemple avec.** Digislides (ladigitale.dev) · Keynote · PowerPoint.

**Référentiel.** Classe II ; fonctions F08, F09, F10 ; patrons, micro-formats, gabarits : MF02 ; TC44 ; procédure : Partie 8 ; décision automatique du 2 novembre 2026, réversible.

**Signature visuelle.** Ordinateur portable affichant une diapositive très épurée (un titre, une image, trois mots), avec à côté la feuille que les élèves complètent pendant la projection. Elle se distingue de la capsule vidéo (TR44) : ici, c'est l'enseignant·e qui parle. Au premier regard : « une image, trois mots, et j'écoute ».

**Texte à intégrer (surimpression).** Diapositive : titre « Les trois états de l'eau » ; trois pictogrammes « glace · eau · vapeur » ; en bas « 3 / 8 ». Feuille élève : « Pendant la présentation, je complète : l'eau devient de la glace quand \_\_\_\_\_\_\_\_ ».

**Prompt d'image.** Vue de dessus en légère plongée d'un ordinateur portable neutre ouvert sur une table claire en bois pâle, écran affichant une diapositive épurée pour élèves de ~10 ans : fond clair, un titre, trois pictogrammes simples alignés (glaçon, goutte, nuage de vapeur), un petit numéro de page ; à côté, une feuille de prise de notes avec une ligne à compléter et un crayon. Interface inventée, aucun logiciel reconnaissable. Couleurs neutres avec un seul accent coloré. Lumière douce et homogène, rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

**Vigilance.** Aucune interface de logiciel de présentation réelle (barres d'outils, vignettes). La diapositive doit rester vide de paragraphe : le défaut probable est un écran surchargé. Ordinateur sans marque.

### TR46 — Tableau interactif ou écran tactile

*Carte R46 · famille V (Audio, vidéo et numérique) · exemple illustré : 3P · cycle 1 · ~7 ans · mathématiques.*

**Verso de la carte.** Grand écran tactile où la classe manipule ensemble des objets, écrit et déplace. Fonctions (Tricot, 2020) : 13 Coopérer ; 9 Résoudre des problèmes et calculer.

**Pour une bonne utilisation.**

- Faire venir les élèves manipuler à l'écran, pas seulement regarder l'enseignant·e.

- Garder une trace (capture) de ce qui a été construit collectivement.

- Alterner avec le matériel réel : l'écran ne remplace pas la manipulation (voir R38).

**Par exemple avec.** OpenBoard (openboard.ch).

**Référentiel.** Classe III ; fonctions F17, F30, F34 ; patrons, micro-formats, gabarits : TC45 ; procédure : équipement : hors production ; contenus : Partie 8 ; décision automatique du 2 novembre 2026, réversible.

**Signature visuelle.** Grand écran de classe vu de face, affichant des jetons à regrouper par dix et un cadre de réponse ; au pied de l'écran, un bac de jetons réels. C'est la seule carte vue de face : l'écran est un objet vertical. Au premier regard : « on manipule ensemble, en grand ».

**Texte à intégrer (surimpression).** Écran : « Groupe les jetons par 10 » ; « Combien de dizaines ? \_\_\_ Combien d'unités ? \_\_\_ ». Un groupe de dix déjà entouré.

**Prompt d'image.** Vue de face d'un grand écran tactile de classe fixé sur un mur clair, pour élèves de ~7 ans, affichant une interface inventée très simple : une vingtaine de jetons ronds dispersés, dont dix entourés d'un trait, et deux cases de réponse vides ; en dessous, un petit meuble bas avec un bac de jetons réels de la même couleur. Aucune personne, aucune main. Écran sans marque. Couleurs neutres avec un seul accent coloré. Lumière douce et homogène, rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

**Vigilance.** Écart assumé au socle : vue de face (comme TR41 est en extérieur). Aucune marque d'écran ni logiciel reconnaissable. Compter les jetons à l'écran : exactement dix dans le cercle.

### TR47 — Quiz interactif

*Carte R47 · famille V (Audio, vidéo et numérique) · exemple illustré : 6P · cycle 2 · ~10 ans · géographie (SHS).*

**Verso de la carte.** Questions à choix multiple à l'écran, avec score et progression. Fonctions (Tricot, 2020) : 15 Évaluer, s'autoévaluer, suivre les progrès ; 12 Motiver.

**Pour une bonne utilisation.**

- Afficher une explication après chaque réponse : le simple juste ou faux aide peu (T).

- Viser l'essentiel de la notion, pas des détails piégeux.

- Le plaisir de jouer ne garantit pas l'apprentissage : vérifier ce qui est retenu (T).

**Par exemple avec.** Digistorm (ladigitale.dev) · LearningApps (learningapps.org) · Kahoot (kahoot.com).

**Référentiel.** Classe III ; fonctions F01, F29, F36 ; patrons, micro-formats, gabarits : MF16, MF17 ; version papier : G6 ; TC46 ; procédure : Partie 8.

**Signature visuelle.** Tablette affichant une question à quatre choix, la bonne réponse validée et, surtout, une courte explication sous la réponse ; barre de progression et score discret. Au premier regard : « je réponds et on m'explique pourquoi ».

**Texte à intégrer (surimpression).** Question : « Quel est le plus grand océan du monde ? » Choix : « Pacifique · Atlantique · Indien · Arctique ». Réponse validée : « Pacifique ». Explication : « Il couvre environ un tiers de la surface de la Terre. » Progression : « Question 4 / 10 ».

**Prompt d'image.** Vue de dessus d'une tablette posée à plat sur une table claire en bois pâle, affichant une interface de quiz inventée et sobre pour élèves de ~10 ans : une question courte, quatre boutons de réponse dont un marqué d'une coche, un encadré d'explication en dessous, une barre de progression fine ; à côté, un carnet fermé et un crayon. Interface neutre, aucune application reconnaissable. Aucune main. Couleurs neutres avec un seul accent coloré. Lumière douce et homogène, rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

**Vigilance.** Aucune interface réelle (Kahoot, LearningApps). Textes posés en surimpression. Pas de podium, de chronomètre agressif ni de confettis : la carte insiste sur l'explication, pas sur la compétition.

**Version primaire.** Illustration et exemple remplacés le 1er novembre 2026 pour situer la carte au primaire ; la version secondaire est conservée hors de cette bibliothèque, pour le futur Catalogue Ressources au secondaire.

### TR48 — Exerciseur numérique

*Carte R48 · famille V (Audio, vidéo et numérique) · exemple illustré : 7P · cycle 2 · ~11 ans · anglais (langue étrangère).*

**Verso de la carte.** Exercices à l'écran avec correction immédiate et série adaptée. Fonctions (Tricot, 2020) : 10 S'entraîner ; 15 Évaluer, s'autoévaluer, suivre les progrès.

**Pour une bonne utilisation.**

- Réserver aux compétences simples et bien définies, déjà en partie maîtrisées (T).

- Vérifier que le retour explique l'erreur (T).

- Fixer une durée courte et suivre les résultats.

**Par exemple avec.** LearningApps (learningapps.org) · Gomaths (gomaths.ch) · H5P via Digiquiz (h5p.org · ladigitale.dev).

**Référentiel.** Classe III ; fonctions F27, F28, F38 ; patrons, micro-formats, gabarits : MF57 ; TC47 ; procédure : Partie 8.

**Signature visuelle.** Écran montrant un exercice unique avec champ de saisie et retour immédiat générique (coche ou croix accompagnée d'un mot), interface neutre. Au premier regard : « on s'entraîne à l'écran avec correction immédiate ».

**Texte à intégrer (surimpression).** À l'écran : une image d'un chat assis sur une table, puis « Choose the right word: The cat is \_\_\_ the table. » Choix : « on · in · under ». Retour : « ✓ Well done! » Compteur : « 4/10 ».

**Prompt d'image.** Photographie d'un ordinateur portable ou d'une tablette sur table claire affichant un exerciseur d'anglais générique (~10-11 ans) : une petite image (un chat assis sur une table), une phrase à trou, des choix de réponse, un retour immédiat (une coche accompagnée d'un court message) et un compteur de série. Interface neutre et inventée, sans logo ni marque. Lumière douce, rendu net. Rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

**Ajustement v6.2.** Sans image, « on » et « under » étaient tous deux corrects : l'image fixe une seule réponse. Le retour associe symbole et message ; la couleur ne porte jamais seule l'information (X-08).

### TR49 — Activité interactive à l'écran

*Carte R49 · famille V (Audio, vidéo et numérique) · exemple illustré : 6P · cycle 2 · ~10 ans · allemand (langue étrangère).*

**Verso de la carte.** Contenu à l'écran où l'élève clique, glisse ou répond au fil de la lecture. Fonctions (Tricot, 2020) : 4 Regarder, lire un document multimédia ; 10 S'entraîner.

**Pour une bonne utilisation.**

- Chaque zone cliquable apporte une information utile, pas un effet.

- Retour immédiat qui explique après chaque réponse (T).

- Courte et centrée sur une notion ; prévoir ce qu'on fait après.

**Par exemple avec.** Digiquiz, H5P (ladigitale.dev · h5p.org) · Genially (genially.com) · LearningApps (learningapps.org).

**Référentiel.** Classe III ; fonctions F27, F36, F38 ; patrons, micro-formats, gabarits : MF16, MF17 ; TC48 ; procédure : Partie 8 ; décision automatique du 2 novembre 2026, réversible.

**Signature visuelle.** Tablette affichant une illustration de salle de classe parsemée de points cliquables, dont un ouvert montre un mot ; à côté, une liste de vocabulaire à cocher. Elle se distingue de l'exerciseur (TR48) par l'exploration d'une image, et du quiz (TR47) par l'absence de score. Au premier regard : « je touche, j'apprends le mot ».

**Texte à intégrer (surimpression).** Écran : titre « Im Klassenzimmer » ; bulle ouverte « die Tafel » ; points sur la chaise, la fenêtre, la porte. Liste papier : « der Stuhl · das Fenster · die Tür · die Tafel ☐ ».

**Prompt d'image.** Vue de dessus d'une tablette posée à plat sur une table claire en bois pâle, affichant une illustration plate et simple d'une salle de classe vide pour élèves de ~10 ans, avec quatre petits points ronds cliquables, dont un ouvert en bulle contenant un mot court flou ; à côté, une fiche de vocabulaire à cases à cocher et un crayon. Interface inventée. Aucune main. Couleurs neutres avec un seul accent coloré. Lumière douce et homogène, rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

**Vigilance.** Mots allemands posés en surimpression (le texte généré est faux). Aucun outil-auteur reconnaissable (H5P, Genially). Quatre points, un seul ouvert.

### TR50 — Récit interactif à embranchements

*Carte R50 · famille V (Audio, vidéo et numérique) · exemple illustré : 6P · cycle 2 · ~10 ans · français (lecture).*

**Verso de la carte.** Selon ses choix, le lecteur ou la lectrice suit un chemin différent dans l'histoire. Fonctions (Tricot, 2020) : 2 Lire et comprendre un texte, apprendre à lire ; 12 Motiver.

**Pour une bonne utilisation.**

- Rendre les choix signifiants pour l'objectif, pas seulement pour l'histoire.

- Garder une trace du chemin suivi.

- Discuter ensuite des choix et de leurs conséquences.

**Par exemple avec.** Twine (twinery.org) · Genially (genially.com) · Keynote ou PowerPoint avec liens.

**Référentiel.** Classe I (papier) ou III ; fonctions F01, F16, F30 ; patrons, micro-formats, gabarits : P02, MF11 ; TC49 ; procédure : Livre I (papier) ou Partie 8 (numérique).

**Signature visuelle.** Petit livret agrafé ouvert sur une page qui se termine par deux choix renvoyant à deux pages différentes ; à côté, une carte « mon chemin » où l'élève note les pages parcourues. Version papier, fabricable par l'enseignant·e. Au premier regard : « je choisis, je tourne à la bonne page ».

**Texte à intégrer (surimpression).** Titre du livret : « La forêt aux trois chemins ». Fin de page : « Si tu suis le renard, va à la page 7. · Si tu rentres au village, va à la page 12. » Carte : « Mon chemin : 1 → 4 → \_\_\_ → \_\_\_ ». Mention : « Récit écrit pour la classe ».

**Prompt d'image.** Vue de dessus, sur une table claire en bois pâle, d'un petit livret agrafé ouvert pour élèves de ~10 ans : page de gauche avec un court texte flou et une petite illustration de sentier en forêt, page de droite se terminant par deux encadrés de choix avec une flèche chacun ; à côté, une carte de suivi avec une ligne de numéros et un crayon. Aucun personnage reconnaissable. Aucune main. Couleurs douces, un seul accent coloré. Lumière douce et homogène, rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

**Vigilance.** Aucun livre ou collection réelle reconnaissable. Textes et numéros de page en surimpression. Deux choix exactement sur la page visible.

**Version primaire.** Illustration et exemple remplacés le 1er novembre 2026 pour situer la carte au primaire ; la version secondaire est conservée hors de cette bibliothèque, pour le futur Catalogue Ressources au secondaire.

### TR51 — Parcours numérique

*Carte R51 · famille V (Audio, vidéo et numérique) · exemple illustré : 8P · cycle 2 · ~12 ans · mathématiques (révision).*

**Verso de la carte.** Suite de modules en ligne à suivre étape par étape. Fonctions (Tricot, 2020) : 14 Apprendre à distance ; 10 S'entraîner.

**Pour une bonne utilisation.**

- Structurer très précisément le parcours : il exige beaucoup d'autonomie (T).

- Prévoir des points de contrôle avec l'enseignant·e.

- Garder des étapes courtes, chacune avec un objectif annoncé.

**Par exemple avec.** Digisteps (ladigitale.dev).

**Référentiel.** Classe III ou V ; fonctions F21, F22, F43 ; patrons, micro-formats, gabarits : MF43 ; TC50 ; procédure : Partie 8.

**Signature visuelle.** Tablette affichant un parcours de cinq étapes en ligne, deux déjà validées, la troisième ouverte ; une étape porte un pictogramme « point de contrôle avec l'enseignant·e ». À côté, une feuille de suivi. Au premier regard : « j'avance étape par étape, et on fait le point ».

**Texte à intégrer (surimpression).** Titre : « Mon parcours — Les fractions ». Étapes : « 1. Lire une fraction ✓ · 2. Représenter ✓ · 3. Comparer (en cours) · 4. Additionner · 5. Point de contrôle avec l'enseignant·e ». Feuille : « Étape terminée le : \_\_\_ · Ce que j'ai réussi : \_\_\_ ».

**Prompt d'image.** Vue de dessus d'une tablette posée à plat sur une table claire en bois pâle, affichant une interface inventée et sobre pour élèves de ~12 ans : un chemin vertical de cinq étapes reliées, deux marquées d'une coche, une mise en évidence, la dernière marquée d'un pictogramme de dialogue ; à côté, une feuille de suivi avec deux lignes et un crayon. Interface neutre, aucune plateforme reconnaissable. Aucune main. Couleurs neutres avec un seul accent coloré. Lumière douce et homogène, rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

**Vigilance.** Aucune interface de plateforme réelle (Moodle, etc.). Cinq étapes exactement ; textes en surimpression. Le point de contrôle humain doit être visible : c'est la condition-clé de la carte.

**Version primaire.** Illustration et exemple remplacés le 1er novembre 2026 pour situer la carte au primaire ; la version secondaire est conservée hors de cette bibliothèque, pour le futur Catalogue Ressources au secondaire.

### TR52 — Mur collaboratif numérique

*Carte R52 · famille V (Audio, vidéo et numérique) · exemple illustré : 7P · cycle 2 · ~11 ans · sciences de la nature.*

**Verso de la carte.** Espace partagé où chacun·e dépose des idées sous forme de vignettes. Fonctions (Tricot, 2020) : 13 Coopérer ; 21 Faire émerger des idées, créativité.

**Pour une bonne utilisation.**

- Proposer une tâche assez complexe pour justifier la collaboration (T).

- Former de petits groupes et donner une consigne de dépôt précise (T).

- Terminer par une synthèse collective.

**Par exemple avec.** Digipad (ladigitale.dev) · Padlet (padlet.com).

**Référentiel.** Classe V ; fonctions F33, F34, F35 ; patrons, micro-formats, gabarits : MF29 ; TC51 ; procédure : Partie 8.

**Signature visuelle.** Grand écran (ou tablette) montrant un mur de vignettes colorées regroupées en trois colonnes, chacune avec le prénom remplacé par un pictogramme d'équipe ; consigne de dépôt visible en haut. Au premier regard : « chaque équipe dépose, on voit tout d'un coup ».

**Texte à intégrer (surimpression).** Titre : « Ce que nous savons sur les volcans ». Colonnes : « Je sais · Je crois savoir · Je me demande ». Consigne : « Une idée par vignette, en une phrase ». Vignettes : textes courts flous ; étiquettes d'équipe « Équipe 1 · 2 · 3 ».

**Prompt d'image.** Vue de dessus d'une tablette posée à plat sur une table claire en bois pâle, affichant un mur collaboratif inventé pour élèves de ~11 ans : trois colonnes avec en-têtes courts, une douzaine de vignettes rectangulaires de deux teintes douces portant du texte flou, une barre de consigne en haut ; à côté, un petit carton « Équipe 2 » et un crayon. Interface neutre, aucune application reconnaissable. Aucune main. Couleurs neutres avec un seul accent coloré. Lumière douce et homogène, rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

**Vigilance.** Aucune interface réelle (Padlet, Digipad). Aucun prénom sur les vignettes. Trois colonnes exactement ; textes en surimpression.

**Version primaire.** Illustration et exemple remplacés le 1er novembre 2026 pour situer la carte au primaire ; la version secondaire est conservée hors de cette bibliothèque, pour le futur Catalogue Ressources au secondaire.

### TR53 — Simulation numérique

*Carte R53 · famille V (Audio, vidéo et numérique) · exemple illustré : 8P · cycle 2 · ~12 ans · sciences de la nature.*

**Verso de la carte.** Modèle à l'écran où l'on fait varier des paramètres et observe les effets, sans risque ni matériel. Fonctions (Tricot, 2020) : 23 Apprendre à faire sur simulateur, en réalité virtuelle ; 22 Expérimenter.

**Pour une bonne utilisation.**

- Donner une question à tester avant de manipuler ; sinon on joue sans apprendre.

- Un retour qui porte sur la connaissance à mettre en œuvre quand on se trompe (T).

- Faire noter chaque essai, puis conclure avec le vrai matériel quand c'est possible.

**Par exemple avec.** PhET (phet.colorado.edu/fr) · eduMedia (edumedia.com/fr) · GeoGebra (geogebra.org).

**Référentiel.** Classe III ; fonctions F15, F17, F18 ; patrons, micro-formats, gabarits : P09, MF06 ; GF-Q ; TC52 ; procédure : logiciel : hors production ; fiche d'exploration : Livre I (GF-Q) ; décision automatique du 2 novembre 2026, réversible.

**Signature visuelle.** Tablette affichant un circuit électrique simulé (pile, interrupteur, lampe) avec un curseur, posée à côté d'une feuille d'essais à cocher. Elle se distingue du matériel d'expérimentation (TR40) par l'absence d'objet réel et la possibilité de recommencer sans limite. Au premier regard : « je change un réglage, je vois l'effet ».

**Texte à intégrer (surimpression).** Écran : « Circuit simple — Ajoute une pile · Ferme l'interrupteur » ; indicateur « La lampe : éteinte / faible / forte ». Feuille : « Essai 1 : 1 pile → \_\_\_ · Essai 2 : 2 piles → \_\_\_ · Ma conclusion : \_\_\_ ».

**Prompt d'image.** Vue de dessus d'une tablette posée à plat sur une table claire en bois pâle, affichant une interface de simulation inventée et épurée pour élèves de ~12 ans : schéma de circuit avec une pile, un interrupteur, une lampe, un curseur et un petit indicateur ; à côté, une feuille d'essais avec trois lignes et un crayon. Interface neutre, aucune application reconnaissable. Aucune main. Couleurs neutres avec un seul accent coloré. Lumière douce et homogène, rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

**Vigilance.** Aucune interface de simulateur réel (PhET ou autre). Le schéma doit être électriquement plausible : un circuit fermé, fils reliés aux bornes ; sinon, poser le schéma en surimpression (banque IC). Pas de valeurs chiffrées générées.

### TR54 — Robot ou programmation

*Carte R54 · famille V (Audio, vidéo et numérique) · exemple illustré : 4P · cycle 1 · ~8 ans · éducation numérique.*

**Verso de la carte.** Robot de sol ou application pour écrire une suite d'instructions. Fonctions (Tricot, 2020) : 19 Programmer.

**Pour une bonne utilisation.**

- Commencer par des activités débranchées.

- Proposer des défis courts et progressifs.

- Fixer un objectif explicite : l'effet sur les autres apprentissages n'est pas démontré (T).

**Par exemple avec.** Thymio (thymio.org) · ScratchJr (scratchjr.org) · Scratch (scratch.mit.edu).

**Référentiel.** Classe III ; fonctions F17, F30 ; patrons, micro-formats, gabarits : TC53 ; procédure : Partie 8.

**Signature visuelle.** Petit robot de sol posé sur un tapis quadrillé, avec en dessous une bande de cartes-flèches qui forme le programme. L'élève prévoit, exécute, corrige. Au premier regard : « je programme, le robot exécute ».

**Texte à intégrer (surimpression).** Titre : « Emmène le robot à la bibliothèque ». Cartes du programme : « ↑ · ↑ · ↻ · ↑ » (avance, avance, tourne à droite, avance). Mention : « Je prévois · je teste · je corrige ». Tapis : cases « école » (départ) et « bibliothèque » (arrivée).

**Prompt d'image.** Vue de dessus d'un tapis quadrillé de quatre cases sur quatre, sur une table claire en bois pâle, pour élèves de ~8 ans : petites illustrations dans certaines cases (une école en bas à gauche, une bibliothèque en troisième rangée à partir du bas, deuxième colonne). Un petit robot de sol arrondi, sans visage de personnage existant et sans marque, posé sur la case école et orienté vers le haut. En bas de l'image, une rangée de quatre cartes-flèches en carton. Aucune main. Couleurs neutres avec un seul accent coloré. Lumière douce et homogène, rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

**Vigilance.** Vérifier le trajet (la bibliothèque a d'abord été générée une rangée trop bas) : départ en bas à gauche, deux cases vers le haut, quart de tour à droite, une case vers la droite ; le robot arrive sur la bibliothèque. Aucun robot réel reconnaissable (Thymio, Bee-Bot, Blue-Bot).

### TR55 — Banque de ressources en ligne

*Carte R55 · famille V (Audio, vidéo et numérique) · exemple illustré : 8P · cycle 2 · ~12 ans · géographie (SHS).*

**Verso de la carte.** Site qui rassemble documents, exercices et vidéos classés par discipline et degré. Fonctions (Tricot, 2020) : 8 Rechercher de l'information ; 14 Apprendre à distance.

**Pour une bonne utilisation.**

- Donner un chemin précis (rubrique, mots-clés), pas « cherche sur internet ».

- Préférer les banques romandes liées au plan d'études, sans traçage des élèves.

- Faire noter la source consultée et la date.

**Par exemple avec.** plandetudes.ch (CIIP) · friportail.ch · educlasse.ch · bdrp.ch · rts.ch/decouverte.

**Référentiel.** Classe V ; fonctions F16, F23 ; patrons, micro-formats, gabarits : GF-O ; procédure : hors production ; chemin de recherche : Livre I (GF-O) ; décision automatique du 2 novembre 2026, réversible.

**Signature visuelle.** Ordinateur portable ouvert sur la page d'accueil d'une banque de ressources inventée, filtres par discipline et degré, et à côté une fiche « ma source ». Au premier regard : « je sais où chercher, et je note d'où ça vient ».

**Texte à intégrer (surimpression).** Écran : « Ma banque de ressources » ; filtres « Discipline : Géographie · Degré : 8P » ; trois résultats « Carte des cantons · Vidéo : le Rhône · Exercice : les lacs ». Fiche : « Source : \_\_\_ · Date : \_\_\_ ».

**Prompt d'image.** Vue de dessus en légère plongée d'un ordinateur portable neutre ouvert sur une table claire en bois pâle, écran affichant un site inventé et sobre pour élèves de ~12 ans : barre de recherche, deux menus déroulants de filtres, trois vignettes de résultats (texte flou) ; à côté, une petite fiche de deux lignes et un crayon. Interface neutre, aucun site réel. Aucune main. Couleurs neutres avec un seul accent coloré. Lumière douce et homogène, rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

**Vigilance.** Aucun logo ni mise en page de site réel (plandetudes, friportail, educlasse). Pas de carte réelle de la Suisse à l'écran. Noms de résultats posés en surimpression.

### TR56 — Contenu IA relu par l'enseignant·e

*Carte R56 · famille V (Audio, vidéo et numérique) · exemple illustré : 5P · cycle 2 · ~9 ans · français (lecture).*

**Verso de la carte.** Texte ou exercice produit avec un outil d'IA par l'enseignant·e, puis vérifié et adapté avant usage. Fonctions (Tricot, 2020) : 1 Présenter de l'information ; 16 Faciliter l'accès (besoins éducatifs particuliers).

**Pour une bonne utilisation.**

- L'enseignant·e génère, relit et corrige ; les élèves n'utilisent pas l'outil eux-mêmes.

- Aucune donnée d'élève dans la demande ; l'outil est validé par l'institution.

- Vérifier faits, niveau de langue et stéréotypes ; signaler que le texte a été produit avec une IA.

**Référentiel.** Classe III ; fonctions F08, F24, F25 ; patrons, micro-formats, gabarits : Partie 9 (prompts) ; contrôles V1 à V19 ; TC55 ; procédure : Livre I (imprimé) ou Partie 8 ; décision automatique du 2 novembre 2026, réversible.

**Signature visuelle.** Trois versions d'un même texte en éventail, de longueurs et de tailles de caractères différentes, portant le même titre ; un tampon « relu » et un crayon de correction. La ressource est banale ; c'est sa fabrication qui change. Au premier regard : « un texte, trois niveaux, relus ».

**Texte à intégrer (surimpression).** Titre commun : « Le hérisson ». Mentions : « Version A · Version B · Version C ». Pied : « Texte produit avec une IA, relu et corrigé par l'enseignant·e ». Tampon : « Relu ».

**Prompt d'image.** Vue de dessus, sur une table claire en bois pâle, de trois feuilles imprimées disposées en éventail, pour élèves de ~9 ans : même titre en haut de chacune, un petit dessin de hérisson identique, mais blocs de texte flou de longueur décroissante et caractères de plus en plus grands ; un tampon encreur et un crayon rouge posés dessus. Aucune main, aucune figure d'IA. Couleurs neutres avec un seul accent coloré. Lumière douce et homogène, rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

**Vigilance.** Aucune représentation anthropomorphe de l'IA, aucune interface de chatbot : seule la ressource finale est montrée. Le dessin de hérisson doit être identique sur les trois feuilles. Mention de transparence posée en surimpression. Règle du module : interdiction de faire utiliser ChatGPT aux élèves, anonymisation obligatoire.

### TR57 — Version adaptée du support

*Carte R57 · famille VI (Accessibilité) · exemple illustré : 4P · cycle 1 · ~8 ans · français (lecture).*

**Verso de la carte.** Même contenu proposé autrement : gros caractères, interligne large, pictogrammes, règle de lecture. Fonctions (Tricot, 2020) : 16 Faciliter l'accès (besoins éducatifs particuliers) ; 2 Lire et comprendre un texte, apprendre à lire.

**Pour une bonne utilisation.**

- Même objectif et même contenu que la version standard : seule la forme change.

- Police sans empattement, taille du degré, jamais moins de 14 pt, interligne large, pas de rouge/vert seuls.

- Proposer l'adaptation à toute la classe quand elle ne nuit à personne.

**Référentiel.** Classe VI ; fonctions F24, F25 ; patrons, micro-formats, gabarits : MF47, MF48 ; MP-D (§ 3.6) ; procédure : Livre I ; décision automatique du 2 novembre 2026, réversible.

**Signature visuelle.** Deux feuilles côte à côte portant le même texte court, l'une en mise en page standard, l'autre en gros caractères aérés avec un pictogramme par phrase ; une règle de lecture colorée posée sur la seconde. Au premier regard : « le même texte, lisible pour tout le monde ».

**Texte à intégrer (surimpression).** Titre commun : « Le chat de Léa ». Texte : « Le chat dort sur le mur. · Il fait chaud. · Léa l'appelle. » Sur la version adaptée : un pictogramme par phrase (chat, soleil, enfant). Mention : « Version standard · Version adaptée ».

**Prompt d'image.** Vue de dessus, sur une table claire en bois pâle, de deux feuilles A5 côte à côte pour élèves de ~8 ans : à gauche, un court texte en caractères normaux (flou) ; à droite, les mêmes trois lignes en très gros caractères espacés, chacune précédée d'un petit pictogramme simple ; une règle de lecture translucide colorée posée sur une ligne de la feuille de droite. Un crayon. Aucune main. Couleurs neutres avec un seul accent coloré (la règle). Lumière douce et homogène, rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

**Vigilance.** Texte posé en surimpression dans les deux versions. La règle de lecture doit réellement isoler une ligne. Pas de rouge ni de vert comme seul code (daltonisme).

### TR58 — Outil d'aide technologique

*Carte R58 · famille VI (Accessibilité) · exemple illustré : 7P · cycle 2 · ~11 ans · français (écriture).*

**Verso de la carte.** Outil numérique qui compense une difficulté : synthèse vocale, dictée vocale, correcteur, lecture audio. Fonctions (Tricot, 2020) : 16 Faciliter l'accès (besoins éducatifs particuliers) ; 18 Produire un texte, un document.

**Pour une bonne utilisation.**

- Choisir l'outil avec l'élève et l'équipe, puis l'entraîner à s'en servir.

- L'autoriser aussi en évaluation quand il compense une difficulté reconnue.

- Vérifier qu'il ne fait pas le travail à la place : la dictée vocale ne remplace pas l'orthographe.

**Par exemple avec.** Synthèse vocale et dictée intégrées à macOS, iOS et Windows.

**Référentiel.** Classe VI ; fonctions F25, F31 ; patrons, micro-formats, gabarits : GF-O ; procédure : hors production ; fiche d'usage : Livre I (GF-O) ; décision automatique du 2 novembre 2026, réversible.

**Signature visuelle.** Tablette affichant un texte d'élève avec un bouton « écouter » et une phrase surlignée, casque audio posé à côté. L'outil est discret ; l'élève reste l'auteur·e. Au premier regard : « j'écoute mon texte pour le corriger ».

**Texte à intégrer (surimpression).** Écran : titre « Mon texte » ; bouton « ▶ Écouter » ; une phrase surlignée ; menu « Lire · Dicter · Vérifier ». Post-it : « J'écoute, je corrige, je relis. »

**Prompt d'image.** Vue de dessus d'une tablette posée à plat sur une table claire en bois pâle, affichant une page de traitement de texte inventée et sobre pour élèves de ~11 ans : quelques lignes de texte flou, une phrase surlignée, un gros bouton de lecture audio, une barre de trois options ; un casque audio filaire posé à côté et un post-it. Interface neutre. Aucune main. Couleurs neutres avec un seul accent coloré. Lumière douce et homogène, rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

**Vigilance.** Aucune application ni assistant vocal reconnaissable, aucune figure d'IA. Mentions posées en surimpression. Casque sans marque.

### TR59 — Atelier à stations autocorrectif

*Carte R59 · famille VII (Dispositifs et organisation de la classe) · exemple illustré : 6P · cycle 2 · ~10 ans · corps et mouvement (éducation physique).*

**Verso de la carte.** Postes numérotés avec consigne illustrée, autocorrection et fiche de suivi. Fonctions (Tricot, 2020) : 10 S'entraîner ; 15 Évaluer, s'autoévaluer, suivre les progrès ; 13 Coopérer.

**Pour une bonne utilisation.**

- Rendre chaque consigne compréhensible sans l'enseignant·e (pictogrammes, exemple).

- Prévoir l'autocorrection à chaque poste.

- Suivre les passages sur une fiche et organiser la rotation.

**Référentiel.** Classe IV ; aménagement de l'espace ; fonctions F17, F21, F27, F39 ; patrons, micro-formats, gabarits : P15, P19, MF38, MF43 ; GF-E ; procédure : Livre I (GF-E).

**Signature visuelle.** Plusieurs postes numérotés « atelier 1, 2, 3 », chacun avec une carte-consigne illustrée d'un mouvement et du petit matériel de motricité ; une fiche de suivi à cocher. Au premier regard : « un circuit d'ateliers moteurs autonomes ».

**Texte à intégrer (surimpression).** Étiquettes : « Atelier 1 — équilibre », « Atelier 2 — lancer », « Atelier 3 — coordination ». Sur une carte : un pictogramme de mouvement. Fiche de suivi : « Réussi : seul · avec aide ».

**Prompt d'image.** Plan large d'un circuit d'ateliers d'éducation physique (~10 ans) dans une salle claire : trois postes numérotés, chacun avec une carte-consigne illustrée d'un mouvement et du petit matériel générique (plots, cordelette, cerceau), une fiche de suivi à cocher posée à côté. Sol de gymnase neutre, organisation nette. Lumière douce, rendu net. Rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

### TR60 — Feuille de route par niveaux et brevet

*Carte R60 · famille VII (Dispositifs et organisation de la classe) · exemple illustré : 5P · cycle 2 · ~9 ans · corps et mouvement.*

**Verso de la carte.** Niveaux à valider un à un, avec un brevet à la fin. Fonctions (Tricot, 2020) : 15 Évaluer, s'autoévaluer, suivre les progrès ; 12 Motiver.

**Pour une bonne utilisation.**

- Des niveaux courts et atteignables : il faut se croire capable de réussir (T).

- Des critères de validation clairs.

- Une validation par un·e camarade ou par l'enseignant·e.

**Référentiel.** Classe I et VII ; fonctions F21, F43 ; patrons, micro-formats, gabarits : MF43, MF61 ; GF-G, GF-L, GF-M ; procédure : Livre I (GF-G, GF-M).

**Signature visuelle.** Feuille verticale organisée en escalier de niveaux numérotés (1 à 5), chacun avec un critère court et une case de validation ; à côté, un petit brevet cartonné remis quand le dernier niveau est atteint. Au premier regard : « je monte de niveau en niveau, puis j'obtiens mon brevet ».

**Texte à intégrer (surimpression).** Titre : « Mon brevet de corde à sauter ». Niveaux : « 1 — 10 sauts pieds joints · 2 — 10 sauts à cloche-pied · 3 — 10 sauts en avançant · 4 — 5 sauts bras croisés · 5 — 30 secondes sans arrêt ». Sous chaque niveau : « Validé par : ________ Date : ________ ». Brevet : « Brevet de corde à sauter — niveau 5 atteint ».

**Prompt d'image.** Vue de dessus, sur une table claire en bois pâle, d'une feuille de route pour élèves de ~9 ans : cinq niveaux disposés en escalier montant, chacun dans un encadré avec une case de validation ; les trois premières cases portent un tampon ou une coche au crayon. À côté, un petit brevet cartonné au format carte postale avec un ruban dessiné, et une corde à sauter enroulée à poignées en bois. Graphisme simple et lisible, couleurs neutres avec un seul accent coloré. Lumière douce et homogène, rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

**Vigilance.** Aucun nom d'élève ni signature lisible sur le brevet ou dans les cases de validation.

### TR61 — Menu à choix

*Carte R61 · famille VII (Dispositifs et organisation de la classe) · exemple illustré : 7P · cycle 2 · ~11 ans · anglais (langue étrangère).*

**Verso de la carte.** Programme composé d'une partie obligatoire et d'activités au choix. Fonctions (Tricot, 2020) : 12 Motiver ; 10 S'entraîner.

**Pour une bonne utilisation.**

- Proposer de vrais choix, d'exigence équivalente.

- Mettre l'objectif essentiel dans la partie obligatoire.

- Garder une trace des choix et en discuter.

**Référentiel.** Classe I ; fonctions F21, F24 ; patrons, micro-formats, gabarits : MF46, MF68 ; GF-I ; procédure : Livre I (GF-I).

**Signature visuelle.** Feuille présentée comme une carte de restaurant : une rubrique obligatoire, une rubrique « au choix » dont il faut retenir un nombre fixé d'activités, une rubrique bonus ; cases à cocher pour le suivi. Au premier regard : « je compose mon programme dans un menu ».

**Texte à intégrer (surimpression).** Titre : « My English menu ». « Starter — obligatoire : Listen and repeat ☐ ». « Main course — choose two: Read a comic ☐ · Write a postcard ☐ · Play memory ☐ · Record a message ☐ ». « Dessert — bonus: Sing the song ☐ ». Bas de page : « Ce que j'ai choisi et pourquoi : ________ ».

**Prompt d'image.** Vue de dessus d'une feuille « menu » d'anglais pour élèves de ~11 ans sur une table claire en bois pâle : mise en page de carte de restaurant simple et soignée, trois rubriques séparées par de fins filets, petites cases à cocher en face de chaque activité, deux cases cochées dans la rubrique centrale. Une petite icône de couverts stylisée en en-tête. Un crayon posé en biais. Typographie simple et lisible, couleurs neutres avec un seul accent coloré. Lumière douce et homogène, rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

**Vigilance.** La rubrique centrale doit contenir plus d'activités que le nombre à choisir (ici quatre pour deux), sinon le choix disparaît.

### TR62 — Débat à partir de productions fictives

*Carte R62 · famille VII (Dispositifs et organisation de la classe) · exemple illustré : 8P · cycle 2 · ~12 ans · formation générale (vivre ensemble).*

**Verso de la carte.** Deux ou trois productions fictives comparées pour argumenter. Fonctions (Tricot, 2020) : 13 Coopérer ; 18 Produire un texte, un document.

**Pour une bonne utilisation.**

- Utiliser des productions inventées, jamais celles d'élèves identifiables.

- Donner des critères de comparaison précis.

- Former de petits groupes et guider les échanges (T).

**Référentiel.** Classe I ; ressources humaines ; fonctions F18, F19, F33 ; patrons, micro-formats, gabarits : P05, P13, MF28, MF30 ; GF-Y ; procédure : Livre I (GF-Y).

**Signature visuelle.** Trois courts textes fictifs d'élèves imaginaires, affichés côte à côte avec une étiquette de position, et une fiche de critères pour comparer. La question est accessible à 12 ans et sans enjeu personnel. Au premier regard : « trois avis, on compare avec des critères ».

**Texte à intégrer (surimpression).** Question : « Faut-il des devoirs à la maison ? ». Étiquettes : « Position A · Position B · Position C ». Fiche : « Je compare : 1. L'avis est-il clair ? 2. Y a-t-il un argument ? 3. Y a-t-il un exemple ? ». Mention : « Textes inventés pour l'exercice ».

**Prompt d'image.** Vue de dessus, sur une table claire en bois pâle, de trois feuilles A5 alignées pour élèves de ~12 ans, chacune avec un court paragraphe manuscrit flou et une étiquette de couleur différente en haut ; en dessous, une fiche de critères à trois lignes et un stylo. Aucun prénom, aucune main. Couleurs neutres avec trois pastilles de couleur distinctes (écart assumé, comme dans la version précédente de la carte). Lumière douce et homogène, rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

**Vigilance.** Écriture floue, jamais lisible ; question et étiquettes posées en surimpression. Aucune production d'élève réelle. Éviter rouge/vert comme seul codage des positions.

**Version primaire.** Illustration et exemple remplacés le 1er novembre 2026 pour situer la carte au primaire ; la version secondaire est conservée hors de cette bibliothèque, pour le futur Catalogue Ressources au secondaire.

### TR63 — Galerie de productions

*Carte R63 · famille VII (Dispositifs et organisation de la classe) · exemple illustré : 6P · cycle 2 · ~10 ans · arts visuels.*

**Verso de la carte.** Productions affichées comme une exposition, avec des commentaires des pairs. Fonctions (Tricot, 2020) : 17 Créer un objet technique, une œuvre ; 15 Évaluer, s'autoévaluer, suivre les progrès.

**Pour une bonne utilisation.**

- Donner des critères de commentaire et un modèle de phrase.

- Demander un point fort et une piste d'amélioration.

- Obtenir l'accord des élèves avant d'exposer.

**Référentiel.** Classe aménagement de l'espace ; fonctions F35, F40 ; patrons, micro-formats, gabarits : MF56 ; GF-Z ; procédure : Partie 8 ; fiche de commentaire : Livre I (GF-Z).

**Signature visuelle.** Plusieurs productions affichées en rangée (comme une exposition), avec des pastilles ou étiquettes de commentaire à côté. Au premier regard : « une exposition de travaux ».

**Texte à intégrer (surimpression).** Titre au mur : « Nos œuvres ». Étiquettes de commentaire : « J'aime la couleur… », « Une idée… ». Trois ou quatre productions plastiques fictives accrochées (dessins, collages).

**Prompt d'image.** Photographie d'une petite galerie de productions plastiques d'élèves (~10 ans) accrochées en rangée sur un mur clair, façon exposition (dessins et collages colorés), avec de petites étiquettes de commentaire à côté (cases vides). Productions fictives et non identifiantes. Cadrage droit, ambiance de classe lumineuse, lumière douce, rendu net. Rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

### TR64 — Cartes de rôle (travail de groupe)

*Carte R64 · famille VII (Dispositifs et organisation de la classe) · exemple illustré : 6P · cycle 2 · ~10 ans · transversal (travail de groupe).*

**Verso de la carte.** Cartes qui attribuent à chaque membre d'un groupe un rôle précis pendant une tâche commune. Fonctions (Tricot, 2020) : 13 Coopérer.

**Pour une bonne utilisation.**

- Petits groupes et tâche assez complexe pour justifier la coopération (T).

- Un rôle utile par carte, décrit en deux phrases ; faire tourner les rôles.

- Débriefer : qu'est-ce que mon rôle a changé dans le travail du groupe ?

**Référentiel.** Classe IV ; ressources humaines et sociales ; fonctions F21, F33, F34 ; patrons, micro-formats, gabarits : P11, MF26, MF29, MF76 ; J13 ; procédure : Livre I (J13) ; décision automatique du 2 novembre 2026, réversible.

**Signature visuelle.** Quatre cartes en éventail, chacune avec un pictogramme et un intitulé de rôle, un petit sablier posé à côté. L'outil est minuscule ; son effet sur la coopération ne l'est pas. Au premier regard : « chacun·e sait ce qu'il ou elle a à faire ».

**Texte à intégrer (surimpression).** Cartes : « Gardien·ne du temps — Je surveille le sablier et j'annonce le temps restant. » · « Secrétaire — J'écris ce que le groupe décide. » · « Porte-parole — Je présente le travail à la classe. » · « Vérificateur·trice — Je relis la consigne et je contrôle le résultat. »

**Prompt d'image.** Vue de dessus, sur une table claire en bois pâle, de quatre cartes rigides de même format disposées en éventail pour élèves de ~10 ans : chacune avec un grand pictogramme simple en haut (sablier, crayon, bulle de parole, coche) et deux lignes de texte flou ; un petit sablier en bois posé à côté. Aucune main. Couleurs neutres avec un seul accent coloré. Lumière douce et homogène, rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

**Vigilance.** Quatre cartes, quatre pictogrammes distincts (banque IC si nécessaire). Intitulés posés en surimpression, écriture inclusive avec point médian.

### TR65 — Coin de classe

*Carte R65 · famille VII (Dispositifs et organisation de la classe) · exemple illustré : 2P · cycle 1 · ~6 ans · transversal (coin lecture).*

**Verso de la carte.** Espace aménagé dans la classe, avec du matériel en libre accès pour un domaine (lecture, sciences, écriture). Fonctions (Tricot, 2020) : 12 Motiver ; 8 Rechercher de l'information.

**Pour une bonne utilisation.**

- Peu de matériel, renouvelé régulièrement, rangé avec des étiquettes illustrées.

- Règles d'usage affichées, construites avec les élèves.

- Relier le coin aux apprentissages en cours : le livre du thème, l'objet à observer.

**Référentiel.** Classe aménagement de l'espace ; fonctions F01, F16, F23 ; patrons, micro-formats, gabarits : SP5, SP9 ; procédure : hors production ; étiquettes et règles d'usage : Livre I (SP5, SP9) ; décision automatique du 2 novembre 2026, réversible.

**Signature visuelle.** Petit coin lecture vu en plongée : tapis, caisse de livres aux couvertures neutres, coussin, étiquette « Coin lecture » et affichette des règles. La ressource est un lieu. Au premier regard : « un endroit où j'ai envie d'aller lire ».

**Texte à intégrer (surimpression).** Étiquette : « Coin lecture ». Affichette : « 1. Je choisis un livre · 2. Je lis sans bruit · 3. Je range à sa place ». Étiquettes de caisse : « albums · documentaires ».

**Prompt d'image.** Vue en plongée d'un petit coin lecture dans une salle de classe claire, pour enfants de ~6 ans : un tapis uni, un gros coussin, une caisse en bois contenant une dizaine de livres aux couvertures unies et sans titre lisible, une petite affichette avec trois pictogrammes et une étiquette sur le mur. Aucune personne. Mobilier simple et sans marque. Couleurs douces, un seul accent coloré. Lumière douce et homogène, rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

**Vigilance.** Écart assumé au socle : vue en plongée d'un espace, pas d'une table. Aucune couverture de livre réelle ni personnage reconnaissable. Textes posés en surimpression.

### TR66 — Billet de sortie

*Carte R66 · famille VIII (Évaluation et traces) · exemple illustré : 8P · cycle 2 · ~12 ans · mathématiques.*

**Verso de la carte.** Mini-retour écrit de fin de leçon : ce que j'ai compris, ce qui me reste à comprendre. Fonctions (Tricot, 2020) : 15 Évaluer, s'autoévaluer, suivre les progrès.

**Pour une bonne utilisation.**

- Une ou deux questions seulement, toujours les mêmes au début.

- Lire les billets et en tenir compte dès la leçon suivante.

- Pour l'humeur, des visages dessinés plutôt que la couleur seule.

**Référentiel.** Classe VII ; fonctions F36, F37, F43 ; patrons, micro-formats, gabarits : MF44, MF32 ; GF-T ; procédure : Livre I (GF-T).

**Signature visuelle.** Tout petit format (quart de page), une ou deux questions rapides, un espace « ce que j'ai compris / ma question ». Au premier regard : « un mini-retour de fin de leçon ».

**Texte à intégrer (surimpression).** Titre : « Billet de sortie ». Questions : « Une chose que j'ai comprise aujourd'hui : \_\_\_\_\_\_\_\_ » et « Une question qui me reste : \_\_\_\_\_\_\_\_ ». Échelle à entourer : « J'ai compris : tout à fait · en partie · pas encore ».

**Prompt d'image.** Gros plan d'un petit billet de sortie (~11-12 ans) au format quart de page, posé sur table claire : un titre court, deux lignes de réponse et une échelle de trois mots à entourer, sans émojis. Papier simple, un crayon à côté. Minimal, aéré, lumière douce, rendu net. Rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

**Ajustement v6.2.** Émojis d'humeur remplacés par une échelle verbale (X-08 ; échelle de confiance MF32).

### TR67 — Grille d'autoévaluation (élève)

*Carte R67 · famille VIII (Évaluation et traces) · exemple illustré : 6P · cycle 2 · ~10 ans · français (production écrite).*

**Verso de la carte.** Tableau de critères où l'élève se situe et note ce qu'il lui reste à améliorer. Fonctions (Tricot, 2020) : 15 Évaluer, s'autoévaluer, suivre les progrès.

**Pour une bonne utilisation.**

- Formuler des critères observables, en « je ».

- Montrer un exemple de réussite pour chaque critère.

- Comparer avec le regard de l'enseignant·e.

**Référentiel.** Classe VII ; fonctions F39, F43 ; patrons, micro-formats, gabarits : MF31 ; G9 ; GF-AA (version élève) ; procédure : Livre I.

**Signature visuelle.** Grille imprimée à trois colonnes « Pas encore · Presque · Oui » avec des critères en « je », quelques cases cochées au crayon ; le texte de l'élève dépasse en dessous. Au premier regard : « je me situe critère par critère ».

**Texte à intégrer (surimpression).** Titre : « Mon récit — je fais le point ». Critères : « Je commence par présenter le lieu et le personnage. · J'utilise des mots pour dire quand (d'abord, ensuite, enfin). · Je mets un point à la fin de chaque phrase. · J'ai relu mon texte à voix basse. » Colonnes : « Pas encore · Presque · Oui ». Bas : « Ce que je vais améliorer : \_\_\_ ».

**Prompt d'image.** Vue de dessus, sur une table claire en bois pâle, d'une grille imprimée A5 pour élèves de ~10 ans : quatre lignes de critères en texte flou, trois colonnes à cases carrées dont certaines cochées au crayon, une ligne libre en bas ; sous la grille dépasse une feuille lignée avec de l'écriture manuscrite floue. Un crayon et une gomme. Aucune main, aucun prénom. Couleurs neutres avec un seul accent coloré. Lumière douce et homogène, rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

**Vigilance.** Critères posés en surimpression. Trois colonnes, pas de visages ni de couleurs feu tricolore (daltonisme ; cohérence avec TR66 qui réserve les visages à l'humeur).

**Version primaire.** Illustration et exemple remplacés le 1er novembre 2026 pour situer la carte au primaire ; la version secondaire est conservée hors de cette bibliothèque, pour le futur Catalogue Ressources au secondaire.

### TR68 — Grille d'évaluation (enseignant·e)

*Carte R68 · famille VIII (Évaluation et traces) · exemple illustré : 6P · cycle 2 · ~10 ans · sciences de la nature (exposé).*

**Verso de la carte.** Outil de jugement de l'enseignant·e : critères et niveaux décrits. Fonctions (Tricot, 2020) : 15 Évaluer, s'autoévaluer, suivre les progrès.

**Pour une bonne utilisation.**

- Aligner chaque critère sur l'objectif visé.

- Décrire chaque niveau par ce que l'on observe.

- Partager une version élève de la grille.

**Référentiel.** Classe méta-ressource pour l'enseignant·e ; fonctions F41 ; E03, E04 ; patrons, micro-formats, gabarits : GF-AA, GF-B2 ; procédure : hors support élève ; Livre I (GF-AA).

**Signature visuelle.** Grille de l'enseignant·e à quatre critères et trois niveaux décrits par des comportements observables, avec en regard une « version élève » simplifiée ; un stylo et un carnet de notes. Au premier regard : « ce que je regarde, décrit niveau par niveau — et la version que les élèves connaissent ».

**Texte à intégrer (surimpression).** Titre : « Exposé sur un animal — grille d'évaluation ». Critères : « Contenu exact · Organisation · Support visuel · Voix et regard ». Niveaux : « À travailler · Acquis · Dépassé », chacun décrit en une phrase floue. Encart : « Version élève : Je dis des choses justes · Mon exposé a un début, un milieu, une fin · Mon affiche aide à comprendre · Je parle fort et je regarde la classe ».

**Prompt d'image.** Vue de dessus, sur une table claire en bois pâle, d'une feuille A4 imprimée en tableau à quatre lignes et trois colonnes, cases remplies de texte flou, et d'une feuille A5 plus simple à côté avec quatre lignes et des pictogrammes ; un stylo et un petit carnet. Aucune main, aucun prénom. Couleurs neutres avec un seul accent coloré. Lumière douce et homogène, rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

**Vigilance.** Textes en surimpression. La grille enseignant·e et la version élève doivent être visuellement distinctes (format, pictogrammes). Statut « ressource enseignant·e » à mentionner sur la carte.

**Version primaire.** Illustration et exemple remplacés le 1er novembre 2026 pour situer la carte au primaire ; la version secondaire est conservée hors de cette bibliothèque, pour le futur Catalogue Ressources au secondaire.

### TR69 — Sondage ou vote en direct

*Carte R69 · famille VIII (Évaluation et traces) · exemple illustré : 7P · cycle 2 · ~11 ans · mathématiques.*

**Verso de la carte.** Question posée à toute la classe, réponses collectées en direct (cartons ou écran) et affichées pour discuter. Fonctions (Tricot, 2020) : 15 Évaluer, s'autoévaluer, suivre les progrès ; 12 Motiver.

**Pour une bonne utilisation.**

- Une question dont les réponses fausses sont plausibles et révèlent des conceptions.

- Faire argumenter entre voisins, puis revoter.

- Réponses anonymes ; expliquer ensuite la bonne réponse, pas seulement l'afficher (T).

**Par exemple avec.** Digistorm (ladigitale.dev) · Wooclap (wooclap.com) · Plickers (plickers.com).

**Référentiel.** Classe VII ; fonctions F01, F06, F33, F36 ; patrons, micro-formats, gabarits : MF16, MF32 ; TC68 ; J16 ; procédure : Partie 8 ; cartons-réponses : Livre I (J16) ; décision automatique du 2 novembre 2026, réversible.

**Signature visuelle.** Trois cartons de vote A, B, C en éventail, une feuille-question et un petit graphique de résultats dessiné à la main. La version papier montre que l'outil importe moins que la question. Au premier regard : « toute la classe répond, puis on discute ».

**Texte à intégrer (surimpression).** Question : « Quelle fraction est la plus grande ? » ; « A : 1/3 · B : 1/4 · C : 2/8 ». Résultats : « A ▮▮▮▮▮▮ · B ▮▮▮ · C ▮▮▮▮ ». Consigne : « Explique ton choix à ton voisin ou ta voisine, puis on revote. »

**Prompt d'image.** Vue de dessus, sur une table claire en bois pâle, de trois cartons de vote rigides marqués A, B et C en éventail, d'une feuille portant une question courte et trois réponses (texte flou) et d'une petite feuille avec un diagramme à barres dessiné au feutre, trois barres de hauteurs différentes. Un feutre posé en biais. Aucune main. Couleurs neutres avec un seul accent coloré. Lumière douce et homogène, rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

**Vigilance.** Lettres A, B, C posées en surimpression si la génération les déforme. Pas d'interface de sondage réelle (Wooclap, Kahoot). Trois barres, pas de pourcentages générés.

### TR70 — Dictée réfléchie

*Carte R70 · famille VIII (Évaluation et traces) · exemple illustré : 5P · cycle 2 · ~9 ans · français (orthographe).*

**Verso de la carte.** Texte dicté ou à compléter dans une forme qui fait réfléchir : dictée à trous, négociée, à choix. Fonctions (Tricot, 2020) : 10 S'entraîner ; 15 Évaluer, s'autoévaluer, suivre les progrès.

**Pour une bonne utilisation.**

- Préférer les formes où l'on justifie (dictée négociée à deux) à la copie sous dictée.

- Cibler une ou deux notions sur un texte court.

- Corriger avec un retour qui explique l'erreur (T), puis faire reprendre.

**Référentiel.** Classe I et VII ; fonctions F27, F33, F38 ; patrons, micro-formats, gabarits : P24, MF33, MF45, MF75 ; G3, G6 ; G20 ; procédure : Livre I (G20) ; décision automatique du 2 novembre 2026, réversible.

**Signature visuelle.** Deux cahiers côte à côte portant la même phrase écrite par deux élèves, avec une version commune au milieu, écrite à deux couleurs. La dictée devient une discussion sur la langue. Au premier regard : « on compare, on décide, on écrit ».

**Texte à intégrer (surimpression).** Consigne : « Dictée négociée — 1. J'écris seul·e · 2. Je compare avec mon binôme · 3. Nous décidons et nous justifions ». Phrase : « Les enfants jouent dans le jardin. » Feuille commune : « Notre phrase : \_\_\_ · Pourquoi “jouent” ? \_\_\_ ».

**Prompt d'image.** Vue de dessus, sur une table claire en bois pâle, de deux cahiers d'écolier ouverts côte à côte pour élèves de ~9 ans, chacun avec une courte phrase manuscrite floue, et entre eux une feuille commune avec la même phrase réécrite, un mot entouré et deux lignes de justification floues ; deux crayons de couleurs différentes. Aucune main, aucun nom. Couleurs neutres avec un seul accent coloré. Lumière douce et homogène, rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

**Vigilance.** Écriture manuscrite floue, jamais lisible ; la phrase et la consigne sont posées en surimpression. Aucun prénom sur les cahiers.

### TR71 — Carnet de bord ou portfolio

*Carte R71 · famille VIII (Évaluation et traces) · exemple illustré : 8P · cycle 2 · ~12 ans · français et formation générale.*

**Verso de la carte.** Carnet où l'élève garde des traces et des réflexions sur ses apprentissages. Fonctions (Tricot, 2020) : 15 Évaluer, s'autoévaluer, suivre les progrès ; 18 Produire un texte, un document.

**Pour une bonne utilisation.**

- Des entrées courtes et régulières.

- Des questions-guides pour écrire.

- Le relire régulièrement avec l'enseignant·e.

**Référentiel.** Classe VII ; fonctions F37, F43 ; patrons, micro-formats, gabarits : P21, MF35 ; GF-H, GF-K, GF-U ; procédure : Livre I (GF-H, GF-K, GF-U).

**Signature visuelle.** Carnet ouvert sur une page datée, écrite à la main selon des rubriques stables, avec des onglets et des productions glissées dedans. Il se distingue de la grille d'autoévaluation (TR67) par le récit daté du parcours. Au premier regard : « je garde la trace de mon chemin ».

**Texte à intégrer (surimpression).** Titre : « Mon carnet de bord — projet journal de classe ». Date : « Mardi 12 mai ». Rubriques : « Aujourd'hui, j'ai fait… · Ce que j'ai appris… · Ce qui a été difficile… · Ma prochaine étape… ».

**Prompt d'image.** Vue de dessus d'un carnet à spirale plié sur une seule page verticale, sur une table claire en bois pâle, pour un·e élève de ~12 ans : quatre rubriques courtes remplies d'une écriture discrète et floue, un post-it vierge. Quelques onglets colorés dépassent du bord, un stylo posé en biais. Aucun nom d'élève. Couleurs neutres avec un seul accent coloré. Lumière douce et homogène, rendu photographique, A5 vertical, matériel fictif et original, sans logo ni marque ; cohérent avec la série.

**Vigilance.** Écriture manuscrite floue, jamais lisible : le texte généré serait déformé. Les rubriques sont posées en surimpression. Aucun nom ni donnée d'élève, y compris sur les onglets. Constat du 31.10.2026 : la double page sortait hors format A5, d'où la page unique.

## A.7 Ajustements des textes et prompts

| **TR** | **Source (carte)** | **Ajustement** | **Règle** |
|---|---|---|---|
| TR02 | « Prénom / Date » en bas de page | Prénom et Date en haut ; titre centré ; objectif ajouté | MP-O-12, R7 |
| TR07 | « Accorde : les (grand) arbres. » | Adjectif à accorder sorti de la phrase, pour que la suite « les grand arbres » n'apparaisse pas | MP-CC-11 |
| TR20 | « Arête — le segment entre deux sommets » | Définition précisée (la formule source désigne aussi une diagonale) ; « sommet » et « perpendiculaires » ajustés | exactitude disciplinaire |
| TR25 | Lettres « s · f · c » pour « soleil » | « c » remplacé par « p » : la lettre c peut noter le son \[s\] (cerise), distracteur ambigu | qualité de l'item (inférence didactique) |
| TR26 | Deux calculs au même résultat (6 × 4 et 8 × 3 font 24) | « 7 × 6 \| 32 », « 4 × 8 \| 45 », « 9 × 5 \| 24 » : résultats distincts, boucle fermée (v7.1) | MP-J-01 |
| TR30 | Gradation par la couleur | Les numéros portent la gradation ; la couleur la double seulement | X-08 |
| TR43 | Titre « Capsule audio ou vidéo courte », image audio seule | Renommée « Capsule audio » ; la vidéo passe en TR44 (v7.1) | cohérence texte-prompt |
| TR48 | Item « on · in · under » sans image ; « coche verte » | Image ajoutée (une seule réponse correcte) ; coche accompagnée d'un message | qualité de l'item ; X-08 |
| TR66 | Émojis d'humeur | Échelle de trois mots à entourer | X-08, MF32 |

Les autres textes et prompts sont repris sans modification de fond. Les cartes TR29 (erreurs de calcul) et TR07 (affirmation fausse sur une catégorie grammaticale) sont conformes : MP-CC-11 restreint P04 à la langue écrite et laisse les erreurs de calcul admises en mathématiques ; un vrai / faux peut porter sur une règle (note de MF16).

**Version primaire (1er novembre 2026).** Les fiches TR29, TR36, TR43, TR47, TR50, TR51, TR52, TR62, TR67, TR68 reprennent les textes et prompts de la version primaire, qui remplacent ceux de la version du 31 octobre 2026 (exemples situés au secondaire I, au secondaire II ou en formation d'adultes). Les ajustements v6.2 des anciennes fiches TR16 et TR18 (aujourd'hui TR62 et TR47) portaient sur ces textes remplacés et ne figurent plus ici.

**Catalogue (1er novembre 2026).** La carte « Tuteur IA encadré » (ancienne R61) n'appartient pas au catalogue primaire : comme le rappelle TR56, les élèves n'utilisent pas eux-mêmes l'outil d'IA.

## A.8 Correspondance avec l'ancienne numérotation

**Renumérotation du 3 novembre 2026.** L'imagier (TR16) prend place dans la famille I ; les types TR16 à TR70 de la version du 2 novembre deviennent TR17 à TR71 (même ordre, un rang de plus). Les documents datés du 1er ou du 2 novembre 2026 (essais, rapports, prompts enrichis) citent la numérotation du 2 novembre. La table ci-dessous donne, pour chaque ancien numéro du 31 octobre, le numéro actuel (3 novembre).

Ancien numéro (cartes R01 à R71 et codes TR01 à TR49 de la version du 31 octobre 2026, où TRnn = ancienne carte Rnn) → numéro actuel. Les anciennes cartes R50 à R71 n'avaient pas de code TR ; l'ancienne R61 (Tuteur IA encadré) est sortie du catalogue primaire.

| **Ancien** | **Actuel** | **Type** | **Ancien** | **Actuel** | **Type** |
|---|---|---|---|---|---|
| TR01 / R01 | TR02 | Fiche d'exercices | TR37 / R37 | TR18 | Affiche-procédure en « je » |
| TR02 / R02 | TR01 | Fiche de découverte | TR38 / R38 | TR44 | Capsule vidéo ou tutoriel |
| TR03 / R03 | TR07 | Fiche diagnostique | TR39 / R39 | TR42 | Comptine ou chanson |
| TR04 / R04 | TR03 | Fiche autocorrective | TR40 / R40 | TR15 | Album ou livre de lecture |
| TR05 / R05 | TR25 | Cartes à pince | TR41 / R41 | TR21 | Carte mentale |
| TR06 / R06 | TR26 | Domino pédagogique | TR42 / R42 | TR22 | Infographie |
| TR07 / R07 | TR27 | Memory pédagogique | TR43 / R43 | TR23 | BD pédagogique |
| TR08 / R08 | TR28 | Cartes à classer | TR44 / R44 | TR34 | Dé pédagogique |
| TR09 / R09 | TR29 | Cartes d'erreurs | TR45 / R45 | TR38 | Matériel de manipulation mathématique |
| TR10 / R10 | TR30 | Cartes d'aide graduée | TR46 / R46 | TR37 | Escape game pédagogique |
| TR11 / R11 | TR35 | Jeu de l'oie pédagogique | TR47 / R47 | TR54 | Robot ou programmation |
| TR12 / R12 | TR36 | Jeu de plateau pédagogique | TR48 / R48 | TR71 | Carnet de bord ou portfolio |
| TR13 / R13 | TR59 | Atelier à stations autocorrectif | TR49 / R49 | TR41 | Fiche-trace de sortie |
| TR14 / R14 | TR17 | Affiche de stratégies | R50 | TR04 | Fiche théorique |
| TR15 / R15 | TR19 | Référentiel collectif | R51 | TR05 | Fiche guide (marche à suivre) |
| TR16 / R16 | TR62 | Débat à partir de productions fictives | R52 | TR06 | Fiche de synthèse (révision) |
| TR17 / R17 | TR63 | Galerie de productions | R53 | TR12 | Manuel ou moyen d'enseignement |
| TR18 / R18 | TR47 | Quiz interactif | R54 | TR13 | Document authentique |
| TR19 / R19 | TR48 | Exerciseur numérique | R55 | TR45 | Diaporama projeté |
| TR20 / R20 | TR51 | Parcours numérique | R56 | TR24 | Image ou œuvre à analyser |
| TR21 / R21 | TR52 | Mur collaboratif numérique | R57 | TR53 | Simulation numérique |
| TR22 / R22 | TR43 | Capsule audio | R58 | TR46 | Tableau interactif ou écran tactile |
| TR23 / R23 | TR66 | Billet de sortie | R59 | TR49 | Activité interactive à l'écran |
| TR24 / R24 | TR67 | Grille d'autoévaluation (élève) | R60 | TR56 | Contenu IA relu par l'enseignant·e |
| TR25 / R25 | TR20 | Glossaire de classe | R61 | — | Tuteur IA encadré (hors catalogue primaire) |
| TR26 / R26 | TR50 | Récit interactif à embranchements | R62 | TR69 | Sondage ou vote en direct |
| TR27 / R27 | TR31 | Cartes de rappel et reprises espacées | R63 | TR39 | Objet fabriqué (FabLearn, 3D) |
| TR28 / R28 | TR68 | Grille d'évaluation (enseignant·e) | R64 | TR57 | Version adaptée du support |
| TR29 / R29 | TR32 | Roue à fenêtre et rabat | R65 | TR58 | Outil d'aide technologique |
| TR30 / R30 | TR11 | Sous-main de l'élève | R66 | TR40 | Matériel d'expérimentation |
| TR31 / R31 | TR60 | Feuille de route par niveaux et brevet | R67 | TR55 | Banque de ressources en ligne |
| TR32 / R32 | TR61 | Menu à choix | R68 | TR14 | Dossier thématique documentaire |
| TR33 / R33 | TR08 | Page d'étude d'un graphème (page-son) | R69 | TR64 | Cartes de rôle (travail de groupe) |
| TR34 / R34 | TR09 | Tracé de chemin orienté | R70 | TR70 | Dictée réfléchie |
| TR35 / R35 | TR10 | Support effaçable sous pochette | R71 | TR65 | Coin de classe |
| TR36 / R36 | TR33 | Loto |  |  |  |
