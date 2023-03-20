def game_type():  # game type selection.
    """
    Allows the player to pick what type of game the want to play. In the UI version of the game this function may be
    easier using two buttons to input this decision.
    This function will be used in the startup sequence of the game.
    @author Tyrell Grant-Williams
    :return: Either 1 or 2 will be returned representing whether the player/s want to play a full game of
    """
    full_or_quick = input(
        "Do you wanna play a full game or a quick game").lower()  # Placeholder before implementing
    # the UI
    # option.
    if full_or_quick == "full":
        return 1
    elif full_or_quick == "quick":
        return 2
    else:
        print("only 'full' or  'quick' will be accepted.")


class Start:
    game_type()
    pass

