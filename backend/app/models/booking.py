from pydantic import BaseModel
from datetime import datetime

class Booking(BaseModel):
    id: int
    user_id: int
    flight_id: int
    passengers: int
    total_price: float
    status: str
    created_at: datetime
    updated_at: datetime
