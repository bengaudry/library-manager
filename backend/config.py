import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///bdd_bibliotheque_massif_central.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False