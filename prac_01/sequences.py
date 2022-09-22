MENU = "(E)ven numbers\n(O)dd numbers\n(S)quared numbers\n(Q)uit"

print("Number sequence generator")
print(MENU)
menu_choice = input(">>>").upper()
while menu_choice != "Q":
    if menu_choice == "E":
        even_minimum = int(input("Minimum number: "))
        even_maximum = int(input("Maximum number: "))
        for i in range(even_minimum + (even_minimum % 2), even_maximum + 1, 2):
            print(i, end=" ")
        print()
    elif menu_choice == "O":
        odd_minimum = int(input("Minimum number: "))
        odd_maximum = int(input("Maximum number: "))
        for i in range(odd_minimum + (odd_minimum % 1), odd_maximum + 1, 2):
            print(i, end=" ")
        print()
    elif menu_choice == "S":
        square_minimum = int(input("Minimum number: "))
        square_maximum = int(input("Maximum number: "))
        for i in range(square_minimum + (square_minimum % 1), square_maximum + 1):
            print(i ** 2, end=" ")
        print()
    else:
        print("Invalid choice")
    print(MENU)
    menu_choice = input(">>>").upper()
print("Fin.")
