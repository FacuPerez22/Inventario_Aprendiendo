import mysql.connector
config = {
    "user": "root",
    "password": "Facu2025.",
    "host" : "localhost",
    "database": "inventario_fa"
}

def conectar_bd():
    try:
        return mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        print(f"Error al conectar:{err}")
        return None

def agragar_producto_bd(nombre, precio, cantidad):
    conexion = conectar_bd()
    if conexion is None:
        return
        
    cursor = conexion.cursor()
    sql = "INSERT INTO producto (nombre, precio, cantidad) VALUES (%s, %s, %s)"
    valores = (nombre, precio, cantidad)

    try:
        cursor.execute(sql, valores)
        conexion.commit()
        print(f"Producto {nombre} agragado a la base de dato")
    except mysql.connector.Error as err:
        print(f"Error al agragar el producto {err}")
    finally:
        cursor.close()
        conexion.close()
    
def mostrar_inventario_db():
    conexion = conectar_bd()
    if conexion is None:
        return None
    
    cursor = conexion.cursor()
    sql = "SELECT nombre, precio, cantidad FROM producto"

    try:
        cursor.execute(sql)
        producto = cursor.fetchall()
        return producto
    except mysql.connector.Error as err:
        print(f" Error al mostrar el inventario {err}")
    finally:
        cursor.close()
        conexion.close()

def eliminar_producto_bd(nombre_a_eliminar):
    conexion = conectar_bd()
    if conexion is None:
        return
    
    cursor = conexion.cursor()
    sql = "DELETE FROM producto WHERE nombre = %s"

    try:
        cursor.execute(sql, (nombre_a_eliminar,))
        conexion.commit()
        print(f"Producto {nombre_a_eliminar} eliminado de la base de datos. ")
    except mysql.connector.Error as err:
        print(f"Error al eliminar el producto {err}")
    finally:
        cursor.close()
        conexion.close()

def buscar_producto_bd(nombre_buscado):
    conexion = conectar_bd()
    if conexion is None:
        return None 
    
    cursor = conexion.cursor()
    sql = "SELECT nombre, precio, cantidad FROM producto WHERE nombre = %s "
 
    try:
        cursor.execute(sql,(nombre_buscado,) )
        producto = cursor.fetchone()
        return producto
    except mysql.connector.Error as err:
        print(f" Error al buscar el Producto {err}")
        return None
    finally:
        cursor.close()
        conexion.close()
        print("Conexion cerrada, ")




