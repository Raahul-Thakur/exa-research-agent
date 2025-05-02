import os
import json

USAGE_FILE = "global_usage.json"
MAX_REQUESTS = 1000

def check_limit():
    """Check and increment usage; return False if over limit."""
    if not os.path.exists(USAGE_FILE):
        with open(USAGE_FILE, "w") as f:
            json.dump({"count": 0}, f)

    with open(USAGE_FILE, "r") as f:
        data = json.load(f)

    if data["count"] >= MAX_REQUESTS:
        return False

    data["count"] += 1

    with open(USAGE_FILE, "w") as f:
        json.dump(data, f)

    return True
