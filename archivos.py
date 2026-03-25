"""
archivos.py
Modulo con las funciones de persistencia CSV del inventario.
Incluye: crear_archivo_si_no_existe, guardar_csv, cargar_csv, gestionar_carga_csv.
"""

import csv
import os

from sistema import buscar_producto

RUTA_DEFAULT = "inventario.csv"
ENCABEZADO = ["nombre", "precio", "cantidad"]


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
