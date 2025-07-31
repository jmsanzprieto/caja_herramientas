import json
import os
from typing import List
from uuid import uuid4
from fastapi import APIRouter, HTTPException

# Importamos los modelos desde el nuevo archivo models.py
from models import ItemBase, ItemCreate, ItemUpdate, ItemInDB

# Definición del archivo JSON donde se guardarán los datos
DATA_FILE = "data.json"

# --- Funciones para manejar el archivo JSON (se mantienen aquí) ---

def read_items_from_json() -> List[ItemInDB]:
    """Lee todos los artículos del archivo JSON."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        try:
            items_data = json.load(f)
            return [ItemInDB(**item) for item in items_data]
        except json.JSONDecodeError:
            # Si el archivo está vacío o corrupto, se inicializa con una lista vacía
            return []

def write_items_to_json(items: List[ItemInDB]):
    """Escribe la lista de artículos al archivo JSON."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump([item.model_dump() for item in items], f, indent=2, ensure_ascii=False)

# --- Creación del APIRouter ---
router = APIRouter(
    prefix="/items",
    tags=["Items CRUD"],
    responses={404: {"description": "Not found"}},
)

# --- Endpoints del CRUD (usan los modelos importados) ---

@router.post("/", response_model=ItemInDB, status_code=201)
async def create_item(item: ItemCreate):
    """
    Crea un nuevo artículo.
    Genera un ID único y lo guarda en el archivo JSON.
    """
    items = read_items_from_json()
    new_id = str(uuid4())
    new_item = ItemInDB(id=new_id, **item.model_dump())
    items.append(new_item)
    write_items_to_json(items)
    return new_item

@router.get("/", response_model=List[ItemInDB])
async def read_all_items():
    """Obtiene una lista de todos los artículos."""
    return read_items_from_json()

@router.get("/{item_id}", response_model=ItemInDB)
async def read_item_by_id(item_id: str):
    """Obtiene un artículo por su ID."""
    items = read_items_from_json()
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Artículo no encontrado")

@router.put("/{item_id}", response_model=ItemInDB)
async def update_item(item_id: str, updated_item_data: ItemUpdate):
    """
    Actualiza un artículo existente por su ID.
    Los campos no proporcionados en el cuerpo de la solicitud no se modificarán.
    """
    items = read_items_from_json()
    found = False
    for i, item in enumerate(items):
        if item.id == item_id:
            # Actualiza solo los campos que se proporcionan en la solicitud
            updated_data = updated_item_data.model_dump(exclude_unset=True)
            for key, value in updated_data.items():
                setattr(items[i], key, value)
            write_items_to_json(items)
            found = True
            return items[i]
    if not found:
        raise HTTPException(status_code=404, detail="Artículo no encontrado")

@router.delete("/{item_id}", status_code=204)
async def delete_item(item_id: str):
    """Elimina un artículo por su ID."""
    items = read_items_from_json()
    initial_len = len(items)
    items = [item for item in items if item.id != item_id]
    if len(items) == initial_len:
        raise HTTPException(status_code=404, detail="Artículo no encontrado")
    write_items_to_json(items)
    return {"message": "Artículo eliminado correctamente"}