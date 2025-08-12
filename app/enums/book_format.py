from enum import Enum


class BookFormat(str, Enum):
    PAPERBACK = 'paperback'
    HARDCOVER = 'hardcover'
    EBOOK = 'ebook'
