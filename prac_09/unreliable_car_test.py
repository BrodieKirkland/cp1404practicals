from unreliable_car import UnreliableCar


my_car = UnreliableCar("Mazda 5", 100, 50)

for i in range(10):
    print(f"Test {i + 1}")
    print(f"Trying to drive 10km")
    my_car.drive(10)
    print(f"{my_car}")

