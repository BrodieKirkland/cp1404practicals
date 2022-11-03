from guitar import Guitar


def main():
    current_year = 2022
    my_guitars = []
    print("My guitars!")
    while True:
        name = input("Name: ")
        if name == "":
            break
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar = Guitar(name, year, cost)
        print(f"{guitar.name} ({guitar.year}) : ${guitar.cost:,.2f} added.")
        my_guitars.append(guitar)
    print("These are my guitars:")
    for i, guitar in enumerate(my_guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage(current_year) else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year:4}), worth ${guitar.cost:10,.2f}{vintage_string}")


main()
