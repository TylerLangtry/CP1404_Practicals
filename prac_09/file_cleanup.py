"""
CP1404/CP5632 Practical
File renaming and os examples
"""
import shutil
import os


def main():
    """Demo file renaming with the os module."""
    print("Current directory is", os.getcwd())

    # change to desired directory
    os.chdir('Lyrics/Christmas')
    # print a list of all files (test)
    print(os.listdir('.'))

    # make a new directory
    # os.mkdir('temp')

    # loop through each file in the (original) directory
    for filename in os.listdir('.'):
        # ignore directories, just process files
        if not os.path.isdir(filename):
            new_name = get_fixed_filename(filename)
            print(new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    # First, replace the spaces and .TXT (the easy part)
    filename = filename.replace(" ", "_").replace(".TXT", ".txt")

    new_name = ""
    # TODO: step-by-step, consider the problem cases and solve them

    for position, char in enumerate(filename):
        if char.isalpha():
            if position > 0:
                if char.isupper() and new_name[-1].isalpha() and new_name[-1].islower():
                    new_name += "_" + char
                elif char.isupper() and new_name[-1].isalpha() and new_name[-1].isupper():
                    new_name += "_" + char
                elif new_name[-1].isalpha() and new_name[-1].isupper and char.islower():
                    new_name += char
                elif new_name[-1] == "_":
                    new_name += char.capitalize()
                elif new_name[-1] == ".":
                    new_name += char
                elif new_name[-1] == "(" or ")":
                    new_name += char.capitalize()
                elif new_name[-1].isalpha() and new_name[-1].islower():
                    new_name += "_" + char
            else:
                new_name += char.capitalize()
        else:
            new_name += char

    # os.rename(filename, new_name)
    return new_name


main()
