import React, { useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import "./ChatPage.css";

export default function ChatPage() {
  const location = useLocation();
  const navigate = useNavigate();
  const user = location.state?.user || "Guest";

  const [messages, setMessages] = useState([
    { sender: "bot", text: "👋 Hi there! I'm your fun chat buddy. How can I help today?" }
  ]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const newMessages = [...messages, { sender: "user", text: input }];
    setMessages(newMessages);

    const userMessage = input;
    setInput("");
    setLoading(true);

    try {

      const res = await fetch(`http://localhost:8000/ask?question=${encodeURIComponent(userMessage)}`, {
                    method: "POST"
                    });


      if (!res.ok) {
        throw new Error("Failed to get response");
      }

      const data = await res.json();

      setMessages((prev) => [
        ...prev,
        { sender: "bot", text: data.answer }
      ]);

    } catch (error) {
      console.error(error);
      setMessages((prev) => [
        ...prev,
        { sender: "bot", text: "⚠️ Sorry, something went wrong." }
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="chat-container">
      <div className="chat-header">
        <div className="header-left">
          <img
            src="https://cdn-icons-png.flaticon.com/512/4712/4712100.png"
            alt="Bot Avatar"
            className="bot-avatar"
          />
          <span>Welcome, {user}!</span>
        </div>
        <button onClick={() => navigate("/")}>🚪 Logout</button>
      </div>

      <div className="chat-messages">
        {messages.map((msg, i) => (
          <div key={i} className={`message ${msg.sender}`}>
            {msg.text}
          </div>
        ))}
        {loading && (
          <div className="message bot">⏳ Thinking...</div>
        )}
      </div>

      <div className="chat-input">
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="💬 Type your message..."
          onKeyDown={(e) => e.key === "Enter" && sendMessage()}
        />
        <button onClick={sendMessage}>📤 Send</button>
      </div>
    </div>
  );
}
