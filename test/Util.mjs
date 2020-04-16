export function centarious_roll() {
    return Math.floor(Math.random() * 2);
}

export function entanglion_roll() {
    return Math.ceil(Math.random() * 8);
}

export var Color = Object.freeze({
    Blue: true,
    Red: false
})

export var Galaxy = Object.freeze({
    Centarious: 0,
    Superious: 1,
    Entanglion: 2
})

export var Component = Object.freeze({
    Physical_Qubits: 0,
    Qubit_Interconnect: 1,
    Dilution_Refrigerator: 2,
    Quantum_Gates: 3,
    Quantum_Programming: 4,
    Quantum_Error_Correction: 5,
    Control_Infrastructure: 6,
    Magnetic_Shielding: 7
})

export var Action = Object.freeze({
    Navigate: 1,
    Exchange: 2,
    Retrieve: 3,
    Event: 4
})

export const MAX_DETECTION_RATE = 12;
export const DETECTION_MAP = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8];
