def setup():
    # Setup for the settlers game
    input("Do you wanna play a full game of settlers or ")

class Mechanics:
    # The basic variables required for the game.
    victory_Points = int
    wood = int
    livestock = int
    clay = int
    stone = int
    hay = int
    roads = int

    @staticmethod
    def dice_roll():
        import random
        """
        This function will emulate the dice d_roll in the game settlers.
        @author Tyrell Grant-Williams
        """
        d_roll = random.randint(1, 6)
        return d_roll


class Player(Mechanics):
    def roll(self):
        super.__init__(self)
