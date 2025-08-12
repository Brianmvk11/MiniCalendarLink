# defines what my tables will look like
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String, DateTime
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
import datetime

class Base(DeclarativeBase):
    pass

class Events(Base):
    '''
    The table for the information on the different events created
    '''
    __tablename__ = "events"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    # created_by: Mapped[str] = mapped_column(String(50))
    description: Mapped[Optional[str]]
    
    start_datetime: Mapped[datetime.datetime] = mapped_column(DateTime)
    end_datetime: Mapped[datetime.datetime] = mapped_column(DateTime)

    location: Mapped[str] = mapped_column(String(100))
    rsvp_description: Mapped[Optional[str]]

    def __repr__(self) -> str: # for debugging
        return f"Events(id={self.id!r}, title={self.title!r}, created_by ={self.created_by!r}, start_datetime={self.start_datetime!r}, end_datetime={self.end_datetime!r}, location={self.location!r})"
    
class Rsvps(Base):
    '''
    The table for the information on the rsvps made for the event
    '''
    __tablename__ = "rsvps"

    id: Mapped[int] = mapped_column(primary_key=True)
    event_id: Mapped[int] = mapped_column(ForeignKey("events.id"))
    name: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(50))

    def __repr__(self) -> str: # for debugging
        return f"Rsvps(id={self.id!r}, event_id={self.event_id!r}, name={self.name!r}, email={self.email!r})"
    