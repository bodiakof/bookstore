from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.book import BookCreate, BookUpdate, Book
from app.crud import book as book_crud
from app.enums.book_format import BookFormat


router = APIRouter()

@router.get('/', response_model=list[Book])
def read_books(db: Session = Depends(get_db)):
    '''Get a list of all books.'''
    return book_crud.get_books(db)

@router.get('/{book_id}', response_model=Book)
def read_book(book_id: int, db: Session = Depends(get_db)):
    '''Get details for a single book by ID.'''
    return book_crud.get_book(db, book_id)

@router.post('/', response_model=Book | list[Book], status_code=201)
def create_books(
    books: BookCreate | list[BookCreate], 
    db: Session = Depends(get_db)
    ):
    '''
    Create one or multiple books.
    - If a single book is sent, returns one Book.
    - If a list of books is sent, returns a list of Books.
    '''
    try:
        return book_crud.create_books(db, books)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put('/{book_id}', response_model=Book)
@router.patch('/{book_id}', response_model=Book)
def update_book(book_id: int, book: BookUpdate, db: Session = Depends(get_db)):
    '''
    Update a book (PUT = full, PATCH = partial).
    '''
    book_data = book.model_dump(exclude_unset=True)
    return book_crud.update_book(db, book_id, book_data)

@router.delete('/{book_id}')
def delete_book(book_id: int, db: Session = Depends(get_db)):
    '''Delete a book by ID.'''
    return book_crud.delete_book(db, book_id)

@router.get('/format/{format}', response_model=list[Book])
def read_books_by_format(format: BookFormat, db: Session = Depends(get_db)):
    return book_crud.get_books_by_format(db, format.value)
