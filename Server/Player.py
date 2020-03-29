from Planet import Planet
from Util import Color


class Player:
    def __init__(self, color, socket):
        self.color = color
        self.engine_deck = []
        self.components = []
        self.event_deck = []
        self.planet = None
        self.socket = socket

    def send_components_map(self):
        pass

    def send_init_player(self, blue: int, red: int, color: Color):
        pass

    def send_locations(self, other_planet: Planet):
        pass

    def send_engine_decks(self, other_engine_deck: list):
        pass

    def ask_action(self):
        pass

    def send_game_over(self, won: bool):
        pass

    def send_components(self, other_components: list):
        pass

    def send_dRate(self, detection_rate: int):
        pass
