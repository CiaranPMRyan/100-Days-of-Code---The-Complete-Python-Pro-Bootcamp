from turtle import Turtle

MOVE_DIST = 20 # Constant Move distance

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self, position):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def up(self):
        new_y = self.ycor() + MOVE_DIST
        if new_y > 260:
            new_y = 260
            self.goto(self.xcor(), y=new_y)
        else:
            self.goto(self.xcor(), y=new_y)

    def down(self):
        new_y = self.ycor() - MOVE_DIST
        if new_y < -260:
            new_y = -260
            self.goto(self.xcor(), y=new_y)
        else:
            self.goto(self.xcor(), y=new_y)
