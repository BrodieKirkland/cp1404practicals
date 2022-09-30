"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
# When there is a non-integer entered into either numerator or denominator inputs
2. When will a ZeroDivisionError occur?
# if a zero is entered into the inputs
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
# Yes, can add an error checking loop to remove the possibility
"""


def main():
    try:
        numerator = get_valid_number("Enter the numerator: ")
        denominator = get_valid_number("Enter the denominator: ")
        fraction = numerator / denominator
        print(fraction)
    except ValueError:  # Could add this check to get_valid_number function
        print("Numerator and denominator must be valid numbers!")
    # except ZeroDivisionError:
    #     print("Cannot divide by zero!")
    print("Finished.")


def get_valid_number(prompt):
    number = int(input(prompt))
    while number <= 0:
        print("Invalid number")
        number = int(input(prompt))
    return number


main()
