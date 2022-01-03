# Projet de session INF5190

## Auteur
Jérémie Gour

## Description
Projet de session effectué dans le cadre du cours INF5190 à la session d'automne 2021. Le programme est un exercice de développement back-end qui offre des services REST pour obtenir de l'information sur les installations sportives de la ville de Montréal.

## Fonctionnement
Le programme s'exécute dans un environnement Vagrant donné par l'enseignant du cours INF5190, mais s'exécute aussi localement. Pour installer un environnement virtuel différent de Vagrant, il faut utiliser les commandes suivantes:

```
python3 -m venv env
pip install -r requirements.txt
```

Le programme s'exécute avec la commande `make` à la racine du projet. Il est peut-être nécessaire d'installer raml2html pour pouvoir générer la documentation automatique des services REST en HTML.

Une base de données `db.db` est déjà fournie, mais elle peut être crée par la commande `cat db.sql | sqlite3 db.db`

## Fichiers
#### /app
* courriel.py : contient les fonctionnalités liées à l'envoi de courriels automatisé.
* database.py : contient les fonctions de gestion de la base de données.
* glissade.py, patinoire.py, piscine.py : contiennent les fonctionnalités de création d'objets utilisés dans l'application.
* index.py : fichier principal de gestion des routes de l'application.
* utilisateur.py : contient la classe et ses méthodes liées à la gestion des utilisateurs.

#### /
* correction.md : contient les instructions pour noter l'application adressées au correcteur du cours.
* courriels.yaml : liste d'adresses courriels.
* doc.raml : fichier RAML qui document les services REST de l'API.
* makefile: fichier pour gérer l'exécution du programme à la ligne de commande.
* requirements.txt : liste des modules à importer.
* wsgi.py : fichier d'exécution de l'application, contient l'importation des données et le background scheduler.

## Heroku
L'application est déployée sur Heroku. La version de l'application qui y est disponible n'est possiblement pas la même que celle contenu dans ce projet. J'ajoute certaines fonctionnalités pour mon portlio. 
<br>
https://installations-mtl.herokuapp.com/
