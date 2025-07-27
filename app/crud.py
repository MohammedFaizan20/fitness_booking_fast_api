from sqlalchemy.orm import Session
from app import models, schemas
from fastapi import HTTPException
from datetime import datetime
from sqlalchemy import func

import logging
logger = logging.getLogger(__name__)

def get_all_classes(db: Session):
    logger.info("Fetching all upcoming classes")
    return db.query(models.Class).filter(models.Class.datetime >= datetime.now()).all()

def book_class(db: Session, booking: schemas.BookingCreate):
    class_obj = db.query(models.Class).filter(models.Class.id == booking.class_id).first()

    if not class_obj:
        raise HTTPException(status_code=404, detail="Class not found")

    if class_obj.available_slots <= 0:
        raise HTTPException(status_code=400, detail="No slots available")

    logger.info(f"Booking created for {booking.client_email} in class ID {booking.class_id}")

    new_booking = models.Booking(
        class_id=booking.class_id,
        client_name=booking.client_name,
        client_email=booking.client_email
    )

    class_obj.available_slots -= 1
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    return new_booking


def get_bookings_by_email(db: Session, email: str):
    logger.info(f"Fetching bookings for {email}")
    return db.query(models.Booking).filter(
        func.lower(models.Booking.client_email) == email.lower()
    ).all()