import json

from fastapi import APIRouter

from app.models.health import HealthResponse
from app.models.trip import TripPlanRequest, TripPlanResponse
from app.models.trip_db import Trip
from app.db.session import SessionLocal
from app.services.travel_planner import TravelPlannerService

api_router = APIRouter()

planner = TravelPlannerService()


@api_router.get("/health", response_model=HealthResponse, tags=["System"])
async def health_check():
    return HealthResponse(status="healthy", service="travel-planner-api")


@api_router.post(
    "/trips/plan",
    response_model=TripPlanResponse,
    tags=["Trips"],
)
async def plan_trip(request: TripPlanRequest):

    db = SessionLocal()

    try:
        trip = Trip(
            origin=request.origin,
            destination=request.destination,
            start_date=request.start_date,
            end_date=request.end_date,
            travelers=request.travelers,
            budget=request.budget,
            currency=request.currency,
            interests=json.dumps(request.interests),
            travel_style=request.travel_style,
        )

        db.add(trip)
        db.commit()

        return planner.create_plan(request)

    finally:
        db.close()