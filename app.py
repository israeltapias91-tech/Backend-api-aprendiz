from flask import Flask, jsonify
from flask_cors import CORS

# Inicializamos la aplicación Flask (equivalente a tu @SpringBootApplication)
app = Flask(__name__)

# Habilitamos CORS para permitir que tu frontend en React se pueda conectar sin bloqueos
CORS(app)

# Creamos nuestro primer endpoint (equivalente a un @GetMapping en Spring Boot)
@app.route('/api/v1/estado', methods=['GET'])
def estado_api():
    # Retornamos un diccionario de Python que Flask convertirá automáticamente a JSON
    return jsonify({
        "mensaje": "¡Hola desde Flask! Tu API en Python está funcionando correctamente.",
        "estado": "OK"
    })

# Punto de entrada para encender el servidor en el puerto 5000
if __name__ == '__main__':
    app.run(debug=True, port=5000)