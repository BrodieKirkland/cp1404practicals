import random
number_of_quick_adds = int(input("How many quick picks? "))

for i in range(number_of_quick_adds):
    for j in range(6):
        print(f"{random.randint(1, 45):2}", end=" ")
    print()
