"""Flight API router.

Provides endpoints for searching flights and retrieving flight details.
"""

from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List

from ..models.flight import FlightSearchRequest, FlightSearchResponse, Flight
from ..services.flight_service import FlightService

router = APIRouter()

# Dependency injection for the service – in a real project this could be
# replaced with a database session or external API client.
flight_service = FlightService()

@router.get("/flights", response_model=FlightSearchResponse, tags=["flights"])
async def search_flights(
    origin: str = Query(..., description="IATA code of departure airport"),
    destination: str = Query(..., description="IATA code of arrival airport"),
    date: str = Query(..., description="Departure date in YYYY-MM-DD format"),
    passengers: int = Query(1, ge=1, le=10, description="Number of passengers"),
):
    """Search for available flights.

    Parameters are validated by FastAPI and passed to the service layer.
    The service returns a list of :class:`~backend.models.flight.Flight`.
    """
    try:
        flights = await flight_service.search_flights(origin, destination, date, passengers)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    return FlightSearchResponse(flights=flights)

@router.get("/flights/{flight_id}", response_model=Flight, tags=["flights"])
async def get_flight(flight_id: str):
    """Retrieve a single flight by its ID."""
    flight = await flight_service.get_flight(flight_id)
    if not flight:
        raise HTTPException(status_code=404, detail="Flight not found")
    return flight
