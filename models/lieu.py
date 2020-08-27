from flask_sqlalchemy import Model
from sqlalchemy import Column, Integer, String, Numeric


class Lieu(Model):
    __tablename__ = 'lieu'

    id = Column(Integer, primary_key=True)
    nom = Column(String(140), nullable=False)
    latitude = Column(Numeric(8, 5), nullable=True)
    longitude = Column(Numeric(8, 5), nullable=True)

    def __init__(self, nom, latitude, longitude):
        self.nom = nom
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return f"<Lieu {self.nom}>"
