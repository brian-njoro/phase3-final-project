from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship, Query
from .base import Base

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    book_id = Column(Integer, ForeignKey('books.id'))
    review_text = Column(String)
    rating = Column(Float)

    def __init__(self, user_id, book_id, review_text):
        self.user_id = user_id
        self.book_id = book_id
        self.review_text = review_text

    @classmethod
    def get_average_rating(cls, book_id):
        ratings = [review.rating for review in cls.query.filter_by(book_id=book_id).all()]
        if ratings:
            return sum(ratings) / len(ratings)
        else:
            return 0.0
        
     # Define relationships
    user = relationship('User', back_populates='reviews')
    book = relationship('Book', back_populates='reviews')

    from models.book import Book
    
