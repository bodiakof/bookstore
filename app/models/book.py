from sqlalchemy import Column, Integer, String, Float, Enum as SqlEnum
from sqlalchemy.orm import relationship

from app.db.database import Base
from app.enums.book_format import BookFormat
from app.enums.category import Category
from app.enums.genre import Genre


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    stock = Column(Integer, default=0)
    isbn = Column(String, unique=True, index=True, nullable=False)

    format = Column(
        SqlEnum(BookFormat, name='book_format_enum'),
        nullable=False, 
        default=BookFormat.PAPERBACK
        )

    category = Column(
        SqlEnum(Category, name='category_enum'),
        nullable=False
    )

    genre = Column(
        SqlEnum(Genre, name='genre_enum'),
        nullable=False
    )

    contributors_assoc = relationship('BookContributor', back_populates='book')
    contributors = relationship('Contributor', secondary='book_contributors', back_populates='books')
