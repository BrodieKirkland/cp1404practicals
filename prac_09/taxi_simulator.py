from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"
TAXIS = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]


def main():
    """Choose and drive from list of taxis"""
    current_taxi = None
    bill_to_date = 0.0
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                distance = int(input("Drive how far? "))
                current_taxi.start_fare()
                drive(current_taxi, distance)
                fare = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${fare:.2f}")
                bill_to_date += fare
            print_bill_to_date_string(bill_to_date)
        elif choice == "c":
            print("Taxis available:")
            print_taxis(TAXIS)
            current_taxi = choose_taxi(TAXIS)
            print(f"You've chosen {current_taxi.name}")
            print_bill_to_date_string(bill_to_date)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").lower()
    print(f"Total trip cost: ${bill_to_date:.2f}")
    print("Taxis are now:")
    print_taxis(TAXIS)


def print_bill_to_date_string(bill_to_date):
    """Print bill to date string"""
    print(f"Bill to date: ${bill_to_date:.2f}")


def print_taxis(taxis):
    """Print taxis with numbering"""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def drive(current_taxi, distance):
    """Drive current taxi distance given"""
    current_taxi.drive(distance)


def choose_taxi(taxis):
    """Choose valid taxi"""
    choice = get_valid_taxi_choice(taxis)
    taxi = taxis[choice]
    return taxi


def get_valid_taxi_choice(taxis):
    """Get valid taxi choice"""
    choice = int(input("Choose taxi: "))
    valid_choice = False
    while not valid_choice:
        if len(taxis) > choice >= 0:
            valid_choice = True
        else:
            print("Invalid taxi choice")
            choice = int(input("Choose taxi: "))
    return choice


if __name__ == '__main__':
    main()
