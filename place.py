from typing import List


def place_up(length: int, player_map: List[List[str]], coordinates: List[int]) -> bool:
    """
    :param length: The length of the ship\n
    :param player_map: The map player having\n
    :param coordinates: Coordinates of the head of the ship\n
    ____________________________________________________________\n
    Checks if possible to place ship up\n
    Coordinates can be taken by get_coordinates()
    """

    x: int = coordinates[0]
    y: int = coordinates[1]

    for i in range(length):
        if player_map[y - i][x] != ' ':
            return False

    return True

def place_down(length: int, player_map: List[List[str]], coordinates: List[int]) -> bool:
    """
    :param length: The length of the ship\n
    :param player_map: The map player having\n
    :param coordinates: Coordinates of the head of the ship\n
    ____________________________________________________________\n
    Checks if possible to place ship down\n
    Coordinates can be taken by get_coordinates()
    """

    x: int = coordinates[0]
    y: int = coordinates[1]

    for i in range(length):
        try:
            if player_map[y + i][x] != ' ':
                return False
        except IndexError:
            return False

    return True

def place_left(length: int, player_map: List[List[str]], coordinates: List[int]) -> bool:
    """
    :param length: The length of the ship\n
    :param player_map: The map player having\n
    :param coordinates: Coordinates of the head of the ship\n
    ____________________________________________________________\n
    Checks if possible to place ship left\n
    Coordinates can be taken by get_coordinates()
    """

    x: int = coordinates[0]
    y: int = coordinates[1]

    for i in range(length):
        if player_map[y][x - i] != ' ':
            return False

    return True


def place_right(length: int, player_map: List[List[str]], coordinates: List[int]) -> bool:
    """
    :param length: The length of the ship\n
    :param player_map: The map player having\n
    :param coordinates: Coordinates of the head of the ship\n
    ____________________________________________________________\n
    Checks if possible to place ship right\n
    Coordinates can be taken by get_coordinates()
    """

    x: int = coordinates[0]
    y: int = coordinates[1]

    for i in range(length):
        try:
            if player_map[y][x + i] != ' ':
                return False
        except IndexError:
            return False

    return True

def place(length: int, direction: str, player_map: List[List[str]], coordinates: List[int]) -> None:
    """
    :param length: The length of the ship\n
    :param direction: Direction the ship look\n
    :param player_map: The map player having\n
    :param coordinates: Coordinates of the head of the ship\n
    ______________________________________________________________\n
    Places the ship in the player's map\n
    Coordinates can be taken by get_coordinates()
    """

    x: int = coordinates[0]
    y: int = coordinates[1]

    if direction == 'down':
        for i in range(length):
            player_map[y + i][x] = 's'
    elif direction == 'right':
        for i in range(length):
            player_map[y][x + i] = 's'
    elif direction == 'up':
        for i in range(length):
            player_map[y - i][x] = 's'
    elif direction == 'left':
        for i in range(length):
            player_map[y][x - i] = 's'
