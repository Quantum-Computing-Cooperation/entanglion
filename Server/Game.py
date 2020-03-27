from Engine import *
from Events import *


class Game:
    def __init__(self, player_blue, player_red, detection_rate):
        self.player_blue = player_blue
        self.player_red = player_red
        self.engine_control = EngineControl()
        self.detection_rate = detection_rate
        self.engine_stack = EngineStack()
        self.event_deck = EventStack()

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
