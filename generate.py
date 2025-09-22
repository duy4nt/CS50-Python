import random

coin = random.choice(["heads", "tails"])
print(coin)

dice = random.randint(1, 6)
print(dice)

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)