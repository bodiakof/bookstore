from app.enums.category import Category
from app.enums.genre import Genre


GENRE_TO_CATEGORY = {
    Genre.FANTASY: Category.FICTION,
    Genre.SCI_FI: Category.FICTION,
    Genre.MYTHOLOGY: Category.FICTION,
    Genre.MAGICAL_REALISM: Category.FICTION,
    Genre.HORROR: Category.FICTION,
    Genre.DYSTOPIAN: Category.FICTION,
    Genre.CLASSIC: Category.FICTION,
    Genre.THRILLER: Category.FICTION,
    Genre.MYSTERY: Category.FICTION,
    Genre.EPIC_POETRY: Category.FICTION,
    Genre.BIOGRAPHY: Category.NONFICTION,
    Genre.HISTORY: Category.NONFICTION,
    Genre.MEMOIR: Category.NONFICTION,
    Genre.SELF_HELP: Category.NONFICTION,
    Genre.PSYCHOLOGY: Category.NONFICTION,
    Genre.PHILOSOPHY: Category.NONFICTION,
    Genre.SCIENCE: Category.NONFICTION,
}
