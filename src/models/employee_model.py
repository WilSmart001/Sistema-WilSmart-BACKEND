from database.db import get_connection

class Employee_Model():
    @classmethod
    def register_employee(self,nombre_completo, telefono, ci, salario, foto, correo, fecha_nacimiento, direccion, estado_civil, cargo):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('''
                                INSERT INTO empleados (nombre_completo_emp, telefono_emp, ci_emp, salario_emp, foto_emp, correo_emp, fecha_nacimiento_emp, direccion_emp, cod_estados_civiles, cod_cargos)
                                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                                RETURNING cod_empleados;
                                ''',(nombre_completo,telefono,ci,salario,foto,correo,fecha_nacimiento,direccion,estado_civil,cargo))
            cod = cursor.fetchone()[0]
            connection.commit()
            connection.close()
            return cod
        except Exception as ex:
            raise(ex)
    
    @classmethod
    def update_employee(self,cod,nombre_completo, telefono, ci, salario, foto, correo, fecha_nacimiento, direccion, estado_civil, cargo):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('''
                                UPDATE empleados
                                SET nombre_completo_emp = %s,
                                    telefono_emp = %s,
                                    ci_emp = %s,
                                    salario_emp = %s,
                                    foto_emp = %s,
                                    correo_emp = %s,
                                    fecha_nacimiento_emp = %s,
                                    direccion_emp = %s,
                                    cod_estados_civiles = %s,
                                    cod_cargos = %s
                                WHERE cod_empleados = %s;
                                ''',(nombre_completo,telefono,ci,salario,foto,correo,fecha_nacimiento,direccion,estado_civil,cargo,cod))
            connection.commit()
            connection.close()
            return cod
        except Exception as ex:
            raise(ex)

    @classmethod
    def get_employee(self,cod):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('''
                                SELECT e.nombre_completo_emp, e.telefono_emp, e.ci_emp, e.salario_emp, e.foto_emp, e.correo_emp, e.fecha_nacimiento_emp, e.direccion_emp, ec.nombre_ec, c.nombre_car
                                FROM empleados AS e
                                JOIN estados_civiles AS ec ON e.cod_estados_civiles = ec.cod_estados_civiles
                                JOIN cargos AS c ON c.cod_cargos = e.cod_cargos
                                WHERE e.cod_empleados = %s;
                                ''',(cod,))
                row = cursor.fetchone()
                return {
                    'nombre': row[0],
                    'telefono': row[1],
                    'ci': row[2],
                    'salario': row[3],
                    'foto': row[4],
                    'correo': row[5],
                    'fecha_nacimiento': row[6],
                    'direccion': row[7],
                    'estado_civil': row[8],
                    'cargo': row[9]
                }
        except Exception as ex:
            raise(ex)

    @classmethod
    def get_employees(self):
        try:
            connection = get_connection()
            employees = []
            with connection.cursor() as cursor:
                cursor.execute('''
                            SELECT e.cod_empleados.foto_emp, e.nombre_completo_emp, c.nombre_car, e.telefono_emp, e.ci_emp, e.salario_emp
                            FROM empleados AS e
                            JOIN cargo AS c ON c.cod_cargos = e.cod_cargos
                            ORDER BY e.cod_empleados;
                                ''')
                result = cursor.fetchall()
                if result is not None:
                    for row in result:
                        employees.append(
                            {
                                'cod': row[0],
                                'nombre': row[1],
                                'cargo': row[2],
                                'telefono': row[3],
                                'ci': row[4],
                                'salario': row[5]
                            }
                        )
            connection.close()
            return employees
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def deleted_employee(self,cod):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('''
                                DELETE FROM empleados
                                WHERE cod_empleados = %s;
                                ''',(cod,))
                connection.commit()
                connection.close()
                return cod
        except Exception as ex:
            raise(ex)