from os import environ, path
from dotenv import load_dotenv
from datetime import timedelta

basedirectory = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedirectory, '.env'))


class Config:
    SQLALCHEMY_DATABASE_URI = environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = environ.get("SECRET_KEY")
    USE_SESSION_FOR_NEXT = True


class ConfigDev(Config):
    DEBUG = True
    TESTING = True


class ConfigTest(Config):
    DEBUG = True
    TESTING = True


class ConfigProd(Config):
    DEBUG = False
    TESTING = False
