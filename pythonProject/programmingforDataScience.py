# A method is essentially just a function that is attached to some particular class

# List: is an ordered collection of objects.
# Tuples: are exactly the same as list except that tuples are immutable, which means they can't be changed
# Sets: are also collection of objects, but they are specified using curly brackets.
# Dictionaries: are an extremely useful data object, especially when rapid access is required, dictionaries
# are much more efficient than list

# Computing the volume of a cylinder

import math

radius = 5
height = 12
area = math.pi

volume = area * radius**2 * height

print(volume)

# Translating a formula into a code

x = (math.sqrt(1535) + 3 / 1 - math.exp(-2) ** 2) % 336030 / 345
print(x)

# Check whether the following statement is correct
data = "A million seconds is 11 days, 12 hours, 46 minutes and 40 seconds"

# Split the data into individual words
data_words = data.split()

# Get the total time in seconds
number_conversion = {'million': 1000000}
time_seconds = number_conversion[data_words[1]]

# Compute the number of days, hours, minutes and seconds this corresponds to
days = time_seconds // (60 * 60 * 24)
hours = (time_seconds % (60 * 60 * 24)) // (60 * 60)
minutes = (time_seconds % (60 * 60)) // (60)
seconds = (time_seconds % 60)

# Get the number of distinct characters in the data
data_characters = {character for character in data}
number_of_distinct_characters = len(data_characters)

# Check whether the true values of days, hours, minutes and seconds are in the statement
correct_amounts = str(days) in data and str(hours) in data and str(minutes) in data and str(seconds) in data

# If the statement is incorrect, print the true statement.
if not correct_amounts:
    true_statement = ' '.join(
        data_words[:2]) + f' seconds is {days} days, {hours} hours, {minutes} minutes and {seconds} seconds'
    print(f"The statement:\n\n'{data}'\n\nis incorrect. The correct version of the statement is\n\n'{true_statement}'")