from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.routes_auth import auth_bp
import os


db_manager = SQLAlchemy()

def create_app():
    # Construct the core app object
    app = Flask(__name__)

    # ruta absoluta d'aquesta carpeta
    basedir = os.path.abspath(os.path.dirname(__file__)) 

    # Inicialitza els plugins
    db_manager.init_app(app)

    with app.app_context():
        from . import routes_main

        # Registra els blueprints
        app.register_blueprint(routes_main.main_bp)

    app.logger.info("Aplicació iniciada")

    return app