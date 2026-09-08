from datetime import datetime, timedelta

import jwt
from pwdlib import PasswordHash

from kaleo_backend.services.config import get_config

password_hash = PasswordHash.recommended()
config = get_config()

SECRET_KEY = config.secret_key
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 3600

def hash_password(password: str) -> str:
    return password_hash.hash(password)

def verify_password(password: str, hashed_password: str) -> bool:
    return password_hash.verify(password, hashed_password)

def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    if expires_delta:
        expire = datetime.now(datetime.UTC) + expires_delta
    else:
        expire = datetime.now(datetime.UTC) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    payload = {
        "sub": data["sub"],
        "exp": expire,
        "iat": datetime.now(datetime.UTC),
    }

    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
