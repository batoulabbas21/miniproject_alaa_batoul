import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Landing from "./pages/Landing";
import Home from "./pages/Home";
import Recommendations from "./pages/Recommendations";
import Analytics from "./pages/Analytics";
import NavigationPage from "./pages/NavigationPage";

const Navbar = () => (
  <nav style={{
    background: "#007BFF",
    padding: "1rem",
    display: "flex",
    gap: "1rem",
    justifyContent: "center",
    fontFamily: "'Segoe UI', Tahoma, Geneva, Verdana, sans-serif"
  }}>
    <Link style={{ color: "white" }} to="/">Landing</Link>
    <Link style={{ color: "white" }} to="/navigate">Navigate</Link>
    <Link style={{ color: "white" }} to="/home">Home</Link>
    <Link style={{ color: "white" }} to="/recommendations">Recommendations</Link>
    <Link style={{ color: "white" }} to="/analytics">Analytics</Link>
  </nav>
);

function App() {
  return (
    <Router>
      <Navbar />
      <div style={{
        fontFamily: "'Segoe UI', Tahoma, Geneva, Verdana, sans-serif",
        textAlign: "center",
        padding: "2rem"
      }}>
        <Routes>
          <Route path="/" element={<Landing />} />
          <Route path="/navigate" element={<NavigationPage />} />
          <Route path="/home" element={<Home />} />
          <Route path="/recommendations" element={<Recommendations />} />
          <Route path="/analytics" element={<Analytics />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
