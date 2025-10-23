import sys
import random

tries = 0;

print("I am thinking of a number between 1 and 20")
random_number = random.randint(1, 20)

print("Take a guess")

while True:
    guessed_number = int(input(">"))
    if guessed_number == random_number:
        print("Correct guess!")
        print("No of tries ", str(tries))
        sys.exit()
    else:
        if guessed_number < random_number:
            print("Your guess is too low")
        if guessed_number > random_number:
            print("Your guess is too high")

        print("Try again")
    tries += 1
