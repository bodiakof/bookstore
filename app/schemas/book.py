from pydantic import BaseModel
from app.enums.book_format import BookFormat


class BookBase(BaseModel):
    title: str
    author: str
    price: float
    stock: int
    format: BookFormat


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int

    class Config:
        orm_mode = True
