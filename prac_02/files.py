name = input("Enter your name: ")
out_file_1 = open('name.txt', 'w')
print(name, file = out_file_1)
out_file_1.close()

in_file_1 = open('name.txt', 'r')
read_name = in_file_1.read()
print("Your name is {}".format(read_name))
in_file_1.close()

in_file_2 = open('numbers.txt', 'r')
Value_1 = int(in_file_2.readline())
Value_2 = int(in_file_2.readline())
total = Value_1 + Value_2
print(total)
