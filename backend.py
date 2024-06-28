import os

from typing import List
from time import sleep
from copy import deepcopy
from pprint import pprint

from maps import game_map, maps
from shared import letters_coordinate, ships
from place import (
    place_up,
    place_right,
    place_down,
    place_left,
    place
)


def clear_screen() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

def remove_and_join(directions: List[str | None]) -> str:
    """
    :param directions: The directions the ship can look\n
    ______________________________________________________\n
    Removes unpossible directions
    """

    element = None
    while element in directions:
        directions.remove(element)

    return ', '.join(directions)

def get_players_names() -> List[str]:
    """
    Gets the names' of the players\n
    Returns:
        Dict[str, str]: names of the players. keys = player_1 or player_2
    """

    player_1: str = input('\n\nNow, first player enter your name: ').title()
    player_2: str = input('OK, second player enter your name as well: ').title()

    return [player_1, player_2]


def get_coordinates() -> List[int | str]:
    """
    Gets coordinates to place ship\n
    Returns:
        List[int]: coordinates of the head of the ship
    """

    while True:
        x_letter: int = input(f"Enter X coordinate ({', '.join(list(letters_coordinate.keys()))}): ").upper()
        if x_letter in list(letters_coordinate.keys()):
            x = letters_coordinate.get(x_letter)
            break
        print("Enter valid coordinate!\n")

    while True:
        y: int = input("Enter Y coordinate (1-9): ")
        if y.isdigit() and int(y) in list(range(1, 10)):
            break
        print("Enter valid coordinate!\n")

    return [x, int(y), x_letter]

def create_opponent_map() -> List[List[str]]:
    """
    Creates changed map
    """
    return deepcopy(game_map)

def create_map(players: List[str], player_index: int) -> List[List[str]]:
    """
    :param players: Names of the players\n
    :param player_index: The number of the player\n
    ___________________________________________________________\n
    Use get_players_names() function to get players' names.\n
    Creates map for a player
    """

    player_map: List[List[str]] = create_opponent_map()
    type_of_ships: List[str] = list(ships.keys())

    print(f"{players[player_index]} start to place your ships\nNote: You shouldn't show to your opponent.\n")
    sleep(1)

    print("By the way, there are 5 maps in which ships were placed.")

    while True:
        question: str = input("Do you want to see? (y/n): ").lower()
        if question == 'y':
            for (i, default_map) in enumerate(maps):
                print(f"Map {i + 1}:\n", end=' ')
                pprint(default_map)

            while True:
                default_map: List[List[str]] | str = input(f"Choose one of the map (1-{len(maps)}) or type exit to place manually: ").lower()
                if default_map == 'exit':
                    break
                elif int(default_map) in list(range(1, 6)):
                    return maps[int(default_map) - 1]
        break

    for i in range(4): # len(ships) = 4
        clear_screen()
        name_ship: str = type_of_ships[i]
        length: int = ships[type_of_ships[i]]['length']

        for num_ship in range(ships[name_ship]['number_of_ships']):
            print('Map:')
            pprint(player_map)
            print(f"\nPlace {num_ship + 1}-{name_ship} ship.")

            while True:
                coordinates: List[int] = get_coordinates()
                possible_directions: str = remove_and_join(
                    [
                        'up' if place_up(length, player_map, coordinates) else None,
                        'down' if place_down(length, player_map, coordinates) else None,
                        'left' if place_left(length, player_map, coordinates) else None,
                        'right' if place_right(length, player_map, coordinates) else None
                    ]
                )

                if possible_directions:
                    break
                print(f"Enter another directions because it is not possible to place ({name_ship}) on {coordinates[2], coordinates[1]} coordinates!\n")
            
            while True:
                direction: str = input(f"Enter the direction the ship looks {possible_directions}: ").lower()

                if direction in possible_directions:
                    break
                print("Enter valid direction")

            place(length, direction, player_map, coordinates)
    return player_map


def shoot(coordinates: List[str | int], player_map: List[List[str]], player_opponent_map: List[List[str]]) -> List[List[List[str]] | bool]:
    """
    :param coordinates: Coordinates\n
    :param player_map: The map of player\n
    :param player_opponent_map: The player's opponent map\n
    _____________________________________\n
    Returns True if shoots
    """

    x, y, = coordinates[0], coordinates[1]

    if player_map[y][x] == 'x':
        return [player_opponent_map, None]
    elif player_map[y][x] == 's':
        player_opponent_map[y][x] = 'x'
        player_map[y][x] = 'x'
        return [player_opponent_map, True]
    return [player_opponent_map, False]

if __name__ == '__main__':
    from maps import map5
    
    shoot([1, 1, 'A'], map5)