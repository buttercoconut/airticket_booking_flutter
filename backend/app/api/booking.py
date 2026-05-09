# Dummy booking API
from fastapi import APIRouter, Depends, HTTPException
from typing import List
from ..models.booking import Booking
from ..services.booking_service import BookingService

router = APIRouter()

@router.post("/create", response_model=Booking)
async def create_booking(booking: Booking, service: BookingService = Depends()):
    try:
        created = await service.create_booking(booking)
        return created
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
