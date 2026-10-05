from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import create_tables
from routes.reviews import router as reviews_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    print("Database tables created successfully.")
    yield
    print("Application shutdown.")

app = FastAPI(
    title="Theatre Review Application",
    description="Theatre reviews API",
    lifespan=lifespan
)

app.include_router(reviews_router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Theatre Review Application!"}
