class Config:
    # Cambia 'root' y '' si tu MySQL tiene otro usuario/contraseña
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1234@localhost/sena_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False