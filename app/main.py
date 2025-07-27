from fastapi import FastAPI
from app.routes import classes, bookings
from app.database import Base, engine
import logging

app = FastAPI(title="Fitness Studio Booking API")

# Create tables
Base.metadata.create_all(bind=engine)

# Routers
app.include_router(classes.router, prefix="/classes", tags=["Classes"])
app.include_router(bookings.router, tags=["Bookings"])

# Logging setup
logging.basicConfig(level=logging.INFO)
