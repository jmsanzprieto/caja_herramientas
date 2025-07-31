from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import json

# Importamos el gestor de conexiones WebSocket
from websocket_manager import manager

app = FastAPI(
    title="FastAPI WebSockets Demo",
    description="Ejemplo de chat simple y notificaciones en tiempo real con WebSockets."
)

# Montar el directorio estático para servir index.html
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def get():
    """
    Sirve la página HTML del cliente WebSocket.
    """
    with open("static/index.html", "r") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content, status_code=200)

@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    """
    Endpoint principal para las conexiones WebSocket.
    """
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            message_data = json.loads(data)

            message_type = message_data.get("type")

            if message_type == "chat":
                # Mensaje de chat: Reenviar a todos los clientes
                sender = message_data.get("sender", "Anónimo")
                message = message_data.get("message", "")
                full_message = {"type": "chat", "sender": sender, "message": message}
                await manager.broadcast(json.dumps(full_message))
                print(f"Chat de '{sender}': {message}")

            elif message_type == "notification":
                # Notificación personal: Enviar solo a este cliente
                notification_message = message_data.get("message", "Notificación personal.")
                personal_notification = {"type": "notification", "message": notification_message}
                await manager.send_personal_message(json.dumps(personal_notification), websocket)
                print(f"Notificación personal enviada a '{client_id}': {notification_message}")

            elif message_type == "broadcast_notification":
                # Notificación de broadcast: Enviar a todos los clientes
                broadcast_message = message_data.get("message", "Notificación de broadcast.")
                full_notification = {"type": "notification", "message": broadcast_message}
                await manager.broadcast(json.dumps(full_notification))
                print(f"Notificación de broadcast enviada: {broadcast_message}")

            else:
                print(f"Tipo de mensaje desconocido: {message_type}")
                await manager.send_personal_message(json.dumps({"type": "error", "message": "Tipo de mensaje no reconocido."}), websocket)

    except WebSocketDisconnect:
        manager.disconnect(websocket)
        # Opcional: Notificar a todos que un cliente se ha desconectado
        await manager.broadcast(json.dumps({"type": "chat", "sender": "Sistema", "message": f"Cliente '{client_id}' se ha desconectado."}))
        print(f"Cliente '{client_id}' desconectado.")
    except Exception as e:
        print(f"Error inesperado en WebSocket para {client_id}: {e}")
        manager.disconnect(websocket)
        # await manager.send_personal_message(json.dumps({"type": "error", "message": f"Error interno: {e}"}), websocket)