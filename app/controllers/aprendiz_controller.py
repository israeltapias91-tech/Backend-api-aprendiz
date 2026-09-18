from flask import Blueprint, jsonify, request
from app.models.aprendiz import Aprendiz
from app import db

# Creamos el Blueprint (nuestro enrutador)
aprendiz_bp = Blueprint('aprendiz', __name__)

# Endpoint GET: Obtener todos los aprendices
@aprendiz_bp.route('/aprendices', methods=['GET'])
def obtener_aprendices():
    aprendices = Aprendiz.query.all()
    return jsonify([aprendiz.to_dict() for aprendiz in aprendices])

# Endpoint POST: Crear un nuevo aprendiz
@aprendiz_bp.route('/aprendices', methods=['POST'])
def crear_aprendiz():
    # Recibimos el JSON que envíe el cliente (Postman, React, etc.)
    datos = request.get_json()
    
    # Creamos el objeto Python (similar a instanciar la clase en Java)
    nuevo_aprendiz = Aprendiz(
        nombre=datos['nombre'],
        documento=datos['documento'],
        ficha=datos.get('ficha', 'No asignada')
    )
    
    # Lo guardamos en la base de datos (Equivalente a repository.save())
    db.session.add(nuevo_aprendiz)
    db.session.commit()
    
    return jsonify({
        "mensaje": "Aprendiz creado exitosamente",
        "aprendiz": nuevo_aprendiz.to_dict()
    }), 201