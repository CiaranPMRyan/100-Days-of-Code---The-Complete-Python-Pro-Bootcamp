# Range function


for number in range(1, 10): # Again, number is just a temp variable to be used inside the loop. Range goes from 1 up to, but not including, 10
    print(number)


gauss = 0 # Set our var to zero

for number in range(1, 101): # Iterates and assigns numbers 1 through 100 in to the variable number
    gauss += number # adds the next number to the running total

print(gauss)