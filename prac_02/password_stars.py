MINIMUM_PASSWORD_LENGTH = 4

password = input("Password: ")
while len(password) < MINIMUM_PASSWORD_LENGTH:
    print(f"Must be {MINIMUM_PASSWORD_LENGTH} characters minimum.")
    password = input("Password: ")
for i in range(len(password)):
    print("*", end="")
print()
