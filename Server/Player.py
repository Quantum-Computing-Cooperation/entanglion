from Events import Event
from Planet import Planet
from Util import *


class Player:
    def __init__(self, color, socket):
        self.color = color
        self.engine_deck = []
        self.components = []
        self.event_deck = []
        self.planet = None
        self.socket = socket

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

    def send_components(self, component_map: dict, other_components: list):
        pass

    def send_dRate(self, detection_rate: int):
        pass

    def send_orbdef_evaded(self):
        pass

    def send_probe_notification(self):
        pass

    def send_event_shuffled(self):
        pass

    def send_event_played(self, drawn: Event):
        pass

    def send_event_decks(self, event_deck: list):
        pass

    def ask_bennett(self, can_ask: bool):
        pass

    def give_bennett(self, comp: Component):
        pass

    def ask_bennett_forcefully(self):
        pass
