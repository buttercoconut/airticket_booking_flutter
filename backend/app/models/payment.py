from pydantic import BaseModel
from datetime import datetime

class Payment(BaseModel):
    id: int
    booking_id: int
    amount: float
    method: str
    status: str
    transaction_id: str
    created_at: datetime
    updated_at: datetime
