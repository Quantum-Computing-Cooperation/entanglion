from Engine import *
from Events import *
from Transitions import *


class Game:
    def __init__(self, player_blue, player_red, detection_rate):
        self.player_blue = player_blue
        self.player_red = player_red
        self.engine_control = EngineControl()
        self.detection_rate = detection_rate
        self.engine_stack = EngineStack()
        self.event_deck = EventStack()

    def navigate(self, player, engine_card):
        if engine_card == EngineCard.SWAP:
            if player.planet == OMEGA0:
                self.player_blue.planet = OMEGA3
                self.player_red.planet = OMEGA3
            elif player.planet == OMEGA3:
                self.player_blue.planet = OMEGA0
                self.player_red.planet = OMEGA0
            else:
                p = self.player_blue.planet
                self.player_blue.planet = self.player_red.planet;
                self.player_red.planet = p
        else:
            self.player_blue.planet, self.player_red.planet = \
                transition(player.color, self.player_blue.planet, self.player_red.planet, engine_card)

        if self.engine_control.full():
            self.engine_control.reset()
            self.event()
        self.engine_control.add(engine_card)
        self.exchange(player, engine_card)

    def exchange(self, player, engineCard):
        player.engine_deck.remove(engineCard)
        # draw new engine card, do the necessary if it's probe
        raise Exception("Not Implemented")

    def retrieve(self):
        raise Exception("Not Implemented")

    def event(self):
        raise Exception("Not Implemented")

    def play(self):
        raise Exception("Not Implemented")
