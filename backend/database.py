# SQLite database connection 
from sqlalchemy import create_engine
from models import Base
from sqlalchemy.orm import sessionmaker

# database setup
engine = create_engine('sqlite:///backend/calendarlink.db', echo=True)
# Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(engine)

#Session uses Engine to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency function
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()