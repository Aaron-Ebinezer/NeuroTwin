import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Login from "./Components/LOGIN-AND-SIGNUP/Login";
import Signup from "./Components/LOGIN-AND-SIGNUP/Signup";
import ChatPage from "./Components/chatpage/ChatPage";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/signup" element={<Signup />} />
        <Route path="/chat" element={<ChatPage />} />
      </Routes>
    </Router>
  );
}

export default App;
