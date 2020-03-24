import random
import enum


class EngineCard(enum.Enum):
    SWAP = 1;
    H = 2;
    CNOT = 3;
    X = 4;


class Deck:
    def __init__(self):
        self.swapCount = 3;
        self.hCount = 8;
        self.cnotCount = 7;
        self.xCount = 5;

    def simulatedraw(self):
        my_list = [EngineCard.SWAP] * self.swapCount + [EngineCard.H] * self.hCount + [EngineCard.CNOT] * self.cnotCount + [EngineCard.X] * self.xCount
        drawncard = random.choice(my_list)
        print(drawncard)
        self.simulatetake(drawncard)
        return drawncard

    def simulatetake(self, enginecard):
        self.modifycard(enginecard, -1)

    def simulateput(self, enginecard):
        self.modifycard(enginecard, 1)

    def modifycard(self, enginecard, n):
        if enginecard == EngineCard.SWAP:
            self.swapCount += n
        elif enginecard == EngineCard.H:
            self.hCount += n
        elif enginecard == EngineCard.CNOT:
            self.cnotCount += n
        elif enginecard == EngineCard.X:
            self.xCount += n

