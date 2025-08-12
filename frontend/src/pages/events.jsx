import { useEffect, useState } from "react";
import axios from "axios";
import { Link } from "react-router-dom";

export default function EventList() {
    //Connecting to the backend
    const [events, setEvents] = useState([]);
  
    useEffect(() => {
        axios.get("http://127.0.0.1:8000/events")
        .then(res => setEvents(res.data))
        .catch(err => console.error(err));
    }, []);

  return (
    <div>
      <h1>Events</h1>
      <Link to="/create">Create Event</Link>
      <ul>
        {events.map(event => (
          <li key={event.id}>
            {event.title} - {event.date}
            <Link to={`/rsvp/${event.id}`}> RSVP </Link>
          </li>
        ))}
      </ul>
    </div>
  );
}