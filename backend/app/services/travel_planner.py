from app.models.trip import TripPlanRequest, TripPlanResponse
from app.agents.destination_agent import DestinationAgent
from app.agents.transportation_agent import TransportationAgent
from app.agents.accommodation_agent import AccommodationAgent
from app.agents.weather_agent import WeatherAgent
from app.agents.activities_agent import ActivitiesAgent
from app.agents.budget_agent import BudgetAgent
from app.agents.itinerary_agent import ItineraryAgent


class TravelPlannerService:
    """Coordinates the agents responsible for building a travel plan."""

    def __init__(self):
        self.destination_agent = DestinationAgent()
        self.transportation_agent = TransportationAgent()
        self.accommodation_agent = AccommodationAgent()
        self.weather_agent = WeatherAgent()
        self.activities_agent = ActivitiesAgent()
        self.budget_agent = BudgetAgent()
        self.itinerary_agent = ItineraryAgent()

    def create_plan(self, request: TripPlanRequest) -> TripPlanResponse:
        nights = (request.end_date - request.start_date).days

        destination_research = self.destination_agent.research(
            request.destination
        )

        transportation_plan = self.transportation_agent.plan(
            request.origin,
            request.destination
        )

        accommodation_plan = self.accommodation_agent.plan(
            request.destination,
            request.travelers,
            request.budget
        )

        weather_forecast = self.weather_agent.forecast(
            request.destination,
            request.start_date.isoformat(),
            request.end_date.isoformat()
        )

        activities_plan = self.activities_agent.plan(
            request.destination,
            request.interests
        )

        budget_plan = self.budget_agent.estimate(
            request.budget,
            request.currency,
            request.travelers
        )

        itinerary_plan = self.itinerary_agent.build(
            request.destination,
            request.start_date.isoformat(),
            request.end_date.isoformat(),
            request.interests
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
            "accommodation_plan": accommodation_plan,
            "weather_forecast": weather_forecast,
            "activities_plan": activities_plan,
            "budget_plan": budget_plan,
            "itinerary_plan": itinerary_plan,
            "agents": {
                "destination": "completed",
                "transportation": "completed",
                "accommodation": "completed",
                "weather": "completed",
                "activities": "completed",
                "budget": "completed",
                "itinerary": "completed",
            },
        }

        return TripPlanResponse(
            message="Destination, transportation, accommodation, weather, activities, budget, and itinerary planning completed.",
            status="accepted",
            trip=trip,
        )