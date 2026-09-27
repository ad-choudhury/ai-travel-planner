class AccommodationAgent:
    def plan(self, destination: str, travelers: int, budget: float) -> dict:
        return {
            "destination": destination,
            "travelers": travelers,
            "budget": budget,
            "summary": f"Accommodation planning for {destination} is ready.",
            "options": [],
        }