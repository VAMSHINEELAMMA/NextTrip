"""
Database seed script for mock data.
Populates flights, hotels, room tiers, and activities.
"""

flights_data = [
    {"origin": "Delhi", "destination": "Goa", "price": 5000, "duration_minutes": 150},
    {"origin": "Delhi", "destination": "Goa", "price": 4500, "duration_minutes": 160},
    {"origin": "Delhi", "destination": "Mumbai", "price": 3500, "duration_minutes": 120},
    # ... add ~15 total flights
]

hotels_data = [
    {"name": "Oceanview Resort", "destination": "Goa", "quality_score": 8.5},
    {"name": "Heritage Hotel", "destination": "Goa", "quality_score": 7.0},
    # ... add ~10 total hotels
]

room_tiers_data = [
    {"tier": "standard", "price_multiplier": 1.0, "base_price": 3000},
    {"tier": "deluxe", "price_multiplier": 1.5, "base_price": 3000},
    {"tier": "suite", "price_multiplier": 2.5, "base_price": 3000},
]

activities_data = [
    {"name": "Beach Sunset Tour", "destination": "Goa", "cost": 500, "quality_score": 8.0, "category": "leisure"},
    {"name": "Spice Plantation Visit", "destination": "Goa", "cost": 800, "quality_score": 7.5, "category": "cultural"},
    # ... add ~8 activities per destination
]

def seed_database():
    """
    Populate database with mock inventory data.
    """
    # TODO: Connect to DB and insert data
    print("Database seeding not yet implemented.")
