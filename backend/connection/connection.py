import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from backend.logging import log_info


def _get_environmental_variables(name: str) -> str:
    
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Required environmental value '{name}' is not set")
    
    return value

DATABASE_URL = _get_environmental_variables("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()