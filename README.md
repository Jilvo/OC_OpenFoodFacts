# Projet 5 du Parcours développeur d'application python d'OpenClassrooms
## Utilisez les données publiques de l'OpenFoodFacts
### Cahier des charges:
L'utilisateur est sur le terminal. Ce dernier lui affiche les choix suivants :

1 - Quel aliment souhaitez-vous remplacer ?
2 - Retrouver mes aliments substitués.

L'utilisateur sélectionne 1. Le programme pose les questions suivantes à l'utilisateur et ce dernier sélectionne les réponses :

* Sélectionnez la catégorie. [Plusieurs propositions associées à un chiffre. L'utilisateur entre le chiffre correspondant et appuie sur entrée]
* Sélectionnez l'aliment. [Plusieurs propositions associées à un chiffre. L'utilisateur entre le chiffre correspondant à l'aliment choisi et appuie sur entrée]
* Le programme propose un substitut, sa description, un magasin ou l'acheter (le cas échéant) et un lien vers la page d'Open Food Facts concernant cet aliment.
* L'utilisateur a alors la possibilité d'enregistrer le résultat dans la base de données.

### Fonctionnalités:
* Recherche d'aliments dans la base Open Food Facts.
* L'utilisateur interagit avec le programme dans le terminal, mais si vous souhaitez développer une interface graphique vous pouvez,
Si l'utilisateur entre un caractère qui n'est pas un chiffre, le programme doit lui répéter la question,
* La recherche doit s'effectuer sur une base MySql.

### Versionnage:
V0.3 installation bdd
V0.5 fin d'installation et création programme principal
V0.6 fin création programme principal et boucle pour programme avec vérification pour savoir si la DB est vide ou non
V0.7 Nettoyer et commenter le code( pylint...)

### Auteur et Contribution:
J'ai développé ce programme dans le cadre d'une formation sur Openclassrooms.Par conséquent toute pull request avec du code sera refusé. Ouvrez plutôt une issue pour signaler un bug, une faute d'orthographe ou pour simplement donner un conseil.