from typing import List
from ..models.booking import Booking

class BookingService:
    def __init__(self):
        self._bookings: List[Booking] = []
        self._next_id = 1

    async def create_booking(self, booking: Booking) -> Booking:
        booking.id = self._next_id
        self._next_id += 1
        self._bookings.append(booking)
        return booking
