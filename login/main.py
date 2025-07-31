from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from models import UserInDB, Token
from auth import get_user_from_json, verify_password, create_access_token, get_current_user

app = FastAPI()

@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Endpoint para el login de usuarios.
    Retorna un token JWT si las credenciales son válidas.
    """
    user = get_user_from_json(form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(
        data={"sub": user.username}
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/protected-content")
async def read_protected_content(current_user: UserInDB = Depends(get_current_user)):
    """
    Endpoint protegido que requiere un token JWT válido.
    Retorna "Hola Mundo" si el usuario está autenticado.
    """
    return {"message": "Hola Mundo"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)