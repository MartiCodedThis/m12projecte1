from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_principal import Principal
from flask_debugtoolbar import DebugToolbarExtension
from .helper_mail import MailManager
import os

db_manager = SQLAlchemy()
login_manager = LoginManager()
principal_manager =  Principal()
mail_manager = MailManager()
toolbar = DebugToolbarExtension()

def create_app():
    # Construct the core app object
    app = Flask(__name__)
    app.logger.debug('Loading config...')
    app.config.from_pyfile("config.py")
    
    # activar debug
    app.debug = True

    # ruta absoluta d'aquesta carpeta
    basedir = os.path.abspath(os.path.dirname(__file__)) 

    # Inicialitza els plugins
    app.logger.debug('Loading manager plugins...')
    db_manager.init_app(app)
    login_manager.init_app(app)
    principal_manager.init_app(app)
    mail_manager.init_app(app)
    db_manager.init_app(app)
    toolbar.init_app(app)
    

    with app.app_context():
        from . import routes_main, routes_auth, routes_admin

        # Registra els blueprints
        app.logger.debug('Loading blueprints...')
        app.register_blueprint(routes_main.main_bp)
        app.register_blueprint(routes_auth.auth_bp)
        app.register_blueprint(routes_admin.admin_bp)

    app.logger.info("Application is up and running!")

    return app