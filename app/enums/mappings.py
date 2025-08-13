from app.enums.category import Category
from app.enums.genre import Genre


GENRE_TO_CATEGORY = {
    Genre.FANTASY: Category.FICTION,
    Genre.SCI_FI: Category.FICTION,
    Genre.BIOGRAPHY: Category.NONFICTION,
    Genre.HISTORY: Category.NONFICTION,
}
