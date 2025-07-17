import React from "react";

const riskAdviceMap = {
  "Diabetes": "Refer to endocrinologist and recommend dietary counseling.",
  "Hypertension": "Check blood pressure regularly and reduce sodium intake.",
  "Sepsis": "Immediate hospitalization and IV antibiotics required.",
  "CKD": "Schedule nephrologist consultation and monitor creatinine levels.",
  "High LDL": "Lifestyle changes and consider statin therapy."
};

const generalAdvice = [
  "💧 Stay hydrated and drink at least 8 glasses of water daily.",
  "🥗 Eat a balanced diet rich in vegetables, fruits, and fiber.",
  "🏃‍♂️ Exercise regularly — at least 30 minutes, 5 times a week.",
  "🧘 Manage stress with mindfulness, meditation, or relaxation.",
  "🛌 Ensure 7-9 hours of quality sleep every night.",
  "🩺 Get regular check-ups even if you feel healthy.",
  "🚭 Avoid smoking and limit alcohol intake."
];

const Recommendations = () => {
  const sampleFlags = [
    "Diabetes Alert: HbA1c ≥ 6.5%",
    "CKD Alert: GFR < 60 mL/min/1.73m²",
    "High LDL Cholesterol Alert: LDL ≥ 160 mg/dL"
  ];

  const matchedAdvice = sampleFlags.flatMap(flag => {
    const key = Object.keys(riskAdviceMap).find(k => flag.includes(k));
    return key ? [{ flag, advice: riskAdviceMap[key] }] : [];
  });

  return (
    <div style={{ padding: "2rem", fontFamily: "'Segoe UI', Tahoma, Geneva, Verdana, sans-serif", textAlign: "center" }}>
      <h2>🧠 Personalized Health Recommendations</h2>

      {matchedAdvice.length > 0 && (
        <>
          <h3 style={{ marginTop: "2rem" }}>⚠️ Your Risk-Based Suggestions</h3>
          <ul style={{ listStyle: "none", padding: 0 }}>
            {matchedAdvice.map(({ flag, advice }, i) => (
              <li key={i} style={{ margin: "1rem 0", backgroundColor: "#f1f5ff", padding: "1rem", borderRadius: "8px" }}>
                <strong>{flag}</strong><br />
                <span style={{ color: "#007BFF" }}>👉 {advice}</span>
              </li>
            ))}
          </ul>
        </>
      )}

      <h3 style={{ marginTop: "3rem" }}>🌱 General Preventive Advice</h3>
      <ul style={{ listStyle: "none", padding: 0 }}>
        {generalAdvice.map((tip, i) => (
          <li key={i} style={{ margin: "0.5rem 0" }}>{tip}</li>
        ))}
      </ul>
    </div>
  );
};

export default Recommendations;
