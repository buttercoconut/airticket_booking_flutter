from typing import List
from ..models.user import User

class UserService:
    def __init__(self):
        self._users: List[User] = []
        self._next_id = 1

    async def create_user(self, user: User) -> User:
        user.id = self._next_id
        self._next_id += 1
        self._users.append(user)
        return user
