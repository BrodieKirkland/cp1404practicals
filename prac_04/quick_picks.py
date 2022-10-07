import random

NUMBER_OF_COLUMNS = 6
MINIMUM_NUMBER = 1
MAX_NUMBER = 45

number_of_rows = int(input("How many quick picks? "))
quick_picks = []
for i in range(number_of_rows):
    new_line = []
    for j in range(NUMBER_OF_COLUMNS):
        is_new_number = False
        while not is_new_number:
            number = random.randint(MINIMUM_NUMBER, MAX_NUMBER)
            if number not in new_line:
                is_new_number = True
                new_line.append(number)
        print(f"{number:2}", end=" ")
    print()


# for i, new_line in enumerate(quick_adds):
#     new_line = str(new_line)
#     print(str(quick_adds[i]))
#     " ".join(str(quick_adds[i]))
#     print(f"{quick_adds}")
