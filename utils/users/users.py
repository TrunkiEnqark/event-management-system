import json
import pandas as pd
from tabulate import tabulate
from enum import Enum

Role = Enum('Role', [('Admin', 0), ('Organizer', 1), ('Visitor', 2)])

class Users:
    def __init__(self, file_dir=None):
        self.file = file_dir
        self.users = {}

    def add_user(self, username: str, name: str, password: str, role: Role, email: str, phone: str):
        if self.is_user_exist(username):
            print(f"User '{username}' already exists!")
        else:
            self.users[username] = {
                "name": name,
                "password": password,
                "role": role.name,  
                "email": email,
                "phone": phone
            }

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
    
    def is_matched_password(self, username: str, entered_password: str) -> bool:
        if username in self.users:
            return self.users[username]['password'] == entered_password
        print(f"There does not exist {username}")
        return False
    
    def is_user_exist(self, username: str) -> bool:
        return username in self.users

    def get_users(self):
        return self.users
    
    def change_attribute(self, username: str, attribute: str, new_val: str):
        self.users[username][attribute] = new_val
    
    def delete_user(self, username: str) -> bool:
        if username in self.users:
            del self.users[username]
            return True
        print(f"There does not exist {username}")
        return False
    
    def view_all_users(self):
        data_dict = {
            key: {"username": key, **value} for key, value in self.users.items()
        }
        df = pd.DataFrame(data_dict.values())
        print(tabulate(
            df,
            headers="keys",
            tablefmt="grid"
        ))
        
    def remove_except_admin(self):
        organizers_count, visitors_count = 0, 0
        users_to_remove = []
        for username in self.users:
            if self.users[username]['role'] != "Admin":
                if self.users[username]['role'] == "Organizer":
                    organizers_count += 1
                else:
                    visitors_count += 1
                users_to_remove.append(username)
        
        for username in users_to_remove:
            del self.users[username]        
        
        print(f'Deleted {organizers_count} organizer accounts.')
        print(f'Deleted {visitors_count} visitor accounts.')
        print(f'Deleted {organizers_count + visitors_count} accounts in total.')