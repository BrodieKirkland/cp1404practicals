MENU = "(H)ello\n(G)oodbye\n(Q)uit"

user_name = input("Enter name: ")
print(MENU)
menu_choice = input(">>> ").upper()
while menu_choice != "Q":
    if menu_choice == "H":
        print(f"Hello {user_name}!")
    elif menu_choice == "G":
        print(f"Goodbye {user_name}!")
    else:
        print("Invalid input")
    print(MENU)
    menu_choice = input(">>> ").upper()
print("Finished.")
