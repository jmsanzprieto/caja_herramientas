import json
from datetime import datetime, timedelta
from typing import Optional

import bcrypt
from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from models import UserInDB, TokenData

# Configuración del JWT
SECRET_KEY = "tu_super_secreto_jwt" # ¡Cambia esto en un entorno de producción!
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# --- Funciones de Utilidad ---

def get_user_from_json(username: str) -> Optional[UserInDB]:
    """Carga los usuarios desde users.json y busca un usuario por nombre."""
    try:
        with open("users.json", "r") as f:
            users_data = json.load(f)
            for user_data in users_data:
                if user_data["username"] == username:
                    return UserInDB(**user_data)
    except FileNotFoundError:
        print("Error: users.json no encontrado.")
    except json.JSONDecodeError:
        print("Error: users.json no es un JSON válido.")
    return None

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifica si la contraseña plana coincide con la contraseña hasheada."""
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """Crea un token de acceso JWT."""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)) -> UserInDB:
    """Dependencia para obtener el usuario actual desde el token JWT."""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudieron validar las credenciales",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user_from_json(token_data.username)
    if user is None:
        raise credentials_exception
    return user