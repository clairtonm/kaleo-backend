from kaleo_backend.entities.user import User
from kaleo_backend.repositories.user_repository import UserRepository


class CreateUser:
    def __init__(self, user_repository: UserRepository):
        self._user_repository = user_repository

    async def execute(self, user: User):
        await self._user_repository.create_user(user)
