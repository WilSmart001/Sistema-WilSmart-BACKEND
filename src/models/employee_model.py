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
            return int(cod)
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
                connection.close()
                return {
                    'nombre': str(row[0]).strip(),
                    'telefono': str(row[1]).strip(),
                    'ci': str(row[2]).strip(),
                    'salario': float(str(str(row[3]).split(' ')[0]).replace(',','.')),
                    'foto': str(row[4]).strip(),
                    'correo': str(row[5]).strip(),
                    'fecha_nacimiento': row[6],
                    'direccion': str(row[7]).strip(),
                    'estado_civil': str(row[8]).strip(),
                    'cargo': str(row[9]).strip()
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
                            SELECT e.cod_empleados, e.nombre_completo_emp, c.nombre_car, e.telefono_emp, e.ci_emp, e.salario_emp
                            FROM empleados AS e
                            JOIN cargos AS c ON c.cod_cargos = e.cod_cargos
                            ORDER BY e.cod_empleados;
                                ''')
                result = cursor.fetchall()
                if result is not None:
                    for row in result:
                        employees.append(
                            {
                                'cod': int(row[0]),
                                'nombre': str(row[1]).strip(),
                                'cargo': str(row[2]).strip(),
                                'telefono': str(row[3]).strip(),
                                'ci': str(row[4]).strip(),
                                'salario': float(str(str(row[5]).split(' ')[0]).replace(',','.'))
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
                return int(cod)
        except Exception as ex:
            raise(ex)