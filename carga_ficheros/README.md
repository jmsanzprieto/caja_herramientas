# 📁 Gestión de Archivos con FastAPI (Subida y Descarga)

Este proyecto es un ejemplo práctico y modular de cómo implementar la subida (simple y múltiple) y descarga de archivos utilizando FastAPI.
## 🚀 Características

- **Subida de Archivo Único**: Un endpoint dedicado para cargar un solo archivo.
- **Subida de Múltiples Archivos**: Capacidad para subir varios archivos en una única solicitud.
- **Descarga de Archivos**: Permite a los usuarios descargar archivos que han sido previamente subidos.
- **Modularidad**: La lógica de gestión de archivos está separada de las rutas de la API y la presentación (HTML).
- **Configuración Flexible**: El directorio de almacenamiento de archivos se configura a través de un archivo `.env`.
- **Seguridad Básica**: Implementa `os.path.basename()` para mitigar ataques de path traversal.
- **Interfaz de Usuario Sencilla**: Una página HTML básica con formularios para interactuar con la funcionalidad de subida/descarga.

## 📂 Estructura del Proyecto

La aplicación sigue una estructura clara y organizada:

```
.
├── .env                # Archivo para variables de entorno (p.ej., UPLOAD_DIR)
├── main.py             # Define la aplicación FastAPI y las rutas HTTP
├── file_manager.py     # Contiene la lógica de negocio para la subida y descarga de archivos
├── templates/          # Directorio para las plantillas HTML
│   └── index.html      # Plantilla principal de la interfaz de usuario
├── requirements.txt    # Dependencias del proyecto
└── README.md           # Este mismo archivo
```

## 🛠️ Requisitos

Asegúrate de tener Python 3.7+ instalado.

## ⚙️ Configuración

1. **Clona el repositorio** (o crea los archivos si los estás copiando manualmente).

2. **Crea el archivo `.env`**: En el directorio raíz del proyecto, crea un archivo llamado `.env` y añade la siguiente línea para especificar la carpeta donde se guardarán los archivos:

   ```ini
   UPLOAD_DIR=./uploads
   ```

   Puedes cambiar `./uploads` a la ruta que prefieras. Si usas una ruta absoluta, asegúrate de que el proceso que ejecuta FastAPI tenga permisos de escritura en ella.

3. **Crea el directorio de carga**: Asegúrate de que la carpeta especificada en `UPLOAD_DIR` exista en la raíz de tu proyecto. Por ejemplo, si usaste `./uploads`, crea una carpeta llamada `uploads`.

   ```bash
   mkdir uploads
   ```

## 📦 Instalación de Dependencias

Instala las librerías necesarias utilizando pip:

```bash
pip install -r requirements.txt
```

El archivo `requirements.txt` debería contener:

```
fastapi
uvicorn
jinja2
python-dotenv
python-multipart
```

## 🚀 Ejecución de la Aplicación

Una vez configurado, puedes iniciar la aplicación usando uvicorn:

```bash
uvicorn main:app --reload
```

- `main`: Se refiere al archivo `main.py`.
- `app`: Es la instancia de FastAPI dentro de `main.py`.
- `--reload`: Reinicia el servidor automáticamente cuando detecta cambios en el código (útil para desarrollo).

## 🌐 Uso

Abre tu navegador web y visita:

```
http://127.0.0.1:8000
```

Aquí encontrarás una interfaz simple para:

- **Subir un Solo Archivo**: Usa el primer formulario para seleccionar y cargar un archivo.
- **Subir Múltiples Archivos**: Usa el segundo formulario para seleccionar varios archivos a la vez y subirlos.
- **Descargar Archivos**: Una vez que hayas subido archivos, aparecerá una lista con enlaces para descargarlos.

## 💻 Detalles Técnicos

### main.py

Este es el punto de entrada de la aplicación. Se encarga de:

- Inicializar la aplicación FastAPI.
- Configurar el motor de plantillas Jinja2 para renderizar la interfaz de usuario.
- Definir los endpoints HTTP (`/`, `/uploadfile/`, `/uploadfiles/`, `/download/{filename}`).
- Delegar la lógica de negocio a las funciones definidas en `file_manager.py`.
- Renderizar la plantilla `index.html` con los datos necesarios (lista de archivos disponibles).

### file_manager.py

Contiene la lógica central de la gestión de archivos:

- Lee el directorio de carga (`UPLOAD_DIRECTORY`) desde el archivo `.env` usando `python-dotenv`.
- `save_single_file(file: UploadFile)`: Guarda un `UploadFile` en el sistema de archivos. Utiliza una lectura en bloques (1MB) para manejar archivos grandes eficientemente y `os.path.basename()` para seguridad.
- `save_multiple_files(files: List[UploadFile])`: Itera sobre una lista de `UploadFile` y guarda cada uno.
- `get_file_for_download(filename: str)`: Prepara y devuelve un `FileResponse` para la descarga de un archivo, verificando su existencia y aplicando `os.path.basename()`.
- `get_available_files()`: Lista los nombres de los archivos presentes en el directorio de carga.

### templates/index.html

La plantilla HTML que define la interfaz de usuario. Utiliza la sintaxis de Jinja2 (`{% if %}`, `{% for %}`, `{{ variable }}`) para mostrar condicionalmente los enlaces de descarga y formatear la información.