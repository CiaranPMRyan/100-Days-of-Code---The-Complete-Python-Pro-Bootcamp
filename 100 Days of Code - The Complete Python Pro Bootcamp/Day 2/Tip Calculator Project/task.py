print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

bill_split = round(((bill * tip / 100) + bill)/people, 2)

print(f"Each person should pay: ${bill_split}")


######## f-strings!! Use the f-string to do an autoconversion to string inside any string using the curly brackets  #######