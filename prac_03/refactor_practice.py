"""
CP1404/CP5632 - Practical
Temperature conversion using functions
"""

def main():

    choice = get_choice()

    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = calculate_fahrenheit(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = calculate_celsius(celsius, fahrenheit)
            print("Result: {:.2f} C".format(celsius))
        else:
            print("Invalid option")
        choice = get_choice()
    print("Thank you.")


def calculate_celsius(celsius, fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def calculate_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def get_choice():
    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    return choice


main()