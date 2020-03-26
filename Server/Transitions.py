from Enums import *
import Planet


def transition(player: Color, blue: Planet, red: Planet, engineCard: EngineCard):
    if engineCard == EngineCard.SWAP or engineCard == EngineCard.PROBE:
        raise Exception("Handle SWAP and PROBE on your own! They aren't worth my time")

    # For now, the comment "CNOT: flip your ship only if the other ship is on CENTARIOUS ONE" was ignored
    if player == Color.Blue:
        g = blue.get_transition(engineCard, player)
        if isinstance(g, Planet):
            return g
        else:
            return g(red)
    else:
        g = red.get_transition(engineCard, player)
        if isinstance(g, Planet):
            return g
        else:
            return g(blue)
