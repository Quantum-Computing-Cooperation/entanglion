from enum import Enum
from random import randrange


def centarious_roll():
    return randrange(2)


def entanglion_roll():
    return randrange(8) + 1


class Color(Enum):
    Blue = True
    Red = False


class Galaxy(Enum):
    Centarious = 0
    Superious = 1
    Entanglion = 2


class Component(Enum):
    Physical_Qubits = 0
    Qubit_Interconnect = 1
    Dilution_Refrigerator = 2
    Quantum_Gates = 3
    Quantum_Programming = 4
    Quantum_Error_Correction = 5
    Control_Infrastructure = 6
    Magnetic_Shielding = 7


class Action(Enum):
    Navigate = 1
    Exchange = 2
    Retrieve = 3
    Event = 4


MAX_DETECTION_RATE = 12
