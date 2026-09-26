# API

## GET /api/v1/health

Returns backend health.

## POST /api/v1/trips/plan

Accepts a trip request.

Example:

```json
{
  "origin": "Kolkata",
  "destination": "Thailand",
  "start_date": "2026-12-12",
  "end_date": "2026-12-19",
  "travelers": 2,
  "budget": 120000,
  "currency": "INR",
  "interests": ["beach", "food", "adventure"],
  "travel_style": "balanced"
}
```
