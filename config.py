from os import environ


class Config(object):
    SQLALCHEMY_DATABASE_URI = environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = environ.get("SECRET_KEY")
    DEBUG = True