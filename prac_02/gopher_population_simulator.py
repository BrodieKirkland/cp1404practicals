"""GPS (Gopher Population Simulator)"""
import random


def main():
    total_years = 10
    year = 1
    total_population = 1000
    print("Welcome to the Gopher Population Simulator!")
    print("Starting population:", total_population)
    print(f"Year {year}")
    print()
    for i in range(total_years - 1):
        total_gophers_born = int(calculate_total_gophers_born(total_population))
        total_gophers_died = int(calculate_total_gophers_died(total_population))
        total_population += total_gophers_born - total_gophers_died
        print(f"{total_gophers_born} gophers were born. {total_gophers_died} died.")
        print(f"Population: {total_population}")
        year += 1
        print(f"Year {year}")
        print()


def calculate_total_gophers_born(total_population):
    gophers_born_percentage = random.randint(10, 20) / 100
    return int(total_population * gophers_born_percentage)


def calculate_total_gophers_died(total_population):
    gophers_died_percentage = random.randint(5, 25) / 100
    return int(total_population * gophers_died_percentage)


main()
