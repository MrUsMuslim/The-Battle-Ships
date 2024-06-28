from typing import List
from time import sleep
from pprint import pprint

from backend import (
    get_coordinates,  
    get_players_names, 
    create_map, 
    clear_screen,
    shoot,
    create_opponent_map
)

from introduction import greet, introduce, explain_rules


def main() -> None:
    # Greetings & Intruduction & Rules
    greet()
    introduce()
    explain_rules()

    # Asking players if they understood the game
    is_understood: str = input("Shall we continue (y/n)? ").lower()
    if is_understood == 'y':
        clear_screen()
    else:
        print("Look at the documentation, please")


    # Taking players' names
    players: List[str] = get_players_names()

    # Placing ships starts
    clear_screen()
    print("Let's start to place ships, Players!!!\n")

    # 1st player's map
    player_1_map: List[List[str]] = create_map(players, 0)
    clear_screen()
    pprint(player_1_map)
    print(f'Take a look to your map {players[0].title()}.\nThe screen will be cleaned in 5 seconds')
    sleep(5)
    clear_screen()

    # 2nd player's map
    player_2_map: List[List[str]] = create_map(players, 1)
    clear_screen()
    pprint(player_2_map)
    print(f'Take a look to your map {players[1].title()}.\nThe screen will be cleaned in 5 seconds')
    sleep(5)
    clear_screen()

    # GAME STARTS
    
    # NUmber of correct shoots.
    CORRECT_SHOOTS: int = 28
    player_1_correct_shoots: int = 0
    player_2_correct_shoots: int = 0

    # Creating maps for player to see opponet's ships
    player_1_opponent_map: List[List[str]] = create_opponent_map()
    player_2_opponent_map: List[List[str]] = create_opponent_map()


    while True:
        if player_1_correct_shoots >= CORRECT_SHOOTS:
            print(f"Congratulations {players[0]}\nYou won in this game!!!")
            break
        
        elif player_2_correct_shoots >= CORRECT_SHOOTS:
            print(f"Congratulations {players[1]}\nYou won in this game!!!")
            break

        # 1st player shoots
        while True:
            print(f"{players[0]} shoots:")
            pprint(player_2_opponent_map)
            coordinates: List[str] = get_coordinates()

            is_shoot = shoot(coordinates, player_2_map, player_2_opponent_map)

            if is_shoot[1] is False:
                print(f"\nSorry, {players[0]} your bullet passed by ship.\nTry again")
                break
            elif is_shoot[1] is None:
                print("\nPlease, shoot to another place.\nYou already shoot there!")
            elif is_shoot[1]:
                print("\nGood, you could shoot it.")
                player_1_correct_shoots += 1
                clear_screen()

        sleep(3)
        clear_screen()

        # 2nd player shoots
        while True:
            print(f"{players[1]} shoots:")
            pprint(player_1_opponent_map)
            coordinates: List[str] = get_coordinates()

            is_shoot = shoot(coordinates, player_1_map, player_1_opponent_map)

            if is_shoot[1] is False:
                print(f"\nSorry, {players[1]} your bullet passed by ship.\nTry again")
                break
            elif is_shoot[1] is None:
                print("\nPlease, shoot to another place.\nYou already shoot there!")
            elif is_shoot[1]:
                print("\nGood, you could shoot it.")
                player_2_correct_shoots += 1
                clear_screen()

        sleep(3)
        clear_screen()

    print(f"The total number of correct shoots {players[0]} has {player_1_correct_shoots}")
    print(f"The total number of correct shoots {players[1]} has {player_2_correct_shoots}")
if __name__ == "__main__":
    main()