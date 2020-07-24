from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt


db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=False)
    print(f"App __init__: {__name__}")
    app.config.from_object('config.ConfigDev')

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

    with app.app_context():

        from . import creator
        app.register_blueprint(creator.creator_bp)

        from . import reader
        app.register_blueprint(reader.reader_bp)

        # db.create_all()
        # create a separate file that will drop all and create all tables
        # also, ensure that the logic adds a few pieces of test data?

        return app