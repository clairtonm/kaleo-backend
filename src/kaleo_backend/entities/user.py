from pydantic import BaseModel, EmailStr, Field, PrivateAttr


class User(BaseModel):
    first_name: str = Field(...)
    last_name: str = Field(...)
    email: EmailStr = Field(...)
    account_type: str = Field(examples=['admin', 'professor', 'student'])
    _hashed_password: str | None = PrivateAttr(default=None)

class UserLogin(BaseModel):
    username: str
    password: str
