from utils.menu.MainMenu import *
from utils.users.User import *

# *** CONSTANTS VARIABLES ***

MAIN_OPTIONS = ["Log in", "Register", "Exit"]
USERS_DIR = "db/users.json"

#=============================

# *** GLOBAL VARIABLES ***

users = Users(file_dir=USERS_DIR)
users.load_users()

#=============================

if __name__ == "__main__":
    # print(users.get_users())
    while True:
        option = main_menu(MAIN_OPTIONS)
        
        match option:
            case 1:
                current_user = load_login(users)
                # print(current_user)
                next_menu(users, current_user)
            case 2:
                load_register(users)
            case 3:
                opt = input("Do you want to EXIT? (Y/n): ")
                if opt == 'Y' or opt == 'y':
                    break
            case default:
                break