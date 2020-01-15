## Utilisez les données publiques de l'OpenFoodFacts
## Projet 5 du Parcours développeur d'application python d'OpenClassrooms
## Cahier des charges:
L'utilisateur est sur le terminal. Ce dernier lui affiche les choix suivants :

1 - Quel aliment souhaitez-vous remplacer ?
2 - Retrouver mes aliments substitués.

L'utilisateur sélectionne 1. Le programme pose les questions suivantes à l'utilisateur et ce dernier sélectionne les réponses :

* Sélectionnez la catégorie. [Plusieurs propositions associées à un chiffre. L'utilisateur entre le chiffre correspondant et appuie sur entrée]
* Sélectionnez l'aliment. [Plusieurs propositions associées à un chiffre. L'utilisateur entre le chiffre correspondant à l'aliment choisi et appuie sur entrée]
* Le programme propose un substitut, sa description, un magasin ou l'acheter (le cas échéant) et un lien vers la page d'Open Food Facts concernant cet aliment.
* L'utilisateur a alors la possibilité d'enregistrer le résultat dans la base de données.
## Comment faire marcher le programme?
Voici les différentes instructions pour faire marcher le programme correctement.
### Installation
Vous devez installer le module pygame avec pip si vous êtes sur Windows:
```bash
pip install pygame
```
Si vous êtes sur Linux:
```bash
sudo apt-get install -y python3-pip
sudo apt-get install -y \
    python3-numpy libav-tools libsdl-image1.2-dev \
    libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev libsdl1.2-dev \
    libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev \
    libfreetype6-dev
sudo pip3 install -q pygame
```
### Utilisation 
Vous devez créer une Base de données nommé "oc_projet_5_off" et autoriser la connexion de l'user "root" avec un mot de passe de champ vide ""
Ensuite lancer le script SQL contenu dans le dossier "oc_projet_5_off.sql"
Vous devez ensuite lancer le fichier _main.py_

### Fonctionnement
Si la base de données est vide alors le programme fait des requests via l'API d'OFF,et la remplie, sinon elle lance directement le choix de produit.

### Environnement virtuel
Les librairies necessaires sont trouvables dans le fichier requirements.txt

## Fonctionnalités:
* Recherche d'aliments dans la base OpenFoodFacts.
* L'utilisateur interagit avec le programme dans le terminal, mais si vous souhaitez développer une interface graphique vous pouvez.
Si l'utilisateur entre un caractère qui n'est pas un chiffre, le programme doit lui répéter la question,
* La recherche doit s'effectuer sur une base MySql.

## Versionnage:
V0.3 installation bdd
V0.5 fin d'installation et création programme principal.
V0.6 fin création programme principal et boucle pour programme avec vérification pour savoir si la DB est vide ou non.
V0.7 Nettoyer et commenter le code( pylint...).
V1.0 Amélioration README.md et Fin pylint,quelques amélioration comme quitter le programme directement,et amélioration de la visibilité pour l'utilisateur.

## Auteur et Contribution:
J'ai développé ce programme dans le cadre d'une formation sur Openclassrooms.Par conséquent toute pull request avec du code sera refusé. Ouvrez plutôt une issue pour signaler un bug, une faute d'orthographe ou pour simplement donner un conseil.