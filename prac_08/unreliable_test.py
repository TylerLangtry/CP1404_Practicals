from prac_08.unreliable_car import UnreliableCar

def main():

    unreliable = UnreliableCar("Bad", 500, 50)
    print(unreliable.drive(80))
    print(unreliable.drive(100))
    print(unreliable.drive(150))
    print(unreliable.drive(20))


main()