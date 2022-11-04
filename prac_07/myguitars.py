from prac_06.guitar import Guitar

INDEX_NAME = 0
INDEX_YEAR = 1
INDEX_COST = 2

with open("guitars.csv", "r") as in_file:
    guitars = []
    for line in in_file:
        parts = line.strip().split(",")
        parts[INDEX_YEAR], parts[INDEX_COST] = int(parts[INDEX_YEAR]), float(parts[INDEX_COST])
        guitars.append(Guitar(*parts))

for guitar in sorted(guitars):
    print(guitar)
