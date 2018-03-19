def main():
    """Get and print select letters of a name"""
    name = get_name()

    print_name(name)


def print_name(name):
    letter = int(input("Which letters?"))
    print(name[1::letter])


def get_name():
    name = input("Name?")
    while len(name) == 0:
        name = input("Name?")
    return name


main()
