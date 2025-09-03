from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.database import Base


class Contributor(Base):
    __tablename__ = 'contributors'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    books_assoc = relationship('BookContributor', back_populates='contributor')
    books = relationship('Book', secondary='book_contributors', back_populates='contributors')
    