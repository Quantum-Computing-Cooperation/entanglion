class Planet {
    constructor(name, galaxy) {
        this.name = name;
        this.galaxy = galaxy;
        this.blue_transitions = new Map();
        this.red_transitions = new Map();
    }

    set_transition_functions(h, x, cnot, color=null) {
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

const ONE = Planet("ONE", Galaxy.Centarious);
const ZERO = Planet("ZERO", Galaxy.Centarious);

const PLUS = Planet("PLUS", Galaxy.Superious);
const MINUS = Planet("MINUS", Galaxy.Superious);

const PSI_PLUS = Planet("PSI PLUS", Galaxy.Entanglion);
const PSI_MINUS = Planet("PSI MINUS", Galaxy.Entanglion);
const PHI_PLUS = Planet("PHI PLUS", Galaxy.Entanglion);
const PHI_MINUS = Planet("PHI MINUS", Galaxy.Entanglion);
const OMEGA0 = Planet("OMEGA ZERO", Galaxy.Entanglion);
const OMEGA1 = Planet("OMEGA ONE", Galaxy.Entanglion);
const OMEGA2 = Planet("OMEGA TWO", Galaxy.Entanglion);
const OMEGA3 = Planet("OMEGA THREE", Galaxy.Entanglion);

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

CLOCKWISE_TABLE = [OMEGA0, OMEGA1, PSI_MINUS, PHI_MINUS, OMEGA3, OMEGA2, PHI_PLUS, PSI_PLUS];