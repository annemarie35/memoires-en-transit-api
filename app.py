from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

import os

from routes import install_routes
from settings import load_environment_variables
from sqlalchemy import Column, Integer, String


app = Flask(__name__)

with app.app_context():
    load_environment_variables()
    install_routes()

#load_environment_variables()

app.config.from_object(os.environ['APP_SETTINGS'])
# TODO Remplacer par quelquechose du genre
#    config_module = f"application.config.{config_name.capitalize()}Config"
#     app.config.from_object(config_module)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Lieu(db.Model):
    __tablename__ = 'lieu'

    id = Column(Integer, primary_key=True)
    nom = Column(String(140), nullable=False)
    latitude = Column(db.Numeric(8, 5), nullable=True)
    longitude = Column(db.Numeric(8, 5), nullable=True)

    def __init__(self, nom, latitude, longitude):
        self.nom = nom
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return f"<Lieu {self.nom}>"

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()
