"""
funciones.py
Modulo con todas las funciones del sistema de gestion de inventario.
Incluye: CRUD, estadisticas y lectura/escritura CSV.
"""

import csv
import os

RUTA_DEFAULT = "inventario.csv"
ENCABEZADO = ["nombre", "precio", "cantidad"]


# Pide un numero decimal valido al usuario
def pedir_precio(prompt="Precio del producto: "):
    precio_valido = False
    while not precio_valido:
        try:
            precio = float(input(prompt))
            if precio < 0:
                print("El precio no puede ser negativo.")
            else:
                precio_valido = True
        except ValueError:
            print("Valor invalido. Ingrese un numero.")
    return precio


# Pide un numero entero valido al usuario
def pedir_cantidad(prompt="Cantidad del producto: "):
    cantidad_valida = False
    while not cantidad_valida:
        try:
            cantidad = int(input(prompt))
            if cantidad < 0:
                print("La cantidad no puede ser negativa.")
            else:
                cantidad_valida = True
        except ValueError:
            print("Valor invalido. Ingrese un numero entero.")
    return cantidad


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
            precio = pedir_precio()
            cantidad = pedir_cantidad()
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
        producto["precio"] = pedir_precio("Nuevo precio: ")

    resp = input("Actualizar cantidad? (si/no): ").strip().lower()
    if resp == "si":
        producto["cantidad"] = pedir_cantidad("Nueva cantidad: ")

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


# Crea el archivo CSV con encabezado si no existe
def crear_archivo_si_no_existe(ruta):
    if not os.path.exists(ruta):
        try:
            archivo = open(ruta, "w", newline="", encoding="utf-8")
            writer = csv.writer(archivo)
            writer.writerow(ENCABEZADO)
            archivo.close()
            print("Archivo '" + ruta + "' creado automaticamente.")
        except OSError as e:
            print("No se pudo crear el archivo: " + str(e))


# Guarda el inventario en un archivo CSV
def guardar_csv(inventario, ruta=RUTA_DEFAULT):
    if len(inventario) == 0:
        print("El inventario esta vacio. No hay datos para guardar.\n")
        return

    try:
        archivo = open(ruta, "w", newline="", encoding="utf-8")
        writer = csv.DictWriter(archivo, fieldnames=ENCABEZADO)
        writer.writeheader()
        writer.writerows(inventario)
        archivo.close()
        print("Inventario guardado en: " + ruta + "\n")
    except PermissionError:
        print("Sin permisos para escribir en '" + ruta + "'.\n")
    except OSError as e:
        print("Error al guardar el archivo: " + str(e) + "\n")


# Carga productos desde un archivo CSV y los retorna como lista
def cargar_csv(ruta=RUTA_DEFAULT):
    # Si el archivo no existe lo crea vacio y avisa
    if not os.path.exists(ruta):
        print("El archivo '" + ruta + "' no existe. Se creara uno vacio.")
        crear_archivo_si_no_existe(ruta)
        return []

    productos = []
    filas_invalidas = 0

    try:
        archivo = open(ruta, "r", newline="", encoding="utf-8")
        reader = csv.DictReader(archivo)

        # Validar encabezado
        if reader.fieldnames is None or list(reader.fieldnames) != ENCABEZADO:
            print("El archivo no tiene el encabezado correcto (nombre,precio,cantidad).\n")
            archivo.close()
            return None

        numero_fila = 2  # la fila 1 es el encabezado
        for fila in reader:
            try:
                precio = float(fila["precio"])
                cantidad = int(fila["cantidad"])
                nombre = fila["nombre"].strip()
                if precio < 0 or cantidad < 0 or nombre == "":
                    raise ValueError("Datos invalidos")
                productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
            except (ValueError, KeyError):
                print("Fila " + str(numero_fila) + " invalida, omitida.")
                filas_invalidas += 1
            numero_fila += 1

        archivo.close()

    except FileNotFoundError:
        print("Archivo no encontrado: " + ruta + "\n")
        return None
    except UnicodeDecodeError:
        print("El archivo tiene un formato de texto no soportado.\n")
        return None
    except OSError as e:
        print("Error al leer el archivo: " + str(e) + "\n")
        return None

    if filas_invalidas > 0:
        print(str(filas_invalidas) + " fila(s) invalida(s) omitida(s).")

    return productos


# Flujo completo de carga: pide ruta, carga y pregunta como integrar los datos
def gestionar_carga_csv(inventario):
    ruta = input("Ruta del archivo CSV (Enter para '" + RUTA_DEFAULT + "'): ").strip()
    if ruta == "":
        ruta = RUTA_DEFAULT

    nuevos = cargar_csv(ruta)

    if nuevos is None:
        print("No se realizaron cambios en el inventario.\n")
        return
    if len(nuevos) == 0:
        print("El archivo no contiene productos validos.\n")
        return

    respuesta = input("Sobrescribir inventario actual? (S/N): ").strip().upper()

    if respuesta == "S":
        # Borra todo y reemplaza
        inventario.clear()
        for producto in nuevos:
            inventario.append(producto)
        print("Inventario reemplazado con " + str(len(nuevos)) + " producto(s).\n")
    else:
        # Fusion: si el nombre ya existe suma cantidad y actualiza precio
        print("Politica de fusion: se suman cantidades y se actualiza el precio.")
        agregados = 0
        fusionados = 0
        for nuevo in nuevos:
            existente = buscar_producto(inventario, nuevo["nombre"])
            if existente is not None:
                existente["cantidad"] += nuevo["cantidad"]
                existente["precio"] = nuevo["precio"]
                fusionados += 1
            else:
                inventario.append(nuevo)
                agregados += 1
        print(str(agregados) + " producto(s) nuevo(s), " +
              str(fusionados) + " producto(s) actualizado(s).\n")
