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
        self.fail()
