import {Color, Galaxy, EngineCard} from './Util.mjs';

class Planet {
    constructor(name, galaxy) {
        this.name = name;
        this.galaxy = galaxy;
        this.blue_transitions = new Map();
        this.red_transitions = new Map();
    }

    toJSON() {
        return this.name;
    }

    set_transitions(h, x, cnot, color=null) {
        var transitions = new Map(); //EngineCard -> (Function(EngineCard) -> Planet)
        transitions.set(EngineCard.H, h);
        transitions.set(EngineCard.X, x);
        transitions.set(EngineCard.CNOT, cnot);

        switch (color) {
            case Color.Blue:
                this.blue_transitions = transitions;
                break;
            case Color.Red:
                this.red_transitions = transitions;
                break;
            default:
                this.blue_transitions = transitions;
                this.red_transitions = transitions;
        }
    }

    get_transition_function(engine_card, color) {
        switch (color) {
            case Color.Blue:
                return this.blue_transitions.get(engine_card);
            case Color.Red:
                return this.red_transitions.get(engine_card);
            default:
                throw new Error();
        }
    }
}

export const ONE = new Planet('ONE', Galaxy.Centarious);
export const ZERO = new Planet('ZERO', Galaxy.Centarious);

export const PLUS = new Planet('PLUS', Galaxy.Superious);
export const MINUS = new Planet('MINUS', Galaxy.Superious);

export const PSI_PLUS = new Planet('PSI PLUS', Galaxy.Entanglion);
export const PSI_MINUS = new Planet('PSI MINUS', Galaxy.Entanglion);
export const PHI_PLUS = new Planet('PHI PLUS', Galaxy.Entanglion);
export const PHI_MINUS = new Planet('PHI MINUS', Galaxy.Entanglion);
export const OMEGA0 = new Planet('OMEGA ZERO', Galaxy.Entanglion);
export const OMEGA1 = new Planet('OMEGA ONE', Galaxy.Entanglion);
export const OMEGA2 = new Planet('OMEGA TWO', Galaxy.Entanglion);
export const OMEGA3 = new Planet('OMEGA THREE', Galaxy.Entanglion);

// null represents an impossible transition
ONE.set_transitions(x => MINUS, x => ZERO, x => ZERO);
ZERO.set_transitions(x => PLUS,x => ONE,x => ONE);

PLUS.set_transitions(x => ZERO, x => null, planet => planet === ONE ? PSI_PLUS : PHI_PLUS);
MINUS.set_transitions(x => ONE, x => null, planet => planet === ONE ? PSI_MINUS : PHI_MINUS);

PSI_PLUS.set_transitions(x => OMEGA3, x => PHI_PLUS, x => null, Color.Blue);
PSI_PLUS.set_transitions(x => OMEGA0, x => PHI_PLUS, x => null, Color.Red);

PSI_MINUS.set_transitions(x => OMEGA1, x => PHI_MINUS, x => null);
PHI_PLUS.set_transitions(x => OMEGA2, x => PSI_PLUS, x => null);

PHI_MINUS.set_transitions(x => OMEGA0, x => PSI_MINUS, x => null, Color.Blue);
PHI_MINUS.set_transitions(x => OMEGA3, x => PSI_MINUS, x => null, Color.Red);

OMEGA0.set_transitions(x => PHI_MINUS, x => OMEGA2, x => OMEGA2, Color.Blue);
OMEGA0.set_transitions(x => PSI_PLUS, x => OMEGA1, x => null, Color.Red);

OMEGA1.set_transitions(x => PSI_MINUS, x => OMEGA3, x => null, Color.Blue);
OMEGA1.set_transitions(x => PSI_MINUS, x => OMEGA0, x => null, Color.Red);

OMEGA2.set_transitions(x => PHI_PLUS, x => OMEGA0, x => OMEGA0, Color.Blue);
OMEGA2.set_transitions(x => PHI_PLUS, x => OMEGA3, x => OMEGA3, Color.Red);

OMEGA3.set_transitions(x => PSI_PLUS, x => OMEGA1, x => null, Color.Blue);
OMEGA3.set_transitions(x => PHI_MINUS, x => OMEGA2, x => OMEGA2, Color.Red);

export const CLOCKWISE_TABLE = [OMEGA0, OMEGA1, PSI_MINUS, PHI_MINUS, OMEGA3, OMEGA2, PHI_PLUS, PSI_PLUS];
