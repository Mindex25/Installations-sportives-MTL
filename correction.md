# Guide de correction des fonctionnalités

## A1 Importation de la base de données
Un script db.sql se trouve à l'adresse TP2/app/db/db.sql. Pour vérifier l'exécution du script, il suffit de supprimer la base de données db.db, d'aller à l'adresse mentionnée et entrer la commande :
> ```cat db.sql | sqlite3 db.db```
>
Lorsque la base de données est initialisée, les données peuvent être importées de la façon suivante: Ouvrir le fichier wsgi.py situé à l'adresse TP2/wsgi.py, décommenter la fonction maj_donnees() et entre la commande ```make```. Avec un explorateur de base de données, vous pourrez vérifier l'importation des données de la ville dans la base de données de cette application.

## A2 BackgroundScheduler
Pour tester le BackgroundScheduler, il suffit de changer la date de l'exécution de ses tâches au moment courrant. Par exemple, si il est 18h59, changer les paramètres pour hour=19,minute=0.

## A3 /doc
Un fichier doc.raml contient les méta-données de l'API. La page à l'adresse /doc est générée automatiquement lors de l'exécution du makefile.

## A4 /api/installations?arrondissement=foobar
Pour tester ce service, vous pouvez lancer l'application avec make et vous diriger à l'adresse /api/installations?arrondissement=Verdun. Le nom de l'arrondissement peut être changé.

## A5 Recherche d'installations par arrondissement
Pour tester l'application Javascript/HTML, vous pouvez vous diriger sur la route « / » de l'application et entrer un nom d'arrondissement dans la barre de recherche. Un tableau créé dynamiquement affiche les résultats de la requête asynchrone.

## A6 Recherche d'informations sur une installation
Pour tester l'application Javascript/HTML, vous pouvez vous diriger sur la route « / » de l'application et sélectionner le nom d'une installation dans la barre de recherche. Un tableau créé dynamiquement affiche les résultats de la requête asynchrone.

## B1 Envoi des nouvelles installations par courriel
Pour tester l'envoie des nouvelles installations, il faut ajouter son adresse courriel au fichier config.yaml. Vous pouvez ouvrir la base de données et exécuter cete séquence de commandes en supposant que des données s'y trouvent déjà.

```
cd app/db
sqlite3 db.db
delete from piscine where type='Pateaugoire'
Control+C
cd ..
make
```
Vous devriez recevoir la liste des piscines ayant comme type Pateaugoire.

## E1 Création d'un profil utilisateur
Le service peut être testé avec l'interface graphique du point E5.

## E2 Interface graphique HTML pour invoquer le service en E1
Vous pouvez entrer vos informations et confirmer votre inscription en consultant la table utilisateur dans la base de données.

## F1 Heroku
Le site est déployé sur la plateforme infonuagique Heroku à l'adresse suivante: 
https://installations-mtl.herokuapp.com/
