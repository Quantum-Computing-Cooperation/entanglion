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


class Event:
    def __init__(self, storable):
        self.storable = storable


Bennett = Event(True)
Heisenberg = Event(True)
Tunnel = Event(True)
Mechanic = Event(True)

Error = Event(False)
Shuffle = Event(False)
Schrodinger = Event(False)
Spooky = Event(False)
Collapse = Event(False)

ENGINE_CONTROL_SIZE = 6
INIT_ENGINE_STACK = {EngineCard.H: 8, EngineCard.CNOT: 7, EngineCard.X: 5, EngineCard.SWAP: 3, EngineCard.PROBE: 1}
INIT_EVENT_DECK = {Bennett, Heisenberg, Tunnel, Mechanic, Error, Shuffle, Schrodinger, Spooky, Collapse}
