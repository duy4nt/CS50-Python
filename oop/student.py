def main():
    name, house = get_student()
    print(f"{name} from {house}")

def get_student():
    return get_name(), get_house()

def get_name():
    return input("Name: ")

def get_house():
    return input("House: ")

if __name__ == "__main__":
    main()