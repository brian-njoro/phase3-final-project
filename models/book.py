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