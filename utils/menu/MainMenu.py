from ..users.User import *
import os

def main_menu(options: list[str]) -> int:
    for (idx, option) in enumerate(options):
        print(f"{idx + 1}. {option}")
    while True:
        try:
            option = int(input(f"Choose your option, enter a number from 1 - {len(options)}: "))
            if 1 <= option and option <= len(options):
                break
            print(f"The number needs to be in the range between 1 and {len(options)}!")
        except ValueError:
            print("Please choose a valid number!")
    return option # return the user's option

def next_menu(users: Users, current_user: str):
    cur_role = users.get_role(current_user)
    match cur_role:
        case "Admin":
            from .sub_menus.AdminMenu import admin_menu
            os.system('cls')
            admin_menu(current_user, users)
        case "Organizer":
            pass
        case "Visitor":
            pass

def load_login(users: Users) -> str:
    while True: 
        try:
            users.load_users()
            # os.system('cls')
            username = input("Username: ")
            password = input("Password: ")

            if not users.is_user_exist(username):
                print(f"Error: {username} does not exist")
            
            if password == users.get_pw(username):
                print(f'Logged in successfully for {username} as {users.get_role(username)}')
                # time.sleep(3)
                users.save_users()
                # os.system('cls')
                return username
            else:
                print("Your entered password does not match the username.")
            
        except Exception as e:
            print(f"{e}")

def load_register(users: Users):
    try:
        users.load_users()
        os.system('cls')
        username = input("Username: ")
        while users.is_user_exist(username):
            print(f'{username} is already exist. Use another one')
            username = input("Username: ")
        
        password = input("Password: ")
        rpassword = input("Re-enter your password: ")
        while password != rpassword:
            print("Passwords do not match. Please try again.")
            password = input("Password: ")
            rpassword = input("Re-enter your password: ")
        
        name = input("Full name: ")
        email = input("Email: ")
        phone = input("Phone number: ")
        
        users.add_user(User(
            name=name,
            username=username,
            upw=password,
            umail=email,
            uphone=phone
        ))
        
        users.save_users()
        print(f'Registered successfully for {username} as {users.get_role(username)}')
        # time.sleep(3)
        os.system('cls')
    except Exception as e:
        print(f"Error: {e}")