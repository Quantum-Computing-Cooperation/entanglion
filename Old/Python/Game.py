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
        self.ground_defenses = True
        self.orbital_defenses = True
        self.mechanic_deck = []

    def start(self):
        self.distribute_components()
        self.determine_first_player()
        self.determine_init_locations()
        self.draw_engine_cards()
        self.run()

    def run(self):
        if len(self.mechanic_deck) > 1:
            engine_card = self.curr_player.ask_mechanic()
            if engine_card is None:
                self.mechanic_deck.clear()
                self.player_blue.send_mechanic_done()
                self.player_red.send_mechanic_done()
            else:
                self.orbital_defenses = False
                self.mechanic_deck.remove(engine_card)
                self.navigate(engine_card)
                self.change_player()
                self.player_blue.send_mechanic_deck(self.mechanic_deck)
                self.player_red.send_mechanic_deck(self.mechanic_deck)
                # if the list drops to size 1, we need to send mechanic_over
        else:
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
            new = transition(self.curr_player.color, self.player_blue.planet, self.player_red.planet, engine_card)
            if new.galaxy == Galaxy.Entanglion:
                self.set_planets(new, new)
            else:
                curr_color = self.curr_player.color
                if curr_color == Color.Blue:
                    self.set_planets(new, self.player_red.planet)
                else:
                    self.set_planets(self.player_blue.planet, new)

        if self.player_blue.planet.galaxy == Galaxy.Entanglion:
            if self.orbital_defenses:
                self.orbital_defense()
                # Detection rate may have been increased if an event was triggered above
                if self.game_over():
                    return
            else:
                self.orbital_defenses = True

        self.engine_control.add(engine_card)
        if self.engine_control.full():
            self.engine_control.reset()
            self.new_event()

        self.player_blue.send_engine_control(self.engine_control)
        self.player_red.send_engine_control(self.engine_control)

        # Detection rate may have been increased if an event was triggered above
        if self.game_over():
            return

        if len(self.mechanic_deck) == 0:  # We are not in the middle of a Mechanic event
            self.exchange(engine_card)

    def exchange(self, thrown: EngineCard):
        self.curr_player.engine_deck.remove(thrown)
        drawn = self.draw_card()
        self.curr_player.engine_deck.append(drawn)
        self.player_blue.send_engine_decks(self.player_red.engine_deck)
        self.player_red.send_engine_decks(self.player_blue.engine_deck)

    def draw_card(self):
        # Draw new engine card, do the necessary if it's probe
        drawn = self.engine_stack.draw()
        if self.engine_stack.empty():
            self.engine_stack.reset(self.player_blue.engine_deck, self.player_red.engine_deck, self.mechanic_deck)
        if drawn == EngineCard.PROBE:
            roll = entanglion_roll()
            if roll <= 4:
                self.set_detection_rate(self.detection_rate + 1)

            self.player_blue.send_probe_notification()
            self.player_red.send_probe_notification()
            return self.draw_card()
        else:
            return drawn

    def retrieve(self):
        if self.ground_defenses:
            roll = entanglion_roll()
            if roll <= DETECTION_MAP[self.detection_rate - 1]:
                self.set_detection_rate(self.detection_rate + 1)
                return
        else:
            self.ground_defenses = True

        component = self.component_map[self.curr_player.planet]
        del self.component_map[self.curr_player.planet]
        self.curr_player.components.append(component)

        self.player_blue.send_components(self.component_map, self.player_red.components)
        self.player_red.send_components(self.component_map, self.player_blue.components)

    def event(self, event):
        if event == Event.Bennett:
            if len(self.player_blue.components) == 0 and len(self.player_red.components) == 0:
                return
            give, comp = self.curr_player.ask_bennett(len(self.other_player().components) != 0)
            if give:
                self.other_player().give_bennett(comp)
            else:
                comp = self.other_player().ask_bennett_forcefully()
                self.curr_player.give_bennett(comp)

        elif event == Event.Heisenberg:
            roll = entanglion_roll()
            planet = CLOCKWISE_TABLE[roll - 1]
            self.set_planets(planet, planet)

        elif event == Event.Tunnel:
            orb = self.curr_player.ask_tunnel_orbital_or_ground()
            if orb:
                self.orbital_defenses = False
            else:
                self.ground_defenses = False
            self.change_player()  # So that the curr player stays the curr player in the next turn

        elif event == Event.Mechanic:
            for i in range(3):
                self.mechanic_deck.append(self.draw_card())
                if self.game_over():
                    return

            self.change_player()  # So that the curr player stays the curr player in the next turn
            self.player_blue.send_mechanic_deck(self.mechanic_deck)
            self.player_red.send_mechanic_deck(self.mechanic_deck)

        elif event == Event.Error:
            self.set_detection_rate(6)  # 6 corresponds to the "first 4"

        elif event == Event.Schrodinger:
            self.set_detection_rate(self.detection_rate + 1)

        elif event == Event.Spooky:
            if len(self.curr_player.components) == 0:
                return

            unoccupied_planets = []
            for i in range(8):
                if not CLOCKWISE_TABLE[i] in self.component_map:
                    unoccupied_planets.append(CLOCKWISE_TABLE[i])

            index = entanglion_roll() % len(unoccupied_planets)
            planet = unoccupied_planets[index]
            component = random.choice(self.curr_player.components)
            self.component_map[planet] = component
            self.player_blue.send_components(self.component_map, self.player_red.components)
            self.player_red.send_components(self.component_map, self.player_blue.components)

        elif event == Event.Collapse:
            self.set_detection_rate(max(self.detection_rate - 2, 1))

    # Helper functions

    def new_event(self):
        drawn = self.event_stack.draw()
        if drawn is Event.Shuffle:
            self.player_blue.send_event_shuffled()
            self.player_red.send_event_shuffled()
            self.new_event()
        else:
            if drawn.can_save_for_later():
                self.curr_player.event_deck.append(drawn)
                self.player_blue.send_event_decks(self.player_red.event_deck)
                self.player_red.send_event_decks(self.player_blue.event_deck)
                return

            self.player_blue.send_event_played(drawn)
            self.player_red.send_event_played(drawn)
            self.event(drawn)

    def orbital_defense(self):
        roll = entanglion_roll()
        if roll <= DETECTION_MAP[self.detection_rate - 1]:
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
        if blue > red:
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
            self.player_blue.engine_deck.append(self.engine_stack.draw())
            self.player_red.engine_deck.append(self.engine_stack.draw())

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
