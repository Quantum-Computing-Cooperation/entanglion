EngineCard = Object.freeze({
    H: 8,
    CNOT: 7,
    X: 5,
    SWAP: 3,
    PROBE: 1
})

class EngineStack {
    constructor() {
        this.never_reset = true;
        this.stack = new Map();

        EngineCard.entries.forEach(entry => this.stack.set(entry.key, entry.value));
    }

    empty() {
        return this.stack.size === 0;
    }

    reset(blue_deck, red_deck, mechanic_deck) {
        EngineCard.entries.forEach(entry => this.stack.set(entry.key, entry.value));
        function rm(item) {
            this.stack.set(item, this.stack.get(item) - 1);
        }

        blue_deck.foreach(rm);
        red_deck.foreach(rm);
        mechanic_deck.foreach(rm);

        this.never_reset = false;
    }

    draw () {
        drawn = null;
        function rand() {
            array = [];
            this.stack.entries.forEach(element => {
                for (let i = 0; i < element.value; ++i) {
                    array.push(element.key);
                }
            });

            return array[Math.floor(Math.random() * array.size)];
        }

        if (this.never_reset) {
            this.stack.delete(EngineCard.PROBE);
            if (this.empty()) {
                return EngineCard.PROBE;
            }
            drawn = rand();
            this.stack.set(EngineCard.PROBE.key, EngineCard.PROBE.value);
        } else {
            drawn = rand();
        }

        this.stack.set(drawn, this.stack.get(drawn) - 1);
        if (this.stack.get(drawn) == 0) {
            this.stack.delete(drawn);
        }

        return drawn;
    }
}

const ENGINE_CONTROL_MAX_SIZE = 6;
const ENGINE_DECK_INIT_SIZE = 3;

class EngineControl {
    constructor() {
        this.control = [];
    }

    full() {
        this.control.size === ENGINE_CONTROL_MAX_SIZE;
    }

    add(engine_card) {
        if (this.full()) {
            throw new Error("Engine Control full, Engine Card cannot be added!");
        }
        self.control.push(engine_card);
    }

    reset() {
        this.control = [];
    }
}