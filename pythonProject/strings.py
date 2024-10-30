# number = input("Enter a number: ")
# separators = ""
#
# for character in number:
#     if not character.isnumeric():
#         separators += character
#
# print(separators)
#
# values = "".join(char if char not in separators else " " for char in number).split()
# print([int(val) for val in values])

# Challenge

quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""
separators = ""

for char in quote:
    if char.isupper():
        separators += char

print(separators)