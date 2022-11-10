from prac_06.guitar import Guitar

INDEX_NAME = 0
INDEX_YEAR = 1
INDEX_COST = 2
CURRENT_YEAR = 2022

with open("guitars.csv", "r") as in_file:
    guitars = []
    for line in in_file:
        parts = line.strip().split(",")
        parts[INDEX_YEAR], parts[INDEX_COST] = int(parts[INDEX_YEAR]), float(parts[INDEX_COST])
        guitars.append(Guitar(*parts))
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    guitar = Guitar(name, year, cost)
    print(f"{guitar.name} ({guitar.year}) : ${guitar.cost:,.2f} added.")
    guitars.append(guitar)
    name = input("Name: ")
print("These are my guitars:")
guitars.sort()
for i, guitar in enumerate(guitars, 1):
    vintage_string = " (vintage)" if guitar.is_vintage(CURRENT_YEAR) else ""
    print(f"Guitar {i}: {guitar.name:>25} ({guitar.year:4}), worth ${guitar.cost:10,.2f}{vintage_string}")
with open("guitars.csv", "w") as out_file:
    for guitar in guitars:
        print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)
        print(f"{guitar} Saved")
# for guitar in sorted(guitars):
#     print(guitar)
