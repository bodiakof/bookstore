from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.book import BookCreate, Book
from app.crud import book as book_crud
from app.enums.book_format import BookFormat


router = APIRouter()

@router.get('/', response_model=list[Book])
def read_books(db: Session = Depends(get_db)):
    return book_crud.get_books(db)

@router.post('/', response_model=Book)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    return book_crud.create_book(db, book)

@router.get('/format/{format}', response_model=list[Book])
def read_books_by_format(format: BookFormat, db: Session = Depends(get_db)):
    return book_crud.get_books_by_format(db, format.value)
