# 🚀 API de Productos con FastAPI y CRUD Modular

¡Bienvenido a la API de Productos! Esta aplicación es un ejemplo práctico de cómo construir una API RESTful con FastAPI, implementando operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre un conjunto de datos almacenados en un archivo JSON. El diseño se ha enfocado en la modularidad, separando los modelos, los endpoints CRUD y la configuración principal de la aplicación en archivos distintos para una mejor organización y mantenibilidad.

## 🌟 Características Principales

**FastAPI**: Framework web moderno y rápido para construir APIs con Python, basado en estándares abiertos como OpenAPI (anteriormente Swagger) y JSON Schema.

**Pydantic**: Permite la definición de modelos de datos claros y robustos, garantizando la validación y serialización de los datos de las solicitudes y respuestas.

**CRUD Completo**: Implementa los cuatro pilares de las operaciones de base de datos para los productos:

- **Crear (POST)**: Añadir nuevos productos.
- **Leer (GET)**: Obtener todos los productos o uno específico por su ID.
- **Actualizar (PUT)**: Modificar un producto existente.
- **Eliminar (DELETE)**: Borrar un producto.

**Almacenamiento JSON**: Los datos se persisten en un archivo `data.json`, sirviendo como una base de datos simple para este ejemplo.

**Diseño Modular**: Código organizado en módulos lógicos para mayor claridad y facilidad de mantenimiento:

- `main.py`: Punto de entrada de la aplicación FastAPI.
- `crud.py`: Contiene los endpoints y la lógica de negocio para las operaciones CRUD.
- `models.py`: Define los modelos de datos Pydantic.

**Documentación Interactiva**: FastAPI genera automáticamente documentación API interactiva (Swagger UI y ReDoc) para probar los endpoints directamente desde el navegador.

## 📂 Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

```
.
├── main.py
├── crud.py
├── models.py
└── data.json
```

**main.py**:
- Es el punto de entrada de la aplicación.
- Inicializa la aplicación FastAPI.
- Importa el APIRouter definido en `crud.py` y lo monta en la aplicación principal, incluyendo todos los endpoints CRUD.
- Puede contener otros endpoints globales o la configuración de otros módulos de la API.

**crud.py**:
- Define un APIRouter que agrupa todos los endpoints relacionados con las operaciones CRUD para los ítems/productos.
- Incluye las funciones para leer y escribir datos en el archivo `data.json`.
- Contiene la lógica de negocio para cada operación CRUD (create, read, update, delete), manejando la interacción con el archivo JSON y las respuestas HTTP.
- Importa los modelos de datos desde `models.py`.

**models.py**:
- Contiene todas las definiciones de los modelos de datos Pydantic.
- Define la estructura esperada para los datos de los productos, incluyendo:
  - `ItemBase`: Campos base para un producto.
  - `ItemCreate`: Modelo para la creación de nuevos productos.
  - `ItemUpdate`: Modelo para la actualización parcial de productos.
  - `ItemInDB`: Modelo que representa un producto tal como se almacena (incluye el ID generado).
- Asegura la validación y serialización/deserialización automática de los datos de entrada y salida de la API.

**data.json**:
- Un archivo JSON simple que actúa como nuestra "base de datos".
- Almacena una lista de objetos JSON, donde cada objeto representa un producto con su `id`, `name`, `description` y `price`.

## 🛠️ Cómo Configurar y Ejecutar

Sigue estos pasos para poner en marcha la API en tu entorno local.

### 1. Clona el Repositorio (o crea los archivos manualmente)
Asegúrate de tener los archivos `main.py`, `crud.py`, `models.py` y `data.json` en el mismo directorio.

### 2. Crea un Entorno Virtual (Recomendado)
Es una buena práctica aislar las dependencias de tu proyecto.

```bash
python -m venv venv
```

### 3. Activa el Entorno Virtual

**Windows:**
```bash
.\venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 4. Instala las Dependencias
Una vez activado el entorno virtual, instala FastAPI y Uvicorn. Uvicorn es el servidor ASGI que ejecuta la aplicación FastAPI.

```bash
pip install "fastapi[all]" uvicorn
```

### 5. Ejecuta la Aplicación
Desde la raíz del proyecto, ejecuta el siguiente comando:

```bash
uvicorn main:app --reload
```

- `main`: Se refiere al archivo `main.py`.
- `app`: Es el objeto FastAPI dentro de `main.py`.
- `--reload`: Recarga el servidor automáticamente cada vez que detecta cambios en el código (ideal para desarrollo).

Una vez ejecutado, verás un mensaje indicando que el servidor está corriendo, generalmente en `http://127.0.0.1:8000`.

