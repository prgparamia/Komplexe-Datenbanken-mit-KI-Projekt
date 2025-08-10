from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base,Session
from dbconfig import DATABASE_URL
from typing import Generator

# Fetch the database URL from the Config class

engine = create_engine(DATABASE_URL,echo=True)  


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
def get_db() -> Generator[Session,None,None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()