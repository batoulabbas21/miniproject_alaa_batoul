import React from "react";
import { useNavigate } from "react-router-dom";
import { FaRocket, FaBrain, FaShieldAlt, FaFileMedical } from "react-icons/fa";

const Landing = () => {
  const navigate = useNavigate();

  return (
    <div style={styles.page}>
      <div style={styles.card}>
        <div style={styles.iconRow}>
          <FaBrain size={60} color="#007BFF" />
          <FaFileMedical size={60} color="#007BFF" style={{ margin: "0 20px" }} />
          <FaShieldAlt size={60} color="#007BFF" />
        </div>
        <h1 style={styles.title}>Welcome to</h1>
        <h2 style={styles.titleHighlight}>Medical Report Analyzer</h2>
        <p style={styles.subtitle}>
          Upload your medical report and get AI-powered summaries and risk analysis instantly.
        </p>
        <button style={styles.button} onClick={() => navigate("/home")}>
          <FaRocket style={{ marginRight: "8px" }} />
          Start Analyzing
        </button>
      </div>
    </div>
  );
};

const styles = {
  page: {
    minHeight: "100vh",
    backgroundColor: "#f2f9ff",
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    padding: "2rem",
  },
  card: {
    textAlign: "center",
    background: "#ffffff",
    padding: "3rem",
    borderRadius: "20px",
    boxShadow: "0 10px 25px rgba(0, 123, 255, 0.1)",
    maxWidth: "600px",
    width: "100%",
  },
  iconRow: {
    display: "flex",
    justifyContent: "center",
    marginBottom: "1rem",
  },
  title: {
    fontSize: "1.75rem",
    color: "#333",
    margin: "0.5rem 0",
  },
  titleHighlight: {
    fontSize: "2rem",
    color: "#007BFF",
    marginBottom: "1rem",
    fontWeight: "bold",
  },
  subtitle: {
    fontSize: "1rem",
    color: "#555",
    marginBottom: "2rem",
  },
  button: {
    backgroundColor: "#007BFF",
    color: "#fff",
    fontSize: "1.1rem",
    padding: "0.75rem 1.5rem",
    border: "none",
    borderRadius: "12px",
    cursor: "pointer",
    display: "flex",
    alignItems: "center",
    margin: "0 auto",
    boxShadow: "0 5px 15px rgba(0, 123, 255, 0.3)",
  },
};

export default Landing;
