"""Pydantic models for flight data.

The models are intentionally simple – they can be extended with more fields
(e.g. pricing, seat availability, airline info) as the project grows.
"""

from datetime import datetime
from typing import List

from pydantic import BaseModel, Field

class Flight(BaseModel):
    id: str
    flight_number: str
    origin: str
    destination: str
    departure_time: datetime
    arrival_time: datetime
    duration_minutes: int
    price: float
    currency: str = "USD"

class FlightSearchRequest(BaseModel):
    origin: str
    destination: str
    date: str
    passengers: int = Field(1, ge=1, le=10)

class FlightSearchResponse(BaseModel):
    flights: List[Flight]
    total: int
    page: int = 1
    per_page: int = 10
