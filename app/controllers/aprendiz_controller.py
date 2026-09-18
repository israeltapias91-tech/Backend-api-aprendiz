from flask import Blueprint, jsonify
from app.models.aprendiz import Aprendiz

# Creamos el Blueprint (nuestro enrutador)
aprendiz_bp = Blueprint('aprendiz', __name__)

@aprendiz_bp.route('/aprendices', methods=['GET'])
def obtener_aprendices():
    aprendices = Aprendiz.query.all()
    return jsonify([aprendiz.to_dict() for aprendiz in aprendices])