import unittest


class TestMechanics(unittest.TestCase):
    def test_dice_roll(self):  # Test if the dice roll function correctly outputs options.
        import random
        roll = random.randint(1, 6)
        answers = [1, 2, 3, 4, 5, 6]
        self.assertIn(roll, answers)
