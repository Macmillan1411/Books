import uuid
from datetime import datetime
from pydantic import BaseModel, Field


class UserSchema(BaseModel):
    uid: uuid.UUID
    username: str
    first_name: str = Field(nullable=True)
    last_name: str = Field(nullable=True)
    is_verified: bool
    email: str
    password_hash: str = Field(exclude=True)
    created_at: datetime = Field()

class UserCreateSchema(BaseModel):
    username: str = Field(max_length = 10)
    first_name: str = Field(max_length = 25)
    last_name: str = Field(max_length = 25)
    email: str
    password: str = Field(min_length = 6)


