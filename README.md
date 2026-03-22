# 📦 Sistema de Gestión de Inventario en Python

Este proyecto es un **sistema de gestión de inventario desarrollado en Python** que permite administrar productos desde la consola.  
El programa utiliza **listas de diccionarios** para almacenar los datos en memoria y permite **guardar y cargar información desde archivos CSV**.

---

# 🚀 Características

El sistema permite realizar las siguientes operaciones:

- ➕ Agregar productos
- 📋 Mostrar inventario
- 🔍 Buscar productos
- ✏️ Actualizar productos
- ❌ Eliminar productos
- 📊 Calcular estadísticas del inventario
- 💾 Guardar inventario en CSV
- 📂 Cargar inventario desde CSV

---

# 🧠 Estructura del Proyecto

El proyecto está dividido en dos archivos principales:

```
inventario-python/
│
├── main_menu.py
├── funciones.py
├── inventario.csv
└── README.md
```

### 📄 `main_menu.py`

Contiene:

- El **menú principal**
- El **flujo de ejecución del programa**
- La conexión con las funciones del sistema

El menú se repite hasta que el usuario elige **salir**.

---

### 📄 `funciones.py`

Contiene todas las funciones del sistema:

- CRUD de productos
- Cálculo de estadísticas
- Lectura y escritura de archivos CSV
- Validación de datos

---

# 📦 Estructura de los Productos

Cada producto se almacena como un **diccionario** dentro de una lista:

```python
producto = {
    "nombre": "Laptop",
    "precio": 2500,
    "cantidad": 10
}
```

El inventario completo se maneja como:

```python
inventario = []
```

---

# 📊 Estadísticas del Inventario

El sistema calcula automáticamente:

- 📦 Tipos de productos registrados
- 🔢 Unidades totales en inventario
- 💰 Valor total del inventario
- 🏷 Producto más caro
- 📈 Producto con mayor stock

---

# 💾 Manejo de Archivos CSV

El sistema guarda los productos en un archivo:

```
inventario.csv
```

Formato del archivo:

```
nombre,precio,cantidad
Laptop,2500,10
Mouse,25,40
Teclado,45,20
```

Funciones implementadas:

- Guardar inventario
- Cargar inventario
- Fusionar datos
- Sobrescribir inventario

---

# 📋 Menú del Programa

Cuando se ejecuta el programa se muestra el siguiente menú:

```
MENU - GESTION INVENTARIO

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

# ▶️ Cómo Ejecutar el Proyecto

1️⃣ Clonar el repositorio

```bash
git clone https://github.com/tuusuario/inventario-python.git
```

2️⃣ Entrar en la carpeta del proyecto

```bash
cd inventario-python
```

3️⃣ Ejecutar el programa

```bash
python main_menu.py
```

---

# 🛠 Tecnologías Utilizadas

- Python
- Listas
- Diccionarios
- Ciclos
- Condicionales
- Manejo de archivos
- Módulo `csv`

---

# 📚 Conceptos de Programación Aplicados

Este proyecto utiliza varios conceptos fundamentales de programación:

- Programación modular
- Estructuras de datos
- Validación de datos
- Manejo de excepciones
- Persistencia de datos
- Diseño de menús interactivos

---

# 📈 Posibles Mejoras

- Interfaz gráfica (Tkinter o PyQt)
- Base de datos (SQLite o MySQL)
- Exportación a Excel
- Sistema de categorías
- Control de usuarios

---

# 👨‍💻 Autor

Proyecto desarrollado como práctica de **programación en Python** para aprender:

- estructuras de datos
- lógica de programación
- manejo de archivos
