name = input("Whats your name? ")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")

with open("names.txt" , "r") as file:
    lines = file.readlines()

for line in sorted(lines):
    print("Hello", line, end = "")