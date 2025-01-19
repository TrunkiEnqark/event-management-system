from ...users.User import *
from ..MainMenu import main_menu
import os

ADMIN_OPTIONS = [
    "View users", 
    "View events", 
    "Back to login menu", 
    "Exit"
]

EDIT_USERS_OPTIONS = [
    "Select user", 
    "Remove all", 
    "Back"
]

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
                view_users(users)
            case 2:
                pass
            case 3:
                pass
            case 4:
                os.system('cls')
                break # out admin menu
            
        users.save_users()

def select_user_by_username() -> str:
    try:
        inp = input("Enter username: ")
        return inp
    except Exception as e:
        print(f'Error: {e}')

def change_attribute(users: Users, sel_user: str, attribute: str) -> bool:
    new_name = input(f"Enter new {attribute}: ")
    
    if attribute == 'role' and not new_name in ["Admin", "Organizer", "Visitor"]:
        print("Role must be choose as 'Admin' or 'Organizer' or 'Visitor'!")
        return False
    
    yno = input(f"Do you want to change {sel_user} to {new_name}? (y/n): ")
    if yno == 'y' or yno == 'Y':
        users.change_attribute(
            username=sel_user,
            attribute=attribute,
            new_val=new_name
        )
        print('Change name successfully') 
        return True
    return False

def edit_user(users: Users, selected_user: str):
    print(f'Selected successfully {selected_user}')
    option = main_menu(EDIT_USER_OPTIONS)
    match option:
        case 1: # change name
            change_attribute(
                users,
                sel_user=selected_user,
                attribute='name',
            )
        case 2: # change password
            change_attribute(
                users,
                sel_user=selected_user,
                attribute='password',
            )
        case 3: # role
            change_attribute(
                users,
                sel_user=selected_user,
                attribute='role',
            )
        case 4: # email
            change_attribute(
                users,
                sel_user=selected_user,
                attribute='email',
            )
        case 5: # phone
            change_attribute(
                users,
                sel_user=selected_user,
                attribute='phone',
            )
        case 6: # delete user
            inp = input(f"Do you want to delete {selected_user}? (y/n): ")
            if inp == 'y' or inp == 'Y':
                users.delete_user(username=selected_user)
        case 7:
            return
        case default:
            return

def view_users(users: Users):
    while True:
        os.system('cls')
        users.view_all_users()
        option = main_menu(EDIT_USERS_OPTIONS)
        
        match option:
            case 1:
                sel = select_user_by_username()
                if users.is_user_exist(sel):
                    edit_user(users, sel)
                else:
                    print(f"There does not exist {sel}")
            case 2:
                pass
            case 3:
                break
            case default:
                break
        
        users.save_users()