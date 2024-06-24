from flask import Flask
from flask_cors import CORS
from config import config
from routers import product, employee

app = Flask(__name__)
CORS(app, resources={r'*': {'origin': 'http://localhost:5173'}})

def page_not_found(error):
    return '<h1>Not found page</h1>', 404

# Configuración de la aplicación Flask
def create_app(config_name):
    app.config.from_object(config[config_name])
    app.register_blueprint(product.main, url_prefix='/product')
    app.register_blueprint(employee.main, url_prefix='/employee')
    app.register_error_handler(404, page_not_found)
    return app

if __name__ == '__main__':
    # Aquí puedes ejecutar la aplicación directamente para pruebas locales
    app = create_app('development')
    app.run(host='0.0.0.0', port=5000)  # Puerto que prefieras para pruebas locales

