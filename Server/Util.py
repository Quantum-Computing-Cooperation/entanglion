from enum import Enum


class EngineCard(Enum):  # The values represent the total number of that type of card in the game
    H = 0
    CNOT = 1
    X = 2
    SWAP = 3
    PROBE = 4

    def total(self): self.value


class Color(Enum):
    Blue = 1
    Red = 2


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
