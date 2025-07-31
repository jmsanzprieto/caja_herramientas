import json
import os
from typing import List, Dict, Optional, Any
from dotenv import load_dotenv
from pydantic import BaseModel

# Carga las variables de entorno
load_dotenv()

# Obtiene la ruta del archivo de datos desde .env
# Usamos un valor por defecto para que sea más robusto si la variable no existe
ITEMS_DATA_PATH = os.getenv("ITEMS_DATA_PATH", "./data/items.json")

# Definición del modelo Pydantic para un Item
class Item(BaseModel):
    id: int
    name: str
    category: str
    status: str
    price: float

_all_items: List[Item] = [] # Almacenará los ítems cargados una vez

def load_items_data() -> None:
    """
    Carga los ítems desde el archivo JSON especificado.
    Solo se carga una vez para evitar lecturas repetidas.
    """
    global _all_items
    if not _all_items: # Si la lista está vacía, cargar los datos
        if not os.path.exists(ITEMS_DATA_PATH):
            raise FileNotFoundError(f"El archivo de datos no se encontró en: {ITEMS_DATA_PATH}")
        
        try:
            with open(ITEMS_DATA_PATH, 'r', encoding='utf-8') as f:
                raw_data = json.load(f)
                _all_items = [Item(**item_data) for item_data in raw_data]
            print(f"Datos cargados desde {ITEMS_DATA_PATH}. Total de ítems: {len(_all_items)}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Error al decodificar JSON en {ITEMS_DATA_PATH}: {e}")
        except Exception as e:
            raise Exception(f"Error inesperado al cargar datos: {e}")

# Aseguramos que los datos se carguen cuando el módulo se importa
load_items_data()

def get_filtered_and_paginated_items(
    skip: int = 0,
    limit: int = 10,
    category: Optional[str] = None,
    status: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None
) -> List[Item]:
    """
    Filtra y pagina la lista de ítems.
    """
    filtered_items = _all_items

    # Aplicar filtros
    if category:
        filtered_items = [item for item in filtered_items if item.category.lower() == category.lower()]
    if status:
        filtered_items = [item for item in filtered_items if item.status.lower() == status.lower()]
    if min_price is not None:
        filtered_items = [item for item in filtered_items if item.price >= min_price]
    if max_price is not None:
        filtered_items = [item for item in filtered_items if item.price <= max_price]

    # Aplicar paginación
    # Asegúrate de que skip y limit sean no negativos
    _skip = max(0, skip)
    _limit = max(0, limit)

    return filtered_items[_skip : _skip + _limit]

def get_total_items_count(
    category: Optional[str] = None,
    status: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None
) -> int:
    """
    Devuelve el número total de ítems después de aplicar los filtros (sin paginación).
    Útil para calcular el número total de páginas.
    """
    filtered_items = _all_items

    if category:
        filtered_items = [item for item in filtered_items if item.category.lower() == category.lower()]
    if status:
        filtered_items = [item for item in filtered_items if item.status.lower() == status.lower()]
    if min_price is not None:
        filtered_items = [item for item in filtered_items if item.price >= min_price]
    if max_price is not None:
        filtered_items = [item for item in filtered_items if item.price <= max_price]
        
    return len(filtered_items)