from utils.menu.main_menu import *
from utils.users.users import *
from utils.events.event import *

# *** CONSTANTS VARIABLES ***

MAIN_OPTIONS = ["Log in", "Register", "Exit"]
USERS_DIR = r"./db/users.json"
EVENTS_DIR = r"./db/events.json"

#=============================

# *** GLOBAL VARIABLES ***

users = Users(file_dir=USERS_DIR)
events = Events(file_dir=EVENTS_DIR)
users.load_users()
events.load_events()

#=============================

if __name__ == "__main__":
    # print(users.get_users())
    while True:
        option = main_menu(MAIN_OPTIONS)
        
        match option:
            case 1:
                current_user = load_login(users)
                # print(current_user)
                next_menu(users, events, current_user)
            case 2:
                load_register(users)
            case 3:
                opt = input("Do you want to EXIT? (Y/n): ")
                if opt == 'Y' or opt == 'y':
                    break
            case default:
                break