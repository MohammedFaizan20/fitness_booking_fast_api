from datetime import datetime
from pydantic import BaseModel, EmailStr

class ClassBase(BaseModel):
    name: str
    instructor: str
    datetime: datetime
    available_slots: int

class PublicClassOut(ClassBase):
    class Config:
        orm_mode = True

class ClassOut(ClassBase):
    id: int
    class Config:
        orm_mode = True

class BookingCreate(BaseModel):
    class_id: int
    client_name: str
    client_email: EmailStr

class BookingOut(BaseModel):
    id: int
    class_id: int
    client_name: str
    client_email: EmailStr

    class Config:
        orm_mode = True
