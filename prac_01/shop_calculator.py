"""
CP1404/CP5632 - Practical
Calculate the total price of multiple items inputed by the user.
"""

items = int(input("Enter No. Items: "))
total = 0

if items <= 0:
    print("Invalid Number of Items!")
    items = int(input("Enter No. Items: "))

for i in range(items):
    price = float(input("Price of Item: "))
    total = total + price

if total > 100:
    total = total*0.9

print("Total Price for ", items, "Items is $", total)
