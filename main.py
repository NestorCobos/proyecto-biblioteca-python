from tabulate import tabulate




from coleccion import (
    agregar_elemento,
    listar_elementos,
    buscar_elemento,
    editar_elemento,
    eliminar_elemento,
    mostrar_recomendados
)

from archivo_json import cargar_datos

from utilidades import (
    limpiar_pantalla,
    pausar
)

def mostrar_menu():

    print("\n" + "=" * 40)
    print("ADMINISTRADOR DE COLECCIÓN")
    print("=" * 40)
    print("1. Agregar elemento")
    print("2. Listar elementos")
    print("3. Buscar elemento")
    print("4. Editar elemento")
    print("5. Eliminar elemento")
    print("6. Mostrar recomendados")
    print("0. Salir")
    print("=" * 40)


coleccion = cargar_datos()

ejecutando = True

while ejecutando:

    limpiar_pantalla()

    mostrar_menu()

    opcion = input(
        "Seleccione una opción: "
    )

    if opcion == "1":

        agregar_elemento(coleccion)
        pausar()

    elif opcion == "2":

        listar_elementos(coleccion)
        pausar()

    elif opcion == "3":

        buscar_elemento(coleccion)
        pausar()

    elif opcion == "4":

        editar_elemento(coleccion)
        pausar()

    elif opcion == "5":

        eliminar_elemento(coleccion)
        pausar()

    elif opcion == "6":

        mostrar_recomendados(coleccion)
        pausar()

    elif opcion == "0":

        print("Gracias por usar el sistema.")
        ejecutando = False

    else:

        print("Opción no válida.")
        pausar()
