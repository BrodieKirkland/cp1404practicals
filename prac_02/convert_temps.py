import random


def main():
    in_file = open("temps_input.txt", "r")
    out_file = open("temps_output.txt", "w")
    for line in in_file:
        fahrenheit = convert_fahrenheit_to_celsius(float(line))
        print(fahrenheit, file=out_file)
    in_file.close()
    out_file.close()


def convert_fahrenheit_to_celsius(fahrenheit):
    """Convert fahrenheit to celsius"""
    return 5 / 9 * (fahrenheit - 32)


def convert_celsius_to_fahrenheit(celsius):
    """convert celsius to fahrenheit"""
    return celsius * 9.0 / 5 + 32


def make_random_numbers_file(number_of_numbers):
    out_file = open("temps_input.txt", "w")
    for i in range(number_of_numbers):
        print(f"{random.randint(-200, 200) + (random.random())}", file=out_file)
    out_file.close()


main()
