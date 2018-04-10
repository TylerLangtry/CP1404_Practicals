from prac_07.guitar import Guitar

guitar_01 = Guitar("Gibson L-5 CES", 1922, 16035.40)
guitar_02 = Guitar("Another Guitar", 2012, 50.00)

print(guitar_01)
print("Expected 96. Got {}".format(guitar_01.get_age()))
print("Expected True. Got {}".format(guitar_01.is_vintage()))

print(guitar_02)
print("Expected 6. Got {}".format(guitar_02.get_age()))
print("Expected False. Got {}".format(guitar_02.is_vintage()))
