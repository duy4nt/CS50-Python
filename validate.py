import re

email = input("Whats your email?").strip()

if re.search(r"^[^@]+@[^@]+\.com$", email):
    print("Valid")
