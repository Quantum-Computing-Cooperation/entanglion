class Player:
    def __init__(self, color):
        self.color = color
        self.engine_deck = []
        self.components = []
        self.event_deck = []
        self.planet = None

    def set_engine_deck(self, engine_deck):
        self.engine_deck = engine_deck

    def add_component(self, component):
        self.components += component

    def add_event_card(self, event_card):
        self.event_deck += event_card

    def encode_and_send(self):
        raise Exception("Not Implemented")

    def parse_and_perform(self, String):
        raise Exception("Not Implemented")

# Communication Protocol
# EC1,EC2,EC3;PLANET;COMPONENTS;EVENT_CARDS::EC1,EC2,EC3;PLANET;COMPONENTS;EVENT_CARDS::ENGINE(1->6);DET_RATE -
# - AVAILABLE_OPTIONS/BUTTONS
