import logging

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.book import BookCreate, BookUpdate, Book
from app.crud import book as book_crud
from app.enums.book_format import BookFormat


router = APIRouter()
logger = logging.getLogger(__name__)

@router.get('/', response_model=list[Book])
def read_books(db: Session = Depends(get_db)):
    '''Get a list of all books.'''
    logger.info('GET /books called')
    books = book_crud.get_books(db)
    logger.info(f'Fetched {len(books)} book(s)')
    return books

@router.get('/{book_id}', response_model=Book)
def read_book(book_id: int, db: Session = Depends(get_db)):
    '''Get details for a single book by ID.'''
    logger.info(f'GET /books/{book_id} called')
    try:
        book = book_crud.get_book(db, book_id)
        logger.info(f'Book {book_id} fetched successfully')
        return book
    except HTTPException as e:
        logger.warning(f'Book {book_id} not found')
        raise e

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
    logger.info(f'POST /books called with payload type: {type(books).__name__}')
    try:
        result = book_crud.create_books(db, books)
        logger.info(f'Created {len(result) if isinstance(result, list) else 1} book(s)')
        return result
    except Exception as e:
        logger.exception('Failed to create books')
        raise HTTPException(status_code=400, detail=str(e))

@router.put('/{book_id}', response_model=Book)
@router.patch('/{book_id}', response_model=Book)
def update_book(book_id: int, book: BookUpdate, db: Session = Depends(get_db)):
    '''
    Update a book (PUT = full, PATCH = partial).
    '''
    logger.info(f'PUT/PATCH /books/{book_id} called')
    book_data = book.model_dump(exclude_unset=True)
    try:
        updated_book = book_crud.update_book(db, book_id, book_data)
        logger.info(f'Book {book_id} updated successfully')
        return update_book
    except HTTPException as e:
        logger.warning(f'Failed to update book {book_id}: {e.detail}')
        raise e
    except Exception:
        logger.exception(f'Unexpected error while updating book {book_id}')
        raise HTTPException(status_code=500, detail='Unexpected error during update')
    
@router.delete('/{book_id}')
def delete_book(book_id: int, db: Session = Depends(get_db)):
    '''Delete a book by ID.'''
    logger.info(f'DELETE /books/{book_id} called')
    try:
        result = book_crud.delete_book(db, book_id)
        logger.info(f'Book {book_id} deleted')
        return result
    except HTTPException as e:
        logger.warning(f'Failed to delete book {book_id}: {e.detail}')
        raise e
    except Exception:
        logger.exception(f'Unexpected error while deleting book {book_id}')
        raise HTTPException(status_code=500, detail='Unexpected error during deletion')

@router.get('/format/{format}', response_model=list[Book])
def read_books_by_format(format: BookFormat, db: Session = Depends(get_db)):
    '''Fetch book(s) by format'''
    logger.info(f'GET /books/format/{format.value} called')
    books = book_crud.get_books_by_format(db, format.value)
    logger.info(f'Fetched {len(books)} book(s) with format {format.value}')
    return books
