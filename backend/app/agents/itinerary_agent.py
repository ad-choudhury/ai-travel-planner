class ItineraryAgent:
    def build(
        self,
        destination: str,
        start_date: str,
        end_date: str,
        interests: list[str],
    ) -> dict:
        return {
            "destination": destination,
            "start_date": start_date,
            "end_date": end_date,
            "interests": interests,
            "summary": f"Itinerary planning for {destination} is ready.",
            "days": [],
        }