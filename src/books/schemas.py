from pydantic import BaseModel
import uuid


class BookModel(BaseModel):
    uid: uuid.UUID
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str


class BookUpdateModel(BaseModel):
    title: str
    author: str
    publisher: str
    page_count: int
    language: str


class BookCreateModel(BaseModel):
    """
    This class is used to validate the request when creating or updating a book
    """

    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str


class UserSchema(BaseModel):
    username: str
    password: str
