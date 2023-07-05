from turtle import *
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Score

# setting the screen
setup(width=800, height=600)
bgcolor("white")
title("Pong Game")
tracer(0)

left_paddle = Paddle((-380, 0))
right_paddle = Paddle((380, 0))
ball = Ball()
score = Score()

# adding listeners
listen()
onkey(left_paddle.paddle_movement_up, "w")
onkey(left_paddle.paddle_movement_down, "s")
onkey(right_paddle.paddle_movement_up, "Up")
onkey(right_paddle.paddle_movement_down, "Down")


# to omit any unnecessary animations
game_on = True
pace = 0.1
while game_on:
    time.sleep(pace)
    update()
    ball.ball_move()

    # detecting collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    # detecting collision with the paddles
    if ball.distance(left_paddle) < 50 and ball.xcor() < -350 or ball.distance(right_paddle) < 50 and ball.xcor() > 350:
        ball.x_bounce()
        pace -= .01


    # detecting when the left player misses
    if ball.xcor() < -400:
        ball.reset_position()
        score.right_point()
        pace = 0.1

    # detecting when the right player misses
    if ball.xcor() > 400:
        ball.reset_position()
        score.left_point()
        pace = 0.1


exitonclick()
