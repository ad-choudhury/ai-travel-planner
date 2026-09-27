class BudgetAgent:
    def estimate(self, budget: float, currency: str, travelers: int) -> dict:
        per_traveler = budget / travelers

        return {
            "total_budget": budget,
            "currency": currency.upper(),
            "travelers": travelers,
            "per_traveler_budget": round(per_traveler, 2),
            "summary": f"Budget estimate prepared for {travelers} travelers.",
        }