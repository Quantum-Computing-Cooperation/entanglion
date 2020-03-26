from enum import Enum


class EngineCard(Enum): # The values represent the total number of that type of card in the game
    H = 8
    CNOT = 7
    X = 5
    SWAP = 3
    PROBE = 1

    def total(self): self.value


class Color(Enum):
    Blue = 1
    Red = 2
