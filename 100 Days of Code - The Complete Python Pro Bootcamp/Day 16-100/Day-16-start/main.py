import turtle
from random import random
from turtle import Turtle, Screen

timmy = Turtle()
timmy.pensize(1)
timmy.speed(0)
timmy.ht()

my_screen = Screen()
my_screen.bgcolor("plum")

def square(name, length):
    for i in range(4):
        name.fd(length)
        name.right(90)

length = 50
angle = 15
density = int(360/angle)
for i in range(5):
    for x in range(density):
        if i == 4:
            timmy.color("plum")
        else:
            col_list = ['BlueViolet', 'blue4', 'maroon', 'orange']
            timmy.color(col_list[i])
        square(timmy, length)
        timmy.right(angle)
    length *= 1.5
    timmy.pensize(i+2)
    timmy.color()

my_screen.exitonclick()







# from prettytable import PrettyTable
#
# table = PrettyTable()
# table.add_column("Pokemon Name",["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
# table.align = "l"
#
# print(table)