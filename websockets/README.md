# 💬 WebSockets en FastAPI: Chat y Notificaciones en Tiempo Real

Este proyecto es un ejemplo práctico y modular de cómo implementar funcionalidades en tiempo real, como un chat simple y notificaciones, utilizando **WebSockets** en FastAPI. Demuestra la comunicación bidireccional persistente entre el cliente y el servidor, esencial para muchas aplicaciones web modernas.

---

## 🚀 Características

* **Chat Simple:** Permite a múltiples clientes conectados intercambiar mensajes en tiempo real.
* **Notificaciones Personales:** Envía mensajes a un cliente WebSocket específico.
* **Notificaciones Globales (Broadcast):** Envía mensajes a todos los clientes WebSocket conectados simultáneamente.
* **Gestión de Conexiones:** Un sistema robusto para añadir, eliminar y gestionar las conexiones WebSocket activas.
* **Modularidad:** La lógica de gestión de WebSockets está separada de la aplicación principal de FastAPI.
* **Cliente HTML/JavaScript:** Incluye un cliente web básico para interactuar fácilmente con los *endpoints* de WebSocket.

---

## 📂 Estructura del Proyecto

```
.
├── main.py             # Define la aplicación FastAPI, rutas HTTP y WebSocket.
├── websocket_manager.py # Gestiona las conexiones WebSocket activas y el envío de mensajes.
├── static/             # Directorio para archivos estáticos del cliente.
│   └── index.html      # Cliente HTML/JavaScript para el chat y notificaciones.
└── README.md           # Este mismo archivo.
```

---

## 🛠️ Requisitos

* Python 3.7+

---

## 📦 Instalación de Dependencias

Instala las librerías necesarias utilizando `pip`:

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

## 🌐 Uso y Demostración

Abre tu navegador web y visita:

```
http://127.0.0.1:8000
```

### Para una demostración completa:

1. **Abre Múltiples Pestañas/Ventanas:** Abre `http://127.0.0.1:8000` en varias pestañas o ventanas de tu navegador para simular múltiples clientes. Cada pestaña tendrá un ID de cliente único generado.

2. **Chatea:**
   - En cualquiera de las pestañas, escribe un mensaje en el campo "Escribe un mensaje..." y presiona Enter o haz clic en "Enviar".
   - Verás cómo el mensaje aparece instantáneamente en el área de chat de todas las pestañas conectadas, con el remitente indicado.

3. **Notificación Personal:**
   - Haz clic en el botón "Enviar Notificación del Sistema (solo para ti)" en una pestaña específica.
   - Observa cómo la notificación solo aparece en la sección "Notificaciones en Tiempo Real" de esa pestaña y no en las demás.

4. **Notificación Global (Broadcast):**
   - Haz clic en el botón "Broadcast Notificación (a todos)" en cualquier pestaña.
   - Verás cómo la notificación aparece en la sección "Notificaciones en Tiempo Real" de todas las pestañas conectadas.

## 💻 Detalles Técnicos

### main.py

Este archivo es el corazón de la aplicación FastAPI. Se encarga de:

- **Inicializar la instancia de FastAPI.**
- **Montar archivos estáticos:** Utiliza `app.mount` para servir el archivo `index.html` del cliente desde el directorio `static/`.
- **Ruta HTTP `/`:** Sirve la página `index.html` cuando se accede a la raíz del servidor.
- **Ruta WebSocket `/ws/{client_id}`:** Este es el endpoint principal para la conexión WebSocket.
  - Acepta la conexión del cliente utilizando `manager.connect()`.
  - Entra en un bucle (`while True`) para `receive_text()` mensajes del cliente.
  - Analiza el tipo de mensaje (`chat`, `notification`, `broadcast_notification`) y delega la acción al `websocket_manager`.
  - Maneja las desconexiones de clientes utilizando `WebSocketDisconnect`.

### websocket_manager.py

Este módulo se especializa en la gestión de las conexiones activas:

**ConnectionManager clase:**
- Mantiene una lista (`active_connections`) de todos los objetos WebSocket conectados.
- `connect(websocket: WebSocket)`: Añade un nuevo WebSocket a la lista y acepta la conexión.
- `disconnect(websocket: WebSocket)`: Elimina un WebSocket de la lista cuando se desconecta.
- `send_personal_message(message: str, websocket: WebSocket)`: Envía un mensaje JSON a un WebSocket específico.
- `broadcast(message: str)`: Itera sobre todas las conexiones activas y envía el mensaje JSON a cada una.

**Instancia global `manager`:** Se crea una única instancia de `ConnectionManager` que es importada y utilizada por `main.py`.

### static/index.html

El archivo del cliente que se ejecuta en el navegador.

- Establece una conexión WebSocket con el backend de FastAPI, pasando un ID de cliente aleatorio en la URL.
- Escucha los eventos `onopen`, `onmessage`, `onclose` y `onerror` del WebSocket.
- Parse los mensajes JSON recibidos y los muestra en las áreas de chat o notificaciones según su `type`.
- Contiene funciones JavaScript para enviar mensajes de chat, notificaciones personales y notificaciones de broadcast al servidor a través del WebSocket.