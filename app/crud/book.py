import logging

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.book import Book
from app.schemas.book import BookCreate, BookUpdate
from app.utils.isbn import generate_fake_isbn


logger = logging.getLogger(__name__)

def get_books(db: Session):
    '''Return all books from the database.'''
    logger.debug('Fetching all books from DB')
    books = db.query(Book).all()
    logger.debug(f'Fetched {len(books)} book(s)')
    return books

def get_book(db: Session, book_id: int):
    '''Fetch a single book by ID or raise 404.'''
    logger.debug(f'Fetching book with ID {book_id}')
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        logger.warning(f'Book with ID {book_id} not found')
        raise HTTPException(status_code=404, detail='Book not found')
    logger.info(f'Book with ID {book_id} fetched successfully')
    return book

def create_books(db: Session, book: BookCreate | list[BookCreate]):
    '''
    Create one or multiple book entries.
    - If 'book' is a single BookCreate, create one book.
    - If 'book' is a list of BookCreate, create multiple books.
    '''
    logger.debug('Creating book(s)')
    if isinstance(book, list):
        db_books = []
        for b in book:
            data = b.model_dump()
            if not data.get('isbn'):
                data['isbn'] = generate_fake_isbn()
            db_books.append(Book(**data))

        db.add_all(db_books)
        try:
            db.commit()
        except IntegrityError as e:
            db.rollback()
            logger.warning(f'IntegrityError: {e}')
            raise HTTPException(status_code=400, detail='Duplicate ISBN detected')
        for db_book in db_books:
            db.refresh(db_book)
        logger.info(f'Created {len(db_books)} books')
        return db_books
    else:
        data = book.model_dump()
        if not data.get('isbn'):
            data['isbn'] = generate_fake_isbn()
        db_book = Book(**data)
        db.add(db_book)
        try:
            db.commit()
        except IntegrityError as e:
            db.rollback()
            logger.warning(f'IntegrityError while creating book: {e}')
            raise HTTPException(status_code=400, detail='Book with this ISBN already exists')
        db.refresh(db_book)
        logger.info(f'Created book with ISBN {db_book.isbn}')
        return db_book

def update_book(db: Session, book_id: int, book_data: dict):
    '''
    Update an existing book with provided data.
    - book_data: dict containing only the fields to update.
    '''
    logger.debug(f'Updating book {book_id} with data {book_data}')
    book = get_book(db, book_id)
    for key, value in book_data.items():
        setattr(book, key, value)

    try:
        db.commit()
    except IntegrityError as e:
        db.rollback()
        logger.warning(f'IntegrityError updating book {book_id}: {e}')
        raise HTTPException(status_code=400, detail='Book with this ISBN already exists')
    
    db.refresh(book)
    logger.info(f'Updated book {book_id} successfully')
    return book

def delete_book(db: Session, book_id: int):
    '''Delete a book by ID.'''
    logger.debug('Deleting book with ID {book_id}')
    book = get_book(db, book_id)
    db.delete(book)
    db.commit()
    logger.info(f'Deleted book {book_id}')
    return {'detail': 'Book was successfully deleted'}

def get_books_by_format(db: Session, format: str):
    '''Return all books of specified format.'''
    logger.debug(f'Fetching books with format {format}')
    books = db.query(Book).filter(Book.format == format).all()
    logger.debug(f'Fetched {len(books)} book(s) with format {format}')
    return books
