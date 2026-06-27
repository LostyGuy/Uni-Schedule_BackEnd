import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from backend.logging import log_info

DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL is None:
    log_info("Database URL is missing in connection.py")
    raise RuntimeError("DATABASE_URL environment variable is required")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()