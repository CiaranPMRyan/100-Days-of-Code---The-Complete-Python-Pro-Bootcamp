import colorgram
from turtle import Turtle, Screen
import random

def get_colors():
    '''Gets the colours from the image and puts them into a list'''
    rgb_colors = []
    colors = colorgram.extract('image.jpg', 30)
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        rgb_colors.append(new_color)
    return rgb_colors
    # print(rgb_colors) # Print out the tuples
    # print(len(rgb_colors)) # Print out the length of the list

def remove_brights(color_list):
    '''Removes the brightest colours from the rgb_color list and returns a new list called color_list'''
    # Loop through the colors list and remove any colour that is more than 700 sum value.
    for color in rgb_colors:
        color_list = [color for color in rgb_colors if sum(color) <= 700]
    return color_list
    # print(color_list) # Print out the new tuples
    # print(len(color_list)) # Print out the length of the new list. It should be smaller than the original

def draw_dot(name, s_size, iterations):
    '''Draws a dot with a random pen colour and then moves the Turtle across based on the number of iterations by the screen size'''
    move_dist = s_size / iterations
    name.dot(20, random.choice(color_list))
    name.fd(move_dist)

def start_pos(name, s_size):
    '''Takes the screen size and calculates a starting position for the Turtle and moves it there'''
    # Define a starting position that is relative to the screen size.
    name.penup()
    start_x = -abs(screen_size * 0.5)  # Moves the turtle -250 pixels
    start_y = -abs(screen_size * 0.5)  # Moves the turtle -250 pixels
    name.goto(start_x, start_y)
    return start_x, start_y

# Create the colour list with the brightest colours removed automatically.
rgb_colors = get_colors()
color_list = remove_brights(rgb_colors)

# Define the screen size. Needs to be 500px in each direction.
screen_size = 500

# Initialise Turtle and the screen
screen = Screen()
screen.screensize(screen_size, screen_size)
screen.colormode(255)
t = Turtle()
t.speed(0)
t.hideturtle()

# Define x and y for the starting position and move the turtle.
x_pos, y_pos = start_pos(t, screen_size)

iterations = 10

for _ in range(iterations):
    for _ in range(iterations):
        # Create a function to do a dot of size 20, with pencolor from the list, then move across an equal distance
        draw_dot(t, screen_size, iterations)
    # After 10 iterations of this, it needs to move back to the starting point and move up 50 pixels and repeat.
    # This also has to be done 10 times.
    # Updates the starting position of the next row
    y_update = screen_size / iterations
    y_pos += y_update
    t.goto(x_pos, y_pos)

# Click to close screen
screen.exitonclick()