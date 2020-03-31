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
        self.engine_stack = EngineStack()
        self.event_stack = EventStack()
        self.component_map = {}
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
            self.exchange()
        elif action == Action.Retrieve:
            self.retrieve()
        elif action == Action.Event:
            self.event(arg)

        game_over = self.game_over()
        if game_over:
            self.player_blue.send_game_over(self.won())
            self.player_red.send_game_over(self.won())
            return

        self.change_player()
        self.run()

    def navigate(self, engine_card):
        if engine_card == EngineCard.SWAP:
            if self.curr_player.planet == OMEGA0:
                self.set_planets(OMEGA3, OMEGA3)
            elif self.curr_player.planet == OMEGA3:
                self.set_planets(OMEGA0, OMEGA0)
            else:
                self.set_planets(self.player_red.planet, self.player_blue.planet)
        else:
            blue, red = transition(self.curr_player.color, self.player_blue.planet, self.player_red.planet, engine_card)
            self.set_planets(blue, red)

        if self.player_blue.planet.galaxy == Galaxy.Entanglion:
            self.orbital_defense()
            # Detection rate may have been increased if an event was triggered above
            if self.game_over():
                return

        self.engine_control.add(engine_card)
        if self.engine_control.full():
            self.new_event()

        # Detection rate may have been increased if an event was triggered above
        if self.game_over():
            return

        self.exchange()

    def exchange(self):
        # draw new engine card, do the necessary if it's probe
        drawn = self.engine_stack.draw()
        if drawn == EngineCard.PROBE:
            roll = entanglion_roll()
            if roll > 4:
                self.set_detection_rate(self.detection_rate + 1)
                self.player_blue.send_probe_notification()
                self.player_red.send_probe_notification()

            self.engine_stack.reset()
            self.exchange()
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

            self.player_blue.send_components(self.component_map, self.player_red.components)
            self.player_red.send_components(self.component_map, self.player_blue.components)
        else:
            self.set_detection_rate(self.detection_rate + 1)

    def event(self, event):
        if event == Event.Bennett:
            give, comp = self.curr_player.ask_bennett(len(self.other_player().components) != 0)
            if give:
                self.other_player().give_bennett(comp)
            else:
                comp = self.other_player().ask_bennett_forcefully()
                self.curr_player.give_bennett(comp)

        elif event == Event.Heisenberg:
            roll = entanglion_roll()
            planet = CLOCKWISE_TABLE[roll]
            self.set_planets(planet, planet)

        elif event == Event.Tunnel:
            raise Exception("TODO")
        elif event == Event.Mechanic:
            raise Exception("TODO")
        elif event == Event.Error:
            self.set_detection_rate(6)  # 6 corresponds to the "first 4"
        elif event == Event.Schrodinger:
            self.set_detection_rate(self.detection_rate + 1)
        elif event == Event.Spooky:
            if len(self.curr_player.components) == 0:
                return

            unoccupied_planets = []
            for i in range(8):
                if not CLOCKWISE_TABLE[i + 1] in self.component_map:
                    unoccupied_planets += CLOCKWISE_TABLE[i + 1]

            index = entanglion_roll() % len(unoccupied_planets)
            planet = unoccupied_planets[index]
            component = random.choice(self.curr_player.components)
            self.component_map[planet] = component
            self.player_blue.send_components(self.component_map, self.player_red.components)
            self.player_red.send_components(self.component_map, self.player_blue.components)

        elif event == Event.Collapse:
            self.set_detection_rate(max(self.detection_rate - 2, 1))

        else:
            raise Exception("Invalid event")

    # Game helping functions

    def new_event(self):
        drawn = self.event_stack.draw()
        if drawn is None:
            self.player_blue.send_event_shuffled()
            self.player_red.send_event_shuffled()
            self.new_event()
        else:
            if drawn.can_save_for_later():
                self.curr_player.event_deck += drawn
                self.player_blue.send_event_decks(self.player_red.event_deck)
                self.player_red.send_event_decks(self.player_blue.event_deck)
                return

            self.player_blue.send_event_played(drawn)
            self.player_red.send_event_played(drawn)
            self.event(drawn)

    def orbital_defense(self):
        roll = entanglion_roll()
        if roll <= self.detection_rate:
            c_roll = centarious_roll()
            if c_roll == 0:
                self.set_planets(ZERO, ZERO)
            else:
                self.set_planets(ONE, ONE)
            self.set_detection_rate(self.detection_rate + 1)
            self.new_event()
        else:
            self.player_blue.send_orbdef_evaded()
            self.player_red.send_orbdef_evaded()

    def set_planets(self, blue, red):
        self.player_blue.planet = blue
        self.player_red.planet = red

        self.player_blue.send_locations(self.player_red.planet)
        self.player_red.send_locations(self.player_blue.planet)

    def set_detection_rate(self, new_rate):
        self.detection_rate = new_rate
        self.player_blue.send_dRate(self.detection_rate)
        self.player_red.send_dRate(self.detection_rate)

    def other_player(self):
        return self.player_blue if self.curr_player is self.player_red else self.player_red

    def won(self):
        return len(self.component_map) == 0

    def game_over(self):
        return self.won() or self.detection_rate == MAX_DETECTION_RATE

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

        self.player_blue.send_components(self.component_map, [])
        self.player_red.send_components(self.component_map, [])
