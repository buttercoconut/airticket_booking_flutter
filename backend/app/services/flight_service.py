from typing import List
from datetime import datetime
from ..models.flight import Flight

class FlightService:
    def __init__(self):
        # In a real implementation this would interface with a database
        self._flights = self._load_dummy_flights()

    def _load_dummy_flights(self) -> List[Flight]:
        from datetime import datetime, timedelta
        flights = []
        for i in range(1, 6):
            flights.append(
                Flight(
                    id=i,
                    airline=f"Airline {i}",
                    departure_airport="JFK",
                    arrival_airport="LAX",
                    departure_time=datetime.now() + timedelta(hours=i*2),
                    arrival_time=datetime.now() + timedelta(hours=i*5),
                    price=200.0 + i*50,
                    stops=0,
                    duration=3.0 + i*0.5,
                )
            )
        return flights

    async def search_flights(self, origin: str, destination: str, date: str, passengers: int) -> List[Flight]:
        # Dummy filter logic
        return [f for f in self._flights if f.departure_airport == origin and f.arrival_airport == destination]
