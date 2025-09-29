import inventario_estru.agregar_producto as agregar_producto
import inventario_estru.mostrar_invetario as mostrar_invetario
import inventario_estru.buscar_producto as buscar_producto
import inventario_estru.eliminar_producto as eliminar_producto
print("************** Gestion de Inventario***********\n")
def main():
    
    opcion = ""
    while opcion != "E":
        print("\n---MENU DEL INVENTARIO---")
        print("A . Agregar producto:")
        print("B . Mostrar inventario:")
        print("C . Buscar producto:")
        print("D . Eliminar producto:")
        print("E . salir:")
        print("**INGRESE UNA OPCION VALIDA**")

        opcion = input("Ingrese la opcion deseada: ").upper()
        if opcion == "A":
            agregar_producto.agregar_producto()
        elif opcion == "B":
            mostrar_invetario.mostrar_inventario()
        elif opcion == "C":
            buscar_producto.buscar_producto()
        elif opcion == "D":
            eliminar_producto.eliminar_producto()
        elif opcion == 'E':
            print("¡Hasta la próxima! 👋")
        else:
            print("opcion Incorrecta intenta de nuevo!")

if __name__ == "__main__":
    main()                