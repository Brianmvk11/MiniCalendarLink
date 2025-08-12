import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import CreateEvent from "./pages/create_event";
import EventList from "./pages/events";
import RSVP from "./pages/rsvp";

ReactDOM.createRoot(document.getElementById("root")).render(
  <BrowserRouter>
    <Routes>
      <Route path="/" element={<EventList />} />
      <Route path="/create" element={<CreateEvent />} />
      <Route path="/rsvp/:eventId" element={<RSVP />} />
    </Routes>
  </BrowserRouter>
);