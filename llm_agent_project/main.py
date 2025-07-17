from fastapi import FastAPI, Request
from transformers import pipeline

app = FastAPI()
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

@app.post("/summarize")
async def summarize(req: Request):
    data = await req.json()
    text = data.get("text", "")
    chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]
    summaries = summarizer(chunks, max_length=150, min_length=40, do_sample=False)
    return {"summary": " ".join([s['summary_text'] for s in summaries])}
