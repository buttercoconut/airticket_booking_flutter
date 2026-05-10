"""Main entry point for the Airticket Booking backend.

This module sets up the FastAPI application, includes routers, and configures
basic middleware such as CORS.  The project follows a very small but
extensible structure:

* ``api`` – FastAPI routers
* ``models`` – Pydantic data models
* ``services`` – Business logic / data access layer

The code below is intentionally lightweight so that it can be used as a
starting point for further development.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import routers
from .api.flight import router as flight_router

# Create FastAPI app with some basic metadata
app = FastAPI(
    title="Airticket Booking API",
    description="A minimal API for searching and booking flights.",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Allow CORS for local dev (adjust origins in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO: restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(flight_router, prefix="/api/v1", tags=["flights"])

# Simple health‑check endpoint
@app.get("/health", tags=["health"])
async def health_check():
    return {"status": "ok"}

# If this file is executed directly, run the development server
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
