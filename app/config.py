import os
from pathlib import Path
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env en la raíz del proyecto
env_path = Path(__file__).resolve().parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS', 'False').lower() in ('true', '1')

    # Parámetros individuales de MySQL
    MYSQL_HOST = os.getenv('MYSQL_HOST', '127.0.0.1')
    MYSQL_PORT = os.getenv('MYSQL_PORT', '3307')
    MYSQL_USER = os.getenv('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', '1234')
    MYSQL_DB = os.getenv('MYSQL_DB', 'sena_db')

    # URI de SQLAlchemy: usa SQLALCHEMY_DATABASE_URI si está definida, o se construye dinámicamente
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'SQLALCHEMY_DATABASE_URI',
        f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}'
    )

    # Conexión para MongoDB
    #MONGO_URI = os.getenv('MONGO_URI', 'mongodb://127.0.0.1:27017/sena_mongodb')
    MONGO_URI = os.getenv(
        'MONGO_URI', 
        'mongodb://127.0.0.1:27017/sena_mongodb'
    )