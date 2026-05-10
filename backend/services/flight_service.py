"""Service layer for flight operations.

In a real application this would talk to a database or external API.  For
this demo we use an in‑memory list of flights.
"""

import asyncio
from datetime import datetime, timedelta
from typing import List, Optional

from ..models.flight import Flight, FlightSearchRequest

# Dummy data – in production replace with DB queries or API calls
_FAKE_FLIGHTS = [
    {
        "id": "FL001",
        "flight_number": "AA123",
        "origin": "JFK",
        "destination": "LAX",
        "departure_time": datetime.utcnow() + timedelta(hours=5),
        "arrival_time": datetime.utcnow() + timedelta(hours=8),
        "duration_minutes": 180,
        "price": 299.99,
    },
    {
        "id": "FL002",
        "flight_number": "DL456",
        "origin": "JFK",
        "destination": "SFO",
        "departure_time": datetime.utcnow() + timedelta(hours=6),
        "arrival_time": datetime.utcnow() + timedelta(hours=9),
        "duration_minutes": 180,
        "price": 349.99,
    },
]

class FlightService:
    """Business logic for flight searching and retrieval."""

    async def search_flights(
        self,
        origin: str,
        destination: str,
        date: str,
        passengers: int,
    ) -> List[Flight]:
        # Simulate async DB/API call
        await asyncio.sleep(0.1)
        # Filter by origin/destination – ignore date for demo
        results = [Flight(**f) for f in _FAKE_FLIGHTS if f["origin"] == origin and f["destination"] == destination]
        if not results:
            raise ValueError("No flights found for the given route")
        return results

    async def get_flight(self, flight_id: str) -> Optional[Flight]:
        await asyncio.sleep(0.05)
        for f in _FAKE_FLIGHTS:
            if f["id"] == flight_id:
                return Flight(**f)
        return None
