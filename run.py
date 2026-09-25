import os
# Crea la importacion de la funcion create_app
from app import create_app

# Inicializa la aplicación Flask
app = create_app()

# Ejecuta la aplicación Flask
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_DEBUG', 'True').lower() in ('true', '1')
    app.run(host='0.0.0.0', port=port, debug=debug)