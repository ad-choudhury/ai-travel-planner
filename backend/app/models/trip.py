from datetime import date
from pydantic import BaseModel, Field, model_validator


class TripPlanRequest(BaseModel):
    origin: str = Field(..., min_length=2, max_length=100)
    destination: str = Field(..., min_length=2, max_length=100)
    start_date: date
    end_date: date
    travelers: int = Field(default=1, ge=1, le=50)
    budget: float = Field(..., gt=0)
    currency: str = Field(default="INR", min_length=3, max_length=3)
    interests: list[str] = Field(default_factory=list, max_length=20)
    travel_style: str = Field(default="balanced", max_length=50)

    @model_validator(mode="after")
    def validate_dates(self):
        if self.end_date <= self.start_date:
            raise ValueError("end_date must be after start_date")
        return self


class TripPlanResponse(BaseModel):
    message: str
    status: str
    trip: dict
