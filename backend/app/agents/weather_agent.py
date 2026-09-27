class WeatherAgent:
    def forecast(self, destination: str, start_date: str, end_date: str) -> dict:
        return {
            "destination": destination,
            "start_date": start_date,
            "end_date": end_date,
            "summary": f"Weather planning for {destination} is ready.",
            "forecast": [],
        }