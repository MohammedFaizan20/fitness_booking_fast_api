from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import SessionLocal
from typing import List

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/book", response_model=schemas.BookingOut)
def book_class(booking: schemas.BookingCreate, db: Session = Depends(get_db)):
    return crud.book_class(db, booking)

@router.get("/bookings", response_model=List[schemas.BookingOut])
def get_bookings(email: str = Query(...), db: Session = Depends(get_db)):
    return crud.get_bookings_by_email(db, email)
