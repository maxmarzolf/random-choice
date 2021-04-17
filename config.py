from os import environ, path
from dotenv import load_dotenv

base_directory = path.abspath(path.dirname(__file__))
load_dotenv(path.join(base_directory, '../../.env'))


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # TODO: is SECRET_KEY used anymore?
    SECRET_KEY = environ.get("SECRET_KEY")
    USE_SESSION_FOR_NEXT = True
    TESTING = False


class Development(Config):
    SQLALCHEMY_DATABASE_URI = environ.get("DEV_DATABASE_URI")
    FLASK_ENV = 'development'


class Production(Config):
    SQLALCHEMY_DATABASE_URI = environ.get("DATABASE_URI")
    FLASK_ENV = 'production'
    DEBUG = False