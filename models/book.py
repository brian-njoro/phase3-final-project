from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True,index = True)
    name = Column(String, index = True)
    genre = Column(String)
    num_pages = Column(Integer)
    author = Column(String)

    def __init__(self, name, genre, num_pages, author):
        self.name = name
        self.genre = genre
        self.num_pages = num_pages
        self.author = author

    @classmethod
    def list_all_books(cls,session):
        from create_db import get_db_session
        session = get_db_session
        all_books = session.query(cls).all()
        book_list = []

        for book in all_books:
            book_dict = {
                'name': book.name,
                'author': book.author,
                'genre': book.genre,
                'num_pages': book.num_pages
            }
            book_list.append(book_dict)
        return book_list