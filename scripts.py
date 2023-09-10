from models.book import Book
from cli import session
from models.user import User

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

     # Define user instances to add
    users_to_add = [
        User(name='John Doe', phone_number='123-456-7890', email='john.doe@example.com', age=30),
        User(name='Alice Smith', phone_number='234-567-8901', email='alice.smith@example.com', age=25),
        User(name='Bob Johnson', phone_number='345-678-9012', email='bob.johnson@example.com', age=40),
        User(name='Emily Wilson', phone_number='456-789-0123', email='emily.wilson@example.com', age=28),
        User(name='Michael Brown', phone_number='567-890-1234', email='michael.brown@example.com', age=35),
        User(name='Sophia Lee', phone_number='678-901-2345', email='sophia.lee@example.com', age=32),
        User(name='William Davis', phone_number='789-012-3456', email='william.davis@example.com', age=27),
        User(name='Olivia Martinez', phone_number='890-123-4567', email='olivia.martinez@example.com', age=29),
        User(name='James Garcia', phone_number='901-234-5678', email='james.garcia@example.com', age=33),
        User(name='Ava Rodriguez', phone_number='012-345-6789', email='ava.rodriguez@example.com', age=31),
        User(name='Liam Wilson', phone_number='112-233-4455', email='liam.wilson@example.com', age=30),
        User(name='Emma Anderson', phone_number='223-344-5566', email='emma.anderson@example.com', age=26),
        User(name='Noah Gonzalez', phone_number='334-455-6677', email='noah.gonzalez@example.com', age=34),
        User(name='Olivia Wilson', phone_number='445-566-7788', email='olivia.wilson@example.com', age=28),
        User(name='Isabella Lopez', phone_number='556-677-8899', email='isabella.lopez@example.com', age=29),
        User(name='Sophia Brown', phone_number='667-788-9900', email='sophia.brown@example.com', age=31),
        User(name='Jackson Martinez', phone_number='778-899-0011', email='jackson.martinez@example.com', age=35),
        User(name='Lucas Davis', phone_number='889-900-1122', email='lucas.davis@example.com', age=32),
        User(name='Henry Lee', phone_number='990-011-2233', email='henry.lee@example.com', age=27),
        User(name='Benjamin Wilson', phone_number='001-122-3344', email='benjamin.wilson@example.com', age=26)
    ]

except Exception as e:
    print(f"An error occurred: {e}")
    session.rollback()

finally:
    # Close the session
    session.close()
