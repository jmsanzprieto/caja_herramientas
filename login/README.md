# Ejemplo de Autenticación JWT con FastAPI

Este proyecto demuestra un sistema básico de autenticación de usuarios usando FastAPI con JSON Web Tokens (JWT). Incluye inicio de sesión de usuario, generación de JWT y un endpoint protegido que requiere un token válido para el acceso. En lugar de una base de datos tradicional, los datos del usuario se almacenan en un sencillo archivo JSON, lo que facilita la comprensión de los conceptos centrales sin configuraciones complejas de bases de datos.

## 🚀 Características

- **Autenticación de Usuarios**: Inicio de sesión seguro de usuarios con nombre de usuario y contraseña.
- **Hash de Contraseñas**: Las contraseñas se almacenan de forma segura utilizando bcrypt.
- **Generación de JWT**: Genera tokens de acceso tras un inicio de sesión exitoso.
- **Endpoint Protegido**: Un endpoint de ejemplo que requiere un JWT válido para el acceso.
- **Estructura Modular**: Clara separación de responsabilidades con archivos dedicados para la lógica de autenticación, modelos de datos y la aplicación principal.

## 📂 Estructura del Proyecto

```
.
├── main.py             # Aplicación principal de FastAPI con los endpoints
├── auth.py             # Lógica de autenticación (manejo de JWT, verificación de contraseñas)
├── models.py           # Modelos Pydantic para la validación de datos
├── users.json          # Archivo JSON simple que actúa como nuestra "base de datos" de usuarios
└── requirements.txt    # Dependencias de Python
```

## 🛠️ Configuración e Instalación

Sigue estos pasos para poner en marcha el proyecto en tu máquina local.

### 1. Crea los archivos
Asegúrate de tener todos los archivos (`main.py`, `auth.py`, `models.py`, `users.json`, `requirements.txt`) en el mismo directorio.

### 2. Crea users.json
Este archivo almacenará nuestro usuario de ejemplo.

```json
[
  {
    "username": "testuser",
    "hashed_password": "$2b$12$R.cWkR2.hB.G.t.f.v.c.N.t.M.n.k.E.s.t.S.f.q.A.f.Q.r.W.y.o.P.v.s.X.z.u.H.j.K.l.M.n.o.p.q.r.s.t.u.v.w.x.y.z.A.B.C.D.E.F.G.H.I.J.K.L.M.N.O.P.Q.R.S.T.U.V.W.X.Y.Z.0.1.2.3.4.5.6.7.8.9"
  }
]
```

**Importante**: La contraseña para `testuser` es `ABC1234`. El `hashed_password` proporcionado en el JSON anterior es un ejemplo de hash. Debes generar un hash real para `ABC1234` usando bcrypt y reemplazarlo.

**Para generar el hash**:

1. Abre un intérprete de Python (o un script Python temporal).
2. Ejecuta el siguiente código:

```python
import bcrypt

password = "ABC1234".encode('utf-8')
hashed_password = bcrypt.hashpw(password, bcrypt.gensalt()).decode('utf-8')
print(hashed_password)
```

3. Copia la salida (la cadena de hash real) y pégala en `users.json` como el valor de `hashed_password`.

### 3. Instala las dependencias
Navega al directorio del proyecto en tu terminal e instala los paquetes de Python requeridos:

```bash
pip install -r requirements.txt
```

### 4. Ejecuta la Aplicación
Puedes ejecutar la aplicación FastAPI usando uvicorn:

```bash
uvicorn main:app --reload
```

El flag `--reload` es útil para el desarrollo, ya que recarga automáticamente el servidor cuando hay cambios en el código. La aplicación será accesible en `http://127.0.0.1:8000`.

## 💡 Cómo Usar

Puedes interactuar con la API usando herramientas como Postman, Insomnia, curl, o directamente a través de la documentación interactiva de la API de FastAPI (Swagger UI o ReDoc).

### 1. Autenticarse y Obtener un JWT

Para acceder a los endpoints protegidos, primero necesitas obtener un token de acceso.

- **Endpoint**: `/token`
- **Método**: `POST`
- **Content-Type**: `application/x-www-form-urlencoded`
- **Datos del Formulario (Cuerpo)**:
  - `username`: testuser
  - `password`: ABC1234 (o la contraseña que hayas hasheado)

**Ejemplo de Solicitud (usando curl)**:

```bash
curl -X POST "http://127.0.0.1:8000/token" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "username=testuser&password=ABC1234"
```

**Ejemplo de Respuesta**:

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0dXNlciIsImV4cCI6MTcxOTc0MTc3MX0.TU_TOKEN_JWT_REAL",
  "token_type": "bearer"
}
```

Copia el valor de `access_token`; lo necesitarás para los endpoints protegidos.

### 2. Acceder al Contenido Protegido

Una vez que tengas un `access_token`, puedes usarlo para acceder a los endpoints que requieren autenticación.

- **Endpoint**: `/protected-content`
- **Método**: `GET`
- **Cabeceras**:
  - `Authorization`: Bearer TU_TOKEN_DE_ACCESO (Reemplaza TU_TOKEN_DE_ACCESO con el token que obtuviste)

**Ejemplo de Solicitud (usando curl)**:

```bash
curl -X GET "http://127.0.0.1:8000/protected-content" \
     -H "Authorization: Bearer TU_TOKEN_DE_ACCESO"
```

**Ejemplo de Respuesta (si el token es válido)**:

```json
{
  "message": "Hola Mundo"
}
```

**Respuesta si el token es inválido o no se proporciona**:

```json
{
  "detail": "No se pudieron validar las credenciales"
}
```