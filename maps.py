from pprint import pprint
from typing import List


game_map: List[List[str]] = [
    [
        '№', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'
    ],
    [
        '1', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
    ],
    [
        '2', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
    ],
    [
        '3', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
    ],
    [
        '4', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
    ],
    [
        '5', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
    ],
    [
        '6', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
    ],
    [
        '7', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
    ],
    [
        '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
    ],
    [
        '9', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
    ]
]

# Custop maps
map1: List[List[str]] = [
    [
        '№', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'
    ],
    [
        '1', 's', ' ', 's', ' ', 's', ' ', 's', ' ', ' '
    ],
    [
        '2', 's', ' ', 's', ' ', 's', ' ', 's', ' ', ' '
    ],
    [
        '3', 's', ' ', 's', ' ', 's', ' ', 's', ' ', ' '
    ],
    [
        '4', 's', ' ', ' ', ' ', ' ', 's', ' ', 's', ' '
    ],
    [
        '5', 's', ' ', 's', 's', ' ', 's', ' ', 's', ' '
    ],
    [
        '6', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
    ],
    [
        '7', ' ', ' ', 's', 's', 's', 's', ' ', ' ', ' '
    ],
    [
        '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
    ],
    [
        '9', ' ', ' ', 's', 's', 's', 's', ' ', ' ', ' '
    ]
]

map2: List[List[str]] = [
    [
        '№', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'
    ],
    [
        '1', 's', ' ', 's', ' ', 's', 's', 's', 's', 's'
    ],
    [
        '2', 's', ' ', 's', ' ', ' ', ' ', ' ', ' ', ' '
    ],
    [
        '3', 's', ' ', 's', ' ', ' ', ' ', 's', ' ', 's'
    ],
    [
        '4', ' ', ' ', ' ', ' ', ' ', ' ', 's', ' ', 's'
    ],
    [
        '5', 's', 's', 's', ' ', ' ', ' ', 's', ' ', 's'
    ],
    [
        '6', ' ', ' ', ' ', ' ', ' ', ' ', 's', ' ', 's'
    ],
    [
        '7', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
    ],
    [
        '8', 's', 's', ' ', 's', 's', ' ', 's', 's', ' '
    ],
    [
        '9', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
    ]
]

map3: List[List[str]] = [
    [
        '№', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'
    ],
    [
        '1', ' ', 's', 's', 's', ' ', 's', 's', 's', ' '
    ],
    [
        '2', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
    ],
    [
        '3', 's', ' ', ' ', 's', 's', 's', ' ', ' ', ' '
    ],
    [
        '4', 's', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
    ],
    [
        '5', ' ', 's', 's', 's', 's', 's', ' ', ' ', ' '
    ],
    [
        '6', 's', ' ', ' ', ' ', ' ', ' ', 's', ' ', ' '
    ],
    [
        '7', 's', ' ', 's', ' ', 's', ' ', 's', ' ', ' '
    ],
    [
        '8', 's', ' ', 's', ' ', 's', ' ', 's', ' ', ' '
    ],
    [
        '9', 's', ' ', ' ', ' ', ' ', ' ', 's', ' ', ' '
    ]
]

map4: List[List[str]] = [
    [
        '№', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'
    ],
    [
        '1', 's', ' ', ' ', ' ', ' ', ' ', 's', 's', 's'
    ],
    [
        '2', 's', ' ', ' ', 's', ' ', 's', ' ', ' ', ' '
    ],
    [
        '3', 's', ' ', ' ', 's', ' ', 's', ' ', ' ', ' '
    ],
    [
        '4', ' ', ' ', ' ', 's', ' ', ' ', 's', 's', 's'
    ],
    [
        '5', 's', ' ', ' ', 's', ' ', ' ', ' ', ' ', ' '
    ],
    [
        '6', 's', ' ', ' ', 's', ' ', 's', ' ', ' ', 's'
    ],
    [
        '7', ' ', ' ', ' ', ' ', ' ', 's', ' ', ' ', 's'
    ],
    [
        '8', ' ', 's', 's', ' ', ' ', 's', ' ', ' ', 's'
    ],
    [
        '9', ' ', ' ', ' ', ' ', ' ', 's', ' ', ' ', 's'
    ]
]

map5: List[List[str]] = [
    [
        '№', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'
    ],
    [
        '1', 's', ' ', 's', ' ', 's', 's', ' ', 's', ' '
    ],
    [
        '2', 's', ' ', 's', ' ', ' ', ' ', ' ', 's', ' '
    ],
    [
        '3', 's', ' ', 's', ' ', 's', 's', ' ', 's', ' '
    ],
    [
        '4', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 's', ' '
    ],
    [
        '5', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
    ],
    [
        '6', ' ', 's', 's', 's', 's', 's', ' ', ' ', ' '
    ],
    [
        '7', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 's'
    ],
    [
        '8', ' ', 's', 's', 's', 's', ' ', 's', ' ', 's'
    ],
    [
        '9', ' ', ' ', ' ', ' ', ' ', ' ', 's', ' ', 's'
    ]
]

maps: List[List[List[str]]] = [
    map1, map2, map3, map4, map5
]


if __name__ == '__main__':
    pprint(map3)