from enum import Enum
from random import randrange


class Dice:
    def __init__(self, faces):
        self.faces = faces

    def roll(self):
        return randrange(self.faces)


Centarious = Dice(2)
Entanglion = Dice(8)


class Color(Enum):
    Blue = True
    Red = False


class Galaxy(Enum):
    Centarious = 0
    Superious = 1
    Entanglion = 2
