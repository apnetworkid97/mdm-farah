import json
from datetime import datetime

from services.storage_service import get_data_file


def ensure_log_file():
    log_file = get_data_file("activity_log.json")

    if not log_file.exists():

        log_file.parent.mkdir(parents=True, exist_ok=True)

        with open(log_file, "w", encoding="utf-8") as file:

            json.dump([], file, indent=4)


def write_log(username: str, action: str, description: str):
    ensure_log_file()
    log_file = get_data_file("activity_log.json")

    with open(log_file, "r", encoding="utf-8") as file:

        logs = json.load(file)

    logs.append(
        {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "username": username,
            "action": action,
            "description": description,
        }
    )

    with open(log_file, "w", encoding="utf-8") as file:

        json.dump(logs, file, indent=4)


def get_logs():
    ensure_log_file()
    log_file = get_data_file("activity_log.json")

    with open(log_file, "r", encoding="utf-8") as file:

        return json.load(file)
