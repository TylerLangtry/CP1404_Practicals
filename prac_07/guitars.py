from prac_07.guitar import Guitar

print("My Guitars!")

guitars = []
i = 0

name = "place_holder"
while name != "":
    name = input("Name: ")
    if name == "":
        break
    else:
        year = int(input("Year: "))
        cost = int(input("Cost: "))
        guitars.append(Guitar(name, year, cost))
        print("{} added".format(guitars[i]))
        i += 1

print("These are my guitars:")
j = 0
for guitar in guitars:
    if guitar.is_vintage():
        vintage_string = "(Vintage)"
    else:
        vintage_string = ""
        j += 1
    print("Guitar {}: {:>20} ({}), worth ${:10,.2f} {}".format(j, guitar.name, guitar.year, guitar.cost, vintage_string))