import axios from "axios";

const BASE = "http://127.0.0.1:8000";


export const uploadFile = async (file) => {
  const form = new FormData();
  form.append("file", file);
  const res = await axios.post(`${BASE}/analyze/`, form);
  return res.data;
};


export const exportReport = async (id) => {
  const res = await axios.get(`${BASE}/analyze/reports/${id}/export`, {
    responseType: "blob"
  });
  return res.data;
};
