"""FastAPI backend main application."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="NERxiv API",
    description="API for NERxiv LLM RAG extractor agent",
    version="0.1.0",
)

# Configure CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """Root endpoint."""
    return {"message": "Welcome to NERxiv API"}


@app.get("/health")
async def health():
    """Health check endpoint."""
    return {"status": "healthy"}
