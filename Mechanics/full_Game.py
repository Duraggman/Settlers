from Player import Player
from Start import Start


# Roll order
def roll_order(num_of_players):
    print("\n Player's roll for order")
    orderRolls = []
    for i in range(num_of_players):
        print(f"{Start.Players[0][i]} turn to roll ")
        orderRolls.append((Start.Players[0][i], Start.Players[][i].roll()))


if __name__ == '__main__':
    start = Start
    roll_order(start.num_players)

