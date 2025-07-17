import React, { useState } from "react";
import { uploadFile, exportReport } from "../api";
import UploadForm from "../components/UploadForm";
import { FaBrain, FaShieldAlt, FaFileMedical, FaFileDownload } from "react-icons/fa";

function Home() {
  const [result, setResult] = useState(null);
  const [reportId, setReportId] = useState(null);

  const handleUpload = async (file) => {
    const res = await uploadFile(file);
    setResult(res);
    const reports = await fetch("http://127.0.0.1:8000/analyze/reports/");
    const all = await reports.json();
    setReportId(all[all.length - 1].id);
  };

  const handleDownload = async () => {
    const blob = await exportReport(reportId);
    const url = window.URL.createObjectURL(new Blob([blob]));
    const link = document.createElement("a");
    link.href = url;
    link.setAttribute("download", `summary_${reportId}.pdf`);
    document.body.appendChild(link);
    link.click();
    link.remove();
  };

  return (
    <div style={{ fontFamily: "Segoe UI", backgroundColor: "#f2f9ff", minHeight: "100vh" }}>
      {/* Header Section */}
      <div style={{
        textAlign: "center",
        padding: "3rem 1rem 2rem",
        background: "linear-gradient(to right, #009FFD, #2A2A72)",
        color: "#fff",
        borderBottomLeftRadius: "40px",
        borderBottomRightRadius: "40px"
      }}>
        <div style={{ fontSize: "3rem", marginBottom: "1rem" }}>
          <FaBrain style={{ margin: "0 0.5rem" }} />
          <FaFileMedical style={{ margin: "0 0.5rem" }} />
          <FaShieldAlt style={{ margin: "0 0.5rem" }} />
        </div>
        <h1 style={{ fontSize: "2.5rem", marginBottom: "0.3rem" }}>Medical Report Analyzer</h1>
        <p style={{ fontSize: "1.1rem", opacity: 0.9 }}>AI-powered summarization and risk detection</p>
      </div>

      {/* Upload and Result Section */}
      <div style={{ padding: "2rem", maxWidth: "800px", margin: "auto" }}>
        <UploadForm onUpload={handleUpload} />

        {result && (
          <div style={{
            marginTop: "2.5rem",
            padding: "2rem",
            borderRadius: "20px",
            backgroundColor: "#ffffff",
            boxShadow: "0 10px 25px rgba(0, 0, 0, 0.1)"
          }}>
            <h3 style={{ marginBottom: "1rem", fontSize: "1.4rem", color: "#007BFF" }}>
              🧠 <strong>Summary</strong>
            </h3>
            <p>{result.summary}</p>

            <h3 style={{ marginTop: "2rem", marginBottom: "1rem", fontSize: "1.4rem", color: "#007BFF" }}>
              🚩 <strong>Risk Flags</strong>
            </h3>
            <ul style={{ paddingLeft: "1.2rem" }}>
              {result.flags.map((f, i) => (
                <li key={i}>{f}</li>
              ))}
            </ul>

            <button
              onClick={handleDownload}
              style={{
                marginTop: "2rem",
                padding: "0.8rem 1.5rem",
                backgroundColor: "#007BFF",
                color: "#fff",
                border: "none",
                borderRadius: "10px",
                fontSize: "1rem",
                cursor: "pointer",
                display: "flex",
                alignItems: "center",
                gap: "0.5rem",
                boxShadow: "0 5px 15px rgba(0, 123, 255, 0.3)"
              }}
            >
              <FaFileDownload /> Download Summary PDF
            </button>
          </div>
        )}
      </div>
    </div>
  );
}

export default Home;
