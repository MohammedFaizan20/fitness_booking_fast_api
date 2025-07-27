from app.database import SessionLocal
from app import models
from datetime import datetime, timedelta

db = SessionLocal()

classes = [
    models.Class(name="Yoga", instructor="Anjali", datetime=datetime.now() + timedelta(days=1), available_slots=50),
    models.Class(name="Zumba", instructor="Ravi", datetime=datetime.now() + timedelta(days=2), available_slots=30),
    models.Class(name="HIIT", instructor="Meena", datetime=datetime.now() + timedelta(days=3), available_slots=25),
]

db.add_all(classes)
db.commit()
db.close()
print(" Seeded initial classes.")
