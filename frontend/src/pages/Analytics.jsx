import React from "react";
import { Bar, Pie } from "react-chartjs-2";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  ArcElement,
  Tooltip,
  Legend,
} from "chart.js";

// Register chart components
ChartJS.register(CategoryScale, LinearScale, BarElement, ArcElement, Tooltip, Legend);

// Sample data (replace with backend data later)
const barData = {
  labels: ["Diabetes", "Hypertension", "Cardiac Risk", "Liver Issue", "Others"],
  datasets: [
    {
      label: "Risk Flags Count",
      data: [12, 9, 6, 3, 5],
      backgroundColor: "rgba(54, 162, 235, 0.6)",
      borderRadius: 6,
    },
  ],
};

const pieData = {
  labels: ["Diabetes", "Hypertension", "Cardiac", "Liver", "Others"],
  datasets: [
    {
      label: "Alert Distribution",
      data: [12, 9, 6, 3, 5],
      backgroundColor: [
        "rgba(255, 99, 132, 0.6)",
        "rgba(255, 206, 86, 0.6)",
        "rgba(75, 192, 192, 0.6)",
        "rgba(153, 102, 255, 0.6)",
        "rgba(255, 159, 64, 0.6)",
      ],
      borderWidth: 1,
    },
  ],
};

const Analytics = () => {
  return (
    <div style={{
      display: "flex",
      flexDirection: "column",
      alignItems: "center",
      padding: "2rem",
      fontFamily: "'Segoe UI', Tahoma, Geneva, Verdana, sans-serif"
    }}>
      <h2 style={{ marginBottom: "2rem" }}>📊 Report Summary Analytics</h2>

      <div style={{ width: "60%", marginBottom: "3rem" }}>
        <Bar data={barData} options={{ responsive: true }} />
      </div>

      <div style={{ width: "40%" }}>
        <Pie data={pieData} options={{ responsive: true }} />
      </div>
    </div>
  );
};

export default Analytics;
