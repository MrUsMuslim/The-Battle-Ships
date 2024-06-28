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
    'titanic': {
        'length': 5,
        'number_of_ships': 1
    },
    'large': {
        'length': 4,
        'number_of_ships': 2
    },
    'standard': {
        'length': 3,
        'number_of_ships': 3
    },
    'small': {
        'length': 2,
        'number_of_ships': 3
    },
}