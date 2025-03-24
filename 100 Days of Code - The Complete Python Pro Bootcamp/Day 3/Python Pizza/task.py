print("Welcome to Python Pizza Deliveries!")

price = 0

size = input("What size pizza do you want? S, M or L: ")
if size == "S":
    price = 15
elif size == "M":
    price = 20
elif size == "L":
    price = 25
else:
    print("You have chosen an invalid size.") # Use this to catch bad entry data

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ") # Here there is no ending else statement. That way if the if is not true, then the code goes to the next line
if pepperoni == "Y":
    if size == "S":
            price += 2
    else:
            price += 3

extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == "Y":
    price += 1

print(f"Your final bill is: ${price}.")

# Throughout this code, we're adding to the Price variable depending on the answers to the if statements