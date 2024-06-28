from time import sleep

from texts import introduction_text, rules

def greet() -> None:
    """
    Greets with players
    """

    print("Greetings!\nLet's play battleship game.")
    sleep(2)

def introduce() -> None:
    """
    Returns brief information about game
    """

    print(introduction_text)

def explain_rules() -> None:
    """
    Explains the rules
    """

    print(rules)