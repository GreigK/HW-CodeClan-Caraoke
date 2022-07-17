class Guest:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # self.wallet = wallet
        self.fav_song = []



    # def customer_reduce_cash(self, amount):
    #     self.wallet -= amount


    def no_fav_song(self):
        return len(self.fav_song)


    def fav_song(self, song):
        self.fav_song.append(song)

