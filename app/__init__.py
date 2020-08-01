from flask import Flask, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
login_manager = LoginManager()


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.ConfigDev')

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    with app.app_context():

        from . import creator
        app.register_blueprint(creator.creator_bp)

        from . import reader
        app.register_blueprint(reader.reader_bp)

        from . import account
        app.register_blueprint(account.account_bp)

        @login_manager.user_loader
        def load_user(user_id):
            if user_id is not None:
                return models.User.query.get(user_id)
            
            return Non
        
        @login_manager.unauthorized_handler
        def unauthorized():
            flash("You must log in to view that page.")

            return redirect(url_for('account_bp.login'))

        # db.create_all()
        # create a separate file that will drop all and create all tables
        # also, ensure that the logic adds a few pieces of test data?

        return app