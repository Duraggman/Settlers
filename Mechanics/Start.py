from Player import Player
def game_type():  # game type selection.
    """
    picked: Is only true if the game type has been selected.
    full_or_quick: decides which game type has been selected. (Either full or quick.)

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


def timer():  # The player selects how long they want the quick game to last.
    """
    Allows the player to decide how long the want the quick game to last in minutes.
    time: How long the quick game should last in minutes

    :return: how long the game will last in minutes.
    """
    picked = False
    while not picked:
        time = input("How long do you want the game to last. (In minutes): ")
        if time.isnumeric():
            return time * 60
        else:
            print("only numbers are allowed as an input.")
            print(" ")


def num_of_players():  # selecting the number of players that will be in the game
    """
    Allows the player to choose how many player roles the want in the settlers game. Also allows the player to decide if
    they want an AI player in the game.

    Ais: The amount of Ais that will be in the game
    players: the amount of players in the game
    picked: assigned false until the number of players and AI amount has been assigned
    ai_chosen: loops until AI amount is chosen.
    ai_picker: checks if AI are wanted in the settlers game.

    :return: Ais and players
    """
    Ais = 0
    players = 0
    picked = False
    while not picked:
        try:
            players = int(input("How many players are there?"))
            if players > 4 or players < 1:
                print("only numbers between 1-4 are allowed.")
            else:
                # Ai selection
                ai_chosen = False
                while not ai_chosen:
                    ai_picker = input("Do you want ai players?(Y/N): ").upper()
                    if ai_picker == "Y":
                        ai_chosen = True
                        players = players - 1
                        Ais = 1
                    elif ai_picker == "N":
                        ai_chosen = True
                    else:
                        print(" ")
                        print("Only Y/N are accepted.")
        except ValueError:
            print("Only numbers are allowed.")
        if Ais == 0:
            return players
        if Ais == 1:
            return Ais, players


class Start:
    Players = []
    gameType = game_type()
    if gameType:
        pass
    else:
        amount_of_time = timer()
    num_players = num_of_players()
    namePicked = False  # Checks if the player has picked a valid name.
    for i in range(num_players):
        while not namePicked:
            name = input("what is the players name?: ")  #
            if len(name) > 10:
                print("Player's names can only be 10 characters")
            elif len(name) == 0 or name == " ":  # check if there's a better way to check for empty strings
                print("No name has been entered.")
            else:
                namePicked = True
            Players.append((name, Player))  # holds the player's number and player object in a list.

