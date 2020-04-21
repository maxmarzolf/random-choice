from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    # init sqlalchemy
    db.init_app()

    with app.app_context():

        from . import creator
        app.register_blueprint(creator.creator_bp)

        from . import reader
        app.register_blueprint(reader.reader_bp)

        return app