# Sistema de Inventario en Python

Este proyecto es un programa en **Python** que permite gestionar un inventario de productos desde la consola.

El sistema permite **agregar, buscar, actualizar y eliminar productos**, además de **guardar y cargar la información en un archivo CSV**.

---

## Funciones del programa

El programa permite:

1. Agregar productos
2. Mostrar inventario
3. Buscar productos
4. Actualizar productos
5. Eliminar productos
6. Ver estadísticas del inventario
7. Guardar inventario en CSV
8. Cargar inventario desde CSV
9. Salir del programa

---

## Estructura del proyecto

El proyecto tiene dos archivos principales:

```
app.py
funciones.py
```

**app.py**

Contiene el menú principal del programa.

**funciones.py**

Contiene todas las funciones del sistema como:

- agregar productos
- buscar productos
- actualizar productos
- eliminar productos
- calcular estadísticas
- guardar y cargar archivos CSV

---

## Estructura de los productos

Los productos se guardan en una **lista de diccionarios**.

Ejemplo:

```python
producto = {
    "nombre": "Mouse",
    "precio": 25,
    "cantidad": 10
}
```

---

## Archivo CSV

El inventario se puede guardar en un archivo llamado:

```
inventario.csv
```

Formato del archivo:

```
nombre,precio,cantidad
Mouse,25,10
Teclado,45,5
Monitor,300,3
```

---

## Cómo ejecutar el programa

1. Descargar o clonar el repositorio

```
git clone https://github.com/tuusuario/tu-repositorio.git
```

2. Entrar en la carpeta del proyecto

```
cd tu-repositorio
```

3. Ejecutar el programa

```
python app.py
```

---

## Autor

Proyecto realizado como práctica para aprender:

- Python
- estructuras de datos
- manejo de archivos
- lógica de programación
