class Config:
    # Tu conexión actual a MySQL (sin contraseña)
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1234@localhost/sena_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # La nueva conexión para MongoDB
    MONGO_URI = 'mongodb://localhost:27017/sena_mongodb'