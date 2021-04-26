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
    TESTING = False


class Production(Config):
    SQLALCHEMY_DATABASE_URI = environ.get("DATABASE_URI")
    TESTING = False


class Test(Config):
    TESTING = True

    def __init__(self, no_db=False):
        self.SQLALCHEMY_DATABASE_URI = environ.get("DEV_DATABASE_URI")
        if no_db:
            # SQLAlchemy throws an error if the string is empty or missing a dialect.
            self.SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://something'
