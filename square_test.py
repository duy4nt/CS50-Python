from square import square

def main():
    test_square()

def test_square():
    if square(2) != 4:
        print("2 Square was not 4")
    if square(3) != 9:
        print("3 Square was not 9")
    try:
        assert square(4) == 16
    except AssertionError:
        print("$ Squared was not 16")
    # Assertion errors are not the most uder friendly

if __main__ == "__main__":
    main()
