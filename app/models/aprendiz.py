# este archivo define la estructura de la tabla "aprendices" en la base de datos MySQL y 
# proporciona un método para convertir los registros en diccionarios,
# lo que facilita su manipulación y visualización en la API.
from app import db
from datetime import date, datetime

class Aprendiz(db.Model):
    __tablename__ = 'aprendices'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    telefono = db.Column(db.String(20))
    direccion = db.Column(db.String(200))
    fechaNacimiento = db.Column(db.Date)
    programaFormacion = db.Column(db.String(150))
    estado = db.Column(db.String(20), default="ACTIVO")
    genero = db.Column(db.String(20))
    documento = db.Column(db.String(20), unique=True, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "email": self.email,
            "telefono": self.telefono,
            "direccion": self.direccion,
            "fechaNacimiento": self.fechaNacimiento.isoformat() if self.fechaNacimiento else "",
            "programaFormacion": self.programaFormacion,
            "estado": self.estado,
            "genero": self.genero,
            "documento": self.documento
        }