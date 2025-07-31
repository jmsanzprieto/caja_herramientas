from fastapi import FastAPI, Query, HTTPException, Depends
from typing import List, Optional

# Importamos las funciones y modelos de nuestro módulo de lógica de datos
import data_manager
from data_manager import Item

app = FastAPI(
    title="API de Items con Paginación y Filtrado",
    description="Ejemplo sencillo de cómo implementar paginación y filtrado en FastAPI."
)

# Endpoint principal para obtener ítems con paginación y filtrado
@app.get("/items/", response_model=List[Item])
async def read_items(
    # Parámetros de paginación
    skip: int = Query(0, ge=0, description="Número de ítems a omitir (offset)."),
    limit: int = Query(10, ge=1, le=100, description="Número máximo de ítems a devolver."),
    
    # Parámetros de filtrado
    category: Optional[str] = Query(None, description="Filtrar por categoría (ej. 'Electronics', 'Books')."),
    status: Optional[str] = Query(None, description="Filtrar por estado (ej. 'available', 'low_stock', 'out_of_stock')."),
    min_price: Optional[float] = Query(None, ge=0, description="Filtrar por precio mínimo."),
    max_price: Optional[float] = Query(None, ge=0, description="Filtrar por precio máximo.")
):
    """
    Obtiene una lista de ítems con opciones de paginación y filtrado.

    **Parámetros de consulta:**
    - `skip`: Número de elementos a saltar (offset).
    - `limit`: Número máximo de elementos a devolver.
    - `category`: Filtra los ítems por su categoría.
    - `status`: Filtra los ítems por su estado.
    - `min_price`: Filtra los ítems con un precio igual o superior a este valor.
    - `max_price`: Filtra los ítems con un precio igual o inferior a este valor.
    """
    
    try:
        items = data_manager.get_filtered_and_paginated_items(
            skip=skip,
            limit=limit,
            category=category,
            status=status,
            min_price=min_price,
            max_price=max_price
        )
        return items
    except FileNotFoundError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {e}")  

# Opcional: Endpoint para obtener el total de ítems filtrados (sin paginación)
@app.get("/items/count/", response_model=dict[str, int])
async def get_items_count(
    category: Optional[str] = Query(None, description="Filtrar por categoría (ej. 'Electronics', 'Books')."),
    status: Optional[str] = Query(None, description="Filtrar por estado (ej. 'available', 'low_stock', 'out_of_stock')."),
    min_price: Optional[float] = Query(None, ge=0, description="Filtrar por precio mínimo."),
    max_price: Optional[float] = Query(None, ge=0, description="Filtrar por precio máximo.")
):
    """
    Obtiene el número total de ítems después de aplicar los filtros.
    Útil para calcular el número total de páginas en el frontend.
    """
    try:
        total_count = data_manager.get_total_items_count(
            category=category,
            status=status,
            min_price=min_price,
            max_price=max_price
        )
        return {"total_items": total_count}
    except FileNotFoundError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {e}")