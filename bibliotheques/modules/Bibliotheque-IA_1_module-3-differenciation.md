# Bibliothèque IA 1 — module « Différenciation et accessibilité » — v1

Édition du 22 novembre 2026. Extrait généré automatiquement de la Bibliothèque IA 1 intégrale et de sections de la Bibliothèque IA 2 par le script outils/modules.py ; ne pas modifier ce fichier : modifier la bibliothèque intégrale, puis relancer le script. Auteur : Emmanuel Flaction, HEP Vaud (UER MI). Licence : CC BY-NC-SA 4.0. Ce référentiel n'est pas une publication officielle de la HEP Vaud.

> **Ce module** : différenciation sur la fiche, statut de lecture, non-lecteurs, repères de différenciation et de coopération.

> **Usage des modules (essai du 21.11.2026).** Joindre toujours le module « Noyau », puis le ou les modules de la tâche (par exemple Noyau + Jeux + Vérification et livraison pour un jeu imprimé). Le module « Code des recettes » ne sert qu'à un outil qui exécute du code Python. Les renvois (§, codes) visent la bibliothèque intégrale : une section absente de ce module se trouve dans un autre module. En cas de doute, ou si l'outil accepte les longs documents, joindre plutôt la Bibliothèque IA 1 intégrale. L'effet de ce découpage sur la fidélité des IA n'est pas encore mesuré.

# ÉTAPE 1 — CADRER

## 1.3 Statut de lecture

Le statut non-lecteur / lecteur change le fonctionnement de toute la fiche.

- **Non-lecteurs et lecteurs débutants (en général 1P-2P, parfois 3P)** : **aucune consigne écrite destinée à l'élève** : la consigne est donnée oralement par l'adulte et portée sur la fiche par un **exemple complet, déjà fait, en tête de la fiche** (première case ou premier item, sur fond teinté) et, au besoin, par un pictogramme stable par verbe de consigne ; le seul texte admis est celui que l'élève travaille (mot à lire, lettre, nombre) et une ligne « Pour l'adulte », en petit, en bas de page ; recette : `definir_jeunes(True)` retire aussi la consigne écrite des fiches dessinées (G23, G24) et y place l'exemple ; pour les lecteurs débutants (3P), un pictogramme stable par verbe de consigne PEUT accompagner la consigne écrite ; **option « pictogrammes de consigne »**, à tout degré : si l'enseignant·e la demande, chaque consigne du document DOIT être précédée, à gauche, du pictogramme de la banque d'icônes qui correspond à son verbe (codes IC-CON, fonction `icone`, 1,2 à 1,5 cm de haut, texte de remplacement de la banque) ; le même verbe reçoit le même pictogramme dans tout le document ; le pictogramme accompagne la consigne écrite et ne la remplace jamais (MP-C-02) ; si aucun pictogramme ne correspond au verbe, ne pas en inventer : choisir un verbe de la banque ou le signaler ; si la banque n'est pas jointe, écrire le code entre crochets (`[IC-CON-ENTOURE]`) et le signaler ; une fois demandée, l'option vaut pour tous les documents de la conversation, jusqu'à avis contraire ; une seule tâche par page est souvent préférable. *Le corpus source ne fournit pour ce public que la taille de 24 pt et le principe de l'image utile : toute autre adaptation est une proposition, à présenter comme telle.*
- **Lecteurs** : consignes écrites d'une phrase, une action par phrase.


# ÉTAPE 3 — CHOISIR : DE L'OBJECTIF AU GABARIT

## 3.6 Différenciation et mise en page (MP-D)

