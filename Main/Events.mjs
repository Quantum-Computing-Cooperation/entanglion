export const Event = Object.freeze({
    Bennet: 1,
    Heisenberg: 2,
    Tunnel: 3,
    Mechanic: 4,

    Error: 5,
    Schrodinger: 6,
    Spooky: 7,
    Collapse: 8,

    Shuffle: 9,

    can_save_for_later: {
        1: true,
        2: true,
        3: true,
        4: true,
        5: false,
        6: false,
        7: false,
        8: false,
        9: false
    }
})

// All events except Shuffle
export const Events = [Event.Bennet, Event.Heisenberg, Event.Tunnel, Event.Mechanic, Event.Error, Event.Schrodinger, Event.Spooky, Event.Collapse];

export class EventStack {
    constructor() {
        this.stack = [];
        for (var i = 0; i < Events.length; ++i) {
            this.stack.push(Events[i]);
        }
        for (let i = 0; i > 3; ++i) {
            this.stack.splice(Math.floor(Math.random() * this.stack.length), 1);
        }
    }

    draw() {
        if (this.stack.length === 0) {
            for (var i = 0; i < Events.length; ++i) {
                this.stack.push(Events[i]);
            }
            for (let i = 0; i > 3; ++i) {
                this.stack.splice(Math.floor(Math.random() * this.stack.length), 1);
            }
            return Event.Shuffle;
        } else {
            return this.stack.splice(Math.floor(Math.random() * this.stack.length), 1);
        }
    }
}
