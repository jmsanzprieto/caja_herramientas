# 🏷️ API de Items con Paginación y Filtrado (FastAPI)

Este proyecto es un ejemplo práctico de cómo implementar una API RESTful con funcionalidades de **paginación** y **filtrado** en FastAPI. Los datos se cargan desde un archivo JSON local, y la configuración del archivo de datos se gestiona a través de variables de entorno para mayor flexibilidad.

---

## 🚀 Características

* **Paginación (`skip` y `limit`):** Controla el número de ítems devueltos y el punto de inicio de la lista.
* **Filtrado por Campos:** Permite filtrar ítems por `category`, `status`, `min_price` y `max_price`.
* **Fuente de Datos JSON:** Utiliza un archivo JSON simple como nuestra "base de datos" para este ejemplo.
* **Modularidad:** La lógica de datos está separada de la capa de la API (`data_manager.py`), promoviendo un código más limpio.
* **Configuración Flexible:** La ruta del archivo de datos se especifica en un archivo `.env`, facilitando los cambios de entorno.
* **Validación de Parámetros:** Usa los `Query` de FastAPI para validar y documentar los parámetros de consulta de la URL.
* **Documentación Automática:** FastAPI genera automáticamente una documentación interactiva de la API (Swagger UI / ReDoc).

---

## 📂 Estructura del Proyecto

```
.
├── .env                # Variables de entorno (p.ej., la ruta al archivo de datos)
├── main.py             # Define la aplicación FastAPI y las rutas
├── data_manager.py     # Contiene la lógica para cargar y manipular los datos (filtrado, paginación)
├── data/               # Directorio para los archivos de datos
│   └── items.json      # Nuestro "base de datos" de ítems
├── requirements.txt    # Dependencias del proyecto
└── README.md           # Este mismo archivo
```

---

## 🛠️ Requisitos

* Python 3.7+

---

## ⚙️ Configuración

1.  **Clona el repositorio** (o crea los archivos si los estás copiando manualmente).

2.  **Crea el directorio `data/`**:

    ```bash
    mkdir data
    ```

3.  **Crea el archivo `data/items.json`**: Copia el siguiente contenido JSON y guárdalo en `data/items.json`.

    ```json
    [
      {
        "id": 1,
        "name": "Laptop Pro",
        "category": "Electronics",
        "status": "available",
        "price": 1200.00
      },
      {
        "id": 2,
        "name": "Mechanical Keyboard",
        "category": "Electronics",
        "status": "available",
        "price": 95.50
      },
      {
        "id": 3,
        "name": "Wireless Mouse",
        "category": "Electronics",
        "status": "low_stock",
        "price": 30.00
      },
      {
        "id": 4,
        "name": "Python Book",
        "category": "Books",
        "status": "available",
        "price": 45.99
      },
      {
        "id": 5,
        "name": "Data Science Guide",
        "category": "Books",
        "status": "out_of_stock",
        "price": 60.00
      },
      {
        "id": 6,
        "name": "Smartwatch X",
        "category": "Wearables",
        "status": "available",
        "price": 250.00
      },
      {
        "id": 7,
        "name": "Fitness Tracker",
        "category": "Wearables",
        "status": "available",
        "price": 75.00
      },
      {
        "id": 8,
        "name": "SQL Handbook",
        "category": "Books",
        "status": "available",
        "price": 35.00
      },
      {
        "id": 9,
        "name": "Webcam HD",
        "category": "Electronics",
        "status": "available",
        "price": 50.00
      },
      {
        "id": 10,
        "name": "External SSD",
        "category": "Electronics",
        "status": "low_stock",
        "price": 150.00
      },
      {
        "id": 11,
        "name": "Fiction Novel",
        "category": "Books",
        "status": "available",
        "price": 20.00
      }
    ]
    ```

4.  **Crea el archivo `.env`**: En el directorio raíz del proyecto, crea un archivo llamado `.env` y añade la siguiente línea para especificar la ruta del archivo de datos:

    ```ini
    ITEMS_DATA_PATH=./data/items.json
    ```

