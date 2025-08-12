try:
    file = open("a_file.txt")
    a_dictionary = {"Key" : "Value"}
    print(a_dictionary["Key"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    raise TypeError("This is an error that I created")