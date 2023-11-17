from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os


db_manager = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    # Construct the core app object
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    
    # ruta absoluta d'aquesta carpeta
    basedir = os.path.abspath(os.path.dirname(__file__)) 

    # Inicialitza els plugins
    db_manager.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        from . import routes_main
        from . import routes_auth

        # Registra els blueprints
        app.register_blueprint(routes_main.main_bp)
        app.register_blueprint(routes_auth.auth_bp)

    app.logger.info("Aplicació iniciada")

    return app