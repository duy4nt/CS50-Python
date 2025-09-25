name = input("Whats your name?")

if "," in name:
    last, first = name.split(", ")
    name = (f"{first}{last}")

print(f"Hello, {name}")

