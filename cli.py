import click
from sqlalchemy.orm import sessionmaker,Query
from models.user import User
from models.book import Book
from create_db import get_db_session
from .library_service import LibraryService

# Initialize the LibraryService with the session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=get_db_session())
library_service = LibraryService(SessionLocal())

#add borrowed book to a txt file
def add_borrowed_book_entry(book_name,borrow_date, return_date):
    #create the txt file on append mode
    with open('borrowed_books.txt', 'a') as file:
        #add info to be appended
        file.write(f"Book: {book_name}\n")
        file.write(f"Date Borrowed: {borrow_date}\n")
        file.write(f"Date Due for Return: {return_date}\n\n")