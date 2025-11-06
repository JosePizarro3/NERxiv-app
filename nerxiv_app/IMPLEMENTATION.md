# FARM Stack Implementation

This directory contains the FARM (FastAPI + React + MongoDB) stack implementation for NERxiv-app.

## Completed Tasks

All tasks from issue #2 have been completed:

1. ✅ Created backend package structure (`nerxiv_app/backend/`)
2. ✅ Created frontend package structure (`nerxiv_app/frontend/`)  
3. ✅ Added FastAPI dependencies to `pyproject.toml`
4. ✅ Created `.env.example` with configuration
5. ✅ Updated README.md with run instructions
6. ✅ Implemented FastAPI backend with:
   - Main application (`main.py`)
   - Configuration management (`config.py`)
   - CORS middleware for React frontend
   - Health check and root endpoints
7. ✅ Created tests for backend endpoints
8. ✅ Verified all tests pass

## Running the Backend

```bash
uvicorn nerxiv_app.backend.main:app --host 0.0.0.0 --port 8000 --reload
```

Access the API at http://localhost:8000 and the docs at http://localhost:8000/docs
