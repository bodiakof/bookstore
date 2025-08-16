from pydantic import BaseModel, field_validator

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
    isbn: str | None = None


class BookUpdate(BaseModel):
    '''Schema for updating a book (partial or full).'''
    title: str | None = None
    author: str | None = None
    price: float | None = None
    stock: int | None = None
    format: BookFormat | None = None
    category: Category | None = None
    genre: Genre | None = None
    isbn: str | None = None


class Book(BookBase):
    '''Schema for reading a book from DB.'''
    id: int
    isbn: str

    class Config:
        orm_mode = True
