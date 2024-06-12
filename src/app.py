from flask import Flask
from flask_cors import CORS
from config import config
from routers import product, employee

app = Flask(__name__)
CORS(app, resources={'*': {'origin': 'http//localhost:5173'}})

def page_not_found(error):
    return '<h1>Not found page</h1>', 404

def run_flask_app():
    app.config.from_object(config['development'])
    app.register_blueprint(product.main, url_prefix='/product')
    app.register_blueprint(employee.main, url_prefix='/employee')
    app.register_error_handler(404, page_not_found)
    app.run()

if __name__ == '__main__':
    run_flask_app()
