from fastapi import APIRouter, HTTPException, WebSocket, WebSocketDisconnect
from pydantic import BaseModel
from typing import Optional, List
import json

router = APIRouter()

class GroupCreateRequest(BaseModel):
    destination: str
    start_date: str  # YYYY-MM-DD
    end_date: str    # YYYY-MM-DD
    host_name: str

class GroupJoinRequest(BaseModel):
    user_name: str
    max_budget: float  # in INR
    room_pref: str  # standard, deluxe, suite

class GroupSession(BaseModel):
    trip_id: str
    destination: str
    host_name: str
    status: str  # CREATED, LOCKED, PENDING_PAYMENT, CONFIRMED, EXPIRED
    members: List[dict] = []

# In-memory store for group sessions (replace with DB)
group_sessions = {}

@router.post("/create", response_model=GroupSession)
async def create_group(request: GroupCreateRequest):
    """
    Create a new group travel session.
    Returns trip_id for sharing with other members.
    """
    import uuid
    trip_id = str(uuid.uuid4())[:8]
    
    session = GroupSession(
        trip_id=trip_id,
        destination=request.destination,
        host_name=request.host_name,
        status="CREATED",
        members=[{"user_name": request.host_name, "role": "host"}]
    )
    
    group_sessions[trip_id] = session
    return session

@router.post("/join/{trip_id}")
async def join_group(trip_id: str, request: GroupJoinRequest):
    """
    Join an existing group travel session.
    """
    if trip_id not in group_sessions:
        raise HTTPException(status_code=404, detail="Trip not found")
    
    session = group_sessions[trip_id]
    session.members.append({
        "user_name": request.user_name,
        "max_budget": request.max_budget,
        "room_pref": request.room_pref
    })
    
    return session

@router.post("/lock/{trip_id}")
async def lock_group(trip_id: str):
    """
    Lock in the group itinerary.
    Runs Smart-Split algorithm and starts escrow countdown.
    """
    if trip_id not in group_sessions:
        raise HTTPException(status_code=404, detail="Trip not found")
    
    session = group_sessions[trip_id]
    session.status = "PENDING_PAYMENT"
    
    # TODO: Run Smart-Split algorithm
    # TODO: Start escrow countdown timer
    
    return {"trip_id": trip_id, "status": "PENDING_PAYMENT", "timeout_seconds": 120}

@router.websocket("/ws/{trip_id}")
async def websocket_endpoint(websocket: WebSocket, trip_id: str):
    """
    WebSocket endpoint for real-time group session updates.
    """
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            # Broadcast to all connected clients for this trip
            await websocket.send_text(json.dumps({"status": "received", "data": data}))
    except WebSocketDisconnect:
        print(f"Client disconnected from trip {trip_id}")
