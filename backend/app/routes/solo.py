from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

class SoloPlanRequest(BaseModel):
    destination: str
    start_date: str  # YYYY-MM-DD
    end_date: str    # YYYY-MM-DD
    total_budget: float  # in INR

class ActivityItem(BaseModel):
    activity_id: str
    name: str
    cost: float

class ItineraryItem(BaseModel):
    flight_id: str
    flight_name: str
    flight_cost: float
    hotel_id: str
    hotel_name: str
    room_tier: str
    hotel_cost: float
    activities: list[ActivityItem]
    buffer: float
    total_cost: float
    remaining: float

@router.post("/plan", response_model=ItineraryItem)
async def create_solo_plan(request: SoloPlanRequest):
    """
    Create a solo travel itinerary based on constraints.
    Uses 0/1 knapsack optimization to maximize quality within budget.
    """
    # TODO: Implement knapsack optimizer
    # For now, return mock data
    return ItineraryItem(
        flight_id="f1",
        flight_name="Indigo Delhi to Goa",
        flight_cost=5000,
        hotel_id="h1",
        hotel_name="Oceanview Resort",
        room_tier="standard",
        hotel_cost=3000,
        activities=[
            ActivityItem(activity_id="a1", name="Beach Sunset Tour", cost=500),
            ActivityItem(activity_id="a2", name="Spice Plantation Visit", cost=800),
        ],
        buffer=1500,
        total_cost=10800,
        remaining=round(request.total_budget - 10800, 2)
    )
