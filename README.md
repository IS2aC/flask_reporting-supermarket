# flask_reporting-supermarket
<img class="img1" src="https://s32519.pcdn.co/wp-content/uploads/2016/06/blog-supermarket-inventory-management-1.jpg.optimal.jpg">

## BUT: Concevoir une api rest de reporting sur un fichier .csv d'un supermarché.

- Analyse univarié et bivarié du jeu de données

![Capture d’écran du 2023-03-07 16-50-20](https://user-images.githubusercontent.com/47854708/223868789-e0b85a73-9138-48e4-b8d0-5e4303980138.png)


- Analyse des resultats de ventes associés au premier trimestre.


![Capture d’écran du 2023-03-07 16-50-52](https://user-images.githubusercontent.com/47854708/223868845-43231e9d-5b49-470b-8623-ce6f44a4cd36.png)



- Analyse des profiles de clientele et des habitudes de consommation **BLEU**(visiteur), et **ROUGE**(client premium) 



![Capture d’écran du 2023-03-07 16-52-36](https://user-images.githubusercontent.com/47854708/223868874-29951a7f-7ab3-4d05-bbd0-e0db7d448265.png)





### Techno utilisés : 
- Python, **flask**
- html, css, java-script(**Chart.js**)






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


###### python app.py
