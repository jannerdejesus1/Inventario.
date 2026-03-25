"""
sistema.py
Modulo con las funciones CRUD y estadisticas del inventario.
"""

import csv
import os


RUTA_DEFAULT = "inventario.csv"
ENCABEZADO = ["nombre", "precio", "cantidad"]


# Pide un valor numerico valido al usuario
# tipo indica el tipo esperado: float para precio, int para cantidad
def pedir_valor(prompt, tipo):
    valor_valido = False
    while not valor_valido:
        try:
            if tipo == float:
                valor = float(input(prompt))
            else:
                valor = int(input(prompt))
            if valor < 0:
                print("El valor no puede ser negativo.")
            else:
                valor_valido = True
        except ValueError:
            if tipo == float:
                print("Valor invalido. Ingrese un numero decimal.")
            else:
                print("Valor invalido. Ingrese un numero entero.")
    return valor


# Agrega uno o varios productos al inventario
def agregar_producto(inventario):
    continuar = "si"
    while continuar.lower() == "si":
        nombre = input("Nombre del producto: ").strip()
        if nombre == "":
            print("El nombre no puede estar vacio.")
            continue

        if buscar_producto(inventario, nombre) is not None:
            print("El producto '" + nombre + "' ya existe. Use Actualizar para modificarlo.")
        else:
            precio = pedir_valor("Precio del producto: ", float)
            cantidad = pedir_valor("Cantidad del producto: ", int)
            producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
            inventario.append(producto)
            print("Producto '" + nombre + "' agregado.")

        continuar = input("Desea agregar otro producto? (si/no): ").strip()

    print("Saliendo del ingreso de productos.\n")


# Muestra todos los productos del inventario
def mostrar_inventario(inventario):
    print("\n--- Inventario ---")
    if len(inventario) == 0:
        print("El inventario esta vacio.\n")
    else:
        for producto in inventario:
            print("Producto: " + producto["nombre"] +
                  " | Precio: " + str(producto["precio"]) +
                  " | Cantidad: " + str(producto["cantidad"]))
        print()


# Busca un producto por nombre y retorna el diccionario o None si no existe
def buscar_producto(inventario, nombre):
    for producto in inventario:
        if producto["nombre"].lower() == nombre.strip().lower():
            return producto
    return None


# Actualiza el precio y/o cantidad de un producto existente
def actualizar_producto(inventario):
    nombre = input("Nombre del producto a actualizar: ").strip()
    producto = buscar_producto(inventario, nombre)

    if producto is None:
        print("Producto '" + nombre + "' no encontrado.\n")
        return

    print("Valores actuales - Precio: " + str(producto["precio"]) +
          " | Cantidad: " + str(producto["cantidad"]))

    resp = input("Actualizar precio? (si/no): ").strip().lower()
    if resp == "si":
        producto["precio"] = pedir_valor("Nuevo precio: ", float)

    resp = input("Actualizar cantidad? (si/no): ").strip().lower()
    if resp == "si":
        producto["cantidad"] = pedir_valor("Nueva cantidad: ", int)

    print("Producto '" + nombre + "' actualizado.\n")


# Elimina un producto del inventario pidiendo confirmacion
def eliminar_producto(inventario):
    nombre = input("Nombre del producto a eliminar: ").strip()
    producto = buscar_producto(inventario, nombre)

    if producto is None:
        print("Producto '" + nombre + "' no encontrado.\n")
        return

    confirmacion = input("Esta seguro de eliminar '" + nombre + "'? (si/no): ").strip().lower()
    if confirmacion == "si":
        inventario.remove(producto)
        print("Producto '" + nombre + "' eliminado.\n")
    else:
        print("Operacion cancelada.\n")


# Calcula y muestra estadisticas del inventario
def calcular_estadisticas(inventario):
    print("\n--- Estadisticas ---")
    if len(inventario) == 0:
        print("No hay productos registrados.\n")
        return

    # Lambda para calcular el subtotal de un producto
    subtotal = lambda p: p["precio"] * p["cantidad"]

    unidades_totales = 0
    valor_total = 0
    for producto in inventario:
        unidades_totales += producto["cantidad"]
        valor_total += subtotal(producto)

    producto_mas_caro = inventario[0]
    producto_mayor_stock = inventario[0]
    for producto in inventario:
        if producto["precio"] > producto_mas_caro["precio"]:
            producto_mas_caro = producto
        if producto["cantidad"] > producto_mayor_stock["cantidad"]:
            producto_mayor_stock = producto

    print("Unidades totales: " + str(unidades_totales))
    print("Valor total del inventario: " + str(round(valor_total, 2)))
    print("Producto mas caro: " + producto_mas_caro["nombre"] +
          " ($" + str(producto_mas_caro["precio"]) + ")")
    print("Producto con mayor stock: " + producto_mayor_stock["nombre"] +
          " (" + str(producto_mayor_stock["cantidad"]) + " unidades)")
    print()
