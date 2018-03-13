"""
CP1404/CP5632 - Practical
Broken program to determine score status using functions
"""

def main():

    score = get_score()

    if score > 100 or score < 0:
        print("Invalid Score")
    elif score == 100 or score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Pass")
    else:
        print("Bad")


def get_score():
    score = float(input("Enter score: "))
    return score


main()