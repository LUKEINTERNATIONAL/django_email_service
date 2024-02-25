from datetime import datetime, timezone

def get_time_ago(timestamp):
    current_date = datetime.now(timezone.utc)
    past_date = datetime.fromisoformat(str(timestamp)).replace(tzinfo=timezone.utc)

    time_diff = abs((current_date - past_date).total_seconds())
    seconds = int(time_diff)
    minutes = seconds // 60
    hours = minutes // 60
    days = hours // 24
    months = days // 30
    years = months // 12

    if years > 0:
        return f"1 year ago" if years == 1 else f"{years} years ago"
    elif months > 0:
        return f"1 month ago" if months == 1 else f"{months} months ago"
    elif days > 0:
        return f"1 day ago" if days == 1 else f"{days} days ago"
    elif hours > 0:
        if hours < 24:
            formatted_time = past_date.strftime("%I:%M %p")
            return f"{hours} hours ago at {formatted_time}"
        return f"1 hour ago" if hours == 1 else f"{hours} hours ago"
    elif minutes > 0:
        return f"1 minute ago" if minutes == 1 else f"{minutes} minutes ago"
    else:
        return "Just now"
