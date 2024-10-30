parrot = "Norwegian Blue"

letter = input("Enter a letter: ")

if letter in parrot:
    print("{} is in {}".format(letter, parrot))
else:
    print("{} is not in {}".format(letter, parrot))

# Challenge

name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age <= 18 and age < 31:
    print("Welcome to the holiday trip, {0}".format(name))
else:
    print("Sorry, you are not eligible for this party!")