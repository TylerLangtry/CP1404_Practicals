
from prac_08.Taxi import Taxi

def main():

    taxi = Taxi("Prius 1", 100)
    taxi.drive(40)
    print(taxi)
    print(taxi.get_fare())
    taxi.start_fare()
    taxi.add_fuel(40)
    taxi.drive(100)
    print(taxi)
    print(taxi.get_fare())

main()