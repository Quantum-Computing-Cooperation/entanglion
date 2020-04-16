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

    # Shuffle = -5

    def can_save_for_later(self):
        return self.value > 0


class EventStack:
    def __init__(self):
        self.stack = []
        self.initialize()

    def initialize(self):
        self.stack = [e for e in Event]
        for i in range(3):
            self.stack.remove(random.choice(self.stack))

    def draw(self):
        if len(self.stack) == 0:
            self.initialize()
            return Event.Shuffle
        else:
            drawn = random.choice(self.stack)
            del self.stack[drawn]
            return drawn
