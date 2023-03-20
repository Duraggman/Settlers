def game_type():  # game type selection.
    """
    Allows the player to pick what type of game the want to play. In the UI version of the game this function may be
    easier using two buttons to input this decision.
    This function will be used in the startup sequence of the game.
    @author Tyrell Grant-Williams
    :return: Either true or false will be returned representing whether the player/s want to play a full game of
    """
    picked = False
    while not picked:
        full_or_quick = input(
            "Do you wanna play a full game or a quick game: ").lower()  # Placeholder before implementing
        # the UI
        # option.
        if full_or_quick == "full":
            return True
        elif full_or_quick == "quick":
            return False
        else:
            print("only 'full' or  'quick' will be accepted.")
            print(" ")


def timer():
    """
    Allows the player to decide how long the want the quick game to last in minutes.
    :return: how long the game will last in minutes.
    """
    picked = False
    while not picked:
        time = input("How long do you want the game to last: ")
        if time.isnumeric():
            return time
        else:
            print("only numbers will allowed as an input.")
            print(" ")


def num_of_players():  # selecting the number of players that will be in the game
    pass


class Start:
    if game_type():
        pass
    else:
        timer()
    num_of_players()
    pass
