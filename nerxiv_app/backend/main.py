"""FastAPI backend main application."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from nerxiv_app._version import __version__

app = FastAPI(
    title="NERxiv API",
    description="API for NERxiv LLM RAG extractor agent",
    version=__version__,
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
    return {
        "message": "Welcome to NERxiv API",
        "version": __version__,
        "docs": "/docs",
    }


@app.get("/health")
async def health():
    """Health check endpoint."""
    return {"status": "healthy"}
