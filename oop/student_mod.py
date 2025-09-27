class Student:
    # __init__ method is called automatically, it is a contructor
    def __init__(self, name, house=None):        
        self.name = name
        self.house = house
        # self helps us to store info in the current object
    # a class is like your own datatype
    # you can make them mutable or immutable
    # raise is for giiving an exception known to the user 
    def __str__(self):
        return f"{student.name} from {student.house}"

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name
        # _ means that its a private variable and dont touch it

    # getter
    @property
    def house(self):
        return self._house

    # setter
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self._house = house

def main():
    student = get_student()
    print(Student)


def get_student:    
    name = input("Name: ")
    house = input("House: ")
    try:
        return Student(name, house)
    except Value:
        ...
    # calling the contructor here

if __name__ == "__main__":
    main()