import json
from enum import Enum, auto, unique
from random import randint
from models.user import User

@unique
class Status(Enum):
    FAILED = auto()
    SUCCESS = auto()

class Backend:
    @staticmethod
    def request_login(credentials) -> tuple[Status, User]:
        users = Database.get_users()
        searched_user = users.get(credentials.get("username"))
        if searched_user is not None and searched_user.get("password") == credentials.get("password"):
                return Status.SUCCESS, User(username=credentials.get("username"), password=searched_user.get("password"), UID=searched_user.get("UID"))
        return Status.FAILED, None

    @staticmethod
    def request_sign_up(credentials) -> Status:
        users = Database.get_users()
        if credentials.get("username") not in users:
            Database.add_user(username=credentials.get("username"), password=credentials.get("password"))
            return Status.SUCCESS
        return Status.FAILED
class Database:
    @staticmethod
    def get_users() -> dict:
        with open("data.txt", 'r') as file:
            file_string = file.read()
            file.close()
            users = json.loads(file_string)
            return users
    @staticmethod
    def add_user(username, password) -> Status:
        new_user = {username:{
            "UID": Database.generate_UID(),
            "password": password,
        }}
        users = Database.get_users()
        with open("data.txt", 'w') as file:
            users.update(new_user)
            jsonify_users = json.dumps(users)
            file.write(str(jsonify_users))
            file.close()
        return Status.SUCCESS
    @staticmethod
    def generate_UID() -> int:
        new_uid = len(Database.get_users())
        return new_uid