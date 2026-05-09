from fastapi import FastAPI
from .api import user, flight, booking, payment

app = FastAPI(title="AirTicket Booking API")

app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(flight.router, prefix="/flights", tags=["flights"])
app.include_router(booking.router, prefix="/bookings", tags=["bookings"])
app.include_router(payment.router, prefix="/payments", tags=["payments"])

@app.get("/")
async def read_root():
    return {"message": "Welcome to AirTicket Booking API"}
