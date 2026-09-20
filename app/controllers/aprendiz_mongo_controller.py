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


# GET: Leer un aprendiz por ID 
@aprendiz_mongo_bp.route('/mongo/aprendices/<id>', methods=['GET'])
def obtener_aprendiz_mongo(id):
    try:
        # Convertimos el ID que llega por la URL a entero
        aprendiz = mongo.db.aprendices.find_one({'_id': int(id)})
        if aprendiz:
            aprendiz['id'] = aprendiz.pop('_id') # Renombramos _id a id para que el frontend no se confunda
            return jsonify(aprendiz), 200
        return jsonify({"mensaje": "Aprendiz no encontrado en MongoDB"}), 404
    except ValueError:
        return jsonify({"mensaje": "El ID debe ser un número entero"}), 400

# POST: Crear aprendiz con ID numérico (Auto-incremental manual)
@aprendiz_mongo_bp.route('/mongo/aprendices', methods=['POST'])
def crear_aprendiz_mongo():
    datos = request.get_json()
    
    # 1. Buscar el último aprendiz insertado, ordenado por _id descendente
    ultimo_aprendiz = mongo.db.aprendices.find_one(sort=[("_id", -1)])
    
    # 2. Calcular el nuevo ID numérico
    nuevo_id = 1
    if ultimo_aprendiz and isinstance(ultimo_aprendiz.get('_id'), int):
        nuevo_id = ultimo_aprendiz['_id'] + 1

    # 3. Insertar forzando el _id numérico
    nuevo_aprendiz = {
        "_id": nuevo_id,
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
    return jsonify({"mensaje": "Aprendiz creado exitosamente en MongoDB con ID numérico"}), 201

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
        {'_id': int(id)}, 
        {'$set': campos_actualizados}
    )
    
    if resultado.matched_count == 0:
        return jsonify({"mensaje": "Aprendiz no encontrado en MongoDB"}), 404
        
    return jsonify({"mensaje": "Aprendiz actualizado correctamente en MongoDB"}), 200

# DELETE: Eliminar aprendiz
@aprendiz_mongo_bp.route('/mongo/aprendices/<id>', methods=['DELETE'])
def eliminar_aprendiz_mongo(id):
    resultado = mongo.db.aprendices.delete_one({'_id': int(id)})
    
    if resultado.deleted_count == 0:
        return jsonify({"mensaje": "Aprendiz no encontrado en MongoDB"}), 404
        
    return jsonify({"mensaje": "Aprendiz eliminado exitosamente de MongoDB"}), 200