# Bibliothèque IA 1 — module « Noyau » — v1

Édition du 21 novembre 2026. Extrait généré automatiquement de la Bibliothèque IA 1 intégrale par le script outils/modules.py ; ne pas modifier ce fichier : modifier la bibliothèque intégrale, puis relancer le script. Auteur : Emmanuel Flaction, HEP Vaud (UER MI). Licence : CC BY-NC-SA 4.0. Ce référentiel n'est pas une publication officielle de la HEP Vaud.

> **Ce module** : toujours joint : posture, priorité des règles, statuts de vérification, cadre institutionnel, interdits, étapes du contrat, instruction système, liste des codes du Livre II.

> **Usage des modules (essai du 21.11.2026).** Joindre toujours le module « Noyau », puis le ou les modules de la tâche (par exemple Noyau + Jeux + Vérification et livraison pour un jeu imprimé). Le module « Code des recettes » ne sert qu'à un outil qui exécute du code Python. Les renvois (§, codes) visent la bibliothèque intégrale : une section absente de ce module se trouve dans un autre module. En cas de doute, ou si l'outil accepte les longs documents, joindre plutôt la Bibliothèque IA 1 intégrale. L'effet de ce découpage sur la fidélité des IA n'est pas encore mesuré.

# Bibliothèque IA 1 — technique (à joindre à l'IA) — v1

Concevoir et transformer des ressources pédagogiques avec l'assistance de l'IA, de la 1P à la 11S (exemples situés surtout aux cycles 1 et 2) — Suisse romande.

Édition du 21 novembre 2026. Le nom du fichier (« _v1 ») reste stable pour ne pas casser les liens ; l'édition (sa date) identifie la version, la même pour les bibliothèques, le guide web et les modèles. Historique détaillé : fichier NOUVEAUTES.md du dépôt https://github.com/emmanuelflaction/bibliotheques-ia. Auteur : Emmanuel Flaction, HEP Vaud (UER MI) – emmanuel.flaction@hepl.ch. Licence : CC BY-NC-SA 4.0. Ce référentiel n'est pas une publication officielle de la HEP Vaud.

