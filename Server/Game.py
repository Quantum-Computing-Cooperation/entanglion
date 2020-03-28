from Engine import *
from Events import *
from Player import *
from Transitions import *


class Game:
    def __init__(self, socket_one, socket_two):
        self.player_blue = Player(Color.Blue, socket_one)
        self.player_red = Player(Color.Red, socket_two)
        self.engine_control = EngineControl()
        self.detection_rate = 1
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
