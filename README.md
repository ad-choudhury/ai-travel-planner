# AI Travel Planner

A portfolio-ready multi-agent AI travel planning system.

## Current milestone
Stage 1 provides the complete project skeleton and a working FastAPI backend foundation. AI agents, external travel APIs, PostgreSQL persistence, and the React frontend will be added in later stages.

## Architecture

```text
User
  |
  v
FastAPI API
  |
  v
Travel Planner Service
  |
  +--> Destination Agent (future)
  +--> Flight Agent      (future)
  +--> Hotel Agent       (future)
  +--> Weather Agent     (future)
  +--> Activity Agent    (future)
  +--> Budget Agent      (future)
  +--> Itinerary Agent   (future)
  |
  v
PostgreSQL (future)
```

## Requirements

- Python 3.11+
- Git
- A virtual environment
- PostgreSQL (needed in a later stage)

## Backend setup

### Windows PowerShell

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env
uvicorn app.main:app --reload
```

### macOS/Linux

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

Open:

- API: http://127.0.0.1:8000
- Swagger docs: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Test the API

```bash
curl http://127.0.0.1:8000/api/v1/health
```

Create a planning request:

```bash
curl -X POST http://127.0.0.1:8000/api/v1/trips/plan ^
  -H "Content-Type: application/json" ^
  -d "{"origin":"Kolkata","destination":"Thailand","start_date":"2026-12-12","end_date":"2026-12-19","travelers":2,"budget":120000,"currency":"INR","interests":["beach","food","adventure"]}"
```

## Environment variables

See `backend/.env.example`. Never commit real API keys or passwords.

## Roadmap

1. Backend foundation - complete
2. Database layer
3. Multi-agent orchestration
4. External travel APIs
5. React frontend
6. Authentication and saved trips
7. Testing
8. Docker/deployment
