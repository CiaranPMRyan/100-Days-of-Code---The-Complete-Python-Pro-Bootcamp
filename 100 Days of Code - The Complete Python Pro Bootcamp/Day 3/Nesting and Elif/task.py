print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print(f"Child ticket is {bill} Euros.")
    elif age <= 18:
        bill = 7
        print(f"Youth ticket is {bill} Euros.")
    else:
        bill = 12
        print(f"Adult ticket is {bill} Euros.")

    want_photo = input("Do you want a photo? Type Y for Yes and N for No.")
    if want_photo == "Y":
        bill += 3

    print(f"Your total cost is: {bill} Euros")


else:
    print("Sorry you have to grow taller before you can ride.")

