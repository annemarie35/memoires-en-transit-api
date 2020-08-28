# README

- Installer les dépendances : `pip3 install -r requirements.txt`
- Lancer le serveur : `python app.py`

Astuce

`export FLASK_APP=app.py` permet de lancer l'app avec la commande `flask run`

# Mettre à jour le modèle de donnée

- Ajouter la class model voulue dans `app.py
- La commande `python manage.py db migrate` génère le fichier de migration dans migrations/version
- Mettre à jour la base de donnée avec `python manage.py db upgrade` ou `python manage.py db downgrade`

# Lancer les tests

`python -m pytest tests -s` le -s permet de visualiser les print 
