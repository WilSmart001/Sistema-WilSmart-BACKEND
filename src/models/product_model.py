from database.db import get_connection

class Product_Model():
    @classmethod
    def register_product(self,nombre, cantidad, fecha, precio, imagen, descripcion, categoria, marca):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('''
                                INSERT INTO productos (nombre_pro, cantidad_pro, fecha_pro, precio_pro, imagen_pro, descripcion_pro, cod_categorias, cod_marcas)
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                                RETURNING cod_productos;
                                ''',(nombre, cantidad, fecha, precio, imagen, descripcion, categoria, marca))
            cod = cursor.fetchone()[0]
            connection.commit()
            connection.close()
            return int(cod)
        except Exception as ex:
            raise(ex)
    
    @classmethod
    def update_product(self, cod, nombre, cantidad, fecha, precio, imagen, descripcion, categoria, marca):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('''
                                UPDATE productos
                                SET nombre_pro = %s,
                                    cantidad_pro = %s,
                                    fecha_pro = %s,
                                    precio_pro = %s,
                                    imagen_pro = %s,
                                    descripcion_pro = %s,
                                    cod_categorias = %s,
                                    cod_marcas = %s,
                                WHERE cod_productos = %s;
                                ''',(nombre, cantidad, fecha, precio, imagen, descripcion, categoria, marca, cod))
            connection.commit()
            connection.close()
            return int(cod)
        except Exception as ex:
            raise(ex)

    @classmethod
    def get_products(self):
        try:
            connection = get_connection()
            products = []
            with connection.cursor() as cursor:
                cursor.execute('''
                            SELECT p.cod_productos, p.nombre_pro, p.descripcion_pro, m.nombre_mar, c.nombre_cat, p.cantidad_pro, p.fecha_pro, p.imagen_pro
                            FROM productos AS p
                            JOIN marcas AS m ON m.cod_marcas = p.cod_marcas
                            JOIN categorias AS c ON c.cod_categorias = p.cod_categorias;
                                ''')
                result = cursor.fetchall()
                if result is not None:
                    for row in result:
                        products.append(
                            {
                                'cod': int(row[0]),
                                'nombre': str(row[1]).strip(),
                                'descripcion': str(row[2]).strip(),
                                'marca': str(row[3]).strip(),
                                'categoria': str(row[4]).strip(),
                                'cantidad': int(row[5]),
                                'fecha': row[6],
                                'imagen': str(row[7]).strip()
                            }
                        )
            connection.close()
            return products
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def deleted_product(self,cod):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('''
                                DELETE FROM productos
                                WHERE cod_productos = %s;
                                ''',(cod,))
                connection.commit()
                connection.close()
                return int(cod)
        except Exception as ex:
            raise(ex)
    
    @classmethod
    def increment_product():
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('''
                                SELECT cod_productos, nombre_pro, cantidad_pro
                                FROM empleados;
                                ''')
                result = cursor.fetchall()
                if result is not None:
                    for row in result:
                        return {
                            'cod': int(row[0]),
                            'nombre': str(row[1]).strip(),
                            'cantidad': int(row[2]),
                        }
        except Exception as ex:
            raise(ex)
    
    @classmethod
    def arithmetic_product(cod, value):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('''
                                UPDATE productos
                                SET cantidad_pro = %s,
                                WHERE cod_productos = %s;
                                ''',(value,cod))
            connection.commit()
            connection.close()
            return int(cod)
        except Exception as ex:
            raise(ex)