# Bibliothèque IA 1 — technique (à joindre à l'IA) — v1
<!-- modules : noyau -->

Concevoir et transformer des ressources pédagogiques avec l'assistance de l'IA, de la 1P à la 11S (exemples situés surtout aux cycles 1 et 2) — Suisse romande.

Édition du 21 novembre 2026. Le nom du fichier (« _v1 ») reste stable pour ne pas casser les liens ; l'édition (sa date) identifie la version, la même pour les bibliothèques, le guide web et les modèles. Historique détaillé : fichier NOUVEAUTES.md du dépôt https://github.com/emmanuelflaction/bibliotheques-ia. Auteur : Emmanuel Flaction, HEP Vaud (UER MI) – emmanuel.flaction@hepl.ch. Licence : CC BY-NC-SA 4.0. Ce référentiel n'est pas une publication officielle de la HEP Vaud.

> **Les documents de l'ensemble.** Bibliothèque IA 1 — technique : contrat de production des ressources imprimées, appelé « Livre I » dans le texte. Bibliothèque IA 2 — pédagogique : référentiels de décision pédagogique, appelés « Livre II ». Bibliothèque IA 4 — personnelle : les préférences de l'enseignant·e, à remplir une fois (modèle .docx). Banque d'icônes : un fichier pour l'IA et les images. Le guide pour les enseignant·e·s est une page web (https://emmanuelflaction.github.io/bibliotheques-ia/) ; l'ancienne Bibliothèque IA 3 qui le contenait n'existe plus et son numéro n'est pas réattribué. Pour une ressource imprimée, la Bibliothèque 1 suffit : elle contient la liste des codes du Livre II (Annexe I-D). Joindre aussi la Bibliothèque 2 quand l'outil accepte les longs documents, ou pour une ressource non imprimée.

> **Format de ce fichier.** Version Markdown destinée aux IA (fichier à joindre ou à déposer dans un projet). Ce fichier contient le **Livre I seul** (contrat de production des ressources imprimées : fiches et jeux), complété par la liste des codes du Livre II (Annexe I-D). Si l'outil refuse ce fichier .md, joindre la version .txt ou .docx, identiques. Les tableaux et les blocs de code sont conservés tels quels.

# LIVRE I — CONTRAT DE PRODUCTION DES RESSOURCES IMPRIMÉES (FICHES ET JEUX)
<!-- modules : noyau -->

## À lire en premier

**Ce livre s'applique à toute ressource imprimée destinée aux élèves** : les fiches et documents écrits de la Classe I de la Partie 4 du Livre II (fiche d'entraînement, d'évaluation, de remédiation, d'atelier, de devoir, fiche interdisciplinaire) et, depuis la v7, les **jeux imprimés** de la Classe IV (cartes, dominos, plateaux, dés à monter, étiquettes). Il décrit **ce que l'IA DOIT faire, dans l'ordre**, de la demande jusqu'à la livraison. Pour ces ressources, **il prévaut sur le Livre II** en cas de différence.

Dans ce livre, le mot **« fiche »** désigne toute page imprimée destinée aux élèves. Les règles propres aux jeux sont signalées par le mot « jeu » ou par les codes **J** (gabarits de jeu, § 3.8), **MP-J** (règles communes aux jeux), **R8** (planche de pièces), **V11 à V13** (contrôles) et **GF-F** (dossier de jeu).

**Depuis la v7.2**, ce livre couvre aussi les fiches de référence, les dispositifs et les traces (GF-G à GF-AA), les outils d'étayage permanents (SP, § 3.9), le format affiche A3 (§ 2.5), l'écriture liée composée (R10) et le dessin vectoriel (R11).

Le **Livre II** (Parties 1 à 10) contient les référentiels de décision pédagogique : fonctions, processus cognitifs, familles de ressources, patrons, micro-formats, règles de combinaison, prompts et références. Il est consulté à l'**Étape 3** du présent livre. Pour les ressources non imprimées (audiovisuel, numérique interactif, environnements et banques, dispositifs humains, aménagement de l'espace, sorties), la procédure applicable reste celle de la Partie 8 du Livre II.

**Pourquoi cette organisation.** Lors d'essais menés les 29 et 30 octobre 2026, cinq IA génératives ont reçu la même demande et le même référentiel (v5), où les règles de mise en page figuraient en fin de document. Les choix pédagogiques ont été globalement bien faits. La mise en page a été traitée de façon très inégale, et les défauts les plus graves (lignes d'écriture fusionnées en une seule, exercices coupés entre deux pages, fiches débordant sur une page presque vide) n'étaient **visibles qu'à l'impression**. Ce livre rend donc la mise en page **obligatoire, calculée avant la rédaction et contrôlée sur le rendu**.

**Pourquoi les jeux (v7).** Le 30 octobre 2026, la v6 a été testée sur une demande réelle : « Crée un jeu (cartes, dominos ou autre) pour travailler la conjugaison des verbes en -er et -ir en 5P ». Le domino-boucle obtenu était utilisable, mais l'IA a dû appliquer le Livre I par extension, sans y être autorisée. Un jeu imprimé présente les mêmes risques qu'une fiche à l'impression (pièce coupée, texte trop petit, traits ambigus) et des risques propres : une pièce qui admet deux réponses, des pièces appariables par un indice non visé, un jeu oral pour une notion orthographique.

Niveaux d'exigence : **DOIT** (obligatoire ; dérogation seulement sur demande explicite de l'enseignant·e, toujours signalée), **DEVRAIT** (par défaut ; s'en écarter seulement pour une raison pédagogique explicite, à mentionner), **PEUT** (option). Les codes **MP-** renvoient au standard de mise en page (Annexe I-A).

#### Priorité des règles (21.11.2026)

**1. Sécurité et droit** (données des élèves, cadre cantonal sur l'IA, droits d'auteur) : toujours, sans dérogation.

**2. Règles DOIT** de ce livre : appliquées ; dérogation seulement sur demande explicite de l'enseignant·e, toujours signalée.

**3. Règles conditionnelles** : une règle ne vaut que dans son champ (degré, âge, statut de lecteur, type de support, discipline). Une règle écrite pour les non-lecteurs ou pour l'apprentissage initial de l'écriture ne s'applique pas au secondaire I. Si le champ d'une règle n'est pas clair, l'IA le dit et retient la lecture la plus prudente pour l'élève.

**4. Règles DEVRAIT** : appliquées par défaut ; l'IA s'en écarte pour une raison pédagogique explicite, qu'elle mentionne.

**5. Conventions éditoriales du projet** (teintes de couleur, motif du dos des cartes, liseré des cartes (MP-J-14), police d'élèves des exemples (MP-T-10), libellé des mentions de planche : nom du jeu en toutes lettres, sans code de gabarit) : appliquées par défaut, sans exception tant que rien n'est demandé ; la demande de l'enseignant·e ou sa Bibliothèque IA 4 peuvent les remplacer.

**6. Préférences de l'enseignant·e** (demande, Bibliothèque IA 4) : elles priment sur les règles DEVRAIT et sur les conventions ; face à une règle DOIT, l'IA signale le conflit et demande.

Deux règles se contredisent : l'IA ne tranche pas en silence ; elle cite les deux, applique la plus protectrice pour l'élève et le signale dans le rapport.

#### Statuts de vérification (21.11.2026)

Dans le rapport de conformité et dans tout compte rendu, chaque contrôle porte l'un de ces quatre statuts :

**Vérifié automatiquement** : mesure ou calcul effectué sur le fichier produit ;

**Vérifié par inspection réelle** : le rendu du fichier (PDF, image de page) a été regardé ;

**À vérifier par l'enseignant·e** : exactitude disciplinaire, adéquation à la classe, impression ;

**Non vérifiable dans cet environnement** : par exemple, aucun rendu n'est possible.

L'IA ne déclare jamais conforme un contrôle qu'elle n'a pas effectué. Elle distingue ce que l'enseignant·e a indiqué, ce qu'elle suppose et ce qui reste à vérifier (par exemple, la progression d'une notion dans le PER).

# ÉTAPE 0 — LE CONTRAT
<!-- modules : noyau -->

## 0.1 Six étapes, six livrables, six portes

L'IA DOIT suivre les six étapes dans l'ordre. Une étape n'est franchie que si sa **porte** est ouverte.

| Étape | Question | Livrable obligatoire | Porte (condition pour passer à l'étape suivante) |
|---|---|---|---|
| 1 Cadrer | Pour qui, pour quoi, dans quel contexte ? | Bloc « Cadrage » (5 lignes au plus) | Discipline, notion et degré connus ; adéquation à la progression PER examinée |
| 2 Spécifier | Combien de place, sur combien de pages ? | **Fiche technique** (tableau) | Chaque zone de réponse dimensionnée ; **budget de page respecté (≤ 22 cm par page)** |
| 3 Choisir | Quelle activité, sous quelle forme ? | Colonnes « patron / micro-format / gabarit » de la fiche technique | Chaque exercice relié à un gabarit G, chaque pièce de jeu à un gabarit J (ou nouveau gabarit décrit selon la fiche-type) |
| 4 Construire | Comment le réaliser dans le fichier ? | Fichier .docx (fiche élève ou dossier de jeu) et fichier .docx séparé (partie enseignant·e) | Recettes R1 à R15 utilisées ; aucun interdit X |
| 5 Vérifier | Que voit-on à l'impression ? | **Rapport de conformité** | Contrôle sur rendu effectué, ou impossibilité déclarée avec la liste des contrôles laissés à l'enseignant·e |
| 6 Livrer | Dans quel ordre, avec quoi ? | Les quatre pièces, dans l'ordre du § 0.2 | — |

## 0.2 Ordre de sortie obligatoire

1. **Cadrage et fiche technique** (courts, dans la réponse).
2. **Fiche élève** (.docx) ; pour un jeu, **dossier de jeu** (.docx : règle et carte-mémoire, planches, trace individuelle ; GF-F).
3. **Partie enseignant·e** (.docx séparé, jamais intégrée à la fiche élève).
4. **Rapport de conformité** et **statut des informations** (dans la partie enseignant·e ou dans la réponse).

## 0.3 Règle d'arbitrage fondamentale

> **Quand le contenu ne tient pas, on réduit le contenu, jamais les dimensions.**

L'IA ne DOIT jamais diminuer la taille du texte, la hauteur ou la longueur des zones de réponse, les interlignes ou les marges pour faire tenir une fiche. Elle réduit le nombre d'items (au minimum trois par exercice), déplace un exercice sur la page suivante, ajoute une page dans la limite du gabarit de fiche, ou propose deux fiches. Pour un jeu, elle réduit le nombre de pièces, jamais leur taille ni celle de leur texte.

#### Ordre de priorité en cas de conflit

1. La demande explicite de l'enseignant·e. Si elle contredit une règle DOIT : l'appliquer, puis signaler l'écart et sa conséquence en une phrase.
2. Le présent contrat (Étapes 0 à 6) et le standard MP-* (Annexe I-A).
3. Les gabarits d'exercice et de fiche (Étape 3, Étape 6).
4. Le Livre II.
5. Les exemples : ils illustrent ; ils ne font pas norme.

## 0.4 Les interdits

Ces dix-huit pratiques ont produit des fiches ou des jeux inutilisables lors des essais, ou sont exclues par le standard. Elles DOIVENT être évitées ; leur présence est un écart grave.

| Code | Interdit | Pourquoi | À la place |
|---|---|---|---|
| X-01 | Faire une zone de réponse d'une phrase ou plus avec des tirets bas « ____ » | Longueur et hauteur non garanties ; l'élève écrit serré | Recette R1 (vraies lignes) ; les tirets bas sont réservés aux lacunes de 1 à 2 mots (R2) |
| X-02 | Empiler des paragraphes vides munis d'une bordure inférieure pour faire des lignes | Word et LibreOffice **fusionnent les bordures de paragraphes consécutifs identiques** : six lignes prévues s'impriment comme **une seule** | Recette R1a (tableau) ou R1b (tabulation) |
| X-03 | Couper un exercice, une consigne, un tableau ou un encadré entre deux pages | L'élève perd le lien consigne–tâche | Recette R4 ; saut de page avant l'exercice |
| X-04 | Réduire la police, l'interligne, les zones ou les marges pour faire tenir | Contredit le standard du degré | Règle d'arbitrage § 0.3 |
| X-05 | Afficher une étiquette de niveau évaluative sur la fiche élève (« soutien », « niveau 1 », « faible », « fort ») | Stigmatise ; fige l'élève dans un niveau | Repère neutre (symbole ♣ ♦ ♠, lettre de version) ; items facultatifs marqués ★ ; pilotage dans la partie enseignant·e |
| X-06 | Placer un titre d'exercice avant la consigne ; mettre plusieurs actions dans une phrase ; formuler une consigne négative | Tâche de lecture avant l'apprentissage | Consigne directe, une action par phrase, étapes numérotées (MP-CO) |
| X-07 | Placer une aide ou un exemple **après** l'exercice qu'il sert | Attention divisée (MP-CC-04) | Aide au-dessus de l'exercice, au plus près |
| X-08 | Texte justifié, majuscules continues, émojis, couleur seule porteuse d'information | Lisibilité, photocopie noir-blanc, daltonisme | MP-T-03, MP-T-07, MP-C-02 |
| X-09 | Pré-marquer (gras, couleur) les éléments que l'élève doit repérer | La réponse est donnée | MP-CC-10 |
| X-10 | Lacune dont la longueur ne correspond pas à la réponse attendue | Incohérence consigne–format | Calibrage R2 ; MP-CO-07 |
| X-11 | Mettre la différenciation, le corrigé ou le barème dans la fiche élève | Mélange des destinataires | Partie enseignant·e séparée |
| X-12 | Livrer sans fiche technique ni rapport de conformité, ou affirmer un contrôle de rendu non effectué | Les défauts d'impression restent invisibles | Étapes 2 et 5 |
| X-13 | Montrer à l'élève une forme écrite fautive ou inexistante : mot mal orthographié, accord ou conjugaison erronés (par exemple « il a manger », « prendu »), y compris dans une phrase à corriger, un vrai/faux, un distracteur, une banque de mots ou un exemple, hors de l'exception encadrée du § 3.7 | Choix didactique du référentiel : par défaut, un support destiné à l'élève ne donne à voir que des formes correctes | Formes correctes à justifier, à trier, à comparer ; travail sur les propres productions de l'élève ; sur décision de l'enseignant·e, dès la 5P, analyse d'erreurs aux quatre conditions du § 3.7 (MP-CC-11) |
| X-14 | Placer le titre avant la ligne Prénom et Date, omettre l'objectif formulé pour l'élève, ou le faire précéder d'une étiquette (« Mon objectif : », « Objectif : ») | Repères instables d'une fiche à l'autre | En-tête obligatoire (R7, MP-O-12) |
| X-15 | Jeu : fabriquer une pièce qui admet deux réponses dans le lot | L'élève ne peut pas trancher ; la boucle ou l'appariement échoue sans erreur de sa part | Une seule pièce correcte par question dans tout le lot (MP-J-01) ; contrôle V11 |
| X-16 | Jeu : rendre des pièces appariables par un indice non visé (radical, longueur, ordre d'impression, position sur la planche) | L'élève réussit sans mobiliser la notion | Au moins trois formes du même mot dans le lot ; ordre d'impression mélangé (MP-J-02, MP-J-03) |
| X-17 | Jeu : proposer un jeu uniquement oral (par exemple « J'ai… Qui a… ? ») pour une notion uniquement orthographique | Les formes visées se prononcent de la même façon (je chante, tu chantes, ils chantent) : le jeu ne travaille pas la notion | Un jeu qui fait lire ou écrire la forme (§ 1.1, vigilance « modalité ») |
| X-18 | Livrer une page élève remplie partiellement (bas de page vide) | Papier gaspillé ; fiche qui paraît inachevée ; l'élève croit avoir oublié une partie | Aérer, compléter ou passer en planche A5 (MP-O-14, R15, V20) |

## 0.5 Si l'outil ne peut pas produire un fichier .docx structuré
<!-- modules : noyau, verification -->

Si l'IA ne peut pas créer de tableaux, de hauteurs de ligne exactes ou de tabulations dans un vrai fichier .docx, elle DOIT **le dire avant de produire**. Elle livre alors :

1. le cadrage et la fiche technique complète (Étapes 1 et 2) ;
2. le contenu de la fiche, balisé rôle par rôle (`[CONSIGNE]`, `[DONNÉES]`, `[ZONE : 2 lignes de 16 cm]`, `[SAUT DE PAGE]`) ;
3. la liste des réglages à appliquer dans Word (Étape 4) ;
4. la mention explicite : « Mise en page à réaliser ; ce texte n'est pas une ressource prête à imprimer. »

Elle ne présente jamais un texte avec des tirets bas comme une fiche prête à imprimer.

## 0.6 Analyser, puis transformer une ressource

**Analyser une ressource.** Quand l'enseignant·e joint une ressource et demande de l'analyser, l'IA remet un bref rapport en quelques points : ce qu'elle en comprend (degré scolaire, notion enseignée, objectif d'enseignement, fonction et utilisation du document), ce qui fonctionne, les possibilités d'amélioration numérotées, en s'appuyant sur la grille de l'Annexe I-B. Elle termine en demandant de confirmer ou de corriger sa lecture. L'analyse s'arrête au rapport.

**Transformer une ressource analysée.** Quand l'enseignant·e choisit une ou plusieurs possibilités du rapport, ou indique d'autres modifications, l'IA transforme la ressource selon les Étapes 1 à 6, en gardant l'objectif et ce qui fonctionne, et dit ce qui a changé. Si l'enseignant·e a corrigé la lecture ou dit ce qu'il ou elle observe avec ses élèves, l'IA en tient compte.

## 0.7 Demandes venant du guide web

Le guide web « Composer un écosystème de ressources » produit des demandes en langage courant, sans code ni renvoi chiffré : l'enseignant·e les lit avant de les coller et doit pouvoir les comprendre. Les détails restent dans cette bibliothèque, et l'IA les applique sans qu'ils soient rappelés :

- le modèle est désigné par son nom, dans une ligne « Jeu choisi », « Type d'exercice », « Forme de la fiche », « Support choisi » ou « Outil choisi » ; l'index ci-dessous donne le gabarit correspondant ; en cas de doute, demander ;
- « si tu ne peux pas créer de fichier Word » renvoie au § 0.5 ;
- « la liste des contrôles, chacun avec son statut » renvoie à l'Étape 5 et à la règle MP-V-03 ;
- « Analyse-la et rédige un bref rapport » et « Transforme la fiche selon la possibilité … de ton rapport » renvoient au § 0.6.

Dans ce qu'elle écrit à l'enseignant·e (propositions, explications, liste des contrôles), l'IA nomme les choses en toutes lettres ; les codes et les renvois chiffrés ne figurent que dans la fiche technique et le rapport de conformité, après le nom.

**Index des noms du guide** (tiré du guide, édition du 21 novembre 2026)

| Ligne de la demande | Gabarit |
|---|---|
| Jeu choisi : Domino-boucle | J1 |
| Jeu choisi : Memory, appariement | J2 |
| Jeu choisi : Familles | J3 |
| Jeu choisi : Cartes recto-verso | J4 |
| Jeu choisi : Plateau · serpent | J5-a |
| Jeu choisi : Plateau · escargot | J5-b |
| Jeu choisi : Plateau · chemin | J5-c |
| Jeu choisi : Plateau · circuit | J5-d |
| Jeu choisi : Dé à monter | J6 |
| Jeu choisi : Loto | J7 |
| Jeu choisi : Symboles communs | J8 |
| Jeu choisi : Trouve quelqu'un qui… | J9 |
| Jeu choisi : Carte à pinces | J10 |
| Jeu choisi : Roue à fenêtre et rabat | J11 |
| Jeu choisi : Lettres à fabriquer | J12 |
| Jeu choisi : Cartes de rôle | J13 |
| Jeu choisi : Cartes d'erreurs | J14 |
| Jeu choisi : Cartes d'aide graduée | J15 |
| Jeu choisi : Cartons-réponses | J16 |
| Jeu choisi : Grille d'alignement | J17 |
| Jeu choisi : Serpents et échelles | J18 |
| Jeu choisi : Bataille navale | J19 |
| Jeu choisi : Roue de tirage | J20 |
| Jeu choisi : Puzzles à deux pièces | J21 |
| Jeu choisi : Puzzle à bandes | J22 |
| Jeu choisi : Mot mystère | J23 |
| Jeu choisi : Cocotte en papier | J24 |
| Jeu choisi : Horloge à aiguilles | J25 |
| Jeu choisi : Mémo-fiches en éventail | J26 |
| Jeu choisi : Bandes graphiques | J27 |
| Jeu choisi : Plateau à camemberts | J28 |
| Jeu choisi : Cherche et trouve | J29 |
| Jeu choisi : Mots interdits | J30 |
| Jeu choisi : Petit bac | J31 |
| Jeu choisi : Cartes à terminaisons | J32 |
| Jeu choisi : Petits chevaux | J33 |
| Jeu choisi : Qui est-ce ? | J34 |
| Jeu choisi : Bataille | J35 |
| Jeu choisi : Tuiles-lettres | J36 |
| Jeu choisi : Sudoku | J37 |
| Jeu choisi : Mot caché : la fleur | J38 |
| Type d'exercice : Entourer | G1 |
| Type d'exercice : Relier | G2 |
| Type d'exercice : Compléter | G3 |
| Type d'exercice : Transformer, recopier | G4 |
| Type d'exercice : Remettre en ordre | G5 |
| Type d'exercice : Cocher | G6 |
| Type d'exercice : Production courte guidée | G7 |
| Type d'exercice : Repérer dans un texte | G8 |
| Type d'exercice : Tableau à compléter | G9 |
| Type d'exercice : Image et écriture | G10 |
| Type d'exercice : Colorier selon une consigne | G11 |
| Type d'exercice : Classer en colonnes | G12 |
| Type d'exercice : Calcul posé | G13 |
| Type d'exercice : Chronologie | G14 |
| Type d'exercice : Copier puis illustrer | G15 |
| Type d'exercice : Recherche visuelle | G16 |
| Type d'exercice : Série chronométrée | G17 |
| Type d'exercice : Grille croisée de nombres | G18 |
| Type d'exercice : Tracé de chemin | G19 |
| Type d'exercice : Dictée réfléchie | G20 |
| Type d'exercice : Imagier, scène à légender | G21 |
| Forme de la fiche : Fiche d'entraînement | GF-A |
| Forme de la fiche : Fiche d'évaluation | GF-B |
| Forme de la fiche : Fiche de remédiation | GF-C |
| Forme de la fiche : Devoir à la maison | GF-D |
| Forme de la fiche : Ateliers | GF-E |
| Forme de la fiche : Dossier de jeu | GF-F |
| Forme de la fiche : Feuille de route par niveaux | GF-G |
| Forme de la fiche : Trace longitudinale | GF-H |
| Forme de la fiche : Menu à choix | GF-I |
| Forme de la fiche : Page-son | GF-J |
| Forme de la fiche : Carnet de rituel | GF-K |
| Forme de la fiche : Dossier de défis | GF-L |
| Forme de la fiche : Brevet d'étape | GF-M |
| Forme de la fiche : Fiche théorique | GF-N |
| Forme de la fiche : Fiche guide | GF-O |
| Forme de la fiche : Fiche de synthèse | GF-P |
| Forme de la fiche : Questionnaire sur document | GF-Q |
| Forme de la fiche : Dossier documentaire et grille de croisement | GF-R |
| Forme de la fiche : Fiche-trace de sortie | GF-S |
| Forme de la fiche : Billet de sortie | GF-T |
| Forme de la fiche : Page de carnet de bord | GF-U |
| Forme de la fiche : Affiche A3 | GF-V |
| Forme de la fiche : Planche de BD | GF-W |
| Forme de la fiche : Dossier d'escape game | GF-X |
| Forme de la fiche : Fiche de comparaison pour le débat | GF-Y |
| Forme de la fiche : Fiche de commentaire de galerie | GF-Z |
| Forme de la fiche : Grille d'évaluation et version élève | GF-AA |
| Support choisi : Lignes d'écriture romandes | G22 |
| Support choisi : Syllabes et sons | G23 |
| Support choisi : Maisons des nombres | G24 |
| Support choisi : Reproduction sur quadrillage | G25 |
| Support choisi : Calendrier mensuel | G26 |
| Support choisi : Étiquettes de l'horaire | G27 |
| Support choisi : Livret à onglets | G28 |
| Support choisi : Page de journal | G29 |
| Support choisi : Planche de BD | G30 |
| Support choisi : Plan d'exposé | G31 |
| Outil choisi : Bande numérique à triple codage | SP1 |
| Outil choisi : Réglette avec repère de latéralité | SP2 |
| Outil choisi : Sous-main personnel | SP3 |
| Outil choisi : Affiche-procédure en « je » | SP4 |
| Outil choisi : Étiquettes de coin ou de journée | SP5 |
| Outil choisi : Affiche-métaphore structurante | SP6 |
| Outil choisi : Affiche-acronyme de stratégie | SP7 |
| Outil choisi : Affiche mnémotechnique | SP8 |
| Outil choisi : Affiche de stratégies | SP9 |
| Outil choisi : Référentiel collectif | SP10 |
| Outil choisi : Glossaire de classe | SP11 |
| Outil choisi : Carte mentale | SP12 |
| Outil choisi : Infographie | SP13 |

# ÉTAPE 1 — CADRER
<!-- modules : noyau -->

## 1.1 Paramètres

Règle de sobriété : ne poser de question que pour les paramètres **indispensables** manquants. Pour les autres, faire une hypothèse raisonnable et l'annoncer en une ligne.

| Paramètre | Valeurs | Si absent |
|---|---|---|
| Discipline et notion | Français, Mathématiques, Connaissance de l'environnement, etc. | **Demander** |
| Degré | 1P à 8P (désignation suisse exclusivement) | **Demander** |
| Type de ressource | fiche d'entraînement, d'évaluation, de remédiation, d'atelier, de devoir, interdisciplinaire ; fiche de référence ; document de suivi ; affiche ; outil permanent ; jeu (cartes, dominos, plateau, dé) | Hypothèse : fiche d'entraînement |
| Durée | ex. 20, 30 ou 40 minutes | Hypothèse : 30 min |
| Contexte d'usage | en classe, à domicile, en autonomie, guidé | Hypothèse : en classe, individuel |
| Statut de lecture | non-lecteur, lecteur débutant, lecteur | Déduire du degré et l'annoncer |
| Matériel | photocopie noir-blanc ou couleur, ciseaux, colle | Hypothèse : photocopie noir-blanc ; si l'enseignant·e imprime en couleur, proposer une teinte (`definir_couleur`, R11) |
| Différenciation | une fiche, parcours sur la même fiche, ou versions parallèles | Hypothèse : parcours sur la même fiche |
| Préférences | zone Prénom / Nom / Date, police scolaire locale ; en 1P à 4P, lignes simples ou lignes d'écriture romandes pour les zones d'écriture (R1) | Prénom + Date ; Arial ; en 1P à 4P, **proposer le choix** entre lignes simples et lignes d'écriture romandes, puis l'appliquer à toute la fiche |
| Jeu : joueurs et joueuses | seul·e, duo, trois, quatre, groupe | Hypothèse : duo |
| Jeu : matériel | papier épais, plastification, massicot ou ciseaux, dé, pions | Hypothèse : papier épais, découpe par l'adulte |
| Jeu : durée d'une partie | en minutes | Hypothèse : environ 10 minutes (inférence de conception) |

#### Si la demande porte sur un jeu

- **Un jeu ou une fiche ?** (question de la Partie 8, Étape 6, reprise ici) : un jeu sert-il mieux l'objectif qu'une fiche ? Il se justifie par l'entraînement répété, la rétroaction immédiate (boucle qui se ferme, vérification par l'autre), la coopération ou la manipulation. Sinon, une fiche est préférable.
- **Vigilance « modalité »** : si la notion est orthographique (terminaisons muettes, accords, homophones), choisir un jeu qui fait **lire ou écrire** la forme. Un jeu uniquement oral ne travaille pas la notion (X-17) : *je chante*, *tu chantes* et *ils chantent* se prononcent de la même façon.
- **Vigilance « notion ambiguë »** : annoncer dans le cadrage l'interprétation retenue. Exemple : « verbes en -ir » = verbes du 2e groupe, du type *finir* ; *partir*, *dormir* et *venir* sont exclus.
- **Paramètres du jeu** : joueurs et joueuses, matériel, durée d'une partie (tableau ci-dessus), à annoncer comme hypothèses s'ils manquent.

## 1.2 Adéquation de la demande à la progression PER (MP-P-09)

Avant de concevoir, l'IA DOIT examiner si la notion, la **modalité** (oral ou écrit) et le **niveau d'attente** (découverte, consolidation, maîtrise) correspondent à la progression des apprentissages du degré dans le PER.

- Si la demande anticipe ou dépasse la progression, l'IA **ne refuse pas** : elle le signale en une phrase et adapte la fiche (par exemple « première approche, sans attente de maîtrise », vocabulaire et verbes limités à ceux du degré, appui oral, moyen de référence disponible).
- Exemple de vigilance : pour une notion de conjugaison, vérifier si le temps visé est attendu à l'écrit ou seulement à l'oral pour le degré (PER, L1 26, rubrique « Conjugaison »).
- L'IA ne cite un texte du PER que si elle l'a effectivement consulté (portail CIIP) ; sinon, elle écrit **[À VÉRIFIER dans le PER]**.
- Source du cycle 2 lisible par une IA, vérifiée lors de la préparation de la v7 (30.10.2026) : CIIP, *Plan d'études romand (PER) – Aperçu des contenus, cycle 2*, 2012 (https://edudoc.ch/record/104591/files/cycle_2_webCIIP.pdf). **Limite** : c'est un aperçu ; il ne contient ni les codes d'objectifs (par exemple L1 26), ni la progression des apprentissages détaillée, ni les attentes fondamentales. Pour une progression précise, la mention [À VÉRIFIER dans le PER] reste nécessaire.

## 1.3 Statut de lecture
<!-- modules : noyau, differenciation -->

Le statut non-lecteur / lecteur change le fonctionnement de toute la fiche.

- **Non-lecteurs et lecteurs débutants (en général 1P-2P, parfois 3P)** : **aucune consigne écrite destinée à l'élève** : la consigne est donnée oralement par l'adulte et portée sur la fiche par un **exemple complet, déjà fait, en tête de la fiche** (première case ou premier item, sur fond teinté) et, au besoin, par un pictogramme stable par verbe de consigne ; le seul texte admis est celui que l'élève travaille (mot à lire, lettre, nombre) et une ligne « Pour l'adulte », en petit, en bas de page ; recette : `definir_jeunes(True)` retire aussi la consigne écrite des fiches dessinées (G23, G24) et y place l'exemple ; pour les lecteurs débutants (3P), un pictogramme stable par verbe de consigne PEUT accompagner la consigne écrite ; **option « pictogrammes de consigne »**, à tout degré : si l'enseignant·e la demande, chaque consigne du document DOIT être précédée, à gauche, du pictogramme de la banque d'icônes qui correspond à son verbe (codes IC-CON, fonction `icone`, 1,2 à 1,5 cm de haut, texte de remplacement de la banque) ; le même verbe reçoit le même pictogramme dans tout le document ; le pictogramme accompagne la consigne écrite et ne la remplace jamais (MP-C-02) ; si aucun pictogramme ne correspond au verbe, ne pas en inventer : choisir un verbe de la banque ou le signaler ; si la banque n'est pas jointe, écrire le code entre crochets (`[IC-CON-ENTOURE]`) et le signaler ; une fois demandée, l'option vaut pour tous les documents de la conversation, jusqu'à avis contraire ; une seule tâche par page est souvent préférable. *Le corpus source ne fournit pour ce public que la taille de 24 pt et le principe de l'image utile : toute autre adaptation est une proposition, à présenter comme telle.*
- **Lecteurs** : consignes écrites d'une phrase, une action par phrase.

## 1.4 Bloc « Cadrage » (modèle)

```
Cadrage — Français, conjugaison : composer le passé composé — 5P
Type : entraînement, 30 min, en classe, individuel, photocopie noir-blanc.
Lecteurs : oui (consignes écrites courtes).
PER : [constat d'adéquation, ou « à vérifier »] → choix qui en découle.
Différenciation : parcours sur la même fiche (hypothèse).
```

#### Exemple de cadrage d'un jeu

```
Cadrage — Français, conjugaison : présent des verbes en -er et en -ir — 5P
Type : jeu (domino-boucle), duo, partie d'environ 10 min, papier épais, découpe par l'adulte.
Modalité : la forme est lue puis posée (notion orthographique) ; pas de jeu uniquement oral.
Interprétation : « verbes en -ir » = type finir ; partir, dormir et venir exclus.
PER : [constat d'adéquation, ou « à vérifier »] → choix qui en découle.
```

## 1.5 Terminologie et cadre institutionnel (DOIT)

- **Plan d'études** : PER (CIIP). Cycle 1 = 1P à 4P ; cycle 2 = 5P à 8P ; cycle 3 = 9e à 11e années, notées 9S à 11S dans ce référentiel.
- **Désignation des degrés** : utiliser **exclusivement** la désignation suisse 1P à 8P, puis 9S à 11S. Ne jamais employer CP, CE1, CE2, CM1, CM2, « petite section » ou les cycles français. Correspondance approximative par âge : CP ≈ 3P, CE1 ≈ 4P, CE2 ≈ 5P, CM1 ≈ 6P, CM2 ≈ 7P.
- **Disciplines (cycle 1, exemple vaudois)** : Français, Mathématiques, Connaissance de l'environnement (regroupe géographie, histoire-éthique et cultures religieuses, sciences de la nature), Éducation physique, Activités créatrices et manuelles, Arts visuels, Musique.
- **Registre** :
  - Consignes adressées aux élèves : **tutoiement et impératif** (« Entoure », « Complète »). Au secondaire I (9S-11S), l'usage peut différer selon l'établissement : l'IA suit la Bibliothèque IA 4 ou la demande ; à défaut, elle garde le tutoiement et le signale.
  - Parties destinées aux adultes : écriture inclusive au point médian (enseignant·e, étudiant·e·s).
  - Documents destinés à des adultes en formation : **vouvoiement**.
- **Cadre cantonal (élèves et IA)** : de la 1P à la 8P, une fiche ne DOIT jamais demander à un·e élève d'utiliser un outil d'IA. De la 9S à la 11S, une fiche PEUT prévoir un tel usage aux quatre conditions suivantes, sinon la règle de la 1P-8P s'applique : (1) l'enseignant·e le demande explicitement ; (2) l'outil est fourni ou autorisé par le canton ou l'établissement, jamais un compte personnel de l'élève sur un service grand public, et aucune donnée personnelle d'élève n'y est saisie ; (3) l'activité a lieu en classe et elle est encadrée ; (4) la tâche fait vérifier, comparer ou critiquer la réponse de l'outil plutôt que la recopier. L'IA rappelle que les directives et les documents de référence du canton et de l'établissement font foi, et qu'elle ne les connaît pas forcément dans leur version en vigueur. Repère : le canton de Vaud a annoncé, pour la rentrée 2026, un outil sécurisé permettant d'expérimenter l'IA avec les élèves de l'école obligatoire et des documents de référence (communiqué du 12 août 2026). Tout outil numérique proposé DEVRAIT être compatible avec la nLPD et les directives cantonales.

# ÉTAPE 2 — SPÉCIFIER : FICHE TECHNIQUE ET BUDGET DE PAGE
<!-- modules : fiches, jeux -->

## 2.1 Table unique des paramètres par degré

C'est la **seule source des valeurs chiffrées**. L'IA lit la colonne du degré et n'invente pas d'autres valeurs.

| Paramètre | 1P-2P | 3P-4P | 5P-6P | 7P-8P | Statut |
|---|---|---|---|---|---|
| Taille du texte lu par l'élève | 24 pt | 18 pt | 14 pt | 12 pt | Standard (MP-T) |
| Titre de la fiche | taille du texte + 2 à 4 pt, gras | idem | idem | idem | Inférence de conception |
| Police | Arial, Verdana, Tahoma ou Calibri ; une seule | idem | idem | idem | MP-T-01, MP-T-02 |
| Interligne de lecture | 1,5 | 1,5 | 1,5 | 1,5 | MP-E-01 |
| Interligne des phrases à trous | 2,0 | 2,0 | 2,0 | 2,0 | MP-E-02 |
| Hauteur d'une ligne d'écriture | ≥ 1,0 cm ; davantage ou « trottoirs » selon l'écriture des élèves (proposition) | 1,0 cm | 1,0 cm | 0,8 à 1,0 cm | MP-E-03 (8-10 mm) |
| Lacune d'un mot ou d'un nombre | 6-8 cm | 6-8 cm | 6-8 cm | 6-8 cm | MP-E-07 |
| Réponse d'une phrase | 2 lignes de 14-16 cm | idem | idem | idem | MP-E-05, MP-E-07 |
| Production courte | 5-6 lignes de 16 cm | idem | idem | idem | MP-E-07 |
| Cellule de tableau à remplir | ≥ 5 cm × ≥ 1 cm | idem | idem | idem | MP-E (table) |
| Exercices par page | 3-5 courts ou 1-2 longs | idem | idem | idem | MP-O-04 |
| Items par exercice | 3-5 (6-10 très courts et identiques pour l'automatisation) | idem | idem | idem | MP-CI-02 |
| Hauteur d'une ligne de texte lue | 1,27 cm | 0,95 cm | 0,74 cm | 0,64 cm | Calculée (taille × 1,5) |
| Hauteur d'un item à trou | 1,69 cm | 1,27 cm | 0,99 cm | 0,85 cm | Calculée (taille × 2,0) |
| Tirets bas pour 6 cm (Arial / Calibri) | 13 / 14 | 17 / 19 | 22 / 24 | 25 / 28 | Calculée (métriques des polices) |
| Tirets bas pour 8 cm (Arial / Calibri) | 17 / 19 | 23 / 25 | 29 / 33 | 34 / 38 | Calculée (métriques des polices) |
| Pièce de domino J1 | 9,3 × 5,3 cm ; 26 pt ; 10 dominos par planche | idem | 9,3 × 3,3 cm (deux moitiés de 4,65 cm) ; 18 pt ; 16 dominos par planche ; deux lignes dans la moitié question | idem | Révision du 19.11.2026 (MP-J-11, variantes par tranche d'âge, § 3.8) : 5P-8P rendu en PDF et regardé ; 1P-4P calculé et rendu en miniature ; non testé en classe. Ancienne pièce de 8 × 2,5 cm, 14 pt : testée le 30.10.2026 |
| Planche de pièces | une page ; toute la surface utile (MP-J-11) | idem | idem | idem | MP-J-11, MP-J-12 |

*Les valeurs « calculées » ont été établies dans cette version à partir de la taille de police et des métriques des polices (Liberation Sans et Carlito, métriquement identiques à Arial et Calibri). Elles servent à planifier ; le contrôle sur rendu (Étape 5) fait foi.*

*Cycle 3 (9S à 11S) — valeurs retenues le 21.11.2026, non testées en classe : appliquer les valeurs de la colonne 7P-8P (texte de 12 pt ; 11 pt seulement sur demande, pour un document dense de 10S-11S). Les règles propres aux non-lecteurs et à l'apprentissage initial de l'écriture (lignes d'écriture romandes, absence de ligne Prénom, consigne remplacée par un exemple déjà fait) ne s'appliquent pas au cycle 3. Les jeux ont leurs propres formats 9S-11S (§ 3.8, variantes par tranche d'âge). La progression d'une notion au cycle 3 se vérifie dans le PER ; sans vérification, elle est marquée « à vérifier ».*

## 2.2 Budget de page (MP-O-11)
<!-- modules : fiches -->

- Hauteur utile d'une page A4 portrait : 29,7 − 2 × 2,5 = **24,7 cm**.
- Pour absorber les écarts de rendu entre logiciels, l'IA DOIT planifier au plus **22 cm de contenu par page**, en-tête compris.
- Hauteur estimée d'un exercice : **consigne** (nombre de lignes × hauteur d'une ligne lue) + **exemple** éventuel + **items** (nombre × hauteur indiquée par le gabarit) + **zones d'écriture** (nombre de lignes × hauteur d'une ligne d'écriture) + **0,8 cm** d'espace après l'exercice.
- En-tête obligatoire (Prénom et Date, titre centré avec espace avant et après, objectif ; R7) : environ 3,5 cm en 5P-6P, 4,5 cm en 3P-4P, 5,5 cm en 1P-2P (estimation).
- **Planche de pièces (jeu)** : mention de la planche (environ 0,9 cm) + nombre de rangées × hauteur d'une pièce ; une planche = une page. Valeur testée : 2 × 8 dominos de 8 × 2,5 cm = **20,9 cm prévus** ; **21,1 cm rendus** lors du test du 30.10.2026, **20,7 cm** (de la marge haute au dernier trait) lors du contrôle des recettes v7. Toute autre dimension de pièce est une inférence de conception, à tester. **Depuis le 19.11.2026**, une planche n'est plus limitée au budget de 22 cm : elle occupe toute la surface utile (MP-J-11), la mention passe dans la marge du haut et des repères de coupe bordent la feuille (MP-J-12) ; les gabarits J1, J3, J4, J6 à J8 et J12 à J16 ont été redimensionnés en conséquence le 19.11.2026 (§ 3.8).
- Si le total d'une page dépasse 22 cm, l'IA applique la règle d'arbitrage (§ 0.3) **avant** de rédiger.
- **Page pleine (MP-O-14, révision du 2.11.2026)** : aucune page élève n'est remplie partiellement. Sur le rendu, le dernier objet imprimé de chaque page DOIT atteindre au moins **90 % du budget** : en A4 portrait, 19,8 cm de contenu sous la marge haute (dernier élément imprimé à 22,3 cm au moins du haut de la feuille, soit au plus 4,9 cm de blanc au-dessus de la marge basse) ; en A4 paysage, 12,8 cm. La mesure se fait sur l'image de la page rendue : seuls les éléments visibles comptent (un cadre blanc ou la marge blanche d'une image ne comptent pas). Si une page reste en dessous, l'IA choisit, selon la fiche, l'un de ces trois remèdes :
  1. **aérer** : augmenter les espacements (hauteur des lignes d'écriture et des cellules, espaces avant et après les exercices), sans dépasser 22 cm ni descendre sous les valeurs du degré ;
  2. **compléter** : ajouter quelques lignes d'écriture, ou un ou deux items ou exercices de même nature, au service du même objectif ;
  3. **passer en planche A5** (R15) : la feuille A4 porte deux exemplaires identiques, à découper ; on imprime deux fois moins. Réservé aux contenus courts : règle de jeu, petite fiche, bande, ticket, brevet. Budget d'un exemplaire A5 : 16,9 cm (A5 portrait, côte à côte) ou 12,3 cm (A5 paysage, empilés), à remplir aussi à 90 % au moins.
- Exceptions à la page pleine : la partie enseignant·e ; la dernière planche d'un jeu quand le nombre de pièces est fixé par le jeu (à déclarer dans la fiche technique). Le contrôle se fait sur le rendu (V20, fonction `verifier_remplissage` de l'Annexe I-C).

## 2.3 Modèle de fiche technique

| N° | Gabarit | Patron / micro-format | Items | Réponse attendue | Zone de réponse | Hauteur estimée | Page |
|---|---|---|---|---|---|---|---|
| — | En-tête R7 | — | — | — | Prénom et Date ; titre centré ; objectif élève | … cm | 1 |
| 1 | G… | P…, MF… | … | geste / mot / phrase / production | … | … cm | 1 |
| … |  |  |  |  |  |  |  |
|  | **Total page 1** |  |  |  |  | **≤ 22 cm** |  |
|  | **Total page 2** |  |  |  |  | **≤ 22 cm** |  |

#### Exemple rempli (illustratif) — Fiche d'entraînement, passé composé, 5P, Arial 14 pt

| N° | Gabarit | Patron / micro-format | Items | Réponse attendue | Zone de réponse | Hauteur estimée | Page |
|---|---|---|---|---|---|---|---|
| — | En-tête R7 | — | — | — | Prénom et Date ; titre centré ; objectif élève | 3,5 cm | 1 |
| — | Encadré R5 | pré-training minimal | — | — | règle + 2 exemples (4 lignes) | 3,6 cm | 1 |
| 1 | G8 Repérage | P06 / MF04 | 4 | geste (souligner, encadrer) | aucune ligne | 5,3 cm | 1 |
| 2 | G9 Tableau | P06 / MF14 | 4 | 1 mot par cellule | cellules 5 cm × 1,1 cm | 7,1 cm | 1 |
|  | **Total page 1** |  |  |  |  | **19,5 cm** |  |
| 3 | G3 Compléter | P06 / MF15 | 5 | 2 mots (auxiliaire + participe) | lacune de 6 cm (22 tirets bas) | 7,4 cm | 2 |
| 4 | G7 Production | P12 / MF23 | 1 | 2 phrases | 4 lignes R1a | 6,3 cm | 2 |
| — | Bilan R6 | MF31 | 3 critères | choix entouré | cellules ≥ 1 cm | 3,8 cm | 2 |
|  | **Total page 2** |  |  |  |  | **17,5 cm** |  |

#### Fiche technique d'un jeu : planches de pièces

Pour un jeu, la fiche technique ajoute une ligne par planche.

| Planche | Gabarit J | Pièce (l × h) | Pièces par rangée × rangées | Contenu d'une pièce | Hauteur de la planche | Page |
|---|---|---|---|---|---|---|
| Lot Lune | J1 Domino-boucle | 8 × 2,5 cm (deux moitiés de 4 cm) | 2 × 8 = 16 | réponse en gras · question sur deux lignes, 14 pt | 0,9 + 8 × 2,5 = 20,9 cm | 2 |

#### Rubrique « Conditionnement » (v7.2, MP-O-13)

Pour toute ressource imprimée autre qu'une fiche à photocopier, la fiche technique ajoute une ligne : support, finition, découpe, montage, quantité par page, autocorrection portée par le matériel.

| Support | Finition | Découpe et montage | Quantité par page | Autocorrection |
|---|---|---|---|---|
| papier épais, feuille sous pochette effaçable, A3 | plastification, velcro, pincette, attache parisienne | par l'adulte, en atelier, par l'élève | n exemplaires, numérotés si les pièces doivent se retrouver | verso, double impression, rabat, forme, grille croisée, ou aucune |

## 2.4 Limites de pages par type de fiche
<!-- modules : fiches -->

| Type de fiche | Pages élève au maximum | Si le budget est dépassé |
|---|---|---|
| Entraînement (GF-A) | 2 | réduire les items, puis supprimer un exercice, ou proposer deux fiches |
| Évaluation (GF-B) | 2 | réduire les items ; ne jamais supprimer la tâche complexe |
| Remédiation (GF-C) | 2 | réduire les items |
| Devoir (GF-D) | 1 | réduire à 4-6 items |
| Atelier (GF-E) | 1 par station | une station = une page |
| Jeu (GF-F) | règle et aide : 1 page par groupe ; planches : annexes à découper, 1 page par planche ; trace écrite individuelle : 1 page au maximum | réduire le nombre de pièces, jamais leur taille ; une planche par page |
| Fiche de référence (GF-N, GF-O, GF-P) | 1 ; GF-P : 1 + verso | réduire le nombre d'exemples ou d'étapes |
| Page-son (GF-J) | 1 par graphème | réduire les mots, jamais la taille de l'écriture liée |
| Fiche sur document (GF-Q) | 1, document compris | agrandir le document sur une page séparée |
| Dossier documentaire (GF-R) | 1 de présentation et 1 de croisement ; documents en annexe | réduire à quatre documents |
| Fiche de terrain (GF-S) | 1 (recto) | réduire les rubriques |
| Billet de sortie (GF-T) | 3 billets par page | deux questions au plus |
| Suivi (GF-G, GF-H, GF-I, GF-K, GF-L, GF-U) | 1 | réduire les niveaux ou les rubriques |
| Dossier d'escape game (GF-X) | mise en situation 1, énigmes 1 par planche, feuille d'équipe 1 | réduire le nombre d'énigmes |
| Affiche (GF-V) | 1 A3 | réduire le nombre d'étapes, jamais le corps |

Les annexes facultatives (aide-mémoire, étiquettes à découper) ne comptent pas dans ce total ; elles sont annoncées dans la fiche technique et dans la partie enseignant·e.

## 2.5 Format affiche A3 et lisibilité à distance (v7.2)
<!-- modules : fiches -->

Le Livre I est calibré pour la page A4. Les affiches, référentiels collectifs, glossaires, cartes mentales et infographies destinés à être lus depuis les places (TR17 à TR22) suivent la table ci-dessous, propre au format A3 (MP-F-07, GF-V, recette R9).

| Paramètre | Valeur | Statut |
|---|---|---|
| Format | A3 (29,7 × 42 cm), portrait ou paysage | Inférence de conception |
| Marges | 2,5 cm (MP-F-03) | Standard |
| Largeur utile | 24,7 cm en portrait ; 37 cm en paysage | Calculé |
| Budget de hauteur | ≤ 33 cm en portrait ; ≤ 22 cm en paysage | Calculé (37 cm ou 24,7 cm utiles, même rapport que 22 / 24,7) |
| Titre | 72 pt, gras, centré, deux lignes au plus | Inférence de conception ; testé sur rendu |
| Texte principal (lecteurs de 3P à 8P) | 48 pt, ou 36 pt si le tableau compte trois colonnes | Inférence de conception ; testé sur rendu |
| Texte principal (1P-2P) | 60 pt, trois à six mots par ligne, pictogramme à chaque ligne | Inférence de conception, non testé |
| Détail, exemple | 36 pt | Inférence de conception ; testé sur rendu |
| Plancher | 28 pt, pour ce qui se lit à moins d'un mètre (consigne de montage, source) | Inférence de conception |
| Nombre d'étapes ou de rubriques | Six au plus ; une ligne d'affiche = une idée | Verso des cartes TR17, TR18 |
| Couleur | Jamais seule porteuse d'information (X-08) ; affiche lisible en noir et blanc | Standard |

#### Distance de lecture selon la taille (Arial)

La hauteur de la capitale d'Arial vaut 0,716 fois le corps (métrique de la police). La distance-seuil suppose qu'une capitale reste identifiable à 5 minutes d'arc, convention de l'acuité 10/10 (connaissance non vérifiée dans la session). La distance de confort applique un facteur 2 (inférence de conception, à éprouver dans la classe).

| Corps | Capitale | Distance-seuil | Distance de confort |
|---|---|---|---|
| 28 pt | 7,1 mm | 4,9 m | 2,4 m |
| 36 pt | 9,1 mm | 6,3 m | 3,1 m |
| 48 pt | 12,1 mm | 8,3 m | 4,2 m |
| 60 pt | 15,2 mm | 10,4 m | 5,2 m |
| 72 pt | 18,2 mm | 12,5 m | 6,3 m |

*Valeurs calculées avec `distance_lecture_m` (Annexe I-C). Elles ne remplacent pas l'essai : placer l'affiche, puis la lire depuis la place la plus éloignée (V17).*

# ÉTAPE 3 — CHOISIR : DE L'OBJECTIF AU GABARIT
<!-- modules : fiches, jeux -->

## 3.1 Chaîne de décision

> Objectif → indices de réussite → fonction (F, Livre II Partie 1) → processus cognitif (Partie 3) → patron (P, Partie 5) → micro-format (MF, Partie 6) → **gabarit d'exercice (G, § 3.3) ou de jeu (J, § 3.8)** → dimensions (Étape 2)

Les choix pédagogiques se font avec le Livre II. **Le gabarit est le point de passage obligé** entre la pédagogie et la mise en page : c'est lui qui apporte les dimensions, la hauteur estimée et la recette de construction.

## 3.2 Règle de couverture (originalité permise, jamais sans dimensions)

- Chaque exercice de la fiche DOIT correspondre à un gabarit G1 à G31 ; chaque pièce d'un jeu, à un gabarit J1 à J38 (§ 3.8) ; chaque outil permanent, à un gabarit SP (§ 3.9) ; chaque document, à un gabarit GF (§ 6.1).
- L'IA PEUT proposer un format non répertorié si elle le juge mieux adapté. Elle DOIT alors le décrire **avant de l'utiliser** avec la même fiche-type que les gabarits ci-dessous (usage, disposition, zone de réponse, items, hauteur estimée, recette, vigilance), et l'inscrire dans la fiche technique.

## 3.3 Catalogue des gabarits d'exercice (auto-portants, G1 à G31)
<!-- modules : fiches -->

Chaque fiche donne tout ce qu'il faut pour construire l'exercice. Les hauteurs sont des **estimations pour 5P-6P (14 pt)** ; pour un autre degré, utiliser les hauteurs de ligne de la table 2.1. Dans les exemples, `______` représente une lacune calibrée (R2) et `[ligne]` une vraie ligne d'écriture (R1).

Règles communes : consigne directe au-dessus des données ; texte aligné à gauche ; numérotation 1, 2, 3 pour les exercices et a), b), c) pour les items ; exercice solidaire (R4).

### G1 — Entourer

- **Usage** : discrimination visuelle (son, nature d'un mot, plus grand / plus petit).
- **Disposition** : propositions alignées à gauche, précédées de a), b), c) ; image éventuelle à gauche de l'item.
- **Zone** : aucune ligne ; espaces blancs entre les propositions.
- **Items** : 3-5 lignes ; 3-4 propositions par ligne au maximum.
- **Hauteur** : consigne + lignes × 0,74 cm + 0,8 cm → environ 4 cm pour 4 lignes.
- **Recette** : texte simple, interligne 1,5 ; R4.
- **Vigilance** : propositions séparées par au moins 1,5 cm pour que le tracé ne déborde pas ; toutes les propositions sont des mots correctement orthographiés (X-13). **Entourer un mot dans une phrase** : une phrase par ligne, les mots séparés par un blanc d'au moins 0,8 cm (trois espaces insécables) et un interligne d'au moins 1,2 cm, pour que l'élève puisse tracer son ovale sans toucher le mot voisin ni la ligne suivante. **Pictogramme de consigne** : quand la consigne vise une chose précise (« Entoure le verbe »), utiliser `pictogramme_consigne(base, 'entoure', 'verbe')`, qui dessine l'ovale autour du mot visé, plutôt que le pictogramme générique « abc ».

### G2 — Relier

- **Usage** : mot ↔ définition, mot ↔ image, calcul ↔ résultat.
- **Disposition** : tableau sans bordures de 3 colonnes : colonne gauche (≈ 5 cm) / colonne vide (≥ 6 cm) / colonne droite (≈ 5 cm) ; point d'ancrage • en fin de colonne gauche et en début de colonne droite.
- **Zone** : la colonne vide centrale ; aucune ligne.
- **Items** : 3-5 paires.
- **Hauteur** : paires × 1,2 cm + consigne → environ 6 cm pour 4 paires.
- **Recette** : R3 sans bordures (lignes ≥ 1,2 cm, insécables).
- **Vigilance** : alignement garanti par le tableau, jamais par des espaces tapés.

### G3 — Compléter (lacune dans une phrase)

- **Usage** : conjugaison, vocabulaire, nombres ; réponse de **1 à 2 mots**.
- **Disposition** : phrase avec lacune au point de réponse ; indication éventuelle entre parenthèses après la lacune.
- **Zone** : lacune de 6-8 cm (nombre de tirets bas selon table 2.1) ; interligne 2,0.
- **Items** : 3-5 phrases.
- **Hauteur** : consigne + exemple + items × 0,99 cm + 0,8 cm → environ 7,5 cm pour 5 items.
- **Recette** : R2.
- **Vigilance** : réponse de 3 mots ou plus → G4 avec lignes en dessous. Éviter l'élision impossible (« Je ___ pris ») : amorce « J'___ » ou autre sujet.

```
3  Complète avec le verbe au passé composé.
   a) Hier, tu ______________________ (chanter) une chanson.
```

### G4 — Transformer, recopier

- **Usage** : changer le temps, la personne, le nombre ; recopier en appliquant une règle. La phrase source est toujours correcte (X-13).
- **Disposition** : phrase source alignée à gauche ; en dessous, 2 lignes d'écriture.
- **Zone** : **2 lignes de 14-16 cm par phrase, à tous les degrés**.
- **Items** : 3-4 phrases (exercice coûteux en place).
- **Hauteur** : par item 0,74 + 2 × 1,0 + 0,3 cm ≈ 3 cm → environ 10 cm pour 3 items.
- **Recette** : R1a.
- **Vigilance** : pas de phrase source fautive « à corriger » (X-13), sauf analyse d'erreurs demandée par l'enseignant·e aux conditions du § 3.7 ; pour travailler le jugement orthographique, voir d'abord les alternatives du § 3.7.

```
4  Écris la phrase au passé composé.
   a) Nous jouons au ballon.
      [ligne]
      [ligne]
```

### G5 — Remettre en ordre

- **Usage** : syntaxe, compréhension de la phrase.
- **Disposition** : mots séparés par des barres obliques, alignés à gauche ; puis lignes d'écriture.
- **Zone** : 2 lignes de 16 cm (la phrase reconstruite est une phrase écrite : MP-E-05).
- **Items** : 1 phrase de 5-7 mots par item ; 2-3 items.
- **Hauteur** : environ 3 cm par item.
- **Recette** : R1a.
- **Vigilance** : ponctuation hors des étiquettes ; vérifier qu'une seule phrase correcte est possible.

### G6 — Cocher (QCM, vrai / faux)

- **Usage** : compréhension, choix, autoévaluation.
- **Disposition** : options en ligne ou en colonne, chacune précédée d'une case.
- **Zone** : aucune ligne.
- **Items** : 3 options, une seule bonne réponse.
- **Hauteur** : environ 1 cm par question.
- **Recette** : cases = cellules vides bordées de 0,6 cm (R3) ou caractère ☐ vérifié sur rendu (R6).
- **Vigilance** : la case est à moins de 1 cm de son texte. Toutes les options sont des formes correctement orthographiées ; un vrai/faux porte sur le sens, un fait ou une règle, jamais sur une forme écrite fautive (X-13).

### G7 — Production courte guidée

- **Usage** : réinvestir une règle dans une ou plusieurs phrases personnelles.
- **Disposition** : consigne (contrainte explicite : verbe, mot, sujet imposé) ; amorce éventuelle ; lignes.
- **Zone** : 2 lignes par phrase demandée ; 5-6 lignes pour un mini-récit.
- **Items** : 1 consigne de production.
- **Hauteur** : consigne + lignes × 1,0 cm + 0,8 cm.
- **Recette** : R1a ; R1b si chaque ligne commence par une amorce (« Le matin, j'ai … »).
- **Vigilance** : une contrainte par phrase de consigne ; contrainte vérifiable.

```
7  Écris deux phrases au passé composé sur ta journée d'hier.
   Le matin, j'ai ________________________________________
   [ligne]
```

### G8 — Repérer dans un texte

- **Usage** : lecture active, grammaire, vocabulaire.
- **Disposition** : consigne en étapes numérotées (une action par étape) ; texte court aligné à gauche.
- **Zone** : aucune ligne ; au moins 1 cm d'espace sous le texte.
- **Items** : 2-4 lignes de texte ou 3-5 phrases courtes.
- **Hauteur** : consigne + lignes de texte × 0,74 cm + 0,8 cm → environ 5 cm.
- **Recette** : texte simple, interligne 1,5 ; R4.
- **Vigilance** : actions différentes (souligne / encadre / entoure) plutôt que couleurs ; aucun pré-marquage.

### G9 — Tableau à compléter

- **Usage** : conjugaison, synthèse, classement.
- **Disposition** : en-tête en gras ; une ligne d'exemple remplie, réponses en police d'élèves (MP-T-10) ; cellules vides aux endroits de réponse.
- **Zone** : cellules ≥ 5 cm × ≥ 1 cm ; largeur totale ≤ 16 cm.
- **Items** : 3-5 lignes + 1 ligne d'exemple.
- **Hauteur** : (1 + lignes) × 1,1 cm + consigne + 0,8 cm → environ 7 cm pour 4 lignes.
- **Recette** : R3.
- **Vigilance** : avec 5 colonnes sur 16 cm, la règle des 5 cm ne peut pas être tenue : réduire les colonnes de rappel (pronom, item) et garder ≥ 4 cm pour les colonnes de réponse, puis **déclarer l'écart**.

### G10 — Image et écriture

- **Usage** : premiers écrits, vocabulaire, description.
- **Disposition** : image au-dessus de la consigne (8 × 10 cm au maximum), lisible en noir et blanc ; lignes en dessous.
- **Zone** : 2 lignes en 3P-4P, 3-5 lignes à partir de 5P.
- **Items** : 1 image, 1 consigne.
- **Hauteur** : jusqu'à 10 cm d'image + lignes → environ 14 cm (exercice long).
- **Recette** : image dans une cellule de tableau insécable avec la consigne (R4) ; R1a.
- **Vigilance** : pas d'image décorative ; pas de photographie de personne réelle ; image générée sans texte incrusté (MP-I-05).

### G11 — Colorier selon une consigne

- **Usage** : formes, catégories, nombres (cycle 1 surtout).
- **Disposition** : dessins simples de 3-4 cm en grille régulière ; consigne qui **nomme les couleurs en toutes lettres**.
- **Zone** : les dessins.
- **Items** : 8 éléments au maximum ; 2-3 couleurs.
- **Hauteur** : environ 9 cm pour deux rangées.
- **Recette** : grille = tableau sans bordures, cellules égales.
- **Vigilance** : éviter rouge/vert et rouge/bleu ; prévoir une version « entoure / barre » pour la photocopie noir-blanc.

### G12 — Classer en colonnes

- **Usage** : tri selon un critère (nom/verbe, vivant/non-vivant).
- **Disposition** : banque de mots **au-dessus** du tableau ; une colonne par catégorie ; un exemple placé par colonne, en police d'élèves (MP-T-10).
- **Zone** : 2 colonnes de 6-8 cm ou 3 colonnes de 5 cm ; une ligne de 1 cm par entrée.
- **Items** : 2-3 catégories × 3-5 mots.
- **Hauteur** : banque 1,5 cm + (1 + entrées) × 1,0 cm + 0,8 cm → environ 7 cm.
- **Recette** : R3.
- **Vigilance** : banque de mots dans un ordre mélangé.

### G13 — Calcul posé

- **Usage** : opérations en colonnes.
- **Disposition** : tableau à cases (un chiffre par case), en-têtes de rang (C, D, U) en début d'apprentissage ; signe à gauche ; trait de résultat.
- **Zone** : cases ≥ 1 cm × 1 cm ; une ligne de cases pour les retenues.
- **Items** : 2-4 calculs côte à côte.
- **Hauteur** : environ 6 cm.
- **Recette** : R3 avec cellules carrées de hauteur exacte.
- **Vigilance** : jamais de calcul « posé » écrit en ligne.

### G14 — Chronologie

- **Usage** : succession dans le temps (récit, journée, cycle).
- **Disposition** : 4-5 vignettes encadrées de largeur égale, lecture de gauche à droite ; case de numéro sous chaque vignette.
- **Zone** : la case de numéro (≥ 1 cm).
- **Items** : 4-5 étapes.
- **Hauteur** : environ 7 cm.
- **Recette** : tableau de 4-5 colonnes égales (≤ 16 cm au total).
- **Vigilance** : vignettes lisibles en noir et blanc.

### G15 — Copier puis illustrer

- **Usage** : passage du non-lecteur au lecteur ; le dessin prouve la compréhension sans production écrite supplémentaire (TR02, BDRP-A1).
- **Structure** : carte à trois zones superposées : modèle (écriture liée ou script), ligne de copie, cadre de dessin. Repère de lot au verso, sans étiquette évaluative (X-05).
- **Dimensions** : carte de 8 × 10,1 cm ; zones de 2,2, 1,6 et 6,3 cm ; quatre cartes par planche (16 × 20,2 cm).
- **Recette** : R14 (`planche_zones`) ; R10 pour le modèle ; R12 pour le verso.
- **Contrôles** : V12, V15 si cursive.
- **Interdits** : modèle cursif dessiné ou généré (MP-CC-11) ; mot non décodable pour la classe.
- **Statut** : testé sur rendu (2.11.2026, LibreOffice, PDF regardé page par page, schéma OOXML valide) ; dimensions = inférence de conception.

### G16 — Planche de recherche visuelle

- **Usage** : attention sélective, vocabulaire, repérage (TR01, TR02, BDRP-A2). La cible se donne par une image ou par un mot.
- **Structure** : consigne ; planche dense de formes ; nombre de cibles connu de l'enseignant·e.
- **Dimensions** : planche de 16 × 13 cm ; 7 cibles parmi 63 formes de 10 à 12 mm (valeurs de l'essai).
- **Recette** : R11 (formes simples ou icônes de la banque IC), jamais une image dense générée ; placement par programme avec une **distance minimale de 3 mm** entre deux formes (aucun contact, aucun chevauchement), vérifiée par calcul avant le rendu.
- **Contrôles** : compte des cibles par programme ; distance entre formes par programme ; V12.
- **Interdits** : reprendre un album ou des dessins tiers ; texte dans l'image (MP-I-05).
- **Statut** : testé sur rendu (2.11.2026, LibreOffice, PDF regardé page par page, schéma OOXML valide) ; dimensions = inférence de conception.

### G17 — Série d'automatisation chronométrée

- **Usage** : automatiser des faits déjà compris (TR02, BDRP-A3, MF63).
- **Structure** : deux séries de 10 items en deux blocs ; sous chaque série, cases « mon temps » et « mon record ».
- **Dimensions** : lignes de 0,9 cm ; quatre colonnes de 4 cm ; case temps de 1 cm.
- **Recette** : R14 (`grille`).
- **Contrôles** : V1 à V10.
- **Interdits** : introduire une notion nouvelle ; afficher les temps ou les comparer entre élèves.
- **Statut** : testé sur rendu (2.11.2026, LibreOffice, PDF regardé page par page, schéma OOXML valide) ; dimensions = inférence de conception.

### G18 — Grille croisée de nombres avec code

- **Usage** : double autovalidation par les cases croisées et par un message (TR03, BDRP-A6, MF64).
- **Structure** : calculs ; grille de 3 × 3 chiffres ; table résultat → lettre, ; six cases pour le message. Les consignes disent où écrire : « Cherche chaque résultat dans le tableau et lis sa lettre. », puis « Écris les lettres dans les six cases, dans l'ordre … » (V21 : aucune consigne « Écris » sans zone désignée).
- **Dimensions** : cases de 1,2 cm ; table de 16 cm.
- **Recette** : R14, avec contrôle par programme de la grille et du message.
- **Contrôles** : V11 (lignes et colonnes concordent ; chaque résultat donne une seule lettre) ; V21 : la consigne indique le sens de lecture de la grille (« un chiffre par case : chaque ligne de gauche à droite, chaque colonne de haut en bas »).
- **Interdits** : message trop prévisible ; grille non vérifiée par programme.
- **Statut** : testé sur rendu (2.11.2026, LibreOffice, PDF regardé page par page, schéma OOXML valide) ; dimensions = inférence de conception.

### G19 — Tracé de chemin orienté

- **Usage** : motricité fine et orientation au cycle 1 (TR09, BDRP-A7, P23).
- **Structure** : échelle en quatre niveaux, de gauche à droite : 1 droit, 2 courbe, 3 zigzag arrondi, 4 labyrinthe. Point noir au départ, barre à l'arrivée.
- **Dimensions** : couloirs de 20, 16 et 11 mm ; labyrinthe de 6 × 10 cases de 13 mm. Dessin de 16 × 15 cm.
- **Recette** : R11 (`couloir`, `arrondir`, `labyrinthe`), inséré dans le .docx à l'échelle 1. Source vectorielle livrée en SVG et en PDF.
- **Contrôles** : V16 (largeur, séparation, chemin unique).
- **Interdits** : angle vif dans un couloir (le bord intérieur se croise) ; consigne écrite seule pour des non-lecteurs.
- **Statut** : testé sur rendu (2.11.2026, LibreOffice, PDF regardé page par page, schéma OOXML valide) ; largeurs = inférence de conception, à éprouver avec des élèves de 1P.

### G20 — Dictée réfléchie

- **Usage** : orthographe raisonnée (TR70, BDRP-I3, P24, MF75). Trois formes : **G20-a** à trous, **G20-b** à choix, **G20-c** négociée.
- **Structure** : le texte dicté figure dans la partie enseignant·e seulement. G20-a : phrases à lacunes, puis une justification. G20-b : tableau de paires de formes existantes à entourer, puis une justification. G20-c : phrase individuelle, phrase du groupe, tableau « le mot / notre raison ».
- **Dimensions** : lacunes de 6 cm (R2) ; cellules ≥ 1 cm ; lignes de 1 cm (R1a).
- **Recette** : R1a, R2, R14.
- **Contrôles** : V1 à V10.
- **Interdits** : texte à corriger, forme fautive imprimée (X-13) ; G20-b propose seulement des formes existantes, sans phrase affichant la mauvaise forme (§ 3.7) ; texte à dicter absent de la partie enseignant·e (V21) ; page à moitié vide : ajouter des phrases ou des paires plutôt qu'aérer à l'excès (MP-O-14).
- **Statut** : testé sur rendu (2.11.2026, LibreOffice, PDF regardé page par page, schéma OOXML valide).

### G21 — Imagier et scène à légender (3.11.2026)

- **Usage** : nommer les éléments d'une scène ou d'une planche d'images : vocabulaire d'un thème, en langue 2 d'abord (TR16, BDRP-C8, MF01, MF17, MF39, F29). Trois formes : **G21-a** étiquettes-mots à découper et à coller dans des cases (élèves qui ne lisent pas encore la langue) ; **G21-b** mot à écrire sur une ligne numérotée ; **G21-c** écoute : l'enseignant·e dit un mot, l'élève écrit le numéro (variante de MF39, sans étiquettes).
- **Structure** : en-tête R7 (titre dans la langue cible, objectif en « je ») ; consigne ; **scène sans aucun texte** avec des pastilles blanches numérotées de 1 à n, posées par le document et non par le dessin ; lignes ou cases numérotées, en deux colonnes ; G21-a : bande d'étiquettes en bas, ordre mélangé, bords en pointillés. Partie enseignant·e : corrigé numéroté, déroulement, réemploi (J2, J7, SP11).
- **Image** : trois sources admises, dans cet ordre : (1) scène dessinée en R11 à partir de formes simples (l'essai) ; (2) image fournie par l'enseignant·e (photo, dessin, illustration sous licence) ; (3) image générée, **sans aucun texte ni enseigne lisible** (MP-I-05), relue élément par élément. Chaque élément est à **dénomination univoque** (un seul mot attendu, sans synonyme courant), bien séparé des autres ; 6 à 12 éléments. Les numéros sont posés par `scene_numerotee`, jamais générés.
- **Mots** : en langue étrangère, **l'article fait partie du mot** (der Baum, a dog) et figure sur l'étiquette et dans le corrigé ; aucune forme fautive ; orthographe et genre vérifiés par l'enseignant·e dans le moyen d'enseignement (l'IA le signale : statut non vérifié). La consigne est dans la langue cible dès 5P, doublée en français au besoin (cadrage).
- **Dimensions** : scène de 16 × 9,5 cm (G21-b) ou 14,5 × 8,6 cm (G21-a) ; pastilles de 4 mm de rayon, numéro en 11 pt ; 8 lignes de 1,1 cm en deux colonnes (G21-b) ou 8 cases de 1,4 cm (G21-a) ; étiquettes de 4 × 1,2 cm, quatre par rangée. Hauteur : 3 + 9,5 + 0,2 + 4,4 + 1,2 ≈ 18,5 cm (G21-b) ; G21-a ≈ 21 cm.
- **Recette** : R7 ; R11 (`Dessin`) ou image fournie ; `scene_numerotee` (pastilles) ; `lignes_numerotees` (lignes ou cases) ; `bande_etiquettes` (R8, MP-J-03, MP-J-05) ; Annexe I-C.
- **Contrôles** : V1 à V10, V12 (étiquettes) ; V21 : `verifier_imagier` (autant de repères que de mots, mots tous différents, article présent) ; pastilles lisibles et non superposées (contrôle par programme : distance ≥ 2 rayons) ; sur le rendu, chaque numéro désigne un seul élément.
- **Interdits** : texte ou enseigne lisible dans l'image ; numéro dessiné dans l'image générée ; élément ambigu (vélo ou bicyclette, banc ou bank) sans choix explicité dans le cadrage ; étiquettes fautives (X-13) ; dessin tiers reconnaissable ; personnage identifiable.
- **Statut** : testé sur rendu (3.11.2026, LibreOffice, PDF regardé page par page, schéma OOXML valide), G21-a et G21-b, scène R11 ; image générée non testée dans le document (le visuel de la carte R16 en est un exemple, hors fiche) ; dimensions = inférence de conception.

### G22 — Lignes d'écriture, lignage romand (20.11.2026 ; rendu contrôlé, non testé en classe)

- **Usage** : page ou bande de lignes pour l'écriture liée, au lignage en usage en Suisse romande : quatre lignes et trois couloirs égaux, **sans quadrillage** (le lignage Seyès français n'est pas utilisé).
- **Structure** : de haut en bas, ligne de plafond en pointillés, ligne du corps des lettres en trait fin, **ligne de base en trait épais**, ligne de plancher en pointillés. Le corps des lettres s'écrit entre la ligne du corps et la ligne de base ; les lettres hautes montent jusqu'au plafond, les lettres basses descendent jusqu'au plancher.
- **Repère en couleur** (facultatif, cycle 1) : couloirs « ciel, herbe, terre » ; la position suffit à les distinguer, la couleur s'ajoute (MP-C-05).
- **Dimensions** : module (hauteur d'un couloir) de 7 mm pour l'entrée dans l'écriture (mesuré sur le document « Lignes, document vertical » de la BDRP : 6,9 mm) ; 4 mm, puis 2,5 mm ou 2 mm ensuite (**indication de l'auteur, non vérifiée à une source officielle**) ; 8, 14 ou 20 lignes d'écriture par page A4.
- **Recette** : R11 : `lignage_romand(base, module_mm, couleurs, entete)` écrit la page en PDF ; inséré dans un .docx, le PDF garde son échelle. **Bande dans une fiche** : `bande_lignage` (R1c) place quelques lignes romandes dans une zone d'écriture, à la place des lignes simples. **Livret A5** : `livret_ecriture(base, module_mm, couleurs, feuilles, titre)` produit un cahier à plier (deux pages A5 par feuille A4 paysage, couverture avec un cartouche vide pour le prénom, sans ligne à remplir, repères du pli) : impression recto-verso avec retournement sur le bord court, pliage, agrafage dans le pli.
- **Modèle d'écriture** : les lettres ne sont jamais dessinées par l'IA ; l'enseignant·e écrit le modèle à la main ou avec la police d'écriture liée de son canton (R10).
- **Contrôles** : V15 si un modèle en écriture liée est ajouté ; impression à 100 %, sans « ajuster à la page ».
- **Interdits** : quadrillage Seyès ; lettre tracée ou générée par l'IA ; module inférieur à 2 mm.
- **Statut** : un format par tranche d'âge produit en PDF et regardé le 20.11.2026 (police Liberation Sans pour l'essai) ; non imprimé, non testé en classe ; le module de 7 mm reproduit le document de la BDRP, les autres modules restent à confirmer avec les cahiers de l'établissement.

### G23 — Syllabes et sons (20.11.2026 ; rendu contrôlé, non testé en classe)

- **Usage** : segmenter un mot en syllabes orales, puis en sons (conscience phonologique, 1P à 4P).
- **Structure** : bandeau de titre et de consigne, ligne du prénom, grille de 8 ou 12 cases. Par case : un cadre en pointillés pour l'image (collée par l'élève, ou insérée par l'enseignant·e), le mot écrit, une ligne « syllabes » où l'élève dessine un carré par syllabe, une ligne « sons » où il dessine un jeton par son.
- **Dimensions** : case de 4,65 × 11,7 cm (8 mots) ou de 4,65 × 7,8 cm (12 mots) ; lignes de 1,1 cm.
- **Recette** : R11 : `fiche_syllabes_sons(base, mots, colonnes, titre, taille_pt, images)` ; `images` : chemins des images, dans l'ordre des mots (banque d'icônes de la boîte à outils, ou images de l'enseignant·e).
- **Corrigé** : le nombre de syllabes et de sons de chaque mot, donné à l'enseignant·e à part ; les syllabes sont **orales** (« poule » : une syllabe orale à Lausanne, deux dans le Midi : choisir la norme de la classe et l'annoncer).
- **Contrôles** : V1 à V10 ; chaque image représente le mot sans ambiguïté.
- **Interdits** : mot dont le découpage en sons prête à discussion sans que le corrigé le signale ; image générée non relue.
- **Statut** : deux formats produit en PDF et regardé le 20.11.2026 (police Liberation Sans pour l'essai) ; non imprimé, non testé en classe ; cadres d'images vides dans l'essai.

### G24 — Maisons des nombres (21.11.2026 ; rendu contrôlé, non testé en classe)

- **Usage** : décompositions additives d'un nombre (cycle 1) : le nombre est dans le toit, chaque étage reçoit deux nombres dont la somme est celle du toit.
- **Structure** : bandeau, ligne du prénom, 2 à 6 maisons par page ; étages de 1,1 cm au moins, deux cases par étage.
- **Recette** : R11 : `maison_des_nombres(base, nombres, titre)` ; jusqu'à 6, autant d'étages que de décompositions (n + 1) ; au-delà, la moitié (les décompositions symétriques ne sont pas répétées).
- **Corrigé** : toutes les décompositions, données à l'enseignant·e ; l'ordre des étages est libre.
- **Interdits** : étage prérempli avec une erreur ; nombre du toit supérieur à 20 sans raison didactique.
- **Statut** : deux pages (3 à 6, 7 à 10) produit en PDF et regardé le 21.11.2026 (police Liberation Sans pour l'essai) ; non imprimé, non testé en classe.

### G25 — Reproduction sur quadrillage (21.11.2026 ; rendu contrôlé, non testé en classe)

- **Usage** : repérage dans le plan, tracé à la règle : reproduire une figure du modèle sur un quadrillage vide.
- **Structure** : en haut, le modèle sur quadrillage ; en bas, le même quadrillage vide, ou seulement ses nœuds (`points=True`, plus difficile) ; carreaux de 1,4 cm.
- **Recette** : R11 : `reproduction_quadrillage(base, figure, cases, points, titre)` ; figures fournies dans `FIGURES` (maison, bateau, sapin, fusée) ; une figure personnelle se donne par ses lignes brisées, points aux nœuds.
- **Contrôles** : la fonction refuse une figure qui sort du quadrillage ; tous les sommets sont sur des nœuds.
- **Interdits** : figure dont un sommet tombe hors d'un nœud ; modèle et quadrillage de tailles différentes.
- **Statut** : quatre figures produit en PDF et regardé le 21.11.2026 (police Liberation Sans pour l'essai) ; non imprimé, non testé en classe.

### Supports de classe et mises en page de projets (G26 à G31, 21.11.2026)

- **Principe** : six gabarits qui ne sont pas des exercices : des supports d'affichage (G26, G27) et des mises en page pour les projets des élèves (G28 à G31). Ils se remplissent à la main ; l'IA peut aussi en préparer le contenu, que l'enseignant·e relit.
- **G26 — Calendrier mensuel** : `calendrier_mensuel(base, annee, mois, titre)` : un mois par page, semaine du lundi au dimanche, jours calculés par programme, samedi et dimanche grisés ; cases de 4,7 cm ou plus pour écrire la date, le temps qu'il fait, un événement.
- **G27 — Étiquettes de l'horaire** : `etiquettes_horaire(base, etiquettes, colonnes, rangees, taille_pt, mention)` : 16 étiquettes de 9,3 × 3,3 cm, un cadre pour le pictogramme et le nom de l'activité ; repères de coupe (MP-J-12). Les pictogrammes viennent de la banque d'icônes ou sont dessinés par les élèves.
- **G28 — Livret à onglets** : `livret_a_onglets(base, onglets, titre, pas_mm)` : une feuille par onglet (3 à 8) ; chaque feuille est coupée 1,4 cm plus court que la suivante, les onglets restent visibles en bas, agrafage en haut.
- **G29 — Page de journal de classe** : `page_journal(base, titre, articles)` : bandeau du titre, numéro et date, 2 à 4 articles sur deux colonnes (titre, cadre d'illustration, lignes de 9 mm, signature).
- **G30 — Planche de bande dessinée** : `planche_bd(base, rangees, titre)` : cases vides numérotées, par bandes (par exemple 2, 3 et 2 cases), bandeau du titre et de l'auteur·e.
- **G31 — Plan d'exposé** : `plan_expose(base, parties, titre)` : sujet et question de départ, 2 à 4 parties (idée principale, mots-clés, image à montrer), conclusion, sources.
- **Vigilance** : pas de photo d'élève ni de nom complet dans un journal diffusé hors de la classe ; les sources d'un exposé sont notées par l'élève.
- **Statut** : un à quatre exemples par gabarit produit en PDF et regardé le 21.11.2026 (police Liberation Sans pour l'essai) ; non imprimé, non testé en classe ; découpe et agrafage du livret à onglets non essayés.

### Variantes de G11 et de G12

- **G11-b — Colorier selon un critère** (BDRP-A4) : neuf dessins au plus, une couleur, critère explicite lié à l'objectif. Grille de 3 × 3 cellules de 5,33 × 4,2 cm (R14). Le critère ne porte jamais sur l'esthétique. Statut : testé sur rendu (2.11.2026, LibreOffice, PDF regardé page par page, schéma OOXML valide).
- **G11-c — Coloriage codé** (BDRP-A8, MF64) : chaque case porte un calcul, le résultat renvoie à un crayon numéroté **et** à un motif nommé en mots (MP-C-05). Grille de 7 × 6 cases de 2,28 × 1,4 cm. Un code fondé sur la seule couleur est interdit (X-08). La légende nomme chaque motif par un mot courant que l'élève connaît (« rayures », « points », « quadrillage »), jamais par un terme technique (« zone rayée ») ; chaque motif de la légende est aussi dessiné (R11) à côté de son nom. Statut : testé sur rendu (2.11.2026, LibreOffice, PDF regardé page par page, schéma OOXML valide).
- **G12-b — Plateau de tri à étiquettes mobiles** (BDRP-A5, TR38) : plateau de deux colonnes de 8 cm, chacune à **cases d'accueil de 8 × 3,5 cm** (la cellule du plateau ; une par étiquette attendue, plus une case vide par colonne, annoncée dans la consigne) ; puis planche d'**étiquettes de 6 × 2,5 cm** (image ou mot), imprimée en double pour l'autocorrection, bords en pointillés (MP-J-05). La case mesure au moins l'étiquette + 0,5 cm par côté (MP-J-10, `verifier_case_piece` : jeu de 1 cm et 0,5 cm) ; les deux dimensions de l'étiquette et de la case figurent dans la fiche technique. La planche d'étiquettes, dernière planche à nombre de pièces fixé, est déclarée en exception de V20 (73 % sur l'essai). Conditionnement : plastification, velcro. Images à dénomination univoque. Statut : testé sur rendu (2.11.2026) ; révision du 2.11.2026, suite : la planche d'étiquettes de 5,33 × 4,2 cm reprise de G11-b dépassait les cases du plateau ; dimensions = inférence de conception.

## 3.4 Fiche-type pour un nouveau gabarit

Tout format nouveau DOIT être décrit ainsi avant usage : **Usage · Disposition · Zone de réponse (dimensions) · Items · Hauteur estimée · Recette (R1 à R8) · Vigilance**, puis reporté dans la fiche technique. Pour un gabarit de jeu, la fiche-type précise en plus la **pièce** (dimensions, contenu) et le **statut** (testé ou non testé).

Les fiches ajoutées en v7.2 sont présentées sous une forme condensée : **Usage · Structure · Dimensions · Recette · Contrôles · Interdits** (la structure reprend la disposition et les items ; les dimensions, la zone de réponse et la hauteur ; les interdits, la vigilance).

## 3.5 Correspondances patron × gabarit × micro-format
<!-- modules : fiches, jeux, sequences -->

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

## 3.6 Différenciation et mise en page (MP-D)
<!-- modules : fiches, differenciation -->

| Code | Règle | Niveau |
|---|---|---|
| MP-D-01 | Aucune étiquette de niveau évaluative sur la fiche élève. Un repère neutre est admis : symbole discret en en-tête (♣ ♦ ♠), lettre de version, items facultatifs marqués ★. **Étoiles de difficulté, sur demande** : si l'enseignant·e le demande, les exercices d'une fiche ou les cartes d'un jeu PEUVENT porter une à trois étoiles, de la tâche la plus simple à la plus difficile ; les étoiles décrivent la tâche, jamais l'élève ni un groupe d'élèves ; une ligne les explique à l'élève (« Choisis ton point de départ ») ; elles sont dessinées ou vérifiées sur le rendu (R6). Sans demande, le repère reste neutre. | DOIT |
| MP-D-02 | Deux dispositifs possibles : **parcours sur la même fiche** (items a-c, a-d, a-e ; aide-mémoire pour un parcours) ou **versions parallèles** (mêmes exercices, mêmes phrases et mêmes lettres d'items ; seuls l'étayage et l'étendue changent), ce qui permet une correction commune et un changement de version en cours de route. Autour d'une **fiche unique**, sans tripler la fiche (leviers : contenus, processus, productions, structures ; Forget, 2018) : difficulté croissante, chacun choisissant son point de départ avec un repère neutre ou, sur demande, des étoiles de difficulté (MP-D-01) ; noyau commun en haut de la fiche et prolongements facultatifs en bas ; aides détachées en libre accès, réutilisables d'une fiche à l'autre (J15) ; quantité plutôt qu'objectif (« au moins quatre exercices sur huit, dont le numéro 5 ») ; forme de la réponse au choix (écrire, entourer, relier, manipuler puis dessiner, expliquer oralement) ; organisation (seul, binôme d'entraide, petit groupe avec l'enseignant·e) ; trame stable (objectif, exemple, exercices gradués, défi). Si un élève choisit toujours trop facile ou trop difficile, l'enseignant·e oriente son point de départ. | DEVRAIT |
| MP-D-03 | Chaque version ou parcours respecte son propre budget de page (Étape 2). | DOIT |
| MP-D-04 | Les modalités d'attribution (diagnostic court, choix accompagné) et la consigne « une version décrit un besoin du moment, pas un niveau d'élève » figurent dans la partie enseignant·e. | DEVRAIT |

## 3.7 Orthographe : par défaut, l'élève ne voit que des formes correctes (MP-CC-11)
<!-- modules : noyau -->

**Règle (DOIT).** Par défaut, aucun support destiné à l'élève (fiche, carte, étiquette, affiche, corrigé élève) ne montre de mot mal orthographié, d'accord ou de conjugaison fautifs, ni de forme inexistante. La règle vaut pour les consignes, les exemples, les items, les distracteurs, les banques de mots et les phrases « à corriger ». La partie enseignant·e peut, elle, nommer les erreurs typiques. Une seule exception, sur décision explicite de l'enseignant·e : l'analyse d'erreurs encadrée décrite ci-dessous.

#### Pour travailler le jugement orthographique sans montrer de forme fautive

- **Justifier une forme correcte** : « Pourquoi écrit-on *allée* dans cette phrase ? »
- **Comparer des formes correctes** dans des contextes différents : *il est allé* / *elle est allée*.
- **Trier des formes correctes** selon une règle (participes en -é, -i, -u).
- **Choisir la règle** qui explique une forme donnée.
- **Relire sa propre production** avec une liste de contrôle : l'erreur éventuelle vient de l'élève, pas du support, et l'élève écrit ensuite la forme correcte.
- **Choisir entre formes existantes**, chacune correcte dans l'absolu (*a* / *à*, *ai* / *suis*), présentées comme options et sans phrase complète affichant la mauvaise forme. *[Règle validée par l'enseignant·e responsable du référentiel (v6.1) : admis, car aucune forme écrite fautive n'est montrée.]*

#### Exception encadrée : l'analyse d'erreurs (décision du 21.11.2026)

Sur **décision explicite de l'enseignant·e**, **à partir de la 5P** et pour une **notion déjà enseignée**, une activité d'analyse d'erreurs dont l'objectif est le jugement orthographique PEUT montrer des formes fautives, aux quatre conditions suivantes, toutes obligatoires :

1. chaque forme fautive est **marquée comme erreur** : barrée ou encadrée, avec la mention « erreur à expliquer » ;
2. la **forme correcte** figure sur le même support, ou l'élève l'écrit aussitôt, avec la **règle** qui la justifie ;
3. une forme fautive n'apparaît **qu'une fois**, jamais dans une banque de mots, un distracteur ou un exemple ;
4. le support ne sert pas à l'**apprentissage initial** de la notion.

L'IA n'applique cette exception que si l'enseignant·e la demande ; quand on lui demande de travailler le jugement orthographique dès la 5P, elle peut la mentionner parmi les possibilités, après les alternatives ci-dessus. Elle vérifie les quatre conditions et les cite dans le rapport de conformité (V10). **Au cycle 1 et pour les lecteurs débutants, la règle ne connaît pas d'exception.** Les **erreurs de raisonnement** (calcul, démarche) peuvent être présentées dès que leur analyse est l'objectif, avec correction et explication (J14, patron P04).

*Fondement (références non vérifiées) : des travaux indiquent qu'être exposé à des graphies erronées peut perturber la mémoire orthographique (par exemple Brown, 1988, à contrôler) ; l'étude d'exemples erronés est aussi un dispositif d'apprentissage documenté, surtout en mathématiques. L'exception limite l'exposition à des élèves lecteurs, à une notion enseignée et à une forme marquée.*

**Images générées par IA (MP-I-05)** : le texte qu'un générateur d'images incruste est souvent fautif ou inexistant. Une image destinée à l'élève ne contient donc aucun texte généré ; le texte nécessaire est ajouté dans le document, puis relu. Voir aussi le socle commun des visuels (Annexe II-A, A.1).

**Contrôle** : relecture orthographique de tout le texte élève avant livraison (V10).

## 3.8 Catalogue des gabarits de jeu (J1 à J38)
<!-- modules : jeux -->

Les gabarits J décrivent les **pièces imprimées** d'un jeu (dominos, cartes, plateau, dé). Ils sont distincts des gabarits d'exercice et de support G1 à G31 et suivent la fiche-type du § 3.4. La règle du jeu, la carte-mémoire et la trace individuelle relèvent des gabarits G et du dossier de jeu GF-F (§ 6.1). Les dimensions sont données pour 5P-6P (14 pt). J1 a été testé en v7 ; J7 à J16 ont été testés sur rendu en v7.2 ; pour J2 à J6, toute dimension est une **inférence de conception, à tester**. J17 à J20 (19.11.2026) sont dessinés par le code de l'Annexe I-C : rendu contrôlé, non testés en classe. J21 à J38 (20.11.2026) de même.

### Règles communes aux jeux (MP-J)

| Code | Règle | Niveau |
|---|---|---|
| MP-J-01 | **Unicité** : chaque question admet une seule pièce correcte dans tout le lot, pas seulement parmi les pièces voisines. | DOIT |
| MP-J-02 | **Aucun indice non visé** : aucune pièce ne se trouve par le radical, la longueur, la position sur la planche ou l'ordre d'impression. Il faut au moins trois formes du même mot dans le lot. | DOIT |
| MP-J-03 | **Ordre d'impression mélangé** : deux pièces voisines dans la solution ne sont jamais voisines sur la planche. | DOIT |
| MP-J-04 | **Autocorrection intégrée** : boucle qui se ferme, verso, ou carte-solution. Depuis la v7.2, la règle s'étend à tout objet imprimé destiné au travail autonome (rabat, forme de la découpe, double impression, grille croisée). Une carte que l'élève tire d'une pioche ne porte jamais sa réponse au verso (MP-J-14). | DEVRAIT |
| MP-J-05 | **Traits** : les traits de coupe sont en pointillés ; les séparations internes, en trait plein épais. | DOIT |
| MP-J-06 | Par défaut, **aucun repère de niveau** sur les pièces (MP-D-01) ; le lot se repère par la couleur du papier et par le contenu. Si l'enseignant·e demande des étoiles de difficulté, elles sont admises sur les cartes, aux conditions de MP-D-01. | DOIT |
| MP-J-07 | **Règle du jeu** en étapes numérotées, une action par phrase, avec un exemple résolu fait de pièces hors lot. Elle répond à **cinq questions** : quel est le but, et qu'apprend-on en jouant ; quel matériel, pour combien de joueurs ; que fait-on à son tour, étape par étape ; que se passe-t-il en cas d'erreur, et comment vérifie-t-on la réponse ; quand la partie est-elle terminée. Pour que chacun travaille, et pas seulement celui qui joue : groupes de trois ou quatre ; **tout le monde répond** (chaque élève note sa réponse, par exemple sur une ardoise, puis celui dont c'est le tour la dit) ; un·e vérificateur·trice tient le corrigé et change à chaque tour ; une partie modèle est jouée devant la classe ; le but d'apprentissage est annoncé avant de jouer (« à la fin, vous saurez… »). | DOIT |
| MP-J-08 | **Carte-mémoire** : elle sert à vérifier après la pose (P14), pas à chercher avant ; la règle le dit. | DEVRAIT |
| MP-J-09 | **En-tête** : la fiche de trace individuelle porte l'en-tête R7 ; la règle du jeu et les planches, matériel de groupe, portent un titre sans ligne Prénom et Date. | DEVRAIT |
| MP-J-10 | **Pièce mobile et case d'accueil** : toute case destinée à recevoir une pièce mobile (étiquette, carte, jeton, pince) mesure au moins la pièce + 0,5 cm par côté, en largeur et en hauteur ; les deux dimensions de la pièce et de la case figurent dans la fiche technique ; contrôle par programme (`verifier_case_piece`, Annexe I-C) et sur le rendu (V12). S'applique aussi aux fiches (G12-b, plateaux, tableaux à étiquettes). (révision du 2.11.2026, suite) | DOIT |
| MP-J-11 | **Surface de la planche** : une planche de pièces à découper (cartes, dominos, étiquettes, pièces, modèles) occupe **toute la surface utile de la page** — en A4 portrait, environ 18,6 × 26,4 cm, avec des marges d'environ 1,2 cm sur les côtés et 1,6 cm en haut et en bas. On **agrandit les pièces** ou on **change leur disposition** (nombre de colonnes et de rangées) au lieu de laisser une bande vide ; la zone restée vide ne dépasse pas une demi-hauteur de pièce. Les dimensions retenues et le calcul (colonnes × largeur, rangées × hauteur) figurent dans la fiche technique. La planche, tableau à hauteur exacte, échappe au budget de 22 cm (MP-O-11) ; son rendu est contrôlé (V12). Le texte et l'image de chaque pièce sont centrés sur la pièce, contrôlés sur le rendu. (révision du 19.11.2026) | DOIT |
| MP-J-12 | **Repères de coupe** : toute planche à découper porte des **repères de coupe au bord de la feuille**, pour la coupe au massicot : un trait fin (0,5 pt, noir, environ 0,45 cm de long) dans le prolongement de **chaque** ligne de coupe — en haut et en bas pour les coupes verticales, à gauche et à droite pour les coupes horizontales —, séparé de la planche par environ 0,25 cm et à au moins 0,5 cm du bord de la feuille (zone imprimable). Les pointillés restent pour la coupe aux ciseaux (MP-J-05). La mention de la planche se place dans la marge du haut, sans toucher les repères. (révision du 19.11.2026) | DOIT |
| MP-J-13 | **Choix présenté** : avant de produire un jeu, et chaque fois que l'enseignant·e demande quelles sont les possibilités, l'IA **montre le panorama des jeux** (image produite par `panorama_jeux`, Annexe I-C ; même image dans la page web du guide et dans le fichier « Panorama des jeux » de la boîte à outils). **Le panorama ne contient que des miniatures tirées des documents réels** — la page elle-même, réduite, du modèle Word ou de la planche prête à imprimer : l'enseignant·e obtient ce qu'il ou elle voit ; un gabarit sans document n'y figure qu'en liste, sans image, et l'IA ne dessine jamais de schéma à la place (20.11.2026). Elle présente ensuite en une ligne chacun les deux ou trois gabarits qui conviennent à la demande, donne sa recommandation et **attend le choix**. Pour un gabarit à variantes (formes J5-a à J5-d, variantes de J2, J3 et J4), elle présente les variantes de la même façon. Quand le degré est connu, elle montre la page de miniatures de la tranche d'âge (`miniatures_tranche`), avec le nombre de pièces ou de cases de chaque format. Si elle ne peut ni exécuter le code ni afficher une image, elle donne la liste des noms des jeux et renvoie au fichier. Dans ce qu'elle présente à l'enseignant·e, elle désigne chaque jeu ou exercice par son nom, sans code ; les panoramas et les mentions de planche ne portent pas de code (21.11.2026). Quand un **modèle Word à remplir** ou une **planche prête à imprimer** existe pour le gabarit retenu (liste à la fin du § 3.8), elle le signale. Pour une fiche, quand l'enseignant·e demande quels exercices sont possibles, elle montre de la même façon le **panorama des exercices** (`panorama_exercices`, gabarits G1 à G23 ; fichier « Panorama des exercices » de la boîte à outils). Exception : l'enseignant·e a déjà nommé le gabarit ou la forme. (19.11.2026) | DOIT |
| MP-J-14 | **Carte tirée, dos neutre** : une carte que l'élève tire d'une pioche ou reçoit face cachée (carte-défi d'un plateau, carte d'appel, carte de memory) a un **dos neutre et identique** : ni réponse ni indice au verso, parce que l'élève verrait la réponse avant de répondre. Chaque carte porte un numéro ; le contrôle passe par une **feuille de solutions numérotée** par lot, tenue par un·e camarade ou retournée sur la table. **Avant de produire les cartes, l'IA pose deux questions** : (1) dos **à motif** ou dos **blanc** ? (2) **avec une mention personnelle** au dos — par exemple le nom du jeu, ou une catégorie de cartes : « Défi », « Bonus », « Malus », « Chance » — ou **sans** ? Sans réponse, elle retient le dos à motif sans mention et le signale. **Dos à motif** (`dos_a_motif`), comme celui d'une carte à jouer : des lignes fines (losanges, carreaux ou vagues) remplissent un cadre aux angles arrondis, tracé d'un trait fin à environ 3 mm du bord de la carte ; la marge reste blanche. Le motif est le même sur toutes les cartes du jeu, il gêne la lecture par transparence et donne son unité au jeu ; un motif différent par jeu permet de trier des jeux mélangés. **Dos blanc** : rien n'est imprimé au verso ; à réserver à un papier assez épais pour que le recto ne se lise pas par transparence. **Mention personnelle** : la même sur toutes les cartes d'une pile, en gras dans un cartouche gris au centre de la carte (paramètre `texte`) ; jamais une mention qui distingue deux cartes d'une même pile ; plusieurs catégories donnent plusieurs piles, donc une planche par catégorie. Le cadre rend visible un décalage du recto-verso : essai d'impression avant de tirer tout le jeu (V13). Le verso-réponse reste réservé aux cartes que l'élève tient lui-même, question vers lui (J4, J14), et à la carte à pinces (J10). (19.11.2026) **Liseré** : chaque carte d'un jeu de cartes porte un cadre à coins arrondis, tracé à 3 mm du trait de coupe ; la teinte de la carte s'arrête au cadre et la marge reste blanche, comme sur une carte à jouer. Les modèles Word de la boîte à outils le portent déjà : pour un jeu de cartes en .docx, partir du modèle plutôt que d'un tableau neuf, qui ne le porte pas. En PDF, `planche_pdf(..., lisere=True)`, `cartes_categories` et `cartes_mots_interdits` le tracent (`lisere_cartes`) ; sans modèle Word, produire la planche de cartes en PDF. Pas de liseré sur un domino, un puzzle ou une tuile. (21.11.2026) | DOIT ; le liseré et le motif du dos sont des conventions (priorité 5) |

*MP-J-09 précise MP-O-12 pour le matériel de groupe (inférence de conception, conforme au test du 30.10.2026). MP-J-10 répond au défaut de G12-b (étiquettes plus grandes que les cases) relevé par la revue indépendante du 2.11.2026. MP-J-11 et MP-J-12 répondent à la demande de l'auteur du 19.11.2026 : planches qui laissaient le bas de la page vide, absence de repères pour le massicot ; règles appliquées au memory des consignes (19.11.2026, rendu PDF contrôlé, non testé en classe). MP-J-13 répond à sa demande du même jour : l'enseignant·e ne connaît pas les possibilités tant que l'IA ne les montre pas.*

### J1 — Domino-boucle (testé)

- **Usage** : entraînement et rappel actif d'une correspondance question ↔ réponse (conjugaison, calcul, mot ↔ image), avec autocorrection par la fermeture de la boucle.
- **Pièce** : domino de 9,3 × 3,3 cm, en deux moitiés de 4,65 cm (révision du 19.11.2026, MP-J-11 ; auparavant 8 × 2,5 cm). Moitié gauche : la réponse, en gras. Moitié droite : la question (par exemple le sujet, puis le verbe entre parenthèses, sur deux lignes). Texte de 16 à 20 pt, même corps sur toute la planche.
- **Disposition** : planche de 2 × 8 dominos sur toute la surface utile (18,6 × 26,4 cm) ; repères de coupe au bord de la feuille (MP-J-12) ; mention dans la marge du haut ; traits de coupe en pointillés, séparation centrale en trait plein épais ; ordre d'impression mélangé ; une planche par page.
- **Zone de réponse** : aucune écriture ; le geste est de poser le domino.
- **Items** : 12 à 16 dominos par boucle ; chaque réponse est unique dans la boucle ; au moins trois formes du même mot (MP-J-02). Deux boucles équivalentes permettent la différenciation (MF46).
- **Hauteur** : 8 × 3,3 = 26,4 cm (calculé ; rendu PDF contrôlé le 19.11.2026). Version antérieure en .docx : mention 0,9 cm + rangées × 2,5 cm, soit 20,9 cm pour 8 rangées (calculé ; 21,1 cm rendus lors du test, 20,7 cm au contrôle des recettes v7).
- **Recette** : R8 (planche de pièces à découper) : en PDF, `planche_pdf` (Annexe I-C), repères de coupe compris, une planche par fichier ; en .docx, saut de page avant chaque planche.
- **Vigilance** : contrôler l'unicité et la fermeture (V11 ; script en Annexe I-C) ; éviter les verbes à voyelle initiale avec *je* (élision) ; imprimer sur papier épais ; la règle précise que la carte-mémoire sert à vérifier après la pose (MP-J-08).
- **Statut** : testé (5P, conjugaison du présent des verbes en -er et en -ir, 30.10.2026 ; rendu PDF contrôlé). Dimensions du 19.11.2026 : planche de la boucle Lune produite en PDF avec `planche_pdf` et regardée (corps de 19,5 pt ; police Liberation Sans pour l'essai) ; non imprimée, non testée en classe.

### J2 — Memory ou appariement (non testé)

- **Usage** : associer deux éléments (mot ↔ image, calcul ↔ résultat, mot ↔ définition), soit cartes face cachée (memory), soit à découvert (appariement).
- **Pièce** : carte de 6,2 × 6,6 cm (3 × 4 cartes remplissent la page, MP-J-11) ; une information par carte ; mot de 22 pt au moins sous une image, 32 pt sur une carte-mot ; image de 5 cm au plus ; texte et image centrés.
- **Disposition** : planche de 3 × 4 cartes (18,6 × 26,4 cm), soit 6 paires par planche ; repères de coupe au bord de la feuille (MP-J-12) ; mention dans la marge du haut.
- **Zone de réponse** : aucune.
- **Items** : 6 à 12 paires ; chaque carte n'a qu'une partenaire dans le lot (MP-J-01).
- **Hauteur** : 4 × 6,6 = 26,4 cm ; marges d'environ 1,65 cm en haut et en bas (calculé ; rendu PDF contrôlé le 19.11.2026).
- **Recette** : R8 avec une seule moitié par pièce (colonnes de 6,2 cm, rangées de 6,6 cm, 3 pièces par rangée), repères de coupe compris. Jeu de cartes : partir du modèle Word (liseré en place) ou, en PDF, `planche_pdf(..., lisere=True)` (MP-J-14).
- **Vigilance** : pour la memory, aucune différence visible au dos : dos à motif encadré ou dos blanc, identique sur toutes les cartes, au choix de l'enseignant·e (`dos_a_motif`, MP-J-14) ; au cycle 1, pour des non-lecteurs, appariement image ↔ image ; aucune forme fautive (MP-CC-11).
- **Statut** : non testé ; dimensions = inférence de conception, à tester.

### J3 — Familles (non testé)

- **Usage** : classer des éléments selon une catégorie en réunissant les cartes d'une même famille (familles de mots, natures, groupes de verbes, multiples).
- **Pièce** : carte de 6,2 × 8,8 cm (révision du 19.11.2026, MP-J-11 ; auparavant 5 × 6,5 cm) ; en haut, le nom de la famille en mots ; au milieu, l'élément ; en bas, la liste des membres de la famille (pour pouvoir demander une carte).
- **Disposition** : planche de 3 × 3 cartes (18,6 × 26,4 cm) ; repères de coupe au bord de la feuille (MP-J-12) ; mention dans la marge du haut.
- **Zone de réponse** : aucune.
- **Items** : 4 à 6 familles de 4 à 6 cartes ; chaque carte appartient à une seule famille (MP-J-01).
- **Hauteur** : 3 × 8,8 = 26,4 cm (calculé ; disposition rendue en PDF le 19.11.2026).
- **Recette** : R8 avec une seule moitié par pièce (colonnes de 6,2 cm, 3 pièces par rangée, hauteur 8,8 cm) ; en PDF : `planche_pdf`, repères de coupe compris. Jeu de cartes : partir du modèle Word (liseré en place) ou, en PDF, `planche_pdf(..., lisere=True)` (MP-J-14).
- **Vigilance** : la famille est nommée en mots, jamais par la seule couleur (X-08) ; familles équilibrées ; pour une catégorie orthographique, les membres sont écrits, pas seulement nommés à l'oral (X-17).
- **Statut** : non testé ; dimensions = inférence de conception, à tester.

### J4 — Cartes de rappel recto-verso (MF18) (non testé)

- **Usage** : rappel actif, seul·e ou en duo : la question au recto, la réponse au verso ; reprises espacées (MF18, P14).
- **Pièce** : carte de 9,3 × 6,6 cm (révision du 19.11.2026, MP-J-11 ; auparavant 8 × 5 cm) ; recto : la question ; verso : la réponse.
- **Disposition** : planche recto de 2 × 4 cartes (18,6 × 26,4 cm), repères de coupe au bord de la feuille (MP-J-12), puis planche verso dont les deux colonnes sont inversées, pour une impression recto-verso sur le bord long. Sans recto-verso : carte pliée en deux (question et réponse côte à côte).
- **Zone de réponse** : aucune ; l'élève répond oralement ou sur une ardoise, puis retourne la carte.
- **Items** : 8 à 16 cartes ; une seule réponse par question (MP-J-01).
- **Hauteur** : 4 × 6,6 = 26,4 cm par planche (calculé ; disposition du recto rendue en PDF le 19.11.2026).
- **Recette** : R8 (deux planches : recto, puis verso aux colonnes inversées) ; en PDF : `planche_pdf`, puis `verso_de` pour l'ordre du verso ; les marges égales à gauche et à droite gardent les repères alignés au verso. Jeu de cartes : partir du modèle Word (liseré en place) ou, en PDF, `planche_pdf(..., lisere=True)` (MP-J-14).
- **Vigilance** : alignement recto-verso contrôlé sur une impression test (V13) ; papier assez épais pour que le verso ne se lise pas par transparence ; une fiche de suivi des reprises (MF43) peut accompagner le jeu. Ces cartes se tiennent en main, question vers l'élève : elles ne servent jamais de pioche (MP-J-14).
- **Statut** : non testé ; dimensions et inversion des colonnes = inférence de conception (calcul à confirmer sur l'imprimante de l'école).

### J5 — Plateau de parcours (révision du 19.11.2026 : quatre formes dessinées ; rendu contrôlé, non testé en classe)

- **Usage** : entraînement varié sur un parcours (jeu de l'oie, course) ; les défis sont tirés sur des cartes.
- **Principe** (révision du 19.11.2026) : le plateau a la forme d'un **parcours** que l'élève suit des yeux — serpent, escargot, chemin ou circuit —, **jamais celle d'un tableau de cases**. Il est dessiné (R11, fonction `plateau_parcours` de l'Annexe I-C) et occupe toute la surface utile de la page (18,6 × 26,4 cm, comme MP-J-11).
- **J5-a — Serpent** : ruban de cases en lacets : 5 rangées de 6 cases, reliées par 4 cases de virage ; 34 cases de 3,1 × 2,9 cm (Départ, 1 à 32, Arrivée).
- **J5-b — Escargot** : spirale ronde qui s'enroule vers le centre, comme le jeu de l'oie traditionnel : 27 cases (Départ, 1 à 25, Arrivée au centre) ; bande de 2,5 cm de large, cases d'environ 3,1 cm de long ; spirale de 17,4 × 18,6 cm, sous deux cases d'accueil pour les cartes (pioche et défausse).
- **J5-c — Chemin** : cases rondes de 2,7 cm (« pas japonais ») reliées par un pointillé, sur 6 rangs en lacets ; 34 cases (Départ, 1 à 32, Arrivée).
- **J5-d — Circuit** : boucle fermée de 24 cases de 3,1 × 3,3 cm au bord de la page (Départ, 1 à 23) ; pioche et défausse au centre ; pour une partie en plusieurs tours ou à durée fixée.
- **Choix de la forme** (inférence de conception) : serpent ou chemin quand le sens du parcours doit se lire sans aide (cycle 1, début du cycle 2) ; escargot pour un jeu de l'oie ; circuit quand la partie ne doit pas se terminer par un « premier arrivé ». Sans indication de l'enseignant·e, l'IA propose l'escargot pour un « jeu de l'oie » et le serpent dans les autres cas, et le signale.
- **Pièce** : plateau d'une page ; Départ et Arrivée écrits en mots, autres cases numérotées (22 pt, gras) ; plus petite dimension d'une case : 2,5 cm au moins, pour qu'un pion y tienne ; cases spéciales grisées **et** au numéro entouré (jamais la teinte seule, MP-C-05), leur effet est écrit dans la règle ; cartes-défis au format J2 (6,2 × 6,6 cm) ou J4, plutôt que du texte dans les cases.
- **Disposition** : A4 portrait, mention dans la marge du haut ; rien à découper, donc aucun repère de coupe ; cases d'accueil des cartes : carte + 0,5 cm par côté (7,2 × 7,6 cm, MP-J-10) ; dé et pions : matériel de classe. Agrandissement en A3 à l'impression (141 %) pour un groupe de quatre : inférence de conception.
- **Zone de réponse** : aucune sur le plateau.
- **Items** : 12 à 24 cartes-défis ; une seule réponse correcte par carte ; cartes numérotées, à dos neutre : à motif encadré ou blanc, avec ou sans mention au dos (nom du jeu, catégorie de la pile : « Défi », « Bonus », « Malus », « Chance »), selon la réponse de l'enseignant·e aux deux questions de MP-J-14 : jamais de réponse au verso, l'élève la verrait en tirant la carte (MP-J-14) ; solutions sur une feuille numérotée par lot (MP-J-04).
- **Hauteur** : 26,4 cm pour les quatre formes (serpent : 9 × 2,93 ; escargot : 7,6 + 0,2 + 18,6 ; chemin : 6 rangs, virages de 2,37 cm de rayon ; circuit : 8 × 3,3) ; calculé par la fonction, contrôlé sur le rendu PDF le 19.11.2026.
- **Recette** : R11 : `plateau_parcours(base, forme, titre, speciales)` écrit le plateau en PDF et en SVG à l'échelle 1 ; il s'imprime tel quel ou s'insère dans le dossier de jeu (`inserer_image`). L'ancien plateau en tableau (6 × 8 cases de 2,5 cm, R8 adaptée) est retiré.
- **Vigilance** : le hasard ne doit pas dominer : une réponse juste fait avancer ; les cases « piège » ne portent aucune information sur la notion ; quatre cases spéciales au plus par plateau (inférence de conception).
- **Interdits** : plateau présenté comme un tableau ou une grille pleine ; parcours dont le sens ne se lit pas (cases qui se suivent sans se toucher ni être reliées) ; case spéciale signalée par la seule teinte.
- **Statut** : les quatre formes ont été produites en PDF et regardées le 19.11.2026 (nombre et dimensions des cases calculés par la fonction ; polices de remplacement Liberation Sans pour l'essai) ; non imprimé, non testé en classe.

### J6 — Dé à monter (révision du 19.11.2026 : grand ou petit ; rendu contrôlé, montage non réalisé)

- **Usage** : tirage au hasard d'un élément (pronom, nombre, consigne) pour un jeu ou un entraînement.
- **Pièce** : patron de cube en croix, avec sept languettes de collage ; deux formats : **J6-a, grand dé** : faces de 6 cm, un dé par page ; **J6-b, petit dé** : faces de 4,2 cm, deux dés identiques par page. Une information par face, centrée, en gras : 48 pt sur le grand dé, 30 pt sur le petit, jamais moins de 14 pt. (Auparavant : faces de 4 cm, puis de 5,5 cm.)
- **Disposition** : grand dé : croix de 3 faces en largeur et 4 en hauteur (18 × 24,9 cm avec la languette du haut) ; petit dé : deux patrons couchés, l'un sous l'autre (17,5 × 12,6 cm chacun). Les languettes des côtés se logent dans les angles libres de la croix. Contour à découper en pointillés (MP-J-05), plis en trait fin ; patron découpé aux ciseaux, donc sans repères de coupe (exception à MP-J-12) ; mention dans la marge du haut.
- **Zone de réponse** : aucune.
- **Items** : 6 faces.
- **Hauteur** : grand dé : 24,9 cm ; petit dé : 2 × 12,6 + 0,8 = 26 cm (calculé par la fonction ; rendu PDF contrôlé le 19.11.2026).
- **Recette** : R11 : `de_a_monter(base, faces, format)` écrit le patron en PDF et en SVG à l'échelle 1 ; `format='grand'` ou `'petit'`. L'IA propose les deux formats et laisse choisir (MP-J-13) : le grand pour un dé lancé devant la classe ou pour les plus jeunes, le petit pour un dé par groupe. L'ancien tableau .docx (R8 adaptée) est retiré.
- **Vigilance** : papier épais ; montage par l'adulte ou en atelier ; vérifier que chaque face reste lisible une fois le dé monté.
- **Statut** : les deux formats ont été produits en PDF et regardés le 19.11.2026 (police Liberation Sans pour l'essai) ; non imprimé, montage réel non réalisé (V18).

### J7 — Loto (testé sur rendu)

- **Usage** : réactiver un répertoire : on entend ou on lit, on couvre (TR33, BDRP-D1).
- **Pièce** : carton de 7,5 × 5 cm, à 6 cases de 2,5 cm ; 8 cartons par planche. Cartes d'appel de 5 × 2,5 cm. Depuis le 19.11.2026 (MP-J-11, MP-J-12) : carton de 9,3 × 6,6 cm, à 6 cases de 3,1 × 3,3 cm, 2 × 4 cartons par planche ; cartes d'appel de 6,2 × 3,3 cm, 3 × 8 par planche ; repères de coupe au bord de la feuille ; dimensions calculées, non rendues.
- **Items** : 12 éléments, chacun sur 4 cartons (calculé : 8 × 6 / 12).
- **Hauteur** : 0,9 + 4 × 5 = 20,9 cm (calculé ; 20,0 cm de tracé mesurés). Depuis le 19.11.2026 : 4 × 6,6 = 26,4 cm (calculé).
- **Recette** : R14 (`planche_zones`, 3 sous-colonnes) ; R13 (`generer_loto`, `verifier_loto`) ; règle du jeu en planche A5 (R15) ; cartes d'appel en deux jeux, pour remplir la page (MP-O-14).
- **Contrôles** : V11, V12, V19 (fréquence exacte, aucun doublon, cartons tous différents).
- **Interdits** : deux cartons identiques ; élément absent des cartes d'appel ; jeu seulement oral pour une notion orthographique (X-17) ; règle rédigée au masculin seul (« le meneur ») : formulation épicène (« la personne qui lit », « on »).
- **Statut** : testé sur rendu (2.11.2026, LibreOffice, PDF regardé page par page, schéma OOXML valide) ; dimensions = inférence de conception.

### J8 — Symboles communs (testé sur rendu)

- **Usage** : discrimination rapide de mots ou d'images : deux cartes ont toujours exactement un élément commun (BDRP-D5). Le nom commercial du jeu n'est pas repris.
- **Pièce** : carte de 5 × 3,9 cm ; 4 éléments par carte ; 13 cartes pour 13 éléments (n = 3). Depuis le 19.11.2026 (MP-J-11, MP-J-12) : carte de 6,2 × 5,28 cm, 3 × 5 par planche ; repères de coupe au bord de la feuille ; dimensions calculées, non rendues.
- **Hauteur** : 0,9 + 5 × 3,9 = 20,4 cm (calculé). Depuis le 19.11.2026 : 5 × 5,28 = 26,4 cm (calculé).
- **Recette** : R14 ; R13 (`plan_projectif`, `verifier_symboles`) ; règle du jeu en planche A5 (R15).
- **Contrôles** : V19 (78 paires vérifiées par programme) ; V12.
- **Interdits** : construire les cartes à la main, sans vérification.
- **Statut** : testé sur rendu (2.11.2026, LibreOffice, PDF regardé page par page, schéma OOXML valide) ; construction n² + n + 1 vérifiée par programme ; dimensions = inférence de conception. Correction du 20.11.2026 : `plan_projectif` accepte n = 4 (21 cartes de 5 éléments, format 9S-11S), que l'ancienne formule ne construisait pas ; les trois formats (n = 2, 3 et 4) sont vérifiés par `verifier_symboles`.

### J9 — Grille « Trouve quelqu'un qui… » (testé sur rendu)

- **Usage** : prise de parole, langues, cohésion (BDRP-D6).
- **Pièce** : fiche individuelle, en-tête R7 ; grille de 4 × 4 cases de 4 × 3,4 cm.
- **Items** : 16 caractéristiques observables, chacune tenant dans sa case sans mot coupé (sinon : raccourcir l'item ; jamais couper un mot).
- **Hauteur** : en-tête + consigne + 13,6 cm (calculé).
- **Recette** : R7, R14.
- **Contrôles** : V1 à V10.
- **Interdits** : items sur la santé, la famille, la religion ou l'origine.
- **Statut** : testé sur rendu (2.11.2026, LibreOffice, PDF regardé page par page, schéma OOXML valide).

### J10 — Carte à pinces (testé sur rendu)

- **Usage** : choix autocorrigé ; l'élève pose une pince à linge sur la réponse de chaque question, puis retourne la carte (TR25, BDRP-C1).
- **Pièce** (révision du 2.11.2026, suite) : **une carte = une page** qui porte autant de questions que possible, et une pince par question. Chaque question occupe un bloc de trois lignes : la question à gauche (13,4 cm), ses trois réponses **empilées dans la colonne du bord droit** (2,2 cm × 0,85 cm par réponse), là où la pince se pose. Verso : le mot « bravo » (ou une image : étoile, coche) dans la cellule de la bonne réponse, rien dans les autres (MP-J-04).
- **Disposition** : A4 portrait, sur toute la hauteur utile de la page : 10 questions (10 × 2,55 cm) de la 5P à la 8P, 6 questions (6 × 4 cm, la phrase du bas étant plus grande) de la 1P à la 4P, 12 questions (12 × 2,1 cm) de la 9S à la 11S (révision du 19.11.2026 ; auparavant 8 questions, bas de page vide) ; marge droite du recto et marge gauche du verso réduites à 1,5 cm pour que la pince atteigne la colonne (dérogation déclarée à MP-F-03) ; blocs séparés par un trait plein épais, réponses par un trait fin ; sous la carte, la phrase « Quand mes 10 pinces sont posées, je retourne la carte : chaque pince doit être sur le mot « bravo ». » Variante A5 : 4 à 5 questions par carte, planche R15.
- **Items** : 10 questions (6 ou 12 selon la tranche d'âge) ; 3 réponses ; distracteurs fondés sur des erreurs typiques, expliqués dans la partie enseignant·e.
- **Hauteur** : mention 0,6 + 10 × 2,55 + phrase 1,2 = 27,3 cm, entre des marges haute et basse de 0,9 cm : la carte occupe toute la page (révision du 19.11.2026, rendu du modèle Word contrôlé ; auparavant 8 questions, 22,2 cm).
- **Règle pour les élèves** : en planche A5 (R15, côte à côte), six étapes numérotées (MP-J-07), exemple résolu avec une question hors carte : 1. Je prends la carte et une pince par question. 2. Je lis la question 1, je pince la réponse que je choisis, au bord de la carte. 3. Une pince par question. 4. Quand toutes mes pinces sont posées, je retourne la carte. 5. Chaque pince doit être sur « bravo » ; sinon je cherche pourquoi et je déplace la pince. 6. Je retire les pinces et je range la carte. Titre sans ligne Prénom et Date (MP-J-09).
- **Partie enseignant·e** (V21) : solution de toutes les questions ; pour chaque distracteur, l'erreur typique visée ; fabrication (recto-verso sur le bord long, impression test V13, plastification, une pince par question) ; débriefing (deux questions).
- **Recette** : `carte_a_pinces` (R14 : tableau à deux colonnes, cellule de question fusionnée sur trois lignes) ; R12 (au verso, colonne des réponses à gauche, même ordre des lignes) ; R15 (règle).
- **Contrôles** : V11 (une seule réponse juste par question ; `bravo` exactement une fois par bloc), V12, V13 (recto-verso sur impression test), V20, V21.
- **Interdits** : une question par carte (l'ancien format du 2.11.2026 : huit cartes de 8 × 5 cm, abandonné) ; forme écrite fautive en distracteur (X-13) ; marque lisible par transparence ; réponses en ligne loin du bord (la pince ne les atteint pas) ; lot livré sans règle élève ni partie enseignant·e.
- **Statut** : testé sur rendu (2.11.2026, suite ; LibreOffice, PDF regardé page par page, schéma OOXML valide) ; alignement recto-verso calculé, V13 non réalisé ; dimensions = inférence de conception. Révision du 19.11.2026 : nombre de questions porté à 6, 10 ou 12 pour remplir la page ; modèle Word rendu et mesuré ; `carte_a_pinces` non relancée avec ces nombres.

### J11 — Roue à fenêtre et rabat (testé sur rendu)

- **Usage** : contenu cyclique, correction immédiate (TR32, BDRP-C2). L'élève lit la question dans la fenêtre, répond, soulève le rabat.
- **Pièce** : deux disques de 11 cm. Dessous : six secteurs de 60°, question à 45 mm du centre, réponse à 28 mm. Dessus : fenêtre de 39 à 52 mm, rabat de 18 à 36 mm, charnière en trait fin à 18 mm ; ouverture de 54°.
- **Disposition** : les deux disques sur une page (dessin de 16 × 24 cm) ; attache parisienne au centre. **Écart déclaré** : 24 cm de haut, au-delà du budget de 22 cm, dans la hauteur utile de 24,7 cm.
- **Items** : 6 paires ; à 14 pt, la réponse tient en 23 mm (calculé).
- **Recette** : R11 (`roue_J11`), dessin vectoriel SVG et PDF à l'échelle 1 ; jamais de construction en .docx. Inséré dans un .docx, il garde 16 cm de large pour rester à l'échelle.
- **Contrôles** : V18 (chaque texte tient dans la fenêtre ou sous le rabat), montage d'essai réel avant la classe.
- **Interdits** : texte sur un trait de coupe ; réduire le disque pour ajouter des secteurs.
- **Statut** : testé sur rendu (2.11.2026, LibreOffice, PDF regardé page par page, schéma OOXML valide) ; géométrie calculée ; montage réel non réalisé. Remplace l'essai v0 PL-J11, dont les étiquettes débordaient sur la découpe.

### J12 — Lettres à fabriquer (testé sur rendu)

- **Usage** : matériel sensoriel de tracé (BDRP-C7).
- **Pièce** : plaque de 8 × 10 cm ; une lettre liée en 130 pt ; quatre plaques par page. Depuis le 19.11.2026 (MP-J-11, MP-J-12) : plaque de 9,3 × 13,2 cm, 2 × 2 par page ; repères de coupe au bord de la feuille ; dimensions calculées, non rendues.
- **Recette** : R10, R14. Les flèches de tracé sont ajoutées à la main par l'enseignant·e.
- **Conditionnement** : papier émeri, plaquette.
- **Contrôles** : V12, V15.
- **Interdits** : lettre dessinée ou générée ; flèche de tracé produite sans contrôle du geste enseigné.
- **Statut** : testé sur rendu (2.11.2026, LibreOffice, PDF regardé page par page, schéma OOXML valide) ; arbitrage du balayage : retenu comme gabarit J.

### J13 — Cartes de rôle (testé sur rendu)

- **Usage** : attribuer un rôle dans un travail de groupe (TR64, MF29, MF76) ; variante : cartes d'identité fictives pour l'interaction orale en langue (BDRP-I4).
- **Pièce** : carte de 8 × 5 cm : titre de 1,5 cm, deux phrases en 3,5 cm ; quatre rôles par groupe ; deux jeux de quatre cartes par planche (page pleine, MP-O-14). Depuis le 19.11.2026 (MP-J-11, MP-J-12) : carte de 9,3 × 6,6 cm, 2 × 4 par planche ; repères de coupe au bord de la feuille ; dimensions calculées, non rendues.
- **Recette** : R14.
- **Contrôles** : V12.
- **Interdits** : personne réelle, rôle lié au genre ou au niveau de l'élève.
- **Statut** : testé sur rendu (2.11.2026, LibreOffice, PDF regardé page par page, schéma OOXML valide).

### J14 — Cartes d'erreurs (testé sur rendu)

- **Usage** : analyser une erreur de calcul ou de raisonnement (TR29, P04).
- **Pièce** : carte de 8 × 10 cm : auteur·e fictif·ve, résolution, consigne. Verso : ce qui s'est passé, calcul juste. Depuis le 19.11.2026 (MP-J-11, MP-J-12) : carte de 9,3 × 13,2 cm, 2 × 2 par planche ; repères de coupe au bord de la feuille ; dimensions calculées, non rendues.
- **Recette** : R14, R12.
- **Contrôles** : V12, V13 ; corrigé recalculé par programme ; V21 : nombres et procédure adaptés à la progression du degré (MP-P-09) ; le verso nomme l'erreur de procédure (par exemple « a écrit 13 à côté du 3, sans faire de retenue »).
- **Interdits** : orthographe et grammaire, sauf analyse d'erreurs demandée par l'enseignant·e, dès la 5P, aux quatre conditions du § 3.7 (X-13, MP-CC-11) ; erreur attribuée à un·e élève identifiable.
- **Statut** : testé sur rendu (2.11.2026, LibreOffice, PDF regardé page par page, schéma OOXML valide).

### J15 — Cartes d'aide graduée (testé sur rendu)

- **Usage** : coup de pouce à prendre soi-même, du plus ouvert au plus guidé (TR30, MP-D).
- **Pièce** : carte de 8 × 5 cm ; titre « Aide 1 » à « Aide 4 » ; une aide par carte. Depuis le 19.11.2026 (MP-J-11, MP-J-12) : carte de 9,3 × 6,6 cm, 2 × 4 par planche ; repères de coupe au bord de la feuille ; dimensions calculées, non rendues.
- **Recette** : R14.
- **Contrôles** : V12 ; gradation portée par le numéro, jamais par la seule couleur (X-08).
- **Interdits** : donner la réponse dans la dernière aide ; repère évaluatif.
- **Statut** : testé sur rendu (2.11.2026, LibreOffice, PDF regardé page par page, schéma OOXML valide).

### J16 — Cartons-réponses (testé sur rendu)

- **Usage** : vote à main levée sans écran (TR69, version papier).
- **Pièce** : carton de 8 × 10,5 cm : lettre de 110 pt, puis une ligne « je choisis A ». Quatre cartons par planche. Depuis le 19.11.2026 (MP-J-11, MP-J-12) : carton de 9,3 × 13,2 cm, 2 × 2 par planche ; repères de coupe au bord de la feuille ; dimensions calculées, non rendues.
- **Recette** : R14, style de cellule dédié.
- **Contrôles** : V12 ; lisible à distance (V17, capitale de 28 mm, seuil calculé de 19 m).
- **Interdits** : distinguer les réponses par la seule couleur.
- **Statut** : testé sur rendu (2.11.2026, LibreOffice, PDF regardé page par page, schéma OOXML valide).

### J17 — Grille d'alignement (19.11.2026 ; rendu contrôlé, non testé en classe)

- **Usage** : entraînement à deux, ou à deux équipes, sur des réponses courtes (résultats de calculs, formes conjuguées, mots) ; principe du « quatre à la suite ».
- **Principe** : chaque rond de la grille porte une réponse. À son tour, l'élève tire une question (carte-défi à dos neutre, MP-J-14, ou dé), trouve la réponse sur la grille et la couvre d'un jeton de sa couleur. Le premier qui aligne trois ou quatre jetons — en ligne, en colonne ou en diagonale — gagne.
- **Pièce** : plateau d'une page, dessiné (R11, fonction `grille_alignement`) : bandeau de titre et de consigne, puis cadre arrondi à double filet ; ronds à double cercle, réponse centrée en gras. 5P-8P : 5 × 7 = 35 ronds de 2,9 cm, corps de 20 pt, aligner 4.
- **Disposition** : A4 portrait, toute la surface utile (18,6 × 26,4 cm, MP-J-11) ; rien à découper, donc aucun repère de coupe ; jetons de deux couleurs ou de deux formes : matériel de classe (rond de 2,2 cm au moins, MP-J-10).
- **Items** : autant de réponses que de ronds ; une réponse peut figurer deux fois sur la grille (l'élève choisit alors où poser son jeton), jamais deux réponses différentes pour une même question (MP-J-01) ; les cartes couvrent toutes les réponses de la grille.
- **Hauteur** : 26,4 cm (bandeau de 1,6 cm, grille de 24,4 cm) ; calculé par la fonction, contrôlé sur le rendu PDF le 19.11.2026.
- **Recette** : R11 : `grille_alignement(base, valeurs, colonnes, rangees, aligner, titre)` écrit le plateau en PDF et en SVG ; sans `valeurs`, les ronds portent les nombres de 1 à n. Un texte trop long pour un rond est refusé.
- **Vigilance** : la stratégie (bloquer l'adversaire) ne doit pas prendre le pas sur la notion : une réponse fausse fait passer le tour ; vérification par la feuille de solutions.
- **Interdits** : grille sans réponses (simple jeu d'alignement, sans apprentissage) ; distinction des joueurs par la seule couleur si les jetons sont imprimés (MP-C-05).
- **Statut** : trois formats produits en PDF et regardés le 19.11.2026 (police Liberation Sans pour l'essai) ; non imprimé, non testé en classe.

### J18 — Serpents et échelles (19.11.2026 ; rendu contrôlé, non testé en classe)

- **Usage** : entraînement varié sur un parcours, quand on veut des retournements de situation ; les défis sont tirés sur des cartes, comme pour J5.
- **Principe** : cases numérotées en lacets, du Départ (en bas à gauche) à l'Arrivée (en haut). Au pied d'une échelle, l'élève tire une carte : s'il répond juste, il monte. Sur la tête d'un serpent, il tire une carte : s'il se trompe, il redescend jusqu'à la queue. **La réponse décide, pas le dé seul.**
- **Pièce** : plateau d'une page, dessiné (R11, fonction `serpents_echelles`) : cases en damier gris clair et blanc, numéro en gras dans le coin de la case ; échelles à deux montants et barreaux ; serpents au corps gris ondulant, tête ronde. 5P-8P : 6 × 8 = 48 cases de 3,0 cm au moins, 3 échelles et 3 serpents.
- **Disposition** : A4 portrait, toute la surface utile (MP-J-11) ; rien à découper ; échelles et serpents tirés au sort par la fonction (paramètre `graine`), sans croisement ni extrémité commune, ou imposés (paramètre `liens`) ; dé, roue J20 et pions : matériel de classe.
- **Exception à la règle des plateaux** : la grille est ici le principe du jeu ; le sens du parcours se lit par les numéros, par les mots Départ et Arrivée et par le damier. Pour un simple parcours, préférer J5.
- **Items** : 12 à 24 cartes-défis numérotées, à dos neutre (MP-J-14) ; feuille de solutions.
- **Hauteur** : 26,4 cm (bandeau de 1,6 cm et 8 rangées de 3,05 cm) ; calculé par la fonction, contrôlé sur le rendu PDF le 19.11.2026.
- **Recette** : R11 : `serpents_echelles(base, colonnes, rangees, liens, graine, titre)` écrit le plateau en PDF et en SVG.
- **Vigilance** : un serpent long en fin de parcours décourage : deux rangées de descente au plus près de l'Arrivée (inférence de conception) ; au cycle 1, expliquer le sens des lacets sur le plateau avant de jouer.
- **Interdits** : serpent ou échelle dont l'effet ne dépend pas d'une réponse ; plus d'un lien par case.
- **Statut** : trois formats produits en PDF et regardés le 19.11.2026 (police Liberation Sans pour l'essai) ; non imprimé, non testé en classe.

### J19 — Bataille navale (19.11.2026 ; rendu contrôlé, non testé en classe)

- **Usage** : entraînement à deux sur une notion qui croise deux entrées : sujet × verbe (la forme conjuguée), nombre × nombre (le produit, la somme), lettre × chiffre (le repérage dans un quadrillage).
- **Principe** : chaque élève reçoit une fiche et la cache derrière un classeur. Il dessine ses bateaux dans la grille « Ma flotte ». Pour tirer, il **dit ou écrit la réponse** de la case visée (« nous finissons ») ; l'adversaire annonce « touché » ou « dans l'eau » ; le tireur note son essai dans la grille « Mes tirs ».
- **Pièce** : fiche d'une page par élève, dessinée (R11, fonction `bataille_navale`) : deux grilles identiques l'une sous l'autre, intitulés des colonnes et des lignes en gras, filet ondulé (l'eau) après chaque titre, trois bateaux modèles à côté de « Ma flotte ». 5P-8P : 6 × 6 = 36 cases par grille.
- **Disposition** : A4 portrait, toute la surface utile (MP-J-11) ; rien à découper ; les cases restent vides : l'élève y dessine et y écrit.
- **Items** : 5, 6 ou 8 intitulés par entrée ; chaque case a une seule réponse (MP-J-01) ; chaque croisement existe (pas de verbe sans la personne visée).
- **Hauteur** : 26,4 cm (bandeau de 1,6 cm, deux blocs de 12,2 cm) ; calculé par la fonction, contrôlé sur le rendu PDF le 19.11.2026.
- **Recette** : R11 : `bataille_navale(base, en_colonnes, en_lignes, taille, titre)` écrit la fiche en PDF et en SVG ; sans intitulés, les colonnes portent des lettres et les lignes des nombres.
- **Vigilance** : la réponse est dite avant le tir, vérifiée avec la carte-mémoire de la notion (MP-J-08) ; la flotte (un bateau de trois cases, un de deux, un d'une case) s'écrit dans la règle.
- **Interdits** : croisement qui produirait une forme inexistante ; tir annoncé par les seules coordonnées quand la notion visée est la réponse de la case.
- **Statut** : trois formats produits en PDF et regardés le 19.11.2026 (police Liberation Sans pour l'essai) ; non imprimé, non testé en classe.

### J20 — Roue de tirage (19.11.2026 ; rendu contrôlé, non testé en classe)

- **Usage** : tirage au sort sans dé ni montage : un pronom, un nombre, une consigne, une catégorie de cartes ; remplace le dé J6 quand il faut plus de six issues ou une préparation immédiate.
- **Principe** : l'élève pose un trombone au centre de la roue, le tient avec la pointe d'un crayon et le fait tourner d'une pichenette ; le secteur où il s'arrête donne le tirage.
- **Pièce** : roue d'une page, dessinée (R11, fonction `roue_tirage`) : disque de 18,2 cm à double filet, 3 à 12 secteurs égaux, alternés blanc et gris clair quand leur nombre est pair, texte en gras (24 pt, réduit si besoin, jamais moins de 10 pt) ; sous la roue, vingt cases « Mes tirages » pour noter.
- **Disposition** : A4 portrait, toute la surface utile (MP-J-11) ; rien à découper ; trombone et crayon : matériel de classe.
- **Items** : 4 secteurs de la 1P à la 4P, 6 de la 5P à la 8P, 8 dès la 9S (inférence de conception) ; un texte court par secteur, sur une ou deux lignes.
- **Hauteur** : 26,4 cm (bandeau de 1,6 cm, roue de 18,2 cm, cases de tirage) ; calculé par la fonction, contrôlé sur le rendu PDF le 19.11.2026.
- **Recette** : R11 : `roue_tirage(base, secteurs, titre)` écrit la roue en PDF et en SVG. Un texte trop long pour un secteur est refusé.
- **Vigilance** : secteurs égaux, pour que le tirage reste équitable ; le texte n'est pas tourné : il se lit sans pencher la tête.
- **Interdits** : secteurs distingués par la seule teinte (le texte porte l'information, MP-C-05) ; plus de 12 secteurs.
- **Statut** : roues de 4, 6 et 8 secteurs produites en PDF et regardées le 19.11.2026 (police Liberation Sans pour l'essai) ; non imprimé, rotation du trombone non essayée.

### J21 — Puzzles à deux pièces (20.11.2026 ; rendu contrôlé, non testé en classe)

- **Usage** : associer deux éléments (calcul et résultat, mot et définition, mot et image, fraction et nombre décimal) en atelier autonome ; l'élève se corrige seul.
- **Principe** : chaque puzzle est un rectangle coupé en deux par une ligne d'une forme propre (pointe, créneau ou demi-rond, à trois hauteurs, vers la gauche ou vers la droite : 18 formes). Seules les deux bonnes pièces s'emboîtent : **la découpe corrige** (MP-J-04).
- **Pièce** : puzzle de 9,3 × 4,4 cm en 5P-8P (deux pièces de 4,65 cm) ; élément de gauche en gras ; contour en pointillés, ligne d'emboîtement en trait plein, à découper aux ciseaux.
- **Disposition** : planche de 2 × 6 puzzles sur toute la surface utile (MP-J-11) ; repères de coupe (MP-J-12) ; mention dans la marge du haut.
- **Items** : 8, 12 ou 18 paires par planche ; chaque élément de gauche a une seule réponse dans le lot, et aucune réponse ne figure deux fois (MP-J-01).
- **Recette** : R11 : `puzzle_association(base, paires, colonnes, rangees, taille_pt, mention)` ; un texte trop long est refusé.
- **Vigilance** : mélanger les paires avant l'appel, pour que deux puzzles voisins n'aient pas des formes proches ; plastifier avant de découper.
- **Interdits** : plus de 18 puzzles dans un même lot (deux formes seraient identiques) ; indice de couleur sur les pièces.
- **Statut** : un format par tranche d'âge produit en PDF et regardé le 20.11.2026 (police Liberation Sans pour l'essai) ; non imprimé, non testé en classe ; emboîtement réel non essayé.

### J22 — Puzzle à bandes (20.11.2026 ; rendu contrôlé, non testé en classe)

- **Usage** : ranger une suite (nombres, lettres, multiples, nombres décimaux, mots dans l'ordre alphabétique, étapes d'un récit).
- **Principe** : une image est coupée en bandes verticales ; chaque bande porte une étiquette en bas. Remises dans l'ordre des étiquettes, les bandes reforment l'image : **l'image corrige**.
- **Pièce** : bande de 26,4 cm de haut ; 5 bandes de 3,7 cm, 10 bandes de 1,9 cm ou 12 bandes de 1,6 cm ; étiquette en gras dans les 2,6 cm du bas.
- **Disposition** : toute la surface utile (MP-J-11) ; repères de coupe (MP-J-12).
- **Image** : celle de l'enseignant·e (paramètre `image` : photo ou dessin libre de droits ; l'image est étirée à la zone de 18,6 × 23,8 cm) ; sans image, la fonction dessine un paysage au trait.
- **Recette** : R11 : `puzzle_bandes(base, etiquettes, image, mention, taille_pt)` ; les étiquettes sont données dans l'ordre correct.
- **Vigilance** : une image aux formes continues d'une bande à l'autre, sans grand aplat uniforme ; les bandes se rangent sur une feuille-support ou dans une réglette.
- **Interdits** : étiquettes en double ; image qui contient déjà l'ordre (numéros visibles).
- **Statut** : un format par tranche d'âge produit en PDF et regardé le 20.11.2026 (police Liberation Sans pour l'essai) ; non imprimé, non testé en classe.

### J23 — Mot mystère (20.11.2026 ; rendu contrôlé, non testé en classe)

- **Usage** : réactiver le vocabulaire d'une leçon ; fiche individuelle ou à deux.
- **Principe** : chaque définition donne un mot, écrit dans sa ligne de cases ; les lignes sont décalées pour que les cases grises, lues de haut en bas, forment le mot mystère.
- **Pièce** : fiche d'une page (R11, fonction `mot_mystere`) : bandeau de titre et de consigne, grille de cases de 2 cm au plus, définitions numérotées, cases du mot mystère en bas de page.
- **Items** : autant de mots que de lettres dans le mot mystère (4, 6 ou 8) ; chaque définition n'admet qu'un mot (MP-J-01) ; majuscules sans accent.
- **Recette** : `mot_mystere(base, mystere, mots, titre, taille_pt)` ; la fonction vérifie que le mot numéro i contient la lettre numéro i du mot mystère et place chaque mot.
- **Vigilance** : le mot mystère appartient à la leçon ; les définitions sont à la portée des élèves sans aide.
- **Interdits** : mot à accent indispensable au sens ; définition qui contient le mot ou un mot de la même famille.
- **Statut** : un format par tranche d'âge produit en PDF et regardé le 20.11.2026 (police Liberation Sans pour l'essai) ; non imprimé, non testé en classe.

### J24 — Cocotte en papier (20.11.2026 ; rendu contrôlé, non testé en classe)

- **Usage** : se poser des défis à deux (calcul mental, conjugaison, vocabulaire) ; l'élève qui tient la cocotte lit la question et vérifie la réponse.
- **Principe** : un carré à plier. Quatre mots à l'extérieur, huit nombres sur les volets, huit défis sous les volets : la question sur le volet, la réponse en gras dessous.
- **Pièce** : carré de 18,6 cm (R11, fonction `cocotte`) ; traits de pliage fins ; sous le carré, la règle du pliage en quatre étapes et la règle du jeu.
- **Items** : 4 mots courts, 8 nombres ou textes courts, 8 couples question-réponse ; une seule réponse par question (MP-J-01).
- **Recette** : `cocotte(base, coins, nombres, defis, titre, taille_pt)` ; un texte trop long pour sa zone est refusé.
- **Vigilance** : le pliage se montre une fois devant la classe ; papier de 80 g, non plastifié.
- **Interdits** : gage ou prédiction sur une personne ; texte sur un trait de pliage.
- **Statut** : un format par tranche d'âge produit en PDF et regardé le 20.11.2026 (police Liberation Sans pour l'essai) ; non imprimé, non testé en classe ; emplacement des textes déduit du pliage par le calcul, **pliage réel non essayé** : plier un exemplaire avant de distribuer.

### J25 — Horloge à aiguilles (20.11.2026 ; rendu contrôlé, non testé en classe)

- **Usage** : lire et régler l'heure ; matériel individuel de manipulation.
- **Pièce** : cadran de 17 cm (R11, fonction `horloge`) et deux aiguilles à découper : la petite, grise, pour les heures ; la grande, blanche, pour les minutes ; attache parisienne au centre.
- **Variantes** : chiffres de 1 à 12 seuls (1P-4P) ; graduations des minutes et nombres de 5 à 60 (5P-8P) ; heures de 13 à 24 en plus (9S-11S).
- **Disposition** : cadran en haut de la page, aiguilles et consigne dessous ; contours de découpe en pointillés.
- **Recette** : `horloge(base, minutes, heures_24, titre)`.
- **Vigilance** : imprimer sur papier épais ou plastifier ; les deux aiguilles se distinguent par la longueur et par la teinte, et leur nom est écrit dessus (MP-C-05).
- **Interdits** : chiffres romains ou cadran sans chiffres pour un premier apprentissage.
- **Statut** : un format par tranche d'âge produit en PDF et regardé le 20.11.2026 (police Liberation Sans pour l'essai) ; non imprimé, non testé en classe ; montage réel non essayé.

### J26 — Mémo-fiches en éventail (20.11.2026 ; rendu contrôlé, non testé en classe)

- **Usage** : réviser une série (tables, conjugaisons, mots-outils, formules) ; les fiches se consultent une à une, réunies par une attache.
- **Pièce** : fiche haute de 13,2 cm, large de 6,2 cm, 4,65 cm ou 3,7 cm selon la tranche d'âge ; titre sur bandeau gris, lignes centrées, rond marquant le trou de l'attache en bas.
- **Disposition** : deux rangées de 3, 4 ou 5 fiches sur toute la surface utile (MP-J-11) ; repères de coupe (MP-J-12).
- **Items** : 6, 8 ou 10 fiches par planche ; 5 à 12 lignes par fiche ; un titre par fiche.
- **Recette** : R11 : `eventail(base, fiches, colonnes, taille_pt, mention)` ; le corps diminue si une ligne est trop longue, puis la planche est refusée.
- **Vigilance** : plastifier, percer à la perforatrice sur le rond, réunir par une attache parisienne ou un anneau.
- **Interdits** : fiche d'entraînement présentée comme évaluation ; repère de niveau sur la fiche, sauf étoiles de difficulté demandées (MP-J-06).
- **Statut** : un format par tranche d'âge produit en PDF et regardé le 20.11.2026 (police Liberation Sans pour l'essai) ; non imprimé, non testé en classe.

### J27 — Bandes graphiques (20.11.2026 ; rendu contrôlé, non testé en classe)

- **Usage** : entraîner le geste graphique avant et pendant l'apprentissage de l'écriture ; bandes plastifiées, feutre effaçable.
- **Pièce** : bande de 18,6 cm de long, haute de 6,6 cm, 4,4 cm ou 3,3 cm ; un point de départ, un modèle en trait plein sur le premier tiers, puis le même tracé en pointillés à repasser.
- **Motifs** : traits, zigzag, vagues, ponts, coupes, créneaux, boucles, spirales (liste `MOTIFS`).
- **Disposition** : 4, 6 ou 8 bandes sur toute la surface utile (MP-J-11) ; repères de coupe (MP-J-12).
- **Recette** : R11 : `bandes_graphiques(base, motifs, mention)`.
- **Vigilance** : le sens du tracé (de gauche à droite, depuis le point) se montre avant l'atelier ; ces bandes ne remplacent pas le modèle d'écriture liée de l'établissement.
- **Interdits** : lettres ou chiffres dessinés par la fonction (le tracé des lettres suit le modèle enseigné, R10).
- **Statut** : un format par tranche d'âge produit en PDF et regardé le 20.11.2026 (police Liberation Sans pour l'essai) ; non imprimé, non testé en classe.

### J28 — Plateau à camemberts (20.11.2026 ; rendu contrôlé, non testé en classe)

- **Usage** : réviser plusieurs domaines ou plusieurs chapitres dans une même partie ; quiz à six catégories, sur le principe d'un jeu de questions connu, dont le nom commercial n'est pas repris.
- **Principe** : une roue à six rayons. Chaque case porte le symbole d'une catégorie : l'élève y répond à une question de cette catégorie. Au bout de chaque rayon, une grande case (grise, ou teintée en couleur) : une réponse juste y fait gagner la part de la catégorie, que l'élève colorie dans son camembert. Six parts : retour au centre et dernière question.
- **Pièce** : plateau d'une page (R11, fonction `plateau_camemberts`) : roue de 18 cm, couronne et rayons de cases, centre « Départ, Arrivée » ; sous la roue, la légende (symbole et nom de chaque catégorie) et quatre camemberts de score.
- **Catégories** : six, distinguées par un **symbole** (disque, triangle, carré, losange, étoile, croix), jamais par la seule couleur (MP-C-05) ; noms courts, au choix de l'enseignant·e.
- **Cartes** : cartes-questions à dos neutre (MP-J-14), une question par catégorie sur chaque carte, lues par un·e camarade ; la réponse est sur la carte, en gras, sous la question : `cartes_categories(base, cartes, colonnes, rangees, taille_pt, mention)` ; modèle Word à remplir dans la boîte à outils.
- **Recette** : `plateau_camemberts(base, categories, entre, rayon, titre)` ; `entre` : cases entre deux rayons ; `rayon` : cases par rayon.
- **Vigilance** : une partie complète est longue : fixer une durée, ou trois parts à gagner au lieu de six.
- **Interdits** : catégorie distinguée par la seule couleur ; question à plusieurs réponses possibles.
- **Statut** : un format par tranche d'âge produit en PDF et regardé le 20.11.2026 (police Liberation Sans pour l'essai) ; non imprimé, non testé en classe.

### J29 — Cherche et trouve de mots (20.11.2026 ; rendu contrôlé, non testé en classe)

- **Usage** : reconnaître vite une classe grammaticale, un son, une famille de mots, une propriété d'un nombre ; jeu de rapidité à deux, trois ou quatre.
- **Principe** : des mots sont dispersés sur la planche, penchés, sans se toucher. Une carte consigne est tirée (« Trouve un adjectif », « Trouve un mot qui contient le son [o] ») ; le premier qui pose le doigt sur un mot qui convient gagne la carte.
- **Pièce** : planche d'une page (R11, fonction `planche_lynx`) : bandeau de titre et de consigne, cadre arrondi, mots en gras ; cartes consignes à dos neutre (MP-J-14), produites avec `planche_pdf` (exemple de douze consignes à la page 4 de la planche prête à imprimer).
- **Items** : 20, 40 ou 65 mots environ ; plusieurs mots conviennent à chaque consigne, et la vérification se fait avec la carte-mémoire de la notion (MP-J-08).
- **Recette** : `planche_lynx(base, mots, graine, taille_pt, titre)` ; les mots sont placés au hasard (paramètre `graine`) ; la fonction refuse la planche s'il n'y a plus de place.
- **Vigilance** : les mots ne portent aucun indice de couleur ou de style ; un mot qui appartient à deux classes (« ferme », « sourire ») s'évite ou se discute.
- **Interdits** : forme fautive sur la planche ; couleur par classe grammaticale.
- **Statut** : un format par tranche d'âge produit en PDF et regardé le 20.11.2026 (police Liberation Sans pour l'essai) ; non imprimé, non testé en classe.

### J30 — Mots interdits (20.11.2026 ; rendu contrôlé, non testé en classe)

- **Usage** : définir, reformuler, mobiliser le vocabulaire d'une leçon à l'oral ; en équipes, dès la 5P.
- **Principe** : l'élève fait deviner à son équipe le mot du bandeau, sans prononcer les mots interdits écrits dessous ; un·e adversaire contrôle. Le nom commercial du jeu n'est pas repris.
- **Pièce** : carte de 6,2 × 8,8 cm (9 par planche) ou de 6,2 × 6,6 cm (12 par planche) : mot à faire deviner en gras sur bandeau gris, mention « sans dire », puis 3 ou 5 mots interdits.
- **Disposition** : toute la surface utile (MP-J-11) ; repères de coupe (MP-J-12) ; cartes tirées d'une pioche : dos neutre (MP-J-14).
- **Recette** : R11 : `cartes_mots_interdits(base, cartes, colonnes, rangees, taille_pt, mention)`.
- **Vigilance** : les mots interdits sont ceux que l'élève dirait en premier ; le mot à deviner appartient à la leçon.
- **Interdits** : nom d'une personne de la classe ; mot dont la définition exige un mot interdit.
- **Statut** : deux formats (5P-8P, 9S-11S) produits en PDF et regardés le 20.11.2026 ; non imprimé, non testé en classe.

### J31 — Petit bac (20.11.2026 ; rendu contrôlé, non testé en classe)

- **Usage** : mobiliser le vocabulaire par catégories, l'orthographe du début des mots, les classes grammaticales ; individuel ou par deux.
- **Principe** : une lettre est tirée par manche (roue J20 ou dé J6) ; chaque élève écrit, par colonne, un mot qui commence par cette lettre. Un mot juste : 1 point ; un mot que personne d'autre n'a : 2 points.
- **Pièce** : fiche d'une page (R11, fonction `petit_bac`) : bandeau de titre et de règle, ligne du prénom, grille (colonne « Lettre », 3 à 6 catégories, colonne « Points »), case du total.
- **Items** : 3 catégories et 4 manches (1P-4P), 5 et 6 (5P-8P), 6 et 8 (9S-11S) ; lignes de 5,2 cm, 3,5 cm ou 2,6 cm de haut.
- **Recette** : `petit_bac(base, categories, manches, titre, taille_pt)`.
- **Vigilance** : écarter les lettres rares (K, W, X, Y, Z) ; le temps d'une manche se fixe à l'avance.
- **Interdits** : catégorie sur la vie privée des élèves ; points retirés pour l'orthographe quand elle n'est pas l'objectif.
- **Statut** : un format par tranche d'âge produit en PDF et regardé le 20.11.2026 (police Liberation Sans pour l'essai) ; non imprimé, non testé en classe.

### J32 — Cartes à terminaisons (20.11.2026 ; rendu contrôlé, non testé en classe)

- **Usage** : automatiser un choix parmi peu de réponses : terminaisons d'un temps, accords, homophones, déterminants ; jeu de cartes à trois ou quatre, dès la 5P.
- **Principe** : chaque joueur reçoit six cartes-réponses (les terminaisons). Une carte-phrase à trou est retournée ; le premier qui pose la bonne terminaison s'en défausse ; une erreur fait piocher deux cartes. Le premier qui n'a plus de cartes gagne.
- **Pièces** : 12 cartes-phrases numérotées de 9,3 × 4,4 cm, le trou marqué par des points de suspension ; 24 cartes-terminaisons de 4,65 × 4,4 cm ; une feuille de solutions numérotée.
- **Vérification** : par la feuille de solutions, tenue par un·e camarade (MP-J-04) ; jamais de réponse au dos d'une carte tirée (MP-J-14).
- **Items** : chaque phrase n'admet qu'une terminaison du jeu (MP-J-01) ; chaque terminaison figure deux fois ; aucune forme fautive n'est imprimée : la phrase à trou reste incomplète.
- **Recette** : `planche_pdf(..., lisere=True)` pour les deux planches (liseré et repères de coupe compris) ; feuille de solutions en R11.
- **Interdits** : phrase qui accepte deux terminaisons ; terminaison absente du jeu.
- **Statut** : exemple 5P-8P (présent, verbes en -er et en -ir du type finir) produit en PDF et regardé le 20.11.2026 (police Liberation Sans pour l'essai) ; non imprimé, non testé en classe.

### J33 — Petits chevaux (20.11.2026 ; rendu contrôlé, non testé en classe)

- **Usage** : entraînement sur cartes-défis dans un jeu de parcours connu des élèves ; deux à quatre joueurs.
- **Principe** : piste de 52 cases en croix, quatre écuries, quatre échelles de cinq marches vers le centre. Un 6 **et** une réponse juste font sortir un pion ; sur l'échelle, une réponse juste par marche. Un pion rejoint par un adversaire retourne à l'écurie.
- **Pièce** : plateau d'une page (R11, fonction `petits_chevaux`) : cases de 1,24 cm ; joueurs distingués par un **symbole** (disque, triangle, carré, étoile), jamais par la couleur seule (MP-C-05) ; règle en trois phrases sous le plateau.
- **Matériel** : seize pions de 1 cm au plus (MP-J-10 : jetons de classe ou pions découpés), un dé, des cartes-défis à dos neutre (modèle J5).
- **Recette** : `petits_chevaux(base, titre)`.
- **Vigilance** : partie longue : limiter à deux pions par joueur ou à une durée ; la capture peut décourager les plus jeunes : variante sans retour à l'écurie.
- **Interdits** : question dont l'enjeu est seulement de rejouer, sans lien avec l'objectif.
- **Statut** : un format produit en PDF et regardé le 20.11.2026 (police Liberation Sans pour l'essai) ; non imprimé, non testé en classe ; taille des cases (1,24 cm) à éprouver avec les pions de la classe.

### J34 — Qui est-ce ? (20.11.2026 ; rendu contrôlé, non testé en classe)

- **Usage** : formuler des questions fermées avec le vocabulaire de la notion (pair, multiple de, supérieur à, décimal, négatif ; nature d'un mot ; propriétés d'une figure) ; à deux.
- **Principe** : chaque élève a la même grille. L'un choisit un élément en secret et l'écrit ; l'autre pose des questions auxquelles on répond par oui ou par non, et barre ce qui ne convient pas, jusqu'à trouver l'élément.
- **Pièce** : fiche d'une page (R11, fonction `grille_qui_est_ce`) : bandeau, 12, 24 ou 30 cases à coins arrondis, élément en gras ; ligne de l'élément secret en bas.
- **Items** : des nombres, des mots ou des figures nommées, **sans portrait** ; chaque élément se distingue des autres par au moins une propriété travaillée.
- **Recette** : `grille_qui_est_ce(base, elements, colonnes, titre, taille_pt)`.
- **Vigilance** : afficher les questions modèles (« Est-ce un multiple de 3 ? ») ; la fiche est à usage unique, ou glissée sous une pochette effaçable.
- **Interdits** : portraits ou caractéristiques physiques de personnes ; question sur un élève de la classe.
- **Statut** : trois formats produit en PDF et regardé le 20.11.2026 (police Liberation Sans pour l'essai) ; non imprimé, non testé en classe.

### J35 — Bataille (20.11.2026 ; rendu contrôlé, non testé en classe)

- **Usage** : comparer deux valeurs : nombres et calculs, fractions, nombres décimaux et pourcentages, longueurs ; à deux.
- **Principe** : chaque joueur retourne une carte ; la plus grande valeur gagne les deux cartes ; deux valeurs égales : « bataille », chacun retourne une nouvelle carte.
- **Pièce** : carte de 6,2 × 6,6 cm (12 par planche), de 4,65 × 6,6 cm (16) ou de 4,65 × 5,28 cm (20) ; une valeur par carte, écrite sous des formes différentes d'une carte à l'autre.
- **Disposition** : `planche_pdf(..., lisere=True)`, toute la surface utile (MP-J-11), liseré et repères de coupe (MP-J-12) ; cartes tirées : dos neutre (MP-J-14) ; valeur écrite en grand (36 à 40 pt), réduite seulement si elle ne tient pas dans le cadre.
- **Items** : quelques valeurs égales sous deux écritures (3/5 et 60 %) pour provoquer des batailles ; vérification avec la carte-mémoire de la notion (MP-J-08).
- **Interdits** : valeurs toutes écrites sous la même forme (le jeu ne ferait plus comparer) ; unités mêlées sans que ce soit l'objectif.
- **Statut** : trois exemples produit en PDF et regardé le 20.11.2026 (police Liberation Sans pour l'essai) ; non imprimé, non testé en classe.

### J36 — Tuiles-lettres (20.11.2026 ; rendu contrôlé, non testé en classe)

- **Usage** : lettres mobiles pour composer des mots, des anagrammes, des mots croisés sur table.
- **Pièce** : tuile de 3,1 × 3,3 cm (48 par planche), de 2,07 × 2,03 cm (117) ou de 1,55 cm de côté (204) ; lettre minuscule en gras ; un trait sous la lettre donne le bas de la tuile (b, d, p, q, n, u).
- **Répartition** : l'alphabet complet, puis les lettres selon leur fréquence en français (liste `FREQUENCES`, voyelles nombreuses) ; majuscules en option.
- **Recette** : R11 : `tuiles_lettres(base, colonnes, rangees, majuscules, mention)` ; repères de coupe (MP-J-12).
- **Vigilance** : plastifier avant de découper ; ranger par lettre dans une boîte à compartiments.
- **Interdits** : valeur en points sur les tuiles quand le calcul du score n'est pas l'objectif.
- **Statut** : trois formats produit en PDF et regardé le 20.11.2026 (police Liberation Sans pour l'essai) ; non imprimé, non testé en classe.

### J37 — Sudoku (20.11.2026 ; rendu contrôlé, non testé en classe)

- **Usage** : raisonner par élimination ; activité d'autonomie, sans lien direct avec une notion.
- **Pièce** : fiche d'une page (R11, fonction `sudoku`) : quatre grilles de 4 × 4 cases (1P-4P), deux de 6 × 6 (5P-8P), deux de 9 × 9 (9S-11S) ; blocs en trait épais.
- **Contrôle** : chaque grille a **une seule solution**, vérifiée par programme (`_sudoku`) ; la page des solutions s'imprime à part (`solutions=True`).
- **Recette** : `sudoku(base, taille, grilles, trous, graine, solutions, titre)` ; `graine` change les grilles, `trous` la difficulté.
- **Vigilance** : montrer la règle sur une grille de 4 × 4 avant de laisser chercher.
- **Interdits** : grille recopiée d'une publication ; grille à plusieurs solutions.
- **Statut** : trois formats et leurs solutions produit en PDF et regardé le 20.11.2026 (police Liberation Sans pour l'essai) ; non imprimé, non testé en classe.

### J38 — Mot caché : la fleur (20.11.2026 ; rendu contrôlé, non testé en classe)

- **Usage** : orthographe lexicale, lettres probables d'un mot ; à deux. Remplace le jeu du pendu : **aucune image de pendu** dans les ressources.
- **Principe** : un élève choisit un mot et trace un tiret par lettre ; l'autre propose des lettres. Lettre du mot : elle s'écrit sur son tiret. Lettre absente : elle est barrée dans l'alphabet, et celui qui a choisi le mot dessine une partie de la fleur : tige, feuille, feuille, cœur, quatre pétales. La fleur terminée en huit erreurs : le mot n'a pas été trouvé.
- **Pièce** : fiche d'une page (R11, fonction `mot_cache_fleur`) : le modèle de la fleur en huit étapes numérotées, puis trois zones de partie (tirets, alphabet à barrer, cadre « ma fleur »).
- **Recette** : `mot_cache_fleur(base, parties, titre)`.
- **Vigilance** : le mot vient de la liste de la semaine ; il est écrit en secret et montré à la fin.
- **Interdits** : potence, pendu ou toute image de violence ; mot inconnu des élèves.
- **Statut** : un format produit en PDF et regardé le 20.11.2026 (police Liberation Sans pour l'essai) ; non imprimé, non testé en classe.

### Variantes par tranche d'âge (19.11.2026 ; formats calculés et rendus en miniature, non testés en classe)

- **Principe** : chaque gabarit de jeu existe en trois formats : moins de pièces ou de cases et une écriture plus grande pour les plus jeunes, davantage de pièces et une écriture plus petite ensuite. L'IA lit la tranche du degré demandé et applique les nombres ci-dessous ; les valeurs sont celles du dictionnaire `VARIANTES` (Annexe I-C), par planche A4.
- **Corps minimal du texte des pièces** : 24 pt de la 1P à la 4P (18 pt admis en 3P-4P, § 2.1), 14 pt de la 5P à la 8P (12 pt admis en 7P-8P), 12 pt de la 9S à la 11S (valeurs retenues le 21.11.2026, non testées en classe).
- **Affichage** (MP-J-13) : quand le degré est connu, l'IA montre la page de miniatures de la tranche (`miniatures_tranche`, ou les fichiers « Jeux par tranche d'âge » de la boîte à outils) à la place du panorama général.
- **Plateaux J5** : au cycle 3, les cases descendent à 2,1 cm au moins : prévoir des jetons plutôt que des pions (`case_min_mm=20`).
- **Gabarits absents d'une tranche** : J12 (lettres à fabriquer) seulement de la 1P à la 4P ; J14 (cartes d'erreurs) dès la 5P ; J9 demande de lire et d'écrire un prénom : dès la 3P (inférences de conception).
- **J1 — Domino-boucle** : 1P-4P : 10 dominos (9,3 × 5,3 cm · 26 pt) ; 5P-8P : 16 dominos (9,3 × 3,3 cm · 18 pt) ; 9S-11S : 20 dominos (9,3 × 2,6 cm · 14 pt).
- **J2 — Memory, appariement** : 1P-4P : 6 cartes (9,3 × 8,8 cm · 40 pt) ; 5P-8P : 12 cartes (6,2 × 6,6 cm · 22 pt) ; 9S-11S : 20 cartes (4,7 × 5,3 cm · 14 pt).
- **J3 — Familles** : 1P-4P : 6 cartes (9,3 × 8,8 cm · 24 pt) ; 5P-8P : 9 cartes (6,2 × 8,8 cm · 16 pt) ; 9S-11S : 16 cartes (4,7 × 6,6 cm · 12 pt).
- **J4 — Cartes recto-verso** : 1P-4P : 6 cartes (9,3 × 8,8 cm · 28 pt) ; 5P-8P : 8 cartes (9,3 × 6,6 cm · 18 pt) ; 9S-11S : 15 cartes (6,2 × 5,3 cm · 14 pt).
- **J5-a — Plateau · serpent** : 1P-4P : 19 cases (case de 3,8 cm au moins) ; 5P-8P : 34 cases (case de 2,9 cm au moins) ; 9S-11S : 53 cases (case de 2,3 cm au moins).
- **J5-b — Plateau · escargot** : 1P-4P : 15 cases (case de 3,2 cm au moins) ; 5P-8P : 27 cases (case de 2,5 cm au moins) ; 9S-11S : 42 cases (case de 2,1 cm au moins).
- **J5-c — Plateau · chemin** : 1P-4P : 21 cases (case de 3,6 cm au moins) ; 5P-8P : 34 cases (case de 2,7 cm au moins) ; 9S-11S : 55 cases (case de 2,2 cm au moins).
- **J5-d — Plateau · circuit** : 1P-4P : 16 cases (case de 4,4 cm au moins) ; 5P-8P : 24 cases (case de 3,1 cm au moins) ; 9S-11S : 34 cases (case de 2,3 cm au moins).
- **J6 — Dé à monter** : 1P-4P : 1 dé (faces de 6 cm) ; 5P-8P : 2 dés (faces de 4,2 cm) ; 9S-11S : 2 dés (faces de 4,2 cm). Les deux formats de dé sont possibles à tout âge.
- **J7 — Loto** : 1P-4P : 6 cartons (4 cases de 4,7 × 4,4 cm) ; 5P-8P : 8 cartons (6 cases de 3,1 × 3,3 cm) ; 9S-11S : 6 cartons (9 cases de 3,1 × 2,9 cm).
- **J8 — Symboles communs** : 1P-4P : 7 cartes (3 éléments par carte · 9,3 × 6,6 cm) ; 5P-8P : 13 cartes (4 éléments par carte · 6,2 × 5,3 cm) ; 9S-11S : 21 cartes (5 éléments par carte · 6,2 × 3,8 cm).
- **J9 — Trouve quelqu'un qui…** : 1P-4P : 6 cases (9,3 × 7,5 cm) ; 5P-8P : 16 cases (4,7 × 5,6 cm) ; 9S-11S : 25 cases (3,7 × 4,5 cm).
- **J10 — Carte à pinces** : 1P-4P : 6 questions (bloc de 4,0 cm · 3 réponses) ; 5P-8P : 10 questions (bloc de 2,5 cm · 3 réponses) ; 9S-11S : 12 questions (bloc de 2,1 cm · 3 réponses).
- **J11 — Roue à fenêtre et rabat** : 1P-4P : 4 secteurs (deux disques de 12,4 cm) ; 5P-8P : 6 secteurs (deux disques de 12,4 cm) ; 9S-11S : 8 secteurs (deux disques de 12,4 cm).
- **J12 — Lettres à fabriquer** : 1P-4P : 4 plaques (9,3 × 13,2 cm · 130 pt) ; 5P-8P : non proposé ; 9S-11S : non proposé.
- **J13 — Cartes de rôle** : 1P-4P : 4 cartes (9,3 × 13,2 cm · 28 pt) ; 5P-8P : 8 cartes (9,3 × 6,6 cm · 16 pt) ; 9S-11S : 8 cartes (9,3 × 6,6 cm · 14 pt).
- **J14 — Cartes d'erreurs** : 1P-4P : non proposé ; 5P-8P : 4 cartes (9,3 × 13,2 cm · 16 pt) ; 9S-11S : 6 cartes (9,3 × 8,8 cm · 14 pt).
- **J15 — Cartes d'aide graduée** : 1P-4P : 4 cartes (9,3 × 13,2 cm · 28 pt) ; 5P-8P : 8 cartes (9,3 × 6,6 cm · 16 pt) ; 9S-11S : 8 cartes (9,3 × 6,6 cm · 14 pt).
- **J16 — Cartons-réponses** : 1P-4P : 4 cartons (9,3 × 13,2 cm · 110 pt) ; 5P-8P : 4 cartons (9,3 × 13,2 cm · 110 pt) ; 9S-11S : 6 cartons (9,3 × 8,8 cm · 90 pt).
- **J17 — Grille d'alignement** : 1P-4P : 20 ronds (ronds de 3,9 cm · aligner 3) ; 5P-8P : 35 ronds (ronds de 2,9 cm · aligner 4) ; 9S-11S : 48 ronds (ronds de 2,6 cm · aligner 4).
- **J18 — Serpents et échelles** : 1P-4P : 30 cases (case de 3,7 cm au moins) ; 5P-8P : 48 cases (case de 3,0 cm au moins) ; 9S-11S : 80 cases (case de 2,3 cm au moins).
- **J19 — Bataille navale** : 1P-4P : 25 cases par grille (case de 2,0 cm au moins) ; 5P-8P : 36 cases par grille (case de 1,6 cm au moins) ; 9S-11S : 64 cases par grille (case de 1,2 cm au moins).
- **J20 — Roue de tirage** : 1P-4P : 4 secteurs ; 5P-8P : 6 secteurs ; 9S-11S : 8 secteurs (roue de 18,2 cm dans les trois cas).
- **J21 — Puzzles à deux pièces** : 1P-4P : 8 puzzles (9,3 × 6,6 cm · 28 pt) ; 5P-8P : 12 puzzles (9,3 × 4,4 cm · 20 pt) ; 9S-11S : 18 puzzles (6,2 × 4,4 cm · 14 pt).
- **J22 — Puzzle à bandes** : 1P-4P : 5 bandes de 3,7 cm ; 5P-8P : 10 bandes de 1,9 cm ; 9S-11S : 12 bandes de 1,6 cm.
- **J23 — Mot mystère** : 1P-4P : 4 mots (cases de 2 cm) ; 5P-8P : 6 mots (cases de 2 cm) ; 9S-11S : 8 mots (cases de 1,45 cm dans l'exemple).
- **J24 — Cocotte en papier** : 8 défis dans les trois tranches ; corps de 14 pt (1P-4P), puis de 12 pt.
- **J25 — Horloge à aiguilles** : 1P-4P : heures seules ; 5P-8P : heures et minutes ; 9S-11S : heures, minutes et heures de 13 à 24.
- **J26 — Mémo-fiches en éventail** : 1P-4P : 6 fiches (6,2 × 13,2 cm · 22 pt) ; 5P-8P : 8 fiches (4,65 × 13,2 cm · 15 pt) ; 9S-11S : 10 fiches (3,72 × 13,2 cm · 12 pt).
- **J27 — Bandes graphiques** : 1P-4P : 4 bandes de 6,6 cm ; 5P-8P : 6 bandes de 4,4 cm ; 9S-11S : 8 bandes de 3,3 cm.
- **J28 — Plateau à camemberts** : 1P-4P : 37 cases ; 5P-8P : 49 cases ; 9S-11S : 73 cases (case de 1,2 cm au moins).
- **J29 — Cherche et trouve de mots** : 1P-4P : 20 mots en 24 pt ; 5P-8P : 40 mots environ en 16 pt ; 9S-11S : 65 mots environ en 13 pt.
- **J30 — Mots interdits** : non proposé de la 1P à la 4P ; 5P-8P : 9 cartes (6,2 × 8,8 cm · 3 mots interdits) ; 9S-11S : 12 cartes (6,2 × 6,6 cm · 5 mots interdits).
- **J31 — Petit bac** : 1P-4P : 3 catégories, 4 manches ; 5P-8P : 5 catégories, 6 manches ; 9S-11S : 6 catégories, 8 manches.
- **J32 — Cartes à terminaisons** : proposé de la 5P à la 8P : 12 cartes-phrases (9,3 × 4,4 cm · 16 pt) et 24 cartes-terminaisons.
- **J33 — Petits chevaux** : un seul format : 52 cases de 1,24 cm.
- **J34 — Qui est-ce ?** : 1P-4P : 12 éléments ; 5P-8P : 24 éléments ; 9S-11S : 30 éléments.
- **J35 — Bataille** : 1P-4P : 12 cartes (6,2 × 6,6 cm · 30 pt) ; 5P-8P : 16 cartes (4,65 × 6,6 cm · 24 pt) ; 9S-11S : 20 cartes (4,65 × 5,28 cm · 22 pt).
- **J36 — Tuiles-lettres** : 1P-4P : 48 tuiles ; 5P-8P : 117 tuiles ; 9S-11S : 204 tuiles.
- **J37 — Sudoku** : 1P-4P : 4 grilles de 4 × 4 ; 5P-8P : 2 grilles de 6 × 6 ; 9S-11S : 2 grilles de 9 × 9.
- **J38 — Mot caché : la fleur** : un seul format : 3 parties par fiche, fleur en 8 étapes.

### Modèles Word à remplir et planches prêtes à imprimer (boîte à outils, 19.11.2026)

- **Principe** : la boîte à outils contient des fichiers que l'enseignant·e peut utiliser sans IA. L'IA les **signale** quand le gabarit retenu en possède un (MP-J-13), en particulier quand elle ne peut pas livrer de fichier ; si l'enseignant·e joint un modèle, l'IA le remplit **sans modifier les dimensions** des cases ni les repères de coupe.
- **Modèles Word à remplir** (dossier « 06_Modèles de jeux à remplir ») : une page de mode d'emploi, puis les planches des trois tranches d'âge, textes d'exemple en gris à remplacer : J1 dominos ; J2 memory (dos à motif, feuille des paires) ; J3 familles ; J4 cartes de rappel (recto-verso) ; J5 cartes-défis des plateaux (dos à motif, feuille de solutions) ; J7 loto (cartons, cartes d'appel à dos à motif, feuille de contrôle) ; J8 symboles communs (cartes construites et vérifiées par programme) ; J9 grille « Trouve quelqu'un qui… » ; J10 carte à pinces (recto-verso) ; J12 lettres à fabriquer (1P à 4P seulement) ; J13 cartes de rôle ; J14 cartes d'erreurs (recto-verso) ; J15 cartes d'aide graduée ; J16 cartons-réponses ; J28 cartes-questions à six catégories (dos à motif).
- **Planches prêtes à imprimer** (dossier « 07_Planches de jeu prêtes à imprimer », PDF) : plateaux de parcours J5 (quatre formes, trois tranches d'âge) ; dés à monter J6 (grand et petit) ; roues à fenêtre et rabat J11 (trois exemples, à 4, 6 et 8 secteurs) ; grilles d'alignement J17, serpents et échelles J18, fiches de bataille navale J19 et roues de tirage J20 (trois tranches d'âge, versions à nombres ou à lettres) ; exemples des gabarits J21 à J27, un par tranche d'âge (puzzles à deux pièces, puzzle à bandes, mot mystère, cocotte, horloge, mémo-fiches en éventail, bandes graphiques) ; plateaux à camemberts J28, planches de cherche-et-trouve J29, cartes à mots interdits J30 et grilles de petit bac J31 ; cartes à terminaisons J32, petits chevaux J33, grilles de « Qui est-ce ? » J34, cartes de bataille J35, tuiles-lettres J36, sudokus J37 avec solutions, fiche du mot caché J38 ; pages de lignes d'écriture au lignage romand G22 (modules de 7 mm, 4 mm et 2,5 mm) et livret d'écriture A5 ; fiches « syllabes et sons » G23, maisons des nombres G24, reproductions sur quadrillage G25, calendriers G26, étiquettes de l'horaire G27, livret à onglets G28, pages de journal G29, planches de bande dessinée G30 et plans d'exposé G31 ; dos à motif (losanges, carreaux, vagues).
- **Limite** : les modèles reprennent les formats des variantes par tranche d'âge ; pour un autre nombre de pièces, l'IA produit la planche avec `planche_pdf`.
- **Statut** : chaque gabarit J1 à J38 a un document réel depuis le 20.11.2026 ; c'est de ces documents, et d'eux seuls, que sont tirées les miniatures du panorama des jeux et des pages par tranche d'âge (table `SOURCES_JEUX`, Annexe I-C). Modèles et planches produits et regardés sur le rendu (LibreOffice, PDF) les 19 et 20.11.2026 ; non imprimés, non testés en classe ; rendu dans Word non contrôlé.

### Variantes de J2, J3 et J4 (non testées)

- **J2, appariement par la forme** (BDRP-C3) : chaque paire reçoit une coupe différente, ce qui corrige par la forme. Dessin vectoriel R11.
- **J2, cartes en double version** (BDRP-C8) : une version réunit image et mot ; elle sert de corrigé à l'association des cartes séparées. Le code couleur de lot est doublé d'un repère écrit.
- **J3, demande par propriété** (BDRP-D4b) : pour obtenir une carte, l'élève nomme la propriété recherchée.
- **J4, cartes construites par l'élève** (BDRP-C4) : l'élève écrit la réponse, fait corriger, découpe ; une carte réussie sort du paquet, une carte ratée y retourne.

## 3.9 Catalogue des outils d'étayage permanents (SP1 à SP13, v7.2)
<!-- modules : fiches -->

Les outils SP restent sous les yeux de l'élève ou de la classe. SP1 à SP3 sont des sous-mains ; SP4 et SP6 à SP13 des affiches au format GF-V (§ 2.5) ; SP5, des étiquettes. Les codes SP1 à SP8 viennent du balayage BDRP ; SP9 à SP13 les prolongent. Tous sont testés sur rendu (2.11.2026) ; leurs dimensions sont des inférences de conception.

**Zones laissées à la classe** (révision du 2.11.2026, suite) : plusieurs outils SP réservent une colonne ou une case que la classe remplit elle-même (photo, dessin, exemple trouvé en commun). Une telle zone porte toujours un **intitulé en tête de colonne** qui dit ce qu'on y mettra (« Notre photo ou notre dessin », « Notre exemple », « Croquis ») ; une colonne vide sans intitulé se lit comme un oubli de l'IA. L'intitulé compte comme contenu pour V20 ; la zone elle-même reste vide à la livraison.

### SP1 — Bande numérique à triple codage

- **Usage** : même quantité en chiffre, constellation de dé et doigts (TR11, BDRP-E1, MF59).
- **Structure** : trois rangées, 0 à 10 : chiffre ; dé (de 7 à 10 : 5 + n) ; main.
- **Dimensions** : A4 paysage ; onze colonnes de 2,24 cm ; rangées de 1,5, 2,3 et 2,3 cm.
- **Recette** : R9, R14, icônes IC-DE et IC-MAIN.
- **Contrôles** : V1 à V10, V12 ; trait de coupe en tirets entre les deux bandes de la page (MP-J-05).
- **Interdits** : polices ou pictogrammes tiers sans licence. La suite de 11 à 20 n'est pas testée.

### SP2 — Réglette avec repère de latéralité

- **Usage** : alphabet lié, chiffres, repère gauche et droite (TR11, BDRP-E2, MF66, MF67).
- **Structure** : main et mot « gauche » à gauche, main et mot « droite » à droite ; deux rangées de lettres ; une rangée de chiffres.
- **Dimensions** : A4 paysage ; 15 colonnes ; rangées de 1,9 cm ; lettres en 26 pt.
- **Recette** : R10, R14, icônes IC-LAT.
- **Contrôles** : V15, V12 ; trait de coupe en tirets entre les deux réglettes de la page (MP-J-05).
- **Interdits** : main seule, sans le mot ; repère placé du mauvais côté.

### SP3 — Sous-main personnel

- **Usage** : prénom en deux écritures, alphabet lié, suite des nombres jusqu'à 100 (TR11, BDRP-E3).
- **Structure** : bandeau prénom ; alphabet sur deux rangées ; tableau de 5 × 20 nombres.
- **Dimensions** : A3 paysage ; bandeau de 4 cm, rangées de 3 cm et de 1,6 cm.
- **Recette** : R9, R10, R14.
- **Contrôles** : V15, V12.
- **Interdits** : prénom réel dans une demande à l'IA ; prénom pré-imprimé sur le rendu livré : sous l'intitulé « Mon prénom », les deux cellules (script, écriture liée) sont livrées vides et remplies localement par l'enseignant·e, en GE Typo Libre pour la seconde (MP-P-10, R10).

### SP4 — Affiche-procédure en « je »

- **Usage** : procédure en étapes à la première personne (TR18, BDRP-E4).
- **Structure** : titre ; six étapes au plus : numéro, image, texte. La colonne d'images porte l'intitulé « Image » (colonne de 3,5 cm : un intitulé plus long se coupe) et reste vide : la classe la remplit (photo de l'élève en train de faire l'étape, ou dessin) ; aucune image générée. Intitulés en 28 pt gras, ligne de 1,6 cm.
- **Dimensions** : GF-V ; colonnes de 2,2, 3,5 et 19 cm ; étapes de 4,3 cm ; existe en format cahier (A5) au besoin.
- **Recette** : R9, R14.
- **Contrôles** : V17.
- **Interdits** : étape à deux actions ; image générée avec du texte (MP-I-05).

### SP5 — Étiquettes de coin ou de journée

- **Usage** : mot et pictogramme pour organiser la journée ou un coin (TR65, BDRP-E5).
- **Structure** : pictogramme, puis mot en gras.
- **Dimensions** : 8 × 4,8 cm ; six par planche.
- **Recette** : R14, icônes IC.
- **Contrôles** : V12 ; même pictogramme d'un support à l'autre.
- **Interdits** : pictogramme sans mot pour une information nécessaire.

### SP6 — Affiche-métaphore structurante

- **Usage** : donner une image stable à une notion : par exemple les wagons de la phrase (TR17, TR19, BDRP-E6).
- **Structure** (révision du 2.11.2026, suite) : quatre colonnes : **wagon** (forme dessinée R11, nom écrit dans le wagon) ; **nom complet** du groupe ou de la fonction ; **« Comment je le reconnais »** : le test opératoire en « je », tel qu'il est enseigné (déplacement, effacement, remplacement, encadrement, addition) ; **exemple** où le groupe est en gras. Une rangée par groupe, quatre rangées au plus ; une seule manipulation-clé par rangée, la plus discriminante (sujet : encadrement par « C'est … qui » ; complément de phrase : déplacement et effacement ; complément de verbe : ni effacement ni déplacement, remplacement par un pronom ; verbe conjugué : encadrement par « ne … pas »). Trois formats : A3, sous-main, gabarit vide (variante de MF02). Les noms sont les termes complets de la grammaire enseignée, dans la forme du moyen d'enseignement en usage (« complément de verbe », « complément de phrase », jamais « complément » seul) ; l'enseignant·e indique sa terminologie dans le cadrage, l'IA ne la devine pas.
- **Dimensions** : A3 paysage ; quatre colonnes de 4,4, 9, 13,6 et 10 cm ; ligne d'intitulés de 1,2 cm, rangées de 4,9 cm ; nom et exemple en 36 pt, test en 28 pt (quatre lignes au plus par cellule) ; wagon dessiné de 4,3 cm (R11), nom écrit dedans en petit ; titre en 56 pt. Valeurs de l'essai du 2.11.2026 (suite), rendu à 106 % du budget A3 ; inférence de conception.
- **Recette** : R9, R11 (wagons), R14.
- **Contrôles** : V17 ; V21 : chaque exemple réussit le test de sa rangée et échoue au test des autres rangées (vérifié à la main avant la mise en page) ; termes complets.
- **Interdits** : couleur des wagons sans repère écrit ; repérage fondé sur une question (« Qui ? », « Quoi ? », « Où ? ») : la question PEUT figurer en appui dans la colonne « Comment je le reconnais », jamais seule et jamais comme critère, parce qu'elle n'est pas le test enseigné et qu'elle confond complément de verbe et complément de phrase (« Où ? »).
- **Choix de conception** : la version « questions » de l'essai du 2.11.2026 a été remplacée par la version « tests opératoires », conforme aux groupes définis par manipulation dans le PER (L1 16 : « reconnaissance des groupes de la phrase simple par manipulation », complément de phrase « facultatif et permutable ») et aux cinq tests de la référence grammaticale romande (CIIP, 2013). Décision prise par l'IA faute d'arbitrage ; à confirmer par l'enseignant·e.

### SP7 — Affiche-acronyme de stratégie

- **Usage** : initiales qui rappellent une suite d'actions (TR17, BDRP-E7, MF71).
- **Structure** : initiale en 72 pt, action en 48 pt ; quatre lignes.
- **Dimensions** : GF-V ; colonnes de 5 et 19,7 cm ; lignes de 6,8 cm.
- **Recette** : R9, R14.
- **Contrôles** : V17.
- **Interdits** : acronyme imposé sans apprentissage des actions.

### SP8 — Affiche mnémotechnique

- **Usage** : repère pour distinguer des formes proches, par exemple b, d, p, q (TR19, BDRP-E8, MF70).
- **Structure** : forme, puis phrase-repère ou geste décrit ; quatre lignes.
- **Dimensions** : GF-V ; lignes de 6,2 cm ; formes-repères (b, d, p, q) en 100 pt ; colonne de texte assez large pour qu'aucun mot ne soit coupé (sinon : réduire à 32 pt dans les limites de § 2.5, jamais couper un mot).
- **Recette** : R9, R14.
- **Contrôles** : V17.
- **Interdits** : geste dessiné par l'IA sans contrôle ; méthode gestuelle tierce sans source.

### SP9 — Affiche de stratégies

- **Usage** : rendre visibles les étapes d'une tâche, à construire avec les élèves (TR17).
- **Structure** : titre ; six étapes : numéro, pictogramme, texte.
- **Dimensions** : GF-V ; étapes de 4,3 cm ; 32,3 cm de haut sur rendu.
- **Recette** : R9, R14, icônes IC-CON.
- **Contrôles** : V17 ; un pictogramme qui représente une opération porte son signe (+, −, ×, :) ; sinon, pictogramme d'action sans signe.
- **Interdits** : plus de six étapes ; pictogramme d'opération sans signe.

### SP10 — Référentiel collectif

- **Usage** : panneau durable, complété au fil des apprentissages (TR19).
- **Structure** : six rubriques : repère, exemple, case libre à compléter ; les trois colonnes portent un intitulé (« Repère », « Exemple », « Notre exemple », 28 pt gras, ligne de 1,6 cm) ; la troisième reste vide pour la classe.
- **Dimensions** : GF-V ; colonnes de 5, 11 et 8,7 cm ; rubriques de 4,2 cm.
- **Recette** : R9, R14.
- **Contrôles** : V17.
- **Interdits** : exemple fautif (MP-CC-11) ; exemple qui ne contient pas le graphème de sa rubrique (V21, `verifier_graphemes`).

### SP11 — Glossaire de classe

- **Usage** : mot, définition courte, croquis (TR20).
- **Structure** : quatre entrées par affiche ; intitulés de colonnes « Mot », « Ce que ça veut dire », « Croquis » (28 pt gras, ligne de 1,6 cm) ; la colonne « Croquis » reste vide, dessinée par la classe.
- **Dimensions** : GF-V ; colonnes de 6, 12 et 6,7 cm ; entrées de 6,2 cm ; texte en 36 pt.
- **Recette** : R9, R14.
- **Contrôles** : V17 ; exactitude disciplinaire de chaque définition.
- **Interdits** : définition recopiée sans vérification.

### SP12 — Carte mentale

- **Usage** : structure de départ à enrichir (TR21, MF03).
- **Structure** : centre ; quatre branches au cycle 1, six au plus ensuite.
- **Dimensions** : dessin de 37 × 22,5 cm ; texte en 44 pt.
- **Recette** : R9, R11 ; insertion à l'échelle 1.
- **Contrôles** : V17.
- **Interdits** : carte livrée finie quand la classe doit la construire.

### SP13 — Infographie

- **Usage** : chiffres, pictogrammes et textes courts (TR22).
- **Structure** : quatre blocs numérotés dans l'ordre de lecture : chiffre, phrase.
- **Dimensions** : GF-V ; colonnes de 2,2, 9 et 13,5 cm ; blocs de 6,8 cm.
- **Recette** : R9, R14.
- **Contrôles** : V17 ; chaque chiffre a une source, ou porte la mention « exemple fictif ».
- **Interdits** : chiffre inventé présenté comme réel.

# ÉTAPE 4 — CONSTRUIRE : STYLES ET RECETTES TECHNIQUES
<!-- modules : fiches, jeux -->

## 4.1 Un rôle, un style (MP-S-01)

L'IA DEVRAIT créer des styles de paragraphe nommés et les utiliser pour **chaque** élément de même rôle. L'homogénéité visuelle (MP-O-09) devient ainsi structurelle, et l'enseignant·e peut ajuster une taille en un seul endroit. À défaut de styles nommés, la mise en forme directe DOIT être identique pour tous les éléments d'un même rôle.

| Style | Rôle | Réglages (5P-6P ; adapter la taille au degré) |
|---|---|---|
| Fiche-Identité | 1re ligne : Prénom et Date | 14 pt ; lignes par tabulation à points de suite (R7) |
| Fiche-Titre | titre de la fiche | 16-18 pt, gras, **centré**, espace avant et après ≥ 12 pt |
| Fiche-Objectif | objectif formulé pour l'élève | 14 pt ; la phrase seule, sans étiquette (« J'écris… ») ; espace après 12 pt |
| Fiche-Consigne | numéro + consigne | 14 pt, gras ; espace avant 10 pt ; solidaire du suivant |
| Fiche-Données | items, textes, phrases sources | 14 pt ; interligne 1,5 ; solidaire |
| Fiche-Lacune | items à lacune (R2) | 14 pt ; interligne 2,0 ; solidaire |
| Fiche-Exemple | exemple résolu | 14 pt ; l'exemple (ou la réponse d'un item déjà fait) en police d'élèves GE Typo Libre, 17,5 pt, sans gras ni italique (MP-T-10, `ecrire_exemple`) ; solidaire |
| Fiche-Aide | contenu d'un encadré d'aide | 13-14 pt dans un encadré R5 |
| Fiche-Bilan | autoévaluation | 14 pt dans un tableau R6 |
| Fiche-Étape | étape d'une règle du jeu | 14 pt ; numéro, tabulation, texte ; retrait suspendu de 0,8 cm ; une action par étape |
| Fiche-Pièce | texte d'une pièce de jeu (R8) | taille du degré, centré, interligne simple, sans espace avant ni après |
| Fiche-Mention | mention d'une planche (« à découper sur les pointillés ») | 11 pt, italique ; texte destiné à l'adulte qui découpe (inférence de conception) |
| Ens-Titre / Ens-Texte | partie enseignant·e | 13 pt gras / 11 pt |
| Affiche-Titre, Affiche-Texte, Affiche-Étape, Affiche-Détail, Affiche-Cellule | rôles d'une affiche A3 (GF-V) | 72 pt gras centré ; 48 pt ; 48 pt ; 36 pt ; 36 pt centré (§ 2.5) |

## 4.2 Recettes
<!-- modules : fiches -->

Les recettes R1 à R6 servent aux exercices, la recette R7 à l'en-tête, la recette R8 aux planches de pièces des jeux. Les recettes R9 à R14 (v7.2) servent à l'affiche A3, à l'écriture liée, au dessin vectoriel, au recto-verso, aux contrôles combinatoires et aux grilles à zones ; la recette R15 (révision du 2.11.2026), à la planche A5. Chaque recette est décrite pour Word (enseignant·e ou IA intégrée à Word) puis renvoie au module python-docx de l'Annexe I-C, testé avec rendu PDF dans cette version.

### R1 — Lignes d'écriture (MP-E-10)

- **R1a, lignes en tableau (méthode par défaut)** : tableau d'**une colonne**, largeur 16 cm ; chaque ligne du tableau a une **hauteur exacte** de 1,0 cm (table 2.1) ; **seule la bordure inférieure** est visible ; lignes « insécables ». Dans Word : Insertion > Tableau > 1 colonne ; Propriétés du tableau > Ligne > Hauteur exacte ; Bordures > Bordure inférieure seule (et bordures intérieures horizontales).
- **R1b, ligne par tabulation (pour une amorce suivie d'une ligne)** : paragraphe à interligne **exact** de 28 pt ; **tabulation droite à 16 cm avec points de suite « ____ »** ; l'amorce est tapée, puis une tabulation trace la ligne jusqu'à la marge. Dans Word : Format > Tabulations > position 16 cm, alignement droite, points de suite 4. La position d'une tabulation se mesure **depuis la marge**, pas depuis le retrait du paragraphe : avec un retrait, la position reste 16 cm. **R1c, lignes d'écriture romandes (1P à 4P, au choix de l'enseignant·e)** : `bande_lignage(base, lignes, module_mm, couleurs, largeur_mm)` dessine une bande de lignes au lignage romand (plafond et plancher en pointillés, ligne du corps en trait fin, ligne de base en trait épais ; fiche G22), insérée à l'échelle 1 par `inserer_image` ; module de 7 mm pour l'entrée dans l'écriture, de 4 mm ensuite (indication non vérifiée à une source officielle, à confirmer avec les cahiers de l'établissement) ; couleurs « ciel, herbe, terre » seulement si l'impression est en couleur. L'IA propose le choix entre R1a et R1c pour une fiche de 1P à 4P qui comporte une zone d'écriture, et garde le même lignage dans toute la fiche ; sans réponse : lignes simples, annoncées en une ligne.
- **Interdit X-02** : des paragraphes vides consécutifs munis d'une bordure inférieure **fusionnent** à l'impression en une seule ligne. Vérifié dans cette version : trois paragraphes ainsi bordés s'impriment comme une seule ligne en bas d'un grand blanc.

### R2 — Lacune dans une phrase (MP-E-11)

- Réservée aux réponses de **1 à 2 mots**.
- Nombre de tirets bas **calculé** selon la police et la taille (table 2.1) : en Arial 14 pt, 22 tirets bas ≈ 6 cm, 29 ≈ 8 cm.
- Interligne 2,0 sur les items.
- Pour deux éléments séparés (auxiliaire et participe), deux lacunes séparées d'un espace sont admises si chacune mesure au moins 3 cm.

#### Typographie insécable (toutes les recettes)

- Les traits d'union des terminaisons et des segments (« -er », « -ir », « -iss- ») sont **insécables**, ainsi que l'espace de « en -ir ». Sans cela, la fin de ligne peut couper « en - » / « ir » (constaté lors du test du 30.10.2026).
- Dans Word : caractères spéciaux « trait d'union insécable » et « espace insécable » (Insertion > Symbole). Dans le module de l'Annexe I-C, la fonction `ecrire` les applique automatiquement.

### R3 — Tableau à compléter

- Lignes de hauteur **au moins** 1 cm (« au moins », pour que le texte ne soit jamais coupé), **insécables** ; ligne d'en-tête répétée.
- Largeur totale ≤ 16 cm ; largeurs de colonnes **fixées** (grille du tableau), jamais laissées en automatique.
- Bordures fines (0,75 pt) grises ou noires, visibles à la photocopie.

### R4 — Solidarité d'un exercice

- Tous les paragraphes d'un exercice, **sauf le dernier**, sont « solidaires du suivant » ; chaque paragraphe a ses « lignes solidaires ».
- Les lignes de tableau sont insécables.
- Ne **pas** enchaîner la solidarité d'un exercice au suivant (le bloc deviendrait plus haut qu'une page et Word l'ignorerait).
- Placer un **saut de page avant** l'exercice qui ne tient plus dans le budget de la page (Étape 2), plutôt que de compter sur la pagination automatique.
- Espace avant chaque consigne ≥ 10 pt ; un paragraphe vide de 6 pt après un tableau pour éviter que la consigne suivante colle à la dernière ligne (fonction `espace` de l'Annexe I-C).

### R5 — Encadré (rappel, aide, objectif de parcours)

- Tableau 1 × 1 bordé, largeur 16 cm, ligne insécable ; trame très claire (gris ≤ F2F2F2) ou aucune trame.
- Jamais de bordure de paragraphe pour un encadré : même risque de fusion que X-02.

### R6 — Symboles, cases et bilan (MP-C-06)

- Vérifié dans cette version : le caractère **☐** et l'étoile **★** **n'existent pas** dans Arial ni dans Calibri ; le demi-cercle **◐** existe dans Arial mais pas dans Calibri. Ils s'affichent par substitution de police, avec une taille et un aspect qui varient selon l'ordinateur.
- Méthode robuste : **bilan en mots dans des cellules** à entourer (« je sais faire » / « presque » / « j'ai besoin d'aide ») ; cases à cocher = **cellules vides bordées** de 0,6 cm.
- Si des symboles sont utilisés : les vérifier sur le rendu (Étape 5) et toujours les doubler d'un mot (MP-C-02).

### R7 — En-tête de la fiche (MP-O-12)

L'en-tête DOIT suivre cet ordre, sur toutes les fiches :

1. **Prénom et Date, tout en haut de la page** (première ligne) : « Prénom : » suivi d'une ligne, puis « Date : » suivi d'une ligne ; lignes tracées par tabulation à points de suite, jamais par des tirets bas tapés.
2. **Titre centré**, avec un espace avant et après d'au moins 12 pt (une ligne blanche).
3. **Objectif en langage élève** : une phrase à la première personne, **sans étiquette** : ni « Mon objectif : » ni « Objectif : » ; la phrase commence directement, avec une majuscule (« J'écris un verbe au passé composé avec ses deux parties. »), avec le vocabulaire du degré, sans code PER ni jargon, en cohérence avec les indices de réussite. La partie enseignant·e garde sa rubrique « Objectif » (§ 4.3, « En bref »).

Le repère discret de version (♣ ♦ ♠, MP-D-01) se place en en-tête de page, au-dessus ou à droite de la ligne Prénom et Date. Dans Word : un paragraphe avec deux tabulations à points de suite (la première vers le milieu de la ligne, la seconde à 16 cm, alignée à droite), puis le titre centré, puis l'objectif.

### R8 — Planche de pièces à découper (jeux J1 à J6)
<!-- modules : jeux -->

- **Tableau à largeurs fixées** : une colonne par moitié de pièce (pour J1 : 4 colonnes de 4 cm, soit deux dominos de 8 cm par rangée) ; largeur et hauteur totales calculées pour occuper toute la surface utile (MP-J-11), en agrandissant les pièces ou en changeant le nombre de colonnes et de rangées ; jamais de largeur automatique.
- **Repères de coupe** (MP-J-12) : un trait fin dans le prolongement de chaque ligne de coupe, dans les quatre marges. Dans Word : formes « Trait » positionnées par rapport à la page ; plus sûr : planche produite en PDF par le code (traits, pointillés et repères dessinés aux coordonnées exactes), contrôlée sur le rendu (V12) : fonctions `planche_pdf` (pièces de texte, dominos compris) et `reperes_de_coupe` de l'Annexe I-C (19.11.2026). Les planches à zones (R14) restent en .docx : marges de la section réduites à 1,2 cm sur les côtés et à 1,65 cm en haut et en bas, repères ajoutés en formes « Trait » ; aucune fonction ne les pose à ce jour.
- **Lignes à hauteur exacte et insécables** (2,5 cm pour J1).
- **Bordures définies cellule par cellule**, jamais par une bordure globale du tableau : contour de chaque pièce en **pointillés** (trait de coupe, 1 pt) ; séparation interne d'une pièce en **trait plein épais** (2,25 pt) (MP-J-05).
- **Saut de page avant chaque planche** (attribut « saut de page avant » sur la mention de la planche) ; une planche = une page ; une mention courte en haut (style Fiche-Mention), par exemple « Boucle Lune · 16 dominos · à découper sur les pointillés ».
- **Texte des pièces** : style Fiche-Pièce, centré verticalement et horizontalement ; la réponse en gras.
- **Ordre des pièces** : mélangé (MP-J-03 ; fonction `melanger_sans_voisins` de l'Annexe I-C).
- Dans Word : Insertion > Tableau ; Propriétés du tableau > Colonne (largeur fixe) et Ligne (hauteur exacte, fractionnement des lignes interdit) ; Bordures et trame > appliquer à la **cellule** (pointillés ou trait plein épais).
- Testé dans cette version : planche de 2 × 8 dominos rendue avec des rangées de 2,50 cm, une largeur de 16,0 cm et une hauteur de 20,7 cm de la marge haute au dernier trait ; fichier valide au schéma OOXML. Testé le 19.11.2026 : memory des consignes, 12 planches de 3 × 4 cartes de 6,2 × 6,6 cm (18,6 × 26,4 cm) produites en PDF avec repères de coupe et mention dans la marge du haut ; mots centrés sur leur boîte d'encre (le centrage d'images dans des cellules de tableau Word décalait légèrement les mots).

### R9 — Format affiche A3 (v7.2)

- `page_format` règle le format (A3 ou A4), l'orientation et les marges, puis renvoie la largeur et la hauteur utiles.
- `styles_affiche` crée les styles du § 2.5. `distance_lecture_m` calcule la distance de lecture d'un corps.
- Dans Word : Mise en page > Taille > A3 ; imprimer à 100 %, sans « Ajuster à la page ».
- Testé : dix documents rendus en A3 (29,7 × 42 cm mesurés) ; contenu de 32,3 cm de haut au plus en portrait, sous le budget de 33 cm.

### R10 — Écriture liée composée (v7.2)
<!-- modules : fiches, jeux -->

- L'écriture liée est **composée** en GE Typo Libre (`ecrire_cursive`) : jamais dessinée, jamais générée par une IA (MP-CC-11).
- Vérifié dans la session : famille exacte « GE Typo Libre », nom PostScript GETypoLibre, fichier `ge_typo_libre.otf`, incorporation autorisée (fsType 0) ; lettres accentuées, œ, guillemets et apostrophe présents. Le **point médian n'a pas de dessin visible** : la fonction le refuse.
- Le logiciel relie les lettres avec les ligatures de la police. Contrôle : V15, `verifier_cursive_pdf`.
- TrueRomande n'est jamais utilisée pour du texte composé automatiquement (MP-T-09) : les glyphes de É, À, « et » manquent, vérifié dans la session.
- Sans police installée : l'IA le déclare, laisse le modèle en script et écrit « écriture liée à ajouter par l'enseignant·e ».

### R11 — Dessin vectoriel (v7.2)
<!-- modules : fiches, jeux -->

- Pour ce que le .docx construit mal : tracés, labyrinthes, disques, schémas. La classe `Dessin` écrit le même dessin en SVG et en PDF, à l'échelle 1, en millimètres.
- `couloir`, `arrondir`, `labyrinthe`, `roue_J11` servent G19 et J11 ; `plateau_parcours` (19.11.2026) sert J5 ; `de_a_monter` (19.11.2026) sert J6 ; `dos_a_motif` (19.11.2026) imprime le dos des cartes tirées ; `grille_alignement`, `serpents_echelles`, `bataille_navale` et `roue_tirage` (19.11.2026) servent J17 à J20 ; `puzzle_association`, `puzzle_bandes`, `mot_mystere`, `cocotte`, `horloge`, `eventail` et `bandes_graphiques` (20.11.2026) servent J21 à J27 ; `plateau_camemberts`, `planche_lynx`, `cartes_mots_interdits` et `petit_bac` servent J28 à J31, `lignage_romand` et `livret_ecriture` servent G22 ; `cartes_categories` (J28), `petits_chevaux`, `grille_qui_est_ce`, `tuiles_lettres`, `sudoku` et `mot_cache_fleur` servent J33 à J38, `fiche_syllabes_sons` sert G23 ; `maison_des_nombres`, `reproduction_quadrillage`, `calendrier_mensuel`, `etiquettes_horaire`, `livret_a_onglets`, `page_journal`, `planche_bd` et `plan_expose` (21.11.2026) servent G24 à G31 ; `panorama_supports` montre les fiches et supports qui ont un document prêt ; `panorama_jeux` et `panorama_exercices` montrent les gabarits disponibles.
- Insertion dans un .docx : image PNG à 300 ppp, avec `inserer_image`, à la largeur du dessin. Le fichier source reste le SVG ou le PDF. **Couleur (option, 21.11.2026)** : `definir_couleur('bleu')` avant l'appel d'une fonction de dessin teinte les fonds gris (cases spéciales, bandeaux, zones), les symboles de catégorie et les traits du dos des cartes ; teintes disponibles : bleu, orange, vert, violet, ciel, vermillon ; `definir_couleur(None)` revient au noir et blanc. La clarté de chaque gris est conservée : une photocopie en noir et blanc donne le même document. Les modèles Word à remplir ne sont pas concernés.
- Les icônes de la banque IC passent par `icone`. `Dessin` requiert PyMuPDF ; les chemins de police (`POLICES_PDF`) sont ceux de macOS, à adapter sur un autre système.

### R12 — Planche recto-verso (v7.2)
<!-- modules : jeux -->

- `verso_de` inverse les colonnes d'une planche, pour une impression sur le bord long. Pour J10, la colonne des réponses passe au bord gauche du verso ; l'ordre des lignes est inchangé (`carte_a_pinces`, verso=True).
- Le PDF ne prouve pas l'alignement : V13 reste obligatoire sur papier.

### R13 — Contrôles combinatoires (v7.2)
<!-- modules : jeux -->

- `generer_loto` et `verifier_loto` (J7), `plan_projectif` et `verifier_symboles` (J8), `verifier_appariement` (J2, J7, J10), `verifier_code` (GF-X : chaque énigme porte son calcul, qui doit donner un chiffre de 0 à 9), `verifier_graphemes` (GF-J, SP10, cartes de sons).
- Ces contrôles s'exécutent **avant** la mise en page (V11, V19, V21).

### R14 — Grille et planche à zones (v7.2)
<!-- modules : fiches, jeux -->

- `grille` : tableau à largeurs fixées dont chaque cellule reçoit du texte, une image ou de l'écriture liée.
- `planche_zones` étend R8 : pièce découpée en zones superposées, sous-cellules côte à côte, contour en pointillés, séparations internes fines.
- `verifier_case_piece` (révision du 2.11.2026, suite ; MP-J-10) : reçoit les dimensions de la pièce mobile et de la case d'accueil (largeur et hauteur en cm) et refuse toute case qui ne dépasse pas la pièce d'au moins 0,5 cm par côté ; appelée avant `grille` pour tout plateau, tableau ou fiche qui reçoit des pièces mobiles (G12-b, J10 : la pince ; SP5 sur un tableau de journée).
- **Mots coupés** : dans toute cellule, un mot qui se coupe impose une cellule plus large, un item plus court ou une taille réduite dans les limites du degré ; jamais de césure (règle commune à R14 et R15 ; `verifier_mots_coupes` sur le texte extrait du PDF, V12 et V10).

### R15 — Planche A5 (révision du 2.11.2026)
<!-- modules : fiches, jeux -->

- Pour un contenu court qui laisserait une page A4 à moitié vide (MP-O-14) : règle de jeu, petite fiche, bande, ticket, brevet. La feuille A4 porte **deux exemplaires identiques**, séparés par un **trait de coupe en tirets** (1 pt) ; on imprime deux fois moins et on coupe la feuille en deux.
- **Côte à côte** : A4 paysage, deux colonnes A5 portrait ; marges de 1 cm ; retrait intérieur de 0,9 cm ; largeur de contenu 12,05 cm. **Empilé** : A4 portrait, deux rangées A5 paysage ; largeur de contenu 17,2 cm.
- Le contenu garde les tailles du degré (MP-T-01) ; seules les largeurs (tableaux, lignes, images) suivent la largeur de l'exemplaire. Un mot qui se coupe mal dans une cellule étroite impose une cellule plus large ou une taille plus petite dans les limites du degré.
- La planche ouvre une **section propre** ; si le document continue après elle, la section suivante reprend l'A4 et ses marges (`nouvelle_section_a4`).
- Contrôle : V20 sur chaque exemplaire (budget A5 portrait 16,9 cm ; A5 paysage 12,3 cm), trait de coupe exclu de la mesure.
- Dans Word : Mise en page > Orientation > Paysage ; Marges 1 cm ; tableau de deux colonnes de 13,85 cm, ligne de hauteur « au moins » 18,9 cm ; bordure en tirets sur le bord commun seulement ; contenu copié dans les deux cellules.
- Fonction `planche_A5` de l'Annexe I-C. Testé dans cette version : règles de GF-X, J7 et J8, GF-B2 (côte à côte) ; GF-M (empilé) ; remplissage mesuré de 90 % au moins par exemplaire.

## 4.3 Partie enseignant·e : structure fixe
<!-- modules : fiches, jeux, verification -->

La partie enseignant·e est un fichier séparé. Elle DOIT contenir, dans cet ordre :

1. **En bref** : objectif, indices de réussite, moment de la séquence, durée, matériel.
2. **Choix pédagogiques** : codes F, P, MF, G mobilisés, en une ligne chacun.
3. **Ancrage PER** : texte consulté et date, ou **[À VÉRIFIER dans le PER]** ; constat d'adéquation (§ 1.2).
4. **Hypothèses annoncées** (§ 1.1).
5. **Déroulement conseillé** (par exemple lancement oral 5 min, travail 20 min, mise en commun 5 min).
6. **Différenciation** : dispositif (MP-D-02), attribution, extension éventuelle.
7. **Corrigé expliqué** : réponse et « Pourquoi » pour chaque item.
8. **Barème indicatif** ou grille formative sans note.
9. **Erreurs typiques** : erreur → hypothèse → rétroaction actionnable → tâche de reprise.
10. **Ticket de sortie et décision** (MF44) : résultat → suite proposée.
11. **Rapport de conformité** (Étape 5).
12. **Statut des informations** : vérifié dans la session / non vérifié / inférence de conception.

**Pour un jeu (GF-F)**, la partie enseignant·e ajoute :

- dans « En bref », un **tableau d'impression** : page, contenu, quantité, papier, découpe ; Sous le tableau, des **astuces pratiques** : faire lancer le dé dans une boîte ou un couvercle (ou dé en mousse, tapis de feutrine) ; cacher la réponse des cartes question-réponse (pochette, rabat, carte tenue par le camarade qui interroge) ; un sablier par groupe ; un sachet étiqueté par jeu, avec la règle et le corrigé ; un essai recto-verso sur une seule feuille ; le jeu laissé en libre accès après la séance.
- dans « Corrigé expliqué », la **solution du jeu** (ordre de la boucle, paires ou familles), avec un « Pourquoi » pour chaque pièce ;
- dans « Différenciation », les **variantes de jeu** : solo, à trois, mélange des lots ; Pour tout jeu de parcours ou de compétition, proposer aussi une **variante coopérative**, fondée sur l'interdépendance positive et la responsabilité individuelle (Johnson & Johnson, 2009) : un seul pion pour le groupe, contre le sablier ou contre un pion adverse qui avance seul ; un but commun chiffré (tous les pions arrivés en moins de dix tours, vingt cartes réussies) ; des rôles tournants (J13) ; l'aide qui rapporte (si l'explication d'un camarade permet de répondre, les deux avancent) ; l'erreur sans recul (le groupe explique, puis l'élève rejoue) ; des binômes par pion ; un bilan de fin de partie (« qu'est-ce qui nous a aidés ? »).
- dans le rapport de conformité, les contrôles **V11 à V13** (et V14 si le fichier est produit par du code ; V15 à V19 selon le gabarit ; V20 et V21 toujours).

**Pour un jeu ou une dictée**, la partie enseignant·e est une page à part entière, jamais oubliée (V21) : pour un jeu, la règle complète, la solution et le débriefing ; pour une dictée (G20), le texte à dicter en entier. La règle destinée aux élèves est imprimée avec le matériel, en étapes numérotées (MP-J-07), en planche A5 si elle tient sur une demi-page (R15). Avant le test en classe, elle renvoie à la grille « utile, utilisable, acceptable » (Tricot et al., 2003 ; Bibliothèque IA 2).

# ÉTAPE 5 — VÉRIFIER SUR LE RENDU
<!-- modules : verification -->

## 5.1 Obligation (MP-V-01)

La vérification porte sur **ce qui s'imprimera**, pas sur le texte du fichier. L'IA DOIT convertir la fiche en PDF (ou en afficher l'aperçu avant impression) et examiner **chaque page**. Si elle ne peut pas produire ou regarder ce rendu, elle DOIT écrire dans le rapport : « Rendu non contrôlé », puis donner à l'enseignant·e la liste des contrôles du § 5.2 (V1 à V10 pour une fiche ; V11 à V13 en plus pour un jeu), réalisables en quelques minutes sur l'aperçu avant impression.

Lors des essais qui ont conduit à cette version, un audit fondé sur le seul texte du fichier avait estimé une fiche conforme à environ 80 %. Le rendu PDF montrait pourtant quatre pages au lieu de deux, deux exercices coupés et des lignes d'écriture fusionnées.

## 5.2 Contrôle visuel en dix points, et contrôles complémentaires V11 à V21

| N° | Contrôle | Référence |
|---|---|---|
| V1 | Le nombre de pages est celui de la fiche technique ; aucune page remplie partiellement (mesure : V20). | MP-O-11, MP-O-14 |
| V2 | Aucun exercice, consigne, tableau ou encadré n'est coupé entre deux pages. | X-03, MP-O-06 |
| V3 | Chaque zone d'écriture affiche **le nombre de lignes prévu**, à la hauteur prévue. | X-02, MP-E-10 |
| V4 | Chaque lacune a la longueur prévue (comparer à la largeur de la page : 6 cm ≈ un peu plus d'un tiers de la ligne). | MP-E-11, X-10 |
| V5 | Le texte lu par l'élève a la taille du degré ; une seule police. | MP-T |
| V6 | Symboles et cases lisibles et de taille homogène ; aucune information portée par la seule couleur. | R6, MP-C-02 |
| V7 | Rien d'essentiel près des bords ; lignes et tableaux dans la largeur utile. | MP-F-04, MP-F-06 |
| V8 | Aucune trace de la partie enseignant·e (corrigé, barème, niveaux) sur la fiche élève. | X-05, X-11 |
| V9 | En-tête dans l'ordre : Prénom et Date tout en haut, puis titre centré avec un espace avant et après, puis objectif en langage élève, sans étiquette « Mon objectif ». | X-14, MP-O-12 |
| V10 | Relecture orthographique de tout le texte élève : aucune forme fautive ou inexistante, ni dans les consignes, ni dans les exemples, items, distracteurs, banques de mots ou textes d'images ; si l'enseignant·e a demandé une analyse d'erreurs (§ 3.7), chaque forme fautive est marquée, corrigée et justifiée, une seule fois, et les quatre conditions sont vérifiées. | X-13, MP-CC-11, MP-I-05 |
| V11 | **Jeu — unicité et fermeture** : chaque question a une seule réponse dans le lot ; la boucle se ferme (ou chaque paire, chaque famille est complète). Contrôle par programme (Annexe I-C) ou à la main, pièce par pièce. | MP-J-01, X-15 |
| V12 | **Jeu — pièces** : dimensions prévues ; aucune pièce coupée entre deux pages ; traits de coupe (pointillés) distincts des séparations internes (trait plein épais) ; ordre d'impression mélangé ; chaque case d'accueil dépasse la pièce mobile d'au moins 0,5 cm par côté (`verifier_case_piece`) ; la planche occupe toute la surface utile, texte et images centrés ; repères de coupe présents au bord de la feuille pour chaque ligne de coupe. | R8, MP-J-03, MP-J-05, MP-J-10, MP-J-11, MP-J-12 |
| V13 | **Jeu recto-verso** : alignement du recto et du verso contrôlé sur une impression test (le PDF ne suffit pas), si le jeu est imprimé recto-verso. | J4 |
| V14 | **Schéma** : validation OOXML du fichier quand il est produit par du code (facultatif, mais recommandé). | Annexe I-C |
| V15 | **Cursive** : GE Typo Libre est incorporée au PDF ; aucun point médian ; aucune écriture liée en image générée. | R10, MP-CC-11 |
| V16 | **Tracé** : largeur du couloir conforme ; deux portions non voisines séparées d'au moins la largeur + 2 mm ; labyrinthe à chemin unique ; aucun angle vif. | R11, G19 |
| V17 | **Affiche** : corps de la table 2.5 ; au plus six étapes ; lecture réelle depuis la place la plus éloignée ; impression à 100 %. | R9, GF-V |
| V18 | **Montage** : chaque texte tient dans sa fenêtre (calcul), puis un exemplaire est réellement monté et manipulé avant la classe. | R11, J11, J6 |
| V19 | **Combinatoire** : fréquence exacte de chaque élément, aucun doublon, cartes toutes différentes ; un seul symbole commun par paire de cartes. | R13, J7, J8 |
| V20 | **Page pleine** : sur le rendu, chaque page élève atteint au moins 90 % du budget de hauteur (position du dernier élément visible, mesurée sur l'image de la page ; `verifier_remplissage`) et ne déborde pas ; sinon aérer, compléter ou passer en planche A5. Exceptions déclarées : partie enseignant·e, dernière planche d'un jeu à nombre de pièces fixé. | MP-O-14, R15 |
| V21 | **Cohérence didactique** : chaque mot contient le graphème étudié (`verifier_graphemes`) ; chaque réponse d'énigme est calculée et vaut un chiffre de 0 à 9 (`verifier_code`) ; aucune case d'autoévaluation ou de réussite pré-remplie ; chaque question a sa zone de réponse ; un schéma correspond au texte qui le commente ; la consigne d'une grille croisée indique le sens de lecture ; les termes grammaticaux sont complets ; la partie enseignant·e accompagne tout jeu (règle, solution, débriefing) et toute dictée (texte à dicter) ; nombres et notions adaptés à la progression du degré. | MP-CC-11, MP-J-01, MP-P-09 |

V1 à V10 et V12 se contrôlent sur le PDF ou l'aperçu ; V11 sur les données du jeu ; V13 sur papier ; V14 avec un validateur ; V15 sur le PDF ; V16 et V19 par calcul ; V17 dans la classe ; V18 par calcul, puis à la main ; V20 sur le PDF, par mesure ; V21 sur les données et le texte, avant la mise en page, puis sur le PDF.

## 5.3 Grille de relecture courte

À appliquer après le contrôle visuel, avant chaque livraison.

| N° | Question | Référence |
|---|---|---|
| 1 | Public, contexte d'usage et objectif identifiés ; hypothèses annoncées ; adéquation PER examinée ? | Étape 1, MP-P-09 |
| 2 | Fiche technique produite ; budget ≤ 22 cm par page respecté ? | Étape 2, MP-O-11 |
| 3 | A4, marges de 2,5 cm, largeur utile de 16 cm ? | MP-F-01 à MP-F-06 |
| 4 | Une police, taille conforme au degré, texte aligné à gauche, pas de majuscules continues ? | MP-T |
| 5 | Structure numéro → consigne → données → réponse identique ; un rôle, un style ? | MP-O-01, MP-O-09, MP-S-01 |
| 6 | Consignes directes, courtes, sans titre, sans négation, une action par phrase ? | MP-CO-01 à MP-CO-05 |
| 7 | Zones d'écriture construites avec R1 (jamais de tirets bas pour une phrase), en nombre suffisant ? | MP-E-05, MP-E-10, X-01, X-02 |
| 8 | Lacunes calibrées (R2) et cohérentes avec la réponse attendue ? | MP-E-11, MP-CO-07 |
| 9 | 3-5 exercices courts ou 1-2 longs par page ; au plus 4 éléments principaux par exercice ? | MP-O-04, MP-CI-02 |
| 10 | Exemple résolu pour toute tâche nouvelle ; aides placées au-dessus de l'exercice ; pré-training ≤ ¼ de page ? | MP-CC-04, MP-CC-06, MP-PT |
| 11 | Différenciation sans étiquette évaluative ; chaque version dans son budget ? | MP-D-01, MP-D-03 |
| 12 | Partie enseignant·e séparée et complète (structure § 4.3) ? | Étape 4 |
| 13 | Contrôle visuel V1-V10 effectué (ou impossibilité déclarée) ; V20 (page pleine) et V21 (cohérence didactique) ; pour un jeu, V11 à V13 ; pour un fichier produit par du code, V14 ? | MP-V-01, MP-O-14 |
| 14 | En-tête conforme : Prénom et Date en première ligne, titre centré entre deux espaces, objectif en langage élève sans étiquette ? | MP-O-12, R7 |
| 15 | Aucune forme écrite fautive ou inexistante montrée à l'élève, y compris dans les exercices de jugement, hors analyse d'erreurs demandée et conforme aux quatre conditions du § 3.7 ? | MP-CC-11, X-13 |
| 16 | Jeu : une seule pièce correcte par question, aucun indice non visé, ordre mélangé, autocorrection intégrée, règle en étapes avec un exemple hors lot, modalité adaptée à la notion, cases d'accueil plus grandes que les pièces mobiles ? | MP-J-01 à MP-J-08, MP-J-10, X-15 à X-17 |

La grille détaillée (audit ou transformation d'une fiche existante) figure en Annexe I-B.

## 5.4 Rapport de conformité (MP-V-02)

L'IA DOIT livrer un rapport court, dans ce format :

| Contrôle | Constat | Statut |
|---|---|---|
| V1 Pages | 2 pages, conforme à la fiche technique | conforme |
| V3 Lignes | ex. 4 : 4 lignes visibles sur 4 prévues | conforme |
| G9 colonnes | colonnes de réponse de 4,2 cm au lieu de 5 cm (5 colonnes sur 16 cm) | **écart déclaré** |
| V6 Symboles | ☐ affiché par substitution de police | **à vérifier sur l'ordinateur de l'école** |
| V11 Unicité (jeu) | 16 réponses distinctes ; chaque question a une seule réponse ; boucle fermée (vérification par programme) | conforme |
| V20 Page pleine | p1 95 %, p2 92 % du budget (mesure du rendu) | conforme |

Puis : **Écarts assumés** (du plus important au plus mineur, avec leur justification) et **Statut des informations** (MP-V-03) : ce qui a été vérifié dans la session (avec la source), ce qui ne l'a pas été, ce qui relève d'une inférence de conception.

# ÉTAPE 6 — LIVRER
<!-- modules : verification -->

## 6.1 Gabarits de fiches et de dossiers de jeu
<!-- modules : fiches -->

Les éléments entre chevrons `< >` sont à remplacer. Les durées figurent **dans la partie enseignant·e**, jamais sur la fiche élève. `[lignes : n]` désigne n lignes R1a ; `[encadré]` un encadré R5 ; `[bilan R6]` un bilan en mots dans des cellules.

### GF-A — Fiche d'entraînement (2 pages au maximum, environ 30 minutes)

```
Prénom : ____________________     Date : ______________   (R7, 1re ligne)

                     <Titre de la fiche>                 (centré)

<objectif : une phrase à la 1re personne, en langage élève, sans étiquette>

[encadré] Rappel : <règle courte> — Exemple : <exemple résolu>
          (≤ ¼ de page ; seulement si la notion est nouvelle, fragile,
           réactivée ou combinée)

1  <Consigne directe — repérage>
   <3 à 5 items selon le gabarit>

2  <Consigne directe — entraînement>
   <items + zones selon le gabarit>

—— saut de page placé d'après la fiche technique ——

3  <Consigne directe — entraînement, variante>
   <items + zones>

4  <Consigne directe — transfert ou production>
   [lignes : 2 par phrase demandée ; 5-6 pour un mini-récit]

Je fais le point   [bilan R6 : 3 critères × je sais faire / presque / j'ai besoin d'aide]
```

### GF-B — Fiche d'évaluation (2 pages au maximum, 25-35 minutes)

```
Prénom : ____________________     Date : ______________   (R7, 1re ligne)

                 <Titre — Évaluation>                    (centré)

<ce que je dois montrer, en langage élève, sans étiquette>     Total : ___ / ___

1  <Consigne — connaissances de base>                       … / __
2  <Consigne — application>                                 … / __
—— saut de page placé d'après la fiche technique ——
3  <Consigne — tâche plus complète>                         … / __
   [lignes : selon la production attendue]
Bonus ★ (facultatif)                                        … / __
```

Règles propres : ni pré-training ni aide-mémoire (MP-PT) ; barème visible ; items courts et une tâche complexe.

### GF-C — Fiche de remédiation (2 pages au maximum, 20-30 minutes)

```
Prénom : ____________________     Date : ______________   (R7, 1re ligne)

                 <Titre — Je reprends …>                 (centré)

<objectif : une phrase en langage élève, sans étiquette>

1  Coche ce qui te correspond.   [cases R6 : 4 énoncés de difficulté]
   Avec ton enseignant·e, écris correctement un mot ou une forme
   qui te pose souvent problème.   [lignes : 2]
2  [encadré] Rappel : <règle courte> — Exemple : <exemple résolu>
3  <Consigne — entraînement guidé ; aide placée à côté de chaque item>
—— saut de page placé d'après la fiche technique ——
4  <Consigne — entraînement sans aide>
5  <Consigne — re-test : 2 items>
```

### GF-D — Devoir à la maison (1 page, environ 10 minutes)

En-tête R7 (Prénom et Date, titre centré, objectif). Quatre à six items courts et une question « explique ». Consignes compréhensibles **sans adulte**. Pas de pré-training ; une banque de mots PEUT figurer en bas de page avec la mention « Utilise cette aide si tu en as besoin ».

### GF-E — Ateliers (une page par station)

Quatre stations au plus (lire, manipuler, écrire, numérique) ; même structure visuelle d'une station à l'autre (MP-O-09) ; seul le contenu change.

### GF-F — Dossier de jeu (règle 1 page par groupe ; 1 page par planche ; trace 1 page)
<!-- modules : fiches, jeux -->

Pièces du dossier, dans cet ordre :

1. **Règle du jeu et carte-mémoire** (1 page par groupe) : titre centré, sans ligne Prénom et Date (MP-J-09) ; phrase d'organisation ; exemple résolu fait de pièces hors lot ; règle en étapes numérotées (style Fiche-Étape, une action par étape) ; carte-mémoire (tableau de référence) dont la règle précise qu'elle sert à vérifier après la pose.
2. **Planches** (annexes à découper) : une page par planche (R8), mention courte en haut ; un lot par couleur de papier, sans repère de niveau (MP-J-06).
3. **Fiche de trace individuelle** (1 page au maximum) : en-tête R7 ; un ou deux exercices G (par exemple G3 et G7) qui font écrire la forme travaillée ; bilan R6.
4. **Partie enseignant·e** (fichier séparé) : structure du § 4.3, avec le tableau d'impression, la solution du jeu et les variantes.

```
<Titre du jeu>                                   [titre centré, sans Prénom ni Date]
Joue avec un ou une camarade.
Exemple : <question> donne <réponse>.            [Fiche-Exemple ; <réponse> en police d'élèves, MP-T-10]
[2 pièces hors lot]                              [R8 sans saut de page]
1  <Une action>                                  [Fiche-Étape]
2  <Une action>
…
<Carte-mémoire>                                  [tableau de référence]
—— saut de page avant chaque planche ——
<Lot> · <n> pièces · à découper sur les pointillés   [Fiche-Mention]
[planche R8 : ordre mélangé, coupe en pointillés, séparation en trait plein épais]
—— saut de page ——
Prénom : ____________________     Date : ______________   (R7, 1re ligne)
                     <Titre de la trace écrite>
<objectif en langage élève, sans étiquette>
1  <Consigne : écrire la forme travaillée>
   a) …   b) …   c) …
[bilan R6]
```

### GF-G — Feuille de route par niveaux

- **Usage** : rendre visible une progression en autonomie (TR60, BDRP-B1, MF43).
- **Structure** : en-tête R7 ; tableau « niveau, ce que je sais faire, validé par, date » ; phrase rappelant qu'un niveau se reprend.
- **Dimensions** : 1 page ; colonnes de 2,4, 7,1, 3,5 et 3 cm ; lignes de 1,3 cm ; six à huit niveaux.
- **Recette** : R7, R14.
- **Contrôles** : V1 à V10.
- **Interdits** : visuels de jeux commerciaux ; niveau affiché comme étiquette de l'élève (X-05).

### GF-H — Trace longitudinale

- **Usage** : même tâche à plusieurs moments, pour voir ses progrès (TR71, BDRP-B2, P21).
- **Structure** : titre ; deux cadres de dessin par page, chacun avec le mois et le prénom.
- **Dimensions** : 1 page ; cadre de 16 × 7 cm ; lignes de 1,2 cm.
- **Recette** : R14.
- **Contrôles** : V1, V3, V7.
- **Interdits** : usage normatif ; production nominative transmise à une IA : l'IA conçoit le gabarit vierge seulement.

### GF-I — Menu à choix

- **Usage** : choix structuré dans un cadre d'exigence (TR61, BDRP-B3, MF46, MF68).
- **Structure** : en-tête R7 ; tableau « obligatoire » ; tableau « au choix » ; question sur les choix faits.
- **Dimensions** : 1 page ; colonnes de 14 et 2 cm ; lignes ≥ 1 cm.
- **Recette** : R7, R14, R1a.
- **Contrôles** : V1 à V10.
- **Interdits** : choix d'exigence inégale ; objectif essentiel placé dans la partie au choix.

### GF-J — Page-son

- **Usage** : étude d'un graphème (TR08, BDRP-A9, MF39, MF66).
- **Structure** : en-tête R7 ; modèle lié, script et capitale, image-clé ; syllabes ; trois mots en deux écritures ; phrase en deux écritures ; copie.
- **Dimensions** : 1 page ; 3P-4P, 18 pt ; modèle lié en minuscule et en majuscule (« ch », « Ch »), 56 pt ; mots et phrase liés en 26 pt ; lignes de 1,2 cm.
- **Recette** : R7, R10, R14, R1a.
- **Contrôles** : V1 à V10, V15.
- **Interdits** : graphème non encore étudié dans les mots ; mot qui ne contient pas le graphème (V21) ; écriture liée dessinée ou générée ; image à dénomination ambiguë.

### GF-K — Carnet de rituel

- **Usage** : même micro-production quotidienne, référentiel à portée de main (TR71, BDRP-B5).
- **Structure** : page quotidienne invariable ; page-référentiel en trois colonnes. La date se demande une seule fois : en-tête R7 sans ligne Date sur la page quotidienne, la date étant écrite dans l'entrée du jour.
- **Dimensions** : 2 pages ; lignes de 1,2 cm ; 18 pt en 3P-4P.
- **Recette** : R7, R14, R1a.
- **Contrôles** : V1 à V10.
- **Interdits** : donner une correction publique du carnet.

### GF-L — Dossier de défis

- **Usage** : série de défis numérotés avec validation (TR60, BDRP-B6).
- **Structure** : en-tête R7 ; consigne ; 12 cases numérotées, chacune avec un défi rédigé, une zone de réponse et la mention « oui · pas encore » à entourer.
- **Dimensions** : 1 page ; cases de 5,33 × 3,6 cm.
- **Recette** : R7, R14.
- **Contrôles** : V1 à V10.
- **Interdits** : compétition affichée entre élèves ; case de défi vide ou mention de réussite pré-remplie (« Réussi : oui ») (V21).

### GF-M — Brevet d'étape

- **Usage** : reconnaître une compétence validée (TR60, BDRP-I1).
- **Structure** : titre ; prénom ; compétence en « je » ; tableau date, validé par, prochaine étape.
- **Dimensions** : A5 paysage, deux brevets par feuille A4 (planche A5 empilée, R15) ; titre en 40 pt ; texte en 18 pt.
- **Recette** : R14, R15.
- **Contrôles** : V5, V7, V10, V20.
- **Interdits** : épreuve sommative déguisée ; absence de reprise possible.

### GF-N — Fiche théorique

- **Usage** : fixer une règle après la découverte (TR04).
- **Structure** : en-tête R7 ; encadré « Règle » ; tableau d'exemples ; encadré « Attention » ; mention de rangement.
- **Dimensions** : 1 page ; une règle, deux à trois exemples, un cas particulier. Le tableau d'exemples couvre **chaque cas énoncé par la règle** (une règle « -s ou -x » montre un exemple en -s et un exemple en -x) ; sinon, l'énoncé de la règle se limite aux cas illustrés.
- **Recette** : R5, R7, R14.
- **Contrôles** : V1 à V10.
- **Interdits** : items à résoudre (la fiche clôt, elle ne fait pas chercher) ; forme fautive en contre-exemple (X-13).

### GF-O — Fiche guide

- **Usage** : marche à suivre gardée sous les yeux (TR05) ; fiche d'accompagnement d'un objet, protocole d'expérience, chemin de recherche ou fiche d'usage (TR39, TR40, TR55, TR58).
- **Structure** : en-tête R7 ; exemple résolu ; tableau de six étapes au plus : numéro, action, image.
- **Dimensions** : 1 page ; colonnes de 1,2, 9,8 et 5 cm ; étapes de 2 cm.
- **Recette** : R7, R14.
- **Contrôles** : V1 à V10.
- **Interdits** : étape à deux actions ; image éloignée de son texte (MP-CC-04) ; notation abrégée non enseignée (« = 2 3 ») : on écrit la forme complète (« 2 dizaines et 3 unités », « 20 + 3 »).

### GF-P — Fiche de synthèse

- **Usage** : résumé à compléter d'une séquence (TR06).
- **Structure** : en-tête R7 ; phrases à trous ; schéma à légender (schéma conforme au contenu des phrases) ; trois questions d'auto-test, chacune suivie d'une ligne de réponse ; verso : « Je vérifie » (réponses) et « Pour aller plus loin » (une question, des lignes).
- **Dimensions** : recto de 22 cm au plus ; verso ; schéma de 14,5 × 5,6 cm.
- **Recette** : R2, R7, R11, R14.
- **Contrôles** : V1 à V10.
- **Interdits** : synthèse livrée finie ; détail décoratif.

### GF-Q — Questionnaire sur document

- **Usage** : chercher une information dans un document réel (TR13) ; variante image (TR24 : je vois, je pense, je me demande) ; variante d'exploration d'une simulation (TR53 : question à tester, essais notés).
- **Structure** : en-tête R7 ; cadre pour le document ; question d'usage ; étapes de recherche ; explication.
- **Dimensions** : cadre de 16 × 6 cm ; 1 page.
- **Recette** : R2, R7, R14, R1a.
- **Contrôles** : V1 à V10.
- **Interdits** : document généré présenté comme authentique ; donnée personnelle visible.

### GF-R — Dossier documentaire et grille de croisement

- **Usage** : enquêter à partir de documents réels (TR14, P17).
- **Structure** : page 1 : question d'enquête et liste des documents (numéro, titre, nature, source). Page 2 : grille de croisement (G9), réponse citant au moins deux documents.
- **Dimensions** : 2 pages ; quatre à six documents ; cellules de 4,5 × 1,8 cm.
- **Recette** : R5, R7, R14, R1a.
- **Contrôles** : V1 à V10 ; chaque source a été consultée.
- **Interdits** : source inventée ; document généré présenté comme réel.

### GF-S — Fiche-trace de sortie

- **Usage** : observer sur le terrain, puis exploiter en classe (TR41) ; relevé d'observations d'une expérience (TR40).
- **Structure** : en-tête R7 ; cadre de dessin et rubriques ; ce que j'entends ; question à poser ; mention pour le retour.
- **Dimensions** : 1 page ; cadre de 9 × 6 cm.
- **Recette** : R7, R14, R1a.
- **Contrôles** : V1 à V10.
- **Interdits** : questionnaire fermé qui empêche d'observer.

### GF-T — Billet de sortie

- **Usage** : mini-retour de fin de leçon (TR66, MF44, MF32).
- **Structure** : trois billets par page : prénom et date ; ce que j'ai compris ; ce qui me reste à comprendre ; trois mots à entourer, précédés de la consigne « Entoure un mot : ».
- **Dimensions** : billet de 16 × 6,4 cm ; zones de 1, 2,2, 2,2 et 1 cm ; marges intérieures de 0,25 cm ; billets séparés par un intervalle et un trait de coupe en tirets.
- **Recette** : R14.
- **Contrôles** : V1, V7, V10 ; MP-J-09 s'applique : le billet n'a pas de titre ni d'objectif.
- **Interdits** : note ; émoji (X-08).

### GF-U — Page de carnet de bord

- **Usage** : entrée courte et régulière (TR71, MF35).
- **Structure** : en-tête R7 sans ligne Date (la date est celle de l'entrée, demandée une seule fois) ; date de l'entrée ; trois questions-guides ; cadre pour une trace collée.
- **Dimensions** : 1 page ; 7 lignes de 1 cm ; cadre de 16 × 4 cm.
- **Recette** : R7, R14, R1a.
- **Contrôles** : V1 à V10.
- **Interdits** : donnée personnelle transmise à une IA.

### GF-V — Affiche A3

- **Usage** : format de base de TR17 à TR22 ; ne contient pas d'exercice.
- **Structure** : titre ; six lignes au plus ; repère, image, texte.
- **Dimensions** : § 2.5.
- **Recette** : R9, R14.
- **Contrôles** : V5, V7, V10, V17.
- **Interdits** : corps sous le plancher ; texte en paragraphe.

### GF-W — Planche de BD

- **Usage** : récit en cases pour présenter une notion (TR23, MF40).
- **Structure** : en-tête R7 ; six cases : image, puis texte ajouté dans le document.
- **Dimensions** : cases de 8 × 3,8 cm ; bandes de texte de 1,2 cm.
- **Recette** : R7, R14.
- **Contrôles** : V1 à V10 ; stéréotypes et anachronismes relus.
- **Interdits** : texte généré dans l'image (MP-I-05).

### GF-X — Dossier d'escape game

- **Usage** : énigmes en équipe (TR37, P10, MF64), à partir de GF-F.
- **Structure** : mise en situation, règle et rôles (planche A5, R15) ; planche de cartes-énigmes ; feuille d'équipe (énigme, raison, chiffre, code, débriefing) ; partie enseignant·e (solution, débriefing). Consignes adressées à l'équipe, au pluriel (« Prenez »), sans mélange avec le singulier.
- **Dimensions** : 3 pages ; cartes de 8 × 6,5 cm ; cellules de 1,5 cm.
- **Recette** : R7, R8, R13 (`verifier_code`), R14.
- **Contrôles** : V11 (chaque énigme donne un seul chiffre, la suite donne le code), V12 ; V21 : chaque réponse est calculée par programme et vaut un chiffre de 0 à 9 (`verifier_code` avec le calcul de chaque énigme).
- **Interdits** : énigme sans lien avec l'objectif ; énigme dont la réponse a deux chiffres ou qui en admet plusieurs ; débriefing absent.

### GF-Y — Fiche de comparaison pour le débat

- **Usage** : comparer des productions inventées, puis argumenter (TR62, P05, P13, MF28).
- **Structure** : en-tête R7 ; deux productions ; tableau de critères ; avis écrit.
- **Dimensions** : 1 page ; colonnes de 6, 1,2, 1,2 et 7,6 cm.
- **Recette** : R7, R14, R1a.
- **Contrôles** : V1 à V10.
- **Interdits** : production d'élève identifiable ; forme écrite fautive (X-13) ; mention « (inventée) » ou « (exemple fictif) » sur la face élève : le caractère fictif des productions est dit dans la partie enseignant·e.

### GF-Z — Fiche de commentaire de galerie

- **Usage** : commenter une production affichée (TR63, MF56).
- **Structure** : deux commentaires par page : un point fort, une piste, avec un modèle de phrase ; les deux commentaires sont séparés par un trait de coupe en tirets (MP-J-05, R15).
- **Dimensions** : 1 page ; quatre lignes par commentaire.
- **Recette** : R1a.
- **Contrôles** : V1, V3, V10.
- **Interdits** : exposer sans l'accord de l'élève.

### GF-AA — Grille d'évaluation et version élève

- **Usage** : outil de jugement de l'enseignant·e et version en « je » (TR68, TR67).
- **Structure** : page 1 (destinée à l'adulte) : critères × trois niveaux décrits. Page 2 : en-tête R7, mêmes critères en « je », bilan R6, puis « Ce que je vais améliorer » et des lignes.
- **Dimensions** : quatre colonnes de 4 cm ; cellules ≥ 2 cm ; 11 pt pour la page adulte.
- **Recette** : R6, R7, R14.
- **Contrôles** : V5, V8 ; critères alignés sur l'objectif ; [À VÉRIFIER dans le PER] si le texte n'a pas été consulté.
- **Interdits** : niveau défini par un adverbe seul ; version élève différente de la grille de l'adulte : mêmes critères, dans le même ordre, mêmes trois niveaux, formulés en « je » (contrôle ligne à ligne, V5) ; consigne « J'entoure le niveau que j'ai atteint. » obligatoire sur la page élève.

### Variantes de GF-B

- **GF-B2 — Grille à deux niveaux** (BDRP-B4) : colonnes « critères de base » et « perfectionnement ». Colonnes de 4, 6 et 6 cm. Objectif en langage élève en tête (R7) ; l'objectif du PER, ou la mention [À VÉRIFIER dans le PER], figure dans la partie enseignant·e, jamais sur la fiche élève. Courte : lignes de commentaire, puis planche A5 (R15).
- **GF-B3 — En-tête d'évaluation avec ressenti et aménagements** (BDRP-B7, MF73, variante de MF32) : deux bandeaux sous R7, tous deux faits de **zones de tracé**, jamais de lignes d'écriture (révision du 2.11.2026, suite). Bandeau 1 « Avant de commencer » : consigne « Entoure comment tu te sens. » ; trois repères à entourer (mots, par exemple « prêt·e · un peu inquiet·ète · perdu·e » ; aucun émoji, X-08), cellules de 4 à 6 cm × 1,1 cm. Bandeau 2 « Mes aménagements » : consigne « Coche ce que tu utilises. » ; cases à cocher (carré de 0,8 cm en bordure de la première colonne) devant chaque aménagement, trois à six items, lignes de 0,8 cm. Le reste de la page est l'évaluation elle-même (gabarit G ou GF) : **toute tâche de tracé ou de dessin (« Trace… », « Dessine… ») reçoit un cadre vide de 16 cm de large et de 2,4 cm au moins**, jamais des lignes d'écriture ; une question reçoit une ligne (R1b) ou une lacune (R2). Pour la page pleine, compléter par le contenu de l'évaluation, pas par des items d'aménagement (MP-O-14) ; les deux bandeaux tiennent en 6 cm. Les aménagements cochés restent visibles des pairs : à réserver à une version individuelle.

Tous les gabarits GF-G à GF-AA, GF-B2 et GF-B3 sont testés sur rendu (2.11.2026, LibreOffice, PDF regardé page par page, schéma OOXML valide) ; leurs dimensions sont des inférences de conception, à ajuster après usage (MP-P-08).

## 6.2 Barèmes et codes de retour
<!-- modules : fiches -->

**Barème générique par item (0-1-2)** : 2 = correct, avec la méthode ou la justification si elle est demandée ; 1 = idée juste, mais erreur de forme ou oubli partiel ; 0 = hors sujet ou non fait.

**Production écrite (/4)** : contrainte respectée (1) + contenu (1) + forme (1) + clarté (1).

**Fiche d'entraînement** : un retour critère par critère (« acquis » / « en cours » / « à revoir ») est préférable à une note.

## 6.3 Instruction système (projet ou assistant personnalisé)
<!-- modules : noyau -->

> Tu conçois des ressources pédagogiques imprimées (fiches et jeux) pour l'école obligatoire romande (PER, 1P à 11S). Tu utilises le Référentiel pédagogique IA joint. Pour toute ressource imprimée destinée aux élèves (fiche, jeu de cartes, dominos, plateau, dé à monter), tu appliques le **Livre I** dans l'ordre : cadrage → **fiche technique avec budget de page** → choix du gabarit (G pour un exercice, J pour une pièce de jeu, GF pour un document, SP pour un outil permanent) → construction avec les recettes R1 à R14 → **contrôle sur le rendu PDF** → livraison (fiche élève ou dossier de jeu .docx, partie enseignant·e .docx séparée, rapport de conformité). Pour un jeu : chaque question a une seule réponse dans le lot, aucune pièce ne se trouve par un indice non visé, l'ordre d'impression est mélangé, tu vérifies l'unicité et la fermeture avant de livrer, et pour une notion orthographique le jeu fait lire ou écrire la forme. Chaque fiche individuelle commence par Prénom et Date tout en haut, puis le titre centré (espace avant et après), puis l'objectif en langage élève. Quand le contenu ne tient pas, tu réduis le contenu, jamais les dimensions. Tu n'utilises jamais de tirets bas pour une réponse d'une phrase. Par défaut, tu ne montres jamais à l'élève une forme écrite fautive ou inexistante (ni phrase à corriger, ni distracteur ou exemple mal orthographié) ; seule exception : une analyse d'erreurs que l'enseignant·e demande explicitement, dès la 5P, aux quatre conditions du § 3.7. Avant de produire un jeu, tu montres le panorama des jeux (ou la page de miniatures de la tranche d'âge), tu proposes deux ou trois gabarits et tu attends le choix, sauf si le gabarit est déjà nommé (MP-J-13) ; pour des cartes tirées, tu demandes d'abord si le dos est à motif ou blanc, avec ou sans mention personnelle (MP-J-14) ; tu signales le modèle Word ou la planche prête à imprimer qui existe pour ce jeu. Désignation suisse des degrés uniquement ; les élèves n'utilisent pas d'IA (de la 9S à la 11S, seulement aux conditions du cadre cantonal, § 1.5) ; tutoiement et impératif pour l'élève, vouvoiement et point médian pour l'adulte. Si la discipline, la notion ou le degré manquent, tu poses la question ; pour le reste, tu fais une hypothèse et tu l'annonces.

## 6.4 Prompts courts pour les enseignant·e·s
<!-- modules : noyau -->

#### Créer

```
Fiche d'entraînement — 5P — français — <notion> — 30 min.
Applique le Livre I : d'abord le cadrage et la fiche technique,
puis la fiche élève et la partie enseignant·e en .docx,
puis le rapport de conformité.
```

**Auditer** (joindre le **PDF** ou une capture de chaque page, pas seulement le .docx)

```
Audite cette fiche selon l'Étape 5 du Livre I :
d'abord le contrôle visuel V1-V10 sur le PDF (V11 à V13 pour un jeu),
puis la grille courte.
Liste les écarts par code, du plus grave au plus mineur.
```

#### Créer un jeu

```
Jeu imprimé — 5P — français — <notion> — duo, partie de 10 min.
Applique le Livre I : cadrage (modalité, interprétation de la notion),
fiche technique avec les planches, gabarit J, puis le dossier de jeu
et la partie enseignant·e en .docx. Vérifie l'unicité des réponses
et la fermeture (V11), puis le rendu des planches (V12).
```

#### Voir les possibilités

```
Quels jeux imprimés peux-tu produire avec la bibliothèque ?
Affiche le panorama des jeux (MP-J-13), puis propose-moi
les deux ou trois gabarits qui conviennent à :
<degré> — <discipline> — <notion> — <durée et nombre de joueurs>.
Attends mon choix avant de produire.
```

#### Analyser, puis transformer

```
Analyse cette fiche et rédige un bref rapport, en quelques points (§ 0.6) :
ce que tu en comprends, ce qui fonctionne, les possibilités d'amélioration numérotées.
Termine en demandant de confirmer ou de corriger ta lecture.
```

# ANNEXE I-A — STANDARD DE MISE EN PAGE MP-* (RÉFÉRENCE DES CODES)
<!-- modules : noyau -->

Cette annexe rassemble toutes les règles codées utilisées dans les fiches techniques, les rapports de conformité et les audits. Les Étapes 0 à 6 en indiquent l'usage ; en cas de doute sur une valeur chiffrée, la table 2.1 fait foi.

## Résumé en 21 règles

| N° | Règle | Référence détaillée |
|---|---|---|
| N1 | Identifier le public (degré, statut de lecture), le contexte d'usage et le type d'objectif (comprendre, agir, explorer) **avant** de générer. | MP-P-01 à MP-P-06 |
| N2 | A4 portrait par défaut, marges de 2,5 cm, aucune information essentielle près des bords. | MP-F-01 à MP-F-04 |
| N3 | Une police sans empattement (deux au maximum), taille selon le degré : 24 pt (1P-2P), 18 pt (3P-4P), 14 pt (5P-6P), 12 pt (7P-8P). | MP-T-01, MP-T-02 |
| N4 | Texte aligné à gauche, jamais justifié ; centrage réservé aux titres courts et éléments isolés. | MP-T-07 |
| N5 | Interligne 1,5 pour la lecture, 2,0 minimum pour l'écriture ; lignes d'écriture d'environ 8-10 mm. | MP-E-01 à MP-E-03 |
| N6 | Structure fixe et identique dans toute la fiche : numéro → consigne → données → zone de réponse. | MP-O-01 |
| N7 | Consigne directe sans titre d'exercice, en une phrase courte ; une seule action par phrase ; étapes numérotées si plusieurs actions ; pas de négation. | MP-CO-01 à MP-CO-05 |
| N8 | Zone de réponse séparée de la consigne et suffisante : au moins deux lignes pour une phrase produite ; environ 6-8 cm pour une réponse courte ; environ 10-14 cm pour une phrase complète. | MP-E-04 à MP-E-07 |
| N9 | Au maximum 3-5 exercices courts ou 1-2 exercices longs par page ; au maximum quatre éléments principaux visibles simultanément par exercice ; espaces blancs préservés. | MP-O-04, MP-O-05, MP-CI-02 |
| N10 | Jamais de saut de page entre une consigne et son exercice, entre une image et sa tâche, ni au milieu d'un tableau ou d'une activité. | MP-O-06 |
| N11 | Image seulement si elle est utile à la tâche ou à la compréhension d'un mot ; placée au-dessus ou à gauche de la tâche ; lisible en noir et blanc. | MP-I-01 à MP-I-03 |
| N12 | La couleur n'est jamais l'unique porteur d'information ; contraste noir sur blanc ; éviter les combinaisons rouge/vert et rouge/bleu. | MP-C-01 à MP-C-04 |
| N13 | Aides placées au plus près des actions ; exemple résolu pour toute tâche nouvelle ; pré-training (≤ ¼ de page) seulement si la notion est nouvelle, fragile, réactivée ou combinée. | MP-CC-04, MP-CC-06, MP-PT |
| N14 | Un même rôle (consigne, données, réponse, aide, exemple) conserve toujours le même format visuel. | MP-O-09 |
| N15 | Livrer la fiche élève et une partie enseignant·e séparée (corrigé expliqué, barème, différenciation), puis contrôler avec la grille de relecture courte (Étape 5) avant livraison. | Étape 5 |
| N16 | Établir la fiche technique et le budget de page (≤ 22 cm par page) **avant** de rédiger ; réduire le contenu, jamais les dimensions ; aucune page élève remplie partiellement : aérer, compléter ou passer en planche A5. | Étape 2, MP-O-11, MP-O-14 |
| N17 | Construire les lignes d'écriture avec R1 (tableau à hauteur exacte ou tabulation à points de suite) ; jamais de tirets bas pour une phrase, jamais de paragraphes bordés consécutifs. | Étape 4, MP-E-10 |
| N18 | Contrôler le rendu imprimé (PDF ou aperçu) avant de livrer, ou déclarer que ce contrôle n'a pas pu être fait. | Étape 5, MP-V-01 |
| N19 | En-tête dans cet ordre : Prénom et Date tout en haut, titre centré avec un espace avant et après, objectif en langage élève (la phrase seule, sans étiquette). | R7, MP-O-12 |
| N20 | Ne jamais montrer à l'élève une forme écrite fautive ou inexistante, y compris dans une phrase à corriger, un distracteur ou un exemple. | § 3.7, MP-CC-11 |
| N21 | Pour un jeu imprimé : une seule pièce correcte par question dans le lot, aucun indice non visé, ordre d'impression mélangé, autocorrection intégrée ; vérifier l'unicité et la fermeture (V11) et le rendu des planches (V12). | § 3.8, MP-J, R8 |

## Règles détaillées
<!-- modules : fiches, jeux -->

### MP-P — Principes de conception

| Id | Règle | Niveau |
|---|---|---|
| MP-P-01 | Concevoir le document à partir des besoins, des connaissances et des capacités des élèves visés. | DOIT |
| MP-P-02 | La mise en page facilite la tâche ; elle ne doit pas devenir une difficulté supplémentaire. Une mise en page cohérente réduit la charge cognitive inutile ; des repères visuels stables favorisent l'autonomie ; une bonne lisibilité réduit la fatigue de lecture et les erreurs. | DOIT |
| MP-P-03 | La disposition rend les actions évidentes ; la cohérence visuelle permet d'identifier rapidement ce qu'il faut faire et le rôle de chaque élément. | DOIT |
| MP-P-04 | Adapter l'interface (vocabulaire, syntaxe, structure, densité) au public cible. | DOIT |
| MP-P-05 | Penser la ressource selon son contexte d'usage : lieu (classe, domicile), moment, modalité (autonomie, guidée, devoir, remédiation), matériel disponible, temps et contraintes. | DOIT |
| MP-P-06 | Correspondance tâche–objectif : identifier si l'activité vise surtout à comprendre, agir ou explorer. Le format d'exercice découle de ce choix. | DOIT |
| MP-P-07 | Préférer des structures simples et familières à des organisations originales mais complexes. | DEVRAIT |
| MP-P-08 | Révision après usage : les supports sont testés et ajustés selon les retours. | DEVRAIT |

### MP-F — Format physique et impression

| Id | Règle | Niveau |
|---|---|---|
| MP-F-01 | Format A4. | DOIT |
| MP-F-02 | Orientation portrait par défaut. Le paysage PEUT être utilisé lorsque la tâche l'exige : tableaux larges, frises, cartes, zones de tracé étendues, lignes d'écriture « trottoirs ». | DOIT / PEUT |
| MP-F-03 | Marges de 2,5 cm sur chaque côté. | DOIT |
| MP-F-04 | Aucune information essentielle près des bords. | DOIT |
| MP-F-05 | Vérifier la cohérence du format et de l'orientation avec la tâche. | DOIT |
| MP-F-06 | **Largeur utile** : 16 cm en portrait (21 − 2 × 2,5), 24,7 cm en paysage (29,7 − 2 × 2,5). Aucune ligne d'écriture, aucun tableau ne dépasse cette largeur. | DOIT |

### MP-T — Typographie et hiérarchie visuelle

| Id | Règle | Niveau |
|---|---|---|
| MP-T-01 | Une police (idéal), deux au maximum ; au-delà de trois, la lisibilité diminue fortement. | DOIT |
| MP-T-02 | Lecteurs novices : police sans empattement (Arial, Verdana, Tahoma, Calibri) ou police scolaire locale. Lecteurs experts : police avec empattement possible. | DOIT / PEUT |
| MP-T-03 | Pas de texte entièrement en MAJUSCULES ; les capitales servent uniquement à attirer ponctuellement l'attention. | DOIT |
| MP-T-04 | Pas de soulignement ni d'italique excessifs. | DOIT |
| MP-T-05 | Pas d'effets décoratifs (ombres, reliefs, contours, ombrages) : incompatibles avec la photocopie. | DOIT |
| MP-T-06 | Hiérarchie d'accentuation, du plus discret au plus marqué : petites capitales → italique → capitales → gras → taille supérieure → autre police. Utiliser le niveau le plus faible suffisant. | DEVRAIT |
| MP-T-07 | Alignement à gauche pour les textes et consignes ; **pas de texte justifié** ; centrage réservé aux titres courts ou éléments isolés. | DOIT |

**Tailles de caractères par degré** (reprises dans la table 2.1)

| Degré | Taille du texte lu par l'élève |
|---|---|
| 1P-2P | 24 pt |
| 3P-4P | 18 pt |
| 5P-6P | 14 pt |
| 7P-8P | 12 pt |

Une réduction progressive est possible au cours du cycle.

### MP-E — Interlignes et zones d'écriture

| Id | Règle | Niveau |
|---|---|---|
| MP-E-01 | Interligne de lecture : 1,5. | DOIT |
| MP-E-02 | Interligne d'écriture : 2,0 minimum, ou lignes calibrées. | DOIT |
| MP-E-03 | Lignes d'écriture primaire calibrées à environ 8-10 mm. | DEVRAIT |
| MP-E-04 | Ne jamais coller la consigne et la zone de réponse. | DOIT |
| MP-E-05 | Au moins deux lignes pour une phrase produite. | DOIT |
| MP-E-06 | Espaces suffisants pour éviter une écriture compressée. | DOIT |
| MP-E-07 | Repères : réponse courte ≈ 6-8 cm ; phrase complète ≈ 10-14 cm ; production longue : 5-6 lignes sur la largeur utile. | DEVRAIT |
| MP-E-08 | Apprentissage du geste d'écriture : des « trottoirs » (trois lignes, dont une ligne principale) sur feuille en paysage permettent de travailler l'espacement entre les mots. La ligne principale DOIT rester identifiable sans couleur (épaisseur, trait). | PEUT |
| MP-E-09 | Pas de zone d'écriture pour les tâches sans production écrite (entourer, souligner, relier, cocher, colorier) : prévoir seulement l'espace nécessaire au geste. | DEVRAIT |

#### Table de dimensionnement des zones de réponse

| Réponse attendue | Zone |
|---|---|
| Un mot, un nombre | 1 ligne de 6-8 cm |
| Une phrase (production ou transformation) | au moins 2 lignes ; longueur 10-14 cm, au maximum la largeur utile (16 cm) |
| Production courte (mini-récit, description) | 5-6 lignes pleine largeur utile |
| Tableau à compléter | cellules d'au moins 5-6 cm de large et ≥ 1 cm de haut |
| Geste sans écriture | aucune ligne ; espace blanc autour des items |

### MP-O — Organisation et densité de page

| Id | Règle | Niveau |
|---|---|---|
| MP-O-01 | Structure stable : numéro → consigne → données → zone de réponse ; identique dans toute la fiche. | DOIT |
| MP-O-02 | Numérotation stable (1, 2, 3… ou A, B, C…) ; ne pas mélanger plusieurs systèmes à un même niveau. Usage courant : exercices 1, 2, 3 et items a), b), c). | DOIT |
| MP-O-03 | Zone d'identification **tout en haut de la page**, en première ligne : Prénom (ou Nom, selon la préférence de l'enseignant·e) et Date ; puis titre centré, puis objectif en langage élève, sans étiquette (MP-O-12, R7). **Exception pour les jeunes élèves** (1P-2P, et tout élève qui n'écrit pas encore sur une ligne) : aucune ligne « Prénom » ni « Date » ; ces élèves apprennent à écrire leur prénom, en grand, et ne peuvent pas le loger sur une ligne. À la place, la mention « Prénom au dos de la feuille » (l'élève l'écrit en grand au dos, ou y colle son étiquette-prénom) ; la date est notée par l'adulte. Recettes : `entete(..., jeunes=True)` pour Word, `definir_jeunes(True)` pour les fiches dessinées. En 3P-4P, demander à l'enseignant·e s'il faut garder la ligne. | DOIT |
| MP-O-04 | Au maximum 3-5 exercices courts par page, ou 1-2 exercices longs. | DOIT |
| MP-O-05 | Maintenir des espaces de respiration visuelle ; éviter la surcharge. | DOIT |
| MP-O-06 | Ne jamais séparer une consigne et son exercice par un saut de page ; ne jamais couper un tableau ou une activité entre deux pages. | DOIT |
| MP-O-07 | Réduire le nombre d'étapes entre la consigne et l'action. | DOIT |
| MP-O-08 | Blocs d'information clairement séparés ; rôles identifiables : consigne, données, réponse, aide, exemple. | DOIT |
| MP-O-09 | Homogénéité visuelle : un même rôle conserve le même format visuel dans tout le document. | DOIT |
| MP-O-10 | Limiter le nombre d'éléments simultanément visibles. | DOIT |

### MP-I — Images et schémas

| Id | Règle | Niveau |
|---|---|---|
| MP-I-01 | Image uniquement si elle est utile à la tâche ou à la compréhension d'un mot ; supprimer toute image ou décoration inutile. | DOIT |
| MP-I-02 | Placer l'image près de la tâche correspondante, au-dessus ou à gauche ; ne jamais séparer image et tâche par un saut de page. | DOIT |
| MP-I-03 | Lisibilité en noir et blanc et compatibilité photocopie ; éviter fonds gris, lignes fines, contrastes faibles. | DOIT |
| MP-I-04 | Utiliser des schémas ou représentations lorsque cela aide à comprendre, et seulement dans ce cas. | DEVRAIT |

### MP-C — Couleurs et contrastes

| Id | Règle | Niveau |
|---|---|---|
| MP-C-01 | Privilégier le contraste noir sur blanc ; garantir un contraste suffisant pour l'impression. | DOIT |
| MP-C-02 | La couleur n'est jamais l'unique porteur d'information ; l'information reste lisible sans couleur. | DOIT |
| MP-C-03 | Éviter les combinaisons vert/rouge et rouge/bleu, problématiques pour les élèves daltoniens. | DOIT |
| MP-C-04 | Si des couleurs sont utilisées : une même signification garde la même couleur dans tout le document. Pour un dessin R11, la couleur est une option (`definir_couleur`) : une seule teinte par document, qui remplace les gris par une teinte de même clarté ; les symboles de catégorie reçoivent chacun leur teinte, en plus de leur forme. | DOIT |
| MP-C-05 | Codage compatible daltonisme : forme + valeur de gris + couleur, par exemple ● plein / ◐ demi / ○ vide. | DEVRAIT |

### MP-CC — Charge cognitive et principes cognitifs

| Id | Règle | Niveau |
|---|---|---|
| MP-CC-01 | Ne conserver que les informations nécessaires à la tâche. | DOIT |
| MP-CC-02 | Mots concrets ; éviter les termes trop abstraits lorsque l'objectif est une action. | DEVRAIT |
| MP-CC-03 | Complexité syntaxique limitée : phrases courtes, peu de subordonnées. | DOIT |
| MP-CC-04 | Éviter l'attention divisée (*split attention*) : placer explications et aides au plus près des éléments concernés. L'élève ne doit pas chercher une information éloignée. | DOIT |
| MP-CC-05 | Informations multimodales complémentaires et non redondantes. | DEVRAIT |
| MP-CC-06 | Exemple résolu avant une production autonome lorsque la tâche est nouvelle. | DOIT |
| MP-CC-07 | Actions compréhensibles sans inférence ; lecture concise ; étapes réduites. | DOIT |
| MP-CC-08 | Conception simple, minimaliste et sans surcharge. | DOIT |
| MP-CC-09 | Lisibilité universelle : consignes courtes, vocabulaire adapté, hiérarchie visuelle claire. | DOIT |
| MP-CC-10 | Ne jamais pré-marquer (gras, italique, couleur) les éléments que l'élève doit lui-même repérer. | DOIT |

*Ancrage théorique :* théorie de la charge cognitive (Sweller et collègues), apprentissage multimédia (Mayer) : effets d'attention divisée, de redondance, d'exemple résolu, de pré-entraînement.

### MP-CO — Consignes

| Id | Règle | Niveau |
|---|---|---|
| MP-CO-01 | La consigne permet de comprendre immédiatement quoi faire ; une phrase courte suffit dans la majorité des cas. | DOIT |
| MP-CO-02 | Une seule action par phrase ; si plusieurs actions sont nécessaires, les présenter en étapes numérotées. | DOIT |
| MP-CO-03 | Pas de paragraphe de consigne : une consigne trop longue devient une tâche de lecture avant l'apprentissage. | DOIT |
| MP-CO-04 | Consigne directe, **sans titre d'exercice** qui la précède. | DOIT |
| MP-CO-05 | **Éviter la négation** (à proscrire : « Entoure les mots qui ne sont pas des verbes »). | DOIT |
| MP-CO-06 | Consigne placée au-dessus des données, et non à côté (lecture verticale). | DEVRAIT |
| MP-CO-07 | **Cohérence consigne ↔ format de réponse** : nombre de blancs, forme attendue, place disponible correspondent exactement à ce que la consigne demande. | DOIT |
| MP-CO-08 | Verbes de consigne stables d'une fiche à l'autre : souligne, entoure, encadre, relie, complète, coche, écris, classe, colorie, remets dans l'ordre. | DEVRAIT |

### MP-CI — Charge informationnelle par exercice

| Id | Règle | Niveau |
|---|---|---|
| MP-CI-01 | Un exercice ne présente pas trop d'informations simultanément. | DOIT |
| MP-CI-02 | Au maximum **quatre éléments principaux** visibles simultanément. « Élément principal » = bloc distinct (consigne, support ou données, aide, exemple, zone de réponse), et non nombre d'items. Items : 3-5 par défaut ; jusqu'à 6-10 items très courts et de structure identique pour l'automatisation (regrouper visuellement par blocs de 5). | DOIT |
| MP-CI-03 | En cas de surcharge, découper l'activité en étapes successives ; vérifier la lisibilité globale en un coup d'œil. | DOIT |

### MP-A — Aides intégrées et guidage

| Type d'activité | Aides à prévoir |
|---|---|
| **Comprendre** | Vocabulaire adapté ; définition des mots difficiles ; schémas ou représentations lorsque cela aide ; retour sur la compréhension ou la réussite. |
| **S'entraîner, répéter** | Consignes compréhensibles ; retour sur les erreurs ; exercices similaires pour stabiliser et consolider ; possibilité d'analyse d'erreur. |
| **Explorer** | But de la tâche explicite et maintenu visible ; indications pour éviter de se perdre ; repères de progression ; retours intermédiaires. |
| **Toutes** | Définitions nécessaires ; exemple résolu si la tâche est nouvelle ; feedback prévu ou auto-correction possible. |

### MP-PT — Pré-training

**Définition.** Rappel bref des éléments nécessaires avant l'activité. Il active des connaissances sans enseigner la notion complète ; il facilite l'autonomie en entrant dans la tâche sans surcharge liée à l'oubli de notions nécessaires.

#### Règle de décision

| Situation | Décision |
|---|---|
| Notion nouvelle, fragile, réactivée ou combinée | **Ajouter** un pré-training |
| Automatisation | Ne pas ajouter |
| Évaluation certificative | Ne pas ajouter |

#### Formats

| Format | Contenu | Usage |
|---|---|---|
| Minimal | Rappel court + un exemple simple | Cas courant |
| Guidé | Règle courte + deux exemples | Notion fragile |
| Renforcé | Plus développé | Réservé aux tâches complexes |

**Contraintes** : DOIT rester court et directement utile à l'exercice ; DOIT ne jamais dépasser **un quart de page** ; DEVRAIT être placé **avant** l'exercice concerné, au plus près de lui (MP-CC-04).

### Règles ajoutées dans les versions 6, 6.1, 6.2, 7 et 7.2 (et révision du 2.11.2026)

| Id | Règle | Niveau |
|---|---|---|
| MP-P-09 | Examiner l'adéquation de la demande à la progression PER du degré (notion, oral ou écrit, niveau d'attente) ; signaler l'écart et adapter sans refuser. | DOIT |
| MP-O-11 | Budget de page : au plus 22 cm de contenu planifié par page A4 portrait, en-tête compris ; calcul dans la fiche technique avant la rédaction. Exception : planche de pièces à découper (MP-J-11). | DOIT |
| MP-E-10 | Lignes d'écriture construites avec la recette R1 (tableau d'une colonne à hauteur exacte, bordure inférieure seule ; ou tabulation droite à points de suite). Interdits : tirets bas pour une réponse d'une phrase ou plus (X-01) ; paragraphes vides bordés consécutifs (X-02). | DOIT |
| MP-E-11 | Lacune dans une phrase : réservée à 1-2 mots ; nombre de tirets bas calculé selon la police et la taille (table 2.1). | DOIT |
| MP-C-06 | Symboles (☐, ★, ◐) : vérifier leur rendu ; préférer des mots dans des cellules et des cases dessinées (cellules vides bordées). | DEVRAIT |
| MP-S-01 | Un rôle, un style de paragraphe nommé (ou une mise en forme directe strictement identique). | DEVRAIT |
| MP-D-01 à MP-D-04 | Différenciation sans étiquette évaluative, dispositifs, budget par version, attribution (voir § 3.6). | DOIT / DEVRAIT |
| MP-V-01 | Contrôle sur le rendu imprimé (V1-V10 et V20 ; V11 à V19 selon le cas ; V21) avant livraison, ou déclaration « Rendu non contrôlé » avec la liste des contrôles. | DOIT |
| MP-V-02 | Rapport de conformité livré avec la fiche. | DOIT |
| MP-O-12 | En-tête obligatoire dans cet ordre : Prénom et Date tout en haut (première ligne) ; titre centré avec un espace avant et après (≥ 12 pt) ; objectif en langage élève (une phrase à la première personne, sans étiquette « Mon objectif : » ; révision du 2.11.2026). Recette R7. Jeunes élèves : pas de ligne Prénom et Date (MP-O-03). | DOIT |
| MP-I-05 | Image générée par IA destinée à l'élève : aucun texte produit par le générateur dans l'image (souvent fautif ou inexistant) ; le texte est ajouté dans le document, puis relu (V10). Ni logo, ni marque, ni personne réelle reconnaissable. | DOIT |
| MP-CC-11 | Par défaut, aucune forme écrite fautive ou inexistante dans un support destiné à l'élève (consignes, exemples, items, distracteurs, banques de mots, phrases à corriger) ; alternatives au § 3.7 ; exception encadrée, sur décision de l'enseignant·e, dès la 5P, pour une analyse d'erreurs (quatre conditions, § 3.7) ; relecture orthographique avant livraison (V10). | DOIT |
| MP-V-03 | Statut des informations : vérifié dans la session (avec la source) / non vérifié / inférence de conception. | DEVRAIT |
| MP-J-01 à MP-J-13 | Règles communes aux jeux imprimés : choix présenté avec le panorama des jeux (MP-J-13) ; surface de la planche et repères de coupe (MP-J-11, MP-J-12) ; unicité, aucun indice non visé, ordre mélangé, autocorrection, traits de coupe, aucun repère de niveau, règle en étapes avec exemple hors lot, carte-mémoire pour vérifier, en-tête, case d'accueil ≥ pièce mobile + 0,5 cm par côté (voir § 3.8). (v7 ; MP-J-10 : révision du 2.11.2026, suite) | DOIT / DEVRAIT |
| MP-F-07 | Format A3 admis pour les affiches lues à distance (TR17 à TR22) ; paramètres du § 2.5 ; dérogation explicite à MP-F-01. (v7.2) | PEUT |
| MP-T-08 | Toute police scolaire est déclarée, installée et vérifiée sur le rendu ; sinon, repli libre annoncé. (v7.2, constat T4 du balayage BDRP) | DOIT |
| MP-T-09 | TrueRomande n'est jamais utilisée pour du texte composé automatiquement ; l'écriture liée est composée en GE Typo Libre (R10). (v7.2) | DOIT |
| MP-T-10 | **Exemple en police d'élèves** : partout où un exemple est donné ou affiché (exemple résolu, exemple déjà fait en tête de fiche, exemple d'un rappel, d'une règle de jeu ou d'une affiche, colonne « Exemple » d'un tableau), l'exemple est composé dans la police d'élèves **GE Typo Libre** (R10), comme écrit à la main, pour que l'élève distingue ce qui est donné de ce qui est montré en exemple. Ce qui est donné reste dans la police de la fiche : consigne, règle, intitulé « Exemple », item de départ. Dans un exercice dont le premier item est fait, l'item reste comme les autres et seule la réponse (ce que l'élève écrit, à l'endroit où il l'écrit) passe en police d'élèves. Corps : même hauteur apparente que le texte de la fiche, soit 1,25 fois le corps pour des lettres (17,5 pt pour 14 pt), 0,9 fois pour des chiffres seuls et 1,1 fois pour un mélange de lettres et de chiffres, un seul corps par exemple (`taille_eleve`) ; ni gras ni italique ; un léger retrait au début d'une cellule, la police ayant des attaques qui débordent à gauche. Caractère absent de la police (Â, Ä, Î, Ï, Ö, Ù, Û, Ü, Ÿ, ä, ÿ, æ, –, %, point médian) : le mot reste en script (`ecrire_exemple` le fait seul). Police non installée : repli annoncé (MP-T-08), l'exemple reste en italique. Ne s'applique pas aux données d'un jeu (texte des cartes, des dominos, des plateaux) ni au contenu d'un modèle rempli à adapter. Recettes : `ecrire_exemple`, option `{'eleve': taille}` d'`ecrire`, police `'Eleve'` de `Dessin` (`police_exemple_pdf`). (21.11.2026) | Convention (priorité 5) : appliquée par défaut |
| MP-P-10 | L'IA travaille avec des prénoms fictifs ou des marqueurs ; les prénoms réels sont insérés localement par l'enseignant·e (nLPD). (v7.2, constat T6 du balayage BDRP) | DOIT |
| MP-O-13 | Rubrique « Conditionnement » dans la fiche technique de toute ressource imprimée autre qu'une fiche à photocopier (§ 2.3). (v7.2) | DEVRAIT |
| MP-O-14 | Page pleine : aucune page élève remplie partiellement ; sur le rendu, chaque page atteint au moins 90 % du budget de hauteur (mesure sur l'image de la page) ; sinon aérer, compléter (lignes, items) ou passer en planche A5 (R15). Exceptions déclarées : partie enseignant·e, dernière planche d'un jeu à nombre de pièces fixé. Contrôle V20. (révision du 2.11.2026) | DOIT |

# ANNEXE I-B — GRILLE DE RELECTURE DÉTAILLÉE
<!-- modules : verification -->

À utiliser pour auditer une fiche existante ou pour transformer une fiche d'une autre source. Chaque écart est référencé par son code ; le relevé est présenté du plus grave au plus mineur, en commençant par les écarts aux règles DOIT.

## Grille détaillée (évaluation ou transformation d'une fiche existante)

À utiliser pour auditer une fiche existante (prompt G) ou transformer une fiche d'une autre source (prompt B). Chaque écart constaté est référencé par son identifiant.

#### Rendu imprimé (à faire en premier, sur le PDF)
- Contrôle visuel V1-V10 (§ 5.2) : pages, coupures, nombre réel de lignes, longueur des lacunes, tailles, symboles, bords, absence de la partie enseignant·e, ordre de l'en-tête, orthographe.
- Budget de page de la fiche technique cohérent avec le rendu (MP-O-11) ; aucune page élève remplie partiellement (MP-O-14, V20).
- Cohérence didactique : graphème présent dans chaque mot, réponses d'énigme calculées, cases de réussite vides, zone de réponse pour chaque question, partie enseignant·e des jeux et des dictées (V21).
- Fichier produit par du code : validation au schéma OOXML (V14).

#### Jeux imprimés (si la ressource est un jeu)
- Unicité de chaque réponse dans le lot et fermeture de la boucle, ou complétude des paires et des familles (V11, MP-J-01, X-15).
- Aucun indice non visé : radical, longueur, position, ordre d'impression (MP-J-02, MP-J-03, X-16).
- Pièces aux dimensions prévues, non coupées ; traits de coupe en pointillés, séparations internes en trait plein épais (V12, MP-J-05) ; chaque case d'accueil dépasse la pièce mobile d'au moins 0,5 cm par côté (MP-J-10) ; planche qui occupe toute la page, repères de coupe au bord de la feuille (MP-J-11, MP-J-12).
- Recto-verso aligné sur une impression test (V13).
- Règle en étapes avec un exemple hors lot ; carte-mémoire pour vérifier ; aucun repère de niveau (MP-J-06 à MP-J-08).
- Modalité adaptée à la notion : pas de jeu uniquement oral pour une notion orthographique (X-17).

#### Contexte et adéquation
- Public cible identifié ; vocabulaire, syntaxe, structure et densité adaptés (MP-P-04).
- Contexte d'usage pris en compte ; durée estimée réaliste (MP-P-05).
- Type d'objectif (comprendre, agir, explorer) et format d'exercice cohérents (MP-P-06).
- Terminologie suisse respectée (1P-8P et 9S-11S, cycles 1 à 3, disciplines romandes).
- Adéquation de la demande à la progression PER examinée et signalée (MP-P-09).
- En-tête : Prénom et Date en première ligne, titre centré entre deux espaces, objectif en langage élève sans étiquette (MP-O-12).
- Aucune forme écrite fautive ou inexistante dans tout le texte élève, y compris exemples, distracteurs et phrases de jugement (MP-CC-11).
- Aucune activité ne demande aux élèves d'utiliser un outil d'IA.

#### Format et impression
- A4 ; orientation cohérente avec la tâche ; marges de 2,5 cm ; largeur utile respectée (MP-F-01 à MP-F-06).
- Compatibilité photocopie : pas de fond gris, pas de trait fin, pas d'ombre, pas de contraste faible (MP-I-03, MP-T-05).
- Contrastes suffisants pour l'impression (MP-C-01).

#### Typographie
- Nombre de polices (signaler tout excès au-delà de deux) (MP-T-01).
- Police adaptée au lecteur (MP-T-02) ; taille conforme au degré.
- Majuscules, soulignement, italique : usage ponctuel (MP-T-03, MP-T-04).
- Accentuations simultanées limitées, hiérarchie respectée (MP-T-06).
- Cohérence typographique d'ensemble.

#### Organisation et densité
- Structure stable et continuité logique entre exercices (MP-O-01).
- Numérotation : un système par niveau (MP-O-02) ; zone d'identification selon la préférence (MP-O-03).
- Nombre d'exercices par page ; espaces blancs ; absence de surcharge (MP-O-04, MP-O-05).
- Aucune coupure de consigne, d'exercice, de tableau ou d'activité entre deux pages (MP-O-06).
- Nombre d'étapes entre consigne et action réduit (MP-O-07).
- Rôles identifiables ; même rôle, même format (MP-O-08, MP-O-09).

#### Consignes et charge cognitive
- Consignes directes, courtes, concrètes, sans négation, une action par phrase (MP-CO-01 à MP-CO-05, MP-CC-02).
- Cohérence consigne ↔ format de réponse (MP-CO-07).
- Informations strictement nécessaires ; pas de redondance inutile (MP-CC-01, MP-CC-05).
- **Aucun pré-marquage** des éléments à repérer (MP-CC-10).
- Aides et explications au plus près des actions (MP-CC-04).
- Exemple résolu pour toute tâche nouvelle (MP-CC-06).
- Lisibilité globale en un coup d'œil ; au plus 4 éléments principaux par exercice (MP-CI-02, MP-CI-03).

#### Zones de réponse
- Présentes pour toute production écrite, séparées de la consigne, suffisantes (MP-E-04 à MP-E-07).
- Construites avec R1 ; aucune ligne en tirets bas pour une phrase ; aucune ligne fusionnée (MP-E-10, X-01, X-02).
- Absentes pour les tâches sans écriture (MP-E-09).
- Interlignes et hauteur de ligne conformes (MP-E-01 à MP-E-03).

#### Images et couleurs
- Pertinence de chaque image ; lien direct image–tâche ; placement au-dessus ou à gauche (MP-I-01, MP-I-02).
- Lisibilité sans couleur ; pas de rouge/vert ni de rouge/bleu ; codes couleur constants (MP-C-02 à MP-C-04).
- Pas d'émoji ni de symbole coloré dans la fiche élève.

#### Aides et guidage
- Définitions des mots difficiles ; feedback ou auto-correction prévus (MP-A).
- Pour l'exploration : but visible, repères de progression, retours intermédiaires (MP-A).
- Pré-training : décision conforme, format adapté, au plus ¼ de page, placé avant l'exercice (MP-PT).

#### Partie enseignant·e
- Corrigé exact, avec explication brève par exercice.
- Barème cohérent (total vérifié par addition).
- Différenciation soutien / défi ; erreurs typiques de la notion ciblées.
- Prolongements numériques facultatifs, sans outil retiré ni non vérifié présenté comme autorisé.

#### Révision
- Proposition de révision après usage (MP-P-08) ; conformité globale au référentiel.

#### Format du relevé d'écarts

| Réf. règle | Constat (localisé : exercice, ligne) | Niveau : DOIT ou DEVRAIT | Correction proposée |
|---|---|---|---|

Le relevé est présenté **du plus grave au plus mineur**, en commençant par les écarts aux règles DOIT, puis DEVRAIT.

# ANNEXE I-C — MODULE PYTHON-DOCX DES RECETTES R1 À R15 (ET CONTRÔLES V11 À V21)
<!-- modules : code -->

Pour les IA qui produisent le fichier .docx par du code. La v7 remplace le module de la v6 par le module « recettes R1-R6 corrigées », issu du test du 30.10.2026, complété par R3, R5, R6, R7 (en-tête), R8 (planche de pièces), les styles nommés et deux outils pour les jeux.

#### Ce que corrige le module (v7)

- **Ordre XML conforme au schéma** : `geometrie` remplace l'élément `w:tblW` existant au lieu d'en ajouter un second après `w:tblLook`, et range chaque élément de `w:tblPr` dans l'ordre du schéma ; `bordures` place `w:tcBorders` avant `w:shd` et `w:vAlign`. Le module de la v6 produisait ces deux erreurs ; le validateur OOXML les signale (contrôle refait dans cette version sur un fichier témoin).
- **Correctif `w:zoom`** : le gabarit de python-docx omet l'attribut obligatoire `w:percent` ; `page_a4` l'ajoute (valeur 100).
- **Traits d'union insécables** dans « -er », « -ir », « -iss- » (élément `w:noBreakHyphen`) et **espace insécable** dans « en -ir » : `ecrire` les applique, pour que la fin de ligne ne coupe pas « en - » / « ir ».
- **Tabulations conservées** : `ecrire` transforme chaque tabulation en élément `w:tab` (une tabulation passée à `add_text` est perdue).
- **Tabulation R1b** : la position se mesure depuis la marge, pas depuis le retrait.

**Test (v7)** : un document de cinq pages couvrant R1 à R8 (en-tête, encadré, lacunes, amorce et lignes, tableau, bilan, règle du jeu en étapes, exemple de deux dominos hors lot, carte-mémoire, deux planches de 2 × 8 dominos) a été généré, converti en PDF avec LibreOffice, regardé page par page et validé au schéma OOXML sans erreur. Mesures sur le rendu : lacune de 22 tirets bas = 6,04 cm ; rangées de dominos de 2,50 cm ; planche de 16,0 cm de large et 20,7 cm de haut ; « en -ir » non coupé. Le rendu dans Word n'a pas été contrôlé ; le contrôle de l'Étape 5 reste obligatoire.

```
"""Recettes R1 à R8 du Livre I (Annexe I-C), version 7.
Base : module « recettes R1-R6 corrigées » (ordre XML conforme au schéma, traits d'union et espaces
insécables, correctif w:zoom, tabulations conservées), complété par R3, R5, R6, R7 (en-tête),
R8 (planche de pièces à découper), les styles nommés et deux outils pour les jeux."""
from docx import Document
from docx.shared import Pt, Cm
import random
from docx.enum.text import WD_LINE_SPACING, WD_TAB_ALIGNMENT, WD_TAB_LEADER, WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.enum.table import WD_ROW_HEIGHT_RULE, WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

LARGEUR_UTILE_CM = 16.0
TW = lambda cm: str(int(round(cm / 2.54 * 1440)))

def page_a4(doc, police='Arial', taille=14, interligne=1.5):
    for s in doc.sections:
        s.page_width, s.page_height = Cm(21), Cm(29.7)
        s.top_margin = s.bottom_margin = s.left_margin = s.right_margin = Cm(2.5)
        s.header_distance = s.footer_distance = Cm(1.25)
    st = doc.styles['Normal']
    st.font.name = police; st.font.size = Pt(taille)
    rpr = st.element.get_or_add_rPr()
    rpr.rFonts.set(qn('w:eastAsia'), police); rpr.rFonts.set(qn('w:hAnsi'), police); rpr.rFonts.set(qn('w:cs'), police)
    lang = OxmlElement('w:lang'); lang.set(qn('w:val'), 'fr-CH'); rpr.append(lang)
    pf = st.paragraph_format
    pf.line_spacing = interligne; pf.space_after = Pt(4); pf.space_before = Pt(0)
    pf.alignment = WD_ALIGN_PARAGRAPH.LEFT
    z = doc.settings.element.find(qn('w:zoom'))
    if z is not None and z.get(qn('w:percent')) is None:
        z.set(qn('w:percent'), '100')          # attribut requis par le schéma (gabarit python-docx)
    cp = doc.core_properties
    cp.author = ''; cp.last_modified_by = ''; cp.comments = ''; cp.keywords = ''

def style_para(doc, nom, taille, gras=False, italique=False, interligne=1.5, avant=0, apres=4,
               retrait=0.0, suspendu=0.0, centre=False, exact_pt=None):
    st = doc.styles.add_style(nom, WD_STYLE_TYPE.PARAGRAPH)
    st.base_style = doc.styles['Normal']
    st.quick_style = True
    st.font.size = Pt(taille); st.font.bold = gras; st.font.italic = italique
    pf = st.paragraph_format
    if exact_pt:
        pf.line_spacing_rule = WD_LINE_SPACING.EXACTLY; pf.line_spacing = Pt(exact_pt)
    else:
        pf.line_spacing = interligne
    pf.space_before = Pt(avant); pf.space_after = Pt(apres)
    pf.left_indent = Cm(retrait); pf.first_line_indent = Cm(-suspendu) if suspendu else Cm(0)
    pf.alignment = WD_ALIGN_PARAGRAPH.CENTER if centre else WD_ALIGN_PARAGRAPH.LEFT
    pf.widow_control = True
    return st

def solidariser(p, avec_suivant=True):
    """R4 : paragraphe solidaire du suivant (dans un exercice uniquement) et lignes solidaires."""
    p.paragraph_format.keep_with_next = avec_suivant
    p.paragraph_format.keep_together = True
    return p

def saut_de_page(doc):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(0); p.paragraph_format.line_spacing = 1.0
    p.add_run().add_break(WD_BREAK.PAGE)
    return p

def ecrire(p, contenu):
    """contenu = str ou liste de segments (texte, {b, i, eleve}). {'eleve': taille} : segment d'exemple en police
    d'élèves, au corps taille_eleve(taille, texte) (MP-T-10, R10)."""
    if isinstance(contenu, str):
        contenu = [(contenu, {})]
    for seg in contenu:
        if isinstance(seg, str):
            seg = (seg, {})
        txt, o = seg
        r = p.add_run()
        txt = txt.replace(' -', ' -')          # « en -ir » ne se coupe pas en fin de ligne
        for t, tabs in enumerate(txt.split('\t')):
            if t:
                r._r.append(OxmlElement('w:tab'))
            for k, m in enumerate(tabs.split('-')):
                if k:
                    r._r.append(OxmlElement('w:noBreakHyphen'))   # trait d'union insécable (« -er », « -iss- »)
                if m:
                    r.add_text(m)
        if 'b' in o: r.bold = o['b']
        if 'i' in o: r.italic = o['i']
        if o.get('eleve'):                                                  # MP-T-10 : exemple en police d'élèves
            r.font.name = POLICE_CURSIVE; r.font.size = Pt(taille_eleve(o['eleve'], txt))
            rf = r._r.get_or_add_rPr().rFonts
            for a in ('w:ascii', 'w:hAnsi', 'w:cs', 'w:eastAsia'): rf.set(qn(a), POLICE_CURSIVE)
    return p

# ---------- géométrie des tableaux (ordre XML conforme) ----------
_TBLPR_ORDRE = ['tblStyle', 'tblpPr', 'tblOverlap', 'bidiVisual', 'tblStyleRowBandSize', 'tblStyleColBandSize',
                'tblW', 'jc', 'tblCellSpacing', 'tblInd', 'tblBorders', 'shd', 'tblLayout', 'tblCellMar',
                'tblLook', 'tblCaption', 'tblDescription']

def _tblpr_set(tblPr, tag, el):
    old = tblPr.find(qn('w:' + tag))
    if old is not None:
        tblPr.remove(old)
    idx = _TBLPR_ORDRE.index(tag)
    for child in list(tblPr):
        name = child.tag.split('}')[1]
        if name in _TBLPR_ORDRE and _TBLPR_ORDRE.index(name) > idx:
            child.addprevious(el)
            return
    tblPr.append(el)

def geometrie(table, largeurs_cm, retrait_cm=0.0, marge_cell_cm=0.15):
    table.alignment = WD_TABLE_ALIGNMENT.LEFT
    table.autofit = False
    tblPr = table._tbl.tblPr
    w = OxmlElement('w:tblW'); w.set(qn('w:w'), TW(sum(largeurs_cm))); w.set(qn('w:type'), 'dxa')
    _tblpr_set(tblPr, 'tblW', w)
    ind = OxmlElement('w:tblInd'); ind.set(qn('w:w'), TW(retrait_cm)); ind.set(qn('w:type'), 'dxa')
    _tblpr_set(tblPr, 'tblInd', ind)
    mar = OxmlElement('w:tblCellMar')
    for edge, v in (('top', 0.0), ('left', marge_cell_cm), ('bottom', 0.0), ('right', marge_cell_cm)):
        e = OxmlElement(f'w:{edge}'); e.set(qn('w:w'), TW(v)); e.set(qn('w:type'), 'dxa'); mar.append(e)
    _tblpr_set(tblPr, 'tblCellMar', mar)
    grid = table._tbl.tblGrid
    for gc in list(grid):
        grid.remove(gc)
    for x in largeurs_cm:
        gc = OxmlElement('w:gridCol'); gc.set(qn('w:w'), TW(x)); grid.append(gc)
    for row in table.rows:
        for j, c in enumerate(row.cells):
            c.width = Cm(largeurs_cm[j])

def bordures(cell, top=None, left=None, bottom=None, right=None):
    """Chaque bord : None (aucun) ou (val, sz en 1/8 pt). val : single, dashed, dotted…"""
    tcPr = cell._tc.get_or_add_tcPr()
    old = tcPr.find(qn('w:tcBorders'))
    if old is not None:
        tcPr.remove(old)
    b = OxmlElement('w:tcBorders')
    for edge, spec in (('top', top), ('left', left), ('bottom', bottom), ('right', right)):
        e = OxmlElement(f'w:{edge}')
        if spec:
            e.set(qn('w:val'), spec[0]); e.set(qn('w:sz'), str(spec[1])); e.set(qn('w:space'), '0')
            e.set(qn('w:color'), spec[2] if len(spec) > 2 else '000000')
        else:
            e.set(qn('w:val'), 'nil')
        b.append(e)
    # tcBorders se place après tcW / gridSpan / vMerge et avant shd / vAlign
    va = tcPr.find(qn('w:vAlign')); shd = tcPr.find(qn('w:shd'))
    anchor = shd if shd is not None else va
    if anchor is not None:
        anchor.addprevious(b)
    else:
        tcPr.append(b)

def trame(cell, couleur='F2F2F2'):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd'); shd.set(qn('w:val'), 'clear'); shd.set(qn('w:color'), 'auto'); shd.set(qn('w:fill'), couleur)
    va = tcPr.find(qn('w:vAlign'))
    if va is not None:
        va.addprevious(shd)
    else:
        tcPr.append(shd)

def ligne_tableau(row, hauteur_cm, exacte=False, entete=False):
    trPr = row._tr.get_or_add_trPr()
    trPr.append(OxmlElement('w:cantSplit'))                      # ligne insécable (R3, R4)
    row.height = Cm(hauteur_cm)
    row.height_rule = WD_ROW_HEIGHT_RULE.EXACTLY if exacte else WD_ROW_HEIGHT_RULE.AT_LEAST
    if entete:
        trPr.append(OxmlElement('w:tblHeader'))

def solidariser_tableau(table, dernier_avec_suivant=False):
    """R4 appliquée aux tableaux : chaque ligne reste avec la suivante (pas de coupure)."""
    rows = table.rows
    for i, row in enumerate(rows):
        for c in row.cells:
            for p in c.paragraphs:
                solidariser(p, avec_suivant=(i < len(rows) - 1) or dernier_avec_suivant)

# ---------- R1 : lignes d'écriture ----------
def lignes_ecriture(doc, n, hauteur_cm=1.0, largeur_cm=LARGEUR_UTILE_CM, retrait_cm=0.0):
    """R1a : tableau d'une colonne, hauteur EXACTE, bordure inférieure seule."""
    t = doc.add_table(rows=n, cols=1)
    geometrie(t, [largeur_cm], retrait_cm)
    for row in t.rows:
        ligne_tableau(row, hauteur_cm, exacte=True)
        c = row.cells[0]
        bordures(c, bottom=('single', 6, '404040'))
        c.vertical_alignment = WD_ALIGN_VERTICAL.BOTTOM
        c.paragraphs[0].paragraph_format.space_after = Pt(0)
    solidariser_tableau(t)
    return t

def ligne_tabulation(doc, debut, style, largeur_cm=LARGEUR_UTILE_CM, retrait_cm=0.0, hauteur_pt=28):
    """R1b : amorce + tabulation droite à points de suite « ___ » jusqu'à la marge."""
    p = doc.add_paragraph(style=style)
    pf = p.paragraph_format
    pf.line_spacing_rule = WD_LINE_SPACING.EXACTLY; pf.line_spacing = Pt(hauteur_pt)
    pf.space_after = Pt(0); pf.space_before = Pt(4)
    pf.left_indent = Cm(retrait_cm); pf.first_line_indent = Cm(0)
    pf.tab_stops.add_tab_stop(Cm(largeur_cm), WD_TAB_ALIGNMENT.RIGHT, WD_TAB_LEADER.LINES)  # mesurée depuis la marge
    p.add_run(debut + '\t')
    solidariser(p)
    return p

# ---------- R2 : lacune ----------
def lacune(longueur_cm, police='Arial', taille=14):
    largeur_tiret = {('Arial', 12): 0.235, ('Arial', 14): 0.275, ('Arial', 18): 0.353, ('Arial', 24): 0.471,
                     ('Calibri', 12): 0.211, ('Calibri', 14): 0.246, ('Calibri', 18): 0.316, ('Calibri', 24): 0.422}
    return '_' * round(longueur_cm / largeur_tiret[(police, taille)])

# ---------- styles nommés (§ 4.1, MP-S-01) ----------
def styles_fiche(doc, taille=14):
    """Crée les styles du § 4.1 pour la taille du degré (table 2.1)."""
    style_para(doc, 'Fiche-Identité', taille, avant=0, apres=0)
    style_para(doc, 'Fiche-Titre', taille + 4, gras=True, centre=True, avant=18, apres=18, interligne=1.15)
    style_para(doc, 'Fiche-Objectif', taille, apres=12)
    style_para(doc, 'Fiche-Consigne', taille, gras=True, avant=10, apres=4)
    style_para(doc, 'Fiche-Données', taille)
    style_para(doc, 'Fiche-Lacune', taille, interligne=2.0, apres=0)
    style_para(doc, 'Fiche-Exemple', taille)              # l'exemple lui-même en police d'élèves (MP-T-10)
    style_para(doc, 'Fiche-Aide', taille, interligne=1.15, apres=2)
    style_para(doc, 'Fiche-Bilan', taille, interligne=1.0, apres=0)
    style_para(doc, 'Fiche-Étape', taille, interligne=1.15, apres=4, retrait=0.8, suspendu=0.8)
    style_para(doc, 'Fiche-Pièce', taille, interligne=1.0, apres=0, centre=True)
    style_para(doc, 'Fiche-Mention', 11, italique=True, interligne=1.0, apres=6)
    style_para(doc, 'Ens-Titre', 13, gras=True, avant=10, apres=4, interligne=1.15)
    style_para(doc, 'Ens-Texte', 11, interligne=1.15)

def paragraphe(doc, contenu, style, lier=True):
    p = doc.add_paragraph(style=style)
    ecrire(p, contenu)
    return solidariser(p, lier)

def _cellule(cell, contenu, style, gras=False):
    p = cell.paragraphs[0]
    p.style = cell.part.document.styles[style]
    ecrire(p, contenu if not gras else [(contenu, {'b': True})] if isinstance(contenu, str) else contenu)
    return p

def espace(doc, pt=6):
    """R4 : paragraphe vide de hauteur exacte (6 pt) après un tableau, pour que la consigne suivante ne colle pas."""
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.line_spacing_rule = WD_LINE_SPACING.EXACTLY; pf.line_spacing = Pt(pt)
    pf.space_before = Pt(0); pf.space_after = Pt(0)
    return p

# ---------- R3 : tableau à compléter ----------
def tableau_a_completer(doc, entetes, lignes, largeurs_cm, hauteur_min_cm=1.0, style='Fiche-Bilan'):
    """R3 : largeurs fixées, lignes ≥ 1 cm (« au moins »), insécables, en-tête répété, bordures 0,75 pt."""
    t = doc.add_table(rows=1 + len(lignes), cols=len(entetes))
    geometrie(t, largeurs_cm)
    trait = ('single', 6, '595959')
    for i, row in enumerate(t.rows):
        ligne_tableau(row, hauteur_min_cm, exacte=False, entete=(i == 0))
        valeurs = entetes if i == 0 else lignes[i - 1]
        for j, c in enumerate(row.cells):
            bordures(c, top=trait, left=trait, bottom=trait, right=trait)
            c.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            _cellule(c, valeurs[j], style, gras=(i == 0))
    solidariser_tableau(t)
    return t

# ---------- R5 : encadré ----------
def encadre(doc, contenus, couleur='F2F2F2', style='Fiche-Aide'):
    """R5 : tableau 1 × 1 bordé, 16 cm, ligne insécable, trame très claire (jamais de bordure de paragraphe)."""
    t = doc.add_table(rows=1, cols=1)
    geometrie(t, [LARGEUR_UTILE_CM])
    row = t.rows[0]; ligne_tableau(row, 0.8)
    c = row.cells[0]
    trait = ('single', 6, '595959')
    bordures(c, top=trait, left=trait, bottom=trait, right=trait)
    if couleur:
        trame(c, couleur)
    _cellule(c, contenus[0], style)
    for contenu in contenus[1:]:
        p = c.add_paragraph(style=style); ecrire(p, contenu)
    solidariser_tableau(t)
    return t

# ---------- R6 : bilan en mots ----------
def cases_bilan(doc, criteres, choix=('je sais faire', 'presque', "j'ai besoin d'aide"),
                largeurs_cm=(7.0, 3.0, 3.0, 3.0), style='Fiche-Bilan'):
    """R6 : choix en MOTS dans des cellules à entourer (aucun glyphe fragile), lignes ≥ 1 cm."""
    t = doc.add_table(rows=len(criteres), cols=1 + len(choix))
    geometrie(t, list(largeurs_cm))
    trait = ('single', 6, '595959')
    for i, crit in enumerate(criteres):
        row = t.rows[i]; ligne_tableau(row, 1.0)
        for j, c in enumerate(row.cells):
            bordures(c, top=trait, left=trait, bottom=trait, right=trait)
            c.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            _cellule(c, crit if j == 0 else choix[j - 1], style)
    solidariser_tableau(t)
    return t

# ---------- R7 : en-tête de la fiche (MP-O-12) ----------
def entete(doc, titre, objectif, largeur_cm=LARGEUR_UTILE_CM, jeunes=False):
    """R7 : 1) Prénom et Date tout en haut (tabulations à points de suite, mesurées depuis la marge) ;
    2) titre centré, espace avant et après ; 3) objectif formulé pour l'élève : la phrase seule, sans étiquette
    (« J'écris un verbe au passé composé avec ses deux parties. »), majuscule initiale, point final.
    jeunes=True (1P-2P, élèves qui n'écrivent pas encore sur une ligne) : pas de ligne Prénom et Date, mais la
    mention « Prénom au dos de la feuille » (MP-O-03)."""
    p = doc.add_paragraph(style='Fiche-Identité')
    if jeunes: ecrire(p, 'Prénom au dos de la feuille')
    ts = p.paragraph_format.tab_stops
    ts.add_tab_stop(Cm(largeur_cm * 0.58), WD_TAB_ALIGNMENT.LEFT, WD_TAB_LEADER.LINES)
    ts.add_tab_stop(Cm(largeur_cm * 0.62), WD_TAB_ALIGNMENT.LEFT)
    ts.add_tab_stop(Cm(largeur_cm), WD_TAB_ALIGNMENT.RIGHT, WD_TAB_LEADER.LINES)
    if not jeunes: ecrire(p, 'Prénom : \t\tDate : \t')
    t = doc.add_paragraph(style='Fiche-Titre'); ecrire(t, titre)
    objectif = objectif.strip()
    for etiquette in ('Mon objectif\u00a0:', 'Mon objectif :', 'Mon objectif:', 'Objectif\u00a0:', 'Objectif :', 'Objectif:'):
        if objectif.startswith(etiquette):
            objectif = objectif[len(etiquette):].strip()
    objectif = objectif[:1].upper() + objectif[1:]
    if objectif[-1:] not in '.!?':
        objectif += '.'
    o = doc.add_paragraph(style='Fiche-Objectif'); ecrire(o, objectif)
    return p, t, o

# ---------- règle du jeu en étapes numérotées (MP-J-07) ----------
def etapes(doc, liste, style='Fiche-Étape'):
    """Une étape = une action ; numéro, tabulation, texte ; retrait suspendu de 0,8 cm."""
    ps = []
    for k, txt in enumerate(liste, 1):
        p = doc.add_paragraph(style=style)
        ecrire(p, f'{k}\t' + txt if isinstance(txt, str) else [f'{k}\t'] + list(txt))
        ps.append(solidariser(p, k < len(liste)))
    return ps

# ---------- R8 : planche de pièces à découper ----------
COUPE = ('dashed', 8, '000000')        # trait de coupe : pointillés, 1 pt
INTERNE = ('single', 18, '000000')     # séparation interne : trait plein épais, 2,25 pt

def planche_pieces(doc, pieces, par_rangee=2, largeurs_moities_cm=(4.0, 4.0), hauteur_cm=2.5,
                   mention=None, saut_avant=True, style='Fiche-Pièce'):
    """R8 : planche de pièces (dominos, cartes) à découper.
    pieces : liste de pièces ; une pièce = liste de moitiés ; une moitié = liste de lignes (str ou segments).
    Tableau à largeurs fixées, lignes à hauteur EXACTE et insécables, bordures définies cellule par cellule
    (pointillés = coupe ; trait plein épais = séparation interne), saut de page avant la planche."""
    if mention:
        m = doc.add_paragraph(style='Fiche-Mention'); ecrire(m, mention)
        m.paragraph_format.page_break_before = saut_avant
        solidariser(m)
    n_m = len(largeurs_moities_cm)
    rangees = [pieces[i:i + par_rangee] for i in range(0, len(pieces), par_rangee)]
    t = doc.add_table(rows=len(rangees), cols=par_rangee * n_m)
    geometrie(t, list(largeurs_moities_cm) * par_rangee, marge_cell_cm=0.1)
    if not mention and saut_avant:
        t.rows[0].cells[0].paragraphs[0].paragraph_format.page_break_before = True
    for r, rangee in enumerate(rangees):
        row = t.rows[r]; ligne_tableau(row, hauteur_cm, exacte=True)
        for k in range(par_rangee):
            piece = rangee[k] if k < len(rangee) else None
            for h in range(n_m):
                c = row.cells[k * n_m + h]
                c.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
                if piece is None:
                    bordures(c)
                    continue
                gauche = COUPE if h == 0 else INTERNE
                droite = COUPE if h == n_m - 1 else INTERNE
                bordures(c, top=COUPE, left=gauche, bottom=COUPE, right=droite)
                lignes = piece[h]
                p = c.paragraphs[0]; p.style = doc.styles[style]; ecrire(p, lignes[0])
                for ligne in lignes[1:]:
                    q = c.add_paragraph(style=style); ecrire(q, ligne)
    return t

# ---------- outils pour les jeux (V11, MP-J-03) ----------
def melanger_sans_voisins(pieces, graine=1, essais=10000):
    """Ordre d'impression mélangé : deux pièces voisines dans la boucle ne sont jamais voisines sur la planche."""
    rng = random.Random(graine); n = len(pieces)
    pos = {id(p): i for i, p in enumerate(pieces)}
    o = list(pieces)
    for _ in range(essais):
        rng.shuffle(o)
        if all(abs(pos[id(o[k])] - pos[id(o[k + 1])]) % n not in (1, n - 1) for k in range(n - 1)):
            return o
    raise RuntimeError('aucun ordre trouvé')

def verifier_domino_boucle(dominos, solution):
    """V11 : dominos = [(réponse, question)], dans l'ordre de la boucle ; solution(question) -> réponse.
    Vérifie : réponses toutes différentes ; chaque question a exactement une pièce-réponse ; la boucle se ferme."""
    reponses = [d[0] for d in dominos]
    assert len(set(reponses)) == len(reponses), 'deux pièces portent la même réponse'
    for rep, q in dominos:
        assert reponses.count(solution(q)) == 1, f'question sans réponse unique : {q}'
    par_rep = {d[0]: d for d in dominos}
    d = dominos[0]
    for _ in range(len(dominos)):
        d = par_rep[solution(d[1])]
    assert d == dominos[0], 'la boucle ne se ferme pas'
    return True
```

#### Extension v7.2 : recettes R9 à R14

Le module ci-dessus reste valable tel quel. La v7.2 lui ajoute, à la suite, les recettes R9 à R14. Le fichier `recettes_v7.2.py` réunit les deux blocs.

**Test (v7.2)** : 54 documents d'essai générés, convertis en PDF avec LibreOffice 7.1, regardés page par page et validés au schéma OOXML sans erreur. Le rendu dans Word n'a pas été contrôlé ; le contrôle de l'Étape 5 reste obligatoire.

```
# =====================================================================================
# Extension v7.2 — recettes R9 à R14 (Référentiel pédagogique IA 7.2)
# =====================================================================================
import math, os, itertools

# ---------- R9 : format affiche A3 et lisibilité à distance ----------
FORMATS_CM = {'A4': (21.0, 29.7), 'A3': (29.7, 42.0)}
ARIAL_CAPITALE = 0.716                 # hauteur des capitales d'Arial, en fraction du corps (métrique de la police)

def page_format(doc, fmt='A3', paysage=False, police='Arial', taille=48, interligne=1.15, marge_cm=2.5):
    """R9 : A3 ou A4, portrait ou paysage, marges de 2,5 cm (MP-F-03). Appelle page_a4 pour la base du document."""
    page_a4(doc, police=police, taille=taille, interligne=interligne)
    from docx.enum.section import WD_ORIENT
    w, h = FORMATS_CM[fmt]
    if paysage:
        w, h = h, w
    for s in doc.sections:
        s.orientation = WD_ORIENT.LANDSCAPE if paysage else WD_ORIENT.PORTRAIT
        s.page_width, s.page_height = Cm(w), Cm(h)
        s.top_margin = s.bottom_margin = s.left_margin = s.right_margin = Cm(marge_cm)
    return w - 2 * marge_cm, h - 2 * marge_cm      # largeur et hauteur utiles (cm)

def styles_affiche(doc, texte=48, titre=72, detail=36):
    """R9 : styles d'une affiche A3 (table du § 2.5). Valeurs par défaut pour des lecteurs de 3P à 8P."""
    style_para(doc, 'Affiche-Titre', titre, gras=True, centre=True, interligne=1.0, avant=0, apres=18)
    style_para(doc, 'Affiche-Texte', texte, interligne=1.1, apres=8)
    style_para(doc, 'Affiche-Étape', texte, interligne=1.1, apres=0)
    style_para(doc, 'Affiche-Détail', detail, interligne=1.1, apres=4)
    style_para(doc, 'Affiche-Cellule', detail, interligne=1.05, apres=0, centre=True)

def distance_lecture_m(taille_pt, facteur=1.0, capitale=ARIAL_CAPITALE):
    """Distance (m) à laquelle la capitale sous-tend 5 minutes d'arc × facteur.
    facteur=1 : seuil théorique ; facteur=2 : confort (inférence de conception)."""
    h_mm = taille_pt * 25.4 / 72 * capitale
    return h_mm / math.tan(math.radians(5 * facteur / 60)) / 1000

# ---------- R10 : écriture liée composée en GE Typo Libre (jamais dessinée ni générée) ----------
POLICE_CURSIVE = 'GE Typo Libre'
CARACTERES_ABSENTS_CURSIVE = '·ÂÄÎÏÖÙÛÜŸäÿæÆ–—%'   # sans dessin dans ge_typo_libre.otf (vérifié le 21.11.2026) : jamais en cursive

def taille_eleve(taille, texte):
    """MP-T-10 : corps de la police d'élèves pour la même hauteur apparente que le texte de la fiche (Arial) :
    1,25 fois le corps pour des lettres (hauteur des minuscules), 0,9 fois pour des chiffres seuls (les chiffres de
    GE Typo Libre sont plus hauts), 1,1 fois pour un mélange. Un même exemple garde un seul corps."""
    chiffres = all(c in '0123456789 +-=×:,./' for c in texte); lettres = not any(c.isdigit() for c in texte)
    return round(taille * (0.9 if chiffres else 1.25 if lettres else 1.1) * 2) / 2

def ecrire_exemple(p, donnee, exemple, taille, suite=''):
    """MP-T-10 : une ligne d'exemple. donnee (consigne, item, intitulé « Exemple : ») dans la police de la fiche ;
    exemple (la réponse ou l'exemple montré) en police d'élèves, sans gras ni italique ; suite éventuelle dans la
    police de la fiche. Un mot qui contient un caractère absent de la police reste en script."""
    if donnee: ecrire(p, donnee)
    mots = exemple.split(' ')
    if not set(exemple) & set(CARACTERES_ABSENTS_CURSIVE): mots = [exemple]
    for k, m in enumerate(mots):
        if k: p.add_run(' ')
        if set(m) & set(CARACTERES_ABSENTS_CURSIVE): ecrire(p, m)
        else: ecrire_cursive(p, m, taille_eleve(taille, exemple))
    if suite: ecrire(p, suite)
    return p

def police_cursive_installee():
    for d in ('~/Library/Fonts', '/Library/Fonts', '~/.fonts', '~/.local/share/fonts'):
        if os.path.exists(os.path.join(os.path.expanduser(d), 'ge_typo_libre.otf')):
            return os.path.join(os.path.expanduser(d), 'ge_typo_libre.otf')
    return None

def ecrire_cursive(p, texte, taille):
    """R10 : run en GE Typo Libre. Refuse les caractères sans dessin ; une seule casse d'origine, aucun effet."""
    assert not set(texte) & set(CARACTERES_ABSENTS_CURSIVE), 'caractère absent de la police cursive'
    r = p.add_run(texte)
    r.font.name = POLICE_CURSIVE; r.font.size = Pt(taille)
    rf = r._r.get_or_add_rPr().rFonts
    for a in ('w:ascii', 'w:hAnsi', 'w:cs', 'w:eastAsia'):
        rf.set(qn(a), POLICE_CURSIVE)
    return r

def verifier_cursive_pdf(chemin_pdf):
    """V15 : la police cursive est incorporée au PDF (équivalent de pdffonts)."""
    import pymupdf
    d = pymupdf.open(chemin_pdf)
    noms = {f[3] for page in d for f in page.get_fonts()}
    return any('GETypoLibre' in n for n in noms), sorted(noms)

# ---------- R11 : dessin vectoriel (SVG et PDF à l'échelle 1, unités en mm) ----------
POLICES_PDF = {'Arial': '/System/Library/Fonts/Supplemental/Arial.ttf',
               'Arial-B': '/System/Library/Fonts/Supplemental/Arial Bold.ttf'}
if police_cursive_installee(): POLICES_PDF['Eleve'] = police_cursive_installee()   # MP-T-10 : police d'élèves

def police_exemple_pdf():
    """MP-T-10 : police de Dessin pour un exemple : 'Eleve' (GE Typo Libre) si elle est installée ; sinon 'Arial',
    repli à signaler (MP-T-08)."""
    return 'Eleve' if 'Eleve' in POLICES_PDF else 'Arial'

# Couleur facultative (21.11.2026). Par défaut : noir et blanc. La couleur ne porte jamais seule une information
# (MP-C-02) : un gris devient une teinte de même clarté, de sorte qu'une photocopie en noir et blanc reste identique.
TEINTES = {'bleu': (0.00, 0.45, 0.70), 'orange': (0.90, 0.62, 0.00), 'vert': (0.00, 0.62, 0.45),
           'violet': (0.80, 0.47, 0.65), 'ciel': (0.34, 0.71, 0.91), 'vermillon': (0.84, 0.37, 0.00)}
TEINTES_CATEGORIES = ('bleu', 'orange', 'vert', 'violet', 'ciel', 'vermillon')   # une teinte par symbole de catégorie
COULEUR = [None]

def definir_couleur(nom=None):
    """nom=None : noir et blanc (défaut). Sinon une clé de TEINTES : tous les dessins créés ensuite sont teintés
    (fonds gris, symboles de catégorie, dos des cartes). À remettre à None après la production."""
    assert nom is None or nom in TEINTES, 'teinte inconnue : ' + str(nom)
    COULEUR[0] = nom

JEUNES = [False]

def definir_jeunes(oui=True):
    """oui=True : fiches dessinées pour des élèves qui n'écrivent pas encore sur une ligne (1P-2P surtout) : la ligne
    « Prénom » devient la mention « Prénom au dos de la feuille » et aucune ligne de date n'est tracée (MP-O-03).
    À remettre à False après la production."""
    JEUNES[0] = bool(oui)

def _prenom():
    return 'Prénom au dos de la feuille' if JEUNES[0] else 'Prénom : ____________________'

def _teinter(fond):
    """Un gris devient une teinte de même clarté ; le blanc, le noir et les couleurs données restent inchangés."""
    if fond is None or COULEUR[0] is None or not (fond[0] == fond[1] == fond[2]) or fond[0] in (0, 1): return fond
    t = TEINTES[COULEUR[0]]; v = fond[0]; lum = 0.3 * t[0] + 0.59 * t[1] + 0.11 * t[2]
    if v >= lum: a = (1 - v) / (1 - lum); return tuple(1 - a * (1 - c) for c in t)
    return tuple(v / lum * c for c in t)

def couleur_trait():
    """Couleur des traits d'un dos de carte : la teinte choisie, assombrie ; noir sans couleur."""
    return (0, 0, 0) if COULEUR[0] is None else tuple(0.75 * c for c in TEINTES[COULEUR[0]])

class Dessin:
    """R11 : tracés, roues, patrons. Mêmes primitives vers SVG (fichier source) et vers PDF (échelle 1).
    Coordonnées en mm depuis le coin supérieur gauche."""
    def __init__(self, l=210, h=297):
        import pymupdf
        self.f = pymupdf; self.l, self.h = l, h
        self.d = pymupdf.open(); self.p = self.d.new_page(width=l * 72 / 25.4, height=h * 72 / 25.4)
        self.s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{l}mm" height="{h}mm" viewBox="0 0 {l} {h}">']
        self.k = 72 / 25.4; self.trait = (0, 0, 0)

    def _hex(self, c):
        return '#' + ''.join(f'{int(v*255):02x}' for v in c)

    def _P(self, x, y):
        return self.f.Point(x * self.k, y * self.k)

    def ligne(self, pts, ep=0.5, tirets=None, ferme=False, fond=None):
        sh = self.p.new_shape(); q = [self._P(*a) for a in pts]; fond = _teinter(fond)
        sh.draw_polyline(q + ([q[0]] if ferme else []))
        sh.finish(width=ep * self.k, color=self.trait, fill=fond, closePath=ferme,
                  dashes=None if not tirets else f'[{tirets[0]*self.k:.2f} {tirets[1]*self.k:.2f}] 0', lineCap=1, lineJoin=1)
        sh.commit()
        d = ' '.join(f'{x:.2f},{y:.2f}' for x, y in pts)
        a = f' stroke-dasharray="{tirets[0]} {tirets[1]}"' if tirets else ''
        f = '#' + ''.join(f'{int(c*255):02x}' for c in fond) if fond else 'none'
        self.s.append(f'<{"polygon" if ferme else "polyline"} points="{d}" fill="{f}" stroke="{self._hex(self.trait)}" stroke-width="{ep}"{a}/>')

    def cercle(self, cx, cy, r, ep=0.5, tirets=None, fond=None):
        sh = self.p.new_shape(); sh.draw_circle(self._P(cx, cy), r * self.k); fond = _teinter(fond)
        sh.finish(width=ep * self.k, color=self.trait if ep else None, fill=fond,
                  dashes=None if not tirets else f'[{tirets[0]*self.k:.2f} {tirets[1]*self.k:.2f}] 0')
        sh.commit()
        a = f' stroke-dasharray="{tirets[0]} {tirets[1]}"' if tirets else ''
        f = '#' + ''.join(f'{int(c*255):02x}' for c in fond) if fond else 'none'
        self.s.append(f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{r:.2f}" fill="{f}" stroke="{self._hex(self.trait)}" stroke-width="{ep}"{a}/>')

    def largeur_texte(self, txt, taille_pt, police='Arial'):
        return self.f.Font(fontfile=POLICES_PDF[police]).text_length(txt, fontsize=taille_pt) / self.k

    def texte(self, x, y, txt, taille_pt=14, ancre='m', police='Arial', rot=0):
        """(x, y) = centre de la ligne de base si ancre='m', début si ancre='s'. rot : degrés, sens horaire."""
        l = self.largeur_texte(txt, taille_pt, police)
        dx = -l / 2 if ancre == 'm' else 0
        a = math.radians(rot)
        px, py = x + dx * math.cos(a), y + dx * math.sin(a)
        Q = self._P(px, py)
        self.p.insert_text(Q, txt, fontsize=taille_pt, fontname=police.replace('-', ''), fontfile=POLICES_PDF[police],
                           morph=(Q, self.f.Matrix(-rot)))
        g = ' font-weight="bold"' if police.endswith('-B') else ''
        t = txt.replace('&', '&amp;').replace('<', '&lt;')
        self.s.append(f'<text x="{x:.2f}" y="{y:.2f}" font-family="Arial" font-size="{taille_pt*25.4/72:.2f}" '
                      f'text-anchor="{"middle" if ancre=="m" else "start"}"{g} transform="rotate({rot} {x:.2f} {y:.2f})">{t}</text>')

    def sauver(self, base):
        """Écrit base.svg (source vectorielle) et base.pdf (vectoriel, échelle 1)."""
        open(base + '.svg', 'w', encoding='utf-8').write('\n'.join(self.s) + '\n</svg>\n')
        self.d.save(base + '.pdf')
        return base + '.pdf'

    def png(self, base, dpi=300):
        self.p.get_pixmap(dpi=dpi).save(base + '.png')
        return base + '.png'

def arc_pts(cx, cy, r, a0, a1, n=40):
    """Points d'un arc ; angles en degrés depuis midi, sens horaire."""
    return [(cx + r * math.sin(math.radians(a0 + (a1 - a0) * i / n)),
             cy - r * math.cos(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]

def couloir(dessin, pts, largeur):
    """R11 : chemin à bords parallèles autour de la ligne médiane pts (G19)."""
    g, d = [], []
    for i, (x, y) in enumerate(pts):
        x0, y0 = pts[max(i - 1, 0)]; x1, y1 = pts[min(i + 1, len(pts) - 1)]
        n = math.hypot(x1 - x0, y1 - y0) or 1
        nx, ny = -(y1 - y0) / n, (x1 - x0) / n
        g.append((x + nx * largeur / 2, y + ny * largeur / 2)); d.append((x - nx * largeur / 2, y - ny * largeur / 2))
    dessin.ligne(g, ep=0.7); dessin.ligne(d, ep=0.7)

def arrondir(pts, n=4):
    """R11 : arrondit une ligne brisée (coupe des coins) pour que le couloir garde sa largeur dans les virages."""
    for _ in range(n):
        q = [pts[0]]
        for a, b in zip(pts, pts[1:]):
            q += [(a[0] * .75 + b[0] * .25, a[1] * .75 + b[1] * .25), (a[0] * .25 + b[0] * .75, a[1] * .25 + b[1] * .75)]
        pts = q + [pts[-1]]
    return pts

def couloir_valide(pts, largeur, marge=2.0, saut=12):
    """V16 : deux portions non voisines du couloir restent séparées d'au moins largeur + marge (mm)."""
    m = min(math.hypot(pts[i][0] - pts[j][0], pts[i][1] - pts[j][1])
            for i in range(len(pts)) for j in range(i + saut, len(pts)))
    return m >= largeur + marge, m

def labyrinthe(lignes, colonnes, graine=1):
    """Labyrinthe parfait : exactement un chemin entre deux cases (arbre couvrant, parcours en profondeur)."""
    rng = random.Random(graine)
    murs = {(l, c): {'N', 'S', 'E', 'O'} for l in range(lignes) for c in range(colonnes)}
    vu = {(0, 0)}; pile = [(0, 0)]
    D = {'N': (-1, 0, 'S'), 'S': (1, 0, 'N'), 'E': (0, 1, 'O'), 'O': (0, -1, 'E')}
    while pile:
        l, c = pile[-1]
        v = [(k, l + a, c + b, o) for k, (a, b, o) in D.items() if (l + a, c + b) in murs and (l + a, c + b) not in vu]
        if not v:
            pile.pop(); continue
        k, a, b, o = rng.choice(v)
        murs[(l, c)].discard(k); murs[(a, b)].discard(o); vu.add((a, b)); pile.append((a, b))
    return murs

def labyrinthe_unique(murs, lignes, colonnes):
    """V16 : case d'arrivée atteinte et nombre de passages = cases − 1 (arbre, donc chemin unique)."""
    passages = sum(len({'N', 'S', 'E', 'O'} - m) for m in murs.values()) // 2
    return passages == lignes * colonnes - 1

def tracer_labyrinthe(dessin, murs, lignes, colonnes, x0, y0, case):
    for (l, c), m in murs.items():
        x, y = x0 + c * case, y0 + l * case
        if 'N' in m and not (l == 0 and c == 0): dessin.ligne([(x, y), (x + case, y)], ep=0.7)
        if 'O' in m and not (l == 0 and c == 0): dessin.ligne([(x, y), (x, y + case)], ep=0.7)
        if l == lignes - 1 and 'S' in m and not c == colonnes - 1: dessin.ligne([(x, y + case), (x + case, y + case)], ep=0.7)
        if c == colonnes - 1 and 'E' in m and not l == lignes - 1: dessin.ligne([(x + case, y), (x + case, y + case)], ep=0.7)

def roue_J11(paires, base, degre_pt=14):
    """R11 : J11, deux disques de 11 cm. paires : [(question, réponse)] ; 6 secteurs.
    Disque inférieur (contenu) et disque supérieur (fenêtre, rabat). Renvoie le Dessin et le rapport V18."""
    n = len(paires); pas = 360 / n
    R, RM, RI = 55, 38, 16
    D = Dessin(160, 240); cx, y1, y2 = 56, 63, 184
    D.texte(0, 5, 'Disque du dessous : découpe sur les pointillés.', 12, ancre='s', police='Arial-B')
    D.cercle(cx, y1, R, ep=0.5, tirets=(3, 2)); D.cercle(cx, y1, RM, ep=0.25); D.cercle(cx, y1, 1.2, ep=0, fond=(0, 0, 0))
    D.cercle(cx, y1, RI, ep=0.25)
    for k, (q, r) in enumerate(paires):
        a = k * pas
        a2 = a + pas / 2
        D.ligne([(cx + RI * math.sin(math.radians(a2)), y1 - RI * math.cos(math.radians(a2))),
                 (cx + R * math.sin(math.radians(a2)), y1 - R * math.cos(math.radians(a2)))], ep=0.25)
        for t, rr in ((q, 45), (r, 28)):
            D.texte(cx + rr * math.sin(math.radians(a)), y1 - rr * math.cos(math.radians(a)), t, degre_pt, rot=a,
                    police='Arial-B' if rr == 28 else 'Arial')
    D.texte(0, 124, 'Disque du dessus : découpe la fenêtre et le rabat. Plie sur le trait fin.', 12, ancre='s', police='Arial-B')
    D.cercle(cx, y2, R, ep=0.5, tirets=(3, 2)); D.cercle(cx, y2, 1.2, ep=0, fond=(0, 0, 0))
    A = pas / 2 - 3
    fen = arc_pts(cx, y2, 52, -A, A) + arc_pts(cx, y2, 39, A, -A)
    D.ligne(fen, ep=0.5, tirets=(3, 2), ferme=True)
    D.ligne(arc_pts(cx, y2, 36, -A, A) + arc_pts(cx, y2, 18, A, A, 1)[1:], ep=0.5, tirets=(3, 2))
    D.ligne(arc_pts(cx, y2, 36, -A, -A, 1) + arc_pts(cx, y2, 18, -A, -A, 1)[1:], ep=0.5, tirets=(3, 2))
    D.ligne(arc_pts(cx, y2, 18, -A, A), ep=0.25, tirets=(1, 1))
    D.texte(cx, y2 + 16, 'Tourne.', 14); D.texte(cx, y2 + 24, 'Réponds.', 14); D.texte(cx, y2 + 32, 'Soulève le rabat.', 14)
    D.texte(118, 59, 'Attache parisienne', 11, ancre='s'); D.texte(118, 64, 'au centre des', 11, ancre='s'); D.texte(118, 69, 'deux disques.', 11, ancre='s')
    # V18 : chaque texte, centré dans la fenêtre ou sous le rabat, y tient entièrement
    rep = []
    for q, r in paires:
        lq, lr = D.largeur_texte(q, degre_pt), D.largeur_texte(r, degre_pt, 'Arial-B')
        cq = 2 * 45 * math.sin(math.radians(A)) ; cr = 2 * 28 * math.sin(math.radians(A))
        rep.append((q, r, round(lq, 1), round(cq, 1), round(lr, 1), round(cr, 1), lq < cq - 2 and lr < cr - 2))
    D.sauver(base); D.png(base)
    return D, rep

def inserer_image(doc_ou_cell, chemin, largeur_cm, centre=True):
    """Image de largeur exacte. Le dessin source reste le fichier SVG ou PDF."""
    p = doc_ou_cell.add_paragraph() if not hasattr(doc_ou_cell, 'add_run') else doc_ou_cell
    p.add_run().add_picture(chemin, width=Cm(largeur_cm))
    if centre:
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(0); p.paragraph_format.line_spacing = 1.0
    return p

def icone(code, dossier, sortie, dpi=300):
    """Icône de la banque IC (SVG) convertie en PNG pour le .docx."""
    import pymupdf
    os.makedirs(sortie, exist_ok=True)
    png = os.path.join(sortie, code + '.png')
    if not os.path.exists(png):
        d = pymupdf.open(os.path.join(dossier, code + '.svg'))
        pymupdf.open('pdf', d.convert_to_pdf())[0].get_pixmap(dpi=dpi, alpha=False).save(png)
    return png

# ---------- R12 : planche recto-verso ----------
def verso_de(rangees):
    """R12 : inverse les colonnes pour une impression recto-verso sur le bord long (J4, J10, J14, G15)."""
    return [list(reversed(r)) for r in rangees]

def en_rangees(pieces, par_rangee):
    r = [pieces[i:i + par_rangee] for i in range(0, len(pieces), par_rangee)]
    while len(r[-1]) < par_rangee:
        r[-1].append(None)
    return r

# ---------- R13 : contrôles combinatoires (V11 élargi, V19) ----------
def generer_loto(elements, n_cartons, par_carton, graine=1, essais=200000):
    """J7 : chaque élément figure sur le même nombre de cartons ; cartons tous différents, aucun doublon dans un carton."""
    f = n_cartons * par_carton / len(elements)
    assert f == int(f), 'le produit cartons × cases doit être un multiple du nombre d\'éléments'
    rng = random.Random(graine); f = int(f)
    for _ in range(essais):
        reste = {e: f for e in elements}; cartons = []
        try:
            for _c in range(n_cartons):
                pris = []
                for _k in range(par_carton):
                    m = max(v for e, v in reste.items() if e not in pris)
                    choix = [e for e, v in reste.items() if v >= max(m - 1, 1) and e not in pris]
                    e = rng.choice(choix); pris.append(e); reste[e] -= 1
                cartons.append(pris)
        except (ValueError, IndexError):
            continue
        if not verifier_loto(cartons, elements, f, silence=True):
            continue
        return cartons
    raise RuntimeError('aucune répartition trouvée')

def verifier_loto(cartons, elements, frequence, silence=False):
    """V19 : fréquence exacte de chaque élément ; pas de doublon dans un carton ; cartons tous différents."""
    try:
        for e in elements:
            assert sum(c.count(e) for c in cartons) == frequence, f'fréquence de {e}'
        assert all(len(set(c)) == len(c) for c in cartons), 'doublon dans un carton'
        assert len({frozenset(c) for c in cartons}) == len(cartons), 'deux cartons identiques'
    except AssertionError:
        if silence:
            return False
        raise
    return True

def plan_projectif(n):
    """J8 : n premier, ou n = 4 ; n² + n + 1 cartes de n + 1 symboles ; deux cartes quelconques partagent exactement un symbole."""
    M = [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 3, 1], [0, 3, 1, 2]]          # produit dans le corps à quatre éléments
    f = (lambda a, x, b: M[a][x] ^ b) if n == 4 else (lambda a, x, b: (a * x + b) % n)
    cartes = []
    for a in range(n):
        for b in range(n):
            cartes.append([x * n + f(a, x, b) for x in range(n)] + [n * n + a])
    for x in range(n):
        cartes.append([x * n + y for y in range(n)] + [n * n + n])
    cartes.append([n * n + i for i in range(n + 1)])
    return cartes

def verifier_symboles(cartes):
    """V19 : chaque paire de cartes a exactement un symbole commun."""
    for a, b in itertools.combinations(cartes, 2):
        assert len(set(a) & set(b)) == 1, (a, b)
    return True

def verifier_appariement(paires):
    """V11 : chaque question a une seule réponse, chaque réponse une seule question (mémoire, carte à pince, loto)."""
    q = [p[0] for p in paires]; r = [p[1] for p in paires]
    assert len(set(q)) == len(q) and len(set(r)) == len(r), 'appariement ambigu'
    return True

def verifier_code(enigmes, code):
    """V11 et V21 (escape game) : chaque énigme porte son calcul ('calcul', expression arithmétique)
    et le chiffre annoncé ('chiffre') ; le calcul DOIT donner un nombre entier de 0 à 9 égal au chiffre annoncé,
    et la suite des chiffres donne le code final. Une énigme dont la réponse a deux chiffres est refusée."""
    for i, e in enumerate(enigmes, 1):
        assert 'calcul' in e, f'énigme {i} : calcul absent, le chiffre ne peut pas être vérifié'
        assert set(e['calcul']) <= set('0123456789+-*/%() '), f'énigme {i} : calcul non arithmétique'
        r = eval(e['calcul'], {'__builtins__': {}})
        assert r == int(r) and 0 <= int(r) <= 9, f"énigme {i} : la réponse {r} n'est pas un chiffre de 0 à 9"
        assert int(r) == int(e['chiffre']), f'énigme {i} : chiffre annoncé {e["chiffre"]}, calcul {int(r)}'
    assert ''.join(str(e['chiffre']) for e in enigmes) == code, 'code incohérent'
    return True

def verifier_graphemes(paires):
    """V21 : chaque mot proposé contient bien le graphème étudié (son et graphème, cartes de sons, mots à trier).
    paires : [(graphème, mot)]. La comparaison ignore la casse ; accents conservés (é ≠ e)."""
    fautes = [(g, m) for g, m in paires if g.lower() not in m.lower()]
    assert not fautes, f'graphème absent du mot : {fautes}'
    return True

# ---------- R14 : grille à zones et planche à zones ----------
TRAIT = ('single', 6, '595959')
TRAIT_FORT = ('single', 12, '000000')

def _remplir(cell, contenu, style, doc):
    """contenu : None ; str ; liste de lignes (str ou segments) ; {'img': chemin ou liste, 'cm': largeur} ; {'cursive': texte, 'pt': taille}."""
    p = cell.paragraphs[0]; p.style = doc.styles[style]
    p.paragraph_format.keep_with_next = True
    if contenu is None:
        return
    lignes = contenu if isinstance(contenu, list) else [contenu]
    for i, l in enumerate(lignes):
        if i:
            p = cell.add_paragraph(style=style)
        if l is None:
            continue
        if isinstance(l, tuple):
            l = [l]
        if isinstance(l, dict) and 'img' in l:
            for im in (l['img'] if isinstance(l['img'], list) else [l['img']]):
                p.add_run().add_picture(im, width=Cm(l['cm']))
        elif isinstance(l, dict) and 'cursive' in l:
            ecrire_cursive(p, l['cursive'], l['pt'])
        else:
            ecrire(p, l)

def grille(doc, lignes, largeurs_cm, hauteurs_cm=1.0, exacte=False, style='Fiche-Bilan', trait=TRAIT,
           entete=False, vertical=WD_ALIGN_VERTICAL.CENTER, marge_cell_cm=0.15):
    """R14 : tableau à largeurs fixées dont chaque cellule reçoit texte, image ou cursive."""
    t = doc.add_table(rows=len(lignes), cols=len(largeurs_cm))
    geometrie(t, list(largeurs_cm), marge_cell_cm=marge_cell_cm)
    hs = hauteurs_cm if isinstance(hauteurs_cm, (list, tuple)) else [hauteurs_cm] * len(lignes)
    for i, row in enumerate(t.rows):
        ligne_tableau(row, hs[i], exacte=exacte, entete=(entete and i == 0))
        for j, c in enumerate(row.cells):
            if trait:
                bordures(c, top=trait, left=trait, bottom=trait, right=trait)
            else:
                bordures(c)
            c.vertical_alignment = vertical
            contenu = lignes[i][j]
            if entete and i == 0 and isinstance(contenu, str):
                contenu = [[(contenu, {'b': True})]]
            _remplir(c, contenu, style, doc)
    solidariser_tableau(t)
    return t

def planche_zones(doc, rangees, largeur_cm, hauteurs_cm, sous_colonnes=1, mention=None, saut_avant=True,
                  style='Fiche-Pièce', zones_verticales=None):
    """R14 / R8 : planche de pièces découpées en zones superposées.
    rangees : liste de rangées ; pièce = liste de zones (une par hauteur) ou None ;
    zone = contenu unique ou tuple de contenus côte à côte (sous-cellules de largeur égale)."""
    if mention:
        m = doc.add_paragraph(style='Fiche-Mention'); ecrire(m, mention)
        m.paragraph_format.page_break_before = saut_avant
        solidariser(m)
    nz = len(hauteurs_cm); npc = len(rangees[0])
    t = doc.add_table(rows=nz * len(rangees), cols=npc * sous_colonnes)
    geometrie(t, [largeur_cm / sous_colonnes] * (npc * sous_colonnes), marge_cell_cm=0.1)
    fin = ('single', 4, '595959')
    for r, rangee in enumerate(rangees):
        for z in range(nz):
            row = t.rows[r * nz + z]; ligne_tableau(row, hauteurs_cm[z], exacte=True)
        for k, piece in enumerate(rangee):
            for z in range(nz):
                zone = None if piece is None else piece[z]
                cells = zone if isinstance(zone, tuple) else (zone,)
                span = sous_colonnes // len(cells)
                for s, contenu in enumerate(cells):
                    c0 = k * sous_colonnes + s * span
                    c = t.cell(r * nz + z, c0)
                    if span > 1:
                        c = c.merge(t.cell(r * nz + z, c0 + span - 1))
                    c.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
                    if piece is None:
                        bordures(c); _remplir(c, None, style, doc); continue
                    bordures(c, top=COUPE if z == 0 else fin, bottom=COUPE if z == nz - 1 else fin,
                             left=COUPE if s == 0 else fin, right=COUPE if s == len(cells) - 1 else fin)
                    _remplir(c, contenu, style, doc)
    return t
```

#### Révision du 2 novembre 2026 : R7, `verifier_code`, `verifier_graphemes`, R15 et V20

Trois changements dans les blocs ci-dessus : R7 écrit l'objectif sans étiquette (une étiquette fournie par erreur est retirée) ; `verifier_code` exige le calcul de chaque énigme et refuse une réponse qui n'est pas un chiffre de 0 à 9 ; `verifier_graphemes` (V21) est ajoutée. Le bloc suivant ajoute R15 (planche A5) et V20 (page pleine) ; il se place à la fin du module. Le fichier `recettes_v7.2.py` (révision du 2 novembre 2026) réunit les trois blocs.

**Test (révision du 2.11.2026)** : 54 documents d'essai corrigés, convertis en PDF avec LibreOffice, mesurés page par page (remplissage de 90 % au moins sur toutes les pages élèves, mesuré sur l'image de la page) et validés au schéma OOXML ; R7, R15, `verifier_code`, `verifier_graphemes` et `verifier_remplissage` testés sur un document d'essai (cas conformes et cas fautifs refusés). Le rendu dans Word n'a pas été contrôlé.

```
# =====================================================================================
# Révision du 2 novembre 2026 — R15 (planche A5) et V20 (page pleine, MP-O-14)
# =====================================================================================
from docx.enum.section import WD_SECTION, WD_ORIENT

COUPE_A5 = ('dashed', 8, '000000')     # trait de coupe entre les deux exemplaires A5

# ---------- R15 : planche A5, deux exemplaires sur une feuille A4 (MP-O-14) ----------
def planche_A5(doc, remplir, disposition='cote_a_cote', marge_cm=1.0, retrait_cm=0.9, nouvelle_section=True):
    """R15 : une feuille A4 porte deux exemplaires A5 identiques séparés par un trait de coupe en tirets.
    'cote_a_cote' : A4 paysage, deux colonnes A5 portrait, largeur de contenu 12,05 cm (règle de jeu, petite fiche) ;
    'empile' : A4 portrait, deux rangées A5 paysage, largeur de contenu 17,2 cm (bande, ticket de sortie).
    remplir(cellule, largeur_cm) écrit UN exemplaire dans la cellule (cellule.add_paragraph, cellule.add_table) ;
    elle est appelée deux fois, pour que les deux moitiés soient identiques.
    La planche ouvre une section propre ; la suite du document reprend sa mise en page avec nouvelle_section_a4()."""
    s = doc.add_section(WD_SECTION.NEW_PAGE) if nouvelle_section else doc.sections[-1]
    if disposition == 'cote_a_cote':
        s.orientation = WD_ORIENT.LANDSCAPE; s.page_width, s.page_height = Cm(29.7), Cm(21.0)
    else:
        s.orientation = WD_ORIENT.PORTRAIT; s.page_width, s.page_height = Cm(21.0), Cm(29.7)
    for m in ('top_margin', 'bottom_margin', 'left_margin', 'right_margin'):
        setattr(s, m, Cm(marge_cm))
    pw, ph = s.page_width.cm, s.page_height.cm
    if disposition == 'cote_a_cote':
        cw, chh = (pw - 2 * marge_cm) / 2, ph - 2 * marge_cm
        t = doc.add_table(rows=1, cols=2); cells = [t.cell(0, 0), t.cell(0, 1)]
    else:
        cw, chh = pw - 2 * marge_cm, (ph - 2 * marge_cm) / 2
        t = doc.add_table(rows=2, cols=1); cells = [t.cell(0, 0), t.cell(1, 0)]
    geometrie(t, [cw] * len(t.columns), marge_cell_cm=0.0)
    for row in t.rows:
        ligne_tableau(row, chh - 0.1)
    if disposition == 'cote_a_cote':
        bordures(cells[0], right=COUPE_A5); bordures(cells[1], left=COUPE_A5)
    else:
        bordures(cells[0], bottom=COUPE_A5); bordures(cells[1])
    for c in cells:
        tcPr = c._tc.get_or_add_tcPr()
        mar = OxmlElement('w:tcMar')
        for edge, v in (('top', 0.6), ('left', retrait_cm), ('bottom', 0.0), ('right', retrait_cm)):
            e = OxmlElement(f'w:{edge}'); e.set(qn('w:w'), TW(v)); e.set(qn('w:type'), 'dxa'); mar.append(e)
        b = tcPr.find(qn('w:tcBorders'))
        if b is not None:
            b.addnext(mar)
        else:
            tcPr.append(mar)
        c.vertical_alignment = WD_ALIGN_VERTICAL.TOP
        remplir(c, cw - 2 * retrait_cm)
    return t

def nouvelle_section_a4(doc, paysage=False, marge_cm=2.5):
    """Après une planche A5 placée en milieu de document : reprend l'A4 avec les marges du Livre I (MP-F-03)."""
    s = doc.add_section(WD_SECTION.NEW_PAGE)
    s.orientation = WD_ORIENT.LANDSCAPE if paysage else WD_ORIENT.PORTRAIT
    s.page_width, s.page_height = (Cm(29.7), Cm(21.0)) if paysage else (Cm(21.0), Cm(29.7))
    for m in ('top_margin', 'bottom_margin', 'left_margin', 'right_margin'):
        setattr(s, m, Cm(marge_cm))
    return s

# ---------- V20 : remplissage des pages sur le rendu (MP-O-14) ----------
_PT_CM = 72 / 2.54

def budget_page(largeur_cm, hauteur_cm):
    """Marge haute et budget de hauteur (§ 2.2 et § 2.5) selon le format de la page."""
    if abs(largeur_cm - 21) < .5 and abs(hauteur_cm - 29.7) < .5:
        return 2.5, 22.0                        # A4 portrait
    if abs(largeur_cm - 29.7) < .5 and abs(hauteur_cm - 21) < .5:
        return 2.5, 16 * 22 / 24.7              # A4 paysage
    if abs(largeur_cm - 29.7) < .5 and abs(hauteur_cm - 42) < .5:
        return 2.5, 33.0                        # A3 portrait
    if abs(largeur_cm - 42) < .5 and abs(hauteur_cm - 29.7) < .5:
        return 2.5, 22.0                        # A3 paysage
    return 2.5, (hauteur_cm - 5) * 22 / 24.7

def remplissage_pages(chemin_pdf, planches_A5=None, dpi=50, gris=200):
    """Mesure, page par page, la position du dernier élément VISIBLE (encre sur l'image rendue de la page),
    rapportée au budget de hauteur. Un cadre blanc, une bordure absente ou la marge blanche d'une image ne
    comptent pas. planches_A5 : {numéro de page: 'cote_a_cote' ou 'empile'} ; pour ces pages, la mesure porte
    sur un exemplaire A5 (marge haute 1,6 cm), le trait de coupe étant ignoré. Requiert PyMuPDF et NumPy."""
    import pymupdf, numpy as np
    planches_A5 = planches_A5 or {}
    res = []
    with pymupdf.open(chemin_pdf) as doc:
        for i, pg in enumerate(doc, 1):
            pix = pg.get_pixmap(dpi=dpi, colorspace=pymupdf.csGRAY, alpha=False)
            img = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.stride)[:, :pix.width]
            px = dpi / 2.54                                  # pixels par centimètre
            encre = img < gris
            disp = planches_A5.get(i)
            if disp == 'cote_a_cote':                        # trait de coupe vertical au milieu
                m = pix.width // 2; d = int(0.3 * px) + 1
                encre[:, m - d:m + d] = False
            if disp == 'empile':                             # exemplaire du haut seulement
                encre = encre[:pix.height // 2 - int(0.3 * px)]
            lignes = np.where(encre.any(axis=1))[0]
            bas = float(lignes[-1] + 1) / px if len(lignes) else 0.0
            if disp == 'empile':
                haut, bud = 1.6, (29.7 - 2) / 2 * 22 / 24.7
            elif disp == 'cote_a_cote':
                haut, bud = 1.6, (21 - 2) * 22 / 24.7
            else:
                haut, bud = budget_page(pix.width / px, pix.height / px)
            bas = float(bas)
            res.append({'page': i, 'bas_cm': round(bas, 1), 'remplissage': round((bas - haut) / bud, 2)})
    return res

def verifier_remplissage(chemin_pdf, seuil=0.90, plafond=1.10, pages_exclues=(), planches_A5=None):
    """V20 (MP-O-14) : aucune page élève remplie partiellement. Chaque page, hors pages exclues (partie
    enseignant·e, dernière planche d'un jeu de pièces déclarée dans la fiche technique), atteint au moins 90 %
    du budget de hauteur (A4 portrait : 19,8 cm sous la marge haute, soit au plus 4,9 cm de blanc en bas) et ne le dépasse pas de plus de 10 % (débordement probable). Renvoie les mesures."""
    mesures = remplissage_pages(chemin_pdf, planches_A5)
    fautes = [m for m in mesures if m['page'] not in pages_exclues and not (seuil <= m['remplissage'] <= plafond)]
    assert not fautes, ('pages hors limites (aérer, ajouter des lignes ou des exercices, ou passer en planche A5) : '
                        + ', '.join(f"p{m['page']} {int(m['remplissage'] * 100)} %" for m in fautes))
    return mesures
```

#### Révision du 2 novembre 2026, suite : `verifier_case_piece` (MP-J-10), `verifier_mots_coupes` et `carte_a_pinces` (J10)

Trois ajouts à la fin du module : `verifier_case_piece` refuse une case d'accueil qui ne dépasse pas la pièce mobile de 0,5 cm par côté (G12-b, plateaux, tableaux à étiquettes) ; `verifier_mots_coupes` compare les mots du .docx aux mots du PDF rendu et signale tout mot coupé par une cellule trop étroite (J9, SP8 ; R14, R15) ; `carte_a_pinces` construit la carte J10 (une page, un bloc de trois lignes par question, réponses empilées au bord, verso avec « bravo »). Le fichier `recettes_v7.2.py` réunit les quatre blocs.

**Test (révision du 2.11.2026, suite)** : `verifier_case_piece` accepte (6 × 2,5 ; 8 × 3,5) et refuse (6 × 2,5 ; 6,8 × 3,5) et l'ancienne étiquette de G12-b (5,33 × 4,2 ; 8 × 3,2) ; `verifier_mots_coupes` signale un mot long placé dans une cellule de 1,5 cm sur un document d'essai rendu par LibreOffice ; `carte_a_pinces` testée sur J10 (recto 103 %, verso 98 %, « bravo » une fois par bloc) (statut : vérifié).

```
# ---------- Révision du 2 novembre 2026, suite : MP-J-10 (pièces mobiles) et mots coupés ----------
MARGE_PIECE_CM = 0.5

def verifier_case_piece(piece_cm, case_cm, marge_cm=MARGE_PIECE_CM, nom='case'):
    """MP-J-10 (V12) : une case destinée à recevoir une pièce mobile (étiquette, carte, jeton, pince)
    dépasse la pièce d'au moins 0,5 cm par côté, en largeur et en hauteur.
    piece_cm, case_cm : (largeur, hauteur) en cm. Refuse (AssertionError) toute case trop petite ;
    renvoie le jeu (dépassement par côté) en cm. À appeler avant grille() pour tout plateau à étiquettes."""
    (lp, hp), (lc, hc) = piece_cm, case_cm
    jeu_l, jeu_h = (lc - lp) / 2, (hc - hp) / 2
    fautes = []
    if jeu_l < marge_cm - 1e-9:
        fautes.append(f'largeur : pièce {lp} cm, {nom} {lc} cm, jeu {jeu_l:.2f} cm par côté (min {marge_cm})')
    if jeu_h < marge_cm - 1e-9:
        fautes.append(f'hauteur : pièce {hp} cm, {nom} {hc} cm, jeu {jeu_h:.2f} cm par côté (min {marge_cm})')
    assert not fautes, 'MP-J-10, case plus petite que la pièce + 0,5 cm par côté — ' + ' ; '.join(fautes)
    return round(jeu_l, 2), round(jeu_h, 2)

def verifier_mots_coupes(chemin_docx, chemin_pdf, minimum=4):
    """V10, V12 (R14, R15) : aucun mot du document n'est coupé au rendu. Compare les mots du .docx
    (python-docx : paragraphes et cellules) aux mots du PDF rendu (PyMuPDF) ; un mot d'au moins `minimum`
    lettres présent dans le .docx et absent du PDF a été coupé par une cellule trop étroite ou une césure.
    Renvoie la liste des mots coupés ; AssertionError s'il y en a."""
    import re, pymupdf
    from docx import Document
    def mots(texte):
        return set(m.lower() for m in re.findall(r"[^\W\d_]+(?:[’'][^\W\d_]+)?", texte) if len(m) >= minimum)
    d = Document(chemin_docx)
    textes = [p.text for p in d.paragraphs]
    for t in d.tables:
        for row in t.rows:
            for c in row.cells:
                textes.append(c.text)
    attendus = mots('\n'.join(textes))
    with pymupdf.open(chemin_pdf) as pdf:
        rendu = mots('\n'.join(page.get_text() for page in pdf))
    coupes = sorted(attendus - rendu)
    assert not coupes, 'mots coupés au rendu (élargir la cellule, raccourcir l’item ou réduire la taille) : ' + ', '.join(coupes)
    return coupes

# ---------- J10 : carte à pinces, une carte = une page (révision du 2.11.2026, suite) ----------
def carte_a_pinces(doc, questions, verso=False, largeur_q=13.4, largeur_opt=2.2, h_opt=0.85, mention=None, taille_q_pt=None):
    """J10 (révision du 2.11.2026, suite) : une carte = une page ; une question par bloc de trois lignes ;
    les trois réponses empilées dans la colonne du bord (droite au recto, gauche au verso) ; une pince par question.
    Au verso, le mot « bravo » dans la cellule de la bonne réponse (MP-J-04). questions : [(question, [r1, r2, r3], indice_juste)].
    Le numéro est tout à gauche ; la question est centrée dans son bloc, en grand (taille_q_pt : 28 pt jusqu'à
    6 questions, 22 pt jusqu'à 10, 18 pt au-delà, à réduire si une question est longue)."""
    if mention:
        m = doc.add_paragraph(style='Fiche-Mention'); ecrire(m, mention); solidariser(m)
    n = len(questions)
    t = doc.add_table(rows=3 * n, cols=2)
    cols = [largeur_opt, largeur_q] if verso else [largeur_q, largeur_opt]
    geometrie(t, cols, marge_cell_cm=0.12)
    iq, io = (1, 0) if verso else (0, 1)
    for k, (q, reps, juste) in enumerate(questions):
        for z in range(3):
            row = t.rows[3 * k + z]; ligne_tableau(row, h_opt, exacte=True)
            c = row.cells[io]; c.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            bordures(c, top=TRAIT_FORT if z == 0 else TRAIT, bottom=TRAIT_FORT if z == 2 else TRAIT,
                       left=TRAIT_FORT, right=TRAIT_FORT)
            txt = ('bravo' if (verso and z == juste) else None) if verso else reps[z]
            _remplir(c, [[(txt, {'b': True})]] if txt else None, 'Fiche-Données', doc)
            for pp in c.paragraphs: pp.alignment = WD_ALIGN_PARAGRAPH.CENTER; pp.paragraph_format.space_after = Pt(0)
        for z in range(3):
            bordures(t.cell(3 * k + z, iq), top=TRAIT_FORT if z == 0 else None, bottom=TRAIT_FORT if z == 2 else None,
                       left=TRAIT_FORT, right=TRAIT_FORT)
        a = t.cell(3 * k, iq).merge(t.cell(3 * k + 2, iq)); a.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        _remplir(a, None if verso else [[(f'{k + 1}.', {'b': True}), '\t' + q]], 'Fiche-Données', doc)
        tq = taille_q_pt or (28 if n <= 6 else 22 if n <= 10 else 18)
        for pp in a.paragraphs:
            pp.paragraph_format.space_after = Pt(0); pp.paragraph_format.left_indent = Cm(0.2)
            pp.paragraph_format.tab_stops.add_tab_stop(Cm(largeur_q / 2), WD_TAB_ALIGNMENT.CENTER)   # question centrée dans le bloc
            for r in pp.runs: r.font.size = Pt(tq)
    solidariser_tableau(t)
    return t
```

#### 3 novembre 2026 : G21, imagier et scène à légender

Quatre fonctions ajoutées pour G21 : `scene_numerotee` pose sur une image sans texte (PDF R11, PNG ou JPG) des pastilles blanches numérotées aux positions données et refuse deux pastilles trop proches ; `lignes_numerotees` écrit n lignes (ou cases, G21-a) numérotées en colonnes ; `bande_etiquettes` produit la bande d'étiquettes-mots à découper (ordre mélangé, pointillés) ; `verifier_imagier` contrôle repères, mots et articles (V21). Le fichier `recettes_v7.2.py` réunit les cinq blocs.

**Test (3.11.2026)** : essais G21-a (105 %) et G21-b (95 %) rendus et mesurés, scène de parc dessinée en R11 (huit éléments), schéma OOXML valide ; `verifier_imagier` refuse un mot sans article et un nombre de mots différent du nombre de repères (statut : vérifié).

```
# ---------- G21 : imagier et scène à légender (3.11.2026) ----------
def scene_numerotee(image, reperes, base, largeur_mm=160, rayon_mm=4.0, taille_pt=11, dpi=300):
    """G21, R11 : pose sur une image (PNG, JPG ou PDF, sans texte : MP-I-05) des pastilles blanches numérotées
    de 1 à n, aux positions données en fraction de la largeur et de la hauteur (0 à 1). L'image est mise à la
    largeur demandée ; la hauteur suit. Écrit base.pdf (vectoriel) et base.png. reperes : [(x, y)], dans l'ordre
    des numéros. Deux pastilles à moins de 2 rayons l'une de l'autre sont refusées (lisibilité)."""
    import pymupdf, math
    k = 72 / 25.4
    src = pymupdf.open(image)
    if src.is_pdf:
        pg = src[0]; w0, h0 = pg.rect.width, pg.rect.height
    else:
        pix = pymupdf.Pixmap(image); w0, h0 = pix.width, pix.height
    hauteur_mm = largeur_mm * h0 / w0
    d = pymupdf.open(); p = d.new_page(width=largeur_mm * k, height=hauteur_mm * k)
    if src.is_pdf:
        p.show_pdf_page(p.rect, src, 0)
    else:
        p.insert_image(p.rect, filename=image)
    pts = [(x * largeur_mm, y * hauteur_mm) for x, y in reperes]
    for i, (xa, ya) in enumerate(pts):
        for xb, yb in pts[i + 1:]:
            assert math.hypot(xa - xb, ya - yb) >= 2 * rayon_mm, f'pastilles trop proches : {i + 1}'
    for i, (x, y) in enumerate(pts, 1):
        c = pymupdf.Point(x * k, y * k)
        sh = p.new_shape(); sh.draw_circle(c, rayon_mm * k)
        sh.finish(width=0.6 * k, color=(0, 0, 0), fill=(1, 1, 1)); sh.commit()
        txt = str(i)
        f = pymupdf.Font('helv'); lt = f.text_length(txt, fontsize=taille_pt)
        p.insert_text(pymupdf.Point(c.x - lt / 2, c.y + taille_pt * 0.36), txt, fontsize=taille_pt, fontname='helv')
    d.save(base + '.pdf'); p.get_pixmap(dpi=dpi).save(base + '.png')
    return base + '.png', hauteur_mm / 10

def lignes_numerotees(doc, n, colonnes=2, hauteur_cm=1.0, largeur_cm=LARGEUR_UTILE_CM, style='Fiche-Données', amorce='', cases=False):
    """G21 : n lignes d'écriture numérotées (1, 2, …), réparties en colonnes, bordure inférieure seule (R1a) ;
    cases=True : cadres complets, pour coller une étiquette (G21-a)."""
    lignes_par_col = -(-n // colonnes)
    t = doc.add_table(rows=lignes_par_col, cols=colonnes)
    geometrie(t, [largeur_cm / colonnes] * colonnes, marge_cell_cm=0.15)
    for i, row in enumerate(t.rows):
        ligne_tableau(row, hauteur_cm, exacte=True)
        for j, c in enumerate(row.cells):
            num = j * lignes_par_col + i + 1
            c.vertical_alignment = WD_ALIGN_VERTICAL.BOTTOM
            if num <= n:
                if cases:
                    bordures(c, top=TRAIT, bottom=TRAIT, left=TRAIT, right=TRAIT); c.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
                else:
                    bordures(c, bottom=TRAIT)
                _remplir(c, [[(f'{num}.  ', {'b': True}), amorce]], style, doc)
            else:
                bordures(c); _remplir(c, None, style, doc)
            for pp in c.paragraphs: pp.paragraph_format.space_after = Pt(0)
    solidariser_tableau(t)
    return t

def bande_etiquettes(doc, mots, par_rangee=4, hauteur_cm=1.2, largeur_cm=LARGEUR_UTILE_CM, style='Fiche-Pièce', melange=True, graine=1):
    """G21-a : étiquettes-mots à découper (R8), bords en pointillés (MP-J-05), ordre mélangé (MP-J-03)."""
    mots = list(mots)
    if melange:
        mots = melanger_sans_voisins(mots, graine=graine)
    rangees = en_rangees(mots, par_rangee)
    t = doc.add_table(rows=len(rangees), cols=par_rangee)
    geometrie(t, [largeur_cm / par_rangee] * par_rangee, marge_cell_cm=0.1)
    for i, row in enumerate(t.rows):
        ligne_tableau(row, hauteur_cm, exacte=True)
        for j, c in enumerate(row.cells):
            c.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            if j < len(rangees[i]):
                bordures(c, top=COUPE, bottom=COUPE, left=COUPE, right=COUPE)
                _remplir(c, [[rangees[i][j]]], style, doc)
                for pp in c.paragraphs: pp.alignment = WD_ALIGN_PARAGRAPH.CENTER; pp.paragraph_format.space_after = Pt(0)
            else:
                bordures(c); _remplir(c, None, style, doc)
    solidariser_tableau(t)
    return t

def verifier_imagier(reperes, mots, articles=('der', 'die', 'das', 'le', 'la', 'les', 'un', 'une', 'a', 'an', 'the')):
    """V21 (G21) : autant de repères que de mots ; mots tous différents ; en langue étrangère, chaque mot
    commence par un article de la liste (l'article fait partie du mot appris)."""
    assert len(reperes) == len(mots), f'{len(reperes)} repères pour {len(mots)} mots'
    assert len(set(m.lower() for m in mots)) == len(mots), 'mot en double'
    sans = [m for m in mots if m.split()[0].lower() not in articles]
    assert not sans, f'mots sans article : {sans}'
    return True
```

#### 19 novembre 2026 : J5, plateaux de parcours (serpent, escargot, chemin, circuit)

`plateau_parcours` dessine le plateau de J5 avec la classe `Dessin` (R11), sur toute la surface utile d'une page A4 portrait, sans tableau : `'serpent'` (ruban de cases en lacets), `'escargot'` (spirale ronde, pioche et défausse en haut), `'chemin'` (cases rondes reliées par un pointillé) ou `'circuit'` (boucle fermée, pioche et défausse au centre). La fonction refuse une case de moins de 2,5 cm, des cases rondes qui se chevauchent et une case d'accueil de cartes trop petite (`verifier_case_piece`, MP-J-10) ; elle renvoie le chemin du PDF, le nombre de cases et la plus petite dimension d'une case. Le bloc se place à la fin du module, après `verifier_case_piece`.

**Test (19.11.2026)** : quatre plateaux produits et regardés sur le rendu PDF : serpent 34 cases (29,3 mm), escargot 27 cases (25,0 mm), chemin 34 cases (27,0 mm), circuit 24 cases (31,0 mm) ; essai fait avec la police Liberation Sans à la place d'Arial ; non imprimé, non testé en classe.

```
# ---------- J5 : plateaux de parcours (19.11.2026) — serpent, escargot, chemin, circuit ----------
PLATEAU_MM = (12.0, 16.5, 186.0, 264.0)        # x0, y0, largeur, hauteur : surface utile A4 portrait (MP-J-11)
CASE_MIN_MM = 25.0                             # plus petite dimension d'une case : un pion y tient
CARTE_DEFI_MM = (62.0, 66.0)                   # carte-défi au format J2

def _mot_ou_numero(d, x, y, i, n, boucle, taille_pt, speciale=False, mots=0.8):
    """Départ et Arrivée en mots, les autres cases numérotées de 1 à n - 2 (circuit : de 1 à n - 1).
    Case spéciale : numéro entouré, en plus du fond gris (jamais la teinte seule, MP-C-05)."""
    mot = 'Départ' if i == 0 else ('Arrivée' if i == n - 1 and not boucle else str(i))
    t = taille_pt if mot.isdigit() else max(taille_pt * mots, 11)             # « Départ », « Arrivée » : presque le corps des numéros
    d.texte(x, y + t * 0.125, mot, t, police='Arial-B')
    if speciale:
        d.cercle(x, y, taille_pt * 0.32, ep=0.8)

def _ruban(d, cases, colonnes, rangees, boucle, speciales, taille_pt):
    """Cases carrées qui se suivent sur une grille : contour du ruban en trait épais, séparation de deux
    cases qui se suivent en trait fin. Renvoie les rectangles (x, y, l, h) dans l'ordre du parcours."""
    x0, y0, L, H = PLATEAU_MM; l, h = L / colonnes, H / rangees
    n = len(cases); rang = {c: i for i, c in enumerate(cases)}
    for (c, r), i in rang.items():
        x, y = x0 + c * l, y0 + r * h
        if i in speciales:
            d.ligne([(x, y), (x + l, y), (x + l, y + h), (x, y + h)], ep=0, ferme=True, fond=(0.85, 0.85, 0.85))
    for (c, r), i in rang.items():
        x, y = x0 + c * l, y0 + r * h
        for (dc, dr), a, b in (((0, -1), (x, y), (x + l, y)), ((1, 0), (x + l, y), (x + l, y + h)),
                               ((0, 1), (x, y + h), (x + l, y + h)), ((-1, 0), (x, y), (x, y + h))):
            j = rang.get((c + dc, r + dr))
            suite = j is not None and (abs(i - j) == 1 or (boucle and abs(i - j) == n - 1))
            if not suite or j > i:
                d.ligne([a, b], ep=0.35 if suite else 1.4)
        _mot_ou_numero(d, x + l / 2, y + h / 2, i, n, boucle, taille_pt, i in speciales, mots=min(0.95, 0.82 * l / d.largeur_texte('Arrivée', taille_pt, 'Arial-B')))
    return [(x0 + c * l, y0 + r * h, l, h) for c, r in cases]

def _logement(d, x, y, mot):
    """Case d'accueil d'une pile de cartes-défis : carte + 0,5 cm par côté (MP-J-10), en tirets."""
    l, h = CARTE_DEFI_MM[0] + 10, CARTE_DEFI_MM[1] + 10
    verifier_case_piece((CARTE_DEFI_MM[0] / 10, CARTE_DEFI_MM[1] / 10), (l / 10, h / 10), nom=mot)
    d.ligne([(x, y), (x + l, y), (x + l, y + h), (x, y + h)], ep=0.5, tirets=(2, 1.5), ferme=True)
    d.texte(x + l / 2, y + h / 2 + 2, mot, 16)
    return l, h

def plateau_parcours(base, forme='serpent', titre='', speciales=(), colonnes=6, rangees=None, bande_mm=25.0,
                     diametre_mm=27.0, rangs=6, taille_pt=22, case_min_mm=CASE_MIN_MM, long_mm=31.0, dessin=None):
    """J5 : plateau de parcours d'une page A4 portrait, sur toute la surface utile, sans tableau.
    forme = 'serpent'  : ruban de cases en lacets, une case de liaison à chaque virage (J5-a) ;
            'escargot' : spirale ronde vers le centre, pioche et défausse en haut de la page (J5-b) ;
            'chemin'   : cases rondes (« pas japonais ») le long d'un chemin en lacets (J5-c) ;
            'circuit'  : boucle fermée au bord de la page, pioche et défausse au centre (J5-d).
    speciales : numéros des cases grisées au numéro entouré (« rejoue », « recule » : sens donné par la règle).
    case_min_mm : 25 par défaut ; 20 pour des jetons, au secondaire. long_mm : longueur d'une case de l'escargot.
    dessin : si un Dessin est fourni, le plateau y est tracé et aucun fichier n'est écrit (miniatures).
    Écrit base.svg et base.pdf ; renvoie (chemin du PDF, nombre de cases, plus petite dimension
    d'une case en mm)."""
    x0, y0, L, H = PLATEAU_MM; d = dessin or Dessin(); speciales = set(speciales)
    if forme in ('serpent', 'circuit'):
        if forme == 'serpent':
            rangees = rangees or 9; assert rangees % 2 == 1, 'serpent : nombre impair de rangées'
            cases = []
            for r in range(rangees):
                if r % 2 == 0:
                    cs = list(range(colonnes)); cases += [(c, r) for c in (cs if r % 4 == 0 else cs[::-1])]
                else:
                    cases.append((colonnes - 1 if r % 4 == 1 else 0, r))
        else:
            rangees = rangees or 8
            cases = ([(c, 0) for c in range(colonnes)] + [(colonnes - 1, r) for r in range(1, rangees)] +
                     [(c, rangees - 1) for c in range(colonnes - 2, -1, -1)] +
                     [(0, r) for r in range(rangees - 2, 0, -1)])
            lg, hg = CARTE_DEFI_MM[0] + 10, CARTE_DEFI_MM[1] + 10
            e = (H - 2 * H / rangees - 2 * hg) / 3
            assert e >= 5 and L - 2 * L / colonnes >= lg + 10, 'circuit : centre trop petit pour les deux piles'
            for k, mot in enumerate(('Pioche', 'Défausse')):
                _logement(d, x0 + (L - lg) / 2, y0 + H / rangees + e + k * (hg + e), mot)
        rects = _ruban(d, cases, colonnes, rangees, forme == 'circuit', speciales, taille_pt)
        n, mini = len(cases), min(rects[0][2], rects[0][3])
    elif forme == 'escargot':
        lg, hg = CARTE_DEFI_MM[0] + 10, CARTE_DEFI_MM[1] + 10; r0 = 20.0
        R = (H - hg - 2 + bande_mm / 2) / 2                                 # spirale sous les piles, centrée
        cx, cy = x0 + L / 2 + bande_mm / 4, y0 + H - R
        T = 2 * math.pi * (R - bande_mm - r0) / bande_mm                    # angle total de la bande
        rext = lambda t: R - bande_mm * t / (2 * math.pi)                   # bord extérieur ; intérieur = rext - bande
        pt = lambda r, t: (cx - r * math.sin(t), cy + r * math.cos(t))      # départ en bas, sens horaire
        pas = 400; ts = [T * i / pas for i in range(pas + 1)]
        cum = [0.0]
        for a, b in zip(ts, ts[1:]):
            cum.append(cum[-1] + (rext((a + b) / 2) - bande_mm / 2) * (b - a))
        n = round(cum[-1] / long_mm); coupes = [0.0]
        for i in range(1, n):
            cible = cum[-1] * i / n; j = next(k for k, v in enumerate(cum) if v >= cible); coupes.append(ts[j])
        coupes.append(T)
        for i in range(n):
            a, b = coupes[i], coupes[i + 1]; arc = [a + (b - a) * k / 20 for k in range(21)]
            if i in speciales:
                d.ligne([pt(rext(t), t) for t in arc] + [pt(rext(t) - bande_mm, t) for t in arc[::-1]],
                        ep=0, ferme=True, fond=(0.85, 0.85, 0.85))
        d.ligne([pt(rext(t), t) for t in ts], ep=1.4); d.ligne([pt(rext(t) - bande_mm, t) for t in ts], ep=1.4)
        for i, t in enumerate(coupes):
            d.ligne([pt(rext(t), t), pt(rext(t) - bande_mm, t)], ep=1.4 if i in (0, n) else 0.35)
        for i in range(n):
            t = (coupes[i] + coupes[i + 1]) / 2; x, y = pt(rext(t) - bande_mm / 2, t)
            _mot_ou_numero(d, x, y, i, n + 1, False, taille_pt, i in speciales)
        d.texte(cx, cy + 2 + taille_pt * 0.1, 'Arrivée', max(16, taille_pt * 1.2), police='Arial-B')
        _logement(d, x0, y0, 'Pioche'); _logement(d, x0 + L - lg, y0, 'Défausse')
        for xc in (x0 + lg, x0 + L - lg):                                   # coins des piles hors de la spirale
            t = math.atan2(cx - xc, y0 + hg - cy) % (2 * math.pi)
            assert math.hypot(cx - xc, cy - y0 - hg) >= rext(t) + 2, 'escargot : une pile touche la spirale'
        mini = min(bande_mm, cum[-1] / n); n += 1                           # longueur mesurée au milieu de la bande
    elif forme == 'chemin':
        r = diametre_mm / 2; R = (H - diametre_mm) / (2 * (rangs - 1))       # rayon des virages
        xa, xb = x0 + r + R, x0 + L - r - R; axe = []                        # ligne médiane du chemin
        for k in range(rangs):
            y = y0 + r + 2 * R * k; va = k % 2 == 0
            axe += [(xa, y), (xb, y)] if va else [(xb, y), (xa, y)]
            if k < rangs - 1:
                c = xb if va else xa
                axe += [(c + (R if va else -R) * math.sin(math.radians(a)), y + R - R * math.cos(math.radians(a)))
                        for a in range(10, 180, 10)]
        cum = [0.0]
        for a, b in zip(axe, axe[1:]):
            cum.append(cum[-1] + math.hypot(b[0] - a[0], b[1] - a[1]))
        n = int(cum[-1] // (diametre_mm + 4)) + 1; pas = cum[-1] / (n - 1); centres = []
        for i in range(n):
            s = min(pas * i, cum[-1] - 1e-6); j = next(k for k in range(len(cum) - 1) if cum[k + 1] >= s)
            f = (s - cum[j]) / (cum[j + 1] - cum[j])
            (xa_, ya_), (xb_, yb_) = axe[j], axe[j + 1]
            centres.append((xa_ + f * (xb_ - xa_), ya_ + f * (yb_ - ya_)))
        d.ligne(axe, ep=0.8, tirets=(2, 2))
        for i, (x, y) in enumerate(centres):
            d.cercle(x, y, r, ep=1.2, fond=(0.85, 0.85, 0.85) if i in speciales else (1, 1, 1))
            _mot_ou_numero(d, x, y, i, n, False, taille_pt * 0.9, i in speciales)
        ecart = min(math.hypot(a[0] - b[0], a[1] - b[1]) for i, a in enumerate(centres) for b in centres[i + 1:])
        mini = min(diametre_mm, ecart)
        assert mini >= diametre_mm - 0.01, 'chemin : deux cases se chevauchent ; réduire rangs ou diametre_mm'
    else:
        raise ValueError(forme)
    assert mini >= case_min_mm, f'cases de {mini:.1f} mm : trop petites pour un pion (minimum {case_min_mm} mm)'
    if titre:
        d.texte(105, 11.5, titre, 10)
    return (None if dessin else d.sauver(base)), n, round(mini, 1)
```

#### 19 novembre 2026 : planches à découper en PDF (MP-J-11, MP-J-12)

`planche_pdf` produit une planche de pièces en PDF avec la classe `Dessin` (R11) : colonnes × rangées de pièces sur toute la surface utile (18,6 × 26,4 cm), contours en pointillés, séparation interne des dominos en trait plein épais, repères de coupe dans les quatre marges, mention dans la marge du haut. Le texte est centré ; s'il est trop large, le corps diminue jusqu'au minimum demandé, puis la planche est refusée. `dimensions_piece` donne la taille d'une pièce pour un nombre de colonnes et de rangées ; `reperes_de_coupe` pose les repères sur n'importe quel `Dessin`. Le bloc se place après `Dessin` et `melanger_sans_voisins`.

**Test (19.11.2026)** : J1, boucle Lune, 2 × 8 dominos de 9,3 × 3,3 cm (corps de 19,5 pt), ordre mélangé ; dispositions J3 (3 × 3 cartes de 6,2 × 8,8 cm) et J4 (2 × 4 cartes de 9,3 × 6,6 cm) ; un texte trop long est refusé ; rendus PDF regardés, police Liberation Sans à la place d'Arial ; non imprimé, non testé en classe.

```
# ---------- MP-J-11 et MP-J-12 : planche de pièces en PDF, toute la page, repères de coupe (19.11.2026) ----------
SURFACE_MM = (12.0, 16.5, 186.0, 264.0)        # x0, y0, largeur, hauteur : surface utile A4 portrait (MP-J-11)

def dimensions_piece(colonnes, rangees):
    """MP-J-11 : largeur et hauteur d'une pièce (cm) quand colonnes × rangees pièces remplissent la page."""
    return round(SURFACE_MM[2] / colonnes / 10, 2), round(SURFACE_MM[3] / rangees / 10, 2)

def reperes_de_coupe(d, xs, ys, long_mm=4.5, ecart_mm=2.5):
    """MP-J-12 : un trait fin (0,5 pt) dans le prolongement de chaque ligne de coupe, dans les quatre marges.
    xs : abscisses des coupes verticales ; ys : ordonnées des coupes horizontales (mm)."""
    x0, y0, L, H = SURFACE_MM; ep = 0.5 * 25.4 / 72
    assert min(x0, y0) - ecart_mm - long_mm >= 5, 'repères hors de la zone imprimable'
    for x in xs:
        d.ligne([(x, y0 - ecart_mm - long_mm), (x, y0 - ecart_mm)], ep=ep)
        d.ligne([(x, y0 + H + ecart_mm), (x, y0 + H + ecart_mm + long_mm)], ep=ep)
    for y in ys:
        d.ligne([(x0 - ecart_mm - long_mm, y), (x0 - ecart_mm, y)], ep=ep)
        d.ligne([(x0 + L + ecart_mm, y), (x0 + L + ecart_mm + long_mm, y)], ep=ep)

def planche_pdf(base, pieces, colonnes, rangees, mention='', taille_pt=16, taille_min_pt=12, gras_gauche=True,
                dessin=None, lisere=False):
    """R8 en PDF : colonnes × rangees pièces sur toute la surface utile (MP-J-11), contour en pointillés
    (MP-J-05), repères de coupe (MP-J-12), mention dans la marge du haut.
    pieces : une chaîne par pièce (lignes séparées par '\\n'), ou un couple (moitié gauche, moitié droite)
    pour un domino : séparation interne en trait plein épais, moitié gauche en gras (la réponse).
    Le texte est centré dans sa pièce ou sa moitié ; s'il est trop large, le corps diminue jusqu'à
    taille_min_pt, puis la planche est refusée. Une planche par appel ; l'ordre des pièces est celui reçu
    (à mélanger avant : melanger_sans_voisins, MP-J-03 ; verso : verso_de, R12).
    dessin : si un Dessin est fourni, la planche y est tracée et aucun fichier n'est écrit (miniatures).
    lisere=True pour un jeu de cartes (MP-J-14) : cadre aux coins arrondis à 3 mm du trait de coupe, tracé avant
    le texte (lisere_cartes) ; le texte reste à l'intérieur du cadre. Pas de liseré pour un domino ni un puzzle.
    Écrit base.svg et base.pdf ; renvoie (chemin du PDF, largeur et hauteur d'une pièce en cm, corps utilisé)."""
    x0, y0, L, H = SURFACE_MM; l, h = L / colonnes, H / rangees; jeu = 10 if lisere else 6
    assert len(pieces) <= colonnes * rangees, 'trop de pièces pour une planche'
    d = dessin or Dessin(); moities = [p if isinstance(p, (tuple, list)) else (p,) for p in pieces]
    corps = taille_pt
    while True:                                                             # même corps pour toute la planche
        trop = [t for m in moities for k, bloc in enumerate(m) for t in bloc.split('\n')
                if d.largeur_texte(t, corps, 'Arial-B' if len(m) == 2 and k == 0 and gras_gauche else 'Arial')
                > l / len(m) - jeu]
        if not trop: break
        corps -= 0.5
        assert corps >= taille_min_pt, f'texte trop long pour la pièce : {trop[0]!r}'
    if lisere: lisere_cartes(d, colonnes, rangees)                         # MP-J-14, sous le texte
    for i, m in enumerate(moities):
        x, y = x0 + (i % colonnes) * l, y0 + (i // colonnes) * h; lm = l / len(m)
        for k, bloc in enumerate(m):
            lignes = bloc.split('\n'); pas = corps * 1.25 * 25.4 / 72
            yb = y + h / 2 - (len(lignes) - 1) * pas / 2 + corps * 0.125
            for j, t in enumerate(lignes):
                d.texte(x + lm * (k + 0.5), yb + j * pas, t, corps,
                        police='Arial-B' if len(m) == 2 and k == 0 and gras_gauche else 'Arial')
            if k:
                d.ligne([(x + lm * k, y), (x + lm * k, y + h)], ep=0.8)       # séparation interne : 2,25 pt
    xs = [x0 + c * l for c in range(colonnes + 1)]; ys = [y0 + r * h for r in range(rangees + 1)]
    for x in xs:
        d.ligne([(x, y0), (x, y0 + H)], ep=0.35, tirets=(1, 1.2))            # traits de coupe : 1 pt, pointillés
    for y in ys:
        d.ligne([(x0, y), (x0 + L, y)], ep=0.35, tirets=(1, 1.2))
    reperes_de_coupe(d, xs, ys)
    if mention:
        assert d.largeur_texte(mention, 8) <= L - 10, 'mention trop longue'
        d.texte(105, 8.0, mention, 8)                                       # marge du haut, au-dessus des repères
    return (None if dessin else d.sauver(base)), (round(l / 10, 2), round(h / 10, 2)), corps
```

#### 19 novembre 2026 : panorama des jeux (MP-J-13)

`panorama_jeux` dessine avec la classe `Dessin` (R11) une image A4 paysage qui présente les jeux disponibles **uniquement par des miniatures tirées des documents réels** : la page du modèle Word ou de la planche prête à imprimer est insérée telle quelle, réduite (`show_pdf_page`), avec le nom, l'usage et la page du document (sans code depuis le 21.11.2026). La table `SOURCES_JEUX` donne, pour chaque gabarit, le document de la boîte à outils, la page de chaque tranche d'âge et le nombre de pièces par planche ; un gabarit sans document est cité dans une liste, sans image (20.11.2026). `miniatures_tranche` compose de la même façon la page d'une tranche d'âge (fonction commune `_page_miniatures`). L'IA l'affiche avant de proposer un jeu, ou quand on lui demande quelles sont les possibilités (MP-J-13). Les listes `JEUX` et `SOURCES_JEUX` se complètent à chaque nouveau gabarit ou nouveau document ; un modèle Word est converti en PDF avant l'appel. `panorama_exercices` fait de même pour les gabarits d'exercice G1 à G23 (liste `EXERCICES`, schémas dans `_vignette_exercice`) : l'IA l'affiche quand on lui demande quels exercices sont possibles. Le bloc se place après `Dessin` et `arc_pts`.

**Test (19.11.2026)** : images produites à partir du code de cette annexe et regardées (panorama des jeux, 20.11.2026 : 41 miniatures de documents réels, aucun gabarit en liste ; pages par tranche d'âge : 38 à 40 miniatures ; panorama des exercices : 23 gabarits, en schémas ; textes sans débordement) ; police Liberation Sans à la place d'Arial ; affichage par une IA dans une conversation : non testé.

```
# ---------- MP-J-13 : panorama des jeux, image à montrer avant de choisir (19.11.2026) ----------
JEUX = [('J1', 'Domino-boucle', 'question et réponse, en boucle'), ('J2', 'Memory, appariement', 'associer deux éléments'),
        ('J3', 'Familles', 'classer par catégorie'), ('J4', 'Cartes recto-verso', 'rappel : question, puis réponse'),
        ('J5-a', 'Plateau · serpent', 'parcours avec cartes-défis'), ('J5-b', 'Plateau · escargot', 'jeu de l\'oie, arrivée au centre'),
        ('J5-c', 'Plateau · chemin', 'parcours de cases rondes'), ('J5-d', 'Plateau · circuit', 'boucle, partie en plusieurs tours'),
        ('J6', 'Dé à monter', 'tirer un élément au hasard'), ('J7', 'Loto', 'on entend ou on lit, on couvre'),
        ('J8', 'Symboles communs', 'trouver vite l\'élément commun'), ('J9', 'Trouve quelqu\'un qui…', 'questionner ses camarades'),
        ('J10', 'Carte à pinces', 'choisir, puis se corriger au verso'), ('J11', 'Roue à fenêtre et rabat', 'réponse sous le rabat'),
        ('J12', 'Lettres à fabriquer', 'tracer avec le doigt'), ('J13', 'Cartes de rôle', 'un rôle dans le groupe'),
        ('J14', 'Cartes d\'erreurs', 'analyser une démarche'), ('J15', 'Cartes d\'aide graduée', 'se donner un coup de pouce'),
        ('J16', 'Cartons-réponses', 'voter sans écran'), ('J17', 'Grille d\'alignement', 'répondre pour aligner ses jetons'),
        ('J18', 'Serpents et échelles', 'monter si l\'on répond juste'), ('J19', 'Bataille navale', 'croiser une colonne et une ligne'),
        ('J20', 'Roue de tirage', 'tirer au sort sans dé'), ('J21', 'Puzzles à deux pièces', 'associer : la découpe corrige'),
        ('J22', 'Puzzle à bandes', 'ranger pour reformer l\'image'), ('J23', 'Mot mystère', 'des définitions, un mot caché'),
        ('J24', 'Cocotte en papier', 'se poser des défis à deux'), ('J25', 'Horloge à aiguilles', 'lire et régler l\'heure'),
        ('J26', 'Mémo-fiches en éventail', 'réviser, fiche après fiche'), ('J27', 'Bandes graphiques', 'repasser un tracé au feutre'),
        ('J28', 'Plateau à camemberts', 'quiz à six catégories'), ('J29', 'Cherche et trouve', 'repérer vite un mot qui convient'),
        ('J30', 'Mots interdits', 'faire deviner sans dire'), ('J31', 'Petit bac', 'un mot par catégorie et par lettre'),
        ('J32', 'Cartes à terminaisons', 'compléter la phrase tirée'), ('J33', 'Petits chevaux', 'avancer en répondant'),
        ('J34', 'Qui est-ce ?', 'questionner par oui ou par non'), ('J35', 'Bataille', 'comparer deux cartes'),
        ('J36', 'Tuiles-lettres', 'composer des mots'), ('J37', 'Sudoku', 'raisonner par élimination'),
        ('J38', 'Mot caché : la fleur', 'deviner un mot, lettre après lettre')]

_J5 = 'J5 — Plateaux de parcours (serpent, escargot, chemin, circuit) — 1P-4P, 5P-8P, 9S-11S'
_DE = ('Dé à monter — grand dé (faces de 6 cm, chiffres)', 'Dé à monter — deux petits dés (faces de 4,2 cm, chiffres)')
# code : (document de la boîte à outils, ou un document par tranche ; page de chaque tranche 1P-4P, 5P-8P, 9S-11S,
#         None si le gabarit n'est pas proposé à cet âge ; unité ; nombre par planche pour chaque tranche)
SOURCES_JEUX = {
    'J1': ('Modèle J1 — dominos', (2, 3, 4), 'dominos', (10, 16, 20)),
    'J2': ('Modèle J2 — memory, paires question-réponse (dos à motif)', (3, 5, 7), 'cartes', (6, 12, 20)),
    'J3': ('Modèle J3 — familles', (2, 3, 4), 'cartes', (6, 9, 16)),
    'J4': ('Modèle J4 — cartes de rappel (recto-verso)', (2, 4, 6), 'cartes', (6, 8, 15)),
    'J5-a': (_J5, (1, 5, 9), 'cases', (19, 34, 53)), 'J5-b': (_J5, (2, 6, 10), 'cases', (15, 27, 42)),
    'J5-c': (_J5, (3, 7, 11), 'cases', (21, 34, 55)), 'J5-d': (_J5, (4, 8, 12), 'cases', (16, 24, 34)),
    'J6': ((_DE[0], _DE[1], _DE[1]), (1, 1, 1), 'dés', (1, 2, 2)),
    'J7': ('Modèle J7 — loto, cartons et cartes d’appel (dos à motif, feuille de contrôle)', (4, 7, 12), 'cartons', (6, 8, 6)),
    'J8': ('Modèle J8 — symboles communs', (2, 3, 4), 'cartes', (7, 13, 21)),
    'J9': ('Modèle J9 — grille « Trouve quelqu’un qui… »', (2, 3, 4), 'cases', (6, 16, 25)),
    'J10': ('Modèle J10 — carte à pinces (recto-verso)', (2, 4, 6), 'questions', (6, 10, 12)),
    'J11': ('J11 — Roue à fenêtre et rabat (exemples à 4, 6 et 8 secteurs)', (1, 2, 3), 'secteurs', (4, 6, 8)),
    'J12': ('Modèle J12 — lettres à fabriquer', (2, None, None), 'plaques', (4, None, None)),
    'J13': ('Modèle J13 — cartes de rôle', (2, 3, 4), 'cartes', (4, 8, 8)),
    'J14': ('Modèle J14 — cartes d’erreurs (recto-verso)', (None, 2, 4), 'cartes', (None, 4, 6)),
    'J15': ('Modèle J15 — cartes d’aide graduée', (2, 3, 4), 'cartes', (4, 8, 8)),
    'J16': ('Modèle J16 — cartons-réponses', (2, 3, 4), 'cartons', (4, 4, 6)),
    'J17': ('J17 — Grille d’alignement (nombres) — 1P-4P, 5P-8P, 9S-11S', (1, 2, 3), 'ronds', (20, 35, 48)),
    'J18': ('J18 — Serpents et échelles — 1P-4P, 5P-8P, 9S-11S', (1, 2, 3), 'cases', (30, 48, 80)),
    'J19': ('J19 — Bataille navale (lettres et nombres) — 1P-4P, 5P-8P, 9S-11S', (1, 2, 3), 'cases par grille', (25, 36, 64)),
    'J20': ('J20 — Roue de tirage (nombres) — 4, 6 et 8 secteurs', (1, 2, 3), 'secteurs', (4, 6, 8)),
    'J21': ('J21 — Puzzles à deux pièces (exemples) — 1P-4P, 5P-8P, 9S-11S', (1, 2, 3), 'puzzles', (8, 12, 18)),
    'J22': ('J22 — Puzzle à bandes (exemples) — 5, 10 et 12 bandes', (1, 2, 3), 'bandes', (5, 10, 12)),
    'J23': ('J23 — Mot mystère (exemples) — 1P-4P, 5P-8P, 9S-11S', (1, 2, 3), 'mots', (4, 6, 8)),
    'J24': ('J24 — Cocotte en papier (exemples) — 1P-4P, 5P-8P, 9S-11S', (1, 2, 3), 'défis', (8, 8, 8)),
    'J25': ('J25 — Horloge à aiguilles — heures, minutes, 24 heures', (1, 2, 3), 'graduations', (12, 60, 60)),
    'J26': ('J26 — Mémo-fiches en éventail (exemples) — 1P-4P, 5P-8P, 9S-11S', (1, 2, 3), 'fiches', (6, 8, 10)),
    'J27': ('J27 — Bandes graphiques — 4, 6 et 8 bandes', (1, 2, 3), 'bandes', (4, 6, 8)),
    'J28': ('J28 — Plateau à camemberts — 1P-4P, 5P-8P, 9S-11S', (1, 2, 3), 'cases', (37, 49, 73)),
    'J29': ('J29 — Cherche et trouve de mots (exemples) — 1P-4P, 5P-8P, 9S-11S', (1, 2, 3), 'mots', (20, 38, 66)),
    'J30': ('J30 — Mots interdits (exemples) — 5P-8P, 9S-11S', (None, 1, 2), 'cartes', (None, 9, 12)),
    'J31': ('J31 — Petit bac — 1P-4P, 5P-8P, 9S-11S', (1, 2, 3), 'cases à remplir', (12, 30, 48)),
    'J32': ('J32 — Cartes à terminaisons (exemple 5P-8P, avec solutions)', (None, 1, None), 'cartes-phrases', (None, 12, None)),
    'J33': ('J33 — Petits chevaux', (1, 1, 1), 'cases', (52, 52, 52)),
    'J34': ('J34 — Qui est-ce (nombres) — 1P-4P, 5P-8P, 9S-11S', (1, 2, 3), 'éléments', (12, 24, 30)),
    'J35': ('J35 — Bataille (exemples) — 1P-4P, 5P-8P, 9S-11S', (1, 2, 3), 'cartes', (12, 16, 20)),
    'J36': ('J36 — Tuiles-lettres — 48, 117 et 204 tuiles', (1, 2, 3), 'tuiles', (48, 117, 204)),
    'J37': ('J37 — Sudoku — 4 × 4, 6 × 6, 9 × 9, avec solutions', (1, 2, 3), 'grilles', (4, 2, 2)),
    'J38': ('J38 — Mot caché, la fleur', (1, 1, 1), 'parties', (3, 3, 3))}

def _page_miniatures(base, titres, entrees, dossier, dpi, sources=None):
    """Page A4 portrait de miniatures. Chaque miniature est la page du document réel, insérée telle quelle et réduite
    (jamais un schéma). entrees : liste de (code, nom, ligne 2, tranche). Écrit base.pdf et base.png ; renvoie le PNG."""
    import os
    d = Dessin(); m = 8; col = 5 if len(entrees) < 25 else 6 if len(entrees) < 36 else 7       # 5 × 5, 6 × 6 ou 7 × 7 miniatures
    k = {5: 0.14, 6: 0.115, 7: 0.097}[col]
    l, h = (210 - 2 * m) / col, (297 - 2 * m) / col
    d.texte(m + l / 2, m + 14, titres[0], {5: 13, 6: 11, 7: 9.5}[col], police='Arial-B')
    for j, t in enumerate(titres[1:]): d.texte(m + l / 2, m + 21 + j * (4.3 if col < 7 else 3.4), t, {5: 7.5, 6: 6.2, 7: 5.2}[col])
    sans = []; ouverts = {}
    for code, nom, ligne2, tranche in entrees:
        doc, pages, unite, nombres = (sources or SOURCES_JEUX).get(code, (None, (None,) * 3, '', ()))
        if doc is None or pages[tranche - 1] is None: sans.append(nom); continue
        i = len([1 for e in entrees[:entrees.index((code, nom, ligne2, tranche))] if e[1] not in sans]) + 1
        x, y = m + (i % col) * l, m + (i // col) * h; mx, my = x + (l - 210 * k) / 2, y + 1.5
        doc = doc if isinstance(doc, str) else doc[tranche - 1]; page = pages[tranche - 1]
        src = ouverts.setdefault(doc, d.f.open(os.path.join(dossier, doc + '.pdf'))); r = src[page - 1].rect; w, t = r.width / d.k * k, r.height / d.k * k
        ox, oy = mx + (210 * k - w) / 2, my + (297 * k - t) / 2
        d.p.show_pdf_page(d.f.Rect(ox * d.k, oy * d.k, (ox + w) * d.k, (oy + t) * d.k), src, page - 1)
        d.ligne([(mx, my), (mx + 210 * k, my), (mx + 210 * k, my + 297 * k), (mx, my + 297 * k)], ep=0.25, ferme=True)
        by = my + 297 * k; lignes = ((nom, 7.2 if col < 7 else 6.2, 'Arial-B'), (ligne2 or f'{nombres[tranche - 1]} {unite}'.replace('1 dés', '1 dé'), 6.4, 'Arial'),
                                    (('modèle Word' if doc.startswith('Modèle') else 'planche PDF') + f' · page {page}', 5.6, 'Arial'))
        for j, (t, c, pol) in enumerate(lignes):
            while d.largeur_texte(t, c, pol) > l - 1.5: c -= 0.2; assert c >= 4.5, t
            d.texte(x + l / 2, by + (3.4 if col < 7 else 3.0) + j * {5: 3.3, 6: 2.9, 7: 2.5}[col], t, c, police=pol)
    if sans:                                                                # sans document : une liste, jamais d'image
        d.texte(m + 2, m + 40, 'Sans document prêt :', 7, ancre='s', police='Arial-B')
        for j, t in enumerate(sans): d.texte(m + 2, m + 44 + j * 3.3, t, 6.2, ancre='s')
    d.d.save(base + '.pdf', garbage=4, deflate=True)
    return d.png(base, dpi)

def panorama_jeux(base, dossier, dpi=200):
    """MP-J-13 : image à afficher avant de choisir un jeu. Elle ne contient que des miniatures tirées des documents
    réels de la boîte à outils (SOURCES_JEUX), au format 5P-8P (ou, à défaut, au premier format existant) :
    l'enseignant·e obtient ce qu'il ou elle voit. dossier : dossier où ces documents se trouvent en PDF (un modèle
    Word y est d'abord converti en PDF, sans rien changer)."""
    def tr(code):
        pages = SOURCES_JEUX.get(code, (None, (None,) * 3))[1]
        return 2 if pages[1] is not None else next((t for t in (1, 3) if pages[t - 1] is not None), 2)
    return _page_miniatures(base, ('Jeux imprimés', 'Chaque miniature est une page', 'du document réel, réduite.', 'Dites le nom', 'du jeu choisi.'),
                            [(c, n, u, tr(c)) for c, n, u in JEUX], dossier, dpi)

SUPPORTS = [('G22', 'Lignes d\'écriture romandes', 'pages de 7, 4 et 2,5 mm'), ('G23', 'Syllabes et sons', 'image, syllabes, sons'),
            ('G24', 'Maisons des nombres', 'décomposer un nombre'), ('G25', 'Reproduction sur quadrillage', 'tracer la même figure'),
            ('G26', 'Calendrier mensuel', 'un mois, lundi à dimanche'), ('G27', 'Étiquettes de l\'horaire', 'afficher la journée'),
            ('G28', 'Livret à onglets', 'une feuille par onglet'), ('G29', 'Page de journal', 'articles sur deux colonnes'),
            ('G30', 'Planche de BD', 'cases vides à dessiner'), ('G31', 'Plan d\'exposé', 'préparer sa présentation')]
SOURCES_SUPPORTS = {
    'G22': ('G22 — Lignes d’écriture, lignage romand — 7 mm, 4 mm et 2,5 mm', (1, 1, 1), '', ()),
    'G23': ('G23 — Syllabes et sons (exemples) — 8 et 12 mots', (2, 2, 2), '', ()),
    'G24': ('G24 — Maisons des nombres — 3 à 6, 7 à 10', (2, 2, 2), '', ()),
    'G25': ('G25 — Reproduction sur quadrillage — maison, bateau, sapin, fusée', (1, 1, 1), '', ()),
    'G26': ('G26 — Calendrier mensuel (exemples) — décembre 2026, janvier et février 2027', (1, 1, 1), '', ()),
    'G27': ('G27 — Étiquettes de l’horaire (exemple, 16 étiquettes)', (1, 1, 1), '', ()),
    'G28': ('G28 — Livret à onglets (exemple, livret de rentrée à 5 onglets)', (1, 1, 1), '', ()),
    'G29': ('G29 — Page de journal de classe — 3 et 4 articles', (1, 1, 1), '', ()),
    'G30': ('G30 — Planches de bande dessinée — 3, 7 et 10 cases', (2, 2, 2), '', ()),
    'G31': ('G31 — Plan d’exposé — 2 et 3 parties', (2, 2, 2), '', ())}

def panorama_supports(base, dossier, dpi=200):
    """Page des fiches et supports qui ont un document prêt à imprimer (G22 à G31) : miniatures tirées des documents
    réels, comme pour les jeux. Complète panorama_exercices, qui montre G1 à G23 en schémas."""
    return _page_miniatures(base, ('Fiches et supports', 'Chaque miniature est une page', 'du document réel, réduite.', 'Dites le nom', 'du support choisi.'),
                            [(c, n, u, 1) for c, n, u in SUPPORTS], dossier, dpi, SOURCES_SUPPORTS)

def miniatures_tranche(base, tranche, dossier, dpi=200):
    """Page des jeux proposés à une tranche d'âge (1 : 1P-4P ; 2 : 5P-8P ; 3 : 9S-11S) : pour chaque gabarit, la page
    réelle du format de cette tranche, réduite, avec le nombre de pièces, de cases ou de questions par planche."""
    noms = ('1P à 4P', '5P à 8P', '9S à 11S')
    return _page_miniatures(base, ('Jeux · ' + noms[tranche - 1], 'Chaque miniature est une page', 'du document réel, réduite.', 'Sous le nom : nombre de pièces,', 'de cases ou de questions.'),
                            [(c, n, None, tranche) for c, n, u in JEUX if SOURCES_JEUX[c][1][tranche - 1] is not None], dossier, dpi)


# ---------- Panorama des gabarits d'exercice G1 à G23 (19.11.2026) ----------
EXERCICES = [('G1', 'Entourer'), ('G2', 'Relier'), ('G3', 'Compléter'), ('G4', 'Transformer, recopier'), ('G5', 'Remettre en ordre'),
             ('G6', 'Cocher'), ('G7', 'Production courte guidée'), ('G8', 'Repérer dans un texte'), ('G9', 'Tableau à compléter'),
             ('G10', 'Image et écriture'), ('G11', 'Colorier selon une consigne'), ('G12', 'Classer en colonnes'), ('G13', 'Calcul posé'),
             ('G14', 'Chronologie'), ('G15', 'Copier puis illustrer'), ('G16', 'Recherche visuelle'), ('G17', 'Série chronométrée'),
             ('G18', 'Grille croisée de nombres'), ('G19', 'Tracé de chemin'), ('G20', 'Dictée réfléchie'), ('G21', 'Imagier, scène à légender'), ('G22', 'Lignes d\'écriture romandes'), ('G23', 'Syllabes et sons')]

def _vignette_exercice(d, code, x, y, l, h):
    """Schéma d'un gabarit d'exercice dans la boîte (x, y, l, h), en mm : des formes, aucun texte d'élève."""
    G = (0.82, 0.82, 0.82); N = (0.35, 0.35, 0.35); cx, cy = x + l / 2, y + h / 2
    def rect(a, b, w, t, ep=0.5, fond=None, tirets=None):
        d.ligne([(a, b), (a + w, b), (a + w, b + t), (a, b + t)], ep=ep, ferme=True, fond=fond, tirets=tirets)
    mot = lambda a, b, w: rect(a, b, w, 1.8, ep=0, fond=N)                   # un mot imprimé : barre sombre
    ligne = lambda a, b, w: d.ligne([(a, b), (a + w, b)], ep=0.35)          # une ligne d'écriture
    if code == 'G1':
        for i in range(5): rect(x + 4 + i * 7.5, cy - 2.5, 5, 5, fond=G if i == 3 else None)
        d.cercle(x + 4 + 3 * 7.5 + 2.5, cy, 5, ep=0.8)
    elif code == 'G2':
        for i in range(3): d.cercle(x + 8, y + 5 + i * 8.5, 1.3, ep=0, fond=N); d.cercle(x + l - 8, y + 5 + i * 8.5, 1.3, ep=0, fond=N); mot(x + 1, y + 4 + i * 8.5, 5); mot(x + l - 6, y + 4 + i * 8.5, 5)
        for a, b in ((0, 2), (1, 0), (2, 1)): d.ligne([(x + 8, y + 5 + a * 8.5), (x + l - 8, y + 5 + b * 8.5)], ep=0.6)
    elif code == 'G3':
        for j in range(3): mot(x + 3, y + 6 + j * 8, 9); ligne(x + 14, y + 7.8 + j * 8, 11); mot(x + 27, y + 6 + j * 8, 8)
    elif code == 'G4':
        mot(x + 3, y + 5, 10); mot(x + 15, y + 5, 7); mot(x + 24, y + 5, 9); d.ligne([(cx, y + 9.5), (cx, y + 14)], ep=0.8); d.ligne([(cx - 1.8, y + 12), (cx, y + 14.4), (cx + 1.8, y + 12)], ep=0.8)
        for j in range(2): ligne(x + 3, y + 19 + j * 5, l - 6)
    elif code == 'G5':
        for i, t in enumerate('312'): rect(x + 3 + i * 12, cy - 5, 10, 10, fond=(1, 1, 1)); d.texte(x + 8 + i * 12, cy + 2, t, 13, police='Arial-B')
    elif code == 'G6':
        for j in range(3): rect(x + 5, y + 4 + j * 8, 4, 4); mot(x + 12, y + 5.2 + j * 8, 14 + 3 * j)
        d.ligne([(x + 5.8, y + 14), (x + 6.9, y + 15.4), (x + 8.6, y + 12.6)], ep=0.9)
    elif code == 'G7':
        mot(x + 3, y + 5, 12); ligne(x + 17, y + 6.8, l - 20)
        for j in range(3): ligne(x + 3, y + 13 + j * 5.5, l - 6)
    elif code == 'G8':
        for j in range(4):
            for i, w in enumerate((8, 6, 10, 7)): mot(x + 3 + sum((8, 6, 10, 7)[:i]) + i * 1.6, y + 5 + j * 6, w)
        rect(x + 3 + 8 + 1.6 - 0.6, y + 5 + 6 - 1, 7.2, 3.8, ep=0.6); rect(x + 3 + 14 + 3.2 - 0.6, y + 5 + 18 - 1, 11.2, 3.8, ep=0.6)
    elif code == 'G9':
        for j in range(4):
            for i in range(3): rect(x + 4 + i * 11, y + 3 + j * 5.6, 11, 5.6, ep=0.4, fond=G if j == 0 else None)
    elif code in ('G10', 'G15'):
        a = x + 3 if code == 'G10' else x + l - 19; b = x + 22 if code == 'G10' else x + 3
        rect(a, y + 4, 16, 16, tirets=(1, 1) if code == 'G15' else None)
        if code == 'G10': d.ligne([(a + 2, y + 17), (a + 7, y + 9), (a + 10, y + 13), (a + 12, y + 11), (a + 15, y + 17)], ep=0.6); d.cercle(a + 12, y + 7.5, 1.5, ep=0.5)
        else: mot(b, y + 2.5, 14)
        for j in range(3): ligne(b, y + 9 + j * 5, l - 25)
    elif code == 'G11':
        for i in range(12): rect(x + 5 + (i % 4) * 8, y + 3 + (i // 4) * 7, 8, 7, ep=0.4, fond=(G if i in (1, 6, 8) else (0.6, 0.6, 0.6) if i in (3, 5, 10) else None))
    elif code == 'G12':
        for i in range(2):
            rect(x + 4 + i * 17, y + 2.5, 16, 5, fond=G); rect(x + 4 + i * 17, y + 7.5, 16, 17, ep=0.4)
            for j in range(2 + i): mot(x + 7 + i * 17, y + 11 + j * 4.5, 9)
    elif code == 'G13':
        for j, t in enumerate(('47', '25')): d.texte(cx + 2, y + 9 + j * 7, t, 15, police='Arial-B')
        d.texte(cx - 9, y + 16, '+', 15, police='Arial-B'); d.ligne([(cx - 12, y + 18.5), (cx + 9, y + 18.5)], ep=0.8); rect(cx - 6, y + 20, 14, 6, ep=0.4)
    elif code == 'G14':
        d.ligne([(x + 3, cy + 3), (x + l - 3, cy + 3)], ep=0.9); d.ligne([(x + l - 5.5, cy + 1), (x + l - 3, cy + 3), (x + l - 5.5, cy + 5)], ep=0.9)
        for i in range(4): d.ligne([(x + 7 + i * 9, cy + 1), (x + 7 + i * 9, cy + 5)], ep=0.6); rect(x + 3.5 + i * 9, cy - 8, 7, 6, ep=0.4)
    elif code == 'G16':
        alea = random.Random(7)
        for i in range(26):
            a, b = x + 3 + alea.random() * (l - 6), y + 3 + alea.random() * (h - 6)
            if i % 9 == 0: d.ligne([(a - 1.5, b + 1.3), (a, b - 1.5), (a + 1.5, b + 1.3)], ep=0.5, ferme=True, fond=N); d.cercle(a, b, 3, ep=0.6)
            else: d.cercle(a, b, 1.2, ep=0.4)
    elif code == 'G17':
        for i in range(2):
            for j in range(4): mot(x + 3 + i * 13, y + 5 + j * 5.5, 5); ligne(x + 9 + i * 13, y + 6.8 + j * 5.5, 5)
        d.cercle(x + l - 7, cy, 5, ep=0.7); d.ligne([(x + l - 7, cy), (x + l - 7, cy - 3.5)], ep=0.6); d.ligne([(x + l - 7, cy), (x + l - 4.8, cy + 1)], ep=0.6); rect(x + l - 8, cy - 7, 2, 1.6, ep=0, fond=N)
    elif code == 'G18':
        for i in range(20): rect(x + 6 + (i % 5) * 6, y + 2 + (i // 5) * 6, 6, 6, ep=0.4, fond=N if i in (2, 6, 13, 17) else None)
    elif code == 'G19':
        pts = [(x + 3 + t * (l - 8) / 30, cy + 7 * math.sin(t * 0.42)) for t in range(31)]
        for s in (-2.2, 2.2): d.ligne([(a, b + s) for a, b in pts], ep=0.5)
        d.ligne([(x + l - 7, pts[-1][1] - 2.5), (x + l - 3, pts[-1][1]), (x + l - 7, pts[-1][1] + 2.5)], ep=0.9)
    elif code == 'G20':
        d.ligne(arc_pts(x + 20, y + 5, 3, 0, 90, 5) + arc_pts(x + 20, y + 8, 3, 90, 180, 5) + [(x + 9, y + 11), (x + 6, y + 14), (x + 6.5, y + 11)] +
                arc_pts(x + 6, y + 8, 3, 180, 270, 5) + arc_pts(x + 6, y + 5, 3, 270, 360, 5), ep=0.6, ferme=True)
        mot(x + 6, y + 5.6, 13)
        for j in range(2): ligne(x + 3, y + 19 + j * 5, l - 6)
        d.cercle(x + l - 6, y + 7, 3.2, ep=0.6); d.texte(x + l - 6, y + 8.6, '?', 10, police='Arial-B')
    elif code == 'G23':
        for i in range(3):
            xx = x + 3 + i * 12.5; rect(xx, y + 2, 11, 23); rect(xx + 1.5, y + 3.5, 8, 8, ep=0.3, tirets=(0.8, 0.8)); mot(xx + 2, y + 13.5, 7)
            for q in range(2): rect(xx + 1.5 + q * 3.2, y + 17, 2.4, 2.4, ep=0.4)
            for q in range(3): d.cercle(xx + 2.6 + q * 3, y + 22.5, 1.1, ep=0.4)
    elif code == 'G22':
        for i in range(3):
            yy = y + 3 + i * 8.5
            for k, (ep, t) in enumerate(((0.25, (0.4, 0.9)), (0.25, None), (0.6, None), (0.25, (0.4, 0.9)))): d.ligne([(x + 2, yy + k * 2), (x + l - 2, yy + k * 2)], ep=ep, tirets=t)
    elif code == 'G21':
        rect(x + 3, y + 2.5, 20, 22); d.ligne([(x + 3, y + 18), (x + 23, y + 18)], ep=0.4); rect(x + 6, y + 10, 6, 8, ep=0.4); d.cercle(x + 18, y + 8, 2.2, ep=0.4)
        for i, (a, b) in enumerate(((x + 9, y + 12), (x + 18, y + 8), (x + 14, y + 20))): d.cercle(a, b, 1.8, ep=0.4, fond=(1, 1, 1)); d.texte(a, b + 1, str(i + 1), 5.5, police='Arial-B')
        for i in range(3): d.texte(x + 27, y + 8.5 + i * 6.5, str(i + 1), 7, police='Arial-B'); ligne(x + 30, y + 8.7 + i * 6.5, l - 33)

def panorama_exercices(base, dpi=150):
    """Image A4 paysage qui présente les gabarits d'exercice G1 à G23 : à afficher avant de composer une fiche, ou
    quand on demande quels exercices sont possibles. Écrit base.svg, base.pdf et base.png ; renvoie le chemin du PNG."""
    L, H, m, col, ran = 297, 210, 8, 6, 4; l, h = (L - 2 * m) / col, (H - 2 * m) / ran; d = Dessin(L, H)
    d.texte(m + l / 2, m + 16, 'Exercices', 16, police='Arial-B'); d.texte(m + l / 2, m + 23, 'les gabarits disponibles', 10)
    d.texte(m + l / 2, m + 33, 'Dites le nom', 9); d.texte(m + l / 2, m + 37.5, 'de l’exercice choisi.', 9)
    for i, (code, nom) in enumerate(EXERCICES, 1):
        x, y = m + (i % col) * l, m + (i // col) * h
        d.ligne([(x + 1.5, y + 1.5), (x + l - 1.5, y + 1.5), (x + l - 1.5, y + h - 1.5), (x + 1.5, y + h - 1.5)], ep=0.3, ferme=True)
        _vignette_exercice(d, code, x + 4, y + 4, l - 8, 27)
        d.texte(x + l / 2, y + 39, nom, 8.4, police='Arial-B')                  # nom seul, sans code (21.11.2026)
        assert d.largeur_texte(nom, 8.4, 'Arial-B') <= l - 6, code
    d.sauver(base)
    return d.png(base, dpi)
```

#### 19 novembre 2026 : dé à monter, grand ou petit (J6)

`de_a_monter` dessine le patron du dé avec la classe `Dessin` (R11) : croix de six faces, sept languettes de collage, contour en pointillés, plis en trait fin, textes centrés. `format='grand'` donne un dé à faces de 6 cm, seul sur la page ; `format='petit'`, deux dés à faces de 4,2 cm. Un texte trop large fait diminuer le corps jusqu'à 14 pt, puis le patron est refusé. Le bloc se place avant `VARIANTES`, qui l'utilise pour les miniatures.

**Test (19.11.2026)** : grand dé et petit dé produits en PDF et regardés (chiffres, puis pronoms sur une ou deux lignes) ; police Liberation Sans à la place d'Arial ; non imprimé, montage non réalisé.

```
# ---------- J6 : dé à monter, grand (un par page) ou petit (deux par page) (19.11.2026) ----------
def de_a_monter(base, faces=('1', '2', '3', '4', '5', '6'), format='grand', taille_pt=None, mention=True, dessin=None):
    """J6 : patron de cube en croix, avec languettes de collage, sur une page A4 portrait.
    format = 'grand' : faces de 6 cm, un dé par page (patron de 18 × 24,9 cm) ;
             'petit' : faces de 4,2 cm, deux dés identiques par page (patrons couchés de 17,5 × 12,6 cm).
    faces : six textes courts (haut de la colonne, bras gauche, centre, bras droit, puis les deux faces du bas).
    Contour à découper en pointillés (MP-J-05), plis en trait fin ; le texte est centré, son corps diminue
    s'il est trop large (minimum 14 pt). Écrit base.svg et base.pdf ; renvoie (chemin du PDF, côté d'une
    face en cm, nombre de dés sur la page)."""
    x0, y0, L, H = SURFACE_MM; d = dessin or Dessin(); grand = format == 'grand'
    c, lang = (60.0, 9.0) if grand else (42.0, 7.0); assert len(faces) == 6, 'un dé a six faces'
    croix = [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2), (1, 3)]
    languettes = {((1, 0), 'haut'), ((1, 0), 'gauche'), ((1, 0), 'droite'), ((1, 2), 'gauche'), ((1, 2), 'droite'),
                  ((1, 3), 'gauche'), ((1, 3), 'droite')}
    cotes = {'haut': ((0, 0), (1, 0), (0, -1)), 'bas': ((0, 1), (1, 1), (0, 1)),
             'gauche': ((0, 0), (0, 1), (-1, 0)), 'droite': ((1, 0), (1, 1), (1, 0))}
    if not grand:                                                           # patron couché : colonnes et rangées échangées
        croix = [(r, q) for q, r in croix]; tourne = {'haut': 'gauche', 'gauche': 'haut', 'droite': 'bas', 'bas': 'droite'}
        languettes = {((r, q), tourne[s]) for (q, r), s in languettes}
    corps = taille_pt or (48 if grand else 30)
    while max(d.largeur_texte(t, corps, 'Arial-B') for f in faces for t in f.split('\n')) > c - 8:
        corps -= 1; assert corps >= 14, 'texte trop long pour une face du dé'
    origines = ([(x0 + (L - 3 * c) / 2, y0 + (H - 4 * c - lang) / 2 + lang)] if grand else
                [(x0 + (L - 4 * c - lang) / 2 + lang, y0 + (H - 6 * c - 8) / 2 + k * (3 * c + 8)) for k in range(2)])
    for ox, oy in origines:
        for i, (q, r) in enumerate(croix):
            X, Y = ox + q * c, oy + r * c
            for nom, (a, b, n) in cotes.items():
                P, Q = (X + a[0] * c, Y + a[1] * c), (X + b[0] * c, Y + b[1] * c)
                if (q + n[0], r + n[1]) in croix:
                    d.ligne([P, Q], ep=0.25)                                 # pli entre deux faces
                elif ((q, r), nom) in languettes:
                    u = ((Q[0] - P[0]) / c, (Q[1] - P[1]) / c); d.ligne([P, Q], ep=0.25)
                    d.ligne([P, (P[0] + n[0] * lang + u[0] * lang, P[1] + n[1] * lang + u[1] * lang),
                             (Q[0] + n[0] * lang - u[0] * lang, Q[1] + n[1] * lang - u[1] * lang), Q], ep=0.35, tirets=(1, 1.2))
                else:
                    d.ligne([P, Q], ep=0.35, tirets=(1, 1.2))                # bord à découper
            lignes = faces[i].split('\n'); pas = corps * 1.2 * 25.4 / 72
            for j, t in enumerate(lignes):
                d.texte(X + c / 2, Y + c / 2 - (len(lignes) - 1) * pas / 2 + corps * 0.125 + j * pas, t, corps, police='Arial-B')
    if mention:
        d.texte(105, 8.0, 'Dé à monter · découper sur les pointillés · plier sur les traits fins · coller les languettes', 8)
    return (None if dessin else d.sauver(base)), c / 10, len(origines)
```

#### 19 novembre 2026 : variantes par tranche d'âge et miniatures des formats

`VARIANTES` donne, pour chaque gabarit de jeu et chaque tranche d'âge (1 : 1P à 4P ; 2 : 5P à 8P ; 3 : 9S à 11S), le format de la planche : colonnes, rangées et corps du texte, ou les paramètres du plateau. Depuis le 20.11.2026, les pages de miniatures par tranche d'âge ne sont plus dessinées ici : `miniatures_tranche` (bloc MP-J-13) les compose à partir des pages réelles des documents. Le bloc se place après `JEUX`.

**Test (19.11.2026)** : douze plateaux J5 produits en pleine page (quatre formes, trois tranches) ; police Liberation Sans à la place d'Arial ; non imprimé, non testé en classe.

```
# ---------- Variantes des jeux par tranche d'âge et miniatures des formats (19.11.2026) ----------
TRANCHES = {1: '1P à 4P (cycle 1, 4 à 8 ans)', 2: '5P à 8P (cycle 2, 8 à 12 ans)', 3: '9S à 11S (cycle 3, 12 à 15 ans)'}
# Par gabarit : une entrée par tranche (None : gabarit non proposé à cet âge).
# planche : (colonnes, rangées, corps en pt) ; plateau : paramètres de plateau_parcours ; autres : paramètres de la fonction du gabarit.
VARIANTES = {
    'J1': ('planche', 'dominos', {1: (2, 5, 26), 2: (2, 8, 18), 3: (2, 10, 14)}),
    'J2': ('planche', 'cartes', {1: (2, 3, 40), 2: (3, 4, 22), 3: (4, 5, 14)}),
    'J3': ('planche', 'cartes', {1: (2, 3, 24), 2: (3, 3, 16), 3: (4, 4, 12)}),
    'J4': ('planche', 'cartes', {1: (2, 3, 28), 2: (2, 4, 18), 3: (3, 5, 14)}),
    'J5-a': ('plateau', 'cases', {1: dict(forme='serpent', colonnes=4, rangees=7, taille_pt=32),
                                  2: dict(forme='serpent'),
                                  3: dict(forme='serpent', colonnes=8, rangees=11, taille_pt=16, case_min_mm=20)}),
    'J5-b': ('plateau', 'cases', {1: dict(forme='escargot', bande_mm=32, long_mm=42, taille_pt=30),
                                  2: dict(forme='escargot'),
                                  3: dict(forme='escargot', bande_mm=21, long_mm=25, taille_pt=15, case_min_mm=20)}),
    'J5-c': ('plateau', 'cases', {1: dict(forme='chemin', diametre_mm=36, rangs=5, taille_pt=30),
                                  2: dict(forme='chemin'),
                                  3: dict(forme='chemin', diametre_mm=22, rangs=8, taille_pt=16, case_min_mm=20)}),
    'J5-d': ('plateau', 'cases', {1: dict(forme='circuit', colonnes=4, rangees=6, taille_pt=32),
                                  2: dict(forme='circuit'),
                                  3: dict(forme='circuit', colonnes=8, rangees=11, taille_pt=16, case_min_mm=20)}),
    'J6': ('de', 'dés', {1: 'grand', 2: 'petit', 3: 'petit'}),                        # format de de_a_monter
    'J7': ('loto', 'cartons', {1: (2, 3, 2, 2), 2: (2, 4, 3, 2), 3: (2, 3, 3, 3)}),      # cartons c × r, cases a × b
    'J8': ('symboles', 'cartes', {1: (2, 4, 7, 3), 2: (3, 5, 13, 4), 3: (3, 7, 21, 5)}),  # c, r, cartes, éléments
    'J9': ('grille', 'cases', {1: (2, 3), 2: (4, 4), 3: (5, 5)}),
    'J10': ('pinces', 'questions', {1: 6, 2: 10, 3: 12}),
    'J11': ('roue', 'secteurs', {1: 4, 2: 6, 3: 8}),
    'J12': ('planche', 'plaques', {1: (2, 2, 130), 2: None, 3: None}),
    'J13': ('planche', 'cartes', {1: (2, 2, 28), 2: (2, 4, 16), 3: (2, 4, 14)}),
    'J14': ('planche', 'cartes', {1: None, 2: (2, 2, 16), 3: (2, 3, 14)}),
    'J15': ('planche', 'cartes', {1: (2, 2, 28), 2: (2, 4, 16), 3: (2, 4, 14)}),
    'J16': ('planche', 'cartons', {1: (2, 2, 110), 2: (2, 2, 110), 3: (2, 3, 90)}),
    'J17': ('alignement', 'ronds', {1: dict(colonnes=4, rangees=5, aligner=3, taille_pt=28), 2: dict(colonnes=5, rangees=7, aligner=4),
                                    3: dict(colonnes=6, rangees=8, aligner=4, taille_pt=15)}),
    'J18': ('echelles', 'cases', {1: dict(colonnes=5, rangees=6, taille_pt=20), 2: dict(colonnes=6, rangees=8),
                                  3: dict(colonnes=8, rangees=10, taille_pt=11, case_min_mm=20)}),
    'J19': ('navale', 'cases par grille', {1: dict(taille=5), 2: dict(taille=6), 3: dict(taille=8)}),
    'J20': ('tirage', 'secteurs', {1: 4, 2: 6, 3: 8}),
    'J21': ('association', 'puzzles', {1: dict(colonnes=2, rangees=4, taille_pt=28), 2: dict(colonnes=2, rangees=6, taille_pt=20),
                                       3: dict(colonnes=3, rangees=6, taille_pt=14)}),
    'J22': ('bandes', 'bandes', {1: 5, 2: 10, 3: 12}),
    'J23': ('mystere', 'mots', {1: 4, 2: 6, 3: 8}),
    'J24': ('cocotte', 'défis', {1: dict(taille_pt=14), 2: dict(taille_pt=12), 3: dict(taille_pt=12)}),
    'J25': ('horloge', 'graduations', {1: dict(), 2: dict(minutes=True), 3: dict(minutes=True, heures_24=True)}),
    'J26': ('eventail', 'fiches', {1: dict(colonnes=3, taille_pt=22), 2: dict(colonnes=4, taille_pt=15), 3: dict(colonnes=5, taille_pt=12)}),
    'J27': ('graphisme', 'bandes', {1: ('traits', 'zigzag', 'vagues', 'ponts'), 2: ('zigzag', 'vagues', 'ponts', 'coupes', 'creneaux', 'boucles'),
                                    3: ('traits', 'zigzag', 'vagues', 'ponts', 'creneaux', 'boucles', 'spirales', 'coupes')}),
    'J28': ('camemberts', 'cases', {1: dict(entre=3, rayon=2), 2: dict(entre=4, rayon=3), 3: dict(entre=6, rayon=5)}),
    'J29': ('lynx', 'mots', {1: dict(taille_pt=24), 2: dict(taille_pt=16), 3: dict(taille_pt=13)}),
    'J30': ('interdits', 'cartes', {1: None, 2: dict(colonnes=3, rangees=3, taille_pt=16), 3: dict(colonnes=3, rangees=4, taille_pt=13)}),
    'J31': ('bac', 'cases à remplir', {1: dict(manches=4, taille_pt=14), 2: dict(manches=6), 3: dict(manches=8, taille_pt=11)}),
    'J32': ('terminaisons', 'cartes-phrases', {1: None, 2: (2, 6, 16), 3: None}),
    'J33': ('chevaux', 'cases', {1: dict(), 2: dict(), 3: dict()}),
    'J34': ('qui', 'éléments', {1: dict(colonnes=3, taille_pt=40), 2: dict(colonnes=4, taille_pt=30), 3: dict(colonnes=5, taille_pt=22)}),
    'J35': ('planche', 'cartes', {1: (3, 4, 30), 2: (4, 4, 24), 3: (4, 5, 22)}),
    'J36': ('tuiles', 'tuiles', {1: dict(colonnes=6, rangees=8), 2: dict(colonnes=9, rangees=13), 3: dict(colonnes=12, rangees=17)}),
    'J37': ('sudoku', 'grilles', {1: dict(taille=4, grilles=4), 2: dict(taille=6, grilles=2), 3: dict(taille=9, grilles=2)}),
    'J38': ('fleur', 'parties', {1: dict(parties=3), 2: dict(parties=3), 3: dict(parties=3)})}
```

#### 19 novembre 2026 : dos à motif des cartes tirées (MP-J-14)

`dos_a_motif` dessine avec la classe `Dessin` (R11) le verso d'une planche de cartes tirées, à la manière d'un dos de carte à jouer : sur chaque carte, des lignes fines (losanges, carreaux ou vagues, pas de 2 mm, trait de 0,2 mm) remplissent un cadre aux angles arrondis, tracé à 3 mm du bord ; la marge reste blanche. `colonnes` et `rangees` reprennent ceux du recto. Le paramètre `texte` ajoute au centre de chaque carte une mention personnelle (nom du jeu, catégorie) dans un cartouche gris. La page s'imprime au verso de la planche, retournement sur le bord long ; le cadre rend visible un décalage, d'où l'essai d'impression. Pour un dos blanc, la fonction n'est pas appelée. Le bloc se place après `planche_pdf`, dont il reprend `SURFACE_MM`, et après `arc_pts`.

**Test du liseré (21.11.2026)** : `lisere_cartes` appelé par `planche_pdf`, `cartes_categories` et `cartes_mots_interdits` ; planches J30, J32 et J35 produites en noir et blanc et en couleur et regardées : cadre à 3 mm du trait de coupe, texte à l'intérieur ; police Liberation Sans à la place d'Arial ; non imprimé.

**Test (19.11.2026)** : trois motifs encadrés produits et regardés sur une planche de 3 × 4 cartes, puis un dos à mention « Bonus » ; planches de 2 × 3 et de 4 × 5 cartes produites ; mention trop longue refusée ; couverture d'encre mesurée sur l'image : 18 % (losanges, carreaux), 11 % (vagues) ; opacité réelle sur papier et alignement recto-verso : non testés à l'impression.

```
# ---------- MP-J-14 : dos des cartes tirées, motif encadré et mention facultative (19.11.2026) ----------
def dos_a_motif(base, motif='losanges', colonnes=3, rangees=4, texte=None, taille_pt=14, marge_mm=3.0, rayon_mm=3.0,
                pas_mm=2.0, ep=0.2, dpi=300):
    """MP-J-14 : verso d'une planche de cartes tirées (cartes-défis, memory, cartes d'appel), comme le dos d'une
    carte à jouer : sur chaque carte, un motif de lignes fines dans un cadre aux angles arrondis, à 3 mm du bord,
    la marge restant blanche. colonnes et rangees : ceux du recto. Le motif est le même sur toutes les cartes.
    motif = 'losanges' (deux séries d'obliques), 'carreaux' (quadrillage) ou 'vagues' (lignes ondulées) :
    un motif par jeu, pour trier des jeux mélangés.
    texte : mention facultative, la même au dos de chaque carte de la planche : nom du jeu ou catégorie de cartes
    (« Défi », « Bonus », « Malus », « Chance »), en gras dans un cartouche gris au centre de la carte ;
    jamais un texte qui distingue deux cartes d'une même pile.
    Le cadre rend visible un décalage du recto-verso : faire un essai d'impression (V13).
    Écrit base.svg, base.pdf et base.png ; renvoie le PDF."""
    x0, y0, L, H = SURFACE_MM; d = Dessin(); l, h = L / colonnes, H / rangees; r = rayon_mm; d.trait = couleur_trait()
    assert motif in ('losanges', 'carreaux', 'vagues'), motif
    if texte:
        lt = d.largeur_texte(texte, taille_pt, 'Arial-B'); ht = taille_pt * 25.4 / 72
        assert lt + 6 <= l - 2 * marge_mm - 4, 'texte trop long pour le dos de la carte'
    for i in range(colonnes * rangees):
        xa, ya = x0 + (i % colonnes) * l + marge_mm, y0 + (i // colonnes) * h + marge_mm
        xb, yb = xa + l - 2 * marge_mm, ya + h - 2 * marge_mm
        def dedans(x, y):                                                   # dans le cadre aux angles arrondis
            if not (xa <= x <= xb and ya <= y <= yb): return False
            cx = xa + r if x < xa + r else (xb - r if x > xb - r else x)
            cy = ya + r if y < ya + r else (yb - r if y > yb - r else y)
            return math.hypot(x - cx, y - cy) <= r + 1e-6
        def trace(pts):                                                     # ne garde que la partie située dans le cadre
            suite = []
            for p in pts:
                if dedans(*p): suite.append(p)
                else:
                    if len(suite) > 1: d.ligne(suite, ep=ep)
                    suite = []
            if len(suite) > 1: d.ligne(suite, ep=ep)
        def segment(a, b):
            n = max(2, int(math.hypot(b[0] - a[0], b[1] - a[1]) / 0.3))
            pts = [(a[0] + (b[0] - a[0]) * k / n, a[1] + (b[1] - a[1]) * k / n) for k in range(n + 1)]
            ok = [p for p in pts if dedans(*p)]
            if len(ok) > 1: d.ligne([ok[0], ok[-1]], ep=ep)
        if motif == 'carreaux':
            for k in range(1, int((xb - xa) / pas_mm) + 1): segment((xa + k * pas_mm, ya), (xa + k * pas_mm, yb))
            for k in range(1, int((yb - ya) / pas_mm) + 1): segment((xa, ya + k * pas_mm), (xb, ya + k * pas_mm))
        elif motif == 'losanges':
            q = pas_mm * math.sqrt(2); cx, cy = (xa + xb) / 2, (ya + yb) / 2; m = int((xb - xa + yb - ya) / q) + 1
            for k in range(-m, m + 1):
                c = cx - cy + k * q; x1, x2 = max(xa, ya + c), min(xb, yb + c)        # obliques x - y = c
                if x1 < x2: segment((x1, x1 - c), (x2, x2 - c))
                c = cx + cy + k * q; x1, x2 = max(xa, c - yb), min(xb, c - ya)        # obliques x + y = c
                if x1 < x2: segment((x1, c - x1), (x2, c - x2))
        else:
            n = int((xb - xa) / (pas_mm / 4))
            for k in range(int((yb - ya) / pas_mm)):
                y = ya + (k + 0.5) * pas_mm
                trace([(xa + (xb - xa) * j / n, y + pas_mm * 0.35 * math.sin(math.pi * j / 8 + k * math.pi)) for j in range(n + 1)])
        cadre = (arc_pts(xb - r, ya + r, r, 0, 90, 8) + arc_pts(xb - r, yb - r, r, 90, 180, 8) +
                 arc_pts(xa + r, yb - r, r, 180, 270, 8) + arc_pts(xa + r, ya + r, r, 270, 360, 8))
        d.ligne(cadre, ep=0.3, ferme=True)
        if texte:
            cx, cy = (xa + xb) / 2, (ya + yb) / 2
            d.ligne([(cx - lt / 2 - 3, cy - ht / 2 - 2), (cx + lt / 2 + 3, cy - ht / 2 - 2), (cx + lt / 2 + 3, cy + ht / 2 + 2),
                     (cx - lt / 2 - 3, cy + ht / 2 + 2)], ep=0.3, ferme=True, fond=(0.85, 0.85, 0.85))
            d.texte(cx, cy + taille_pt * 0.125, texte, taille_pt, police='Arial-B')
    d.png(base, dpi)
    return d.sauver(base)

def lisere_cartes(d, colonnes, rangees, marge_mm=3.0, rayon_mm=3.5, ep=0.44):
    """MP-J-14 : liseré de chaque carte d'une planche de colonnes × rangees cartes (SURFACE_MM), comme sur une carte
    à jouer : cadre aux coins arrondis à marge_mm du trait de coupe, trait de 1,25 pt ; en couleur (definir_couleur),
    l'intérieur du cadre est teinté et la marge reste blanche. À appeler AVANT de tracer le contenu des cartes,
    qui reste à l'intérieur du cadre (au moins 2 mm de jeu)."""
    x0, y0, L, H = SURFACE_MM; l, h = L / colonnes, H / rangees; r = rayon_mm
    garde = d.trait
    if COULEUR[0] is not None and tuple(d.trait) == (0, 0, 0): d.trait = couleur_trait()
    fond = _teinter((0.93, 0.93, 0.93)) if COULEUR[0] is not None else None
    for i in range(colonnes * rangees):
        xa, ya = x0 + (i % colonnes) * l + marge_mm, y0 + (i // colonnes) * h + marge_mm
        xb, yb = xa + l - 2 * marge_mm, ya + h - 2 * marge_mm
        d.ligne(arc_pts(xb - r, ya + r, r, 0, 90, 8) + arc_pts(xb - r, yb - r, r, 90, 180, 8) +
                arc_pts(xa + r, yb - r, r, 180, 270, 8) + arc_pts(xa + r, ya + r, r, 270, 360, 8), ep=ep, ferme=True, fond=fond)
    d.trait = garde
```

#### 19 novembre 2026 : grille d'alignement, serpents et échelles, bataille navale, roue de tirage (J17 à J20)

Quatre fonctions dessinent avec la classe `Dessin` (R11) les plateaux des gabarits J17 à J20, sur toute la surface utile de la page : `grille_alignement`, `serpents_echelles`, `bataille_navale` et `roue_tirage`. Elles partagent un bandeau de titre arrondi (`_bandeau`, `_cadre_arrondi`), renvoient le chemin du PDF, le nombre de ronds, de cases ou de secteurs et la dimension utile, et acceptent le paramètre `dessin` pour les miniatures. Le bloc se place après `Dessin`, `arc_pts` et `SURFACE_MM`.

**Test (19.11.2026)** : douze planches produites et regardées sur le rendu PDF (quatre gabarits, trois tranches d'âge) ; serpents et échelles tirés au sort sans croisement sur les trois formats ; un texte trop long pour un rond ou pour un secteur est refusé ; police Liberation Sans à la place d'Arial ; non imprimé, non testé en classe.

```
# ---------- J17 à J20 : grille d'alignement, serpents et échelles, bataille navale, roue de tirage (19.11.2026) ----------
def _cadre_arrondi(d, x, y, l, h, r=6.0, ep=1.2, fond=None):
    """Rectangle aux angles arrondis (cadre de plateau, bandeau de titre)."""
    d.ligne(arc_pts(x + l - r, y + r, r, 0, 90, 8) + arc_pts(x + l - r, y + h - r, r, 90, 180, 8) +
            arc_pts(x + r, y + h - r, r, 180, 270, 8) + arc_pts(x + r, y + r, r, 270, 360, 8), ep=ep, ferme=True, fond=fond)

def _bandeau(d, titre, consigne, haut=20.0):
    """Bandeau de titre d'un plateau : cadre gris arrondi, titre en gras, consigne pour les élèves. Renvoie sa hauteur.
    Pour des non-lecteurs (definir_jeunes), la consigne n'est pas écrite : passer consigne=None et montrer un exemple."""
    x0, y0, L, H = SURFACE_MM
    _cadre_arrondi(d, x0, y0, L, haut - 4, r=5, ep=0.8, fond=(0.9, 0.9, 0.9))
    d.texte(x0 + 6, y0 + 7.5, titre, 17, ancre='s', police='Arial-B')
    if consigne: d.texte(x0 + 6, y0 + 13.2, consigne, 10, ancre='s')
    return haut

def grille_alignement(base, valeurs=None, colonnes=5, rangees=7, aligner=4, titre=None, taille_pt=20, dessin=None):
    """J17 : grille d'alignement (principe du « quatre à la suite »). Chaque rond porte une réponse ; l'élève tire une
    question, trouve la réponse sur la grille et la couvre d'un jeton de sa couleur ; le premier qui aligne `aligner`
    jetons gagne. valeurs : colonnes × rangees réponses (par défaut les nombres de 1 à n).
    Renvoie (chemin du PDF, nombre de ronds, diamètre d'un rond en mm)."""
    x0, y0, L, H = SURFACE_MM; d = dessin or Dessin(); n = colonnes * rangees
    valeurs = [str(v) for v in (valeurs or range(1, n + 1))]; assert len(valeurs) == n, 'une réponse par rond'
    haut = _bandeau(d, titre or f'Aligne {aligner} !', f'Réponds, puis pose ton jeton sur la réponse. Aligne {aligner} jetons : en ligne, en colonne ou en diagonale.')
    _cadre_arrondi(d, x0, y0 + haut, L, H - haut, r=9, ep=1.4); _cadre_arrondi(d, x0 + 1.8, y0 + haut + 1.8, L - 3.6, H - haut - 3.6, r=7.5, ep=0.35)
    l, h = (L - 10) / colonnes, (H - haut - 10) / rangees; r = min(l, h) * 0.44
    for i, v in enumerate(valeurs):
        cx, cy = x0 + 5 + (i % colonnes + 0.5) * l, y0 + haut + 5 + (i // colonnes + 0.5) * h
        d.cercle(cx, cy, r, ep=1.0, fond=(1, 1, 1)); d.cercle(cx, cy, r - 1.4, ep=0.3)
        t = taille_pt
        while d.largeur_texte(v, t, 'Arial-B') > 2 * r - 6: t -= 1; assert t >= 9, f'réponse trop longue pour un rond : {v!r}'
        d.texte(cx, cy + t * 0.125, v, t, police='Arial-B')
    assert 2 * r >= 22, 'ronds trop petits pour un jeton'
    return (None if dessin else d.sauver(base)), n, round(2 * r, 1)

def serpents_echelles(base, colonnes=6, rangees=8, liens=None, graine=1, titre='Serpents et échelles', taille_pt=14,
                      case_min_mm=25.0, dessin=None):
    """J18 : plateau de serpents et échelles. Cases numérotées en lacets, du bas à gauche (Départ) jusqu'en haut
    (Arrivée). Une échelle fait monter, un serpent fait redescendre : l'élève ne monte l'échelle, ou n'évite le
    serpent, que s'il répond juste à la carte-défi tirée (le hasard ne décide pas seul).
    liens : couples (case de départ, case d'arrivée) ; arrivée plus grande = échelle, plus petite = serpent ;
    par défaut, tirés au sort avec `graine`. Renvoie (chemin du PDF, nombre de cases, plus petit côté d'une case)."""
    x0, y0, L, H = SURFACE_MM; d = dessin or Dessin(); n = colonnes * rangees
    haut = _bandeau(d, titre, 'Échelle : je monte si je réponds juste. Serpent : je redescends si je me trompe.')
    l, h = L / colonnes, (H - haut) / rangees; assert min(l, h) >= case_min_mm, f'cases de {min(l, h):.1f} mm : trop petites'
    def centre(k):                                                          # centre de la case numéro k (1 à n)
        r, q = divmod(k - 1, colonnes); q = q if r % 2 == 0 else colonnes - 1 - q
        return x0 + (q + 0.5) * l, y0 + H - (r + 0.5) * h
    if liens is None:                                                       # tirage : extrémités toutes différentes
        alea = random.Random(graine); liens = []; nb = max(2, n // 16)
        def croise(p, q, u, v):                                             # deux liens se coupent ou se frôlent
            pts = lambda a, b: [(a[0] + (b[0] - a[0]) * t / 12, a[1] + (b[1] - a[1]) * t / 12) for t in range(13)]
            return min(math.hypot(a[0] - b[0], a[1] - b[1]) for a in pts(p, q) for b in pts(u, v)) < 0.95 * max(l, h)
        for sens in (1, -1) * nb:
            for _ in range(400):
                a = alea.randrange(2, n); b = a + sens * alea.randrange(colonnes + 1, 3 * colonnes)
                if not 2 <= b <= n - 1: continue
                p, q = centre(a), centre(b)
                if l * 0.6 < abs(p[0] - q[0]) < l * 2.6 and not any(croise(p, q, centre(u), centre(v)) for u, v in liens):
                    liens.append((a, b)); break
    for k in range(1, n + 1):
        cx, cy = centre(k); r, q = divmod(k - 1, colonnes)
        d.ligne([(cx - l / 2, cy - h / 2), (cx + l / 2, cy - h / 2), (cx + l / 2, cy + h / 2), (cx - l / 2, cy + h / 2)], ep=0.35,
                ferme=True, fond=(0.93, 0.93, 0.93) if (r + round((cx - x0) / l - 0.5)) % 2 else (1, 1, 1))
    for a, b in liens:
        (xa, ya), (xb, yb) = centre(a), centre(b); xa += l * 0.1; xb += l * 0.1; ya += h * 0.14; yb += h * 0.14   # sous les numéros
        lg = math.hypot(xb - xa, yb - ya); ux, uy = (xb - xa) / lg, (yb - ya) / lg
        if b > a:                                                           # échelle : deux montants, des barreaux
            e = min(l, h) * 0.13
            for s in (-1, 1): d.ligne([(xa - s * uy * e, ya + s * ux * e), (xb - s * uy * e, yb + s * ux * e)], ep=0.9)
            for j in range(1, int(lg / 6.5)):
                px, py = xa + ux * j * 6.5, ya + uy * j * 6.5; d.ligne([(px - uy * e, py + ux * e), (px + uy * e, py - ux * e)], ep=0.7)
        else:                                                               # serpent : corps ondulant, de la tête (a) à la queue (b)
            m = 80; amp = min(l, h) * 0.26; ondes = max(1.5, round(lg / 34) + 0.5); g, dr = [], []
            for j in range(m + 1):
                t = j / m; o = amp * math.sin(t * ondes * 2 * math.pi) * min(1, t * 5)
                px, py = xa + ux * lg * t - uy * o, ya + uy * lg * t + ux * o; w = 2.5 if t < 0.7 else 2.5 - 2.1 * (t - 0.7) / 0.3
                g.append((px - uy * w, py + ux * w)); dr.append((px + uy * w, py - ux * w))
            d.ligne(g + dr[::-1], ep=0.5, ferme=True, fond=(0.72, 0.72, 0.72))
            d.cercle(xa, ya, 3.6, ep=0.6, fond=(0.72, 0.72, 0.72)); d.cercle(xa - ux * 1.2 - uy * 1.3, ya - uy * 1.2 + ux * 1.3, 0.6, ep=0, fond=(0, 0, 0))
            d.cercle(xa - ux * 1.2 + uy * 1.3, ya - uy * 1.2 - ux * 1.3, 0.6, ep=0, fond=(0, 0, 0))
            d.ligne([(xa - ux * 3.6, ya - uy * 3.6), (xa - ux * 6, ya - uy * 6), (xa - ux * 7.2 - uy * 1, ya - uy * 7.2 + ux * 1)], ep=0.4)
            d.ligne([(xa - ux * 6, ya - uy * 6), (xa - ux * 7.2 + uy * 1, ya - uy * 7.2 - ux * 1)], ep=0.4)
    for k in range(1, n + 1):                                               # numéros par-dessus, dans le coin de la case
        cx, cy = centre(k); mot = 'Départ' if k == 1 else ('Arrivée' if k == n else str(k)); t = taille_pt if mot.isdigit() else max(taille_pt * 0.95, 10)
        r, lm = divmod(k - 1, colonnes), d.largeur_texte(mot, t, 'Arial-B'); xg, yh = cx - l / 2 + 0.5, cy - h / 2 + 0.5
        d.ligne([(xg, yh), (xg + lm + 2.6, yh), (xg + lm + 2.6, yh + t * 0.36 + 2.4), (xg, yh + t * 0.36 + 2.4)], ep=0, ferme=True,
                fond=(0.93, 0.93, 0.93) if (r[0] + round((cx - x0) / l - 0.5)) % 2 else (1, 1, 1))   # pastille : le numéro reste lisible
        d.texte(cx - l / 2 + 1.8, cy - h / 2 + 1.5 + t * 0.36, mot, t, ancre='s', police='Arial-B')
    d.ligne([(x0, y0 + haut), (x0 + L, y0 + haut), (x0 + L, y0 + H), (x0, y0 + H)], ep=1.4, ferme=True)
    return (None if dessin else d.sauver(base)), n, round(min(l, h), 1)

def bataille_navale(base, en_colonnes=None, en_lignes=None, taille=6, titre='Bataille navale', taille_pt=12, dessin=None):
    """J19 : fiche de bataille navale pour un joueur : en haut « Ma flotte » (il y dessine ses bateaux), en bas
    « Mes tirs » (il y note ses essais). Pour tirer sur une case, l'élève dit la réponse formée par la colonne et la
    ligne (par exemple un sujet et un verbe : la forme conjuguée ; deux nombres : leur produit).
    en_colonnes, en_lignes : intitulés des colonnes et des lignes (par défaut A, B, C… et 1, 2, 3…).
    Renvoie (chemin du PDF, nombre de cases par grille, côté d'une case en mm)."""
    x0, y0, L, H = SURFACE_MM; d = dessin or Dessin()
    en_colonnes = list(en_colonnes or 'ABCDEFGHIJ'[:taille]); en_lignes = [str(v) for v in (en_lignes or range(1, taille + 1))]
    c, r = len(en_colonnes), len(en_lignes)
    haut = _bandeau(d, titre, 'Dis la réponse de la case pour tirer. Touché : une croix. Dans l’eau : un point.')
    marge = max(d.largeur_texte(t, taille_pt, 'Arial-B') for t in en_lignes) + 6; bloc = (H - haut) / 2
    cl, ch = (L - marge) / c, (bloc - 24) / r; gx = x0 + marge; cote = min(cl, ch)
    for k, nom in enumerate(('Ma flotte', 'Mes tirs')):
        gy = y0 + haut + k * bloc + 19; lt = d.largeur_texte(nom, 14, 'Arial-B'); fin = x0 + L - (34 if k == 0 else 0)
        d.texte(x0, gy - 12, nom, 14, ancre='s', police='Arial-B')
        d.ligne([(x0 + lt + 4 + 0.5 * j, gy - 13.5 + 1.2 * math.sin(j * 0.55)) for j in range(int((fin - x0 - lt - 6) * 2))], ep=0.35)
        if k == 0:                                                          # la flotte à dessiner : trois coques arrondies
            for q, cases in enumerate((3, 2, 1)): _cadre_arrondi(d, x0 + L - 31 + (0, 16, 27)[q], gy - 16, cases * 4.5 - 0.5, 4.5, r=2, ep=0.6, fond=(0.8, 0.8, 0.8))
        for i, t in enumerate(en_colonnes):
            s = taille_pt
            while d.largeur_texte(t, s, 'Arial-B') > cl - 2: s -= 0.5; assert s >= 7, f'intitulé trop long : {t!r}'
            d.texte(gx + (i + 0.5) * cl, gy - 2.5, t, s, police='Arial-B')
        for j, t in enumerate(en_lignes): d.texte(gx - 3 - d.largeur_texte(t, taille_pt, 'Arial-B') / 2, gy + (j + 0.5) * ch + taille_pt * 0.125, t, taille_pt, police='Arial-B')
        for i in range(c + 1): d.ligne([(gx + i * cl, gy), (gx + i * cl, gy + r * ch)], ep=1.2 if i in (0, c) else 0.35)
        for j in range(r + 1): d.ligne([(gx, gy + j * ch), (gx + c * cl, gy + j * ch)], ep=1.2 if j in (0, r) else 0.35)
    assert cote >= 12, 'cases trop petites'
    return (None if dessin else d.sauver(base)), c * r, round(cote, 1)

def roue_tirage(base, secteurs=('1', '2', '3', '4', '5', '6'), titre='Roue de tirage', taille_pt=24, dessin=None):
    """J20 : roue de tirage à faire tourner avec un trombone tenu par la pointe d'un crayon : elle remplace le dé
    et tire un mot, un nombre ou une consigne. secteurs : 3 à 12 textes courts.
    Renvoie (chemin du PDF, nombre de secteurs, diamètre de la roue en mm)."""
    x0, y0, L, H = SURFACE_MM; d = dessin or Dessin(); n = len(secteurs); assert 3 <= n <= 12, 'de 3 à 12 secteurs'
    haut = _bandeau(d, titre, 'Pose un trombone au centre, tiens-le avec la pointe d’un crayon, puis fais-le tourner.')
    R = min(L, H - haut - 40) / 2 - 2; cx, cy = x0 + L / 2, y0 + haut + 6 + R
    for k, t in enumerate(secteurs):
        a0, a1 = 360 * k / n, 360 * (k + 1) / n
        d.ligne(arc_pts(cx, cy, R, a0, a1, 24) + [(cx, cy)], ep=0.6, ferme=True, fond=(0.88, 0.88, 0.88) if k % 2 and n % 2 == 0 else (1, 1, 1))
        am = math.radians((a0 + a1) / 2); px, py = cx + 0.62 * R * math.sin(am), cy - 0.62 * R * math.cos(am); s = taille_pt
        large = 2 * 0.62 * R * math.sin(math.pi / n) - 6
        for j, ligne in enumerate(t.split('\n')):
            while d.largeur_texte(ligne, s, 'Arial-B') > large: s -= 1; assert s >= 10, f'texte trop long pour un secteur : {ligne!r}'
        lignes = t.split('\n'); pas = s * 1.2 * 25.4 / 72
        for j, ligne in enumerate(lignes): d.texte(px, py - (len(lignes) - 1) * pas / 2 + s * 0.125 + j * pas, ligne, s, police='Arial-B')
    d.cercle(cx, cy, R, ep=1.4); d.cercle(cx, cy, R + 2, ep=0.35); d.cercle(cx, cy, 5, ep=0.8, fond=(1, 1, 1)); d.cercle(cx, cy, 1, ep=0, fond=(0, 0, 0))
    by = cy + R + 12; cases = 10; cb = (y0 + H - by - 8 - 2) / 2; d.texte(x0, by + 4, 'Mes tirages', 12, ancre='s', police='Arial-B')
    for k in range(2 * cases):                                              # vingt cases pour noter les tirages
        _cadre_arrondi(d, x0 + (k % cases) * (L / cases) + 1, by + 8 + (k // cases) * (cb + 2), L / cases - 2, cb, r=2.5, ep=0.5)
    return (None if dessin else d.sauver(base)), n, round(2 * R, 1)
```

#### 20 novembre 2026 : puzzles, mot mystère, cocotte, horloge, éventail, bandes graphiques (J21 à J27)

Sept fonctions dessinent avec la classe `Dessin` (R11) les gabarits J21 à J27 : `puzzle_association`, `puzzle_bandes`, `mot_mystere`, `cocotte`, `horloge`, `eventail` et `bandes_graphiques`. Les planches à découper occupent toute la surface utile et portent les repères de coupe (`reperes_de_coupe`). Chaque fonction renvoie le chemin du PDF, le nombre de pièces et la dimension utile. Le bloc se place après `Dessin`, `arc_pts`, `SURFACE_MM`, `reperes_de_coupe` et `_bandeau`.

**Test (20.11.2026)** : vingt et une planches produites et regardées sur le rendu PDF (sept gabarits, trois tranches d'âge) ; un texte trop long est refusé ; `mot_mystere` refuse un mot qui ne contient pas la lettre attendue ; police Liberation Sans à la place d'Arial ; non imprimé ; pliage de la cocotte, emboîtement des puzzles et montage de l'horloge non essayés.

```
# ---------- J21 à J27 : puzzles, mot mystère, cocotte, horloge, éventail, bandes graphiques (20.11.2026) ----------
def _mention(d, texte):
    """Mention d'une planche à découper, dans la marge du haut."""
    assert d.largeur_texte(texte, 8) <= SURFACE_MM[2] - 10, 'mention trop longue'; d.texte(105, 8.0, texte, 8)

def _texte_ajuste(d, x, y, t, taille_pt, large, police='Arial', mini=8):
    """Écrit t centré en (x, y) ; réduit le corps jusqu'à ce que le texte tienne dans large (mm) ; refuse sous mini."""
    while d.largeur_texte(t, taille_pt, police) > large: taille_pt -= 0.5; assert taille_pt >= mini, f'texte trop long : {t!r}'
    d.texte(x, y + taille_pt * 0.125, t, taille_pt, police=police); return taille_pt

def puzzle_association(base, paires, colonnes=2, rangees=6, taille_pt=18, mention='', dessin=None):
    """J21 : puzzles à deux pièces. paires : [(gauche, droite)], par exemple (mot, définition) ou (calcul, résultat).
    Chaque puzzle est coupé par une ligne d'une forme différente : seules les deux bonnes pièces s'emboîtent
    (autocorrection par la découpe, 18 formes). Renvoie (chemin du PDF, nombre de puzzles, largeur et hauteur en cm)."""
    x0, y0, L, H = SURFACE_MM; d = dessin or Dessin(); l, h = L / colonnes, H / rangees
    assert len(paires) <= min(colonnes * rangees, 18), 'trop de paires (18 formes de coupe au plus)'
    for i, (g, dr) in enumerate(paires):
        x, y = x0 + (i % colonnes) * l, y0 + (i // colonnes) * h; xm = x + l / 2; a = min(l * 0.09, h * 0.2)
        cy = y + h * (0.3, 0.5, 0.7)[i % 3]; s = 1 if (i // 3) % 2 == 0 else -1; forme = (i // 6) % 3
        if forme == 0: dent = [(xm, cy - a), (xm + s * a, cy), (xm, cy + a)]                          # pointe
        elif forme == 1: dent = [(xm, cy - a), (xm + s * a, cy - a), (xm + s * a, cy + a), (xm, cy + a)]  # créneau
        else: dent = [(xm + s * a * math.sin(math.radians(t)), cy - a * math.cos(math.radians(t))) for t in range(0, 181, 15)]  # demi-rond
        d.ligne([(xm, y)] + dent + [(xm, y + h)], ep=0.6)
        for k, t in enumerate((g, dr)):
            lignes = t.split('\n'); c = taille_pt; cx = x + l * (0.25 + 0.5 * k)
            while max(d.largeur_texte(z, c, 'Arial-B' if k == 0 else 'Arial') for z in lignes) > l / 2 - a - 5: c -= 0.5; assert c >= 9, f'texte trop long : {t!r}'
            pas = c * 1.25 * 25.4 / 72
            for j, z in enumerate(lignes): d.texte(cx, y + h / 2 - (len(lignes) - 1) * pas / 2 + c * 0.125 + j * pas, z, c, police='Arial-B' if k == 0 else 'Arial')
    xs = [x0 + c * l for c in range(colonnes + 1)]; ys = [y0 + r * h for r in range(rangees + 1)]
    for x in xs: d.ligne([(x, y0), (x, y0 + H)], ep=0.35, tirets=(1, 1.2))
    for y in ys: d.ligne([(x0, y), (x0 + L, y)], ep=0.35, tirets=(1, 1.2))
    reperes_de_coupe(d, xs, ys)
    if mention: _mention(d, mention)
    return (None if dessin else d.sauver(base)), len(paires), (round(l / 10, 2), round(h / 10, 2))

def _scene(d, x, y, l, h):
    """Image par défaut du puzzle à bandes : un paysage au trait (collines, soleil, maison, arbre, nuages)."""
    d.ligne([(x, y), (x + l, y), (x + l, y + h), (x, y + h)], ep=0.5, ferme=True, fond=(0.95, 0.95, 0.95))
    d.cercle(x + l * 0.8, y + h * 0.2, h * 0.09, ep=0.8, fond=(1, 1, 1))
    for k in range(12):
        a = math.radians(k * 30); d.ligne([(x + l * 0.8 + h * 0.11 * math.cos(a), y + h * 0.2 + h * 0.11 * math.sin(a)), (x + l * 0.8 + h * 0.14 * math.cos(a), y + h * 0.2 + h * 0.14 * math.sin(a))], ep=0.6)
    for cx, cy, r in ((0.2, 0.16, 0.05), (0.27, 0.14, 0.065), (0.34, 0.17, 0.05), (0.52, 0.3, 0.04), (0.58, 0.28, 0.05)): d.cercle(x + l * cx, y + h * cy, h * r, ep=0.6, fond=(1, 1, 1))
    for base_y, amp, ph, gris in ((0.62, 0.07, 0.0, 0.8), (0.74, 0.05, 1.7, 0.88)):
        pts = [(x + l * t / 60, y + h * (base_y - amp * math.sin(ph + t / 60 * 2 * math.pi * 1.3))) for t in range(61)]
        d.ligne(pts + [(x + l, y + h), (x, y + h)], ep=0.7, ferme=True, fond=(gris,) * 3)
    mx, my, w = x + l * 0.36, y + h * 0.66, l * 0.2
    d.ligne([(mx, my), (mx + w, my), (mx + w, my + w * 0.7), (mx, my + w * 0.7)], ep=0.8, ferme=True, fond=(1, 1, 1))
    d.ligne([(mx - w * 0.08, my), (mx + w / 2, my - w * 0.45), (mx + w * 1.08, my)], ep=0.8, ferme=True, fond=(0.6, 0.6, 0.6))
    d.ligne([(mx + w * 0.4, my + w * 0.7), (mx + w * 0.4, my + w * 0.3), (mx + w * 0.6, my + w * 0.3), (mx + w * 0.6, my + w * 0.7)], ep=0.6)
    for q in (0.12, 0.72): d.ligne([(mx + w * q, my + w * 0.15), (mx + w * (q + 0.16), my + w * 0.15), (mx + w * (q + 0.16), my + w * 0.33), (mx + w * q, my + w * 0.33)], ep=0.5, ferme=True)
    tx, ty = x + l * 0.13, y + h * 0.78
    d.ligne([(tx - l * 0.012, ty), (tx - l * 0.012, ty - h * 0.14), (tx + l * 0.012, ty - h * 0.14), (tx + l * 0.012, ty)], ep=0.7, ferme=True, fond=(0.5, 0.5, 0.5))
    for cx, cy, r in ((0, -0.2, 0.07), (-0.04, -0.16, 0.05), (0.04, -0.16, 0.05)): d.cercle(tx + l * cx, ty + h * cy, h * r, ep=0.7, fond=(0.75, 0.75, 0.75))

def puzzle_bandes(base, etiquettes, image=None, mention='', taille_pt=28, dessin=None):
    """J22 : puzzle à bandes. Une image est coupée en bandes verticales ; chaque bande porte en bas une étiquette
    (nombre, lettre, mot) : remises dans l'ordre des étiquettes, les bandes reforment l'image (autocorrection).
    etiquettes : dans l'ordre correct, de gauche à droite. image : chemin d'une image (photo, dessin) ; sans image,
    un paysage au trait est dessiné. Renvoie (chemin du PDF, nombre de bandes, largeur d'une bande en mm)."""
    x0, y0, L, H = SURFACE_MM; d = dessin or Dessin(); n = len(etiquettes); l = L / n; hi = H - 26
    assert 3 <= n <= 12, 'de 3 à 12 bandes'
    if image and dessin is None: d.p.insert_image(d.f.Rect(x0 * d.k, y0 * d.k, (x0 + L) * d.k, (y0 + hi) * d.k), filename=image, keep_proportion=False)
    else: _scene(d, x0, y0, L, hi)
    d.ligne([(x0, y0 + hi), (x0 + L, y0 + hi)], ep=0.6)
    for i, t in enumerate(etiquettes): _texte_ajuste(d, x0 + (i + 0.5) * l, y0 + hi + 13, str(t), taille_pt, l - 3, 'Arial-B')
    xs = [x0 + i * l for i in range(n + 1)]
    for x in xs: d.ligne([(x, y0), (x, y0 + H)], ep=0.35, tirets=(1, 1.2))
    for y in (y0, y0 + H): d.ligne([(x0, y), (x0 + L, y)], ep=0.35, tirets=(1, 1.2))
    reperes_de_coupe(d, xs, (y0, y0 + H))
    if mention: _mention(d, mention)
    return (None if dessin else d.sauver(base)), n, round(l, 1)

def mot_mystere(base, mystere, mots, titre='Le mot mystère', taille_pt=12, dessin=None):
    """J23 : grille de mots à un mot mystère. mots : [(mot, définition)], un par lettre du mot mystère, dans l'ordre ;
    le mot numéro i contient la lettre numéro i du mot mystère. Chaque mot s'écrit sur une ligne ; les lignes sont
    décalées pour que les lettres du mot mystère tombent dans la colonne grisée. Majuscules sans accent.
    Renvoie (chemin du PDF, nombre de mots, côté d'une case en mm)."""
    x0, y0, L, H = SURFACE_MM; d = dessin or Dessin(); n = len(mystere); assert len(mots) == n, 'un mot par lettre du mot mystère'
    pos = []
    for lettre, (mot, _) in zip(mystere, mots):
        assert mot.isalpha() and mot == mot.upper() and lettre in mot, f'{mot!r} doit contenir {lettre!r}, en majuscules sans accent'
        pos.append(min(range(len(mot)), key=lambda k: (mot[k] != lettre, abs(k - len(mot) / 2))))
    g, dr = max(pos), max(len(m) - p for (m, _), p in zip(mots, pos)); haut = _bandeau(d, titre, 'Écris chaque mot dans sa ligne. Les cases teintées donnent le mot mystère.')
    hd = max(26.0, n * (taille_pt * 0.62 + 1.5) + 14); c = min((L - 12) / (g + dr), (H - haut - hd - 22) / n, 20.0); gx = x0 + 12 + ((L - 12) - (g + dr) * c) / 2
    d.ligne([(gx + g * c, y0 + haut), (gx + (g + 1) * c, y0 + haut), (gx + (g + 1) * c, y0 + haut + n * c), (gx + g * c, y0 + haut + n * c)], ep=0, ferme=True, fond=(0.82, 0.82, 0.82))
    for i, ((mot, _), p) in enumerate(zip(mots, pos)):
        y = y0 + haut + i * c; xa = gx + (g - p) * c
        d.texte(xa - 5, y + c / 2 + 1.6, str(i + 1), 12, police='Arial-B')
        for k in range(len(mot)): d.ligne([(xa + k * c, y), (xa + (k + 1) * c, y), (xa + (k + 1) * c, y + c), (xa + k * c, y + c)], ep=0.5, ferme=True)
    yd = y0 + haut + n * c + 9; pas = (y0 + H - 20 - yd) / n
    for i, (_, definition) in enumerate(mots):
        t = taille_pt
        while d.largeur_texte(f'{i + 1}. {definition}', t) > L: t -= 0.5; assert t >= 9, f'définition trop longue : {definition!r}'
        d.texte(x0, yd + i * pas + 3, f'{i + 1}.', t, ancre='s', police='Arial-B'); d.texte(x0 + 8, yd + i * pas + 3, definition, t, ancre='s')
    d.texte(x0, y0 + H - 5, 'Le mot mystère :', 13, ancre='s', police='Arial-B'); lx = x0 + d.largeur_texte('Le mot mystère :', 13, 'Arial-B') + 5
    for k in range(n): d.ligne([(lx + k * 11, y0 + H - 12), (lx + k * 11 + 10, y0 + H - 12), (lx + k * 11 + 10, y0 + H - 2), (lx + k * 11, y0 + H - 2)], ep=0.6, ferme=True, fond=(0.9, 0.9, 0.9))
    assert c >= 9, 'cases trop petites : raccourcir les mots'
    return (None if dessin else d.sauver(base)), n, round(c, 1)

def cocotte(base, coins, nombres, defis, titre='Cocotte en papier', taille_pt=12, dessin=None):
    """J24 : cocotte en papier (salière). coins : 4 mots visibles à l'extérieur ; nombres : 8 textes courts sur les
    volets ; defis : 8 couples (question, réponse) cachés sous les volets, dans le même ordre que nombres.
    Carré de 18,6 cm à découper, puis règle du pliage en quatre étapes.
    Renvoie (chemin du PDF, nombre de défis, côté du carré en mm)."""
    x0, y0, L, H = SURFACE_MM; d = dessin or Dessin(); S = L; cx, cy = x0 + S / 2, y0 + S / 2
    assert len(coins) == 4 and len(nombres) == 8 and len(defis) == 8, '4 coins, 8 nombres, 8 défis'
    d.ligne([(x0, y0), (x0 + S, y0), (x0 + S, y0 + S), (x0, y0 + S)], ep=0.35, tirets=(1, 1.2), ferme=True); reperes_de_coupe(d, (x0, x0 + S), (y0, y0 + S))
    for a, b in (((x0, y0), (x0 + S, y0 + S)), ((x0 + S, y0), (x0, y0 + S)), ((cx, y0), (cx, y0 + S)), ((x0, cy), (x0 + S, cy))): d.ligne([a, b], ep=0.25)
    for q in (-S / 4, S / 4): d.ligne([(cx + q, y0), (cx + q, y0 + S)], ep=0.25); d.ligne([(x0, cy + q), (x0 + S, cy + q)], ep=0.25)
    d.ligne([(cx, y0), (x0 + S, cy), (cx, y0 + S), (x0, cy)], ep=0.6, ferme=True)
    for k, t in enumerate(coins):                                           # carrés des coins : l'extérieur de la cocotte
        sx, sy = ((-1, -1), (1, -1), (1, 1), (-1, 1))[k]; tt = taille_pt + 4
        while d.largeur_texte(t, tt, 'Arial-B') > S * 0.25: tt -= 0.5; assert tt >= 9, f'texte trop long : {t!r}'
        d.texte(cx + sx * S * 0.385, cy + sy * S * 0.385, t, tt, police='Arial-B', rot=(-45, 45, -45, 45)[k])
    for k in range(8):                                                      # par huitième : nombre (volet), question et réponse (dessous)
        sx, sy = ((1, -1), (1, 1), (-1, 1), (-1, -1))[k // 2]; inv = (k % 2 == 1) != (sx * sy > 0)
        def P(u, v): return (cx + sx * S * (v if inv else u), cy + sy * S * (u if inv else v))
        q, r = defis[k]
        for (u, v), t, c, pol in (((0.4167, 0.165), nombres[k], taille_pt + 4, 'Arial-B'), ((0.325, 0.075), q, taille_pt, 'Arial'), ((0.175, 0.075), r, taille_pt, 'Arial-B')):
            px, py = P(u, v); _texte_ajuste(d, px, py, t, c, S * 0.105, pol, mini=7)
    y = y0 + S + 9; d.texte(x0, y, titre + ' : le pliage', 13, ancre='s', police='Arial-B')
    etapes = ('1. Découpe le carré. Pose-le, face imprimée contre la table.', '2. Plie les quatre coins vers le centre. Retourne le carré.',
              '3. Plie encore les quatre coins vers le centre.', '4. Plie en deux, glisse le pouce et l’index de chaque main sous les quatre coins.',
              'Le jeu : ton camarade choisit un mot, puis un nombre ; soulève le volet, lis le défi, vérifie la réponse (en gras).')
    pas = (y0 + H - y - 8) / len(etapes)
    for j, t in enumerate(etapes): _texte_ajuste(d, x0 + L / 2, y + 8 + j * pas, t, 11.5, L, mini=9)
    return (None if dessin else d.sauver(base)), 8, round(S, 1)

def horloge(base, minutes=False, heures_24=False, titre='Mon horloge', dessin=None):
    """J25 : horloge à aiguilles mobiles. Cadran de 17 cm, chiffres de 1 à 12 ; minutes=True ajoute les graduations
    des minutes et les nombres 5, 10… 60 ; heures_24=True ajoute les heures de 13 à 24. Sous le cadran, les deux
    aiguilles à découper ; une attache parisienne au centre.
    Renvoie (chemin du PDF, nombre de graduations, diamètre du cadran en mm)."""
    x0, y0, L, H = SURFACE_MM; d = dessin or Dessin(); R = 85.0; cx, cy = x0 + L / 2, y0 + R + 1
    d.cercle(cx, cy, R, ep=0.35, tirets=(1, 1.2)); re = R - (13 if minutes else 3); d.cercle(cx, cy, re, ep=1.2); d.cercle(cx, cy, 1.2, ep=0, fond=(0, 0, 0))
    for k in range(60 if minutes else 12):
        a = math.radians(k * (6 if minutes else 30)); gros = (k % 5 == 0) or not minutes; r1 = re - (6 if gros else 3)
        d.ligne([(cx + re * math.sin(a), cy - re * math.cos(a)), (cx + r1 * math.sin(a), cy - r1 * math.cos(a))], ep=1.0 if gros else 0.4)
    for hh in range(1, 13):
        a = math.radians(hh * 30); d.texte(cx + (re - 15) * math.sin(a), cy - (re - 15) * math.cos(a) + 3.2, str(hh), 26, police='Arial-B')
        if heures_24: d.texte(cx + (re - 29) * math.sin(a), cy - (re - 29) * math.cos(a) + 1.6, str(hh + 12), 13)
        if minutes: d.texte(cx + (R - 6.5) * math.sin(a), cy - (R - 6.5) * math.cos(a) + 1.5, str(hh * 5), 12)
    y = y0 + 2 * R + 12; d.texte(x0, y, titre + ' : découpe le cadran et les deux aiguilles. Fixe-les au centre avec une attache parisienne.', 10.5, ancre='s')
    for k, (lg, nom, large) in enumerate(((re - 26, 'heures', 13), (re - 9, 'minutes', 9))):  # aiguilles : la petite et la grande
        ya = y + 14 + k * 26; xa = x0 + 14
        d.ligne([(xa - 9, ya - large / 2), (xa + lg - large, ya - large / 2), (xa + lg, ya), (xa + lg - large, ya + large / 2), (xa - 9, ya + large / 2)], ep=0.35, tirets=(1, 1.2), ferme=True, fond=(0.85, 0.85, 0.85) if k == 0 else (1, 1, 1))
        d.cercle(xa, ya, 1.2, ep=0, fond=(0, 0, 0)); d.texte(xa + lg / 2, ya + 1.5, nom, 11, police='Arial-B')
    return (None if dessin else d.sauver(base)), 60 if minutes else 12, round(2 * R, 1)

def eventail(base, fiches, colonnes=4, taille_pt=16, mention='', dessin=None):
    """J26 : mémo-fiches en éventail. fiches : [(titre, [lignes])] ; deux rangées de `colonnes` fiches hautes de
    13,2 cm ; un rond marque le trou de l'attache (attache parisienne ou anneau) : les fiches s'ouvrent en éventail.
    Renvoie (chemin du PDF, nombre de fiches, largeur et hauteur d'une fiche en cm)."""
    x0, y0, L, H = SURFACE_MM; d = dessin or Dessin(); l, h = L / colonnes, H / 2
    assert len(fiches) <= 2 * colonnes, 'trop de fiches pour une planche'
    for i, (t, lignes) in enumerate(fiches):
        x, y = x0 + (i % colonnes) * l, y0 + (i // colonnes) * h
        d.ligne([(x + 2, y + 2), (x + l - 2, y + 2), (x + l - 2, y + 17), (x + 2, y + 17)], ep=0, ferme=True, fond=(0.88, 0.88, 0.88))
        _texte_ajuste(d, x + l / 2, y + 10.5, t, taille_pt + 2, l - 7, 'Arial-B', mini=9)
        pas = (h - 17 - 16) / max(len(lignes), 1)
        for j, z in enumerate(lignes): _texte_ajuste(d, x + l / 2, y + 17 + (j + 0.6) * pas, z, taille_pt, l - 5, mini=8)
        d.cercle(x + l / 2, y + h - 7, 2.5, ep=0.5); d.ligne([(x + l / 2 - 1.2, y + h - 7), (x + l / 2 + 1.2, y + h - 7)], ep=0.3); d.ligne([(x + l / 2, y + h - 8.2), (x + l / 2, y + h - 5.8)], ep=0.3)
    xs = [x0 + c * l for c in range(colonnes + 1)]; ys = [y0, y0 + h, y0 + H]
    for x in xs: d.ligne([(x, y0), (x, y0 + H)], ep=0.35, tirets=(1, 1.2))
    for y in ys: d.ligne([(x0, y), (x0 + L, y)], ep=0.35, tirets=(1, 1.2))
    reperes_de_coupe(d, xs, ys)
    if mention: _mention(d, mention)
    return (None if dessin else d.sauver(base)), len(fiches), (round(l / 10, 2), round(h / 10, 2))

MOTIFS = ('traits', 'zigzag', 'vagues', 'ponts', 'creneaux', 'boucles', 'spirales', 'coupes')

def _motif(nom, x, y, l, a, pas):
    """Points d'un motif graphique : départ en (x, y), longueur l, amplitude a, largeur d'un motif pas (mm)."""
    n = max(1, int(l / pas)); pts = []
    for k in range(n):
        xk = x + k * pas
        if nom == 'traits': pts.append([(xk + pas / 2, y - a), (xk + pas / 2, y + a)])
        elif nom == 'zigzag': pts += [(xk, y + a), (xk + pas / 2, y - a)] + ([(xk + pas, y + a)] if k == n - 1 else [])
        elif nom == 'vagues': pts += [(xk + pas * t / 16, y - a * math.sin(2 * math.pi * t / 16)) for t in range(17 if k == n - 1 else 16)]
        elif nom == 'ponts': pts += [(xk + pas * t / 16, y + a - 2 * a * math.sin(math.pi * t / 16)) for t in range(17 if k == n - 1 else 16)]
        elif nom == 'coupes': pts += [(xk + pas * t / 16, y - a + 2 * a * math.sin(math.pi * t / 16)) for t in range(17 if k == n - 1 else 16)]
        elif nom == 'creneaux': pts += [(xk, y + a), (xk, y - a), (xk + pas / 2, y - a), (xk + pas / 2, y + a)] + ([(xk + pas, y + a)] if k == n - 1 else [])
        elif nom == 'boucles': pts += [(xk + pas * t / 24 - a * 0.75 * math.sin(2 * math.pi * t / 24), y + a * math.cos(2 * math.pi * t / 24)) for t in range(25 if k == n - 1 else 24)]
        elif nom == 'spirales': pts.append([(xk + pas / 2 + (a * t / 60) * math.cos(t / 60 * 5 * math.pi), y + (a * t / 60) * math.sin(t / 60 * 5 * math.pi)) for t in range(61)])
    return pts if nom in ('traits', 'spirales') else [pts]

def bandes_graphiques(base, motifs=('traits', 'zigzag', 'vagues', 'ponts', 'boucles'), mention='', dessin=None):
    """J27 : bandes graphiques à plastifier (feutre effaçable). Une bande par motif de MOTIFS : un point de départ,
    un modèle en trait plein sur le premier tiers, puis le même tracé en pointillés à repasser.
    Renvoie (chemin du PDF, nombre de bandes, hauteur d'une bande en mm)."""
    x0, y0, L, H = SURFACE_MM; d = dessin or Dessin(); n = len(motifs); h = H / n; assert 3 <= n <= 8, 'de 3 à 8 bandes'
    for i, nom in enumerate(motifs):
        assert nom in MOTIFS, nom
        y = y0 + (i + 0.5) * h; a = h * 0.3; pas = (a * 1.1 if nom == 'traits' else a * 2.6 if nom == 'spirales' else a * 2)
        d.cercle(x0 + 7, y + (0 if nom in ('vagues', 'spirales') else -a if nom in ('traits', 'coupes') else a), 1.8, ep=0, fond=(0, 0, 0))
        nb = max(1, int((L - 20) / pas)); modele = max(1, nb // 3)
        for part, dx, k, tirets in ((modele, 0, 0, None), (nb - modele, modele * pas, 1, (1.2, 1.6))):
            if part <= 0: continue
            for seg in _motif(nom, x0 + 12 + dx, y, part * pas, a, pas): d.ligne(seg, ep=0.9 if k == 0 else 0.6, tirets=tirets)
    xs = (x0, x0 + L); ys = [y0 + r * h for r in range(n + 1)]
    for x in xs: d.ligne([(x, y0), (x, y0 + H)], ep=0.35, tirets=(1, 1.2))
    for y in ys: d.ligne([(x0, y), (x0 + L, y)], ep=0.35, tirets=(1, 1.2))
    reperes_de_coupe(d, xs, ys)
    if mention: _mention(d, mention)
    return (None if dessin else d.sauver(base)), n, round(h, 1)
```

#### 20 novembre 2026 : plateau à camemberts, cherche-et-trouve, mots interdits, petit bac, lignage romand (J28 à J31, G22)

Cinq fonctions dessinent avec la classe `Dessin` (R11) les gabarits J28 à J31 et G22 : `plateau_camemberts`, `planche_lynx`, `cartes_mots_interdits`, `petit_bac` et `lignage_romand`. Les catégories du plateau se distinguent par un symbole (`_symbole`), jamais par la couleur seule. Le bloc se place après le bloc J21 à J27 (il utilise `_bandeau`, `_cadre_arrondi`, `_mention` et `_texte_ajuste`).

**Test (20.11.2026)** : quatorze pages produites et regardées sur le rendu PDF ; `planche_lynx` place 20, 38 et 66 mots sans chevauchement ; le module de 7 mm de `lignage_romand` reproduit le document « Lignes, document vertical » de la BDRP (6,9 mm mesurés) ; police Liberation Sans à la place d'Arial ; non imprimé, non testé en classe.

```
# ---------- J28 à J31 et G22 : plateau à camemberts, cherche-et-trouve, mots interdits, petit bac, lignage romand (20.11.2026) ----------
def _symbole(d, k, x, y, r, fond=(0.15, 0.15, 0.15)):
    """Symbole de la catégorie k (0 à 5) : disque, triangle, carré, losange, étoile, croix. Jamais la couleur seule."""
    if COULEUR[0]: fond = TEINTES[TEINTES_CATEGORIES[k % 6]]
    if k == 0: d.cercle(x, y, r * 0.9, ep=0.3, fond=fond)
    elif k == 1: d.ligne([(x, y - r), (x + r, y + r * 0.8), (x - r, y + r * 0.8)], ep=0.3, ferme=True, fond=fond)
    elif k == 2: d.ligne([(x - r * 0.85, y - r * 0.85), (x + r * 0.85, y - r * 0.85), (x + r * 0.85, y + r * 0.85), (x - r * 0.85, y + r * 0.85)], ep=0.3, ferme=True, fond=fond)
    elif k == 3: d.ligne([(x, y - r * 1.1), (x + r * 0.8, y), (x, y + r * 1.1), (x - r * 0.8, y)], ep=0.3, ferme=True, fond=fond)
    elif k == 4: d.ligne([(x + (r * 1.1 if j % 2 == 0 else r * 0.45) * math.sin(math.radians(36 * j)), y - (r * 1.1 if j % 2 == 0 else r * 0.45) * math.cos(math.radians(36 * j))) for j in range(10)], ep=0.3, ferme=True, fond=fond)
    else:
        a, b = r, r * 0.35
        d.ligne([(x - b, y - a), (x + b, y - a), (x + b, y - b), (x + a, y - b), (x + a, y + b), (x + b, y + b), (x + b, y + a), (x - b, y + a), (x - b, y + b), (x - a, y + b), (x - a, y - b), (x - b, y - b)], ep=0.3, ferme=True, fond=fond)

def plateau_camemberts(base, categories, entre=4, rayon=3, titre='Le tour des savoirs', dessin=None):
    """J28 : plateau de quiz à six catégories (roue à six rayons). categories : 6 noms courts. entre : cases entre deux
    rayons sur la couronne ; rayon : cases par rayon. Chaque case porte le symbole d'une catégorie ; au bout de chaque
    rayon, une grande case : une réponse juste y fait gagner la part de cette catégorie. Sous la roue : la légende
    et quatre camemberts de score à colorier. Renvoie (chemin du PDF, nombre de cases, plus petit côté d'une case en mm)."""
    x0, y0, L, H = SURFACE_MM; d = dessin or Dessin(); assert len(categories) == 6, 'six catégories'
    R = 90.0; cx, cy = x0 + L / 2, y0 + R + 1; w = 15.0; rh = 15.0; n = 6 * (entre + 1); pas = 360 / n; lr = (R - w - rh) / rayon; lw = 14.0
    P = lambda r, a: (cx + r * math.sin(math.radians(a)), cy - r * math.cos(math.radians(a)))
    for j in range(6):                                                      # rayons, du bord vers le centre
        a = 60 * j; ux, uy = math.sin(math.radians(a)), -math.cos(math.radians(a))
        for q in range(rayon):
            r1, r2 = R - w - q * lr, R - w - (q + 1) * lr; k = (j + q + 2) % 6
            d.ligne([(cx + ux * r1 - uy * lw / 2, cy + uy * r1 + ux * lw / 2), (cx + ux * r1 + uy * lw / 2, cy + uy * r1 - ux * lw / 2),
                     (cx + ux * r2 + uy * lw / 2, cy + uy * r2 - ux * lw / 2), (cx + ux * r2 - uy * lw / 2, cy + uy * r2 + ux * lw / 2)], ep=0.5, ferme=True, fond=(1, 1, 1))
            _symbole(d, k, cx + ux * (r1 + r2) / 2, cy + uy * (r1 + r2) / 2, 2.8)
    for i in range(n):                                                      # couronne
        a = i * pas; j, p = divmod(i, entre + 1); grande = p == 0
        rejoue = entre >= 5 and p in (2, entre - 1)
        d.ligne(arc_pts(cx, cy, R, a - pas / 2, a + pas / 2, 8) + arc_pts(cx, cy, R - w, a + pas / 2, a - pas / 2, 8), ep=1.1 if grande else 0.5, ferme=True,
                fond=(0.85, 0.85, 0.85) if grande else (1, 1, 1))
        px, py = P(R - w / 2, a)
        if rejoue: d.texte(px, py + 1.2, 'rejoue', 6.5, police='Arial-B', rot=a if a <= 90 or a >= 270 else a - 180)
        else: _symbole(d, j if grande else (j + p + 1 + (p > entre // 2)) % 6, px, py, 4.2 if grande else 2.8)
    d.cercle(cx, cy, rh, ep=1.1, fond=(0.92, 0.92, 0.92)); d.texte(cx, cy - 1, 'Départ', 9, police='Arial-B'); d.texte(cx, cy + 4, 'Arrivée', 9, police='Arial-B')
    y = y0 + 2 * R + 8; d.texte(x0, y, titre, 14, ancre='s', police='Arial-B')
    for k, nom in enumerate(categories):                                    # légende : symbole et nom
        xx, yy = x0 + 4 + (k % 2) * 62, y + 11 + (k // 2) * 11; _symbole(d, k, xx, yy - 1.5, 3.2)
        t = 11
        while d.largeur_texte(nom, t) > 50: t -= 0.5; assert t >= 8, f'nom de catégorie trop long : {nom!r}'
        d.texte(xx + 7, yy, nom, t, ancre='s')
    for t, yy in (('Grande case au bout d’un rayon : si tu réponds juste, colorie la part de ton camembert.', y + 47), ('Six parts coloriées : retourne au centre et réponds à une dernière question.', y + 53)): d.texte(x0, yy, t, 9, ancre='s')
    for k in range(4):                                                      # quatre camemberts de score
        px, py = x0 + L - 46 + (k % 2) * 30, y + 6 + (k // 2) * 31; rr = 13.0
        for s in range(6):
            d.ligne(arc_pts(px, py, rr, 60 * s - 30, 60 * s + 30, 6) + [(px, py)], ep=0.5, ferme=True)
            _symbole(d, s, px + rr * 0.62 * math.sin(math.radians(60 * s)), py - rr * 0.62 * math.cos(math.radians(60 * s)), 1.6)
    cote = min(w, 2 * math.pi * (R - w / 2) / n, lr, lw); assert cote >= 11, 'cases trop petites'
    return (None if dessin else d.sauver(base)), n + 6 * rayon + 1, round(cote, 1)

def planche_lynx(base, mots, graine=1, taille_pt=15, titre='Cherche et trouve', dessin=None):
    """J29 : planche de cherche-et-trouve. Les mots sont dispersés sur la page, penchés, sans se toucher. Une carte
    consigne est tirée (« Trouve un adjectif », « Trouve un mot de la famille de… ») ; le premier qui pose le doigt
    sur un mot qui convient gagne la carte. Renvoie (chemin du PDF, nombre de mots, corps en pt)."""
    x0, y0, L, H = SURFACE_MM; d = dessin or Dessin(); alea = random.Random(graine)
    haut = _bandeau(d, titre, 'Tire une carte, lis la consigne, cherche un mot qui convient et pose ton doigt dessus.')
    _cadre_arrondi(d, x0, y0 + haut, L, H - haut, r=8, ep=1.2); poses = []; rc = taille_pt * 0.19
    for mot in sorted(mots, key=len, reverse=True):
        lg = d.largeur_texte(mot, taille_pt, 'Arial-B')
        candidats = []                                                      # (écart au mot le plus proche, x, y, rot, points)
        for essai in range(4000):
            rot = alea.choice((-35, -25, -15, -8, 0, 8, 15, 25, 35, 0, 0, 90, -90)); a = math.radians(rot)
            x, y = alea.uniform(x0 + 6, x0 + L - 6), alea.uniform(y0 + haut + 6, y0 + H - 6)
            pts = [(x + (t - lg / 2) * math.cos(a), y + (t - lg / 2) * math.sin(a)) for t in [lg * k / max(1, int(lg / rc)) for k in range(max(1, int(lg / rc)) + 1)]]
            if any(not (x0 + 5 < px < x0 + L - 5 and y0 + haut + 5 < py < y0 + H - 5) for px, py in pts): continue
            ecart = min((math.hypot(px - qx, py - qy) for autres in poses for qx, qy in autres for px, py in pts), default=1e9)
            if ecart < 2 * rc + 3.5: continue
            candidats.append((ecart, x, y, rot, pts))
            if len(candidats) == 40: break
        if not candidats: raise AssertionError(f'plus de place pour {mot!r} : réduire le corps ou le nombre de mots')
        _, x, y, rot, pts = max(candidats, key=lambda c: c[0]); a = math.radians(rot)   # le plus loin des autres : mots bien répartis
        poses.append(pts); d.texte(x + rc * 0.6 * math.sin(a) * -1, y + rc * 0.6 * math.cos(a), mot, taille_pt, police='Arial-B', rot=rot)
    return (None if dessin else d.sauver(base)), len(mots), taille_pt

def cartes_mots_interdits(base, cartes, colonnes=3, rangees=3, taille_pt=16, mention='', dessin=None, lisere=True):
    """J30 : cartes à mots interdits. cartes : [(mot à faire deviner, [mots interdits])]. L'élève fait deviner le mot
    du bandeau sans prononcer les mots interdits. lisere : cadre arrondi à 3 mm du trait de coupe (MP-J-14).
    Renvoie (chemin du PDF, nombre de cartes, largeur et hauteur en cm)."""
    x0, y0, L, H = SURFACE_MM; d = dessin or Dessin(); l, h = L / colonnes, H / rangees
    assert len(cartes) <= colonnes * rangees, 'trop de cartes pour une planche'
    if lisere: lisere_cartes(d, colonnes, rangees)
    e = 5.5 if lisere else 3                                                # bandeau à l'intérieur du liseré
    for i, (mot, interdits) in enumerate(cartes):
        x, y = x0 + (i % colonnes) * l, y0 + (i // colonnes) * h; hb = min(18.0, h * 0.24)
        d.ligne([(x + e, y + e), (x + l - e, y + e), (x + l - e, y + e + hb), (x + e, y + e + hb)], ep=0.6, ferme=True, fond=(0.85, 0.85, 0.85))
        _texte_ajuste(d, x + l / 2, y + e + hb / 2 + 1, mot, taille_pt + 3, l - 2 * e - 4, 'Arial-B', mini=10)
        d.texte(x + l / 2, y + e + hb + 6.5, 'sans dire', 8); pas = (h - hb - 2 * e - 13) / max(len(interdits), 1)
        for j, z in enumerate(interdits): _texte_ajuste(d, x + l / 2, y + e + hb + 10 + (j + 0.5) * pas, z, taille_pt, l - 2 * e - 4, mini=9)
    xs = [x0 + c * l for c in range(colonnes + 1)]; ys = [y0 + r * h for r in range(rangees + 1)]
    for x in xs: d.ligne([(x, y0), (x, y0 + H)], ep=0.35, tirets=(1, 1.2))
    for y in ys: d.ligne([(x0, y), (x0 + L, y)], ep=0.35, tirets=(1, 1.2))
    reperes_de_coupe(d, xs, ys)
    if mention: _mention(d, mention)
    return (None if dessin else d.sauver(base)), len(cartes), (round(l / 10, 2), round(h / 10, 2))

def petit_bac(base, categories, manches=6, titre='Petit bac', taille_pt=12, dessin=None):
    """J31 : grille de petit bac. Une lettre est tirée par manche ; chaque élève écrit un mot par catégorie qui commence
    par cette lettre. categories : 3 à 6 noms courts. Renvoie (chemin du PDF, nombre de cases à remplir, hauteur d'une ligne en mm)."""
    x0, y0, L, H = SURFACE_MM; d = dessin or Dessin(); n = len(categories); assert 3 <= n <= 6, 'de 3 à 6 catégories'
    haut = _bandeau(d, titre, 'Une lettre par ligne. Écris un mot par colonne. Un mot juste : 1 point ; un mot que personne d’autre n’a : 2 points.')
    d.texte(x0, y0 + haut + 6, 'Prénom : ____________________', 12, ancre='s'); y1 = y0 + haut + 12; he = 12.0; hl = (y0 + H - y1 - he - 12) / manches
    la, lp = 18.0, 20.0; lc = (L - la - lp) / n; xs = [x0, x0 + la] + [x0 + la + (k + 1) * lc for k in range(n)] + [x0 + L]
    d.ligne([(x0, y1), (x0 + L, y1), (x0 + L, y1 + he), (x0, y1 + he)], ep=0, ferme=True, fond=(0.85, 0.85, 0.85))
    for k, t in enumerate(['Lettre'] + list(categories) + ['Points']): _texte_ajuste(d, (xs[k] + xs[k + 1]) / 2, y1 + he / 2 + 0.5, t, taille_pt, xs[k + 1] - xs[k] - 3, 'Arial-B', mini=8)
    for x in xs: d.ligne([(x, y1), (x, y1 + he + manches * hl)], ep=1.0 if x in (x0, x0 + L) else 0.4)
    for j in range(manches + 1): d.ligne([(x0, y1 + he + j * hl), (x0 + L, y1 + he + j * hl)], ep=1.0 if j in (0, manches) else 0.4)
    d.ligne([(x0, y1), (x0 + L, y1)], ep=1.0); yt = y1 + he + manches * hl + 8
    d.texte(x0 + L - lp - 3 - d.largeur_texte('Total :', 13, 'Arial-B'), yt, 'Total :', 13, ancre='s', police='Arial-B')
    d.ligne([(x0 + L - lp, yt - 6.5), (x0 + L, yt - 6.5), (x0 + L, yt + 3), (x0 + L - lp, yt + 3)], ep=0.8, ferme=True)
    assert hl >= 12, 'lignes trop basses'
    return (None if dessin else d.sauver(base)), n * manches, round(hl, 1)

def lignage_romand(base, module_mm=7.0, couleurs=True, entete=True, dessin=None):
    """G22 : page de lignes d'écriture au lignage romand (quatre lignes, trois couloirs égaux, sans quadrillage) :
    ligne de base épaisse, ligne du corps des lettres en trait fin, lignes de plafond et de plancher en pointillés.
    module_mm : hauteur d'un couloir (7 mm : modèle de la BDRP pour l'entrée dans l'écriture ; 4 mm, 2,5 mm ou 2 mm
    ensuite). couleurs=True colore les couloirs : ciel (lettres hautes), herbe (corps), terre (lettres basses).
    Renvoie (chemin du PDF, nombre de lignes d'écriture, module en mm)."""
    x0, y0, L, H = SURFACE_MM; d = dessin or Dessin(); m = module_mm; assert 2 <= m <= 10, 'module de 2 à 10 mm'
    haut = 12.0 if entete else 0.0; esp = max(5.0, 1.6 * m); n = int((H - haut + esp) / (3 * m + esp)); esp = (H - haut - n * 3 * m) / max(n - 1, 1)
    if entete and JEUNES[0]: d.texte(x0, y0 + 6, _prenom(), 12, ancre='s')
    elif entete: d.texte(x0, y0 + 6, 'Prénom : ____________________', 12, ancre='s'); d.texte(x0 + L - d.largeur_texte('Date : ______________', 12), y0 + 6, 'Date : ______________', 12, ancre='s')
    for i in range(n):
        y = y0 + haut + i * (3 * m + esp)
        if couleurs:
            for k, c in enumerate(((0.83, 0.93, 1.0), (0.84, 0.95, 0.80), (0.99, 0.89, 0.78))): d.ligne([(x0, y + k * m), (x0 + L, y + k * m), (x0 + L, y + (k + 1) * m), (x0, y + (k + 1) * m)], ep=0, ferme=True, fond=c)
        d.ligne([(x0, y), (x0 + L, y)], ep=0.3, tirets=(0.3, 1.2)); d.ligne([(x0, y + m), (x0 + L, y + m)], ep=0.25)
        d.ligne([(x0, y + 2 * m), (x0 + L, y + 2 * m)], ep=0.55); d.ligne([(x0, y + 3 * m), (x0 + L, y + 3 * m)], ep=0.3, tirets=(0.3, 1.2))
    return (None if dessin else d.sauver(base)), n, m
```

#### 20 novembre 2026 : cartes à catégories, petits chevaux, Qui est-ce ?, tuiles-lettres, sudoku, mot caché, syllabes et sons, livret d'écriture

Huit fonctions complètent les gabarits J28, J33 à J38, G22 et G23 : `cartes_categories`, `petits_chevaux`, `grille_qui_est_ce`, `tuiles_lettres`, `sudoku`, `mot_cache_fleur`, `fiche_syllabes_sons` et `livret_ecriture`. `_decoupe` trace les pointillés et les repères de coupe d'une planche ; `_sudoku` construit une grille et vérifie par programme que sa solution est unique ; `_fleur` dessine la fleur étape par étape. Le bloc se place après le bloc J28 à J31 (il utilise `_symbole`, `_bandeau`, `_cadre_arrondi`, `_mention` et `_texte_ajuste`).

**Test (20.11.2026)** : toutes les pages produites et regardées sur le rendu PDF ; sudokus de 4 × 4, 6 × 6 et 9 × 9 à solution unique, pages de solutions comprises ; police Liberation Sans à la place d'Arial ; non imprimé, non testé en classe ; pliage et agrafage du livret non essayés ; insertion d'images dans la fiche « syllabes et sons » non essayée.

```
# ---------- J28 (cartes), J33 à J38, G22 (livret), G23 : cartes à catégories, petits chevaux, qui est-ce, tuiles-lettres, sudoku, fleur, syllabes (20.11.2026) ----------
def _decoupe(d, colonnes, rangees, mention=''):
    """Pointillés et repères de coupe d'une planche de colonnes × rangees pièces ; renvoie (largeur, hauteur) d'une pièce."""
    x0, y0, L, H = SURFACE_MM; l, h = L / colonnes, H / rangees
    xs = [x0 + c * l for c in range(colonnes + 1)]; ys = [y0 + r * h for r in range(rangees + 1)]
    for x in xs: d.ligne([(x, y0), (x, y0 + H)], ep=0.35, tirets=(1, 1.2))
    for y in ys: d.ligne([(x0, y), (x0 + L, y)], ep=0.35, tirets=(1, 1.2))
    reperes_de_coupe(d, xs, ys)
    if mention: _mention(d, mention)
    return l, h

def cartes_categories(base, cartes, colonnes=2, rangees=2, taille_pt=11, mention='', dessin=None, lisere=True):
    """J28 : cartes-questions du plateau à camemberts. cartes : une liste par carte de six couples (question, réponse),
    dans l'ordre des catégories (disque, triangle, carré, losange, étoile, croix). La carte est lue par un·e camarade :
    la réponse est écrite en gras sous la question. lisere : cadre arrondi à 3 mm du trait de coupe (MP-J-14).
    Renvoie (chemin du PDF, nombre de cartes, largeur et hauteur en cm)."""
    x0, y0, L, H = SURFACE_MM; d = dessin or Dessin(); l, h = L / colonnes, H / rangees
    assert len(cartes) <= colonnes * rangees and all(len(c) == 6 for c in cartes), 'six questions par carte'
    if lisere: lisere_cartes(d, colonnes, rangees)
    e = 2.5 if lisere else 0                                                # contenu à l'intérieur du liseré
    for i, carte in enumerate(cartes):
        x, y = x0 + (i % colonnes) * l, y0 + (i // colonnes) * h; pas = (h - 8 - 2 * e) / 6
        for k, (q, r) in enumerate(carte):
            yy = y + 4 + e + k * pas; _symbole(d, k, x + 8 + e, yy + pas / 2, 2.8)
            if k: d.ligne([(x + 4 + e, yy), (x + l - 4 - e, yy)], ep=0.2)
            lignes = q.split('\n'); t = taille_pt
            while max(d.largeur_texte(z, t) for z in lignes) > l - 20 - 2 * e: t -= 0.5; assert t >= 7.5, f'question trop longue : {q!r}'
            p = t * 1.2 * 25.4 / 72; ya = yy + pas / 2 - (len(lignes) + 1) * p / 2 + t * 0.3
            for j, z in enumerate(lignes): d.texte(x + 14 + e, ya + j * p, z, t, ancre='s')
            tr = t
            while d.largeur_texte(r, tr, 'Arial-B') > l - 20 - 2 * e: tr -= 0.5
            d.texte(x + 14 + e, ya + len(lignes) * p + 0.6, r, tr, ancre='s', police='Arial-B')
    _decoupe(d, colonnes, rangees, mention)
    return (None if dessin else d.sauver(base)), len(cartes), (round(l / 10, 2), round(h / 10, 2))

def petits_chevaux(base, titre='Les petits chevaux', dessin=None):
    """J33 : plateau de petits chevaux pour quatre joueurs (symboles : disque, triangle, carré, étoile). Piste de
    52 cases en croix, quatre écuries, quatre échelles numérotées de 1 à 5 vers le centre. Pour sortir un pion ou
    monter une marche de l'échelle, l'élève répond à une carte-défi.
    Renvoie (chemin du PDF, nombre de cases de la piste, côté d'une case en mm)."""
    x0, y0, L, H = SURFACE_MM; d = dessin or Dessin(); haut = _bandeau(d, titre, 'Un 6 et une réponse juste : ton pion sort de l’écurie. Sur l’échelle : une réponse juste par marche.')
    c = L / 15; oy = y0 + haut; sym = (0, 1, 2, 4)
    def case(i, j, fond=None, ep=0.5): d.ligne([(x0 + i * c, oy + j * c), (x0 + (i + 1) * c, oy + j * c), (x0 + (i + 1) * c, oy + (j + 1) * c), (x0 + i * c, oy + (j + 1) * c)], ep=ep, ferme=True, fond=fond)
    piste = 0
    for i in range(15):
        for j in range(15):
            croix = 6 <= i <= 8 or 6 <= j <= 8; centre = 6 <= i <= 8 and 6 <= j <= 8
            if not croix or centre: continue
            echelle = (i == 7 and 1 <= j <= 13) or (j == 7 and 1 <= i <= 13)
            case(i, j, fond=(0.88, 0.88, 0.88) if echelle else (1, 1, 1)); piste += 0 if echelle else 1
            if echelle:
                n = j if (i == 7 and j < 7) else 14 - j if i == 7 else i if i < 7 else 14 - i
                d.texte(x0 + (i + 0.5) * c, oy + (j + 0.5) * c + 1.8, str(n), 13, police='Arial-B')
    d.ligne([(x0 + 6 * c, oy + 6 * c), (x0 + 9 * c, oy + 6 * c), (x0 + 9 * c, oy + 9 * c), (x0 + 6 * c, oy + 9 * c)], ep=1.0, ferme=True, fond=(1, 1, 1))
    d.ligne([(x0 + 6 * c, oy + 6 * c), (x0 + 9 * c, oy + 9 * c)], ep=0.4); d.ligne([(x0 + 9 * c, oy + 6 * c), (x0 + 6 * c, oy + 9 * c)], ep=0.4)
    d.cercle(x0 + 7.5 * c, oy + 7.5 * c, c * 0.75, ep=0.6, fond=(1, 1, 1)); d.texte(x0 + 7.5 * c, oy + 7.5 * c + 1.2, 'Arrivée', 8.5, police='Arial-B')
    for k, (ex, ey, dep, tete) in enumerate(((0, 0, (6, 1), (7, 0)), (9, 0, (13, 6), (14, 7)), (9, 9, (8, 13), (7, 14)), (0, 9, (1, 8), (0, 7)))):
        _cadre_arrondi(d, x0 + ex * c + 3, oy + ey * c + 3, 6 * c - 6, 6 * c - 6, r=8, ep=1.0, fond=(0.94, 0.94, 0.94))
        _symbole(d, sym[k], x0 + (ex + 3) * c, oy + (ey + 3) * c, 6.5)
        for a, b in ((1.4, 1.4), (4.6, 1.4), (1.4, 4.6), (4.6, 4.6)): d.cercle(x0 + (ex + a) * c, oy + (ey + b) * c, c * 0.55, ep=0.8, fond=(1, 1, 1))
        _symbole(d, sym[k], x0 + (dep[0] + 0.5) * c, oy + (dep[1] + 0.5) * c, 3.0); _symbole(d, sym[k], x0 + (tete[0] + 0.5) * c, oy + (tete[1] + 0.5) * c, 1.8, fond=(0.6, 0.6, 0.6))
    y = oy + 15 * c + 8
    for j, t in enumerate(('Chaque joueur choisit un symbole et pose ses quatre pions dans son écurie.', 'Case marquée de ton symbole : le départ de tes pions. Ils font le tour de la piste dans le sens des aiguilles d’une montre.',
                           'Tu arrives sur un pion adverse : il retourne à son écurie. Le premier qui amène ses quatre pions au centre gagne.')):
        _texte_ajuste(d, x0 + L / 2, y + j * ((y0 + H - y - 4) / 3) + 3, t, 10.5, L, mini=8.5)
    return (None if dessin else d.sauver(base)), piste, round(c, 1)

def grille_qui_est_ce(base, elements, colonnes=4, titre='Qui est-ce ?', taille_pt=26, dessin=None):
    """J34 : grille de « Qui est-ce ? » sans images : des nombres, des mots ou des figures nommées. Chaque élève a une
    grille ; l'un choisit un élément en secret, l'autre pose des questions auxquelles on répond par oui ou par non et
    barre ce qui ne convient pas. Renvoie (chemin du PDF, nombre d'éléments, largeur et hauteur d'une case en mm)."""
    x0, y0, L, H = SURFACE_MM; d = dessin or Dessin(); n = len(elements); r = -(-n // colonnes); assert n == r * colonnes, 'grille incomplète'
    haut = _bandeau(d, titre, 'Pose une question à laquelle on répond par oui ou par non. Barre ce qui ne convient pas. Trouve l’élément secret.')
    hs = 14.0; l, h = L / colonnes, (H - haut - hs) / r
    for i, e in enumerate(elements):
        x, y = x0 + (i % colonnes) * l, y0 + haut + (i // colonnes) * h
        _cadre_arrondi(d, x + 1.5, y + 1.5, l - 3, h - 3, r=4, ep=0.8); _texte_ajuste(d, x + l / 2, y + h / 2 + 1, str(e), taille_pt, l - 8, 'Arial-B', mini=10)
    d.texte(x0, y0 + H - 4, 'Mon élément secret (écris-le, puis cache-le) : ____________', 12, ancre='s')
    return (None if dessin else d.sauver(base)), n, (round(l, 1), round(h, 1))

FREQUENCES = 'eeeeeeeeeeeeeeeaaaaaaaaaiiiiiiiinnnnnnooooooorrrrrrsssssstttttttuuuuuuullllldddmmmggbbccppffhhvvjqkwxyzéè'

def tuiles_lettres(base, colonnes=9, rangees=13, majuscules=False, mention='', dessin=None):
    """J36 : planche de tuiles-lettres à découper, pour composer des mots (lettres mobiles, jeux de mots croisés sur
    table). Les lettres suivent leur fréquence en français (FREQUENCES) ; un trait sous chaque lettre donne le bas
    de la tuile (b, d, p, q, n, u). Renvoie (chemin du PDF, nombre de tuiles, largeur et hauteur d'une tuile en mm)."""
    x0, y0, L, H = SURFACE_MM; d = dessin or Dessin(); n = colonnes * rangees; l, h = L / colonnes, H / rangees
    lettres = sorted(FREQUENCES[k * len(FREQUENCES) // n] if n <= len(FREQUENCES) else FREQUENCES[k % len(FREQUENCES)] for k in range(n))
    if n >= 26: lettres = sorted(set('abcdefghijklmnopqrstuvwxyz')) + sorted(FREQUENCES[k * len(FREQUENCES) // (n - 26)] for k in range(n - 26)); lettres.sort()
    t = min(l, h) * 1.75
    for i, z in enumerate(lettres):
        x, y = x0 + (i % colonnes) * l, y0 + (i // colonnes) * h; z = z.upper() if majuscules else z
        d.texte(x + l / 2, y + h * 0.66, z, t, police='Arial-B'); d.ligne([(x + l * 0.25, y + h * 0.85), (x + l * 0.75, y + h * 0.85)], ep=0.5)
    _decoupe(d, colonnes, rangees, mention)
    return (None if dessin else d.sauver(base)), n, (round(l, 1), round(h, 1))

def _sudoku(n, trous, graine):
    """Grille de sudoku n × n (4, 6 ou 9) à solution unique : renvoie (grille à trous, solution) ; 0 = case vide."""
    br, bc = {4: (2, 2), 6: (2, 3), 9: (3, 3)}[n]; alea = random.Random(graine)
    def ordre(taille, nb):                                                  # mélange des groupes, puis dans chaque groupe
        g = list(range(nb)); alea.shuffle(g); o = []
        for a in g: q = list(range(taille)); alea.shuffle(q); o += [a * taille + b for b in q]
        return o
    lig, col = ordre(br, n // br), ordre(bc, n // bc); ch = list(range(1, n + 1)); alea.shuffle(ch)
    sol = [[ch[(bc * (r % br) + r // br + c) % n] for c in col] for r in lig]
    def nombre(g, limite=2):                                                # nombre de solutions, arrêté à limite
        best = None
        for r in range(n):
            for c in range(n):
                if g[r][c] == 0:
                    pris = set(g[r]) | {g[k][c] for k in range(n)} | {g[a][b] for a in range(r - r % br, r - r % br + br) for b in range(c - c % bc, c - c % bc + bc)}
                    cand = [v for v in range(1, n + 1) if v not in pris]
                    if best is None or len(cand) < len(best[2]): best = (r, c, cand)
        if best is None: return 1
        total = 0
        for v in best[2]:
            g[best[0]][best[1]] = v; total += nombre(g, limite - total); g[best[0]][best[1]] = 0
            if total >= limite: break
        return total
    g = [row[:] for row in sol]; cases = [(r, c) for r in range(n) for c in range(n)]; alea.shuffle(cases); faits = 0
    for r, c in cases:
        if faits >= trous: break
        v = g[r][c]; g[r][c] = 0
        if nombre(g) == 1: faits += 1
        else: g[r][c] = v
    return g, sol

def sudoku(base, taille=6, grilles=2, trous=None, graine=1, solutions=False, titre='Sudoku', dessin=None):
    """J37 : sudokus de 4 × 4, 6 × 6 ou 9 × 9 cases, à solution unique (vérifiée par programme). grilles : nombre de
    grilles sur la page (1, 2 ou 4) ; solutions=True imprime les grilles remplies (page de l'enseignant·e).
    Renvoie (chemin du PDF, nombre de grilles, côté d'une case en mm)."""
    x0, y0, L, H = SURFACE_MM; d = dessin or Dessin(); n = taille; br, bc = {4: (2, 2), 6: (2, 3), 9: (3, 3)}[n]
    trous = trous or {4: 9, 6: 20, 9: 46}[n]
    haut = _bandeau(d, titre + (' : solutions' if solutions else ''), f'Chaque ligne, chaque colonne et chaque bloc contient une seule fois les nombres de 1 à {n}.')
    cg, rg = (2, 2) if grilles == 4 else (1, grilles); lz, hz = L / cg, (H - haut) / rg; cote = min(lz, hz) - 8; c = cote / n
    for k in range(grilles):
        g, sol = _sudoku(n, trous, graine + k); g = sol if solutions else g
        gx, gy = x0 + (k % cg) * lz + (lz - cote) / 2, y0 + haut + (k // cg) * hz + (hz - cote) / 2
        for r in range(n):
            for q in range(n):
                if g[r][q]: d.texte(gx + (q + 0.5) * c, gy + (r + 0.5) * c + c * 0.17, str(g[r][q]), c * 1.35, police='Arial-B' if not solutions else 'Arial')
        for i in range(n + 1):
            d.ligne([(gx + i * c, gy), (gx + i * c, gy + cote)], ep=1.3 if i % bc == 0 else 0.35); d.ligne([(gx, gy + i * c), (gx + cote, gy + i * c)], ep=1.3 if i % br == 0 else 0.35)
    return (None if dessin else d.sauver(base)), grilles, round(c, 1)

def _fleur(d, x, y, s, etapes=8):
    """La fleur du jeu du mot caché, dessinée jusqu'à l'étape donnée : tige, deux feuilles, cœur, quatre pétales.
    (x, y) : pied de la tige ; s : hauteur totale en mm."""
    if etapes >= 1: d.ligne([(x, y), (x, y - s * 0.62)], ep=0.9)
    for k, sx in ((2, -1), (3, 1)):
        if etapes >= k: d.ligne([(x, y - s * 0.22)] + [(x + sx * s * 0.2 * (t / 8), y - s * 0.22 - s * 0.16 * math.sin(math.pi * t / 8) * (1 if t <= 8 else 0) - s * 0.05 * t / 8) for t in range(9)] + [(x + sx * s * 0.2 * (t / 8), y - s * 0.22 - s * 0.05 * t / 8 + s * 0.05 * math.sin(math.pi * t / 8)) for t in range(8, -1, -1)], ep=0.7, ferme=True)
    cy = y - s * 0.75
    for k, (ax, ay) in ((5, (0, -1)), (6, (1, 0)), (7, (0, 1)), (8, (-1, 0))):
        if etapes >= k: d.cercle(x + ax * s * 0.16, cy + ay * s * 0.16, s * 0.1, ep=0.7, fond=(1, 1, 1))
    if etapes >= 4: d.cercle(x, cy, s * 0.085, ep=0.8, fond=(0.75, 0.75, 0.75))

def mot_cache_fleur(base, parties=3, titre='Le mot caché : la fleur', dessin=None):
    """J38 : jeu du mot caché à deux. Un élève choisit un mot et trace un tiret par lettre ; l'autre propose des lettres.
    Lettre absente du mot : celui qui a choisi le mot dessine une partie de la fleur (tige, feuille, feuille, cœur,
    quatre pétales). La fleur terminée en huit erreurs : le mot n'est pas trouvé. Aucune image de pendu.
    Renvoie (chemin du PDF, nombre de parties par fiche, nombre d'étapes de la fleur)."""
    x0, y0, L, H = SURFACE_MM; d = dessin or Dessin(); haut = _bandeau(d, titre, 'Lettre du mot : écris-la sur son tiret. Lettre absente : barre-la et dessine une partie de la fleur.')
    for k in range(1, 9):                                                   # le modèle, étape par étape
        xx = x0 + (k - 0.5) * L / 8; _fleur(d, xx, y0 + haut + 24, 22, k); d.texte(xx - 9, y0 + haut + 6, str(k), 9, police='Arial-B')
    yz = y0 + haut + 30; hz = (y0 + H - yz) / parties
    for p in range(parties):
        y = yz + p * hz; _cadre_arrondi(d, x0, y + 2, L, hz - 4, r=6, ep=0.9); lf = min(46.0, hz - 14)
        d.ligne([(x0 + L - lf - 6, y + 7), (x0 + L - 6, y + 7), (x0 + L - 6, y + hz - 7), (x0 + L - lf - 6, y + hz - 7)], ep=0.4, tirets=(1, 1.2), ferme=True)
        d.texte(x0 + L - lf / 2 - 6, y + hz - 9.5, 'ma fleur', 8); d.texte(x0 + 6, y + 13, 'Le mot (un tiret par lettre) :', 11, ancre='s', police='Arial-B')
        d.ligne([(x0 + 6, y + hz * 0.52), (x0 + L - lf - 12, y + hz * 0.52)], ep=0.3, tirets=(0.4, 1.4))
        lz = (L - lf - 20) / 13
        for i, z in enumerate('abcdefghijklmnopqrstuvwxyz'): d.texte(x0 + 8 + (i % 13 + 0.5) * lz, y + hz - 17 + (i // 13) * 7.5, z, 13)
    return (None if dessin else d.sauver(base)), parties, 8

def fiche_syllabes_sons(base, mots, colonnes=4, titre='Syllabes et sons', taille_pt=16, images=None, dessin=None, exemple=None):
    """G23 : fiche « syllabes et sons ». Par mot : un cadre pour l'image (collée par l'élève, ou insérée : images =
    liste de chemins), le mot écrit, une ligne où dessiner un carré par syllabe et une ligne où dessiner un jeton par son.
    Non-lecteurs (definir_jeunes, ou exemple donné) : aucune consigne écrite ; la première case est un exemple déjà
    fait, sur fond teinté : exemple = (mot, nombre de syllabes, nombre de sons), par défaut ('ballon', 2, 4), avec un
    ballon dessiné ; un petit carré et un petit rond remplacent les mots « syllabes » et « sons ».
    Renvoie (chemin du PDF, nombre de mots, largeur et hauteur d'une case en mm)."""
    x0, y0, L, H = SURFACE_MM; d = dessin or Dessin(); n = len(mots)
    if exemple is None and JEUNES[0]: exemple = ('ballon', 2, 4)
    dec = 1 if exemple else 0; r = -(-(n + dec) // colonnes)
    haut = _bandeau(d, titre, None if exemple else 'Colle l’image du mot. Dessine un carré par syllabe, puis un jeton par son.')
    d.texte(x0, y0 + haut + 5, _prenom(), 12, ancre='s'); yg = y0 + haut + 10; l, h = L / colonnes, (y0 + H - yg - (5 if exemple else 0)) / r
    for i, mot in enumerate(([exemple[0]] if exemple else []) + list(mots)):
        x, y = x0 + (i % colonnes) * l, yg + (i // colonnes) * h; hi = h - 34; ex = bool(exemple) and i == 0
        d.ligne([(x, y), (x + l, y), (x + l, y + h), (x, y + h)], ep=1.4 if ex else 0.7, ferme=True, fond=(0.9, 0.9, 0.9) if ex else None)
        if ex:                                                                # exemple déjà fait : un ballon, ses carrés, ses jetons
            cx, cy, rb = x + l / 2, y + 4 + (hi - 4) / 2, min(l - 12, hi - 8) / 2; d.cercle(cx, cy, rb, ep=1.0, fond=(1, 1, 1))
            d.ligne([(cx + rb * math.cos(a * math.pi / 20) * 0.45, cy + rb * math.sin(a * math.pi / 20)) for a in range(-10, 11)], ep=0.6); d.ligne([(cx - rb, cy), (cx + rb, cy)], ep=0.6)
        elif images and dessin is None: d.p.insert_image(d.f.Rect((x + 3) * d.k, (y + 3) * d.k, (x + l - 3) * d.k, (y + hi) * d.k), filename=images[i - dec])
        else: d.ligne([(x + 4, y + 4), (x + l - 4, y + 4), (x + l - 4, y + hi), (x + 4, y + hi)], ep=0.3, tirets=(1, 1.2), ferme=True)
        _texte_ajuste(d, x + l / 2, y + hi + 7, mot, taille_pt, l - 6, mini=10)
        for k, nom in enumerate(('syllabes', 'sons')):
            yy = y + hi + 11 + k * 11; d.ligne([(x, yy), (x + l, yy)], ep=0.3)
            if not exemple: d.texte(x + 2, yy + 3, nom, 6, ancre='s'); continue
            if k == 0: d.ligne([(x + 1.5, yy + 1.5), (x + 4.5, yy + 1.5), (x + 4.5, yy + 4.5), (x + 1.5, yy + 4.5)], ep=0.4, ferme=True)   # repère : carré = syllabe
            else: d.cercle(x + 3, yy + 3, 1.5, ep=0.4)                                                                               # repère : rond = son
            if ex:
                for j in range(exemple[1 + k]):
                    xj = x + 10 + j * 8.5
                    if k == 0: d.ligne([(xj, yy + 2), (xj + 6.5, yy + 2), (xj + 6.5, yy + 8.5), (xj, yy + 8.5)], ep=0.8, ferme=True, fond=(0.45, 0.45, 0.45))
                    else: d.cercle(xj + 3.2, yy + 5.3, 3.2, ep=0.8, fond=(0.45, 0.45, 0.45))
    if exemple: d.texte(x0, y0 + H - 0.5, 'Pour l’adulte : un carré par syllabe, un jeton par son. La première case montre l’exemple.', 7, ancre='s')
    return (None if dessin else d.sauver(base)), n, (round(l, 1), round(h, 1))

def livret_ecriture(base, module_mm=7.0, couleurs=True, feuilles=3, titre='Mon cahier d’écriture'):
    """G22, livret : cahier A5 de lignes d'écriture au lignage romand. Chaque feuille A4 paysage porte deux pages A5 ;
    impression recto-verso (retournement sur le bord court), pliage au milieu, agrafage dans le pli. La première
    face porte la couverture : le titre et un cartouche vide pour le prénom, sans ligne Prénom ni Classe (MP-O-03).
    Renvoie (chemin du PDF, nombre de pages A5 de lignes, module en mm)."""
    d = Dessin(297, 210); m = module_mm; assert feuilles >= 1
    def lignes(x, large):
        esp = max(5.0, 1.6 * m); n = int((180 + esp) / (3 * m + esp)); esp = (180 - n * 3 * m) / max(n - 1, 1)
        for i in range(n):
            y = 15 + i * (3 * m + esp)
            if couleurs:
                for k, c in enumerate(((0.83, 0.93, 1.0), (0.84, 0.95, 0.80), (0.99, 0.89, 0.78))): d.ligne([(x, y + k * m), (x + large, y + k * m), (x + large, y + (k + 1) * m), (x, y + (k + 1) * m)], ep=0, ferme=True, fond=c)
            d.ligne([(x, y), (x + large, y)], ep=0.3, tirets=(0.3, 1.2)); d.ligne([(x, y + m), (x + large, y + m)], ep=0.25)
            d.ligne([(x, y + 2 * m), (x + large, y + 2 * m)], ep=0.55); d.ligne([(x, y + 3 * m), (x + large, y + 3 * m)], ep=0.3, tirets=(0.3, 1.2))
    for face in range(2 * feuilles):
        if face: d.p = d.d.new_page(width=297 * d.k, height=210 * d.k)
        d.ligne([(148.5, 4), (148.5, 9)], ep=0.3); d.ligne([(148.5, 201), (148.5, 206)], ep=0.3)   # repères du pli
        if face == 0:                                                       # couverture à droite, dos à gauche
            _cadre_arrondi(d, 160.5, 14, 124.5, 182, r=8, ep=1.2); _cadre_arrondi(d, 163, 16.5, 119.5, 177, r=6.5, ep=0.35)
            d.texte(222.75, 70, titre, 22, police='Arial-B')
            _cadre_arrondi(d, 172.75, 98, 100, 36, r=6, ep=0.8)               # cartouche du prénom, sans ligne (MP-O-03) :
                                                                                # l'enfant l'écrit en grand, ou l'adulte y colle l'étiquette
            lignes(12, 124.5)
        else: lignes(12, 124.5); lignes(160.5, 124.5)
    d.d.save(base + '.pdf', garbage=4, deflate=True)
    return base + '.pdf', 4 * feuilles - 1, m
```

#### 21 novembre 2026 : maisons des nombres, quadrillage, calendrier, étiquettes, livret à onglets, journal, bande dessinée, exposé (G24 à G31)

Huit fonctions dessinent avec la classe `Dessin` (R11) les gabarits G24 à G31 : `maison_des_nombres`, `reproduction_quadrillage`, `calendrier_mensuel`, `etiquettes_horaire`, `livret_a_onglets`, `page_journal`, `planche_bd` et `plan_expose`. Le bloc se place après le bloc précédent (il utilise `_bandeau`, `_cadre_arrondi`, `_mention`, `_texte_ajuste` et `_decoupe`).

**Test (21.11.2026)** : vingt-trois pages produites et regardées sur le rendu PDF ; les jours de décembre 2026, de janvier et de février 2027 sont calculés par le module `calendar` ; police Liberation Sans à la place d'Arial ; non imprimé, non testé en classe.

```
# ---------- G24 à G31 : maison des nombres, quadrillage, calendrier, étiquettes, livret à onglets, journal, BD, exposé (21.11.2026) ----------
def maison_des_nombres(base, nombres=(5, 6, 7, 8), titre='Les maisons des nombres', dessin=None):
    """G24 : maisons des nombres. Le nombre est écrit dans le toit ; chaque étage reçoit deux nombres dont la somme
    est celle du toit (décompositions additives). nombres : 2 à 6 maisons par page.
    Renvoie (chemin du PDF, nombre de maisons, hauteur d'un étage en mm)."""
    x0, y0, L, H = SURFACE_MM; d = dessin or Dessin(); n = len(nombres); assert 2 <= n <= 6, 'de 2 à 6 maisons'
    haut = _bandeau(d, titre, None if JEUNES[0] else 'À chaque étage, écris deux nombres : ensemble, ils font le nombre du toit.')
    d.texte(x0, y0 + haut + 5, _prenom(), 12, ancre='s'); col = 2 if n <= 4 else 3; ran = -(-n // col)
    lz, hz = L / col, (H - haut - 10 - (5 if JEUNES[0] else 0)) / ran; et = 0
    if JEUNES[0]: d.texte(x0, y0 + H - 0.5, 'Pour l’adulte : à chaque étage, deux nombres qui font ensemble le nombre du toit. Le premier étage montre l’exemple.', 7, ancre='s')
    for i, nb in enumerate(nombres):
        x, y = x0 + (i % col) * lz + 6, y0 + haut + 10 + (i // col) * hz + 3; l, h = lz - 12, hz - 8; ht = min(30.0, h * 0.26); etages = nb + 1 if nb <= 6 else (nb + 2) // 2
        d.ligne([(x - 3, y + ht), (x + l / 2, y), (x + l + 3, y + ht)], ep=1.2, ferme=True, fond=(0.88, 0.88, 0.88)); d.texte(x + l / 2, y + ht * 0.78, str(nb), min(30, ht * 1.6), police='Arial-B')
        he = (h - ht) / etages; et = he
        for k in range(etages + 1): d.ligne([(x, y + ht + k * he), (x + l, y + ht + k * he)], ep=1.0 if k in (0, etages) else 0.4)
        if JEUNES[0]:                                                         # non-lecteurs : le premier étage est déjà rempli
            d.ligne([(x, y + ht), (x + l, y + ht), (x + l, y + ht + he), (x, y + ht + he)], ep=0, ferme=True, fond=(0.9, 0.9, 0.9)); te = min(26, he * 1.9)
            pe = police_exemple_pdf(); te = te * 0.9 if pe == 'Eleve' else te   # MP-T-10 : l'exemple en police d'élèves
            dy = te * (0.14 if pe == 'Eleve' else 0.125)                     # ligne de base : chiffres centrés dans l'étage
            d.texte(x + l / 4, y + ht + he / 2 + dy, '1', te, police=pe); d.texte(x + 3 * l / 4, y + ht + he / 2 + dy, str(nb - 1), te, police=pe)
            d.ligne([(x, y + ht), (x + l, y + ht)], ep=1.0); d.ligne([(x, y + ht + he), (x + l, y + ht + he)], ep=0.4)
        for xx, ep in ((x, 1.0), (x + l / 2, 0.4), (x + l, 1.0)): d.ligne([(xx, y + ht), (xx, y + h)], ep=ep)
    return (None if dessin else d.sauver(base)), n, round(et, 1)

FIGURES = {'maison': [[(1, 6), (1, 3), (4, 0), (7, 3), (7, 6), (1, 6)], [(3, 6), (3, 4), (5, 4), (5, 6)], [(1, 3), (7, 3)]],
           'bateau': [[(0, 5), (8, 5), (6, 7), (2, 7), (0, 5)], [(4, 5), (4, 0), (7, 4), (4, 4)], [(4, 1), (1, 4), (4, 4)]],
           'sapin': [[(4, 0), (6, 2), (5, 2), (7, 4), (6, 4), (8, 6), (5, 6), (5, 7), (3, 7), (3, 6), (0, 6), (2, 4), (1, 4), (3, 2), (2, 2), (4, 0)]],
           'fusée': [[(4, 0), (6, 2), (6, 6), (7, 7), (5, 7), (5, 6), (3, 6), (3, 7), (1, 7), (2, 6), (2, 2), (4, 0)], [(3, 3), (5, 3), (5, 4), (3, 4), (3, 3)]]}

def reproduction_quadrillage(base, figure='maison', cases=(8, 7), points=False, titre='Je reproduis la figure', dessin=None):
    """G25 : reproduction d'une figure sur quadrillage. En haut, le modèle ; en bas, le même quadrillage vide.
    figure : nom d'une figure de FIGURES, ou liste de lignes brisées (points aux nœuds du quadrillage) ;
    cases : (colonnes, rangées) ; points=True remplace le quadrillage du bas par les seuls nœuds (plus difficile).
    Renvoie (chemin du PDF, nombre de segments à tracer, côté d'un carreau en mm)."""
    x0, y0, L, H = SURFACE_MM; d = dessin or Dessin(); fig = FIGURES[figure] if isinstance(figure, str) else figure; c, r = cases
    haut = _bandeau(d, titre, 'Observe le modèle. Trace la même figure sur le quadrillage du bas, à la règle.')
    d.texte(x0, y0 + haut + 5, _prenom(), 12, ancre='s'); hz = (H - haut - 14) / 2; pas = min((L - 10) / c, (hz - 12) / r, 14.0)
    for k, nom in enumerate(('Le modèle', 'À toi')):
        gx, gy = x0 + (L - c * pas) / 2, y0 + haut + 14 + k * hz + 6; d.texte(x0, gy - 2, nom, 12, ancre='s', police='Arial-B')
        if k == 1 and points:
            for i in range(c + 1):
                for j in range(r + 1): d.cercle(gx + i * pas, gy + j * pas, 0.5, ep=0, fond=(0, 0, 0))
        else:
            for i in range(c + 1): d.ligne([(gx + i * pas, gy), (gx + i * pas, gy + r * pas)], ep=0.25)
            for j in range(r + 1): d.ligne([(gx, gy + j * pas), (gx + c * pas, gy + j * pas)], ep=0.25)
        if k == 0:
            for ligne in fig: d.ligne([(gx + a * pas, gy + b * pas) for a, b in ligne], ep=1.3)
    assert all(0 <= a <= c and 0 <= b <= r for ligne in fig for a, b in ligne), 'figure hors du quadrillage'
    return (None if dessin else d.sauver(base)), sum(len(q) - 1 for q in fig), round(pas, 1)

MOIS = ('janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre')

def calendrier_mensuel(base, annee, mois, titre=None, dessin=None):
    """G26 : calendrier d'un mois, semaine du lundi au dimanche, grandes cases pour écrire ou coller une étiquette.
    Les jours sont calculés par programme. Renvoie (chemin du PDF, nombre de jours, hauteur d'une case en mm)."""
    import calendar
    x0, y0, L, H = SURFACE_MM; d = dessin or Dessin(); semaines = calendar.Calendar(firstweekday=0).monthdayscalendar(annee, mois)
    haut = _bandeau(d, titre or f'{MOIS[mois - 1].capitalize()} {annee}', 'Chaque jour : la date, le temps qu’il fait, un événement de la classe.')
    he = 10.0; l, h = L / 7, (H - haut - he) / len(semaines); y1 = y0 + haut
    d.ligne([(x0, y1), (x0 + L, y1), (x0 + L, y1 + he), (x0, y1 + he)], ep=0, ferme=True, fond=(0.85, 0.85, 0.85))
    for i, j in enumerate(('lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche')): d.texte(x0 + (i + 0.5) * l, y1 + he / 2 + 1.5, j, 11, police='Arial-B')
    for s, semaine in enumerate(semaines):
        for i, jour in enumerate(semaine):
            x, y = x0 + i * l, y1 + he + s * h
            d.ligne([(x, y), (x + l, y), (x + l, y + h), (x, y + h)], ep=0.5, ferme=True, fond=(0.94, 0.94, 0.94) if (i >= 5 or not jour) else (1, 1, 1))
            if jour: d.texte(x + 3, y + 7.5, str(jour), 16, ancre='s', police='Arial-B')
    d.ligne([(x0, y1), (x0 + L, y1), (x0 + L, y0 + H), (x0, y0 + H)], ep=1.1, ferme=True)
    return (None if dessin else d.sauver(base)), calendar.monthrange(annee, mois)[1], round(h, 1)

def etiquettes_horaire(base, etiquettes, colonnes=2, rangees=8, taille_pt=20, mention='', dessin=None):
    """G27 : étiquettes de l'horaire de la journée, à afficher dans l'ordre. Par étiquette : un cadre pour un
    pictogramme (dessiné, collé ou inséré) et le nom de l'activité. Renvoie (chemin du PDF, nombre d'étiquettes,
    largeur et hauteur en cm)."""
    x0, y0, L, H = SURFACE_MM; d = dessin or Dessin(); l, h = L / colonnes, H / rangees; assert len(etiquettes) <= colonnes * rangees
    for i, t in enumerate(etiquettes):
        x, y = x0 + (i % colonnes) * l, y0 + (i // colonnes) * h; c = h - 8
        _cadre_arrondi(d, x + 4, y + 4, c, c, r=3, ep=0.6); _texte_ajuste(d, x + c + 8 + (l - c - 12) / 2, y + h / 2 + 0.5, t, taille_pt, l - c - 14, 'Arial-B', mini=10)
    _decoupe(d, colonnes, rangees, mention)
    return (None if dessin else d.sauver(base)), len(etiquettes), (round(l / 10, 2), round(h / 10, 2))

def livret_a_onglets(base, onglets, titre='Mon livret', pas_mm=14.0):
    """G28 : livret à onglets étagés. Une feuille par onglet : chaque feuille est coupée un peu plus court que la
    suivante, de sorte que tous les onglets restent visibles en bas ; les feuilles s'agrafent en haut.
    onglets : 3 à 8 titres, du premier (feuille la plus courte) au dernier (feuille entière).
    Renvoie (chemin du PDF, nombre de feuilles, hauteur d'un onglet en mm)."""
    x0, y0, L, H = SURFACE_MM; d = Dessin(); n = len(onglets); assert 3 <= n <= 8, 'de 3 à 8 onglets'
    for k, nom in enumerate(onglets):
        if k: d.p = d.d.new_page(width=210 * d.k, height=297 * d.k)
        bas = y0 + H - (n - 1 - k) * pas_mm; _mention(d, f'{titre} · feuille {k + 1} sur {n} · couper sur le pointillé, agrafer en haut')
        if k == 0: d.texte(x0 + L / 2, y0 + 16, titre, 26, police='Arial-B'); d.texte(x0 + L / 2, y0 + 30, 'Prénom : ____________________', 13)
        else: d.texte(x0, y0 + 12, nom, 18, ancre='s', police='Arial-B')
        for j in range(int((bas - pas_mm - y0 - (40 if k == 0 else 22)) / 11)): d.ligne([(x0, y0 + (48 if k == 0 else 30) + j * 11), (x0 + L, y0 + (48 if k == 0 else 30) + j * 11)], ep=0.25)
        d.ligne([(x0, bas - pas_mm), (x0 + L, bas - pas_mm), (x0 + L, bas), (x0, bas)], ep=0.8, ferme=True, fond=(0.88, 0.88, 0.88)); d.texte(x0 + L / 2, bas - pas_mm / 2 + 1.8, nom, 14, police='Arial-B')
        if k < n - 1: d.ligne([(0, bas), (210, bas)], ep=0.35, tirets=(1, 1.2))
        d.ligne([(x0, y0), (x0 + L, y0), (x0 + L, bas), (x0, bas)], ep=0.5, ferme=True)
    d.d.save(base + '.pdf', garbage=4, deflate=True)
    return base + '.pdf', n, pas_mm

def page_journal(base, titre='Le journal de la classe', articles=3, dessin=None):
    """G29 : page de journal de classe à remplir à la main : bandeau du titre, numéro et date, puis des articles sur
    deux colonnes (titre, cadre d'illustration, lignes d'écriture, signature). articles : 2 à 4.
    Renvoie (chemin du PDF, nombre d'articles, interligne en mm)."""
    x0, y0, L, H = SURFACE_MM; d = dessin or Dessin(); assert 2 <= articles <= 4
    d.ligne([(x0, y0), (x0 + L, y0), (x0 + L, y0 + 24), (x0, y0 + 24)], ep=1.2, ferme=True, fond=(0.9, 0.9, 0.9)); d.texte(x0 + L / 2, y0 + 15, titre, 26, police='Arial-B')
    d.texte(x0, y0 + 31, 'Numéro ______', 11, ancre='s'); d.texte(x0 + L - d.largeur_texte('Date : ____________________', 11), y0 + 31, 'Date : ____________________', 11, ancre='s')
    d.ligne([(x0, y0 + 34), (x0 + L, y0 + 34)], ep=0.8); zones = {2: [(0, 0, 1, 1), (1, 0, 1, 1)], 3: [(0, 0, 1, 1), (1, 0, 1, 0.5), (1, 0.5, 1, 0.5)], 4: [(0, 0, 1, 0.5), (1, 0, 1, 0.5), (0, 0.5, 1, 0.5), (1, 0.5, 1, 0.5)]}[articles]
    yz = y0 + 38; hz = y0 + H - yz; lc = (L - 8) / 2; il = 9.0
    for cx, fy, _, fh in zones:
        x, y, h = x0 + cx * (lc + 8), yz + fy * hz + 2, fh * hz - 6
        d.ligne([(x, y + 9), (x + lc, y + 9)], ep=0.9); d.texte(x, y + 3.5, 'Titre :', 8, ancre='s'); hi = min(42.0, h * 0.3)
        d.ligne([(x, y + 13), (x + lc, y + 13), (x + lc, y + 13 + hi), (x, y + 13 + hi)], ep=0.4, tirets=(1, 1.2), ferme=True); d.texte(x + lc / 2, y + 13 + hi / 2 + 1, 'dessin ou photo', 8)
        for j in range(int((h - hi - 30) / il)): d.ligne([(x, y + hi + 24 + j * il), (x + lc, y + hi + 24 + j * il)], ep=0.25)
        d.texte(x, y + h - 1, 'Écrit par : ____________________', 9, ancre='s')
    d.ligne([(x0 + lc + 4, yz), (x0 + lc + 4, y0 + H)], ep=0.3)
    return (None if dessin else d.sauver(base)), articles, il

def planche_bd(base, rangees=(2, 3, 2), titre=True, dessin=None):
    """G30 : planche de bande dessinée vide. rangees : nombre de cases de chaque bande, de haut en bas
    (par exemple (2, 3, 2)) ; titre=True réserve un bandeau pour le titre et le nom de l'auteur·e.
    Renvoie (chemin du PDF, nombre de cases, hauteur d'une bande en mm)."""
    x0, y0, L, H = SURFACE_MM; d = dessin or Dessin(); g = 5.0; haut = 20.0 if titre else 0.0
    if titre: _cadre_arrondi(d, x0, y0, L, 15, r=4, ep=0.9); d.texte(x0 + 4, y0 + 9.5, 'Titre :', 11, ancre='s', police='Arial-B'); d.texte(x0 + L - 62, y0 + 9.5, 'Par :', 11, ancre='s', police='Arial-B')
    hb = (H - haut - g * (len(rangees) - 1)) / len(rangees); n = 0
    for j, nb in enumerate(rangees):
        lc = (L - g * (nb - 1)) / nb
        for i in range(nb):
            x, y = x0 + i * (lc + g), y0 + haut + j * (hb + g); d.ligne([(x, y), (x + lc, y), (x + lc, y + hb), (x, y + hb)], ep=1.2, ferme=True); n += 1
            d.texte(x + 3, y + 5, str(n), 8, ancre='s')
    return (None if dessin else d.sauver(base)), n, round(hb, 1)

def plan_expose(base, parties=3, titre='Mon exposé', dessin=None):
    """G31 : plan d'exposé sur une page : sujet et question de départ, deux à quatre parties (idée principale, mots-clés,
    image à montrer), conclusion, sources. Renvoie (chemin du PDF, nombre de parties, hauteur d'une partie en mm)."""
    x0, y0, L, H = SURFACE_MM; d = dessin or Dessin(); assert 2 <= parties <= 4
    haut = _bandeau(d, titre, 'Prépare ton exposé : une idée par partie, quelques mots-clés, pas de phrases entières.')
    def bloc(y, h, nom, lignes):
        _cadre_arrondi(d, x0, y, L, h, r=4, ep=0.8); d.texte(x0 + 4, y + 6.5, nom, 11, ancre='s', police='Arial-B')
        for j in range(lignes): d.ligne([(x0 + 4, y + 15 + j * 9), (x0 + L - 4, y + 15 + j * 9)], ep=0.25)
    y = y0 + haut; d.texte(x0, y + 5, 'Prénom : ____________________', 12, ancre='s'); y += 9
    bloc(y, 28, 'Mon sujet et ma question de départ', 2); y += 31; hp = (y0 + H - y - 31 - 22 - 3 * (parties + 1)) / parties
    for k in range(parties):
        _cadre_arrondi(d, x0, y, L, hp, r=4, ep=0.8); d.texte(x0 + 4, y + 6.5, f'Partie {k + 1} : mon idée principale', 11, ancre='s', police='Arial-B'); li = hp - 14
        d.ligne([(x0 + L - 4 - li, y + 10), (x0 + L - 4, y + 10), (x0 + L - 4, y + 10 + li - 2), (x0 + L - 4 - li, y + 10 + li - 2)], ep=0.4, tirets=(1, 1.2), ferme=True); d.texte(x0 + L - 4 - li / 2, y + 10 + li / 2, 'image à montrer', 8)
        for j in range(int((hp - 12) / 9)): d.ligne([(x0 + 4, y + 16 + j * 9), (x0 + L - 10 - li, y + 16 + j * 9)], ep=0.25)
        y += hp + 3
    bloc(y, 31, 'Ma conclusion : ce qu’il faut retenir', 2); y += 34; bloc(y, 22, 'Mes sources (livre, site, personne interrogée)', 1)
    return (None if dessin else d.sauver(base)), parties, round(hp, 1)
```

#### 21 novembre 2026 : bande de lignes d'écriture romandes dans une fiche (R1c)

`bande_lignage` dessine avec la classe `Dessin` (R11) une bande de une à douze lignes d'écriture au lignage romand, de la largeur utile de la fiche (16 cm par défaut) : le même tracé que la page G22, sans en-tête. Elle remplace les lignes simples R1a dans une zone d'écriture quand l'enseignant·e de 1P à 4P le demande ; l'image PNG s'insère à l'échelle 1 avec `inserer_image(doc, chemin, largeur_cm=16)`. Le bloc se place après `Dessin` et `inserer_image`.

**Test (21.11.2026)** : bandes de trois lignes produites en modules de 7 mm et de 4 mm, en noir et blanc et en couleur, et regardées sur le rendu ; insertion dans un .docx contrôlée (largeur de 16 cm) ; non imprimé, non testé en classe ; modules à confirmer avec les cahiers de l'établissement.

```
# ---------- Pictogramme de consigne composé : le geste et le mot visé (21.11.2026) ----------
def pictogramme_consigne(base, geste='entoure', mot='verbe', hauteur_mm=13.0, dpi=300):
    """Pictogramme qui porte la consigne entière : le mot visé (« verbe », « nom », « sujet », un son…) avec le geste
    à faire dessus. geste : 'entoure' (ovale), 'encadre' (rectangle), 'souligne' (trait dessous), 'barre' (trait
    en travers). Remplace le pictogramme générique « abc » quand la consigne vise une chose précise ; se place à
    gauche de la consigne écrite, qu'il ne remplace jamais (MP-C-02). Renvoie (chemin du PNG, largeur en cm) ;
    insertion à l'échelle : inserer_image(doc, chemin, largeur_cm=largeur)."""
    assert geste in ('entoure', 'encadre', 'souligne', 'barre'), 'geste inconnu : ' + geste
    t = hauteur_mm * 1.25; d0 = Dessin(60, 20); lm = d0.largeur_texte(mot, t, 'Arial-B'); H = hauteur_mm; L = lm + H * 1.1; d = Dessin(L, H)
    cx, cy = L / 2, H / 2; d.texte(cx, cy + t * 0.125, mot, t, police='Arial-B')
    if geste == 'entoure': d.ligne([(cx + (L / 2 - 0.8) * math.cos(a * math.pi / 30), cy + (H / 2 - 0.8) * math.sin(a * math.pi / 30)) for a in range(60)], ep=0.8, ferme=True)
    elif geste == 'encadre': d.ligne([(0.8, 0.8), (L - 0.8, 0.8), (L - 0.8, H - 0.8), (0.8, H - 0.8)], ep=0.8, ferme=True)
    elif geste == 'souligne': d.ligne([(cx - lm / 2, H - 1.6), (cx + lm / 2, H - 1.6)], ep=0.9)
    else: d.ligne([(cx - lm / 2 - 1, H - 2.0), (cx + lm / 2 + 1, 2.0)], ep=0.9)
    d.sauver(base)
    return d.png(base, dpi), round(L / 10, 2)

# ---------- R1c : bande de lignes d'écriture romandes, à insérer dans une fiche (21.11.2026) ----------
def bande_lignage(base, lignes=3, module_mm=7.0, couleurs=False, largeur_mm=160.0, dpi=300):
    """R1c : bande de lignes d'écriture au lignage romand, pour une zone d'écriture d'une fiche (1P à 4P, si
    l'enseignant·e la préfère aux lignes simples R1a). Même tracé que la page G22 : plafond et plancher en
    pointillés, ligne du corps en trait fin, ligne de base en trait épais. module_mm : 7 pour l'entrée dans
    l'écriture, 4 ensuite. couleurs=True colore les couloirs ciel, herbe, terre (impression en couleur).
    Écrit base.svg, base.pdf et base.png ; renvoie (chemin du PNG, hauteur en cm). Insertion à l'échelle 1 :
    inserer_image(doc, chemin, largeur_cm=largeur_mm / 10)."""
    m = module_mm; assert 2 <= m <= 10, 'module de 2 à 10 mm'; assert 1 <= lignes <= 12, '1 à 12 lignes'
    esp = max(4.0, 1.2 * m); H = lignes * 3 * m + (lignes - 1) * esp + 1.0; L = largeur_mm; d = Dessin(L, H)
    for i in range(lignes):
        y = 0.5 + i * (3 * m + esp)
        if couleurs:
            for k, c in enumerate(((0.83, 0.93, 1.0), (0.84, 0.95, 0.80), (0.99, 0.89, 0.78))): d.ligne([(0, y + k * m), (L, y + k * m), (L, y + (k + 1) * m), (0, y + (k + 1) * m)], ep=0, ferme=True, fond=c)
        d.ligne([(0, y), (L, y)], ep=0.3, tirets=(0.3, 1.2)); d.ligne([(0, y + m), (L, y + m)], ep=0.25)
        d.ligne([(0, y + 2 * m), (L, y + 2 * m)], ep=0.55); d.ligne([(0, y + 3 * m), (L, y + 3 * m)], ep=0.3, tirets=(0.3, 1.2))
    d.sauver(base)
    return d.png(base, dpi), round(H / 10, 2)
```

#### Exemple d'usage (fiche, puis jeu)

```
doc = Document(); page_a4(doc, police="Arial", taille=14); styles_fiche(doc, 14)
entete(doc, "Le passé composé", "J'écris un verbe au passé composé avec ses deux parties.")  # R7 : la phrase seule
paragraphe(doc, "1\tÉcris la phrase au passé composé.", "Fiche-Consigne")
paragraphe(doc, "a) Nous jouons au ballon.", "Fiche-Données")
lignes_ecriture(doc, 2)                                   # R1a : 2 vraies lignes de 1 cm
ligne_tabulation(doc, "Le matin, j'ai ", "Fiche-Données")  # R1b : amorce + ligne
paragraphe(doc, "b) Hier, tu " + lacune(6) + " (chanter).", "Fiche-Lacune")  # R2
# Jeu : dominos = [(réponse, question)] dans l'ordre de la boucle
verifier_domino_boucle(dominos, solution)                 # V11
def regle_du_jeu(cellule, largeur):                       # un exemplaire de la règle (liste regle)
    cellule.paragraphs[0].text = "Règle du jeu"
    for i, e in enumerate(regle, 1):
        cellule.add_paragraph(f"{i}. {e}")
planche_A5(doc, regle_du_jeu)                              # R15 : deux exemplaires A5 sur une feuille A4
nouvelle_section_a4(doc)                                   # retour à l'A4 pour la planche de pièces
ordre = melanger_sans_voisins(dominos, graine=3)           # MP-J-03
planche_pieces(doc, [[[[(r, {"b": True})]], [q[0], f"({q[1]})"]] for r, q in ordre],
               mention="Boucle Lune · 16 dominos · à découper sur les pointillés")  # R8
```

**Exemple de vérification d'un domino-boucle (V11)** : script du test du 30.10.2026. Il calcule les formes du présent (verbes en -er réguliers et verbes en -ir du type finir), construit deux boucles, vérifie l'unicité de chaque forme, l'unicité de la réponse à chaque question et la fermeture, puis mélange l'ordre d'impression sans voisins.

```
"""Données du domino-boucle : conjugaison calculée, boucles construites et vérifiées."""
import random

PERS = {'je': 1, 'tu': 2, 'il': 3, 'elle': 3, 'on': 3, 'nous': 4, 'vous': 5, 'ils': 6, 'elles': 6}
GN = {'Tom et moi': 4, 'Mes amies': 6, 'Le chat': 3, 'Lina et toi': 5, 'Mes parents': 6,
      'Le bébé': 3, 'Léa et moi': 4, 'Les arbres': 6, 'Ma tante': 3, 'Noé et toi': 5, 'Les élèves': 6}
PRONOM_DE = {1: 'je', 2: 'tu', 3: 'il, elle, on', 4: 'nous', 5: 'vous', 6: 'ils, elles'}

def personne(sujet):
    return PERS.get(sujet) or GN[sujet]

def groupe(verbe):
    return 'er' if verbe.endswith('er') else 'ir'

def present(verbe, p):
    """Présent de l'indicatif : verbes réguliers en -er (sans -cer, -ger, -yer, -eler, -eter)
    et verbes en -ir du type finir (2e groupe)."""
    rad = verbe[:-2]
    if groupe(verbe) == 'er':
        assert not verbe.endswith(('cer', 'ger', 'yer', 'eler', 'eter')), verbe
        return rad + ['e', 'es', 'e', 'ons', 'ez', 'ent'][p - 1]
    return rad + ['is', 'is', 'it', 'issons', 'issez', 'issent'][p - 1]

def terminaison(verbe, p):
    return present(verbe, p)[len(verbe) - 2:]

# Items (sujet, verbe) — 4 verbes × 4 formes distinctes par boucle
LUNE = [('je', 'chanter'), ('tu', 'chanter'), ('nous', 'chanter'), ('elles', 'chanter'),
        ('on', 'jouer'), ('tu', 'jouer'), ('vous', 'jouer'), ('ils', 'jouer'),
        ('je', 'choisir'), ('elle', 'choisir'), ('nous', 'choisir'), ('ils', 'choisir'),
        ('tu', 'remplir'), ('il', 'remplir'), ('vous', 'remplir'), ('elles', 'remplir')]

SOLEIL = [('je', 'danser'), ('Tom et moi', 'danser'), ('Mes amies', 'danser'), ('tu', 'danser'),
          ('Le chat', 'regarder'), ('tu', 'regarder'), ('Lina et toi', 'regarder'), ('Mes parents', 'regarder'),
          ('je', 'grandir'), ('Le bébé', 'grandir'), ('Léa et moi', 'grandir'), ('Les arbres', 'grandir'),
          ('tu', 'réussir'), ('Ma tante', 'réussir'), ('Noé et toi', 'réussir'), ('Les élèves', 'réussir')]

def boucle(items, graine):
    """Ordre circulaire : groupes alternés (-er / -ir), jamais deux fois le même sujet de suite."""
    rng = random.Random(graine)
    er = [i for i in items if groupe(i[1]) == 'er']
    ir = [i for i in items if groupe(i[1]) == 'ir']
    for _ in range(10000):
        rng.shuffle(er); rng.shuffle(ir)
        seq = [x for pair in zip(er, ir) for x in pair]
        ok = all(seq[k][0] != seq[(k + 1) % len(seq)][0] and seq[k][1] != seq[(k + 1) % len(seq)][1]
                 for k in range(len(seq)))
        # éviter deux occurrences consécutives du même verbe à deux positions d'écart (variété)
        ok = ok and all(seq[k][1] != seq[(k + 2) % len(seq)][1] for k in range(len(seq)))
        if ok:
            return seq
    raise RuntimeError('pas de boucle')

def dominos(seq):
    """Domino k = [forme de l'item k | item k+1] ; le dernier renvoie au premier."""
    n = len(seq)
    return [(present(seq[k][1], personne(seq[k][0])), seq[(k + 1) % n]) for k in range(n)]

def verifier(seq, nom):
    ds = dominos(seq)
    formes = [d[0] for d in ds]
    assert len(set(formes)) == len(formes), f'{nom} : formes en double'
    # chaque moitié droite a exactement une moitié gauche correspondante
    for d in ds:
        s, v = d[1]
        rep = present(v, personne(s))
        assert formes.count(rep) == 1, (nom, d)
    # la chaîne parcourue depuis n'importe quel domino revient au départ après n poses
    par_forme = {d[0]: d for d in ds}
    d = ds[0]
    for _ in range(len(ds)):
        s, v = d[1]
        d = par_forme[present(v, personne(s))]
    assert d == ds[0]
    return ds

def ordre_impression(ds, graine):
    rng = random.Random(graine)
    o = ds[:]
    while True:
        rng.shuffle(o)
        # aucune paire voisine sur la planche ne doit être une paire voisine de la boucle
        pos = {d: i for i, d in enumerate(ds)}
        if all(abs(pos[o[k]] - pos[o[k + 1]]) % len(ds) not in (1, len(ds) - 1) for k in range(len(o) - 1)):
            return o

SEQ_LUNE = boucle(LUNE, 5)
SEQ_SOLEIL = boucle(SOLEIL, 11)
DOM_LUNE = verifier(SEQ_LUNE, 'Lune')
DOM_SOLEIL = verifier(SEQ_SOLEIL, 'Soleil')
IMP_LUNE = ordre_impression(DOM_LUNE, 3)
IMP_SOLEIL = ordre_impression(DOM_SOLEIL, 7)

# Fiche « Après le jeu » : items G3 (sujet, verbe, début, fin)
FICHE = [('a', 'Je ', 'marcher', ' jusqu’à l’école.', 'je'),
         ('b', 'Tu ', 'remplir', ' ta gourde.', 'tu'),
         ('c', 'Mes cousins ', 'bâtir', ' une cabane.', 'ils'),
         ('d', 'Vous ', 'dessiner', ' un dragon.', 'vous'),
         ('e', 'Ma voisine ', 'nourrir', ' son chat.', 'elle')]

if __name__ == '__main__':
    for nom, seq, ds in (('LUNE', SEQ_LUNE, DOM_LUNE), ('SOLEIL', SEQ_SOLEIL, DOM_SOLEIL)):
        print(nom)
        for k, d in enumerate(ds, 1):
            print(f'{k:2d}  [{d[0]:13s}| {d[1][0]} ({d[1][1]})]')
    for it in FICHE:
        print(it[0], present(it[2], PERS[it[4]]))
    for v in ('parler', 'finir'):
        print([present(v, p) for p in range(1, 7)])
```

# ANNEXE I-D — LISTE DES CODES DU LIVRE II (NOMS SEULEMENT)
<!-- modules : noyau -->

Ce fichier contient le Livre I seul. Les définitions complètes des fonctions, patrons, micro-formats et types de ressources figurent dans le Livre II (fichier complet). Pour une fiche courante, cette liste, le tableau 3.5 et le catalogue des gabarits (§ 3.3) suffisent ; pour un choix pédagogique fin, utiliser le fichier complet.

## Fonctions pédagogiques (F01 à F43)
<!-- modules : noyau, sequences -->

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
<!-- modules : noyau, sequences -->

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

## Fonctions pour le travail enseignant (E01 à E11)

- E01 — Planifier
- E02 — Piloter
- E03 — Observer
- E04 — Analyser
- E05 — Adapter
- E06 — Communiquer et assurer le suivi
- E07 — Renouveler et générer des variantes
- E08 — Transformer les modalités pédagogiques
- E09 — Créer des supports complémentaires
- E10 — Analyser et auditer une ressource
- E11 — Personnaliser avec discernement

## Patrons pédagogiques (P01 à P24)

- P01 — Le défi initial
- P02 — L'enquête par indices
- P03 — La comparaison contrastée
- P04 — L'erreur à débusquer
- P05 — Le choix argumenté
- P06 — L'exemple guidé puis autonome
- P07 — Le tri raisonné
- P08 — Les associations à justifier
- P09 — Prédire, tester, expliquer
- P10 — Le cas à résoudre
- P11 — Les experts complémentaires
- P12 — La production sous contraintes
- P13 — La confrontation des solutions
- P14 — Le rappel actif progressif
- P15 — Les ateliers différenciés
- P16 — Le transfert de contexte
- P17 — L'investigation critique des sources
- P18 — Le retour sur sa démarche
- P19 — Le rallye de postes
- P20 — Apprivoiser un outil de référence
- P21 — Même tâche, plusieurs temps
- P22 — Les élèves conçoivent l'exercice
- P23 — Du vécu corporel à la trace
- P24 — La dictée réfléchie

## Micro-formats (MF01 à MF76)

- MF01 — Image à annoter
- MF02 — Schéma à compléter
- MF03 — Carte mentale ou carte conceptuelle à enrichir
- MF04 — Document avec indices à relever
- MF05 — Observation guidée
- MF06 — Prédiction à vérifier
- MF07 — Tableau à double entrée
- MF08 — Classement multicritère
- MF09 — Frise ou ligne du temps
- MF10 — Carte à légender
- MF11 — Arbre de décision
- MF12 — Fiche-synthèse structurée
- MF13 — Exercice à difficulté progressive
- MF14 — Procédure partiellement complétée
- MF15 — Situation d'application variée
- MF16 — Vrai / faux justifié
- MF17 — Appariement avec distracteurs
- MF18 — Carte de rappel
- MF19 — Dispositif « JE / JE PENSE / JE CONCLUS »
- MF20 — Argument à compléter
- MF21 — Comparaison avant / après
- MF22 — Reformulation ciblée
- MF23 — Défi de production
- MF24 — Conclusion argumentée
- MF25 — Think / pair / share écrit
- MF26 — Fiche expert
- MF27 — Grille de restitution
- MF28 — Débat structuré (fiche)
- MF29 — Production collaborative à rôles
- MF30 — Annotation croisée
- MF31 — Autoévaluation critériée
- MF32 — Échelle de confiance
- MF33 — Bilan d'erreur
- MF34 — Question de transfert
- MF35 — Carnet d'apprentissage
- MF36 — Diagnostic court
- MF37 — Tri matériel d’objets
- MF38 — Séquence gestuelle ou motrice
- MF39 — Association son–image–objet
- MF40 — Récit construit avec images
- MF41 — Dictée à l’adulte ou transcription accompagnée
- MF42 — Parcours spatial ou manipulation située
- MF43 — Tableau de suivi de progrès
- MF44 — Ticket de sortie et décision pédagogique
- MF45 — Boucle rétroaction–révision–nouvel essai
- MF46 — Variantes équivalentes d’une même tâche
- MF47 — Transposition de modalité
- MF48 — Fiche de communication simplifiée
- MF49 — Problème en 3 étapes (mathématiques)
- MF50 — Schéma en barres / \*bar model\* (mathématiques)
- MF51 — Procédure en deux lignes (mathématiques, autoexplicitation)
- MF52 — Observe → Décris → Explique (sciences)
- MF53 — Expérience « recette » (sciences)
- MF54 — Analyse d'un document source (SHS)
- MF55 — Avant / Après (histoire, SHS)
- MF56 — Analyse sensible (arts visuels, musique)
- MF57 — Mini-dialogue à trous (langues étrangères)
- MF58 — Résumé 3-2-1 (toutes disciplines, bilan)
- MF59 — Triple codage du nombre
- MF60 — Arcs syllabiques
- MF61 — Compteur de progression illustré
- MF63 — Record personnel
- MF64 — Message codé autovalidant
- MF66 — Double modèle script / cursif
- MF67 — Repère de latéralité
- MF68 — Rubrique « pour mes camarades »
- MF70 — Geste mnémotechnique
- MF71 — Acronyme de stratégie
- MF73 — Cases d'aménagements accordés
- MF74 — Piège nommé, avec origine et autotest
- MF75 — Dictée réfléchie (trous, choix, négociation)
- MF76 — Rotation des rôles

*Les numéros MF62, MF65, MF69 et MF72 ne sont pas attribués : ces candidats du balayage BDRP sont devenus des variantes de MF32, MP-J-04, MF12 et MF02.*

## Types de ressources (TR01 à TR71, Annexe II-A — Catalogue Ressources au primaire)

TRnn = carte Rnn du Catalogue Ressources au primaire (TR02 = carte R02). Le préfixe TR distingue les types de ressources des recettes R1 à R8. Les types imprimés destinés aux élèves se produisent avec ce Livre I ; la correspondance de chaque type avec les gabarits (G, J, GF, SP) et les trames (TC) figure dans l'Annexe II-A (A.4) du Livre II.

**Famille I — Fiches et documents écrits**

- TR01 — Fiche de découverte
- TR02 — Fiche d'exercices
- TR03 — Fiche autocorrective
- TR04 — Fiche théorique
- TR05 — Fiche guide (marche à suivre)
- TR06 — Fiche de synthèse (révision)
- TR07 — Fiche diagnostique
- TR08 — Page d'étude d'un graphème (page-son)
- TR09 — Tracé de chemin orienté
- TR10 — Support effaçable sous pochette
- TR11 — Sous-main de l'élève
- TR12 — Manuel ou moyen d'enseignement
- TR13 — Document authentique
- TR14 — Dossier thématique documentaire
- TR15 — Album ou livre de lecture
- TR16 — Imagier et scène à légender (ajouté le 3.11.2026 ; G21)

**Famille II — Affiches, référentiels et visuels**

- TR17 — Affiche de stratégies
- TR18 — Affiche-procédure en « je »
- TR19 — Référentiel collectif
- TR20 — Glossaire de classe
- TR21 — Carte mentale
- TR22 — Infographie
- TR23 — BD pédagogique
- TR24 — Image ou œuvre à analyser

**Famille III — Cartes et jeux**

- TR25 — Cartes à pince
- TR26 — Domino pédagogique
- TR27 — Memory pédagogique
- TR28 — Cartes à classer
- TR29 — Cartes d'erreurs
- TR30 — Cartes d'aide graduée
- TR31 — Cartes de rappel et reprises espacées
- TR32 — Roue à fenêtre et rabat
- TR33 — Loto
- TR34 — Dé pédagogique
- TR35 — Jeu de l'oie pédagogique
- TR36 — Jeu de plateau pédagogique
- TR37 — Escape game pédagogique

**Famille IV — Matériel, objets et terrain**

- TR38 — Matériel de manipulation mathématique
- TR39 — Objet fabriqué (FabLearn, 3D)
- TR40 — Matériel d'expérimentation
- TR41 — Fiche-trace de sortie

**Famille V — Audio, vidéo et numérique**

- TR42 — Comptine ou chanson
- TR43 — Capsule audio
- TR44 — Capsule vidéo ou tutoriel
- TR45 — Diaporama projeté
- TR46 — Tableau interactif ou écran tactile
- TR47 — Quiz interactif
- TR48 — Exerciseur numérique
- TR49 — Activité interactive à l'écran
- TR50 — Récit interactif à embranchements
- TR51 — Parcours numérique
- TR52 — Mur collaboratif numérique
- TR53 — Simulation numérique
- TR54 — Robot ou programmation
- TR55 — Banque de ressources en ligne
- TR56 — Contenu IA relu par l'enseignant·e

**Famille VI — Accessibilité**

- TR57 — Version adaptée du support
- TR58 — Outil d'aide technologique

**Famille VII — Dispositifs et organisation de la classe**

- TR59 — Atelier à stations autocorrectif
- TR60 — Feuille de route par niveaux et brevet
- TR61 — Menu à choix
- TR62 — Débat à partir de productions fictives
- TR63 — Galerie de productions
- TR64 — Cartes de rôle (travail de groupe)
- TR65 — Coin de classe

**Famille VIII — Évaluation et traces**

- TR66 — Billet de sortie
- TR67 — Grille d'autoévaluation (élève)
- TR68 — Grille d'évaluation (enseignant·e)
- TR69 — Sondage ou vote en direct
- TR70 — Dictée réfléchie
- TR71 — Carnet de bord ou portfolio
