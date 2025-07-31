import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# Carga las variables de entorno desde el archivo .env
load_dotenv()

# Obtiene la URL de la base de datos desde las variables de entorno
DATABASE_URL = os.getenv("DATABASE_URL")

# Crea el motor de la base de datos
# connect_args={"check_same_thread": False} es necesario para SQLite con FastAPI
# porque SQLAlchemy espera que cada hilo use su propia conexión,
# pero SQLite no permite esto por defecto. Para una DB multi-hilo real, esto no sería necesario.
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {}
)

# Crea una clase SessionLocal. Cada instancia de SessionLocal será una sesión de base de datos.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos declarativos de SQLAlchemy
Base = declarative_base()

def get_db():
    """
    Dependencia para obtener una sesión de base de datos.
    Cierra la sesión después de que la solicitud haya terminado.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_db_tables():
    """
    Crea las tablas de la base de datos.
    """
    Base.metadata.create_all(bind=engine)