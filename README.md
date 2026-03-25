# Sistema de Gestion de Inventario

Sistema de consola desarrollado en Python para gestionar productos mediante operaciones CRUD, estadisticas y persistencia de datos en archivos CSV.

---

## Caracteristicas

- Agregar, mostrar, buscar, actualizar y eliminar productos
- Calcular estadisticas del inventario (valor total, producto mas caro, mayor stock)
- Guardar y cargar el inventario desde archivos CSV
- Fusion o reemplazo al cargar un CSV externo
- Validacion de datos en cada entrada del usuario
- Manejo de errores sin cierre inesperado del programa

---

## Estructura del proyecto

```
inventario/
├── main_menu.py          # Menu principal y bucle de ejecucion
├── funciones.py    # Logica CRUD, estadisticas y manejo de CSV
└── inventario.csv  # Archivo de datos (se crea automaticamente)
```

---

## Requisitos

- Python 3.8 o superior
- No requiere librerias externas

---

## Instalacion y uso

```bash
# 1. Clonar el repositorio
git clone https://github.com/usuario/inventario.git

# 2. Entrar a la carpeta
cd inventario

# 3. Ejecutar el programa
python app.py
```

---

## Menu de opciones

```
=============================
  MENU - GESTION INVENTARIO
=============================
1. Agregar producto
2. Mostrar inventario
3. Buscar producto
4. Actualizar producto
5. Eliminar producto
6. Estadisticas
7. Guardar CSV
8. Cargar CSV
9. Salir
```

---

## Formato del archivo CSV

El archivo `inventario.csv` utiliza el siguiente formato:

```
nombre,precio,cantidad
Manzana,1.5,100
Pera,2.0,50
Uva,5.0,10
```

Al cargar un CSV externo el sistema ofrece dos opciones:
- **Sobrescribir**: reemplaza el inventario completo
- **Fusionar**: suma cantidades y actualiza precios de productos existentes

---

## Modulos

| Archivo | Contenido |
|---|---|
| `app.py` | Menu principal, bucle `while` y llamadas a funciones |
| `sistema.py` | CRUD, estadisticas, `guardar_csv`, `cargar_csv`, `gestionar_carga_csv` |
| `archivos.py` | `guardar_csv`, `cargar_csv`, `gestionar_carga_csv` |
---

