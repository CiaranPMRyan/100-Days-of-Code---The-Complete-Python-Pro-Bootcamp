from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.create_ball()
        self.x_move = 10
        self.y_move = 10

    def create_ball(self):
        self.shape("circle")
        self.color("white")
        self.penup()


    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_pos(self):
        self.goto(0, 0)
        self.bounce_x()

    def skewy(self):
        self.shapesize(stretch_wid=0.5, stretch_len=2)

    def skewx(self):
        self.shapesize(stretch_wid=2, stretch_len=0.5)

    def shape_reset(self):
        self.shapesize(stretch_wid=1, stretch_len=1)