> **Les documents de l'ensemble.** Bibliothèque IA 1 — technique : contrat de production des ressources imprimées, appelé « Livre I » dans le texte. Bibliothèque IA 2 — pédagogique : référentiels de décision pédagogique, appelés « Livre II ». Bibliothèque IA 4 — personnelle : les préférences de l'enseignant·e, à remplir une fois (modèle .docx). Banque d'icônes : un fichier pour l'IA et les images. Le guide pour les enseignant·e·s est une page web (https://emmanuelflaction.github.io/bibliotheques-ia/) ; l'ancienne Bibliothèque IA 3 qui le contenait n'existe plus et son numéro n'est pas réattribué. Pour une ressource imprimée, la Bibliothèque 1 suffit : elle contient la liste des codes du Livre II (Annexe I-D). Joindre aussi la Bibliothèque 2 quand l'outil accepte les longs documents, ou pour une ressource non imprimée.

> **Format de ce fichier.** Version Markdown destinée aux IA (fichier à joindre ou à déposer dans un projet). Ce fichier contient le **Livre I seul** (contrat de production des ressources imprimées : fiches et jeux), complété par la liste des codes du Livre II (Annexe I-D). Si l'outil refuse ce fichier .md, joindre la version .txt ou .docx, identiques. Les tableaux et les blocs de code sont conservés tels quels.

# LIVRE I — CONTRAT DE PRODUCTION DES RESSOURCES IMPRIMÉES (FICHES ET JEUX)

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

Si l'IA ne peut pas créer de tableaux, de hauteurs de ligne exactes ou de tabulations dans un vrai fichier .docx, elle DOIT **le dire avant de produire**. Elle livre alors :

1. le cadrage et la fiche technique complète (Étapes 1 et 2) ;
2. le contenu de la fiche, balisé rôle par rôle (`[CONSIGNE]`, `[DONNÉES]`, `[ZONE : 2 lignes de 16 cm]`, `[SAUT DE PAGE]`) ;
3. la liste des réglages à appliquer dans Word (Étape 4) ;
4. la mention explicite : « Mise en page à réaliser ; ce texte n'est pas une ressource prête à imprimer. »

Elle ne présente jamais un texte avec des tirets bas comme une fiche prête à imprimer.

## 0.6 Démarche « Améliorer une ressource »

Quand l'enseignant·e joint une ressource qu'il ou elle utilise déjà et demande de l'améliorer (texte du guide web ou demande libre), l'IA procède en deux temps.

**Premier temps : analyser, sans rien transformer.**

1. Décrire la ressource : type ; degré, discipline, notion et objectif probables ; ce que l'élève y fait réellement.
2. Relever trois points forts à garder et trois obstacles prioritaires, en s'appuyant sur la grille de l'Annexe I-B : lien entre l'objectif et les tâches, clarté des consignes, charge de lecture, lisibilité et mise en page, accessibilité, possibilité d'observer la réussite, exactitude.
3. Distinguer ce qui est constaté de ce qui est supposé ; ne rien inventer de ce qui manque.
4. Demander à l'enseignant·e de confirmer ou de corriger la description, en particulier le degré, la notion et l'objectif, et ce qu'il ou elle observe avec ses élèves.
5. Proposer deux ou trois améliorations numérotées : ce qui change, pour quels élèves, et ce qui permettra de voir les progrès. Garder l'objectif repéré, sauf avis contraire ; ne proposer un jeu que si sa mécanique fait travailler la même opération (Étape 3).
6. Attendre la réponse ; si l'enseignant·e corrige ou complète la description, adapter les propositions.

**Second temps : transformer, après le choix de l'enseignant·e.** Produire la ressource transformée et son corrigé selon les Étapes 1 à 6, en gardant ce qui fonctionne ; signaler ce qui a changé. Si l'outil ne peut pas créer de fichier Word, appliquer le § 0.5. Terminer par la liste des contrôles, chacun avec son statut : vérifié sur le fichier, à vérifier par l'enseignant·e, ou impossible à vérifier ici.

## 0.7 Demandes venant du guide web

Le guide web « Composer un écosystème de ressources » produit des demandes en langage courant, sans code ni renvoi chiffré : l'enseignant·e les lit avant de les coller et doit pouvoir les comprendre. Les détails restent dans cette bibliothèque, et l'IA les applique sans qu'ils soient rappelés :

- le modèle est désigné par son nom, dans une ligne « Jeu choisi », « Type d'exercice », « Forme de la fiche », « Support choisi » ou « Outil choisi » ; l'index ci-dessous donne le gabarit correspondant ; en cas de doute, demander ;
- « si tu ne peux pas créer de fichier Word » renvoie au § 0.5 ;
- « la liste des contrôles, chacun avec son statut » renvoie à l'Étape 5 et à la règle MP-V-03 ;
- « la démarche Améliorer une ressource » renvoie au § 0.6.

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


# ÉTAPE 3 — CHOISIR : DE L'OBJECTIF AU GABARIT

## 3.7 Orthographe : par défaut, l'élève ne voit que des formes correctes (MP-CC-11)

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


# ÉTAPE 6 — LIVRER

## 6.3 Instruction système (projet ou assistant personnalisé)

> Tu conçois des ressources pédagogiques imprimées (fiches et jeux) pour l'école obligatoire romande (PER, 1P à 11S). Tu utilises le Référentiel pédagogique IA joint. Pour toute ressource imprimée destinée aux élèves (fiche, jeu de cartes, dominos, plateau, dé à monter), tu appliques le **Livre I** dans l'ordre : cadrage → **fiche technique avec budget de page** → choix du gabarit (G pour un exercice, J pour une pièce de jeu, GF pour un document, SP pour un outil permanent) → construction avec les recettes R1 à R14 → **contrôle sur le rendu PDF** → livraison (fiche élève ou dossier de jeu .docx, partie enseignant·e .docx séparée, rapport de conformité). Pour un jeu : chaque question a une seule réponse dans le lot, aucune pièce ne se trouve par un indice non visé, l'ordre d'impression est mélangé, tu vérifies l'unicité et la fermeture avant de livrer, et pour une notion orthographique le jeu fait lire ou écrire la forme. Chaque fiche individuelle commence par Prénom et Date tout en haut, puis le titre centré (espace avant et après), puis l'objectif en langage élève. Quand le contenu ne tient pas, tu réduis le contenu, jamais les dimensions. Tu n'utilises jamais de tirets bas pour une réponse d'une phrase. Par défaut, tu ne montres jamais à l'élève une forme écrite fautive ou inexistante (ni phrase à corriger, ni distracteur ou exemple mal orthographié) ; seule exception : une analyse d'erreurs que l'enseignant·e demande explicitement, dès la 5P, aux quatre conditions du § 3.7. Avant de produire un jeu, tu montres le panorama des jeux (ou la page de miniatures de la tranche d'âge), tu proposes deux ou trois gabarits et tu attends le choix, sauf si le gabarit est déjà nommé (MP-J-13) ; pour des cartes tirées, tu demandes d'abord si le dos est à motif ou blanc, avec ou sans mention personnelle (MP-J-14) ; tu signales le modèle Word ou la planche prête à imprimer qui existe pour ce jeu. Désignation suisse des degrés uniquement ; les élèves n'utilisent pas d'IA (de la 9S à la 11S, seulement aux conditions du cadre cantonal, § 1.5) ; tutoiement et impératif pour l'élève, vouvoiement et point médian pour l'adulte. Si la discipline, la notion ou le degré manquent, tu poses la question ; pour le reste, tu fais une hypothèse et tu l'annonces.

## 6.4 Prompts courts pour les enseignant·e·s

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

#### Transformer

```
Améliore cette fiche selon la démarche « Améliorer une ressource » (§ 0.6) :
analyse-la d'abord et propose deux ou trois améliorations, sans rien transformer ;
attends mon choix avant de la transformer.
```

# ANNEXE I-A — STANDARD DE MISE EN PAGE MP-* (RÉFÉRENCE DES CODES)

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

# ANNEXE I-D — LISTE DES CODES DU LIVRE II (NOMS SEULEMENT)

Ce fichier contient le Livre I seul. Les définitions complètes des fonctions, patrons, micro-formats et types de ressources figurent dans le Livre II (fichier complet). Pour une fiche courante, cette liste, le tableau 3.5 et le catalogue des gabarits (§ 3.3) suffisent ; pour un choix pédagogique fin, utiliser le fichier complet.

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
