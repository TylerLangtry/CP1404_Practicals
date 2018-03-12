"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""


numerator = int(input("Enter the numerator: "))
denominator = int(input("Enter the denominator: "))

while denominator == 0:
    denominator = int(input("Please enter a denominator that isn't 0!: "))

try:
    fraction = numerator / denominator
    print(fraction)
except ValueError:
        print("Numerator and denominator must be valid numbers!")
print("Finished.")

# 1. Value error occurs when anything but a number is inputted
# 2. ZeroDivisionError occurs when denominator is set to 0