import unittest

from src.guest import Guest
from src.song import Song
from src.room import Room

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guests_0 = Guest('Fred', 56)
        self.guests_1 = Guest('Betty', 34)
        self.guests_2 = Guest('Bob', 45)
        self.guests_3 = Guest('Ann', 56)
        self.guests_4 = Guest('Jim', 67)

    def test_guest_name(self):
        self.assertEqual('Fred', self.guests_0.name)

    def test_guest_age(self):
        self.assertEqual(67, self.guests_4.age)

    # def test_guest_has_money(self):
    #     self.assertEqual(100, self.guests_2.wallet)

    # def tests_customer_reduce_cash(self):
    #     self.customer.customer_reduce_cash
    #     self.assertEqual(9, self.guests_0.wallet)

    # def test_no_fav_song(self):
    #     self.assertEqual(0, self.guests_0.no_fav_song())


    # def test_fav_song(self):
    #     song = Song('Ozzy', 'Snowblind')
    #     self.guests_0.fav_song(song)
    #     self.assertEqual(1, self.guests_0.no_fav_song())