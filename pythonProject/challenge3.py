name = input("Please enter your name: ")
age = int(input("How old are you? "))

if age > 18 and age < 31:
    print(f"Welcome to your holiday trip {name}")
else:
    print(f"Sorry! {name} you need to apply again for vacation")