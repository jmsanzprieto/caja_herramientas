from fastapi import FastAPI, UploadFile, File, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import List

# Importamos las funciones de nuestro módulo de lógica
import file_manager

app = FastAPI()

# Configuramos el directorio de plantillas
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """
    Muestra la página de inicio con formularios y enlaces a archivos.
    """
    files_in_uploads = file_manager.get_available_files()
    return templates.TemplateResponse("index.html", {"request": request, "files_in_uploads": files_in_uploads})

@app.post("/uploadfile/")
async def upload_single_file(file: UploadFile = File(...)):
    """
    Endpoint para subir un solo archivo, usando la lógica de file_manager.
    """
    # La lógica de guardar el archivo está en file_manager
    response_data = await file_manager.save_single_file(file)
    return response_data

@app.post("/uploadfiles/")
async def upload_multiple_files(files: List[UploadFile] = File(...)):
    """
    Endpoint para subir múltiples archivos, usando la lógica de file_manager.
    """
    # La lógica de guardar los archivos está en file_manager
    response_data = await file_manager.save_multiple_files(files)
    return response_data

@app.get("/download/{filename}")
async def download_file(filename: str):
    """
    Endpoint para descargar un archivo específico, usando la lógica de file_manager.
    """
    # La lógica de servir el archivo está en file_manager
    return file_manager.get_file_for_download(filename)