| Code | Règle | Niveau |
|---|---|---|
| MP-D-01 | Aucune étiquette de niveau évaluative sur la fiche élève. Un repère neutre est admis : symbole discret en en-tête (♣ ♦ ♠), lettre de version, items facultatifs marqués ★. **Étoiles de difficulté, sur demande** : si l'enseignant·e le demande, les exercices d'une fiche ou les cartes d'un jeu PEUVENT porter une à trois étoiles, de la tâche la plus simple à la plus difficile ; les étoiles décrivent la tâche, jamais l'élève ni un groupe d'élèves ; une ligne les explique à l'élève (« Choisis ton point de départ ») ; elles sont dessinées ou vérifiées sur le rendu (R6). Sans demande, le repère reste neutre. | DOIT |
| MP-D-02 | Deux dispositifs possibles : **parcours sur la même fiche** (items a-c, a-d, a-e ; aide-mémoire pour un parcours) ou **versions parallèles** (mêmes exercices, mêmes phrases et mêmes lettres d'items ; seuls l'étayage et l'étendue changent), ce qui permet une correction commune et un changement de version en cours de route. Autour d'une **fiche unique**, sans tripler la fiche (leviers : contenus, processus, productions, structures ; Forget, 2018) : difficulté croissante, chacun choisissant son point de départ avec un repère neutre ou, sur demande, des étoiles de difficulté (MP-D-01) ; noyau commun en haut de la fiche et prolongements facultatifs en bas ; aides détachées en libre accès, réutilisables d'une fiche à l'autre (J15) ; quantité plutôt qu'objectif (« au moins quatre exercices sur huit, dont le numéro 5 ») ; forme de la réponse au choix (écrire, entourer, relier, manipuler puis dessiner, expliquer oralement) ; organisation (seul, binôme d'entraide, petit groupe avec l'enseignant·e) ; trame stable (objectif, exemple, exercices gradués, défi). Si un élève choisit toujours trop facile ou trop difficile, l'enseignant·e oriente son point de départ. | DEVRAIT |
| MP-D-03 | Chaque version ou parcours respecte son propre budget de page (Étape 2). | DOIT |
| MP-D-04 | Les modalités d'attribution (diagnostic court, choix accompagné) et la consigne « une version décrit un besoin du moment, pas un niveau d'élève » figurent dans la partie enseignant·e. | DEVRAIT |
| MP-D-05 | **Classe multi-âges** (deux degrés, ou deux niveaux de programme, dans la même classe : très fréquente en 1P-2P, possible à tous les degrés, notamment dans les petits établissements et les classes spécialisées). Un seul matériel commun, avec une entrée par degré ou par niveau : par exemple une collection jusqu'à 5 ou jusqu'à 10, des images ou des mots, moins ou plus de cartes, une tâche de base et un prolongement. Aucun repère de degré ou de niveau n'est visible pour les élèves (MP-D-01) ; les entrées se distinguent par le contenu ou par un repère neutre. Dès qu'un des degrés ne lit pas encore, les consignes sont prévues à l'oral ou en pictogrammes. La partie enseignant·e indique quelle entrée convient à quel degré ou niveau, l'objectif du plan d'études de chacun (§ 1.2) et un moment commun (lancement, mise en commun). L'IA ne demande et n'utilise aucune information sur des élèves : elle part des degrés ou des niveaux annoncés. | DOIT |
| MP-D-06 | **Encadré « Si je bloque »**, sur demande ou pour un travail autonome (atelier, plan de travail, devoir) : deux ou trois stratégies dans l'ordre (relire la consigne et l'exemple, utiliser une aide en libre accès, demander à un·e camarade), puis le moment où demander à l'enseignant·e ; formulé en « je », avec pictogrammes si les élèves lisent peu ; jamais la réponse. | PEUT |


# EXTRAITS DE LA BIBLIOTHÈQUE IA 2

# PARTIE 10 — DÉPLOIEMENT PROGRESSIF ET RÉFÉRENCES

## Repères pour les jeux, la coopération et la différenciation

Ces repères complètent les règles de la Bibliothèque IA 1 (MP-J-07, MP-D-02, § 4.3). Ils servent à conseiller l'enseignant·e avant la production et à justifier les choix dans la partie enseignant·e.

**Évaluer une ressource : utile, utilisable, acceptable**

Le triptyque utilité, utilisabilité, acceptabilité (Tricot et al., 2003) donne trois questions : la ressource fait-elle apprendre ce qui est visé ? Est-elle facile à utiliser ? Les élèves et l'enseignant·e ont-ils envie de s'en servir, et le peuvent-ils dans leur contexte ? L'acceptabilité (ce que les utilisateurs pensent de la ressource) ne se confond pas avec l'accessibilité (la possibilité d'y accéder). La mise en page réduit la charge extrinsèque, celle qui vient de la présentation ; la charge intrinsèque dépend du contenu lui-même (Maitre, 2020).

- Utile : l'objectif d'apprentissage tient en une phrase et se relie au plan d'études ; chaque carte ou chaque case fait travailler cet objectif, sans tâche décorative ; le temps passé à apprendre dépasse le temps passé à attendre ou à gérer le matériel ; tous les élèves du groupe répondent ; quand l'exactitude ne s'entend pas (orthographe, accords), la réponse est écrite ou épelée ; l'erreur est exploitée (vérification, explication, nouvelle tentative) ; un moyen permet de savoir ce que les élèves ont appris ; les contenus sont relus.
- Utilisable : une marche à suivre écrite accompagne le jeu et dit aussi qui commence, comment disposer le matériel, qui vérifie et ce que fait celui qui s'est trompé ; un élève peut expliquer la règle après une partie modèle ; les textes se lisent à la distance d'utilisation et la mise en page est la même sur toutes les cartes ; les images sont de style homogène ; la réponse n'est pas visible par celui qui doit la trouver et un corrigé est disponible ; le matériel est solide, facile à distribuer et à ranger ; la taille des groupes et la durée d'une partie sont définies ; des niveaux ou des variantes permettent à chacun de réussir.
- Acceptable : les élèves ont envie de rejouer ; la règle favorise l'entraide et ne met personne en échec devant les autres ; aucun élève n'est désigné comme « différent » par le matériel qu'il reçoit ; le niveau sonore et l'organisation conviennent à la classe ; les rôles, les situations et les récompenses véhiculent des valeurs compatibles avec celles de l'école (pas de rôle de voleur pour s'exercer à la soustraction) ; le temps de préparation reste raisonnable, et le matériel sobre (pages, couleur, plastification) et réutilisable ; un·e collègue pourrait reprendre le jeu sans explications ; les images sont libres de droits ou sourcées, et aucune donnée d'élève n'apparaît.

**Un jeu pour apprendre, pas seulement pour s'occuper ou s'amuser**

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

## Gamification, styles d’apprentissage et différenciation

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
