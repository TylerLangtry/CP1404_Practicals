from prac_08.Taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]

    taxis = run_menu(taxis)

def run_menu(taxis):
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
        elif choice.upper() == "D":
            distance = input("Drive how far?:")
            taxis[chosen_taxi].name.drive(distance)
        else:
            print("Invalid menu choice")
        print(menu)
        choice = input(">>> ")
    print("b")
    return taxis


def choose_taxi(taxis):
    list_number = 0
    for taxi in taxis:
        print("{} - {}".format(list_number, taxi))
        list_number += 1
    choice = input("Choose taxi:")
    print("Bill to date: {}".format(calculate_bill()))
    return choice


#def calculate_bill():


main()
