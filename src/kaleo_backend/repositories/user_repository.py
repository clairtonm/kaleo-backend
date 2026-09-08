from kaleo_backend.entities.user import User


class UserRepository:
    def __init__(self, db):
        self.db = db

    async def get_user_by_id(self, user_id):
        query = "SELECT * FROM kaleo.users WHERE id = %s"
        result = await self.db.query(query, (user_id,))
        return User(**result[0]) if result else None

    async def get_user_by_email(self, email):
        query = "SELECT * FROM kaleo.users WHERE email = %s"
        result = await self.db.query(query, (email,))
        return User(**result[0]) if result else None

    async def create_user(self, user: User):
        query = "INSERT INTO kaleo.users (first_name, last_name, email, account_type) VALUES (%s, %s, %s, %s)"
        await self.db.insert_many(query, [(user.first_name, user.last_name, user.email, user.account_type)])

    async def get_users_by_account_type(self, account_type):
        query = "SELECT * FROM kaleo.users WHERE account_type = %s"
        result = await self.db.query(query, (account_type,))
        return [User(**row) for row in result]

    async def update(self, user: User):
        query = "UPDATE kaleousers SET first_name = %s, last_name = %s, email = %s, account_type = %s, updated_at = NOW() WHERE id = %s"
        await self.db.insert_many(query, [(user.first_name, user.last_name, user.email, user.account_type, user.id)])

    async def update_password(self, user_id: str, hashed_password: str):
        query = "UPDATE kaleo.users SET hashed_password = %s, updated_at = NOW() WHERE id = %s"
        await self.db.insert_many(query, [(hashed_password, user_id)])
