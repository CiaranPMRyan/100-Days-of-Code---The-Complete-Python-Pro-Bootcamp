from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
NUM_CARS = 6
START_Y = [68, 112, -35, -80, -185, -230]

class CarManager:

    def __init__(self):
        #super().__init__()
        self.num_cars = 6
        self.cars = []
        self.add_car()
        self.move_dist = 5

    def add_car(self):
        for num in range(self.num_cars):
            self.car()

    def car(self):
        # Create a turtle with a length of 40 and pick a colour from the list.
        new_car = Turtle("square")
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.goto(x=random.randrange(-250, 350, 100), y=random.choice(START_Y))
        self.cars.append(new_car)

    def car_move(self):
        for item in range(len(self.cars)):
            if self.cars[item].xcor() < -280:
                self.cars[item].goto(x=350, y=self.cars[item].ycor())
            new_x = self.cars[item].xcor() - self.move_dist
            self.cars[item].goto(x=new_x, y=self.cars[item].ycor())
