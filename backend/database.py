# SQLite database connection 
from sqlalchemy import create_engine

engine = create_engine('sqlite:///calendarlink.db', echo=True)