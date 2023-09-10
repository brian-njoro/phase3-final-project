from models.user import User
from cli import session

try:
   
    # Define user instances to add
    users_to_add = [
        User(name='John Doe', phone_number='123-456-7890', email='john.doe@example.com', age=30),
        User(name='Alice Smith', phone_number='234-567-8901', email='alice.smith@example.com', age=25),
        User(name='Bob Johnson', phone_number='345-678-9012', email='bob.johnson@example.com', age=40),
        User(name='Emily Wilson', phone_number='456-789-0123', email='emily.wilson@example.com', age=28),
        User(name='Michael Brown', phone_number='567-890-1234', email='michael.brown@example.com', age=35),
        User(name='Sophia Lee', phone_number='678-901-2345', email='sophia.lee@example.com', age=32),
        User(name='Brian Njoroge', phone_number='789-012-3456', email='william.davis@example.com', age=27),
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

    # Add users to the session
    for user in users_to_add:
        session.add(user)

    # Commit changes to the database
    session.commit()
    print("Users added successfully!")

except Exception as e:
    print(f"An error occurred: {e}")
    session.rollback()

finally:
    # Close the session
    session.close()