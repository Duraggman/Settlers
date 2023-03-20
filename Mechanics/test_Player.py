from Mechanics import Mechanics


def test_roll():
    dice_1 = Mechanics.dice_roll()
    dice_2 = Mechanics.dice_roll()
    dice_roll = dice_1 + dice_2
    if dice_roll < 2 or 12 < dice_roll:
        assert False
    else:
        assert True
