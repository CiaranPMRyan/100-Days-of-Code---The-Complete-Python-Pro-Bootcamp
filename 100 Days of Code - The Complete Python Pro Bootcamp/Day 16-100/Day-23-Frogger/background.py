from turtle import Turtle

class Background(Turtle):

    def __init__(self):
        super().__init__()
        self.bg_start = -280
        self.draw_order = ["g", "d", "r"] # Order for drawing the main graphics - "Grass", "Dash", and "Road"
        self.segs = [] # List for storing the graphics turtles
        self.draw()
        self.border() # Main screen border
        self.water()

    def draw(self):
        '''Loops the main graphics 3 times to create the road system'''
        for i in range(3):
            self.create_trims()
            self.bg_start += 148

    # Create a loop that creates a piece of grass, a thin line, a road, a thick line, and another thin line. The draw method loops this 3 times.
    # Give it the grass start pos and offset everything from that.
    def create_trims(self):
        for item in self.draw_order:
            if item == "g":
                self.grass()
            elif item == "d":
                self.big_dash()
            elif item == "r":
                self.road()
            self.segs.append(item)

    def grass(self):
        grass = Turtle()
        grass.shape("square")
        grass.penup()
        grass.color("Green4")
        grass.shapesize(stretch_wid=2, stretch_len=28)
        grass.goto(x=0, y=self.bg_start)

    def road(self):
        road = Turtle()
        road.shape("square")
        road.penup()
        road.color("grey")
        road.shapesize(stretch_wid=5, stretch_len=28)
        road.goto(x=0, y=self.bg_start + 74)

    def big_dash(self):
        def loop():
            for i in range(10):
                big_dash.pendown()
                big_dash.fd(16)
                big_dash.penup()
                big_dash.fd(40)
                big_dash.pendown()

        big_dash = Turtle()
        big_dash.hideturtle()
        big_dash.width(5)
        big_dash.pencolor("black")
        big_dash.setheading(180)

        big_dash.penup()
        big_dash.goto(260, self.bg_start + 22)
        loop()
        big_dash.penup()
        big_dash.goto(260, self.bg_start + 126)
        loop()

    def water(self):
        road = Turtle()
        road.shape("square")
        road.penup()
        road.color("blue")
        road.shapesize(stretch_wid=1, stretch_len=28)
        road.goto(x=0, y=155)

    def border(self):

        def line(iteration):
            for item in range(iteration):
                border.pendown()
                border.fd(10)
                border.penup()
                border.fd(10)
            border.right(90)

        border = Turtle()
        border.width(5)
        border.color("blue")
        border.penup()
        border.hideturtle()
        border.goto(x=287, y=285)
        border.setheading(270)
        for i in range(4):
            line(29)
        border.penup()
        border.goto(x=-50, y=272)
        border.setheading(270)
        line(6)