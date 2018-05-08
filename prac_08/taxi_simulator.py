from prac_08.Taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    taxi_1 = Taxi("Prius", 100)
    taxi_2 = SilverServiceTaxi("Limo", 100, 2)
    taxi_3 = SilverServiceTaxi("Hummer", 200, 4)
    taxis = [taxi_1, taxi_2,taxi_3]
    bill = 0
    run_menu(taxis, bill)


def run_menu(taxis, bill):
    """Display a menu and run the appropriate function based off user input"""
    menu = """Menu:
Q - Quit
C - Choose Taxi
D - Drive"""
    print(menu)
    choice = input(">>> ")
    while choice.upper() != "Q":
        if choice.upper() == "C":
            chosen_taxi = choose_taxi(taxis)
            bill = calculate_bill(bill, 0)
        elif choice.upper() == "D":
            distance = int(input("Drive how far?:"))
            taxis[chosen_taxi].start_fare()
            taxis[chosen_taxi].drive(distance)
            cost = taxis[chosen_taxi].get_fare()
            print("Your {} trip cost you ${}".format(taxis[chosen_taxi].name, cost))
            bill = calculate_bill(bill, cost)
        else:
            print("Invalid menu choice")
        print(menu)
        choice = input(">>> ")
    print("Total trip cost: ${:.2f}".format(bill))
    print("Taxis are now:")
    list_number = 0
    for taxi in taxis:
        print("{} - {}".format(list_number, taxi))
        list_number += 1
    return taxis


def choose_taxi(taxis):
    list_number = 0
    print("Taxis Available:")
    for taxi in taxis:
        print("{} - {}".format(list_number, taxi))
        list_number += 1
    choice = int(input("Choose taxi:"))
    return choice


def calculate_bill(bill, cost):
    bill += cost
    print("Bill to date: ${:.2f}".format(bill))
    return bill


main()
