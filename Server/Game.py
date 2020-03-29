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
        self.curr_player = self.player_blue  # Doesn't matter @see determine_first_player
        self.component_map = {}
        self.engine_stack = EngineStack()
        self.event_stack = EventStack()
        self.distribute_components()

    def start(self):
        self.determine_first_player()
        self.determine_init_locations()
        self.draw_engine_cards()
        self.run()

    def run(self):
        action, arg = self.curr_player.ask_action()
        if action == Action.Navigate:
            self.navigate(arg)
        elif action == Action.Exchange:
            self.exchange(arg)
        elif action == Action.Retrieve:
            self.retrieve()
        elif action == Action.Event:
            self.event(arg)

        game_over = self.game_over()
        if game_over:
            self.player_blue.send_game_over(game_over)
            self.player_red.send_game_over(game_over)
            return

        self.change_player()
        self.run()

    def navigate(self, engine_card):
        if engine_card == EngineCard.SWAP:
            if self.curr_player.planet == OMEGA0:
                self.player_blue.planet = OMEGA3
                self.player_red.planet = OMEGA3
            elif self.curr_player.planet == OMEGA3:
                self.player_blue.planet = OMEGA0
                self.player_red.planet = OMEGA0
            else:
                p = self.player_blue.planet
                self.player_blue.planet = self.player_red.planet
                self.player_red.planet = p
        else:
            self.player_blue.planet, self.player_red.planet = \
                transition(self.curr_player.color, self.player_blue.planet, self.player_red.planet, engine_card)

        self.player_blue.send_locations(self.player_red.planet)
        self.player_red.send_locations(self.player_blue.planet)

        if self.player_blue.planet.galaxy == Galaxy.Entanglion:
            self.orbital_defense()

        self.engine_control.add(engine_card)
        self.check_engine()

        self.exchange(engine_card)

    def exchange(self, engineCard):
        # draw new engine card, do the necessary if it's probe
        drawn = self.engine_stack.draw()
        if drawn == EngineCard.PROBE:
            self.handle_probe()
        else:
            self.curr_player.engine_deck += drawn

            self.player_blue.send_engine_decks(self.player_red.engine_deck)
            self.player_red.send_engine_decks(self.player_blue.engine_deck)

    def retrieve(self):
        roll = entanglion_roll()
        if roll > self.detection_rate:
            component = self.component_map[self.curr_player.planet]
            del self.component_map[self.curr_player.planet]
            self.curr_player.components += component

            self.player_blue.send_components(self.player_red.components)
            self.player_red.send_components(self.player_blue.components)
        else:
            self.detection_rate += 1
            self.player_blue.send_dRate(self.detection_rate)
            self.player_red.send_dRate(self.detection_rate)

    def event(self, event):
        raise Exception("Not Implemented")

    # Game helping functions

    def check_engine(self):
        pass

    def handle_probe(self):
        pass

    def orbital_defense(self):
        pass

    def game_over(self):
        return len(self.component_map) == 0

    def change_player(self):
        self.curr_player = self.player_blue if self.curr_player == self.player_red else self.player_red

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

        self.player_blue.send_locations(self.player_red.planet)
        self.player_red.send_locations(self.player_blue.planet)

    def draw_engine_cards(self):
        for i in range(ENGINE_DECK_INIT_SIZE):
            self.player_blue.engine_deck += self.engine_stack.draw()
            self.player_red.engine_deck += self.engine_stack.draw()

        self.player_blue.send_engine_decks(self.player_red.engine_deck)
        self.player_red.send_engine_decks(self.player_blue.engine_deck)

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
