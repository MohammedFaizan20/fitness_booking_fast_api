from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Class(Base):
    __tablename__ = "classes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    instructor = Column(String, nullable=False)
    datetime = Column(DateTime, nullable=False)
    available_slots = Column(Integer, nullable=False)

    bookings = relationship("Booking", back_populates="class_")

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    class_id = Column(Integer, ForeignKey("classes.id"))
    client_name = Column(String, nullable=False)
    client_email = Column(String, nullable=False)

    class_ = relationship("Class", back_populates="bookings")
