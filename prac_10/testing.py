"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""

import doctest
from prac_07.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    words = []
    while n != 0:
        words.append(s)
        n -= 1
    return " ".join(words)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    print(repeat_string("Python", 1))
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    print(repeat_string("hi", 2))
    assert repeat_string("hi", 2) == "hi hi"

    # Hint: "-".join(["yo", "yo"] -> "yo-yo"

    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    test_car = Car()
    assert test_car.odometer == 0, "Car does not set odometer correctly"

    assert test_car.fuel == 0, "Car does not set fuel correctly"
    print("good")
    # Note that Car's __init__ function sets the fuel in one of two ways:
    # using the value passed in or the default
    # You should test both of these
    test_car = Car(fuel=10)
    assert test_car.fuel == 10, "Car does not set fuel correctly"
    print("good")

def make_scentence(sentence):
    """
    >>> make_scentence("hello")
    'Hello.'
    >>> make_scentence("It is an ex parrot.")
    'It is an ex parrot.'
    >>> make_scentence("Test test test")
    'Test test test.'
    """
    if not sentence[0].isupper():
       sentence = sentence.capitalize()
    if not sentence[-1] == ".":
        sentence += (".")
    return sentence


run_tests()

doctest.testmod()



# TODO: 5. Write and test a function to format a phrase as a sentence,
# starting with a capital and ending with a single full stop.
# Important: start with a function header and just use pass as the body
# then add doctests so that:
# 'hello' -> ''Hello.'
# 'It is an ex parrot.' -> 'It is an ex parrot.'
# and one more you decide (that's valid!)
# then write the body of the function so that the tests pass