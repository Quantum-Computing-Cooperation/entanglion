from random import randrange


class Dice:
    def __init__(self, faces):
        self.faces = faces

    def roll(self):
        return randrange(self.faces)


Centarious = Dice(2)
Entanglion = Dice(8)
