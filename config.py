from os import environ, path
from dotenv import load_dotenv


class Config:
    base_directory = path.abspath(path.dirname(__file__))
    load_dotenv(path.join(base_directory, '.env'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = environ.get("SECRET_KEY")
    USE_SESSION_FOR_NEXT = True


class Development(Config):
    SQLALCHEMY_DATABASE_URI = environ.get("DEV_DATABASE_URI")
    ENV = 'development'
    FLASK_ENV = 'development'
    TESTING = False
    DEBUG = True


class Production(Config):
    SQLALCHEMY_DATABASE_URI = environ.get("DATABASE_URI")
    ENV = 'production'
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False


class Test(Config):
    TESTING = True

    def __init__(self, no_db=False):
        self.SQLALCHEMY_DATABASE_URI = environ.get("DEV_DATABASE_URI")
        if no_db:
            # SQLAlchemy throws an error if the string is empty or missing a dialect.
            self.SQLALCHEMY_DATABASE_URI = 'postgres+psycopg2://something'
