import { useEffect, useState } from "react";
import axios from "axios";
import { Link } from "react-router-dom";
import "../styles/events.css"; // Import styles

export default function EventList() {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/events")
      .then((res) => setEvents(res.data))
      .catch((err) => console.error(err));
  }, []);

  return (
    <div className="events-page">
      <h1 className="events-title">Events</h1>
      <div style={{ textAlign: "center", marginBottom: "2rem" }}>
        <Link to="/create" className="create-event-link">
          + Create Event
        </Link>
      </div>

      <div className="events-grid">
        {events.map((event) => (
          <div key={event.id} className="event-card">
            <h2 className="event-title">{event.title}</h2>
            <p className="event-date">
              {new Date(event.start_datetime).toLocaleString()}
            </p>
            <Link to={`/rsvp/${event.id}`} className="rsvp-link">
              RSVP
            </Link>
          </div>
        ))}
      </div>
    </div>
  );
}
