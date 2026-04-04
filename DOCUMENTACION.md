# 📚 Documentación - Sistema de Gestión de Biblioteca

## 📋 Índice
1. [Descripción General](#descripción-general)
2. [Estructura del Proyecto](#estructura-del-proyecto)
3. [Requisitos](#requisitos)
4. [Instalación y Configuración](#instalación-y-configuración)
5. [Modelos de Datos](#modelos-de-datos)
6. [Controladores](#controladores)
7. [Configuración de Base de Datos](#configuración-de-base-de-datos)
8. [Vista de Usuario](#vista-de-usuario)
9. [Base de Datos](#base-de-datos)
10. [Ejemplos de Uso](#ejemplos-de-uso)
11. [Estado del Proyecto](#estado-del-proyecto)

---

## 📖 Descripción General

**Proyecto Biblioteca** es una aplicación en **Python** que gestiona un sistema completo de bibliotecas. Permite:

- ✅ Gestionar múltiples bibliotecas
- ✅ Organizar libros por secciones
- ✅ Buscar libros por título, autor, ISBN
- ✅ Administrar secciones de cada biblioteca
- ✅ Consultar información de libros y ubicaciones

El proyecto utiliza una **arquitectura MVC (Model-View-Controller)** con:
- **Base de datos**: MySQL
- **Framework**: Python puro (sin framework web)
- **Dependencias**: `mysql-connector-python`, `python-dotenv`, `prettytable`

---

## 🗂️ Estructura del Proyecto

```
proyectoBiblioteca/
├── main.py                          # Punto de entrada de la aplicación
├── menuView.py                      # Vista principal del menú
├── db.sql                           # Script SQL de la base de datos
├── exa.env                          # Archivo de ejemplo de variables de entorno
├── Config/
│   └── database_config.py           # Configuración de conexión a MySQL
├── Controllers/
│   ├── biblioteca_controller.py     # Controlador de bibliotecas
│   ├── libros_controller.py         # Controlador de libros
│   └── seccion_controller.py        # Controlador de secciones
├── Models/
│   ├── biblioteca.py                # Modelo de Biblioteca
│   ├── libro.py                     # Modelo de Libro
│   └── seccion.py                   # Modelo de Sección
└── View/
    └── menuView.py                  # Vista del menú (copia de menuView.py)
```

---

## 🛠️ Requisitos

- Python 3.8 o superior
- MySQL Server
- pip (gestor de paquetes de Python)

### Dependencias Python

```
mysql-connector-python==8.0.x
python-dotenv==0.x.x
prettytable==3.x.x
```

---

## 🚀 Instalación y Configuración

### 1. Clonar/Descargar el proyecto

```bash
cd proyectoBiblioteca
```

### 2. Crear un entorno virtual (recomendado)

```bash
# En Windows
python -m venv venv
venv\Scripts\activate

# En Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install mysql-connector-python python-dotenv prettytable
```

### 4. Configurar variables de entorno

Crear un archivo `.env` en la raíz del proyecto:

```
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=tu_contraseña
DB_NAME=bibliotecapythonc4
```

### 5. Crear la base de datos

Ejecutar el script SQL `db.sql` en MySQL:

```bash
mysql -u root -p < db.sql
```

O ejecutar manualmente en MySQL Workbench importando el archivo `db.sql`.

### 6. Ejecutar la aplicación

```bash
python main.py
```

---

## 📦 Modelos de Datos

### 1. Biblioteca

**Archivo**: `Models/biblioteca.py`

```python
class Biblioteca:
    def __init__(self, id, nombre, direccion):
        self.id              # ID único de la biblioteca
        self.nombre          # Nombre de la biblioteca
        self.direccion       # Dirección física
```

**Responsabilidad**: Representa una biblioteca física.

---

### 2. Libro

**Archivo**: `Models/libro.py`

```python
class Libro:
    def __init__(self, id, id_seccion, nombre, generos, prologo, isbn, autores, id_biblioteca):
        self.id              # ID único del libro
        self.id_seccion      # ID de la sección donde está
        self.nombre          # Título del libro
        self.generos         # Género(s) literario(s)
        self.prologo         # Sinopsis o prólogo
        self.isbn            # Código ISBN
        self.autores         # Autor(es)
        self.id_biblioteca   # ID de la biblioteca
```

**Responsabilidad**: Representa un libro en el sistema.

---

### 3. Sección

**Archivo**: `Models/seccion.py`

```python
class Seccion:
    def __init__(self, id, id_biblioteca, nombre, piso):
        self.id              # ID único de la sección
        self.id_biblioteca   # ID de la biblioteca a la que pertenece
        self.nombre          # Nombre de la sección (ej: Literatura, Ciencia)
        self.piso            # Piso en el que está ubicada
```

**Responsabilidad**: Representa una sección temática dentro de una biblioteca.

---

## 🎮 Controladores

### 1. BibliotecaController

**Archivo**: `Controllers/biblioteca_controller.py`

#### Métodos

| Método | Descripción | Parámetros | Retorna |
|--------|-------------|-----------|---------|
| `create_bibliteca()` | Crea una nueva biblioteca | `nombre`, `direccion` | JSON con ID de la nueva biblioteca |
| `get_all_bibliotecas()` | Obtiene todas las bibliotecas | - | Lista de objetos `Biblioteca` |

**Ejemplo de uso**:
```python
from Controllers.biblioteca_controller import BibliotecaController

b1 = BibliotecaController()
result = b1.create_bibliteca("GonzalezBook", "Chivolo 13-11 Centro")
# Resultado: {"message": "Biblioteca creada exitosamente.", "id": 1}

bibliotecas = b1.get_all_bibliotecas()
# Resultado: Lista de objetos Biblioteca
```

---

### 2. SeccionController

**Archivo**: `Controllers/seccion_controller.py`

#### Métodos

| Método | Descripción | Parámetros | Retorna |
|--------|-------------|-----------|---------|
| `create_seccion()` | Crea una nueva sección | `id_biblioteca`, `nombre`, `piso` | JSON con ID de la nueva sección |
| `get_all_secciones()` | Obtiene todas las secciones | - | Lista de objetos `Seccion` |
| `get_seccion_by_id()` | Obtiene una sección por ID | `id` | Objeto `Seccion` o error |
| `get_secciones_by_bibliotecas()` | Obtiene secciones de una biblioteca | `id_biblioteca` | Lista de diccionarios con información |
| `update_seccion()` | Actualiza una sección | `nuevo_nombre`, `nuevo_piso`, `id` | Booleano indicando éxito |
| `delete_seccion()` | Elimina una sección | `id` | JSON con estado de la operación |

**Ejemplo de uso**:
```python
from Controllers.seccion_controller import SeccionController

s1 = SeccionController()

# Crear sección
result = s1.create_seccion(7, "Historia Colombiana", 2)

# Obtener secciones de una biblioteca
secciones = s1.get_secciones_by_bibliotecas(1)

# Actualizar sección
s1.update_seccion("Literatura Moderna", 3, 11)

# Eliminar sección
result = s1.delete_seccion(13)
```

---

### 3. LibroController

**Archivo**: `Controllers/libros_controller.py`

#### Métodos

| Método | Descripción | Parámetros | Retorna |
|--------|-------------|-----------|---------|
| `create_libro()` | Crea un nuevo libro | `id_seccion`, `nombre`, `generos`, `prologo`, `isbn`, `autores`, `id_biblioteca` | JSON con ID del nuevo libro |
| `buscar_por_libro()` | Busca libros por título | `titulo_busqueda` | Lista de tuplas con información del libro |
| `buscar_libro_por_isbn()` | Busca un libro por ISBN | `isbn` | Tupla con información del libro |
| `buscar_libro_por_autor()` | Busca libros por autor | `nombre_autor` | Lista de tuplas con información de libros |

**Ejemplo de uso**:
```python
from Controllers.libros_controller import LibroController

l1 = LibroController()

# Crear libro
result = l1.create_libro(1, "Don Quijote", "Clásico", "En un lugar de la Mancha", 
                         "9788491053456", "Miguel de Cervantes", 1)

# Buscar por título
libros = l1.buscar_por_libro("Historia de España")

# Buscar por ISBN
libro = l1.buscar_libro_por_isbn(9788491053456)

# Buscar por autor
libros = l1.buscar_libro_por_autor("Marquez")
```

---

## ⚙️ Configuración de Base de Datos

**Archivo**: `Config/database_config.py`

### Clase DatabaseConfig

Gestiona la conexión a la base de datos MySQL.

#### Métodos

| Método | Descripción |
|--------|-----------|
| `__init__()` | Inicializa con variables de entorno |
| `connect()` | Establece conexión a MySQL |
| `disconnect()` | Cierra la conexión |
| `get_connection()` | Retorna objeto de conexión |
| `execute_query()` | Ejecuta INSERT, UPDATE, DELETE |
| `fetch_all()` | Ejecuta SELECT y retorna todos los resultados |
| `fetch_one()` | Ejecuta SELECT y retorna un resultado |

#### Ejemplo de uso:

```python
from Config.database_config import DatabaseConfig

db = DatabaseConfig()
if db.connect():
    # Ejecutar consulta
    result = db.fetch_all("SELECT * FROM bibliotecas")
    db.disconnect()
```

---

## 💾 Base de Datos

**Archivo**: `db.sql`

### Tablas

#### 1. **bibliotecas**
```sql
CREATE TABLE bibliotecas (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NULL,
    direccion VARCHAR(255) NULL,
    date_create DATETIME DEFAULT CURRENT_TIMESTAMP,
    date_update DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```

#### 2. **secciones**
```sql
CREATE TABLE secciones (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    id_biblioteca INT NOT NULL,
    nombre VARCHAR(255) NOT NULL,
    piso INT NOT NULL,
    date_create DATETIME DEFAULT CURRENT_TIMESTAMP,
    date_update DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY(id_biblioteca) REFERENCES bibliotecas(id)
);
```

#### 3. **libros**
```sql
CREATE TABLE libros (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    id_seccion INT NOT NULL,
    nombre VARCHAR(255) NOT NULL,
    generos VARCHAR(255) NOT NULL,
    prologo VARCHAR(255) NOT NULL,
    isbn VARCHAR(255) NOT NULL,
    autores VARCHAR(255) NOT NULL,
    id_biblioteca INT NOT NULL,
    date_create DATETIME DEFAULT CURRENT_TIMESTAMP,
    date_update DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY(id_seccion) REFERENCES secciones(id),
    FOREIGN KEY(id_biblioteca) REFERENCES bibliotecas(id)
);
```

### Relaciones

```
bibliotecas (1) ──┬──> (N) secciones
                  └──> (N) libros
                  
secciones (1) ──> (N) libros
```

### Datos de Ejemplo

La base de datos incluye:
- **5 bibliotecas** españolas
- **10 secciones** distribuidas en las bibliotecas
- **21 libros** clásicos y de referencia

---

## 👁️ Vista de Usuario

**Archivo**: `menuView.py` / `View/menuView.py`

### Clase MenuView

Presenta un menú interactivo al usuario.

#### Métodos

| Método | Descripción |
|--------|-------------|
| `mostrar_menu()` | Muestra el menú principal en bucle |
| `buscar_por_libro()` | Submenu para buscar libros |

#### Opciones del Menú

```
1. Buscar un libro
2. Ver bibliotecas
0. Salir
```

#### Submenu de Búsqueda

```
=== BUSQUEDA POR LIBRO ===
1. Titulo
2. Genero
3. Autores
4. ISBN
5. Palabra
0. Salir
```

**Nota**: El menú se encuentra en desarrollo. Los botones aún no están completamente implementados.

---

## 📝 Entrada Principal

**Archivo**: `main.py`

El archivo principal actualmente contiene ejemplos de uso de los controladores:

```python
from prettytable import PrettyTable
from Controllers.biblioteca_controller import BibliotecaController
from Controllers.seccion_controller import SeccionController
from Controllers.libros_controller import LibroController

# Instanciar controladores
b1 = BibliotecaController()
s1 = SeccionController()
l1 = LibroController()

# Buscar libro por autor
print(l1.buscar_libro_por_autor("Marquez"))
```

---

## 💡 Ejemplos de Uso

### Ejemplo 1: Crear una Biblioteca

```python
from Controllers.biblioteca_controller import BibliotecaController

b = BibliotecaController()
resultado = b.create_bibliteca("Biblioteca Municipal", "Calle Principal 123")
print(resultado)
# Salida: {"message": "Biblioteca creada exitosamente.", "id": 6}
```

### Ejemplo 2: Obtener todas las Bibliotecas

```python
from Controllers.biblioteca_controller import BibliotecaController
from prettytable import PrettyTable

b = BibliotecaController()
bibliotecas = b.get_all_bibliotecas()

tabla = PrettyTable()
tabla.field_names = ["ID", "Nombre", "Dirección"]
for bib in bibliotecas:
    tabla.add_row([bib.id, bib.nombre, bib.direccion])
print(tabla)
```

### Ejemplo 3: Buscar Libro por Autor

```python
from Controllers.libros_controller import LibroController
from prettytable import PrettyTable

l = LibroController()
libros = l.buscar_libro_por_autor("Marquez")

tabla = PrettyTable()
tabla.field_names = ["Título", "Autores", "Biblioteca", "Sección", "Piso"]
for libro in libros:
    tabla.add_row(libro)
print(tabla)
```

### Ejemplo 4: Obtener Secciones de una Biblioteca

```python
from Controllers.seccion_controller import SeccionController
from prettytable import PrettyTable

s = SeccionController()
secciones = s.get_secciones_by_bibliotecas(1)

tabla = PrettyTable()
tabla.field_names = ["Biblioteca", "Sección", "Piso"]
tabla.title = f"Secciones de Biblioteca ID 1"

for sec in secciones:
    tabla.add_row([sec['nombre_biblioteca'], sec['nombre_seccion'], sec['piso']])
print(tabla)
```

---

## 🔄 Flujo de Operaciones

```
┌─────────────────────────────────────┐
│      USUARIO / APLICACIÓN           │
└────────────┬────────────────────────┘
             │
             ↓
┌─────────────────────────────────────┐
│   VIEW (menuView.py)                │
│   - Interface de usuario            │
└────────────┬────────────────────────┘
             │
             ↓
┌─────────────────────────────────────┐
│   CONTROLLERS                       │
│   - Lógica de negocio               │
│   - BibliotecaController            │
│   - SeccionController               │
│   - LibroController                 │
└────────────┬────────────────────────┘
             │
             ↓
┌─────────────────────────────────────┐
│   MODELS                            │
│   - Representación de datos         │
│   - Biblioteca, Libro, Seccion      │
└────────────┬────────────────────────┘
             │
             ↓
┌─────────────────────────────────────┐
│   DatabaseConfig                    │
│   - Conexión a MySQL                │
│   - Ejecución de queries            │
└────────────┬────────────────────────┘
             │
             ↓
┌─────────────────────────────────────┐
│   MYSQL DATABASE                    │
│   - Almacenamiento de datos         │
└─────────────────────────────────────┘
```

---

## ✅ Estado del Proyecto

### Funcionalidades Implementadas ✓

- ✅ Modelo de datos (Biblioteca, Libro, Sección)
- ✅ Controlador de Bibliotecas (crear, obtener todas)
- ✅ Controlador de Secciones (crear, actualizar, eliminar, obtener)
- ✅ Controlador de Libros (crear, buscar por título, autor, ISBN)
- ✅ Configuración de base de datos
- ✅ Script SQL con datos de ejemplo
- ✅ Conexión a MySQL
- ✅ Manejo de errores básico

### Funcionalidades en Desarrollo 🚧

- 🚧 Menu interactivo completo
- 🚧 Búsqueda por género
- 🚧 Búsqueda por palabra clave
- 🚧 Interfaz gráfica

### Funcionalidades Pendientes 📋

- 📋 Modificar libros (UPDATE)
- 📋 Eliminar libros (DELETE)
- 📋 Filtros avanzados
- 📋 Reportes y estadísticas
- 📋 Autenticación de usuarios
- 📋 API REST (Flask/FastAPI)

---

## 🐛 Manejo de Errores

Todos los controladores incluyen validación de conexión:

```python
if not self.db.connect():
    return {"[ERROR]": "No se pudo conectar a la base de datos"}
```

Los errores se capturan y registran en la consola.

---

## 📞 Notas Adicionales

- Asegúrate de que MySQL esté corriendo antes de ejecutar la aplicación
- Las variables de entorno en `.env` son obligatorias
- Los datos de ejemplo se pueden modificar en `db.sql`
- La aplicación usa `PrettyTable` para formatear salidas de consola

---

## 📚 Referencias

- [MySQL Connector Python](https://dev.mysql.com/doc/connector-python/en/)
- [Python-dotenv](https://github.com/theskumar/python-dotenv)
- [PrettyTable](https://github.com/jazzband/prettytable)

---

**Última actualización**: Abril 2026  
**Versión**: 1.0  
**Autor**: Proyecto Biblioteca

---
