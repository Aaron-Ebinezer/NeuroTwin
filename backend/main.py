from fastapi import FastAPI
from backend.api.endpoints import user, ask, feedback
from backend.services.database.session import init_db
import asyncio

app = FastAPI()

# Include routers
app.include_router(user.router, prefix="/user")
app.include_router(ask.router, prefix="/ask")
app.include_router(feedback.router, prefix="/feedback")

@app.on_event("startup")
async def startup_event():
    await init_db()