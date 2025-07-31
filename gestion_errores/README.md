# 🚫 Manejo de Errores Personalizado en FastAPI

Este proyecto es un ejemplo práctico y modular de cómo implementar un manejo de errores personalizado en FastAPI. Demuestra cómo interceptar y transformar las respuestas de errores HTTP estándar, así como la creación y gestión de excepciones de negocio propias para una API más robusta e informativa.

## 🚀 Características

- **Manejo de HTTPException**: Personaliza las respuestas para errores HTTP comunes (400, 404, 403, etc.) lanzados por FastAPI o explícitamente en tu código.
- **Excepciones de Negocio Personalizadas**: Define tus propias clases de excepción para escenarios específicos de tu lógica de negocio (por ejemplo, `ItemNotFoundException`, `UnauthorizedAccessException`, `InvalidInputException`).
- **Manejadores de Excepciones Centralizados**: Registra manejadores globales en la aplicación FastAPI para capturar estas excepciones y devolver respuestas JSON consistentes y descriptivas.
- **Separación de Responsabilidades**: La lógica de manejo de errores (`errors.py`) y la lógica de negocio (`services.py`) están claramente separadas de la capa de la API (`main.py`).
- **Mensajes de Error Informativos**: Las respuestas de error personalizadas incluyen detalles útiles para el cliente, como códigos de estado, mensajes descriptivos y tipos de error específicos.
- **Documentación Automática**: FastAPI integra la personalización de errores en su documentación de API (Swagger UI / ReDoc).

## 📂 Estructura del Proyecto

```
.
├── main.py             # Define la aplicación FastAPI, rutas y registra los manejadores de excepciones.
├── errors.py           # Contiene las definiciones de excepciones personalizadas y los handlers para ellas.
├── services.py         # Contiene la lógica de negocio que puede lanzar excepciones.
└── README.md           # Este mismo archivo.
```

## 🛠️ Requisitos

- Python 3.7+

## 📦 Instalación de Dependencias

Instala las librerías necesarias utilizando pip:

```bash
pip install "fastapi[all]" uvicorn
```

## 🚀 Ejecución de la Aplicación

Una vez que tengas los archivos en su lugar, puedes iniciar la aplicación usando uvicorn:

```bash
uvicorn main:app --reload
```

- `main`: Se refiere al archivo `main.py`.
- `app`: Es la instancia de FastAPI dentro de `main.py`.
- `--reload`: Reinicia el servidor automáticamente cuando detecta cambios en el código (útil para desarrollo).

## 🌐 Endpoints de la API y Ejemplos de Errores

Una vez que la aplicación esté en funcionamiento, puedes acceder a la documentación interactiva de la API (Swagger UI) en:

```
http://127.0.0.1:8000/docs
```

Aquí puedes probar los diferentes endpoints para ver cómo se manejan las excepciones.

### GET /items/{item_id}

Este endpoint intenta obtener un ítem por su ID.

**Éxito:**
- `GET /items/1`
- `GET /items/2`

**Error (ItemNotFoundException - 404 Not Found):**
- `GET /items/999` (ID no existente)

**Respuesta esperada (ejemplo):**

```json
{
  "message": "Ítem con ID '999' no encontrado.",
  "item_id": 999,
  "code": 404,
  "error_type": "ITEM_NOT_FOUND"
}
```

### POST /items/

Este endpoint permite crear un nuevo ítem, simulando escenarios de autorización y validación.

**Éxito:**
- Método: `POST`
- Cuerpo (JSON): `{"name": "Mi Nuevo Producto"}`
- Parámetro de consulta `user_role`: `admin` o `editor`

**Error (UnauthorizedAccessException - 403 Forbidden):**
- Método: `POST`
- Cuerpo (JSON): `{"name": "Mi Nuevo Producto"}`
- Parámetro de consulta `user_role`: `guest`

**Respuesta esperada (ejemplo):**

```json
{
  "message": "Acceso no autorizado. Se requiere el rol 'admin o editor'.",
  "required_role": "admin o editor",
  "code": 403,
  "error_type": "UNAUTHORIZED_ACCESS"
}
```

**Error (InvalidInputException - 400 Bad Request):**
- Método: `POST`
- Cuerpo (JSON): `{"name": "ab"}` (nombre demasiado corto) o `{"invalid_field": "test"}` (campo incorrecto)
- Parámetro de consulta `user_role`: `admin`

**Respuesta esperada (ejemplo):**

```json
{
  "message": "Entrada inválida para 'name': 'ab'. Razón: El nombre debe ser una cadena de al menos 3 caracteres.",
  "field": "name",
  "received_value": "ab",
  "reason": "El nombre debe ser una cadena de al menos 3 caracteres.",
  "code": 400,
  "error_type": "INVALID_INPUT"
}
```

### DELETE /items/{item_id}

Este endpoint elimina un ítem, requiriendo un rol de administrador.

**Éxito:**
- `DELETE /items/1?user_role=admin`

**Error (UnauthorizedAccessException - 403 Forbidden):**
- `DELETE /items/2?user_role=guest`

**Error (ItemNotFoundException - 404 Not Found):**
- `DELETE /items/999?user_role=admin`

### GET /force-404/ y GET /force-400/

Estos endpoints son solo para demostración, y forzarán un `HTTPException` estándar para que puedas ver cómo el manejador global de `HTTPException` lo procesa.

- `GET /force-404/`
- `GET /force-400/`

**Respuesta esperada (ejemplo para 404):**

```json
{
  "detail": "Este recurso fue forzado a no ser encontrado.",
  "code": 404,
  "error_type": "HTTP_ERROR"
}
```

## 💡 ¿Cómo funciona la personalización?

FastAPI utiliza el método `app.add_exception_handler()` para registrar funciones que se ejecutarán cuando se lance una excepción específica.

### Excepciones HTTP Estándar (HTTPException)

Aunque FastAPI ya las maneja, registrando un `http_exception_handler` para `HTTPException`, podemos sobrescribir el formato de respuesta por defecto con uno más consistente con nuestras excepciones personalizadas.

### Excepciones Personalizadas

**Definición:** Nuestras excepciones (`ItemNotFoundException`, `UnauthorizedAccessException`, `InvalidInputException`) heredan de `HTTPException`. Esto es clave porque ya llevan un `status_code` asociado y un `detail` (mensaje).

**Manejadores Específicos:** Cada excepción personalizada tiene su propio manejador (`item_not_found_exception_handler`, etc.) registrado en `main.py`. Esto nos permite personalizar la respuesta JSON, añadiendo campos adicionales específicos para ese tipo de error (p.ej., `item_id`, `required_role`, `field`, `reason`).