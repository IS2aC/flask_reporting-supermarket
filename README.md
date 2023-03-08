# flask_reporting-supermarket
<img class="img1" src="https://s32519.pcdn.co/wp-content/uploads/2016/06/blog-supermarket-inventory-management-1.jpg.optimal.jpg">

## BUT: Concevoir une api rest de reporting sur un fichier .csv d'un supermarché.

- Analyse univarié et bivarié du jeu de données
- Analyse des resultats de ventes associés au premier trimestre.


- Analyse des profiles de clientele et des habitudes de consommation




## COMMENT LANCER L'APPLICATION 
##### *methode dockerfile*
NB: pour les versions 3.x de python

- builder l'image :  


docker build --tag *nom_image_docker* .


- lancement de l'application dans un conteneur docker: 

sudo docker run -d -p 5000:5000 *nom_image_docker*



##### *methode pip*

- Creation d'un environnement

linux : virtualenv *nom_environnement*


windows : python -m venv *nom_environnement*



- lancer la commande : 

pip install -r prequirements.txt
