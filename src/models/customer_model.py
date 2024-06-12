from database.db import get_connection

class Customer_Model():
    @classmethod
    def insert_customer(self, nombre, identificacion, celular, correo, domicilio):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('''
                                INSERT INTO clientes (nombre_cli, identificacion_cli, celular_cli, correo_cli, domicilio_cli)
                                VALUES (%s, %s, %s, %s, %s)
                                RETURNING cod_clientes
                                ''',(nombre,identificacion,celular,correo,domicilio))
            connection.commit()
            cod = cursor.fetchone()[0]
            return cod
        except Exception as ex:
            raise(ex)

    @classmethod
    def get_customer(self,cod):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('''
                                SELECT cod_clientes, nombre_cli, identificacion_cli, celular_cli, correo_cli, domicilio_cli
                                FROM clientes
                                WHERE cod_clientes = %s;
                                ''',(cod,))
                row = cursor.fetchone()
                return {
                    'cod': row[0],
                    'nombre': row[1],
                    'identificacion': row[2],
                    'celular': row[3],
                    'correo': row[4],
                    'domicilio': row[5]
                }
        except Exception as ex:
            raise(ex)

    @classmethod
    def get_customers(self):
        try:
            connection = get_connection()
            customers = []
            with connection.cursor() as cursor:
                cursor.execute('''
                            SELECT cod_clientes, nombre_cli, identificacion_cli
                            FROM clientes
                            ORDER BY cod_clientes ASC;
                                ''')
                result = cursor.fetchall()
                if result is not None:
                    for row in result:
                        customers.append(
                            {
                                'cod': row[0],
                                'nombre': row[1],
                                'identificacion': row[2]
                            }
                        )
            connection.close()
            return customers
        except Exception as ex:
            raise Exception(ex)


