from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routers.analyze import router as analyze_router

app = FastAPI(
    title="Medical Report Analyzer",
    description="Summarizes reports, extracts entities, and flags risks.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update in production!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(analyze_router)

@app.get("/health", tags=["health"])
def health_check():
    return {"status": "up"}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
