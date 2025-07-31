# 🚀 FastAPI Toolbox: Una Colección de Microproyectos Esenciales

¡Bienvenido a la **Caja de Herramientas de FastAPI**! Este repositorio es una colección de microproyectos independientes, cada uno diseñado para ilustrar una funcionalidad clave y común en el desarrollo de APIs con FastAPI. El objetivo es proporcionar ejemplos claros, modulares y listos para usar que te ayuden a construir aplicaciones robustas y eficientes.

Cada microproyecto es un caso de uso práctico, desarrollado con buenas prácticas como la separación de la lógica, la gestión de configuraciones a través de variables de entorno (`.env`), y la claridad en el código.

---

## 📂 Microproyectos Incluidos

Aquí tienes un resumen de cada una de las herramientas que encontrarás en esta colección:

---

### 🔐 1. Autenticación y Autorización (Login Básico)

Este microproyecto implementa un sistema básico de inicio de sesión con FastAPI. Ideal para entender cómo proteger tus *endpoints* y gestionar el acceso de usuarios.

* **Características Principales:**
    * Gestión de usuarios y un sistema de login.
    * Generación y validación de tokens JWT (JSON Web Tokens).
    * Protección de rutas (solo usuarios autenticados pueden acceder).
    * Modularidad en el código.
* **Ir al proyecto:** [login/README.md](https://github.com/jmsanzprieto/caja_herramientas/blob/main/login/README.md)

---

### 📝 2. CRUD (Crear, Leer, Actualizar, Borrar)

Un ejemplo fundamental de cómo construir una API RESTful completa con las operaciones básicas para un recurso, utilizando SQLAlchemy para la interacción con la base de datos.

* **Características Principales:**
    * Implementación de las operaciones CRUD (Create, Read, Update, Delete).
    * Uso de **SQLAlchemy ORM** para la interacción con la base de datos.
    * **Pydantic** para la validación de modelos de datos (esquemas de entrada y salida).
    * Estructura modular y limpia.
* **Ir al proyecto:** [crud/README.md](https://github.com/jmsanzprieto/caja_herramientas/blob/main/crud/README.md)

---

### 📁 3. Gestión de Archivos (Subida y Descarga)

Casi cualquier aplicación necesita manejar archivos. Este proyecto te muestra cómo subir archivos (individuales y múltiples) y servirlos para su descarga.

* **Características Principales:**
    * **Subida de Archivo Único:** Un *endpoint* para cargar un solo archivo.
    * **Subida de Múltiples Archivos:** Funcionalidad para subir varios archivos a la vez.
    * **Descarga de Archivos:** Cómo servir archivos almacenados para su descarga por el usuario.
    * Configuración del directorio de carga desde un archivo `.env`.
    * Seguridad básica contra *path traversal*.
* **Ir al proyecto:** [carga_ficheros/README.md](https://github.com/jmsanzprieto/caja_herramientas/blob/main/carga_ficheros/README.md)

---

### 🔍 4. Paginación y Filtrado

Esencial para manejar grandes conjuntos de datos de manera eficiente. Este ejemplo demuestra cómo implementar paginación y filtrado en tus *endpoints*.

* **Características Principales:**
    * **Paginación:** Implementación de `skip` y `limit` (o `offset`) para controlar el flujo de datos.
    * **Filtrado Básico:** Permite filtrar resultados por uno o más campos (e.g., `category`, `status`, rango de precios).
    * Datos provenientes de un archivo JSON, configurable vía `.env`.
    * Validación de parámetros de consulta con FastAPI `Query`.
* **Ir al proyecto:** [paginacion_filtrado/README.md](https://github.com/jmsanzprieto/caja_herramientas/blob/main/paginacion_filtrado/README.md)

---

### 🚫 5. Manejo de Errores Personalizado

Mejora la experiencia del desarrollador con respuestas de error informativas y amigables.

* **Características Principales:**
    * **Manejo de `HTTPException` Estándar:** Personaliza las respuestas para errores HTTP comunes (400, 404, 403, etc.).
    * **Excepciones de Negocio Personalizadas:** Define y gestiona tus propias clases de excepción para escenarios específicos (e.g., `ItemNotFoundException`, `UnauthorizedAccessException`).
    * Manejadores de excepciones centralizados para respuestas JSON consistentes.
    * Separación de la lógica de errores del código de negocio.
* **Ir al proyecto:** [gestion_errores/README.md](https://github.com/jmsanzprieto/caja_herramientas/blob/main/gestion_errores/README.md)

---

### 💬 6. WebSockets (Chat y Notificaciones en Tiempo Real)

Para aplicaciones en tiempo real, como chats, notificaciones o actualizaciones en vivo. Demuestra la comunicación bidireccional entre cliente y servidor.

* **Características Principales:**
    * **Chat Simple:** Permite el intercambio de mensajes en tiempo real entre múltiples clientes.
    * **Notificaciones Personales:** Envío de mensajes a un cliente WebSocket específico.
    * **Notificaciones Globales (Broadcast):** Envío de mensajes a todos los clientes conectados.
    * Gestión centralizada de las conexiones WebSocket activas.
    * Cliente HTML/JavaScript básico para la interacción.
* **Ir al proyecto:** [websockets/README.md](https://github.com/jmsanzprieto/caja_herramientas/blob/main/websockets/README.md)

---

### 🐳 7. Dockerización (con SQLite)

Indispensable para el despliegue y la consistencia del entorno. Este proyecto muestra cómo empaquetar una aplicación FastAPI y su base de datos SQLite en contenedores Docker.

* **Características Principales:**
    * **Aplicación FastAPI Completa:** Un CRUD básico listo para Docker.
    * **Base de Datos SQLite:** Integración de una base de datos ligera dentro del contenedor.
    * **`Dockerfile`:** Define los pasos para construir la imagen Docker de la aplicación.
    * **`docker-compose.yml`:** Orquesta el levantamiento y la gestión de la aplicación en un entorno contenedorizado.
    * **Persistencia de Datos:** La base de datos SQLite persiste en el *host* gracias a los volúmenes de Docker.
    * Configuración de la URL de la base de datos a través de `.env`.
* **Ir al proyecto:** [dockerizacion/README.md](https://github.com/jmsanzprieto/caja_herramientas/blob/main/dockerizacion/README.md)

---

## 🛠️ Cómo Usar esta Caja de Herramientas

Cada microproyecto es independiente. Para usar cualquiera de ellos:

1.  **Navega al directorio del proyecto** que te interese (ej. `cd carga_ficheros`).
2.  **Consulta su `README.md` específico** para conocer los requisitos, la configuración (especialmente el archivo `.env`) y los pasos de ejecución.
3.  Instala las dependencias (`pip install -r requirements.txt`) y ejecuta la aplicación como se indica en su README.

---

¡Esperamos que esta colección de ejemplos te sea de gran utilidad para tus proyectos con FastAPI!