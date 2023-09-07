import datetime
from sqlalchemy.orm import Session
from models.user import User
from models.book import Book
from models.borrowing import Borrowing

class LibraryService:
    def __init__(self, session: Session):
        self.session = session

    def borrow_book(self, user: User, book: Book) -> Borrowing:
        # Check if a user has already borrowed the book
        existing_borrowing = self.session.query(Borrowing).filter(
            Borrowing.user_id == user.id,
            Borrowing.book_id == book.id,
            Borrowing.return_date >= datetime.date.today()
        ).first()

        if existing_borrowing:
            raise ValueError(f"{user.name} has already borrowed '{book.name}'.")

        # Calculate the return date (6 weeks from day of borrowing)
        return_date = datetime.date.today() + datetime.timedelta(weeks=6)

        # Create a new Borrowing record
        borrowing = Borrowing(user_id=user.id, book_id=book.id, borrow_date=datetime.date.today(), return_date=return_date)
        
        # Add the borrowing record to the database
        self.session.add(borrowing)
        self.session.commit()

        return borrowing
