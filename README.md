# 🏋️‍♂️ Fitness Booking API

A simple FastAPI-based project to manage fitness class bookings.

## 📋 Features

- View upcoming fitness classes
- Book a class (validates slot availability)
- View all bookings for a specific user via email
- Handles timezones (default is Asia/Kolkata)

---

## 🛠 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/fitness_booking.git
cd fitness_booking

**2. (Optional) Create a Virtual Environment**
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies

pip install -r requirements.txt

4. Run the Application

uvicorn app.main:app --reload

The app will be available at: http://127.0.0.1:8000

Seed the Database with Sample Classes
Run this to insert initial classes:

python seed_data.py

Running Tests:
pytest

🧾 API Endpoints & Sample Requests:

1) GET /classes
Get all upcoming fitness classes.

http://127.0.0.1:8000/classes

Optional Query Param:
tz: Timezone string (default is Asia/Kolkata)

Example: /classes?tz=America/New_York

2) POST /book
Book a class (if slots available).
http://127.0.0.1:8000/book

Example Request Body:
{
  "class_id": 1,
  "client_name": "Faizan",
  "client_email": "faizan@example.com"
}

3) GET /bookings
Returns all bookings made by a specific email.
Required Query Parameter:
email (e.g., ?email=faizan@example.com)

http://127.0.0.1:8000/bookings?email=jay@example.com

Response Body:

[
    {
        "id": 3,
        "class_id": 1,
        "client_name": "Jay",
        "client_email": "jay@example.com"
    }
]

