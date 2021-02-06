using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class EngineDeckBehaviour : MonoBehaviour
{
    bool firstTime;
    public enum EngineCard : ushort
    {
        H = 0,
        CNOT = 1,
        X = 2,
        SWAP = 3,
        PROBE = 4,
        nEngineCards = 5

    }
    readonly static int nH = 8;
    readonly static int nCNOT = 7;
    readonly static int nX = 5;
    readonly static int nSWAP = 3;
    readonly static int nPROBE = 1;

    Dictionary<int, int> countMap = new Dictionary<int, int>();
    // Start is called before the first frame update
    void Start()
    {
        firstTime = true;
        countMap.Add((int) EngineCard.H, nH);
        countMap.Add((int) EngineCard.CNOT, nCNOT);
        countMap.Add((int) EngineCard.X, nX);
        countMap.Add((int) EngineCard.SWAP, nSWAP);
        countMap.Add((int) EngineCard.PROBE, nPROBE);
    }
    public EngineCard drawCard()
    {
        if (firstTime)
        {
            if (countMap[0] == 0 && countMap[1] == 0 && countMap[2] == 0 && countMap[3] == 0)
            {
                countMap[(int) EngineCard.PROBE]--;
                return EngineCard.PROBE;
            }
            else{
                ArrayList temp = new ArrayList();
                for(EngineCard card = EngineCard.H; card < EngineCard.PROBE; card++)
                {
                    for(int i = 0; i < countMap[(int)card]; i++)
                    {
                        temp.Add(card);
                    }
                }
                EngineCard drawn = (EngineCard) temp[Random.Range(0, temp.Count)];
                countMap[(int)drawn]--;
                return drawn;
            }
        }
        else
        {
            ArrayList temp = new ArrayList();
            for (EngineCard card = EngineCard.H; card < EngineCard.nEngineCards; card++)
            {
                for (int i = 0; i < countMap[(int)card]; i++)
                {
                    temp.Add(card);
                }
            }
            EngineCard drawn = (EngineCard)temp[Random.Range(0, temp.Count)];
            countMap[(int)drawn]--;
            return drawn;
        }
    }
    public void reshuffle()
    {
        firstTime = false;
        countMap.Add((int)EngineCard.H, nH);
        countMap.Add((int)EngineCard.CNOT, nCNOT);
        countMap.Add((int)EngineCard.X, nX);
        countMap.Add((int)EngineCard.SWAP, nSWAP);
        countMap.Add((int)EngineCard.PROBE, nPROBE);
    }
    // Update is called once per frame
    void Update()
    {
        
    }
}

/*
export class EngineStack
{
    constructor()
    {
        this.never_reset = true;
        this.card_stack = new Map();

        for (var i = 0; i < EngineCards.length; ++i)
        {
            this.card_stack.set(EngineCards[i], EngineCard.initial_count[EngineCards[i]]);
        }
    }

    empty()
    {
        return this.card_stack.size === 0;
    }

    reset(blue_deck, red_deck, mechanic_deck)
    {
        for (var i = 0; i < EngineCards.length; ++i)
        {
            this.card_stack.set(EngineCards[i], EngineCard.initial_count[EngineCards[i]]);
        }

        for (var i = 0; i < blue_deck.length; ++i)
        {
            this.card_stack.set(blue_deck[i], this.card_stack.get(blue_deck[i]) - 1)
        }

        for (var i = 0; i < red_deck.length; ++i)
        {
            this.card_stack.set(red_deck[i], this.card_stack.get(red_deck[i]) - 1)
        }

        for (var i = 0; i < mechanic_deck.length; ++i)
        {
            this.card_stack.set(mechanic_deck[i], this.card_stack.get(mechanic_deck[i]) - 1)
        }

        this.never_reset = false;
    }

    rand()
    {
        var array = [];

        for (var[key, value] of this.card_stack)
        {
            for (let i = 0; i < value; ++i)
            {
                array.push(key);
            }
        }

        return array[Math.floor(Math.random() * array.length)];
    }

    draw()
    {
        var drawn = null;
        if (this.never_reset)
        {
            this.card_stack.delete(EngineCard.PROBE);
            if (this.empty())
            {
                return EngineCard.PROBE;
            }
            drawn = this.rand();
            this.card_stack.set(EngineCard.PROBE, EngineCard.initial_count[EngineCard.PROBE]);
        }
        else
        {
            drawn = this.rand();
        }

        this.card_stack.set(drawn, this.card_stack.get(drawn) - 1);
        if (this.card_stack.get(drawn) === 0)
        {
            this.card_stack.delete(drawn);
        }

        return drawn;
    }
}

export class EngineControl
{
    constructor()
    {
        this.control = [];
    }

    full()
    {
        this.control.length === ENGINE_CONTROL_MAX_SIZE;
    }

    add(engine_card)
    {
        if (this.full())
        {
            throw new Error("Engine Control full, Engine Card cannot be added!");
        }
        self.control.push(engine_card);
    }

    reset()
    {
        this.control = [];
    }

    get()
    {
        return this.control;
    }
}


export function centarious_roll()
{
    return Math.floor(Math.random() * 2);
}

export function entanglion_roll()
{
    return Math.ceil(Math.random() * 8);
}

export const Color = Object.freeze({
    'Blue': 0,
    'Red': 1
});

export const Galaxy = Object.freeze({
    'Centarious': 0,
    'Superious': 1,
    'Entanglion': 2
});

export const Component = Object.freeze({
    'Physical_Qubits': 3,
    'Qubit_Interconnect': 6,
    'Dilution_Refrigerator': 2,
    'Quantum_Gates': 1,
    'Quantum_Programming': 4,
    'Quantum_Error_Correction': 5,
    'Control_Infrastructure': 7,
    'Magnetic_Shielding': 0
});

export const Action = Object.freeze({
    'Navigate': 1,
    'Exchange': 2,
    'Retrieve': 3,
    'Event': 4
});

export const EngineCard = Object.freeze({
    'H': 1,
    'CNOT': 2,
    'X': 3,
    'SWAP': 4,
    'PROBE': 5,
    'initial_count': {
        1: 8,
        2: 7,
        3: 5,
        4: 3,
        5: 1
    }
})

export const EngineCards = [EngineCard.H, EngineCard.CNOT, EngineCard.X, EngineCard.SWAP, EngineCard.PROBE];

export const MAX_DETECTION_RATE = 12;
export const DETECTION_MAP = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8];

export const ENGINE_CONTROL_MAX_SIZE = 6;
export const ENGINE_DECK_INIT_SIZE = 3; */