

def main():
    password = get_valid_password()
    print_asterisks(password)


def print_asterisks(password):
    for i in range(len(password)):
        print("*", end="")


def get_valid_password():
    minimum_password_length = 4
    password = input("Password: ")
    while len(password) < minimum_password_length:
        print(f"Must be {minimum_password_length} characters minimum.")
        password = input("Password: ")
    return password


main()
