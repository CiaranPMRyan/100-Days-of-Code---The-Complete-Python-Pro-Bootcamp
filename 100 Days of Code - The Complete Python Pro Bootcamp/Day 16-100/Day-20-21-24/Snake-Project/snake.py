from turtle import Turtle

MOVE_DIST = 20 # Constant Move distance
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

STARTING_POS = [(0,0), (-20, 0), (-40, 0)]

class Snake:

    def __init__(self): # Initialise our Snake. Creates the segments list and sets the starting pos
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self): # Creates the actual segments for the starting snake
        for position in STARTING_POS:
            self.add_segment(position)
        self.seg_size()


    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())
        self.seg_size()


    # Looks at the length of the list and starts at the end.
    # It moves each segment to the position of the segment before
    # We then move the first segment to a new position.
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DIST)

    def seg_size(self):
        seg_size_fac = 18/(len(self.segments) -1)
        mult_factor = len(self.segments) -1
        for seg_num in range(0, len(self.segments), 1):
            seg_size = seg_size_fac * mult_factor + 2
            self.segments[seg_num].shapesize(seg_size / 20)

            mult_factor -= 1


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
