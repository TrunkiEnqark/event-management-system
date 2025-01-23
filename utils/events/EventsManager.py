# Event manager for 3 roles
# Admin: edit, change

import pandas as pd
import tabulate

from datetime import date, datetime
from .Event import *
from ..users.User import *
from ..menu.MainMenu import *

EVENTS_MANAGER_OPTIONS = [
    "View events",
    "Add new event",
    "Delete all events",
    "Back",
]

STATUS_OPTIONS = [
    'Upcoming',
    'OnGoing',
    'Completed',
    'Cancelled',
    'Closed',
]

# Function to input date string and convert 
def enter_date(script: str) -> date:
    try:
        # Convert the string to a datetime object, then extract the date
        date_str = input(script)
        date_obj = datetime.strptime(date_str, "%Y/%m/%d").date()
        return date_obj
    except ValueError:
        return "Invalid date format. Please enter in the format YYYY/MM/DD."

# Function to input organizers or attendees
def add_usernames(typ: str) -> list[str]:
    add_users = input(f'Do you want to add {typ}s to this event? (y/n): ')
    event_users = []
    if add_users == 'y' or add_users == 'Y':
        stop = False
        while not stop:
            name = input(f"Enter {typ}'s username: ")
            event_users.append(name)
            stop = input('Do you want to stop adding new {typ}s? (y/n): ').lower() == 'y'
    return event_users

# to control all events (only Admin role can access)
class EventsManager:
    def __init__(self, events: Events, curr_user: str):
        self.events = events
        self.current_user = curr_user
    
    def view_events(self):
        events_dict = {
            key: {"name": key, **value} for key, value in self.events.data.items()
        }
        df = pd.DataFrame(events_dict.values())
        print(tabulate.tabulate(
            df,
            headers="keys",
            tablefmt="grid"
        ))
    
    def add_event(self, event: Event):
        try:
            self.events[event.name] = event.details
        except Exception as e:
            print(f'Error: {e}')
    
    def manager(self):
        while True:
            option = main_menu(EVENTS_MANAGER_OPTIONS)
            match option:
                case 1: # view events
                    self.view_events()
                case 2: # add new event
                    event_name = input('Enter event name: ')
                    print('Choose status: ')
                    event_status = EventStatus(main_menu(STATUS_OPTIONS) - 1)
                    event_type = input('Enter event type: ')
                    event_price = input('Enter price/ticket: ')
                    event_start = enter_date('Enter date time to start in the format YYYY/MM/DD: ')
                    event_end   = enter_date('Enter date time to end in the format YYYY/MM/DD: ')
                    event_location = input('Enter location: ')
                    event_attendees = []
                    event_priority = int(input('Enter the priority of this event (0-99) from High to Low: '))
                    event_organizers = add_usernames('organizer')
                    event_description = input('Enter description: ')

                    self.add_event(Event(
                        ename=event_name,
                        status=event_status,
                        event_type=event_type,
                        price=event_price,
                        start_date=event_start,
                        end_date=event_end,
                        location=event_location,
                        organizers=event_organizers,
                        attendees=event_attendees,
                        priority=event_priority,
                        description=event_description
                    ))
                case 3: # delete all events
                    pass
                case 4:
                    break
                case default:
                    pass
            self.events.save_events()