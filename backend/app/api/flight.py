from fastapi import APIRouter, Depends, HTTPException
from typing import List
from ..models.flight import FlightOut
from ..services.flight_service import FlightService

router = APIRouter()

@router.get("/search", response_model=List[FlightOut])
async def search_flights(origin: str, destination: str, date: str, passengers: int = 1, service: FlightService = Depends()):
    try:
        flights = await service.search_flights(origin, destination, date, passengers)
        return flights
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
