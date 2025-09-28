from conemysql import eliminar_producto_bd

def eliminar_producto():
    nombre_a_eliminar = input("Nombre del poroducto a eliminar: ").lower()
    eliminar_producto_bd(nombre_a_eliminar)
    
    