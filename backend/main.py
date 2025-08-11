from typing import Union

from fastapi import FastAPI, Depends
# from pydantic import BaseModel

from sqlalchemy.orm import Session
from database import engine, get_db
from models import Base, Events, Rsvps
import os

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/events/")
def create_event(event:Events, db: Session = Depends(get_db)):
    new_event = Events(
        title = event.title,
        created_by = event.created_by,
        description = event.description,
        
        start_datetime = event.start_datetime,
        end_datetime = event.end_datetime,

        location = event.location,
        rsvp_description = event.rsvp_description
    )

    db.add(new_event)
    db.commit()
    db.refresh(new_event)
    return {"message": "Event created successfully", "event": new_event}

@app.post("/rsvp/")
def create_rsvp(rsvp: Rsvps, db: Session = Depends(get_db)): #MIGHT BE WRONG

    from models import Event, RSVP

    new_rsvp = Rsvps(
        id = rsvp.id,
        event_id = rsvp.event_id,
        name = rsvp.name,
        email = rsvp.email
    )

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
        <p>Hi {rsvp.email},</p>
        <p>Thank you for RSVPing to <strong>{event.title}</strong>.</p>
        <p><b>Date:</b> {event.date}</p>
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

    return {"message": "Rsvp created successfully", "Rsvp": new_rsvp}

