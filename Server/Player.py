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

    def send_init_player(self, blue, red, color):
        pass

    def send_init_locations(self):
        pass

    def send_init_engine_deck(self):
        pass

# Communication Protocol
# EC1,EC2,EC3;PLANET;COMPONENTS;EVENT_CARDS::EC1,EC2,EC3;PLANET;COMPONENTS;EVENT_CARDS::ENGINE(1->6);DET_RATE -
# - AVAILABLE_OPTIONS/BUTTONS
