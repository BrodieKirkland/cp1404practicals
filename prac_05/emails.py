"""
Time estimate: 15 minutes
actual: 35 minutes
"""

email_to_name = {}

email_address = input("Email: ")
while email_address != "":
    parts = email_address.split("@")
    name = parts[0]
    parts = name.split(".")
    name = " ".join(parts).title()
    is_correct = input(f"Is your name {name}? (Y/n) ").lower()
    if is_correct == "n":
        name = input("Name: ")
    email_to_name[email_address] = name
    email_address = input("Email: ")
for email_address, name in email_to_name.items():
    print(f"{name} ({email_address})")

