from taxi import Taxi

my_taxi = Taxi("Prius 1", 100)
my_taxi.drive(40)
print(f"Driven {my_taxi.name} 40km")
print(my_taxi)
my_taxi.start_fare()
my_taxi.drive(100)
print(f"Driven {my_taxi.name} 100km")
print(my_taxi)
