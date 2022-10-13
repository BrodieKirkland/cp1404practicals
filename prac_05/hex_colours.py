COLOUR_TO_CODE = {"absolutezero": "#0048ba", "amaranth": "#e52b50", "amethyst": "#9966cc", "aqua": "#00ffff",
                "aureolin": "#fdee00", "bananaMania": "#fae7b5", "barnred": "#7c0a02"}

max_length = max(len(colour_name) for colour_name in COLOUR_TO_CODE.keys())

for colour_name in COLOUR_TO_CODE:
    print(f"{colour_name:{max_length}} is {COLOUR_TO_CODE[colour_name]}")

colour_name = input("Enter colour name: ").lower()
while colour_name != "":
    try:
        print(colour_name, "is", COLOUR_TO_CODE[colour_name])
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").lower()