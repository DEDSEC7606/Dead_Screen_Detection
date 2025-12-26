import os
from datetime import datetime, timedelta

AUTO_DIR = "auto_screens"

def get_screenshots_by_minutes(minutes):
    cutoff = datetime.now() - timedelta(minutes=minutes)

    valid_paths = []

    for filename in os.listdir(AUTO_DIR):
        if not filename.lower().endswith(".png"):
            continue

        try:
            ts_str = filename.replace(".png", "")
            ts = datetime.strptime(ts_str, "%H:%M:%S_%d|%m|%Y")
        except:
            continue

        if ts >= cutoff:
            valid_paths.append(os.path.join(AUTO_DIR, filename))
            print("FILE:", filename, "| TIMESTAMP:", ts)

    valid_paths.sort(key=lambda x: os.path.getmtime(x))

    return valid_paths