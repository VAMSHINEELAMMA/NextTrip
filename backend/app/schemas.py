"""
Pydantic schemas for request/response validation.
"""

from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class FlightSchema(BaseModel):
    flight_id: str
    origin: str
    destination: str
    price: float
    duration_minutes: Optional[int] = None
    quality_score: float = 5.0

class HotelSchema(BaseModel):
    hotel_id: str
    name: str
    destination: str
    quality_score: float = 5.0

class RoomTierSchema(BaseModel):
    tier_id: str
    hotel_id: str
    tier: str
    price_multiplier: float
    base_price: float

class ActivitySchema(BaseModel):
    activity_id: str
    name: str
    destination: str
    cost: float
    quality_score: float = 5.0
    category: Optional[str] = None

class TripSchema(BaseModel):
    trip_id: str
    mode: str
    destination: str
    start_date: str
    end_date: str
    status: str
    itinerary: Optional[dict] = None
    created_at: datetime

class TripMemberSchema(BaseModel):
    member_id: str
    trip_id: str
    user_name: str
    max_budget: float
    room_pref: Optional[str] = None
    allocated_share: Optional[float] = None
    room_tier: Optional[str] = None
    payment_status: str
    joined_at: datetime
