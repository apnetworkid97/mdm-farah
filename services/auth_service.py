import json

from services.storage_service import get_data_file

def load_users():
    users_file = get_data_file("users.json")

    if not users_file.exists():

        return []

    with open(users_file, "r", encoding="utf-8") as file:

        return json.load(file)


def save_users(users):
    users_file = get_data_file("users.json")

    with open(users_file, "w", encoding="utf-8") as file:

        json.dump(users, file, indent=4)


def login(username, password):
    users = load_users()

    for user in users:

        if user["username"] == username and user["password"] == password:

            return True

    return False


def register_user(username, password, email):
    users = load_users()

    users.append({"username": username, "password": password, "email": email})

    save_users(users)
