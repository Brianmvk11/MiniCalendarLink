import { useParams, useNavigate } from "react-router-dom";
import { useState } from "react";
import axios from "axios";

export default function RSVP() {
  const { event_id } = useParams();
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const navigate = useNavigate();

  const handleRSVP = (e) => {
    e.preventDefault();
    axios.post(`http://127.0.0.1:8000/rsvp`, { event_id, name, email })
      .then(() => {
        alert("RSVP successful! Check the generated HTML file.");
        navigate("/");
      })
      .catch(err => console.error(err));
  };

return (
    <form onSubmit={handleRSVP}>
      <h1>RSVP</h1>

      <input
        type="text"
        value={name}
        onChange={e => setName(e.target.value)}
        placeholder="Your name"
        required
      />

      <input
        type="email"
        value={email}
        onChange={e => setEmail(e.target.value)}
        placeholder="Your email"
        required
      />

      <button type="submit">RSVP</button>
    </form>
  );
}
