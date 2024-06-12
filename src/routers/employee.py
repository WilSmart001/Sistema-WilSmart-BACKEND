from flask import Blueprint,jsonify,request
from models.employee_model import Employee_Model

main = Blueprint('employee_blueprint',__name__)

@main.route('/register', methods=['POST'])
def register_employee():
    try:
        nombre_completo = request.json['nombre_completo']
        telefono = request.json['telefono']
        ci = request.json['ci']
        salario = request.json['salario']
        foto = request.json['foto']
        correo = request.json['correo']
        fecha_nacimiento = request.json['fecha_nacimiento']
        direccion = request.json['direccion']
        estado_civil = request.json['estado_civil']
        cargo = request.json['cargo']
        cod = Employee_Model.register_employee(nombre_completo,telefono,ci,salario,foto,correo,fecha_nacimiento,direccion,estado_civil,cargo)
        if cod > 0:
            return jsonify(cod)
        return jsonify({'message': "Error while registering"}), 500
    except Exception as ex:
        return jsonify({'message':str(ex)}), 500

@main.route('/update/<cod>', methods=['PUT'])
def update_employee(cod):
    try:
        nombre_completo = request.json['nombre_completo']
        telefono = request.json['telefono']
        ci = request.json['ci']
        salario = request.json['salario']
        foto = request.json['foto']
        correo = request.json['correo']
        fecha_nacimiento = request.json['fecha_nacimiento']
        direccion = request.json['direccion']
        estado_civil = request.json['estado_civil']
        cargo = request.json['cargo']
        cod = Employee_Model.update_employee(cod,nombre_completo,telefono,ci,salario,foto,correo,fecha_nacimiento,direccion,estado_civil,cargo)
        if cod > 0:
            return jsonify(cod)
        return jsonify({'message': "Error during update"}), 404
    except Exception as ex:
        return jsonify({'message':str(ex)}), 500
    
@main.route('/get_one/<cod>')
def get_employee(cod):
    try:
        employee = Employee_Model.get_employee(cod)
        if employee != None:
            return jsonify(employee)
        return jsonify({}),404
    except Exception as ex:
        return jsonify({'message':str(ex)}),500

@main.route('/get_all')
def get_employees():
    try:
        employees = Employee_Model.get_employees()
        return jsonify(employees)
    except Exception as ex:
        return jsonify({'message':str(ex)}),500
    
@main.route('/delete/<cod>', methods=['DELETE'])
def delete_employee(cod):
    try:
        cod = Employee_Model.deleted_employee(cod)
        if cod > 0:
            return jsonify(cod)
        return jsonify({'message': "Employee not deleted"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
