from fastapi import FastAPI
from database import engine
from models import Base
from routes.orders import router as order_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Restaurant Order System",
    description="Backend-only system using FastAPI, RabbitMQ and SQLite",
    version="1.0.0"
)


app.include_router(order_router)

@app.get("/")
def read_root():
    return {"status": "OK", "message": "Restaurant Order System is running"}
