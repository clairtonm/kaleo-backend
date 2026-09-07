from kaleo_backend.entities.user import User


class UserRepository:
    def __init__(self, db):
        self.db = db

    def get_user_by_id(self, user_id):
        query = "SELECT * FROM users WHERE id = %s"
        result = self.db.execute(query, (user_id,))
        return User(**result.fetchone())

    def get_user_by_email(self, email):
        query = "SELECT * FROM users WHERE email = %s"
        result = self.db.execute(query, (email,))
        return User(**result.fetchone())

    def create_user(self, user: User):
        if not user.hashed_password:
            user.create_hashed_password()
        query = "INSERT INTO users (first_name, last_name, email, account_type, hashed_password) VALUES (%s, %s, %s, %s, %s)"
        self.db.execute(query, (user.first_name, user.last_name, user.email, user.account_type, user.hashed_password))
        self.db.commit()
