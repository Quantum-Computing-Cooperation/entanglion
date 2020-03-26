from Util import *


class Game:
    def __init__(self, player_one, player_two, detection_rate):
        self.player_blue = player_one
        self.player_red = player_two
        self.engine_control = [None] * ENGINE_CONTROL_SIZE
        self.detection_rate = detection_rate
        self.engine_stack = INIT_ENGINE_STACK
        self.event_deck = INIT_EVENT_DECK

    def navigate(self):
        raise Exception("Not Implemented")

    def exchange(self):
        raise Exception("Not Implemented")

    def retrieve(self):
        raise Exception("Not Implemented")

    def event(self):
        raise Exception("Not Implemented")

    def play(self):
        raise Exception("Not Implemented")
