# System Architecture

## Stage 1

The current backend is intentionally modular:

```text
FastAPI
  |
  +-- API routes
  |
  +-- Pydantic models
  |
  +-- TravelPlannerService
  |
  +-- Agents (reserved)
  |
  +-- Database (reserved)
```

## Target architecture

The service layer will later invoke an agent orchestration graph:

```text
Trip Request
     |
     v
Planner / Orchestrator
     |
     +--> Destination Research
     +--> Transportation
     +--> Accommodation
     +--> Weather
     +--> Activities
     |
     v
Budget Agent
     |
     v
Itinerary Agent
     |
     v
Validation
     |
     v
Final Trip Plan
```
