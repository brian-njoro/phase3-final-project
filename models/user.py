from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship,Query
from models.base import Base
from models.review import Review

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index = True)
    phone_number = Column(String, unique=True)
    email = Column(String, unique = True)
    age = Column(Integer)

    def __init__(self, name, phone_number, email, age):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.age = age

    def get_reviews(self):
        from review import Review
        return [review.review_text for review in self.reviews]

    def get_borrowings(self):
        from book import Book
        from borrowing import Borrowing
        return [(borrowing.book.name, borrowing.borrow_date, borrowing.return_date) for borrowing in self.borrowings]
    
    # Define relationships
    reviews = relationship('Review', back_populates='user')
    borrowings = relationship('Borrowing', back_populates='user')
