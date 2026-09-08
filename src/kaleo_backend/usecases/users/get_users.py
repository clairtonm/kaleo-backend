from kaleo_backend.repositories.user_repository import UserRepository


class GetUserById:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, user_id: int):
        user = self.user_repository.get_user_by_id(user_id)
        return user

class GetUserByEmail:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, email: str):
        user = self.user_repository.get_user_by_email(email)
        return user
