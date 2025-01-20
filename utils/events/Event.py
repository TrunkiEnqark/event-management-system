import json
import tabulate
from enum import Enum

EventStatus = Enum('Status', 
                    [
                        ('Upcoming', 0),
                        ('OnGoing', 1),
                        ('Completed', 2),
                        ('Cancelled', 3),
                        ('Closed', 4),
                    ])
class Event:
    def __init__(self, 
                 ename: str, 
                 status: EventStatus, 
                 event_type: str, 
                 price: str, 
                 start_date=None, 
                 end_date=None, 
                 location=None, 
                 organizers=[], 
                 attendees=[], 
                 priority=99, 
                 description=""):
        self.name = ename
        self.details = {
            "status": status.value,
            "type": event_type,
            "price": price,
            "start": start_date,
            "end": end_date,
            "location": location,
            "attendees": attendees,
            "priority": priority,
            "organizers": organizers,
            "description": description,
            "subevents": [] # empty subevents, need Admin role to add subevents
        }
        
class Events:
    def __init__(self, file_dir=None):
        self.file = file_dir
        self.data = dict()
        
    def load_events(self, file_dir=None):
        if file_dir is not None:
            self.file = file_dir
        try:
            with open(self.file, 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            print(f"{self.file} does not exist!")
        except json.JSONDecodeError:
            print("Error when reading JSON file.")
            
    def save_events(self, file_dir=None):
        if file_dir is not None:
            self.file = file_dir
        
        try:
            with open(self.file, 'w') as f:
                json.dump(self.data, f, indent=4)
        except Exception as e:
            print(f"{e}: Error when saving file")
            
    def list_events(self):
        if not self.data:
            print("No events to display.")
            return
        
        table = []
        for event_name, event_details in self.data.items():
            table.append([
                event_name,
                ", ".join(event_details["organizers"]),
                event_details["priority"],
                event_details["description"],
                len(event_details["subevents"])
            ])
        
        headers = ["Event Name", "Organizers", "Priority", "Description", "Subevents Count"]
        print(tabulate(table, headers, tablefmt="grid"))