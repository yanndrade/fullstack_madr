from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    full_name: str
    password: str


class UserPublicSchema(BaseModel):
    username: str
    email: EmailStr
    full_name: str


class UserInDBSchema(UserSchema):
    id: int
