import turtle
from turtle import Turtle, Screen
import random


is_race_on = False # while loop

screen = Screen()

# Create width and height for the screen size and subsequent calculations
w_size = 500
h_size = 400
screen.setup(width=w_size, height=h_size) # Create canvas with size inputs
user_bet = screen.textinput(title="Place your bet", prompt="Which turtle will win the race? Enter a colour: ")
all_turtles = []


# Colours for our turtles
colors = ["red", "orange", "yellow", "green", "blue", "purple"]


start_x_pos = ((w_size / 2) * -1) * .95 # Starting position is always in 5% of the left hand side of the screen regardless of the screen size
start_y_pos = ((h_size / 2) * -1) * .80 # Starting position is always up 20% from the bottom of the screen regardless of the screen size
y_increment = h_size / len(colors) # Amount to offset each subsequent turtle based on the height and the amount of turtles

for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(x=start_x_pos, y=start_y_pos)
    start_y_pos += y_increment # Increment the y value of each turtle
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > (w_size / 2) - 20: # Set the endline dynamically
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win! The {winning_color} turtle is the winner!")
            else:
                print(f"You lose! The {winning_color} turtle is the winner!")


        random_dist = random.randint(0, 10)
        turtle.fd(random_dist)

screen.exitonclick()