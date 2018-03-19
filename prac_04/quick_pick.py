from random import randint


def main():
    """Generate a lottery quick pick with select amount of lines"""
    lottery = []

    quick_picks = int(input("How many Quick Picks? "))

    generate_quickpick(lottery, quick_picks)


def check_duplicates(number, line):
    if number in line:
        return True
    else:
        return False


def generate_numbers():
    number = randint(1, 45)
    return number


def generate_quickpick(lottery, quick_picks):
    for i in range(quick_picks):
        line = [0, 0, 0, 0, 0, 0]
        for j in range(6):
            number = generate_numbers()
            check = check_duplicates(number, line)
            while check == True:
                number = generate_numbers()
                check = check_duplicates(number, line)
            line[j] = number
        lottery.append(line)
    for row in lottery:
        print(row)


main()




