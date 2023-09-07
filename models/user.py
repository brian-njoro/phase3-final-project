from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = (String)
    phone_number = Column(String, unique=True)
    email = Column(String, unique = True)
    age = Column(Integer)

    def __init__(self, name, phone_number, email, age):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.age = age

    def get_reviews(self):
        return [review.review_text for review in self.reviews]

    def get_borrowings(self):
        return [(borrowing.book.name, borrowing.borrow_date, borrowing.return_date) for borrowing in self.borrowings]
