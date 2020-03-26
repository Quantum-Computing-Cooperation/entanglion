import Galaxy
from Enums import *


class Planet:
    def __init__(self, name, galaxy, component=None):
        self.name = name
        self.galaxy = galaxy
        self.component = component
        self.blueTransitions = None
        self.redTransitions = None

    def set_transitions(self, h, x, cnot, color=None):
        transitions = {EngineCard.H: h, EngineCard.X: x, EngineCard.CNOT: cnot}
        if color == Color.Blue:
            self.blueTransitions = transitions
        elif color == Color.Red:
            self.redTransitions = transitions
        else:
            self.blueTransitions = transitions
            self.redTransitions = transitions


ONE = Planet("ONE", Galaxy.Centarious)
ZERO = Planet("ZERO", Galaxy.Centarious)

PLUS = Planet("PLUS", Galaxy.Superious)
MINUS = Planet("MINUS", Galaxy.Superious)

PSI_PLUS = Planet("PSI PLUS", Galaxy.Entanglion)
PSI_MINUS = Planet("PSI MINUS", Galaxy.Entanglion)
PHI_PLUS = Planet("PHI PLUS", Galaxy.Entanglion)
PHI_MINUS = Planet("PHI MINUS", Galaxy.Entanglion)
OMEGA0 = Planet("OMEGA ZERO", Galaxy.Entanglion)
OMEGA1 = Planet("OMEGA ONE", Galaxy.Entanglion)
OMEGA2 = Planet("OMEGA TWO", Galaxy.Entanglion)
OMEGA3 = Planet("OMEGA THREE", Galaxy.Entanglion)

ONE.set_transitions(MINUS, ZERO, ZERO)
ZERO.set_transitions(PLUS, ONE, ONE)

PLUS.set_transitions(ZERO, None, {ONE: PSI_PLUS, ZERO: PHI_PLUS})
MINUS.set_transitions(ONE, None, {ONE: PSI_MINUS, ZERO: PHI_MINUS})

