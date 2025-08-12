from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

# Shared properties for Event
class EventBase(BaseModel):
    title: str
    created_by: str
    description: Optional[str] = None
    start_datetime: datetime
    end_datetime: datetime
    location: str
    rsvp_description: Optional[str] = None

# Request body for creating an event
class EventCreate(EventBase):
    pass

# Response model for Event (includes ID)
class EventResponse(EventBase):
    id: int

    class Config:
        orm_mode = True  # Allows Pydantic to read SQLAlchemy objects


# Shared properties for RSVP
class RsvpBase(BaseModel):
    event_id: int
    name: str
    email: EmailStr

class RsvpCreate(RsvpBase):
    pass

class RsvpResponse(RsvpBase):
    id: int

    class Config:
        orm_mode = True
