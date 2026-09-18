from app import db

class Aprendiz(db.Model):
    __tablename__ = 'aprendices'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    documento = db.Column(db.String(20), unique=True, nullable=False)
    ficha = db.Column(db.String(50))

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "documento": self.documento,
            "ficha": self.ficha
        }