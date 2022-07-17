
from tests import guest_test


class Room:
    def __init__(self, name):
        self.name = name
        self.capacity = []
        self.song_list = []

    def current_playlist(self):
        return len(self.song_list)

    def add_song_to_playlist(self, song):
        self.song_list.append(song)

    def room_is_empty(self):
        return len(self.capacity)

    def check_in_guest(self, guest):
        self.capacity.append(guest)

    def check_out_guest(self, guest):
        self.capacity.remove(guest)



# def Enquiry(lis1):
#     if len(lis1) == 0:
#         return 0
#     else:
#         return 1
    def room_in_the_room(self):
        while len(self.capacity) < 4:
            return "Room isn't at capacity"
        if len(self.capacity) == 4:
            return 'Room is at capacity'
        if len(self.capacity) > 4:
            return "Room capacity met, can't exceed"

    
