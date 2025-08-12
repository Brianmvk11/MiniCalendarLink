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
    <body style="font-family: Arial, sans-serif; background-color: #f0f8ff; margin: 0; padding: 20px;">
        <table width="100%" cellpadding="0" cellspacing="0" style="max-width: 600px; margin: auto; background: white; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 10px rgba(0,0,0,0.1);">
        <tr>
            <td style="background-color: #2563eb; padding: 15px; text-align: center; color: white; font-size: 20px; font-weight: bold;">
            Event Confirmation
            </td>
        </tr>
        <tr>
            <td style="padding: 20px; color: #333;">
            <p style="font-size: 16px;">Hi {rsvp.name},</p>
            <p style="font-size: 16px;">Thank you for RSVPing to <strong style="color: #2563eb;">{event.title}</strong>.</p>
            
            <p style="font-size: 15px; margin: 10px 0;">
                <b>Date:</b> {event.start_datetime}<br>
                <b>Location:</b> {event.location}
            </p>
            
            <p style="font-size: 15px; color: #555;">{event.description}</p>
            
            <hr style="border: none; height: 1px; background-color: #ddd; margin: 20px 0;">
            
            <p style="font-size: 15px;">We look forward to seeing you!</p>
            </td>
        </tr>
        <tr>
            <td style="background-color: #f3f4f6; padding: 10px; text-align: center; font-size: 13px; color: #777;">
            © {event.title} | Event Management System
            </td>
        </tr>
        </table>
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


