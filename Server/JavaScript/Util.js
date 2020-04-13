function centarious_roll() {
    return Math.floor(Math.random() * 2);
}

function entanglion_roll() {
    return Math.ceil(Math.random() * 8);
}

Color = Object.freeze({
    Blue: true,
    Red: false
})

Galaxy = Object.freeze({
    Centarious: 0,
    Superious: 1,
    Entanglion: 2
})

Component = Object.freeze({
    Physical_Qubits: 0,
    Qubit_Interconnect: 1,
    Dilution_Refrigerator: 2,
    Quantum_Gates: 3,
    Quantum_Programming: 4,
    Quantum_Error_Correction: 5,
    Control_Infrastructure: 6,
    Magnetic_Shielding: 7
})

Action = Object.freeze({
    Navigate: 1,
    Exchange: 2,
    Retrieve: 3,
    Event: 4
})

const MAX_DETECTION_RATE = 12;
const DETECTION_MAP = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8];
