
import uvicorn
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware

from kaleo_backend.entities.user import User, UserLogin
from kaleo_backend.infra.db.postgres_adapter import PostgresAdapter
from kaleo_backend.repositories.user_repository import UserRepository
from kaleo_backend.services.config import get_config
from kaleo_backend.usecases.users.create_users import CreateUser
from kaleo_backend.usecases.users.user_password import DefinePassword


async def lifespan(app: FastAPI):
    config = get_config()
    db = PostgresAdapter(config.database_url)
    await db.connect()
    app.state.db = db
    app.state.config = config
    user_repository = UserRepository(db)
    app.state.user_repository = user_repository

    yield

    await db.disconnect()

app = FastAPI(title="Kaleo Backend", lifespan=lifespan)

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

@app.post("/users", status_code=status.HTTP_200_OK)
async def create_user(user: User):
    user_repository = app.state.user_repository
    create_user_usecase = CreateUser(user_repository)
    await create_user_usecase.execute(user)
    return {"message": "User created successfully"}

@app.put("/users/{user_id}/password", status_code=status.HTTP_200_OK)
async def define_password(user_id: str, password: str):
    user_repository = app.state.user_repository
    update_password_usecase = DefinePassword(user_repository)
    await update_password_usecase.execute(user_id, password)
    return {"message": "Password updated successfully"}


def main():
    uvicorn.run("kaleo_backend.main:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    main()
