import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

import config

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    if os.environ.get('FLASK_ENV') == "production":
        app.config.from_object("config.Production")
    elif os.environ.get('FLASK_ENV') == "development":
        app.config.from_object("config.Development")
    elif os.environ.get('FLASK_ENV') == "test":
        app.config.from_object("config.Test")
    else:
        app.config.from_object("config.Development")    

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    login_manager.login_view = "account_bp.login"
    login_manager.login_message = "Please login"
    login_manager.refresh_view = "account_bp.login"
    login_manager.needs_refresh_message = "You need to login again to access this page."

    with app.app_context():

        from . import error_handlers
        app.register_error_handler(404, error_handlers.page_not_found)
        #app.register_error_handler(500, error_handlers.internal_server_error)
        app.register_error_handler(403, error_handlers.forbidden)
        #app.register_error_handler(ValueError, error_handlers.internal_server_error)
        app.register_error_handler(SQLAlchemyError, error_handlers.sqlalchemy_error)

        from . import creator
        app.register_blueprint(creator.creator_bp)

        from . import reader
        app.register_blueprint(reader.reader_bp)

        from . import account
        app.register_blueprint(account.account_bp)

        @login_manager.user_loader
        def load_user(user_id):
            print('load_user hit')
            if user_id is not None:
                return models.User.query.get(user_id)
            return None

        return app

    
