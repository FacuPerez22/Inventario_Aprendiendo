from inventario_estru.conemysql import mostrar_inventario_db

def mostrar_inventario():
    productos = mostrar_inventario_db()
    if productos:
        print("\n---Inventario actual---")
        for producto in productos:
            nombre, precio, cantidad = producto
            print(f"Nombre {nombre} | Precio {precio:.2f} | Cantidad {cantidad}")
        print("-------------------------\n")
        print("\n---MOSTRAR INVENTARIO---")
    else:
        print("\n El programa esta vacio  o se pudo conectar con la BAse de dATO")