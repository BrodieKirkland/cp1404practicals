from silver_service_taxi import SilverServiceTaxi

my_fancy_taxi = SilverServiceTaxi("Fancy Pants", 200, 2)

print(my_fancy_taxi)
my_fancy_taxi.drive(20)
print(f"price for fare ${my_fancy_taxi.get_fare():.2f}")
print(my_fancy_taxi)
print("New fare")
my_fancy_taxi.start_fare()
my_fancy_taxi.drive(100)
print(f"price for fare ${my_fancy_taxi.get_fare():.2f}")
print(my_fancy_taxi)
print("New fare")
my_fancy_taxi.start_fare()
my_fancy_taxi.drive(18)
print(f"price for fare ${my_fancy_taxi.get_fare():.2f}")
print(my_fancy_taxi)
