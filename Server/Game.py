from Engine import *
from Events import *
from Planet import *
from Player import Player
from Transitions import *


class Game:
    def __init__(self, socket_one, socket_two):
        self.player_blue = Player(Color.Blue, socket_one)
        self.player_red = Player(Color.Red, socket_two)
        self.engine_control = EngineControl()
        self.detection_rate = 1
        self.curr_player = None
        self.component_map = {}
        self.engine_stack = EngineStack()
        self.event_stack = EventStack()
        self.distribute_components()

    def distribute_components(self):
        shuffled_components = [e for e in Component]
        random.shuffle(shuffled_components)
        self.component_map[PSI_PLUS] = shuffled_components[0]
        self.component_map[PSI_MINUS] = shuffled_components[1]
        self.component_map[PHI_PLUS] = shuffled_components[2]
        self.component_map[PHI_MINUS] = shuffled_components[3]
        self.component_map[OMEGA0] = shuffled_components[4]
        self.component_map[OMEGA1] = shuffled_components[5]
        self.component_map[OMEGA2] = shuffled_components[6]
        self.component_map[OMEGA3] = shuffled_components[7]

        self.player_blue.send_components_map()
        self.player_red.send_components_map()

    def start(self):
        self.determine_first_player()
        self.determine_init_locations()
        self.draw_engine_cards()
        self.run()

    def determine_first_player(self):
        blue, red = 0, 0
        while blue == red:
            blue, red = centarious_roll(), entanglion_roll()
        if blue < red:
            self.curr_player = self.player_blue
        else:
            self.curr_player = self.player_red

        self.player_blue.send_init_player(blue, red, self.curr_player.color)
        self.player_red.send_init_player(blue, red, self.curr_player.color)

    def determine_init_locations(self):
        blue, red = centarious_roll(), centarious_roll()
        self.player_blue.planet = ZERO if blue == 0 else ONE
        self.player_red.planet = ZERO if red == 0 else ONE

        self.player_blue.send_init_locations()
        self.player_red.send_init_locations()

    def draw_engine_cards(self):
        for i in range(ENGINE_DECK_INIT_SIZE):
            self.player_blue.engine_deck += self.engine_stack.draw()
            self.player_red.engine_deck += self.engine_stack.draw()

        self.player_blue.send_init_engine_deck()
        self.player_red.send_init_engine_deck()

    def run(self):
        raise Exception("Not Implemented")

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
        # draw new engine card, do the necessary if it's probe
        raise Exception("Not Implemented")

    def retrieve(self):
        raise Exception("Not Implemented")

    def event(self):
        raise Exception("Not Implemented")

    def play(self):
        raise Exception("Not Implemented")
