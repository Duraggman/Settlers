def test_start():
    test_return = bool
    full_or_quick = input("Do you wanna play a full game or a quick game").lower()
    if full_or_quick == "full":
        test_return = True
    elif full_or_quick == "quick":
        test_return = False
    else:
        print("only 'full' or  'quick' will be accepted.")
    if not test_return or test_return:
        assert True
    else:
        assert False


def test_timer():
    assert False
