import random
MENU = "(G)et score\n(R)esult\n(P)rint stars\n(Q)uit"


def main():
    score = 0
    print(MENU)
    menu_choice = input(">>>").upper()
    while menu_choice != "Q":
        if menu_choice == "G":
            score = random.randint(0, 100)
        elif menu_choice == "R":
            return_result(score)
        elif menu_choice == "P":
            print_stars(score)
        print(MENU)
        menu_choice = input(">>>").upper()
    print("Fin.")


def print_stars(score):
    """Print stars * score"""
    for i in range(score + 1):
        print("*", end="")


def return_result(score):
    """return result"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"


main()
