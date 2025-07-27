from datetime import datetime
from zoneinfo import ZoneInfo
from app.models import Class

def convert_ist_to_timezone(class_obj: Class, target_tz: str):
    ist = ZoneInfo("Asia/Kolkata")
    try:
        target_zone = ZoneInfo(target_tz)
    except Exception:
        target_zone = ist  # fallback

    class_obj.datetime = class_obj.datetime.replace(tzinfo=ist).astimezone(target_zone)
    return class_obj
