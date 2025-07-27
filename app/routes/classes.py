from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas
from app.database import SessionLocal
from app.utils.timezone import convert_ist_to_timezone

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[schemas.PublicClassOut])
def get_classes(tz: str = Query(default="Asia/Kolkata"), db: Session = Depends(get_db)):
    classes = crud.get_all_classes(db)
    return [convert_ist_to_timezone(class_obj, tz) for class_obj in classes]
