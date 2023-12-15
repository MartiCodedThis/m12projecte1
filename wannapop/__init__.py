from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_principal import Principal
from flask_debugtoolbar import DebugToolbarExtension
from .helper_mail import MailManager
import os
import logging
from logging.handlers import RotatingFileHandler

db_manager = SQLAlchemy()
login_manager = LoginManager()
principal_manager =  Principal()
mail_manager = MailManager()
toolbar = DebugToolbarExtension()
log_handler = RotatingFileHandler('app.log', maxBytes=10240, backupCount=3)

def create_app():
    # Construct the core app object
    app = Flask(__name__)
    app.logger.debug('Loading config...')
    app.config.from_pyfile("config.py")
    
    # activar debug i logs
    app.debug = True

    log_handler = RotatingFileHandler('app.log', maxBytes=10240, backupCount=3)
    log_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]'
    ))
    log_handler.setLevel(logging.DEBUG)
    app.logger.addHandler(log_handler)
    app.logger.setLevel(logging.DEBUG)

    log_level = app.config.get('LOG_LEVEL', 'DEBUG')
    if log_level not in ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']:
        raise ValueError('Nivell de registre no vàlid')
    app.logger.setLevel(getattr(logging, log_level))

    # Inicialitza els plugins
    app.logger.debug('Loading manager plugins...')
    db_manager.init_app(app)
    login_manager.init_app(app)
    principal_manager.init_app(app)
    mail_manager.init_app(app)
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