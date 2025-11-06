# NERxiv-app

A desktop app for running the NERxiv LLM RAG extractor agent.

## Architecture

This is a FARM (FastAPI + React + MongoDB) stack application:
- **Backend**: FastAPI server with MongoDB for data storage
- **Frontend**: React application (under development)
- **AI/ML**: Ollama integration for LLM-based extraction

## Prerequisites

- Python 3.10 or higher
- MongoDB (local or remote instance)
- Ollama (for LLM functionality)

## Setup

1. Clone the repository:
```bash
git clone https://github.com/JosePizarro3/NERxiv-app.git
cd NERxiv-app
```

2. Install the package with dependencies:
```bash
pip install -e ".[dev]"
```

3. Configure environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

4. Ensure MongoDB is running:
```bash
# If using local MongoDB
mongod
```

5. Ensure Ollama is running:
```bash
# Start Ollama service
ollama serve
```

## Running the Application

### Backend (FastAPI)

Start the backend API server:
```bash
uvicorn nerxiv_app.backend.main:app --host 0.0.0.0 --port 8000 --reload
```

The API will be available at:
- API: http://localhost:8000
- API Documentation: http://localhost:8000/docs
- Health Check: http://localhost:8000/health

### Frontend (React)

The React frontend is under development. See `nerxiv_app/frontend/README.md` for details.

## Development

### Running Tests

```bash
pytest tests/
```

### Linting

```bash
ruff check .
ruff format .
```

### Type Checking

```bash
mypy nerxiv_app/
```

## Project Structure

```
nerxiv_app/
├── backend/          # FastAPI backend
│   ├── main.py      # Main FastAPI application
│   └── config.py    # Configuration settings
├── frontend/        # React frontend (under development)
└── __init__.py
```

## Environment Variables

See `.env.example` for all available configuration options:
- `MONGODB_URI`: MongoDB connection string
- `MONGODB_DATABASE`: Database name
- `OLLAMA_HOST`: Ollama server URL
- `API_HOST`: API server host
- `API_PORT`: API server port

