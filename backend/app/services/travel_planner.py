from app.models.trip import TripPlanRequest, TripPlanResponse


class TravelPlannerService:
    """Application service.

    This is intentionally lightweight in Stage 1. The multi-agent graph will
    replace the placeholder response in a later stage.
    """

    def create_plan(self, request: TripPlanRequest) -> TripPlanResponse:
        nights = (request.end_date - request.start_date).days

        trip = {
            "origin": request.origin,
            "destination": request.destination,
            "start_date": request.start_date.isoformat(),
            "end_date": request.end_date.isoformat(),
            "nights": nights,
            "travelers": request.travelers,
            "budget": request.budget,
            "currency": request.currency.upper(),
            "interests": request.interests,
            "travel_style": request.travel_style,
            "agents": {
                "destination": "pending",
                "transportation": "pending",
                "accommodation": "pending",
                "weather": "pending",
                "activities": "pending",
                "budget": "pending",
                "itinerary": "pending",
            },
        }

        return TripPlanResponse(
            message="Trip request accepted. Multi-agent planning will be connected in the next stage.",
            status="accepted",
            trip=trip,
        )
