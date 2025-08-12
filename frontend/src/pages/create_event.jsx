import { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

export default function CreateEvent() {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [start_datetime, setStart] = useState("");
  const [end_datetime, setEnd] = useState("");
  const [location, setLocation] = useState("");
  const [rsvp_description, setRsvpDescription] = useState("");
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    axios.post("http://127.0.0.1:8000/events", { 
      title, 
      description, 
      start_datetime: new Date(start_datetime).toISOString(),
      end_datetime: new Date(end_datetime).toISOString(), 
      location, 
      rsvp_description   
    })
      .then(() => navigate("/"))
      .catch(err => console.error(err));
  };

  return (
    <form onSubmit={handleSubmit}>
      <h1>Create Event</h1>

      <input 
        type="text" 
        value={title} 
        onChange={e => setTitle(e.target.value)} 
        placeholder="Title" 
        required 
      />

      <textarea
        value={description}
        onChange={e => setDescription(e.target.value)}
        placeholder="Description"
        required
      />

      <label>
        Start Date & Time:
        <input 
          type="datetime-local" 
          value={start_datetime} 
          onChange={e => setStart(e.target.value)} 
          required 
        />
      </label>

      <label>
        End Date & Time:
        <input 
          type="datetime-local" 
          value={end_datetime} 
          onChange={e => setEnd(e.target.value)} 
          required 
        />
      </label>

      <input 
        type="text" 
        value={location} 
        onChange={e => setLocation(e.target.value)} 
        placeholder="Location" 
        required 
      />

      <textarea
        value={rsvp_description}
        onChange={e => setRsvpDescription(e.target.value)}
        placeholder="RSVP Description"
      />

      <button type="submit">Create</button>
    </form>
  );
}
