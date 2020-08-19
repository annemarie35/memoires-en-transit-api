# 18/08/2020 Installation de flask

First step, as you originally tried to do, but this time you specify the "virtualenv" module and the name of the virtualenv. In this case flask:

`python -m virtualenv flask`
Then you activate your virtualenv like this:

`source flask/bin/activate`
Then install flask with pip inside the virtualenv

`pip install flask`
If you want to deactivate your virtualenv, simply type:

`deactivate`
If running on Python 3, the venv command is built-in and you can simply do:

`python3 -m venv flask`
Note, depending on how your Python 3 is installed, your python execution command might differ. You could be running it as python3, python3.5, python3.6.


https://medium.com/@dushan14/create-a-web-application-with-python-flask-postgresql-and-deploy-on-heroku-243d548335cc
