from inventario_estru.conemysql import buscar_producto_bd

def buscar_producto():
    nombre_buscado = input("Cual es el nombre del producto a buscar: ").lower()
    producto_encontrado = buscar_producto_bd(nombre_buscado)
    
    if producto_encontrado:
            print("---Producto encontrado---")
            nombre, precio, cantidad = producto_encontrado
            print(f" Nombre {nombre} | precio {precio:.2f} | Cantidad {cantidad}") 
            return # termina si se encuentra el producto
    else:   
        print("Producto no encontrado")