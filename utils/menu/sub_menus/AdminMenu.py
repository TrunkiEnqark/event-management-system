from ...users.User import *
from ..MainMenu import main_menu
import os

ADMIN_OPTIONS = ["View users", "View events", "Back to login menu", "Exit"]
EDIT_USERS_OPTIONS = ["Select user", "Remove all", "Back"]
EDIT_USER_OPTIONS = [
    "Change name", 
    "Change password", 
    "Change role", 
    "Change email", 
    "Change phone",
    "Delete this user",
    "Back"
]


def admin_menu(username: str, users: Users):
    print("============ ADMIN MENU ==============")
    print(f"User: {username}")
    while True:
        option = main_menu(ADMIN_OPTIONS)
        match option:
            case 1:
                view_users()
            case 2:
                pass
            case 3:
                pass
            case 4:
                os.system('cls')
                break # out admin menu
            
def view_users():
    pass