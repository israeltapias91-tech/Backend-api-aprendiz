from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

# Inicializamos SQLAlchemy sin conectarlo a la app todavía
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)
    
    # Vinculamos la base de datos a esta app
    db.init_app(app)

    # Importamos y registramos nuestro controlador (Blueprint)
    from app.controllers.aprendiz_controller import aprendiz_bp
    app.register_blueprint(aprendiz_bp, url_prefix='/api/v1')

    # Creamos las tablas si no existen
    with app.app_context():
        db.create_all()

    return app