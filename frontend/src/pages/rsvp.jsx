import { useParams, useNavigate } from "react-router-dom";
import { useState } from "react";
import axios from "axios";
import "../styles/rsvp.css"; // Import styles

export default function RSVP() {
  const { event_id } = useParams();
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const navigate = useNavigate();

  const handleRSVP = (e) => {
    e.preventDefault();
    axios
      .post(`http://127.0.0.1:8000/rsvp`, { event_id, name, email })
      .then(() => {
        alert("RSVP successful! Check the generated HTML file.");
        navigate("/");
      })
      .catch((err) => console.error(err));
  };

  return (
    <div className="rsvp-container">
      <form onSubmit={handleRSVP} className="rsvp-form">
        <h1 className="rsvp-title">RSVP</h1>

        <input
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
          placeholder="Your name"
          required
          className="rsvp-input"
        />

        <input
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          placeholder="Your email"
          required
          className="rsvp-input"
        />

        <button type="submit" className="rsvp-button">
          RSVP
        </button>
      </form>
    </div>
  );
}
