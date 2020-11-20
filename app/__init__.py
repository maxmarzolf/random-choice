from flask import Flask, flash, redirect, url_for, session, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, current_user

from datetime import timedelta


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

    #login_manager settings
    login_manager.login_view = "account_bp.login"
    login_manager.login_message = "Please login"
    login_manager.refresh_view = "account_bp.login"
    login_manager.needs_refresh_message = "You need to login again to access this page."

    with app.app_context():

        from . import error_handlers
        app.register_error_handler(404, error_handlers.page_not_found)
        app.register_error_handler(500, error_handlers.internal_server_error)
        app.register_error_handler(403, error_handlers.forbidden)
        app.register_error_handler(ValueError, error_handlers.internal_server_error)
        app.register_error_handler(SQLAlchemyError, error_handlers.sqlalchemy_error)

        from . import creator
        app.register_blueprint(creator.creator_bp)

        from . import reader
        app.register_blueprint(reader.reader_bp)

        from . import account
        app.register_blueprint(account.account_bp)

        # login_manager.refresh_view = "accounts_bp.login"
        # login_manager.needs_refresh_message = "Please login again to continue."

        @login_manager.user_loader
        def load_user(user_id):
            if user_id is not None:
                return models.User.query.get(user_id)
            
            return None
        
        # @login_manager.unauthorized_handler
        # def unauthorized():
        #     flash("You must log in to view that page.")
        #     print("hit unauthorized_handler")

        #     return redirect(url_for('account_bp.login'))
        
        # @login_manager.needs_refresh_handler
        # def needs_refresh():
        #     flash("Your session has expired. Please login again.")
        #     print("hit needs_refresh_handler")
        #     #current_user.logout()            

        #     return redirect(url_for('account_bp.login'))
        
        # @app.route('/needs-refresh')
        # def needs_refresh():
        #     return login_manager.needs_refresh()
        
        # @app.before_request
        # def make_session_permanent():
        #     session.permanent = True
        #     app.permanent_session_lifetime = timedelta(minutes=1)
            

        # db.create_all()
        # create a separate file that will drop all and create all tables
        # also, ensure that the logic adds a few pieces of test data?

        return app