
def main():

    lottery = []

    quick_picks = int(input("How many Quick Picks? "))

    lottery_generator(lottery, quick_picks)


def lottery_generator(lottery, quick_picks):
    from random import randint

    def duplicate_check(number, line):
        if number in line:
            return True
        else:
            return False

    def number_generator():
        number = randint(1, 45)
        return number

    for i in range(quick_picks):
        line = [0, 0, 0, 0, 0, 0]
        for j in range(6):
            number = number_generator()
            check = duplicate_check(number, line)
            while check == True:
                number = number_generator()
                check = duplicate_check(number, line)
            line[j] = number
        lottery.append(line)
    for row in lottery:
        print(row)


main()




