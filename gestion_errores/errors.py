from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from starlette.status import HTTP_404_NOT_FOUND, HTTP_403_FORBIDDEN, HTTP_400_BAD_REQUEST

# --- 1. Excepciones HTTP Estándar Personalizadas ---
# FastAPI ya maneja estas, pero podemos registrar un handler para personalizar su respuesta.

async def http_exception_handler(request: Request, exc: HTTPException):
    """
    Manejador personalizado para todas las HTTPException de FastAPI.
    """
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "detail": exc.detail,
            "code": exc.status_code,
            "error_type": "HTTP_ERROR"
        }
    )

# --- 2. Excepciones de Negocio Personalizadas ---
# Definimos nuestras propias clases de excepción para casos específicos de negocio.

class ItemNotFoundException(HTTPException):
    """Excepción para cuando un ítem específico no se encuentra."""
    def __init__(self, item_id: int):
        super().__init__(status_code=HTTP_404_NOT_FOUND, detail=f"Ítem con ID '{item_id}' no encontrado.")
        self.item_id = item_id
        self.error_type = "ITEM_NOT_FOUND"

class UnauthorizedAccessException(HTTPException):
    """Excepción para cuando un usuario no tiene permisos."""
    def __init__(self, required_role: str):
        super().__init__(status_code=HTTP_403_FORBIDDEN, detail=f"Acceso no autorizado. Se requiere el rol '{required_role}'.")
        self.required_role = required_role
        self.error_type = "UNAUTHORIZED_ACCESS"

class InvalidInputException(HTTPException):
    """Excepción para cuando la entrada del usuario no es válida para la lógica de negocio."""
    def __init__(self, field: str, value: any, reason: str):
        super().__init__(status_code=HTTP_400_BAD_REQUEST, detail=f"Entrada inválida para '{field}': '{value}'. Razón: {reason}")
        self.field = field
        self.value = value
        self.reason = reason
        self.error_type = "INVALID_INPUT"

# --- 3. Manejadores para Excepciones Personalizadas ---
# Registramos un handler para cada una de nuestras excepciones de negocio.

async def item_not_found_exception_handler(request: Request, exc: ItemNotFoundException):
    """
    Manejador para ItemNotFoundException.
    """
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "message": exc.detail,
            "item_id": exc.item_id,
            "code": exc.status_code,
            "error_type": exc.error_type
        }
    )

async def unauthorized_access_exception_handler(request: Request, exc: UnauthorizedAccessException):
    """
    Manejador para UnauthorizedAccessException.
    """
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "message": exc.detail,
            "required_role": exc.required_role,
            "code": exc.status_code,
            "error_type": exc.error_type
        }
    )

async def invalid_input_exception_handler(request: Request, exc: InvalidInputException):
    """
    Manejador para InvalidInputException.
    """
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "message": exc.detail,
            "field": exc.field,
            "received_value": exc.value,
            "reason": exc.reason,
            "code": exc.status_code,
            "error_type": exc.error_type
        }
    )