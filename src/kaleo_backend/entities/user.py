from pydantic import BaseModel, EmailStr, Field

from kaleo_backend.services.security import hash_password


class User(BaseModel):
    first_name: str = Field(...)
    last_name: str = Field(...)
    email: EmailStr = Field(...)
    account_type: str = Field(examples=['admin', 'professor', 'student'])
    hashed_password: str = Field(...)

    def create_hashed_password(self):
        self.hashed_password = hash_password(self.hashed_password)
