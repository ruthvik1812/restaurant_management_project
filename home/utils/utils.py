from datetime import datetime
from .models import DailyOperatingHours  # import your existing model

def get_today_operating_hours():
    """
    Returns the restaurant's operating hours for the current day.
    If no entry is found, returns (None, None).
    """
    # Get current day name (e.g., 'Monday', 'Tuesday', etc.)
    today = datetime.today().strftime('%A')

    try:
        # Query the DailyOperatingHours model for today's entry
        operating_hours = DailyOperatingHours.objects.get(day_of_week=today)
        return (operating_hours.open_time, operating_hours.close_time)
    except DailyOperatingHours.DoesNotExist:
        # If no record exists for today
        return (None, None)
