# TypeError
# len(123)

# No TypeError
len("Hello")

# Type Checking - the type() function will return the class type
print(type("abc"))
print(type(123))
print(type(3.14))
print(type(True))

# Type Conversion - converts the data inside the brackets to said class.
str()
int()
float()
bool()

name_of_the_user = input("Enter your name") # Gets the name as a string
length_of_name = len(name_of_the_user) # gets the length of the variable and puts that into a new variable. len is always an integer

print(type("Number of letters in your name: "))  # str
print(type(length_of_name))  # int

print("Number of letters in your name: " + str(length_of_name)) # The length_of_name variable has to be converted to a string to be concatenated.
