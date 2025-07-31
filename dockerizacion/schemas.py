from pydantic import BaseModel, Field
from typing import Optional

class ItemBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    description: Optional[str] = None
    price: int = Field(..., ge=0) # ge=0 para precio >= 0
    is_active: bool = True

class ItemCreate(ItemBase):
    pass

class ItemUpdate(ItemBase):
    # En una actualización, todos los campos son opcionales
    name: Optional[str] = Field(None, min_length=3, max_length=50)
    price: Optional[int] = Field(None, ge=0)


class Item(ItemBase):
    id: int

    class Config:
        from_attributes = True # Equivalente a orm_mode = True en Pydantic v1.x