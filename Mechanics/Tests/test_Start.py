import unittest
from unittest import TestCase


class TestStart(unittest.TestCase):
    def test_game_type(self):  # test for game type selection
        picked = False
        while not picked:
            test_return = bool
            full_or_quick = input("Do you wanna play a full game or a quick game").lower()
            if full_or_quick == "full":
                test_return = True
            elif full_or_quick == "quick":
                test_return = False
            else:
                print(" ")
                print("only 'full' or  'quick' will be accepted.")
            if not test_return or test_return:
                assert True
            else:
                assert False

    def test_timer(self):
        time = input("How long do you want the game to last: ")
        if time.isnumeric():
            print("Passed")
            assert True
        elif not time.isnumeric():
            print("Failed")
            assert False
        else:
            print("Passed")
            assert True

    def test_num_of_players(self):
        Ais = 0
        players = 0  # number of players
        picked = False  # Controls if the
        while not picked:
            try:
                players = int(input("How many players are there?"))
                if players > 4 or players < 1:
                    print("only numbers between 1-4 are allowed.")
                else:
                    if players > 4 or players < 1:
                        assert False
                    else:
                        # Ai selection
                        ai_chosen = False
                        while not ai_chosen:
                            ai_picker = input("Do you want ai players?(Y/N): ").upper()
                            if ai_picker == "Y":
                                ai_chosen = True
                                players = players - 1
                                Ais = 1
                                assert True
                            elif ai_picker == "N":
                                ai_chosen = True
                                assert True
                            else:
                                print(" ")
                                print("Only Y/N are accepted.")
                                assert False
            except ValueError:
                print("Only numbers are allowed.")
            if Ais == 0:
                return players
            if Ais == 1:
                return Ais, players
