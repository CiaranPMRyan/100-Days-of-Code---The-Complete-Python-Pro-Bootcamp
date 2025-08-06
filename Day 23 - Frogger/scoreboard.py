from turtle import Turtle

from prettytable.prettytable import VAlignType

FONT = ("System", 30, "bold")
ALIGNMENT = 'center'

# Use START_X and START_Y to position the title
START_X = 10
START_Y = 170
START_POS = [(START_X,START_Y), (START_X + 3, START_Y + 3), (START_X + 6, START_Y + 6)]
COLS = ["red", "white", "blue"] # Title colours

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        # The first set of turtle definitions are the scoreboard
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-250, 200)
        self.level = 0
        self.update_level()

        # This creates the coloured game title text
        self.header = []
        self.main_header()
        self.new_layer_col = 0

    def update_level(self):
        self.clear()
        self.write(f"Level: {self.level}", font=FONT)

    def main_header(self):
        for index in range(len(START_POS)):
            self.add_layer(index)

    def add_layer(self, index):
        new_layer = Turtle("square")
        new_layer.hideturtle()
        new_layer.color(COLS[index])
        new_layer.penup()
        new_layer.goto(START_POS[index])
        new_layer.write(f"  TURTLE \nCROSSING", font=FONT)
        self.header.append(new_layer)

    def game_over(self):
        self.color("white")
        self.goto(0, -10)
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)
