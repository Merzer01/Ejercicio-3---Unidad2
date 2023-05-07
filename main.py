from classManejador import manejador

def menu(m):
    print("---------->MENU<----------")
    print("Opcion 1: Mostrar para cada variable el dia y hora de menor y mayor valor")
    print("Opcion 2: Indicar la temperatura promedio por cada hora")
    print("Opcion 3: Listado de valores")
    print("Opcion 0: Salir\n")
    op = int(input("INGRESE NUMERO DE OPCION: "))
    print("----------------------------------------")
    
    while True:
        if op == 1:
            m.opcion1()     #PROBLEMA CON LOS INDICES DE LA MATRIZ
        elif op == 2:
            m.opcion2()
        elif op == 3:
            dia = int(input("Ingrese numero de dia a listar: "))
            m.opcion3(dia)
        elif op == 0:
            print("Saliendo...")
            break
        else:
            print("OPCION INVALIDA")
        op = int(input("INGRESE NUMERO DE OPCION: "))


if __name__ == '__main__':
    m = manejador()
    m.cargadatos()  #ITEM 2 -> REALIZAR LA CARGA DE LA MATRIZ CON INSTANCIA DE LA CLASE REGISTRO
    menu(m)