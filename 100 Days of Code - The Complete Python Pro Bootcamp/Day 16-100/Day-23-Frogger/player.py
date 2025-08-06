from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DIST = 10

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.create_player()

    def create_player(self):
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        self.fd(MOVE_DIST)

    def player_reset(self):
        self.goto(STARTING_POSITION)
