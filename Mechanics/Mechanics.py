def dice_roll():
    import random
    """
    This function will emulate the dice d_roll in the game settlers.
    @author Tyrell Grant-Williams
    """
    d_roll = random.randint(1, 6)
    return d_roll


class Mechanics:
    # The basic variables required for the game.
    victory_Points = int
    wood = int
    livestock = int
    clay = int
    stone = int
    hay = int
    roads = int



