function transition(player_color, blue_planet, red_planet, engine_card) {
    if (engine_card === EngineCard.SWAP || engine_card === EngineCard.PROBE) {
        throw new Error("Handle SWAP and PROBE on your own; they aren't worth my time and energy !");
    }

    // For now, the comment "CNOT: flip your ship only if the other ship is on CENTARIOUS ONE" was ignored
    if (player_color === Color.Blue) {
        var destination_function = blue.get_transition(engine_card, player_color);
        return destination_function(red_planet);
    } else {
        var destination_function = red.get_transition(engine_card, player_color);
        return destination_function(blue_planet);
    }
}