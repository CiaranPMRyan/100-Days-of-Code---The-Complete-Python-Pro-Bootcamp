from turtle import Turtle, Screen
import math
import random

# Creates a random spirogragh based off user imputs
# WARNING - This can be slow to render and the results are not always full proof.
# This is just for some fun. Put in some numbers and grab a coffee :)

def rand_col():
    """Creates a random RGB color"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def draw_spirograph(R, r, A, step=1, theta_offset=0):
    """Draws a spirograph with the given parameters"""

    # Convert offset angle to radians
    theta_offset = math.radians(theta_offset)

    tim.penup()

    # Get the starting position
    theta = 0
    x_start = (R - r) * math.cos(math.radians(theta) + theta_offset) + A * math.cos(
        math.radians((R - r) / r * theta) + theta_offset)
    y_start = (R - r) * math.sin(math.radians(theta) + theta_offset) - A * math.sin(
        math.radians((R - r) / r * theta) + theta_offset)

    tim.goto(x_start, y_start)
    tim.pendown()
    tim.hideturtle()

    # Start drawing
    while True:
        theta += step
        x = (R - r) * math.cos(math.radians(theta) + theta_offset) + A * math.cos(
            math.radians((R - r) / r * theta) + theta_offset)
        y = (R - r) * math.sin(math.radians(theta) + theta_offset) - A * math.sin(
            math.radians((R - r) / r * theta) + theta_offset)

        tim.goto(x, y)

        # Check if we're back at the start position
        if math.isclose(x, x_start, abs_tol=0.5) and math.isclose(y, y_start, abs_tol=0.5):
            break  # Stop drawing when back to start


# Draw multiple spirographs with different colors and angles

# Make an input for total loops, and iterations per loop.
print("Be aware that large numbers will be slow to render. "
                  "It is recommended to keep both inputs under 5")
loops = int(input("How many loops would you like? (1-5): "))
iteration = int(input("How many iterations of each loop would you like? (1-5): "))
theta_angle = 0

# Create the Screen object
screen = Screen()
screen.colormode(255)  # Allow RGB colors
screen.bgcolor(228, 228, 228)

# Create Turtle object
tim = Turtle()
tim.speed(0)
tim.shape("arrow")

# Drawing controls.
# R is the radius of the large circle. r is the radius of the inside circle which travels around the large circle
# A is the distance of the pen from r. If A is close to r, you get a classic Spirogragh image.
# The values in my random setup are all based off an initial value of 250 for the large circle.
# You can use hard numbers as mentioned below to set your own starting values.

R = 250
for loop in range(loops):
    # Make each r factor between 1-25 percent of the main loop
    r = random.randint(int(R * 0.01), int(R * 0.25))

    # Make each A factor between plus/minus 10 of the r factor
    A = random.randint(int(r - 10), int(r + 10))

    for num in range(iteration):
        theta_angle += 360 / iteration  # Offset for each iteration
        tim.pencolor(rand_col())  # Random color for each spirograph
        # You can put in hard numbers for R, r, and A. SOmething like 250, 30 and 50 make a nice starting point
        draw_spirograph(R=R, r=r, A=A, theta_offset=theta_angle)

    # Make each subsequent loop's R 65% of previous
    R = int(R * 0.65)

screen.exitonclick()
