numbers = []

for i in range(5):
    number = float(input("Number: "))
    numbers.append(number)

print("The first number is {:1.2f}" .format(numbers[0]))
print("the last number is {:1.2f}" .format(numbers[4]))
print("The smallest number is: {:1.2f}" .format(min(numbers)))
print("The largest number is: {:1.2f}" .format(max(numbers)))
print("The average of the numbers is: {:1.2f}" .format(sum(numbers)/len(numbers)))
