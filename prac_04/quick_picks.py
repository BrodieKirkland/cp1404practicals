import random
number_of_quick_adds = int(input("How many quick picks? "))
quick_adds = []
for i in range(number_of_quick_adds):
    new_line = []
    for j in range(6):
        is_new_number = False
        while not is_new_number:
            number = random.randint(1, 45)
            if number not in new_line:
                is_new_number = True
                new_line.append(number)
        print(f"{number:2}", end=" ")
    quick_adds.append(new_line)

    print()
