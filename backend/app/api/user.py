from fastapi import APIRouter, Depends, HTTPException
from typing import List
from ..models.user import UserOut
from ..services.user_service import UserService

router = APIRouter()

@router.post("/register", response_model=UserOut)
async def register_user(user: UserOut, service: UserService = Depends()):
    try:
        created_user = await service.create_user(user)
        return created_user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
