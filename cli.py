import click
from sqlalchemy.orm import sessionmaker,Query
from models.user import User
from models.book import Book
from create_db import get_db_session
from library_service import LibraryService

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


@click.group()
def main():
    pass

@main.command()
def list_books():
    """List all available books."""
    books = Book.list_all_books()
    for book in books:
        print(book)

@main.command()
@click.option('--user-id', prompt='Enter user ID', type=int)
@click.option('--book-id', prompt='Enter book ID', type=int)
def borrow_book(user_id, book_id):
    """Borrow a book."""
    user = User.query.get(user_id)
    book = Book.query.get(book_id)
    borrow_date = '2023-09-10'  
    return_date = '2023-10-10'  
    library_service.borrow_book(user, book)
    
    # Add the borrowed book entry to borrowed_books.txt
    add_borrowed_book_entry(book.name, borrow_date, return_date)
    
    # Print a successful borrowing message
    print(f"Borrowed '{book.name}' on {borrow_date}. Return by {return_date}")

if __name__ == '__main__':
    main()