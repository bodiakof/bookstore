from enum import Enum


class ContributorRole(str, Enum):
    AUTHOR = 'Author'
    TRANSLATOR = 'Translator'
    ILLUSTRATOR = 'Illustrator'
