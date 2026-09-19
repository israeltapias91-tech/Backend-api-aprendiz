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
    # Recibimos el JSON que envíe el cliente
    datos = request.get_json()
    
    # Creamos el objeto Python
    nuevo_aprendiz = Aprendiz(
        nombre=datos['nombre'],
        documento=datos['documento'],
        ficha=datos.get('ficha', 'No asignada')
    )
    
    # Lo guardamos en la base de datos
    db.session.add(nuevo_aprendiz)
    db.session.commit()
    
    return jsonify({
        "mensaje": "Aprendiz creado exitosamente",
        "aprendiz": nuevo_aprendiz.to_dict()
    }), 201

# Endpoint PUT: Actualizar un aprendiz existente
@aprendiz_bp.route('/aprendices/<int:id>', methods=['PUT'])
def actualizar_aprendiz(id):
    # Buscamos al aprendiz por su ID
    aprendiz = Aprendiz.query.get(id)
    if not aprendiz:
        return jsonify({"error": "Aprendiz no encontrado"}), 404
    
    datos = request.get_json()
    
    # Actualizamos los datos
    aprendiz.nombre = datos.get('nombre', aprendiz.nombre)
    aprendiz.documento = datos.get('documento', aprendiz.documento)
    aprendiz.ficha = datos.get('ficha', aprendiz.ficha)
    
    db.session.commit()
    
    return jsonify({
        "mensaje": "Aprendiz actualizado correctamente",
        "aprendiz": aprendiz.to_dict()
    })

# Endpoint DELETE: Eliminar un aprendiz
@aprendiz_bp.route('/aprendices/<int:id>', methods=['DELETE'])
def eliminar_aprendiz(id):
    aprendiz = Aprendiz.query.get(id)
    if not aprendiz:
        return jsonify({"error": "Aprendiz no encontrado"}), 404
    
    db.session.delete(aprendiz)
    db.session.commit()
    
    return jsonify({"mensaje": "Aprendiz eliminado exitosamente"})