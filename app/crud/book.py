from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.book import Book
from app.schemas.book import BookCreate, BookUpdate
from app.utils.isbn import generate_fake_isbn


def get_books(db: Session):
    '''Return all books from the database.'''
    return db.query(Book).all()

def get_book(db: Session, book_id: int):
    '''Fetch a single book by ID or raise 404.'''
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail='Book not found')
    return book

def create_books(db: Session, book: BookCreate | list[BookCreate]):
    '''
    Create one or multiple book entries.
    - If 'book' is a single BookCreate, create one book.
    - If 'book' is a list of BookCreate, create multiple books.
    '''
    if isinstance(book, list):
        db_books = []
        for b in book:
            data = b.model_dump()
            if not data.get('isbn'):
                data['isbn'] = generate_fake_isbn()
            db_books.append(Book(**data))

        db.add_all(db_books)
        db.commit()
        for db_book in db_books:
            db.refresh(db_book)
        return db_books
    else:
        data = book.model_dump()
        if not data.get('isbn'):
            data['isbn'] = generate_fake_isbn()
        db_book = Book(**data)
        db.add(db_book)
        try:
            db.commit()
        except IntegrityError:
            db.rollback()
            raise HTTPException(status_code=400, detail='Book with this ISBN already exists.')


        db.refresh(db_book)
        return db_book

def update_book(db: Session, book_id: int, book_data: dict):
    '''
    Update an existing book with provided data.
    - book_data: dict containing only the fields to update.
    '''
    book = get_book(db, book_id)
    for key, value in book_data.items():
        setattr(book, key, value)

    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail='Book with this ISBN already exists.')
    
    db.refresh(book)
    return book

def delete_book(db: Session, book_id: int):
    '''Delete a book by ID.'''
    book = get_book(db, book_id)
    db.delete(book)
    db.commit()
    return {'detail': 'Book was successfully deleted'}

def get_books_by_format(db: Session, format: str):
    '''Return all books of specified format.'''
    return db.query(Book).filter(Book.format == format).all()
