# Import the modules

from turtle import Turtle, Screen
import random

# All the main functions

def square(name):
    '''Creates a square'''
    for i in range(4):
        name.forward(100)
        name.right(90)

def shape(name, num_sides):
    '''Creates a shape dependent on the number of sides input'''
    angle = 360/num_sides
    for _ in range(num_sides):
        name.forward(100)
        name.right(angle)

def rand_col():
    '''Creates a random RGB colour'''
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

def offset(name):
    '''Offsets the pens position'''
    name.penup()
    name.bk(20)
    name.left(90)
    name.fd(20)
    name.right(90)
    name.pendown()

def random_walk(name):
    '''Simple random walk function'''
    angle_choice = [0, 90, 180, 270]
    angle = random.choice(angle_choice)
    name.fd(30)
    name.setheading(angle)

def spirograph(name, gap, rad):
    for _ in range(int(360/gap)):
        name.color(rand_col())
        name.circle(rad)
        name.left(gap)
        #offset(name)

# Create the Screen object
screen = Screen()

# Create my Turtle object
tim = Turtle()
tim.speed(0)
tim.shape("arrow")
# Set the colour mode to allow RGB values
screen.colormode(255)

##### MAIN CODE #####

# You can uncomment the function to draw a simple square
#square(tim)

# Looping fun
# Here we set the pen size to 3 and then enter a loop that has several uses

p = 3

spirograph(tim, 8, 100)
tim.pensize(4)
spirograph(tim, 15, 120)
tim.pensize(5)
spirograph(tim, 20, 180)

# If using the shape() function, set the range from 3 to whatever you would like. Something around 16-24 works well for the screen size.
# Also nice to uncomment the offset() function and the pensize.
# If using the random_walk() function, best to comment out the shape() function. The offset() and pensize parts can be used to have some fun
#for i in range(3, 16):

    #tim.color(rand_col())
    #shape(tim, i)
    #offset(tim)
    #p += 1
    #tim.pensize(p)
    #random_walk(tim)

# Spirograph



# Click to close screen
screen.exitonclick()