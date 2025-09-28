from conemysql import agragar_producto_bd

def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    agragar_producto_bd(nombre, precio, cantidad)    
