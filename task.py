import random

highest = 10
answer = random.randint(1, highest)

print(f"Please guess number between 1 and {highest}")
guess = int(input())

print(f"Computer's guess {answer}")

if guess == answer:
    print("You got it first time")
elif guess < answer:
    print("Please guess higher")
else:
    print("Please guess lower")