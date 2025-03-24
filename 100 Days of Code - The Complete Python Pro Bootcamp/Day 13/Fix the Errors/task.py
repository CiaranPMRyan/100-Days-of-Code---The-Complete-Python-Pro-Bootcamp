try:
    age = int(input("How old are you?"))
except ValueError:
    print("You have typed an invalid number. Please try again using only number characters")
    age = int(input("How old are you?"))


if age > 18:
    print(f"You can drive at age {age}.")
