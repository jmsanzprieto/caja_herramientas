from typing import List, Dict, Optional
from errors import ItemNotFoundException, UnauthorizedAccessException, InvalidInputException

# Simulación de una base de datos de ítems
_items_db = [
    {"id": 1, "name": "Producto A", "owner": "admin", "status": "active"},
    {"id": 2, "name": "Servicio B", "owner": "user", "status": "inactive"},
    {"id": 3, "name": "Artículo C", "owner": "admin", "status": "active"}
]

def get_item_by_id(item_id: int) -> Dict:
    """
    Busca un ítem por ID. Simula un caso donde el ítem no se encuentra.
    """
    for item in _items_db:
        if item["id"] == item_id:
            return item
    raise ItemNotFoundException(item_id=item_id)

def create_item(item_data: Dict, user_role: str) -> Dict:
    """
    Crea un nuevo ítem. Simula un caso de acceso no autorizado y validación de entrada.
    """
    if user_role not in ["admin", "editor"]:
        raise UnauthorizedAccessException(required_role="admin o editor")

    name = item_data.get("name")
    if not name or not isinstance(name, str) or len(name) < 3:
        raise InvalidInputException(field="name", value=name, reason="El nombre debe ser una cadena de al menos 3 caracteres.")
    
    # Simulación de añadir el ítem
    new_id = max([item["id"] for item in _items_db]) + 1 if _items_db else 1
    new_item = {"id": new_id, "name": name, "owner": user_role, "status": "pending"}
    _items_db.append(new_item)
    return new_item

def delete_item(item_id: int, user_role: str) -> Dict:
    """
    Elimina un ítem. Requiere rol de admin.
    """
    if user_role != "admin":
        raise UnauthorizedAccessException(required_role="admin")
    
    global _items_db
    initial_len = len(_items_db)
    _items_db = [item for item in _items_db if item["id"] != item_id]
    if len(_items_db) == initial_len:
        raise ItemNotFoundException(item_id=item_id)
    return {"message": f"Ítem con ID {item_id} eliminado."}