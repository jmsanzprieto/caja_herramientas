from typing import List
from fastapi import WebSocket, WebSocketDisconnect

class ConnectionManager:
    """
    Gestiona las conexiones activas de WebSocket.
    """
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        """
        Añade una nueva conexión WebSocket activa.
        """
        await websocket.accept()
        self.active_connections.append(websocket)
        print(f"Conexión WebSocket establecida. Clientes activos: {len(self.active_connections)}")

    def disconnect(self, websocket: WebSocket):
        """
        Elimina una conexión WebSocket de la lista de activas.
        """
        self.active_connections.remove(websocket)
        print(f"Conexión WebSocket cerrada. Clientes activos: {len(self.active_connections)}")

    async def send_personal_message(self, message: str, websocket: WebSocket):
        """
        Envía un mensaje a un cliente WebSocket específico.
        """
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        """
        Envía un mensaje a todos los clientes WebSocket activos.
        """
        for connection in self.active_connections:
            try:
                await connection.send_text(message)
            except RuntimeError as e:
                # Esto puede ocurrir si el socket se cierra inesperadamente
                print(f"Error al enviar mensaje a un cliente (posiblemente desconectado): {e}")
                # Opcional: desconectar si hay un error persistente, aunque el disconnect se encargue
                # self.disconnect(connection) # Esto podría modificar la lista mientras se itera, mejor evitar aquí

# Instancia global del gestor de conexiones
manager = ConnectionManager()