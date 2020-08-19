# README

Installer les dépendances : `pip3 install -r requirements.txt`
Lancer le serveur : `python app.py`


`export FLASK_APP=app.py` permet de lancer l'app avec la commande `flask run`

# Mettre à jour le modèle de donnée

Ajouter la class model voulue dans app.py

puis  `python manage.py db migrate` génère la migrations/version
`python manage.py db upgrade` ou downgrade
