from flask import Blueprint,jsonify,request
from models.product_model import Product_Model

main = Blueprint('product_blueprint',__name__)

@main.route('/register', methods=['POST'])
def register_product():
    try:
        nombre = request.json['nombre']
        cantidad = request.json['cantidad']
        fecha = request.json['fecha']
        precio = request.json['precio']
        imagen = request.json['imagen']
        descripcion = request.json['descripcion']
        categoria = request.json['categoria']
        marca = request.json['marca']
        cod = Product_Model.register_product(nombre, cantidad, fecha, precio, imagen, descripcion, categoria, marca)
        if cod > 0:
            return jsonify(cod)
        return jsonify({'message': "Error while registering"}), 500
    except Exception as ex:
        return jsonify({'message':str(ex)}), 500

@main.route('/update/<cod>', methods=['PUT'])
def update_product(cod):
    try:
        nombre = request.json['nombre']
        cantidad = request.json['cantidad']
        fecha = request.json['fecha']
        precio = request.json['precio']
        imagen = request.json['imagen']
        descripcion = request.json['descripcion']
        categoria = request.json['categoria']
        marca = request.json['marca']
        cod = Product_Model.update_product(cod,nombre, cantidad, fecha, precio, imagen, descripcion, categoria, marca)
        if cod > 0:
            return jsonify(cod)
        return jsonify({'message': "Error during update"}), 404
    except Exception as ex:
        return jsonify({'message':str(ex)}), 500

@main.route('/get_all')
def get_products():
    try:
        products = Product_Model.get_products()
        return jsonify(products)
    except Exception as ex:
        return jsonify({'message':str(ex)}),500
    
@main.route('/delete/<cod>', methods=['DELETE'])
def delete_product(cod):
    try:
        cod = Product_Model.deleted_product(cod)
        if cod > 0:
            return jsonify(cod)
        return jsonify({'message': "Product not deleted"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/get_increment')
def increment_product():
    try:
        pruducts = Product_Model.increment_product()
        return jsonify(pruducts)
    except Exception as ex:
        return jsonify({'message':str(ex)}),500

@main.route('/arithmetic/<cod>', methods=['PUT'])
def arithmetic_product(cod):
    try:
        cod = request.json['cod']
        value = request.json['value']
        cod = Product_Model.arithmetic_product(cod,value)
        if cod > 0:
            return jsonify(cod)
        return jsonify({'message': "Error during update"}), 404
    except Exception as ex:
        return jsonify({'message':str(ex)}), 500
