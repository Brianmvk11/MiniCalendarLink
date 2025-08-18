import { useEffect, useState } from "react";
import axios from "axios";
import "../styles/events.css";

export default function EventList() {
  const [events, setEvents] = useState([]);
  const [expandedEvent, setExpandedEvent] = useState(null); // to show details
  const [rsvpStatus, setRsvpStatus] = useState({});
  const [formData, setFormData] = useState({ name: "", email: "" });

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/events")
      .then((res) => setEvents(res.data))
      .catch((err) => console.error(err));
  }, []);

  const handleExpand = (eventId) => {
    setExpandedEvent(expandedEvent === eventId ? null : eventId);
  };

  const handleRSVPSubmit = (eventId) => {

    if (!formData.name || !formData.email || !rsvpStatus[eventId]) {
    alert("Please fill in all fields and choose an RSVP option.");
    return; // Stop here if validation fails
    }

    axios
      .post(`http://127.0.0.1:8000/rsvp`, {
        event_id: eventId,
        name: formData.name,
        email: formData.email,
        rsvp_status: rsvpStatus[eventId]    
      })
      .then(() => {
        alert("RSVP successful! Check the generated HTML file.");
        setFormData({ name: "", email: "" });
        setRsvpStatus({ ...rsvpStatus, [eventId]: "" });
      })
      .catch((err) => console.error(err));
  };

  return (
    <div className="events-page">
      <h1 className="events-title">Events</h1>

      <div style={{ textAlign: "center", marginBottom: "2rem" }}>
        <a href="/create" className="create-event-link">
          + Create Event
        </a>
      </div>

      <div className="events-grid">
        {events.map((event) => (
          <div key={event.id} className="event-card">
            <h2
              className="event-title"
              style={{ cursor: "pointer" }}
              onClick={() => handleExpand(event.id)}
            >
              {event.title}
            </h2>
            <p className="event-date">
              {new Date(event.start_datetime).toLocaleString()}
            </p>

            {expandedEvent === event.id && (
              <>
                <p><b>Location:</b> {event.location}</p>
                <p><b>Description:</b> {event.description}</p>

                <label>
                  RSVP:
                  <select
                    value={rsvpStatus[event.id] || ""}
                    onChange={(e) =>
                      setRsvpStatus({ ...rsvpStatus, [event.id]: e.target.value })
                    }
                  >
                    <option value="">Select</option>
                    <option value="Yes">Yes</option>
                    <option value="Maybe">Maybe</option>
                    <option value="No">No</option>
                  </select>
                </label>

                {["Yes", "Maybe", "No"].includes(rsvpStatus[event.id]) && (
                  <div style={{ marginTop: "1rem" }}>
                    <input
                      type="text"
                      placeholder="Your name"
                      value={formData.name}
                      onChange={(e) =>
                        setFormData({ ...formData, name: e.target.value })
                      }
                      style={{ display: "block", marginBottom: "0.5rem" }}
                    />
                    <input
                      type="email"
                      placeholder="Your email"
                      value={formData.email}
                      onChange={(e) =>
                        setFormData({ ...formData, email: e.target.value })
                      }
                      style={{ display: "block", marginBottom: "0.5rem" }}
                    />
                    <button onClick={() => handleRSVPSubmit(event.id)}>
                      Submit RSVP
                    </button>
                  </div>
                )}
              </>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}
