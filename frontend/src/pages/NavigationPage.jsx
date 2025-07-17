import React from "react";
import { useNavigate } from "react-router-dom";
import { FaHome, FaChartPie, FaLightbulb } from "react-icons/fa";

const NavigationPage = () => {
  const navigate = useNavigate();

  return (
    <div style={{ padding: "3rem", textAlign: "center", background: "#f2f9ff", minHeight: "100vh" }}>
      <h1 style={{ fontSize: "2rem", color: "#007BFF", marginBottom: "2rem" }}>📂 Choose Where to Go</h1>
      <div style={{ display: "flex", justifyContent: "center", gap: "2rem", flexWrap: "wrap" }}>
        <button onClick={() => navigate("/home")} style={buttonStyle}><FaHome /> Home</button>
        <button onClick={() => navigate("/analytics")} style={buttonStyle}><FaChartPie /> Analytics</button>
        <button onClick={() => navigate("/recommendations")} style={buttonStyle}><FaLightbulb /> Recommendations</button>
      </div>
    </div>
  );
};

const buttonStyle = {
  padding: "1rem 2rem",
  borderRadius: "12px",
  backgroundColor: "#ffffff",
  color: "#007BFF",
  border: "2px solid #007BFF",
  cursor: "pointer",
  fontSize: "1.1rem",
  display: "flex",
  alignItems: "center",
  gap: "0.5rem",
  boxShadow: "0 5px 15px rgba(0, 123, 255, 0.1)",
};

export default NavigationPage;
