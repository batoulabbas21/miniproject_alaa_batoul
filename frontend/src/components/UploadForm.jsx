import React, { useRef } from "react";

function UploadForm({ onUpload }) {
  const inputRef = useRef();

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    if (file) onUpload(file);
  };

  const handleClick = () => {
    inputRef.current.click();
  };

  return (
    <div style={{ textAlign: "center", marginTop: "2rem" }}>
      {/* Hidden file input */}
      <input
        type="file"
        accept=".pdf,.txt"
        ref={inputRef}
        onChange={handleFileChange}
        style={{ display: "none" }}
      />

      {/* Custom button */}
      <button
        onClick={handleClick}
        style={{
          padding: "1rem 2rem",
          backgroundColor: "#007BFF",
          color: "#fff",
          fontSize: "1.1rem",
          border: "none",
          borderRadius: "10px",
          cursor: "pointer",
          boxShadow: "0 4px 10px rgba(0,0,0,0.1)",
          transition: "background 0.3s ease"
        }}
      >
        📄 Upload File Here
      </button>
    </div>
  );
}

export default UploadForm;
