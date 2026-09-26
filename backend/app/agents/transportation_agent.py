class TransportationAgent:
    def plan(self, origin: str, destination: str) -> dict:
        return {
            "origin": origin,
            "destination": destination,
            "summary": f"Transportation planning from {origin} to {destination} is ready.",
            "options": [],
        }