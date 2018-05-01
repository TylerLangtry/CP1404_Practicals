from prac_08.silver_service_taxi import SilverServiceTaxi

def main():

    silver = SilverServiceTaxi("Hummer", 100, 2)
    silver.drive(18)
    print(silver)
    print(silver.get_fare())

main()