---

## 📦 Instalación de Dependencias

Instala las librerías necesarias utilizando `pip`:

```bash
pip install -r requirements.txt
```

El archivo `requirements.txt` debería contener:

```
fastapi
uvicorn
python-dotenv
pydantic
```

## 🚀 Ejecución de la Aplicación

Una vez configurado, puedes iniciar la aplicación usando uvicorn:

```bash
uvicorn main:app --reload
```

- `main`: Se refiere al archivo `main.py`.
- `app`: Es la instancia de FastAPI dentro de `main.py`.
- `--reload`: Reinicia el servidor automáticamente cuando detecta cambios en el código (útil para desarrollo).

## 🌐 Endpoints de la API

Una vez que la aplicación esté en funcionamiento, puedes acceder a la documentación interactiva de la API (Swagger UI) en:

```
http://127.0.0.1:8000/docs
```

O la documentación alternativa (ReDoc) en:

```
http://127.0.0.1:8000/redoc
```

### GET /items/

Este endpoint devuelve una lista paginada y filtrada de ítems.

**Parámetros de consulta (Query Parameters):**

- `skip` (integer, default: 0, minimum: 0): Número de ítems a omitir (offset).
- `limit` (integer, default: 10, minimum: 1, maximum: 100): Número máximo de ítems a devolver por página.
- `category` (string, optional): Filtra los ítems por su categoría (ej. Electronics, Books, Wearables).
- `status` (string, optional): Filtra los ítems por su estado (ej. available, low_stock, out_of_stock).
- `min_price` (float, optional, minimum: 0): Filtra los ítems con un precio igual o superior a este valor.
- `max_price` (float, optional, minimum: 0): Filtra los ítems con un precio igual o inferior a este valor.

**Ejemplos de Uso:**

- **Todos los ítems (primera página, 10 ítems):**
  ```
  http://127.0.0.1:8000/items/
  ```

- **Paginación (segunda página, 5 ítems por página):**
  ```
  http://127.0.0.1:8000/items/?skip=5&limit=5
  ```

- **Filtrar por categoría 'Electronics':**
  ```
  http://127.0.0.1:8000/items/?category=Electronics
  ```

- **Filtrar por estado 'available' y límite de 3 ítems:**
  ```
  http://127.0.0.1:8000/items/?status=available&limit=3
  ```

- **Combinar filtros y paginación (libros disponibles, segunda página):**
  ```
  http://127.0.0.1:8000/items/?category=Books&status=available&skip=1&limit=2
  ```

- **Filtrar por rango de precios:**
  ```
  http://127.0.0.1:8000/items/?min_price=50&max_price=100
  ```

### GET /items/count/

Este endpoint devuelve el número total de ítems después de aplicar los filtros, sin considerar la paginación. Esto es útil para los frontends para calcular el número total de páginas.

**Parámetros de consulta (Query Parameters):**

Los mismos parámetros de filtrado que `/items/`.

**Ejemplo de Uso:**

- **Total de ítems disponibles:**
  ```
  http://127.0.0.1:8000/items/count/?status=available
  ```

- **Total de libros en stock:**
  ```
  http://127.0.0.1:8000/items/count/?category=Books&status=available
  ```

## 💡 Consideraciones Adicionales

**Optimización de Datos:** Para aplicaciones con grandes volúmenes de datos, cargar todo el archivo JSON en memoria (`_all_items`) no es eficiente. En un entorno de producción, esta lógica de `data_manager.py` sería reemplazada por consultas directas a una base de datos real (SQL, NoSQL), donde la paginación y el filtrado se realizarían a nivel de la base de datos para un rendimiento óptimo.

**Seguridad:** Este ejemplo se enfoca en la paginación y el filtrado. Para una aplicación de producción, considera implementar autenticación, autorización y validación de entrada más robusta.

**Manejo de Errores:** Se incluye un manejo básico de errores con `HTTPException`. Puedes personalizar aún más las respuestas de error para una mejor experiencia del usuario.