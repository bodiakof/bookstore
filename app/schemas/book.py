from pydantic import BaseModel, validator
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

    @validator('genre')
    def check_genre_category_match(cls, genre_value, values):
        category_value = values.get('category')

        if category_value and GENRE_TO_CATEGORY.get(genre_value) != category_value:
            raise ValueError(
                f'Genre "{genre_value}" does not match category "{category_value}"'
                )

        return genre_value


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int

    class Config:
        orm_mode = True
