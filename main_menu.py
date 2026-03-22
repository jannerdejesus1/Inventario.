"""
app.py
Menu principal del sistema de gestion de inventario.
Importa todas las funciones desde funciones.py.
"""

from funciones import (
    agregar_producto,
    mostrar_inventario,
    buscar_producto,
    actualizar_producto,
    eliminar_producto,
    calcular_estadisticas,
    guardar_csv,
    gestionar_carga_csv,
    crear_archivo_si_no_existe,
    RUTA_DEFAULT
)

# Inventario en memoria como lista de diccionarios
inventario = []

# Al iniciar el programa se verifica que el archivo CSV exista
crear_archivo_si_no_existe(RUTA_DEFAULT)


# Muestra las opciones del menu y retorna la opcion elegida
def mostrar_menu():
    print("=============================")
    print("  MENU - GESTION INVENTARIO  ")
    print("=============================")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Estadisticas")
    print("7. Guardar CSV")
    print("8. Cargar CSV")
    print("9. Salir")
    print("-----------------------------")
    return input("Seleccione una opcion (1-9): ")


# Subflujo para buscar: pide el nombre y muestra el resultado
def opcion_buscar():
    nombre = input("Nombre del producto a buscar: ").strip()
    resultado = buscar_producto(inventario, nombre)
    if resultado is not None:
        print("Encontrado - Nombre: " + resultado["nombre"] +
              " | Precio: " + str(resultado["precio"]) +
              " | Cantidad: " + str(resultado["cantidad"]) + "\n")
    else:
        print("Producto '" + nombre + "' no encontrado.\n")


# Subflujo para guardar: pide la ruta y llama a guardar_csv
def opcion_guardar():
    ruta = input("Ruta de destino (Enter para '" + RUTA_DEFAULT + "'): ").strip()
    if ruta == "":
        ruta = RUTA_DEFAULT
    guardar_csv(inventario, ruta)


# El menu se repite hasta que el usuario elija salir
ejecutando = True
while ejecutando:
    opcion = mostrar_menu()

    if opcion == "1":
        agregar_producto(inventario)
    elif opcion == "2":
        mostrar_inventario(inventario)
    elif opcion == "3":
        opcion_buscar()
    elif opcion == "4":
        actualizar_producto(inventario)
    elif opcion == "5":
        eliminar_producto(inventario)
    elif opcion == "6":
        calcular_estadisticas(inventario)
    elif opcion == "7":
        opcion_guardar()
    elif opcion == "8":
        gestionar_carga_csv(inventario)
    elif opcion == "9":
        print("\nHasta luego!\n")
        ejecutando = False
    else:
        print("\nOpcion invalida. Ingrese un numero del 1 al 9.\n")
