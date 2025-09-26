import re

name = input("Whats your name?").strip()

matches =re.search(r"^(.+), *(.+$)", name)
# The groups start from 1; rather than 0.

if matches:
    last, first = matches.groups()
    name = f"{first} {last}"

print(f"Hello {name}")
