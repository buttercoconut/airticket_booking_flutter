from typing import List
from datetime import datetime
from ..models.user import User

class UserOut(User):
    hashed_password: str = None  # Exclude hashed_password from output

# For simplicity, we return the same User model
