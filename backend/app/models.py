"""
Database models for NexTrip.
Uses SQLAlchemy ORM with PostgreSQL (SQLite fallback).
"""

from sqlalchemy import Column, String, Float, DateTime, Integer, ForeignKey, JSON, Enum as SQLEnum
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import enum

Base = declarative_base()

class TripStatus(str, enum.Enum):
    CREATED = "CREATED"
    LOCKED = "LOCKED"
    PENDING_PAYMENT = "PENDING_PAYMENT"
    CONFIRMED = "CONFIRMED"
    EXPIRED = "EXPIRED"

class PaymentStatus(str, enum.Enum):
    UNPAID = "UNPAID"
    PAID = "PAID"

class Trip(Base):
    __tablename__ = "trips"
    
    trip_id = Column(String(36), primary_key=True, index=True)
    mode = Column(String(10))  # SOLO or GROUP
    destination = Column(String(100), nullable=False)
    start_date = Column(String(10), nullable=False)  # YYYY-MM-DD
    end_date = Column(String(10), nullable=False)    # YYYY-MM-DD
    status = Column(SQLEnum(TripStatus), default=TripStatus.CREATED)
    itinerary = Column(JSON, nullable=True)  # JSONB
    created_at = Column(DateTime, default=datetime.utcnow)

class TripMember(Base):
    __tablename__ = "trip_members"
    
    member_id = Column(String(36), primary_key=True, index=True)
    trip_id = Column(String(36), ForeignKey("trips.trip_id"), nullable=False)
    user_name = Column(String(100), nullable=False)
    max_budget = Column(Float, nullable=False)  # in INR
    room_pref = Column(String(20))  # standard, deluxe, suite
    allocated_share = Column(Float, nullable=True)
    room_tier = Column(String(20), nullable=True)
    payment_status = Column(SQLEnum(PaymentStatus), default=PaymentStatus.UNPAID)
    joined_at = Column(DateTime, default=datetime.utcnow)

class Flight(Base):
    __tablename__ = "inventory_flights"
    
    flight_id = Column(String(36), primary_key=True, index=True)
    origin = Column(String(50), nullable=False)
    destination = Column(String(50), nullable=False)
    price = Column(Float, nullable=False)  # in INR
    duration_minutes = Column(Integer, nullable=True)
    quality_score = Column(Float, default=5.0)  # 1-10

class Hotel(Base):
    __tablename__ = "inventory_hotels"
    
    hotel_id = Column(String(36), primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    destination = Column(String(50), nullable=False)
    quality_score = Column(Float, default=5.0)  # 1-10

class RoomTier(Base):
    __tablename__ = "inventory_room_tiers"
    
    tier_id = Column(String(36), primary_key=True, index=True)
    hotel_id = Column(String(36), ForeignKey("inventory_hotels.hotel_id"), nullable=False)
    tier = Column(String(20))  # standard, deluxe, suite
    price_multiplier = Column(Float, default=1.0)  # e.g., deluxe = 1.5x, suite = 2.5x base
    base_price = Column(Float, nullable=False)  # price per night in INR

class Activity(Base):
    __tablename__ = "inventory_activities"
    
    activity_id = Column(String(36), primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    destination = Column(String(50), nullable=False)
    cost = Column(Float, nullable=False)  # in INR
    quality_score = Column(Float, default=5.0)  # 1-10
    category = Column(String(50), nullable=True)  # adventure, cultural, leisure, etc.
