from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

# Import routes
from app.routes import solo, group

# Lifecycle events
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("Starting NexTrip API...")
    yield
    # Shutdown
    print("Shutting down NexTrip API...")

# Create FastAPI app
app = FastAPI(
    title="NexTrip API",
    description="Constraint-driven travel planner for HackCellence 2026",
    version="0.1.0",
    lifespan=lifespan
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(solo.router, prefix="/api/solo", tags=["solo"])
app.include_router(group.router, prefix="/api/group", tags=["group"])

@app.get("/")
async def root():
    return {"message": "Welcome to NexTrip API", "version": "0.1.0"}

@app.get("/health")
async def health():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
