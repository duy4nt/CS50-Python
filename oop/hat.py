import random

class Hat:
        houses = ["Gryffindor", "Huffleppuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))
        
Hat.sort("Harry")