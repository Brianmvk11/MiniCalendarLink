from typing import List

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel

from sqlalchemy.orm import Session
from database import engine, get_db
from models import Base, Events, Rsvps
import os
import schemas

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Allow React dev server to talk to FastAPI since running on different ports
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # where your frontend runs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/events", response_model=List[schemas.EventResponse])
def get_events(db: Session = Depends(get_db)):
    events = db.query(Events).all()
    return events

@app.post("/events", response_model=schemas.EventResponse)
def create_event(event: schemas.EventCreate, db: Session = Depends(get_db)):
    new_event = Events(**event.model_dump())

    db.add(new_event)
    db.commit()
    db.refresh(new_event)
    return new_event

@app.post("/rsvp", response_model=schemas.RsvpResponse)
def create_rsvp(rsvp: schemas.RsvpCreate, db: Session = Depends(get_db)):

    # from models import Events, RSVP

    #Get event 
    event = db.query(Events).filter(Events.id == rsvp.event_id).first()
    if not event:
        return {"error": "Event not found"}
    
    new_rsvp = Rsvps(**rsvp.model_dump())

    db.add(new_rsvp)
    db.commit()
    db.refresh(new_rsvp)

    # Create email folder if not exists
    os.makedirs("emails", exist_ok=True)

    # Simulate email HTML
    email_content = f"""
    <html>
    <body>
        <h2>Event Confirmation</h2>
        <p>Hi {rsvp.name},</p>
        <p>Thank you for RSVPing to <strong>{event.title}</strong>.</p>
        <p><b>Date:</b> {event.start_datetime}</p>
        <p><b>Location:</b> {event.location}</p>
        <p>{event.description}</p>
        <hr>
        <p>We look forward to seeing you!</p>
    </body>
    </html>
    """

    # Save to file
    filename = f"emails/{rsvp.email.replace('@', '_at_')}_{event.id}.html"
    with open(filename, "w") as f:
        f.write(email_content)

    return new_rsvp

# @app.get("/events")
# def get_events():
#     return [{"id": 1, "title": "Test Event"}]


