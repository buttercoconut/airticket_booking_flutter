from pydantic import BaseModel, Field
from datetime import datetime

class User(BaseModel):
    id: int
    username: str
    email: str
    hashed_password: str
    is_active: bool = True
    created_at: datetime
    updated_at: datetime
