from fastapi import FastAPI
from crud import router as crud_router # Importamos el router y le damos un alias

app = FastAPI(
    title="API de Productos con CRUD Modular",
    description="Una API simple para realizar operaciones CRUD sobre un archivo JSON, con endpoints separados.",
    version="1.0.0",
)

# --- Montar el router de CRUD ---
app.include_router(crud_router)

# Puedes añadir otros endpoints o routers aquí si tu aplicación crece
@app.get("/")
async def root():
    return {"message": "Bienvenido a la API de Productos"}

# --- Para ejecutar la aplicación ---
# Puedes ejecutarla con: uvicorn main:app --reload