from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Borrowing(Base):
    __tablename__ = 'borrowings'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    book_id = Column(Integer, ForeignKey('books.id'))
    borrow_date = Column(Date)
    return_date = Column(Date)

    def __init__(self, user_id, book_id, borrow_date, return_date):
        self.user_id = user_id
        self.book_id = book_id
        self.borrow_date = borrow_date
        self.return_date = return_date
