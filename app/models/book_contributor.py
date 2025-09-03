from sqlalchemy import Column, Integer, ForeignKey, Enum as SqlEnum
from sqlalchemy.orm import relationship
from app.db.database import Base
from app.enums.contributor_role import ContributorRole


class BookContributor(Base):
    __tablename__ = 'book_contributors'

    book_id = Column(Integer, ForeignKey('books.id'), primary_key=True)
    contributor_id = Column(Integer, ForeignKey('contributors.id'), primary_key=True)
    role = Column(SqlEnum(ContributorRole, name='contributor_role_enum'), nullable=False)

    book = relationship('Book', back_populates='contributors_assoc')
    contributor = relationship('Contributor', back_populates='books_assoc')
