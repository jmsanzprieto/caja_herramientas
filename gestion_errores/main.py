from fastapi import FastAPI, HTTPException, Query
from typing import Optional, Dict

# Importamos las excepciones y sus manejadores
from errors import (
    http_exception_handler,
    ItemNotFoundException,
    item_not_found_exception_handler,
    UnauthorizedAccessException,
    unauthorized_access_exception_handler,
    InvalidInputException,
    invalid_input_exception_handler
)

# Importamos la lógica de negocio
import services

app = FastAPI(
    title="API de Manejo de Errores Personalizado",
    description="Demostración de cómo interceptar y personalizar respuestas de error en FastAPI."
)

# --- Registro de Manejadores de Excepciones ---

# 1. Registrar un manejador para HTTPException (para errores 404, 422, etc.)
app.add_exception_handler(HTTPException, http_exception_handler)

# 2. Registrar manejadores para nuestras excepciones personalizadas
app.add_exception_handler(ItemNotFoundException, item_not_found_exception_handler)
app.add_exception_handler(UnauthorizedAccessException, unauthorized_access_exception_handler)
app.add_exception_handler(InvalidInputException, invalid_input_exception_handler)

# --- Endpoints de Demostración ---

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    """
    Obtiene un ítem por ID. Demuestra `ItemNotFoundException`.
    """
    return services.get_item_by_id(item_id)

@app.post("/items/")
async def create_new_item(
    item_data: Dict[str, str], # Esperamos un JSON con al menos {"name": "..."}
    user_role: Optional[str] = Query("guest", description="Rol del usuario para simular autorización (e.g., 'admin', 'editor', 'guest').")
):
    """
    Crea un nuevo ítem. Demuestra `UnauthorizedAccessException` e `InvalidInputException`.
    """
    return services.create_item(item_data, user_role)

@app.delete("/items/{item_id}")
async def remove_item(
    item_id: int,
    user_role: Optional[str] = Query("guest", description="Rol del usuario para simular autorización (e.g., 'admin', 'editor', 'guest').")
):
    """
    Elimina un ítem por ID. Demuestra `UnauthorizedAccessException` y `ItemNotFoundException`.
    """
    return services.delete_item(item_id, user_role)

@app.get("/force-404/")
async def force_404():
    """
    Endpoint que fuerza un error 404 HTTP estándar para ver el manejador personalizado.
    """
    raise HTTPException(status_code=404, detail="Este recurso fue forzado a no ser encontrado.")

@app.get("/force-400/")
async def force_400():
    """
    Endpoint que fuerza un error 400 HTTP estándar para ver el manejador personalizado.
    """
    raise HTTPException(status_code=400, detail="Petición incorrecta forzada por el servidor.")