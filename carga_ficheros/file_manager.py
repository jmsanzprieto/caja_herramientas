import os
from fastapi import UploadFile, HTTPException
from fastapi.responses import FileResponse
from typing import List
from dotenv import load_dotenv # Importa load_dotenv

# Carga las variables de entorno desde el archivo .env
load_dotenv()

# Obtiene la ruta del directorio de carga desde las variables de entorno
# Si no está definida en .env, usa 'uploads' como valor por defecto
UPLOAD_DIRECTORY = os.getenv("UPLOAD_DIR", "./uploads")

# Asegúrate de que el directorio de subida exista al importar el módulo
os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)

async def save_single_file(file: UploadFile) -> dict:
    """
    Guarda un solo archivo en el directorio de subida.
    """
    try:
        # Usamos os.path.basename para evitar path traversal si el nombre de archivo contiene rutas
        safe_filename = os.path.basename(file.filename)
        file_path = os.path.join(UPLOAD_DIRECTORY, safe_filename)
        
        # Escribir el archivo en bloques para manejar archivos grandes eficientemente
        with open(file_path, "wb") as buffer:
            while contents := await file.read(1024 * 1024): # Lee en bloques de 1MB
                buffer.write(contents)
        return {"filename": safe_filename, "message": "Archivo subido exitosamente."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al subir el archivo: {e}")

async def save_multiple_files(files: List[UploadFile]) -> dict:
    """
    Guarda múltiples archivos en el directorio de subida.
    """
    uploaded_filenames = []
    for file in files:
        try:
            # Usamos os.path.basename para evitar path traversal si el nombre de archivo contiene rutas
            safe_filename = os.path.basename(file.filename)
            file_path = os.path.join(UPLOAD_DIRECTORY, safe_filename)
            
            with open(file_path, "wb") as buffer:
                while contents := await file.read(1024 * 1024):
                    buffer.write(contents)
            uploaded_filenames.append(safe_filename)
        except Exception as e:
            print(f"Error al subir {file.filename}: {e}")
            raise HTTPException(status_code=500, detail=f"Error al subir uno o más archivos.")
    return {"filenames": uploaded_filenames, "message": "Archivos subidos exitosamente."}

def get_file_for_download(filename: str) -> FileResponse:
    """
    Prepara un archivo para su descarga, verificando su existencia.
    """
    # Usamos os.path.basename para evitar path traversal
    safe_filename = os.path.basename(filename)
    file_path = os.path.join(UPLOAD_DIRECTORY, safe_filename)
    
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Archivo no encontrado.")
    
    return FileResponse(file_path, media_type="application/octet-stream", filename=safe_filename)

def get_available_files() -> List[str]:
    """
    Obtiene una lista de los nombres de los archivos disponibles en el directorio de subida.
    """
    # También es buena práctica verificar si el directorio existe antes de listarlo
    if not os.path.exists(UPLOAD_DIRECTORY):
        return []
    return os.listdir(UPLOAD_DIRECTORY)