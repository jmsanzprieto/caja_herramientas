# 🐳 FastAPI Dockerizado con SQLite (CRUD de Items)

Este proyecto es un ejemplo práctico y completo de cómo **dockerizar** una aplicación FastAPI que implementa un CRUD (Crear, Leer, Actualizar, Borrar) básico de ítems, utilizando **SQLite** como base de datos. Está diseñado para demostrar cómo empaquetar tu aplicación y su base de datos ligera en contenedores Docker, facilitando el desarrollo, las pruebas y el despliegue.

---

## 🚀 Características

* **Aplicación FastAPI Completa:** Un API RESTful con operaciones CRUD para gestionar ítems.
* **Base de Datos SQLite:** Utiliza SQLite para una configuración de base de datos sencilla y ligera, ideal para desarrollo y ejemplos.
* **SQLAlchemy ORM:** Interactúa con la base de datos de forma robusta y orientada a objetos a través de SQLAlchemy.
* **Pydantic para Validación:** Valida los datos de entrada y salida de la API utilizando esquemas Pydantic.
* **Modularidad:** El código está organizado en módulos (`models.py`, `schemas.py`, `database.py`, `crud.py`) para una mejor separación de responsabilidades.
* **Configuración con `.env`:** La URL de la base de datos se gestiona a través de un archivo de variables de entorno (`.env`).
* **Dockerización con `Dockerfile`:** Define los pasos para construir la imagen Docker de la aplicación.
* **Orquestación con `docker-compose.yml`:** Simplifica el levantamiento y la gestión de la aplicación en un entorno contenedorizado.
* **Persistencia de Datos:** La base de datos SQLite persiste en el sistema de archivos del *host* gracias a los volúmenes de Docker, manteniendo los datos incluso si el contenedor se elimina.

---

## 📂 Estructura del Proyecto

```
.
├── .env                  # Archivo de variables de entorno (p.ej., DATABASE_URL)
├── main.py               # Aplicación FastAPI principal con los endpoints API
├── database.py           # Configuración de SQLAlchemy y gestión de sesiones DB
├── models.py             # Definición de modelos de base de datos (tablas)
├── schemas.py            # Esquemas Pydantic para validación de datos
├── crud.py               # Operaciones CRUD para interactuar con la DB
├── Dockerfile            # Instrucciones para construir la imagen Docker de la app
├── docker-compose.yml    # Configuración para levantar la app en Docker Compose
├── requirements.txt      # Dependencias de Python
└── README.md             # Este mismo archivo
```

---

## 🛠️ Requisitos

* **Python 3.7+**
* **Docker Desktop** (o Docker Engine) instalado y funcionando en tu sistema.

---

## ⚙️ Configuración

1.  **Clona el repositorio** (o crea los archivos si los estás copiando manualmente).

2.  **Crea el archivo `.env`**: En el directorio raíz del proyecto, crea un archivo llamado `.env` y añade la siguiente línea para especificar la ruta de tu base de datos SQLite:

    ```ini
    DATABASE_URL=sqlite:///./sql_app.db
    ```
    
    * `sqlite:///./sql_app.db` indica que la base de datos se creará como un archivo llamado `sql_app.db` en el mismo directorio donde se ejecuta la aplicación (dentro del contenedor, y mapeado al *host*).

---

## 📦 Instalación de Dependencias

Para asegurarte de que Docker pueda construir la imagen correctamente, tu `requirements.txt` debe contener:

```
fastapi
uvicorn
sqlalchemy
python-dotenv
pydantic
```

---

## 🚀 Ejecución de la Aplicación con Docker Compose

Una vez configurado, puedes construir y levantar la aplicación contenedorizada con un solo comando:

1.  Asegúrate de que el **Docker Desktop** (o tu demonio Docker) esté en ejecución.

2.  Abre tu terminal, navega al directorio raíz del proyecto donde se encuentran `Dockerfile` y `docker-compose.yml`.

