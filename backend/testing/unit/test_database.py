import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Testengine = create_engine('postgresql://postgres:postgres@localhost:15432/postgres')
TestSessionLocal = sessionmaker(bind=Testengine, autoflush=False, autocommit=False)

def get_db():
    """
    Provide a test database session with automatic cleanup.
    
    Yields:
        SQLAlchemy session for database operations in tests.
    """
    Testdb = TestSessionLocal()
    try:
        yield Testdb
    finally:
        Testdb.close()

