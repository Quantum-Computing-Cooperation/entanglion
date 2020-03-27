from Engine import EngineCard
from Planet import *
from Util import *


def transition(player: Color, blue: Planet, red: Planet, engineCard: EngineCard):
    if engineCard == EngineCard.SWAP or engineCard == EngineCard.PROBE:
        raise Exception("Handle SWAP and PROBE on your own! They aren't worth my time")

    # For now, the comment "CNOT: flip your ship only if the other ship is on CENTARIOUS ONE" was ignored
    if player == Color.Blue:
        new = blue.get_transition(engineCard, player)
        if isinstance(new, Planet):
            return new, red
        else:
            return new[red], new[red]
    else:
        new = red.get_transition(engineCard, player)
        if isinstance(new, Planet):
            return blue, new
        else:
            return new[blue], new[blue]
