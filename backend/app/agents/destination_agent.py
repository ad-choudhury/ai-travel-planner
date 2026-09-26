class DestinationAgent:
    def research(self, destination: str) -> dict:
        return {
            "destination": destination,
            "summary": f"Destination research for {destination} is ready.",
            "highlights": [],
            "tips": [],
        }