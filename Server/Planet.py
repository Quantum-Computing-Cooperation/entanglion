from Engine import EngineCard
from Util import *


class Planet:
    # TODO Do we actually need name and galaxy ?
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy
        self.blueTransitions = None
        self.redTransitions = None

    # swap is mostly trivial except for omega0 and omega3, which is why it's not modeled here
    def set_transitions(self, h, x, cnot, color=None):
        transitions = {EngineCard.H: h, EngineCard.X: x, EngineCard.CNOT: cnot}
        if color == Color.Blue:
            self.blueTransitions = transitions
        elif color == Color.Red:
            self.redTransitions = transitions
        else:
            self.blueTransitions = transitions
            self.redTransitions = transitions

    def get_transition(self, engineCard, color):
        if color == Color.Blue:
            return self.blueTransitions[engineCard]
        else:
            return self.redTransitions[engineCard]


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

PSI_PLUS.set_transitions(OMEGA3, PHI_PLUS, None, Color.Blue)
PSI_PLUS.set_transitions(OMEGA0, PHI_PLUS, None, Color.Red)

PSI_MINUS.set_transitions(OMEGA1, PHI_MINUS, None)

PHI_PLUS.set_transitions(OMEGA2, PSI_PLUS, None)

PHI_MINUS.set_transitions(OMEGA0, PSI_MINUS, None, Color.Blue)
PHI_MINUS.set_transitions(OMEGA3, PSI_MINUS, None, Color.Red)

OMEGA0.set_transitions(PHI_MINUS, OMEGA2, OMEGA2, Color.Blue)
OMEGA0.set_transitions(PSI_PLUS, OMEGA1, None, Color.Red)

OMEGA1.set_transitions(PSI_MINUS, OMEGA3, None, Color.Blue)
OMEGA1.set_transitions(PSI_MINUS, OMEGA0, None, Color.Red)

OMEGA2.set_transitions(PHI_PLUS, OMEGA0, OMEGA0, Color.Blue)
OMEGA2.set_transitions(PHI_PLUS, OMEGA3, OMEGA3, Color.Red)

OMEGA3.set_transitions(PSI_PLUS, OMEGA1, None, Color.Blue)
OMEGA3.set_transitions(PHI_MINUS, OMEGA2, OMEGA2, Color.Red)

CLOCKWISE_TABLE = {1: OMEGA0, 2: OMEGA1, 3: PSI_MINUS, 4: PHI_MINUS, 5: OMEGA3, 6: OMEGA2, 7: PHI_PLUS, 8: PSI_PLUS}
