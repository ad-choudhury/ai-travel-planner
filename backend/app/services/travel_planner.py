from app.models.trip import TripPlanRequest, TripPlanResponse
from app.agents.destination_agent import DestinationAgent
from app.agents.transportation_agent import TransportationAgent


class TravelPlannerService:
    """Coordinates the agents responsible for building a travel plan."""

    def __init__(self):
        self.destination_agent = DestinationAgent()
        self.transportation_agent = TransportationAgent()

    def create_plan(self, request: TripPlanRequest) -> TripPlanResponse:
        nights = (request.end_date - request.start_date).days

        destination_research = self.destination_agent.research(
            request.destination
        )

        transportation_plan = self.transportation_agent.plan(
            request.origin,
            request.destination
        )

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
            "destination_research": destination_research,
            "transportation_plan": transportation_plan,
            "agents": {
                "destination": "completed",
                "transportation": "completed",
                "accommodation": "pending",
                "weather": "pending",
                "activities": "pending",
                "budget": "pending",
                "itinerary": "pending",
            },
        }

        return TripPlanResponse(
            message="Destination and transportation planning completed.",
            status="accepted",
            trip=trip,
        )