3.  Ejecuta el siguiente comando para construir la imagen Docker y levantar el contenedor:

    ```bash
    docker-compose up --build
    ```
    
    * `--build`: Fuerza la reconstrucción de la imagen Docker. Esto es necesario la primera vez que ejecutas el comando, o cada vez que realices cambios en el `Dockerfile` o `requirements.txt`.
    * Si la imagen ya está construida y solo quieres iniciar el contenedor: `docker-compose up`

4.  Verás los logs de Uvicorn indicando que la aplicación está corriendo. La base de datos `sql_app.db` se creará automáticamente en el directorio raíz de tu proyecto en el *host*.

---

## 🌐 Endpoints de la API

Una vez que el contenedor esté levantado, la API estará accesible en:

[http://localhost:8000/docs](http://localhost:8000/docs)

Aquí encontrarás la **documentación interactiva de Swagger UI** donde puedes probar todos los *endpoints*:

### `POST /items/`

* **Descripción:** Crea un nuevo ítem en la base de datos.
* **Cuerpo de la solicitud (JSON):**
    ```json
    {
      "name": "Laptop Gaming",
      "description": "Portátil de alto rendimiento para juegos",
      "price": 1500,
      "is_active": true
    }
    ```
* **Códigos de estado:** `201 Created` (éxito), `400 Bad Request` (nombre duplicado, validación fallida).

### `GET /items/`

* **Descripción:** Obtiene una lista de todos los ítems. Soporta paginación básica.
* **Parámetros de consulta:**
    * `skip` (integer, default: `0`): Número de ítems a omitir.
    * `limit` (integer, default: `100`): Número máximo de ítems a devolver.

### `GET /items/{item_id}`

* **Descripción:** Obtiene un ítem específico por su ID.
* **Parámetros de ruta:**
    * `item_id` (integer): El ID del ítem a buscar.
* **Códigos de estado:** `200 OK` (éxito), `404 Not Found` (ítem no encontrado).

### `PUT /items/{item_id}`

* **Descripción:** Actualiza un ítem existente por su ID.
* **Parámetros de ruta:**
    * `item_id` (integer): El ID del ítem a actualizar.
* **Cuerpo de la solicitud (JSON):** Puedes proporcionar solo los campos que quieres actualizar.
    ```json
    {
      "price": 1450,
      "is_active": false
    }
    ```
* **Códigos de estado:** `200 OK` (éxito), `404 Not Found` (ítem no encontrado), `422 Unprocessable Entity` (validación fallida).

### `DELETE /items/{item_id}`

* **Descripción:** Elimina un ítem específico por su ID.
* **Parámetros de ruta:**
    * `item_id` (integer): El ID del ítem a eliminar.
* **Códigos de estado:** `204 No Content` (éxito), `404 Not Found` (ítem no encontrado).

---

## 🛑 Detener y Limpiar Contenedores

Para detener la aplicación y eliminar los contenedores (pero manteniendo la base de datos `sql_app.db` en tu *host*):

```bash
docker-compose down
```

Si deseas eliminar también la imagen Docker y todos los volúmenes asociados (para empezar desde cero, incluyendo la base de datos):

```bash
docker-compose down --volumes --rmi all
```

## 💡 Consideraciones sobre la Dockerización

**Persistencia de Datos:** El `docker-compose.yml` utiliza un volumen de montaje (`.:/app`) que mapea tu directorio local (`.`) al directorio `/app` dentro del contenedor. Esto es crucial para SQLite, ya que el archivo `sql_app.db` se creará y persistirá en tu host, incluso si el contenedor se detiene o se elimina.

**Bases de Datos en Producción:** Para bases de datos más robustas como PostgreSQL o MySQL en producción, generalmente usarías un servicio de base de datos separado en tu `docker-compose.yml` (o un servicio de base de datos gestionado por la nube). En ese caso, la `DATABASE_URL` en tu `.env` cambiaría para apuntar a ese servicio.

**Entorno de Desarrollo vs. Producción:** Este `docker-compose.yml` es ideal para desarrollo. En producción, podrías tener configuraciones más avanzadas, como redes personalizadas, variables de entorno secretas, límites de recursos, etc.

**Imágenes Ligeras:** Se utiliza una imagen base de Python `slim-buster` en el `Dockerfile` para reducir el tamaño final de la imagen, lo que es una buena práctica.