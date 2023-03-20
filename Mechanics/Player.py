from Mechanics import Mechanics


def roll():
    dice_1 = Mechanics.dice_roll()
    dice_2 = Mechanics.dice_roll()
    dice_roll = dice_1 + dice_2
    return dice_roll


class Player(Mechanics):
    victory_Points = 0
    wood = 0
    livestock = 0
    clay = 0
    stone = 0
    hay = 0
    roads = 0
    settlements = 0
    cities = 0
    knights = 0
    cards_in_hand = 0
