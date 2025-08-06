from turtle import Screen, Turtle
from pad import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

# Screen setup
width = 820
height = 620
screen = Screen()
screen.setup(width, height)
screen.bgcolor("green")
screen.title("Pong")
screen.tracer(0)

mid_line = Turtle()
mid_line.color("white")
mid_line.width(5)
mid_line.penup()
mid_line.goto(0, 280)
mid_line.setheading(270)
mid_line.hideturtle()
for i in range(28):
    mid_line.pendown()
    mid_line.fd(10)
    mid_line.penup()
    mid_line.fd(10)



r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
scoreboard = Scoreboard()
ball = Ball()

screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")

screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

ball_speed = 0.1

game_is_on = True
while game_is_on:
    time.sleep(ball_speed)
    screen.update()
    ball.shape_reset()
    ball.move_ball()

    # Wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        ball.skewy()

   # Paddle collision
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.skewx()
        ball.bounce_x()
        ball_speed *= 0.9

    if ball.distance(l_paddle) < 50 and ball.xcor() > -318:
        ball.skewx()
        ball.bounce_x()
        ball_speed *= 0.9

    # Ball goes out right
    if ball.xcor() > 380:
        r_paddle.goto(350, 0)
        l_paddle.goto(-350, 0)
        ball.reset_pos()
        scoreboard.l_point()
        ball_speed = 0.1

    # Ball out left
    if ball.xcor() < -380:
        r_paddle.goto(350, 0)
        l_paddle.goto(-350, 0)
        ball.reset_pos()
        scoreboard.r_point()
        ball_speed = 0.1



screen.exitonclick()