import unittest

from src.guest import Guest
from src.song import Song
from src.room import Room

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song_0 = Song('BBKing', 'How Blue Can You Get')
        self.song_1 = Song('Eric Clapton', 'Lalya')
        self.song_2 = Song('Ozzy', 'Snowblind')
        self.song_3 = Song('MFDoom', 'One Beer')

    def test_get_artist_name(self):
        self.assertEqual('BBKing', self.song_0.name)

    def test_get_song_name(self):
        self.assertEqual('How Blue Can You Get', self.song_0.song)


