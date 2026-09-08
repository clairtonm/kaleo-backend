
from kaleo_backend.repositories.user_repository import UserRepository
from kaleo_backend.services.security import hash_password


class DefinePassword:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def execute(self, user_id: str, password: str):
        hashed_password: str = hash_password(password)
        await self.user_repository.update_password(user_id, hashed_password)
