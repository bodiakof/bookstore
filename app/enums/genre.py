from enum import Enum


class Genre(str, Enum):
    FANTASY = 'fantasy'
    SCI_FI = 'sci-fi'
    MYTHOLOGY = 'mythology'
    MAGICAL_REALISM = 'magical realism'
    HORROR = 'horror'
    DYSTOPIAN = 'dystopian'
    CLASSIC = 'classic'
    THRILLER = 'thriller'
    MYSTERY = 'mystery'
    EPIC_POETRY = 'epic poetry'

    HISTORY = 'history'
    BIOGRAPHY = 'biography'
    MEMOIR = 'memoir'
    SELF_HELP = 'self-help'
    PSYCHOLOGY = 'psychology'
    PHILOSOPHY = 'philosophy'
    SCIENCE = 'science'
