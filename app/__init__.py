from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo
from app.config import Config

# Instancias de las bases de datos
db = SQLAlchemy()
mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Orígenes permitidos (Netlify, Vercel y desarrollo local con Vite)
    origins_permitidos = [
        "https://shimmering-frangipane-c83ef7.netlify.app", # <-- Lee tu página en Netlify
        r"https://.*\.netlify\.app",                        # <-- Lee cualquier enlace de Netlify
        "https://frontend-api-myproyecto.vercel.app",       # <-- Sigue leyendo tu página en Vercel
        r"https://.*\.vercel\.app",                         # <-- Sigue leyendo cualquier enlace de Vercel
        "http://localhost:5173",                            # <-- Sigue funcionando en tu PC local
        "http://127.0.0.1:5173",
        "http://localhost:3000"
    ]
    
    # Configuración de CORS para todas las rutas bajo /api/
    CORS(app, resources={
        r"/api/*": {
            "origins": origins_permitidos,
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": ["Content-Type", "Authorization"]
        }
    })
    
    # Inicializamos ambas bases de datos
    db.init_app(app)
    mongo.init_app(app)
    
    # Registramos el controlador de MySQL
    from app.controllers.aprendiz_controller import aprendiz_bp
    app.register_blueprint(aprendiz_bp, url_prefix='/api/v1')

    # Registramos el controlador de MongoDB
    from app.controllers.aprendiz_mongo_controller import aprendiz_mongo_bp
    app.register_blueprint(aprendiz_mongo_bp, url_prefix='/api/v1')

    # Creamos las tablas si no existen
    with app.app_context():
        db.create_all()

    return app