from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base


from models.user import User
from models.book import Book
from models.review import Review
from models.borrowing import Borrowing

# Define  database URL
DATABASE_URL = "sqlite:///library.db"  

# Create the database engine
engine = create_engine(DATABASE_URL)

# Create the tables in the database
Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

def close_db_session():
    session.close()

def get_db_session():
    return session
