
import uvicorn
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware

from kaleo_backend.entities.user_login import UserLogin
from kaleo_backend.infra.db.postgres_adapter import PostgresAdapter
from kaleo_backend.services.config import Config


async def lifespan(app: FastAPI):
    config = Config()
    db = PostgresAdapter(config.database_url)
    db.connect()
    app.state.db = db
    app.state.config = config
    yield

app = FastAPI(title="Kaleo Backend")

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/login", status_code=status.HTTP_200_OK)
async def login(credentials: UserLogin):
    if credentials.username == "admin@admin" and credentials.password == "secret123":
        return {
            "message": "Login successful",
            "token": "mock-jwt-token-xyz-123",
            "user": {
                "username": credentials.username,
            },
        }

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid username or password",
    )

def main():
    uvicorn.run("kaleo_backend.main:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    main()
