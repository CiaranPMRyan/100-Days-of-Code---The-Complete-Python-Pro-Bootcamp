# This is the way to do it with the CSV importer
#
# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#
# print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         temperatures.append(row[1])
#     temperatures.pop(0)
#     intlist = list(map(int, temperatures))
#     print(intlist)

# Pandas is much more efficient
import pandas

# data_file = pandas.read_csv("weather_data.csv") # Reads the CSV and is ready to operate on
# print(type(data_file))
# print(data_file["temp"])
#
# data_dict = data_file.to_dict() # Converts the data to a dictionary using the headers as Key values
# print(data_dict)
#
# data_list = data_file["temp"].to_list() # converts a column to a list
# print(data_list)
#
# print(data_file["temp"].max())
# print(data_file.temp.max())
#
# print(data_file[data_file.temp == data_file.temp.max()])

# monday = data_file[data_file.day == "Monday"]
# cel = monday.temp
# fahr = cel * 1.8 + 32
# print(fahr)

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

# TODO 1: Open the CSV
data_file = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250707.csv")
#print(data_file)

# TODO 2: Open the colours column. create 3 new lists, one for each of the colours
list_gray = []
list_cinnamon = []
list_black = []

color_list = data_file["Primary Fur Color"].to_list()
#print(data_file["Primary Fur Color"])

for item in color_list:
    if item == "Gray":
        list_gray.append(item)
    elif item == "Cinnamon":
        list_cinnamon.append(item)
    elif item == "Black":
        list_black.append(item)

# TODO 3: Get the length of each list.

len_gray = len(list_gray)
len_red = len(list_cinnamon)
len_black = len(list_black)

# Todo 4: Create a new dictionary and populate it with the lists and save it as a csv

color_dict = {
    "Fur Colour": [f"{list_gray[0]}", f"{list_cinnamon[0]}", f"{list_black[0]}"],
    "Count": [f"{len_gray}", f"{len_red}", f"{len_black}"]
}
# print(color_dict)
write_data = pandas.DataFrame(color_dict)
print(write_data)
write_data.to_csv("squirrel_count.csv")
