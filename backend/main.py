from fastapi import FastAPI
from backend.api.endpoints import user, ask, feedback
from backend.services.database.session import init_db
import asyncio
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router)
app.include_router(ask.router)
app.include_router(feedback.router)

@app.on_event("startup")
async def startup_event():
    await init_db()