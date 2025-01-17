import json
from enum import Enum

Role = Enum('Role', [('Admin', 0), ('Organizer', 1), ('Normal', 2)])

class User:
    def __init__(self, name: str, username: str, upw: str, umail: str, uphone: str, urole: Role = Role.Normal):
        self.username = username
        self.data = {
            "name": name,
            "password": upw,
            "role": urole.name,  
            "email": umail,
            "phone": uphone
        }

    def get_role(self) -> str:
        return self.data["role"]
    
    def get_username(self) -> str:
        return self.username
    
    def to_json(self):
        return json.dumps(self.data)

class Users:
    def __init__(self, file_dir=None):
        self.file = file_dir
        self.users = dict()

    def add_user(self, new_user: User):
        if self.is_user_exist(new_user.get_username()):
            print(f"User '{new_user.get_username()}' already exists!")
        else:
            self.users[new_user.get_username()] = new_user.data

    def load_users(self, file=None):
        if file is not None:
            self.file=file
        try:
            with open(self.file, 'r') as f:
                self.users = json.load(f) 
        except FileNotFoundError:
            print(f"{self.file} does not exist!")
        except json.JSONDecodeError:
            print("Error when reading JSON file.")

    def save_users(self, file=None):
        if file is not None:
            self.file = file
        try:
            with open(self.file, 'w') as f:
                json.dump(self.users, f, indent=4)  
        except Exception as e:
            print(f"{e}: Error when saving file")
        
    def get_role(self, username: str) -> str:
        user_data = self.users.get(username)
        if user_data:
            return user_data["role"]
        return None
    
    def get_pw(self, username: str) -> str:
        user_data = self.users.get(username)
        if user_data:
            return user_data["password"]
        return None
    
    def is_user_exist(self, username: str) -> bool:
        return username in self.users

    def get_users(self):
        return self.users