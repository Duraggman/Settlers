def test_start():

    full_or_quick = input(
        "Do you wanna play a full game or a quick game").lower()
    if full_or_quick == "full":
        test_return = True
    elif full_or_quick == "quick":
        test_return = False
    else:
        print("only 'full' or  'quick' will be accepted.")
