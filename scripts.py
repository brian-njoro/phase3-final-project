from models.book import Book
from cli import session

try:
   
    # Define book instances to add
    books_to_add = [
        Book(name='ASOIAF', genre='Fiction', num_pages=300, author='George R.R Martin'),
        Book(name='Under the dome', genre='Mystery', num_pages=250, author='Stephen King'),
        Book(name='Interstellar', genre='Science Fiction', num_pages=400, author='Christopher Nolan'),
        Book(name='Lord of the rings', genre='Fantasy', num_pages=350, author='John Ronald Tolkien'),
        Book(name='Romeo and Juliet', genre='Romance', num_pages=200, author='Wiliam shakespear'),
        Book(name='gone girl', genre='Mystery', num_pages=280, author='Gilian Flynn'),
        Book(name='Handmaids tale', genre='Fiction', num_pages=320, author='Margaret Atwood'),
        Book(name='hyperion', genre='Science Fiction', num_pages=450, author='Dan Simmons'),
        Book(name='Alice in wonderland', genre='Fantasy', num_pages=380, author='Lewis Carroll'),
        Book(name='Outlander', genre='Romance', num_pages=220, author='Diana Gabaldon'),
        Book(name='In the woods', genre='Mystery', num_pages=300, author='Tana French'),
        Book(name='Great gatsby', genre='Fiction', num_pages=340, author='F. Scott Fitzgerald'),
        Book(name='Dune', genre='Science Fiction', num_pages=420, author='Frank Herbert'),
        Book(name='wizard of oz', genre='Fantasy', num_pages=360, author='L. Frank Baum'),
        Book(name='Hamlet', genre='Romance', num_pages=240, author='Wiliam Shakespear'),
    ]

    # Add books to the session
    for book in books_to_add:
        session.add(book)

    # Commit changes to the database
    session.commit()
    print("Books added successfully!")

except Exception as e:
    print(f"An error occurred: {e}")
    session.rollback()

finally:
    # Close the session
    session.close()