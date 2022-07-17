import unittest
from src.guest import Guest
from src.song import Song
from src.room import Room


class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room_0 = Room('Ozzy')
        self.room_1 = Room('Muddy Waters')
        self.room_2 = Room('Clapton')

    def test_room_has_name(self):
        self.assertEqual('Ozzy', self.room_0.name)
    
    def test_songs_in_list(self):
        self.assertEqual(0, self.room_0.current_playlist())

    def test_add_song_to_playlist(self):
        self.room_0.add_song_to_playlist(self.room_0)
        self.assertEqual(1, self.room_0.current_playlist())

    def test_room_is_empty(self):
        self.assertEqual(0, self.room_0.room_is_empty())

    def test_check_in_guest(self):
        guest = Guest('Fred', 56)
        self.room_0.check_in_guest(guest)
        self.assertEqual(1, self.room_0.room_is_empty())

    def test_check_out_guest(self):
        guest = Guest('Fred', 56)
        self.room_0.check_in_guest(guest)
        self.room_0.check_out_guest(guest)
        self.assertEqual(0, self.room_0.room_is_empty())

    def test_check_room_in_room(self):
        guest_0 = Guest('Fred', 56)
        guest_1 = Guest('Betty', 34)
        self.room_0.check_in_guest(guest_0)
        self.room_0.check_in_guest(guest_1)
        self.assertEqual("Room isn't at capacity", self.room_0.room_in_the_room())

    def test_check_is_at_capacity(self):
        guest_0 = Guest('Fred', 56)
        guest_1 = Guest('Betty', 34)
        guest_2 = Guest('Bob', 45)
        guest_3 = Guest('Ann', 56)
        self.room_0.check_in_guest(guest_0)
        self.room_0.check_in_guest(guest_1)
        self.room_0.check_in_guest(guest_2)
        self.room_0.check_in_guest(guest_3)
        self.assertEqual("Room is at capacity", self.room_0.room_in_the_room())

    def test_check_is_at_capacity(self):
        guest_0 = Guest('Fred', 56)
        guest_1 = Guest('Betty', 34)
        guest_2 = Guest('Bob', 45)
        guest_3 = Guest('Ann', 56)
        guest_4 = Guest('Jim', 67)
        self.room_0.check_in_guest(guest_0)
        self.room_0.check_in_guest(guest_1)
        self.room_0.check_in_guest(guest_2)
        self.room_0.check_in_guest(guest_3)
        self.room_0.check_in_guest(guest_4)
        self.assertEqual("Room capacity met, can't exceed", self.room_0.room_in_the_room())

    # def test_no_fav_song(self):
    #     self.assertEqual(0, self.room_0.no_fav_song())


    # def test_fav_song(self):
    #     song = Song('Ozzy', 'Snowblind')
    #     self.room_0.fav_song(song)
    #     self.assertEqual(1, self.room_0.no_fav_song())
