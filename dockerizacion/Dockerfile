# Usa una imagen base oficial de Python
FROM python:3.10-slim-buster

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de requerimientos e instala las dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de la aplicación
COPY . .

# Expone el puerto en el que la aplicación FastAPI se ejecutará
EXPOSE 8000

# Comando para ejecutar la aplicación cuando el contenedor se inicie
# `--host 0.0.0.0` es necesario para que Uvicorn escuche en todas las interfaces de red
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]