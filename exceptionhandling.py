try:
    print("Run this piece of code")
    result = 5 / 0
    print("Bad idea")
except ZeroDivisionError:
    print("Failed because division by zero isn't possible")
    result = None

print(result)