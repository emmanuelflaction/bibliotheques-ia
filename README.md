# Bibliothèques IA — créer des ressources imprimées pour la classe

Des « bibliothèques » à joindre à une IA générative pour lui faire produire des jeux, des fiches et des supports imprimables, de la 1P à la 11S (école romande), avec un guide pour choisir un modèle.

**Auteur** : Emmanuel Flaction, enseignant à la Haute école pédagogique du canton de Vaud (HEP Vaud, UER MI).

## Pour commencer

- **Le guide en ligne, « Composer un écosystème de ressources »** : https://emmanuelflaction.github.io/bibliotheques-ia/
- **Composer une séquence** : une rubrique du guide relie plusieurs ressources autour d'un objectif (une fonction par ressource, et ce qui passe de l'une à l'autre), puis rédige une demande d'ensemble pour l'IA.
- **Ce qu'il contient** : le guide (fichier `index.html`) présente tous les modèles (jeux, exercices, formes de fiches, supports et affiches, icônes) et rédige la demande à coller dans la conversation avec l'IA.
- **Avec une IA** : joignez `bibliotheques/Bibliotheque-IA_1-technique_pour-IA_v1.md` à votre conversation (ou la version `.txt` ou `.docx` si votre outil refuse le `.md`), puis collez la demande proposée par le guide.
- **Sans IA** : les dossiers `modeles` et `planches` contiennent des documents à remplir ou à imprimer tels quels.

## Contenu

| Dossier | Contenu |
|---|---|
| `bibliotheques` | Bibliothèque IA 1 (technique), Bibliothèque IA 2 (pédagogique), Bibliothèque IA 4 (modèle personnel à remplir), panoramas des modèles ; dans `bibliotheques/modules`, la Bibliothèque IA 1 découpée en modules à joindre selon la tâche (à l'essai : leur effet sur les réponses des IA n'est pas encore mesuré) |
| `modeles` | Modèles Word de jeux à remplir, en noir et blanc et en couleur |
| `planches` | Planches et exemples prêts à imprimer (PDF) |
| `icones` | Banque d'icônes en noir et blanc (licence CC0, voir le fichier de licence du dossier) |
| `apercus` | Images d'aperçu affichées par le guide en ligne (chargées à la demande) |
| `outils` | `verifier.py` : contrôle que chaque fichier annoncé par le guide existe et que les éditions concordent ; `guide_local.py` : construit la version du guide pour un dossier partagé (un seul fichier, aperçus intégrés) ; `modules.py` : tire les modules de la Bibliothèque IA 1 intégrale, d'après les balises placées sous ses titres |

**Publication.** Le site est servi par GitHub Pages depuis la branche `gh-pages`, copie de `main` : après chaque dépôt sur `main`, la pousser aussi vers `gh-pages` (`git push origin main:gh-pages`).

## Versions

Une seule **édition**, identifiée par sa date, vaut pour l'ensemble : bibliothèques, guide web, modèles et planches. L'édition actuelle est celle du **21 novembre 2026**. Elle figure en tête de chaque bibliothèque et au pied du guide ; deux éléments de même édition sont conçus pour fonctionner ensemble. Les noms de fichiers (« _v1 ») ne changent pas, pour que les liens restent valables. Le détail des changements est dans [NOUVEAUTES.md](NOUVEAUTES.md) ; toutes les éditions antérieures restent dans l'historique du dépôt.

## Statut

Ce projet est conçu par un enseignant de la HEP Vaud ; ce n'est pas une publication officielle de l'institution. Les typologies et les procédures des bibliothèques sont des propositions de conception, appuyées sur des travaux de recherche cités ; elles ne constituent pas un modèle validé empiriquement.

## État du travail

Les bibliothèques et le guide sont développés avec l'assistance d'IA génératives (Claude et quelques autres). Les documents sont contrôlés à l'écran ; tous n'ont pas encore été expérimentés en classe. Faites toujours un essai d'impression avant de préparer un jeu complet.

Les nouveautés sont décrites dans [NOUVEAUTES.md](NOUVEAUTES.md).

## Participer

Signalez une erreur, proposez un modèle ou racontez un essai en classe : emmanuel.flaction@hepl.ch, ou ouvrez un ticket (*issue*) dans ce dépôt. N'envoyez ni nom ni photo d'élève.

## Droits

© 2026 Emmanuel Flaction. Contenu en accès libre sous licence [CC BY-NC-SA 4.0](LICENCE.md) : vous pouvez l'utiliser et l'adapter en citant l'auteur, sans usage commercial, et en partageant vos adaptations sous la même licence. La banque d'icônes du dossier `icones` est sous licence CC0 1.0.
