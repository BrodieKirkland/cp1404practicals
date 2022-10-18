"""
Time estimate: 15 minutes
actual: 35 minutes
"""


def main():
    """Create dictionary of emails_to_names"""
    email_to_name = {}
    email_address = input("Email: ")
    while email_address != "":
        name = get_name_from_email(email_address)
        confirmation = input(f"Is your name {name}? (Y/n) ").lower()
        if confirmation == "n":
            name = input("Name: ")
        email_to_name[email_address] = name
        email_address = input("Email: ")
    for email_address, name in email_to_name.items():
        print(f"{name} ({email_address})")


def get_name_from_email(email_address):
    """Extract name from email address"""
    prefix = email_address.split("@")[0]
    parts = prefix.split(".")
    name = " ".join(parts).title()
    return name


main()

