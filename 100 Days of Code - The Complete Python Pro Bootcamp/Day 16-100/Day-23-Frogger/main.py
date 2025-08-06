import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from background import Background


screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)
screen.listen()

background = Background()

player = Player()
screen.onkey(player.move, "Up")

scoreboard = Scoreboard()
cars = CarManager()

# Main Game
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    cars.car_move()

    # Check collision
    for car in cars.cars:
        if player.distance(car) < 30:
            game_is_on = False
            scoreboard.game_over()

    # Check for player reaching the goal and update the score
    if player.ycor() == 170:
        player.player_reset()
        scoreboard.level += 1
        scoreboard.update_level()
        cars.car()
        cars.move_dist += 2

screen.exitonclick()