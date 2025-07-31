from typing import Optional
from pydantic import BaseModel, Field

class ItemBase(BaseModel):
    """Modelo base para un artículo, sin el ID."""
    name: str = Field(..., min_length=3, max_length=50)
    description: Optional[str] = None
    price: float = Field(..., gt=0)

class ItemCreate(ItemBase):
    """Modelo para crear un nuevo artículo (usa ItemBase)."""
    pass

class ItemUpdate(ItemBase):
    """
    Modelo para actualizar un artículo.
    Todos los campos son opcionales para permitir actualizaciones parciales.
    """
    name: Optional[str] = None
    price: Optional[float] = None
    description: Optional[str] = None # Agregamos description para permitir su actualización

class ItemInDB(ItemBase):
    """
    Modelo para un artículo tal como se almacena en la "base de datos"
    (incluye el ID).
    """
    id: str

    class Config:
        from_attributes = True # Importante para Pydantic v2