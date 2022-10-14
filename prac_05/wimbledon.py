"""
Time  estimate: 40 minutes
actual: 70 minutes
"""

FILENAME = "wimbledon.csv"


def main():
    champions_data = make_champion_list(FILENAME)
    name_to_count, champion_countries = count_name_country(champions_data)
    display_results(champion_countries, name_to_count)


def display_results(champion_countries, name_to_count):
    """ Display champions and countries"""
    print("Wimbledon Champions:")
    for name, count in name_to_count.items():
        print(f"{name} {count}")
    print()
    print(f"These {len(champion_countries)} countries have won Wimbledon:")
    champion_countries = list(champion_countries)
    champion_countries.sort()
    countries = ", ".join(champion_countries)
    print(countries)


def count_name_country(champions_data):
    """Count name and unique countries"""
    name_to_count = {}
    countries = set()
    for data in champions_data:
        name = data[2]
        country = data[1]
        countries.add(country)
        try:
            name_to_count[name] += 1
        except KeyError:
            name_to_count[name] = 1
    return name_to_count, countries


def make_champion_list(filename):
    """ make list of lists from filename"""
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            champion_data = line.split(",")
            champion_data = champion_data[:3]
            data.append(champion_data)
    return data


main()
