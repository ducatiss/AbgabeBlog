import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    SECRETKEY = 'poierprtgjhzugihpgfofphöioj89ptphpihguz'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
