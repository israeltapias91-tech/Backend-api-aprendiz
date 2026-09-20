from flask import Blueprint, jsonify, request
from app import mongo
from bson.objectid import ObjectId 

aprendiz_mongo_bp = Blueprint('aprendiz_mongo', __name__)

# GET: Obtener todos
@aprendiz_mongo_bp.route('/mongo/aprendices', methods=['GET'])
def obtener_aprendices_mongo():
    aprendices = mongo.db.aprendices.find()
    resultado = []
    for ap in aprendices:
        resultado.append({
            "id": str(ap["_id"]),
            "nombre": ap.get("nombre", ""),
            "documento": ap.get("documento", ""),
            "ficha": ap.get("ficha", "")
        })
    return jsonify(resultado)

# POST: Crear aprendiz
@aprendiz_mongo_bp.route('/mongo/aprendices', methods=['POST'])
def crear_aprendiz_mongo():
    datos = request.get_json()
    nuevo_aprendiz = {
        "nombre": datos['nombre'],
        "documento": datos['documento'],
        "ficha": datos.get('ficha', 'No asignada')
    }
    mongo.db.aprendices.insert_one(nuevo_aprendiz)
    return jsonify({"mensaje": "Aprendiz creado exitosamente en MongoDB"}), 201

# PUT: Actualizar aprendiz
@aprendiz_mongo_bp.route('/mongo/aprendices/<id>', methods=['PUT'])
def actualizar_aprendiz_mongo(id):
    datos = request.get_json()
    resultado = mongo.db.aprendices.update_one(
        {"_id": ObjectId(id)}, 
        {"$set": datos}
    )
    if resultado.matched_count == 0:
        return jsonify({"error": "Aprendiz no encontrado en Mongo"}), 404
    return jsonify({"mensaje": "Aprendiz actualizado correctamente en MongoDB"})

# DELETE: Eliminar aprendiz
@aprendiz_mongo_bp.route('/mongo/aprendices/<id>', methods=['DELETE'])
def eliminar_aprendiz_mongo(id):
    resultado = mongo.db.aprendices.delete_one({"_id": ObjectId(id)})
    if resultado.deleted_count == 0:
        return jsonify({"error": "Aprendiz no encontrado en Mongo"}), 404
    return jsonify({"mensaje": "Aprendiz eliminado exitosamente de MongoDB"})