from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo
from app.config import Config

db = SQLAlchemy()
mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)
    
    # Inicializamos ambas bases de datos
    db.init_app(app)
    mongo.init_app(app)
    
    # Registramos el controlador de MySQL
    from app.controllers.aprendiz_controller import aprendiz_bp
    app.register_blueprint(aprendiz_bp, url_prefix='/api/v1')

    # Registramos el nuevo controlador de MongoDB
    from app.controllers.aprendiz_mongo_controller import aprendiz_mongo_bp
    app.register_blueprint(aprendiz_mongo_bp, url_prefix='/api/v1')

    with app.app_context():
        db.create_all()

    return app