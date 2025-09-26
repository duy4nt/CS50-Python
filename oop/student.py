class Students:
    ...



def main():
    name, house = get_student()
    if name == "Padma":
        house = "RavenClaw"
    print(f"{name} from {house}")

def get_student():
    return [get_name(), get_house()]
    # The above line returns a list rather than default Tuple, but it is immutable

def get_name():
    return input("Name: ")

def get_house():
    return input("House: ")

if __name__ == "__main__":
    main()