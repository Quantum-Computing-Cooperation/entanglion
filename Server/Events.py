from enum import Enum
from random import random


class Event(Enum):
    Bennett = 1
    Heisenberg = 2
    Tunnel = 3
    Mechanic = 4

    Error = -1
    Schrodinger = -2
    Spooky = -3
    Collapse = -4

    # Shuffle = -5 doesn't need to be represented

    def can_save_for_later(self):
        return self.value > 0


class EventStack:
    def __init__(self):
        self.deck = {}
        self.initialize()

    def initialize(self):
        self.deck = {e for e in Event}
        for i in range(3):
            del self.deck[random.choice(list(self.deck))]

    def draw(self):
        if len(self.deck) == 0:
            self.initialize()
            return None
        else:
            drawn = random.choice(list(self.deck))
            del self.deck[drawn]
            return drawn
