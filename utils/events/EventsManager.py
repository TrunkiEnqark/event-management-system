# Event manager for 3 roles
# Admin: edit, change

from Event import *
from ..users.User import *

class EventsManager(Events):
    def __init__(self, file_dir: str, curr_user: User):
        self.file = file_dir
        self.data = dict()
        self.current_user = curr_user