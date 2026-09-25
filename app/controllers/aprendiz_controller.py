from flask import request, jsonify, Blueprint
from app.models.aprendiz import Aprendiz
from app import db
from datetime import datetime

aprendiz_bp = Blueprint('aprendiz_bp', __name__)

# GET: Leer todos los aprendices
@aprendiz_bp.route('/aprendices', methods=['GET'])
def obtener_aprendices():
    aprendices = Aprendiz.query.all()
    return jsonify([a.to_dict() for a in aprendices]), 200

# GET: Leer un aprendiz por ID
@aprendiz_bp.route('/aprendices/<int:id>', methods=['GET'])
def obtener_aprendiz(id):
    aprendiz = Aprendiz.query.get(id)
    if aprendiz:
        return jsonify(aprendiz.to_dict()), 200
    return jsonify({"mensaje": "Aprendiz no encontrado"}), 404

# POST: Crear un aprendiz
@aprendiz_bp.route('/aprendices', methods=['POST'])
def crear_aprendiz():
    datos = request.get_json()
    
    # Transformar la fecha de texto (YYYY-MM-DD) a un objeto Date de Python
    fecha_nac_str = datos.get('fechaNacimiento')
    fecha_obj = datetime.strptime(fecha_nac_str, '%Y-%m-%d').date() if fecha_nac_str else None

    nuevo_aprendiz = Aprendiz(
        nombre=datos['nombre'],
        apellido=datos['apellido'],
        email=datos['email'],
        telefono=datos.get('telefono'),
        direccion=datos.get('direccion'),
        fechaNacimiento=fecha_obj,
        programaFormacion=datos.get('programaFormacion'),
        estado=datos.get('estado', 'ACTIVO'),
        genero=datos.get('genero'),
        documento=datos['documento']
    )
    db.session.add(nuevo_aprendiz)
    db.session.commit()
    
    return jsonify({"mensaje": "Aprendiz creado exitosamente en MySQL"}), 201

# PUT: Actualizar un aprendiz
@aprendiz_bp.route('/aprendices/<int:id>', methods=['PUT'])
def actualizar_aprendiz(id):
    aprendiz = Aprendiz.query.get(id)
    if not aprendiz:
        return jsonify({"mensaje": "Aprendiz no encontrado"}), 404
        
    datos = request.get_json()
    
    # Si envían una nueva fecha, la convertimos
    fecha_nac_str = datos.get('fechaNacimiento')
    if fecha_nac_str:
        aprendiz.fechaNacimiento = datetime.strptime(fecha_nac_str, '%Y-%m-%d').date()

    # Actualizamos el resto de los datos
    aprendiz.nombre = datos.get('nombre', aprendiz.nombre)
    aprendiz.apellido = datos.get('apellido', aprendiz.apellido)
    aprendiz.email = datos.get('email', aprendiz.email)
    aprendiz.telefono = datos.get('telefono', aprendiz.telefono)
    aprendiz.direccion = datos.get('direccion', aprendiz.direccion)
    aprendiz.programaFormacion = datos.get('programaFormacion', aprendiz.programaFormacion)
    aprendiz.estado = datos.get('estado', aprendiz.estado)
    aprendiz.genero = datos.get('genero', aprendiz.genero)
    aprendiz.documento = datos.get('documento', aprendiz.documento)

    db.session.commit()
    return jsonify({"mensaje": "Aprendiz actualizado correctamente en MySQL"}), 200

# DELETE: Eliminar un aprendiz
@aprendiz_bp.route('/aprendices/<int:id>', methods=['DELETE'])
def eliminar_aprendiz(id):
    aprendiz = Aprendiz.query.get(id)
    if not aprendiz:
        return jsonify({"mensaje": "Aprendiz no encontrado"}), 404
        
    db.session.delete(aprendiz)
    db.session.commit()
    return jsonify({"mensaje": "Aprendiz eliminado exitosamente de MySQL"}), 200