from enum import Enum


class Event(Enum):
    Bennett = 1
    Heisenberg = 2
    Tunnel = 3
    Mechanic = 4

    Error = -1
    Schrodinger = -2
    Spooky = -3
    Collapse = -4
    Shuffle = -5

    def can_save_for_later(self):
        return self.value > 0


class EventStack:
    def __init__(self):
        self.deck = {e for e in Event}
