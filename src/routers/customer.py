from flask import Blueprint,jsonify,request
from models.customer_model import Customer_Model

main = Blueprint('customer_blueprint',__name__)

@main.route('/insert', methods=['POST'])
def insert_customer():
    try:
        nombre = request.json['nombre']
        identificacion = request.json['identificacion']
        celular = request.json['celular']
        correo = request.json['correo']
        domicilio = request.json['domicilio']
        cod = Customer_Model.insert_customer(nombre,identificacion,celular,correo,domicilio)
        if cod > 0:
            return jsonify(cod)
        return jsonify({'message': "Error al insertar"}), 500
    except Exception as ex:
        return jsonify({'message':str(ex)}), 500
    
@main.route('/get_one/<cod>')
def get_customer(cod):
    try:
        customer = Customer_Model.get_customer(cod)
        if customer != None:
            return jsonify(customer)
        else:
            return jsonify({}),404
    except Exception as ex:
        return jsonify({'message':str(ex)}),500

@main.route('/get_all')
def get_customers():
    try:
        customers = Customer_Model.get_customers()
        return jsonify(customers)
    except Exception as ex:
        return jsonify({'message':str(ex)}),500
