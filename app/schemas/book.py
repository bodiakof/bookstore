from pydantic import BaseModel, field_validator
from typing import Optional

from app.enums.book_format import BookFormat
from app.enums.category import Category
from app.enums.genre import Genre
from app.enums.mappings import GENRE_TO_CATEGORY


class BookBase(BaseModel):
    title: str
    author: str
    price: float
    stock: int
    format: BookFormat
    category: Category
    genre: Genre

    @field_validator('genre')
    def check_genre_category_match(cls, genre_value, info):
        category_value = info.data.get('category')

        if category_value and GENRE_TO_CATEGORY.get(genre_value) != category_value:
            raise ValueError(
                f'Genre "{genre_value}" does not match category "{category_value}"'
                )

        return genre_value


class BookCreate(BookBase):
    '''Schema for creating a book.'''
    pass


class BookUpdate(BaseModel):
    '''Schema for updating a book (partial or full).'''
    title: Optional[str] = None
    author: Optional[str] = None
    price: Optional[float] = None
    stock: Optional[int] = None
    format: Optional[BookFormat] = None
    category: Optional[Category] = None
    genre: Optional[Genre] = None


class Book(BookBase):
    '''Schema for reading a book from DB.'''
    id: int

    class Config:
        orm_mode = True
