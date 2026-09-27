class ActivitiesAgent:
    def plan(self, destination: str, interests: list[str]) -> dict:
        return {
            "destination": destination,
            "interests": interests,
            "summary": f"Activity planning for {destination} is ready.",
            "activities": [],
        }