from flask import request, jsonify, Blueprint
from app import mongo
from bson import ObjectId

aprendiz_mongo_bp = Blueprint('aprendiz_mongo_bp', __name__)

# GET: Leer todos los aprendices
@aprendiz_mongo_bp.route('/mongo/aprendices', methods=['GET'])
def obtener_aprendices_mongo():
    aprendices = mongo.db.aprendices.find()
    resultado = []
    for a in aprendices:
        a['_id'] = str(a['_id'])
        resultado.append(a)
    return jsonify(resultado), 200

# POST: Crear aprendiz
@aprendiz_mongo_bp.route('/mongo/aprendices', methods=['POST'])
def crear_aprendiz_mongo():
    datos = request.get_json()
    
    nuevo_aprendiz = {
        "nombre": datos['nombre'],
        "apellido": datos['apellido'],
        "email": datos['email'],
        "telefono": datos.get('telefono'),
        "direccion": datos.get('direccion'),
        "fechaNacimiento": datos.get('fechaNacimiento'), 
        "programaFormacion": datos.get('programaFormacion'),
        "estado": datos.get('estado', 'ACTIVO'),
        "genero": datos.get('genero'),
        "documento": datos['documento']
    }
    
    mongo.db.aprendices.insert_one(nuevo_aprendiz)
    return jsonify({"mensaje": "Aprendiz creado exitosamente en MongoDB"}), 201

# PUT: Actualizar aprendiz
@aprendiz_mongo_bp.route('/mongo/aprendices/<id>', methods=['PUT'])
def actualizar_aprendiz_mongo(id):
    datos = request.get_json()
    
    campos_actualizados = {
        "nombre": datos.get('nombre'),
        "apellido": datos.get('apellido'),
        "email": datos.get('email'),
        "telefono": datos.get('telefono'),
        "direccion": datos.get('direccion'),
        "fechaNacimiento": datos.get('fechaNacimiento'),
        "programaFormacion": datos.get('programaFormacion'),
        "estado": datos.get('estado'),
        "genero": datos.get('genero'),
        "documento": datos.get('documento')
    }
    
    # Limpiamos los campos vacíos por si el frontend no envía todo
    campos_actualizados = {k: v for k, v in campos_actualizados.items() if v is not None}

    resultado = mongo.db.aprendices.update_one(
        {'_id': ObjectId(id)}, 
        {'$set': campos_actualizados}
    )
    
    if resultado.matched_count == 0:
        return jsonify({"mensaje": "Aprendiz no encontrado en MongoDB"}), 404
        
    return jsonify({"mensaje": "Aprendiz actualizado correctamente en MongoDB"}), 200

# DELETE: Eliminar aprendiz
@aprendiz_mongo_bp.route('/mongo/aprendices/<id>', methods=['DELETE'])
def eliminar_aprendiz_mongo(id):
    resultado = mongo.db.aprendices.delete_one({'_id': ObjectId(id)})
    
    if resultado.deleted_count == 0:
        return jsonify({"mensaje": "Aprendiz no encontrado en MongoDB"}), 404
        
    return jsonify({"mensaje": "Aprendiz eliminado exitosamente de MongoDB"}), 200