## 📄 Documentación Interactiva de la API

FastAPI genera automáticamente documentación interactiva basada en el estándar OpenAPI.

Abre tu navegador y navega a:

- **Swagger UI**: `http://127.0.0.1:8000/docs`
- **ReDoc**: `http://127.0.0.1:8000/redoc`

Aquí podrás ver todos los endpoints disponibles, sus parámetros de entrada y salida, y probarlos directamente desde la interfaz. Observa cómo los endpoints para los productos están agrupados bajo el prefijo `/items` y el tag "Items CRUD", gracias a la configuración del APIRouter.

## 🚀 Endpoints de la API

Todos los endpoints CRUD de productos están prefijados con `/items`.

### 1. Crear un Nuevo Producto (POST)

- **URL**: `/items/`
- **Método**: `POST`
- **Cuerpo de la Solicitud (JSON)**:

```json
{
  "name": "Nuevo Producto",
  "description": "Una breve descripción del nuevo producto.",
  "price": 19.99
}
```

- **Respuesta Exitosa (201 Created)**:

```json
{
  "id": "generado-uuid-unico",
  "name": "Nuevo Producto",
  "description": "Una breve descripción del nuevo producto.",
  "price": 19.99
}
```

### 2. Obtener Todos los Productos (GET)

- **URL**: `/items/`
- **Método**: `GET`
- **Respuesta Exitosa (200 OK)**:

```json
[
  {
    "id": "a1b2c3d4",
    "name": "Producto A",
    "description": "Descripción del Producto A",
    "price": 10.99
  },
  {
    "id": "e5f6g7h8",
    "name": "Producto B",
    "description": "Descripción del Producto B",
    "price": 25.50
  }
]
```

### 3. Obtener un Producto por ID (GET)

- **URL**: `/items/{item_id}`
- **Método**: `GET`
- **Ejemplo**: `/items/a1b2c3d4`
- **Respuesta Exitosa (200 OK)**:

```json
{
  "id": "a1b2c3d4",
  "name": "Producto A",
  "description": "Descripción del Producto A",
  "price": 10.99
}
```

- **Respuesta de Error (404 Not Found)**:

```json
{
  "detail": "Artículo no encontrado"
}
```

### 4. Actualizar un Producto (PUT)

- **URL**: `/items/{item_id}`
- **Método**: `PUT`
- **Ejemplo**: `/items/a1b2c3d4`
- **Cuerpo de la Solicitud (JSON)**: (Puedes enviar solo los campos que deseas actualizar)

```json
{
  "name": "Producto A Actualizado",
  "price": 12.50
}
```

- **Respuesta Exitosa (200 OK)**:

```json
{
  "id": "a1b2c3d4",
  "name": "Producto A Actualizado",
  "description": "Descripción del Producto A",
  "price": 12.50
}
```

- **Respuesta de Error (404 Not Found)**:

```json
{
  "detail": "Artículo no encontrado"
}
```

### 5. Eliminar un Producto (DELETE)

- **URL**: `/items/{item_id}`
- **Método**: `DELETE`
- **Ejemplo**: `/items/e5f6g7h8`
- **Respuesta Exitosa (204 No Content)**: No devuelve contenido en el cuerpo de la respuesta.
- **Respuesta de Error (404 Not Found)**:

```json
{
  "detail": "Artículo no encontrado"
}
```

## 💡 Próximos Pasos (Ideas de Mejora)

- **Base de Datos Real**: Para una aplicación de producción, se recomienda reemplazar el archivo JSON por una base de datos más robusta (ej. PostgreSQL con SQLAlchemy/Alembic, MongoDB, SQLite).

- **Manejo de Errores Mejorado**: Implementar un manejo de excepciones más granular y respuestas de error personalizadas.

- **Autenticación y Autorización**: Añadir mecanismos de seguridad para proteger los endpoints de la API.

- **Validación de Datos Avanzada**: Explorar más funcionalidades de Pydantic para validaciones complejas.

- **Pruebas Unitarias/Integración**: Escribir tests para asegurar la funcionalidad de los endpoints.

- **Contenedorización**: Empaquetar la aplicación en un contenedor Docker para facilitar el despliegue.