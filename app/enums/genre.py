from enum import Enum


class Genre(str, Enum):
    FANTASY = 'fantasy'
    SCI_FI = 'sci-fi'
    HISTORY = 'history'
    BIOGRAPHY = 'biography'
