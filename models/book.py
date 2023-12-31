from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, Query
from models.base import Base
from models.borrowing import Borrowing 


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True,index = True)
    name = Column(String, index = True)
    genre = Column(String)
    num_pages = Column(Integer)
    author = Column(String)

    # Define relationships
    reviews = relationship('Review', back_populates='book')
    borrowings = relationship('Borrowing', back_populates='book')


    def __init__(self, name, genre, num_pages, author):
        self.name = name
        self.genre = genre
        self.num_pages = num_pages
        self.author = author

    @classmethod
    def list_all_books(cls,session):
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
    
    
