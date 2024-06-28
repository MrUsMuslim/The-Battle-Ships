from typing import Dict, List

letters_coordinate: Dict[str, int] = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 5,
    'F': 6,
    'G': 7,
    'H': 8,
    'I': 9
}

ships: Dict[str, Dict[str, int]] = {
    'battleship': {
        'length': 5,
        'number_of_ships': 1
    },
    'kreuzer': {
        'length': 4,
        'number_of_ships': 2
    },
    'destroyers': {
        'length': 3,
        'number_of_ships': 3
    },
    'submarines': {
        'length': 2,
        'number_of_ships': 3
    },
}
