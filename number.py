while True:
    try:
        x = int(input("Whats x?"))
        print(f"x is {x}")
    except ValueError:
        print("x is not a number")
    else:
        break

print(f"x is {x}")