from pydantic import BaseModel, Field
from datetime import datetime

class Flight(BaseModel):
    id: int
    airline: str
    departure_airport: str
    arrival_airport: str
    departure_time: datetime
    arrival_time: datetime
    price: float
    stops: int
    duration: float
    # Additional fields can be added as needed
