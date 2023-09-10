from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base

# Define  database URL
DATABASE_URL = "sqlite:///library.db"  

# Create the database engine
engine = create_engine(DATABASE_URL)

Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db_session():
    return SessionLocal()
