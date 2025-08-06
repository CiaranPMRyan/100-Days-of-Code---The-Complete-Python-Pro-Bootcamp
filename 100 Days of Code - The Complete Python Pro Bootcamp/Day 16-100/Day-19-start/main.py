from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet= screen.textinput(title="Place your bet", prompt="Which turtle will win the race? Enter a colour: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y = (400 / len(colors) )
for color in colors:
    color = Turtle(shape="turtle")
    color.penup()
    #color.color(color)
    color.goto(x=-230, y=y)
    y += y

screen.exitonclick()
