# # Functions with input
#
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
#
# greet_with_name("Jack Bauer")


# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in  {location}?")
#
#
# greet_with(location="Nowhere" ,name="Jack Bauer")


def calculate_love_score(name1, name2):
    namelist = list(name1 + name2)

    print(namelist)

    total1 = 0
    total2 = 0

    for char in namelist:
        if char ==  "t":
            total1 += 1
        elif char ==  "r":
            total1 += 1
        if char ==  "u":
            total1 += 1
        elif char ==  "e":
            total1 += 1
        else:
            total1 = total1

    for char in namelist:
        if char ==  "l":
            total2 += 1
        elif char ==  "o":
            total2 += 1
        if char ==  "v":
            total2 += 1
        elif char ==  "e":
            total2 += 1
        else:
            total2 = total2

    print(f"{total1}{total2}")


calculate_love_score("Kanye West", "Kim Kardashian")