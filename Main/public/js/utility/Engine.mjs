import {EngineCard, ENGINE_CONTROL_MAX_SIZE, ENGINE_DECK_INIT_SIZE, EngineCards} from './Util.mjs';

export class EngineStack {
    constructor() {
        this.never_reset = true;
        this.card_stack = new Map();

        for (var i = 0; i < EngineCards.length; ++i) {
            this.card_stack.set(EngineCards[i], EngineCard.initial_count[EngineCards[i]]);
        }
    }

    empty() {
        return this.card_stack.size === 0;
    }

    reset(blue_deck, red_deck, mechanic_deck) {
        for (var i = 0; i < EngineCards.length; ++i) {
            this.card_stack.set(EngineCards[i], EngineCard.initial_count[EngineCards[i]]);
        }

        for (var i = 0; i < blue_deck.length; ++i) {
            this.card_stack.set(blue_deck[i], this.card_stack.get(blue_deck[i]) - 1)
        }

        for (var i = 0; i < red_deck.length; ++i) {
            this.card_stack.set(red_deck[i], this.card_stack.get(red_deck[i]) - 1)
        }

        for (var i = 0; i < mechanic_deck.length; ++i) {
            this.card_stack.set(mechanic_deck[i], this.card_stack.get(mechanic_deck[i]) - 1)
        }

        this.never_reset = false;
    }

    rand() {
        var array = [];

        for (var [key, value] of this.card_stack) {
            for (let i = 0; i < value; ++i) {
                array.push(key);
            }
        }

        return array[Math.floor(Math.random() * array.length)];
    }

    draw () {
        var drawn = null;
        if (this.never_reset) {
            this.card_stack.delete(EngineCard.PROBE);
            if (this.empty()) {
                return EngineCard.PROBE;
            }
            drawn = this.rand();
            this.card_stack.set(EngineCard.PROBE, EngineCard.initial_count[EngineCard.PROBE]);
        } else {
            drawn = this.rand();
        }

        this.card_stack.set(drawn, this.card_stack.get(drawn) - 1);
        if (this.card_stack.get(drawn) === 0) {
            this.card_stack.delete(drawn);
        }

        return drawn;
    }
}

export class EngineControl {
    constructor() {
        this.control = [];
    }

    full() {
        this.control.length === ENGINE_CONTROL_MAX_SIZE;
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

    get() {
        return this.control;
    }
}
