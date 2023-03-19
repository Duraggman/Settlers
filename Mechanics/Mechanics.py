class Mechanics:
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
