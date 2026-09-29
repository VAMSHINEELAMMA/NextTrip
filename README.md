# NexTrip - Constraint-Driven Travel Planner

A full-stack prototype for HackCellence 2026. Mock data only, no real payments.

## Tech Stack
- **Frontend:** Next.js 14 + React + Tailwind CSS
- **Backend:** FastAPI + Python
- **Real-time:** Socket.io for Group Mode
- **Database:** PostgreSQL (SQLite fallback)
- **Optimization:** NumPy/SciPy for budget optimization

## Features

### Solo Mode
User inputs destination, dates, and budget. System generates a complete itinerary maximizing quality within constraints using 0/1 knapsack optimization.

### Group Mode
Host creates a shareable trip session. Members join with their own budget and room preference. Asymmetrical Smart-Split algorithm ensures fair cost distribution.

### Escrow Pipeline
Mock payment system with countdown timer, payment status tracking, and simulated refunds on expiry.

## Project Structure

```
backend/
  app/
    main.py
    models.py
    schemas.py
    optimizer.py
    seed.py
    routes/
      solo.py
      group.py

frontend/
  app/
    page.tsx
    solo/
      page.tsx
    trip/
      [trip_id]/
        page.tsx
    components/
      ItineraryCard.tsx
      BudgetMatrix.tsx
      CountdownTimer.tsx
    lib/
      socket.ts
```

## Build Order
1. DB models + seed data
2. Solo knapsack optimizer
3. Solo endpoint + frontend flow
4. Group join/session + WebSocket
5. Smart-split algorithm
6. Group dashboard frontend
7. Escrow countdown + payment sim
8. Polish: loading/error states, mobile layout, landing page

## Getting Started

### Prerequisites
- Node.js 18+
- Python 3.9+
- PostgreSQL (or SQLite)

### Installation

```bash
# Backend setup
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Frontend setup
cd ../frontend
npm install
```

### Running the Application

```bash
# Backend
cd backend
uv run main.py  # or: python -m uvicorn app.main:app --reload

# Frontend (in another terminal)
cd frontend
npm run dev
```

Application runs at `http://localhost:3000`.
