from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from constants import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    UP,
    RIGHT,
    LEFT,
    TOP_BOUNDARY,
    BOTTOM_BOUNDARY,
    BALL_COLLISION_WITH_PADDLE_LEFT,
    BALL_COLLISION_WITH_PADDLE_RIGHT,
    RIGHT_BOUNDARY,
    LEFT_BOUNDARY,
)
import time

game_over = False

screen = Screen()
screen.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
screen.bgcolor("black")
screen.title("PONG")
screen.listen()
screen.tracer(0)

paddles = []

paddle_left = Paddle("left")
paddle_right = Paddle("right")
paddles.append(paddle_left)
paddles.append(paddle_right)

scoreboard = Scoreboard()
ball = Ball()
screen.update()


screen.onkey(paddle_left.up, "w")
screen.onkey(paddle_left.down, "s")
screen.onkey(paddle_right.up, "Up")
screen.onkey(paddle_right.down, "Down")
ball.set_direction(RIGHT, UP)



def main_event():
    screen.update()
    ball.move()
    # Detect collision with top and bottom boundaries
    if ball.ycor() > TOP_BOUNDARY or ball.ycor() < BOTTOM_BOUNDARY:
        ball.bounce_y()

    # Detect collision with paddles
    for paddle in paddles:
        if ball.distance(paddle) < 60.0 and (
            ball.xcor() > BALL_COLLISION_WITH_PADDLE_RIGHT
            or ball.xcor() < BALL_COLLISION_WITH_PADDLE_LEFT
        ):
            ball.bounce_x()

    # Detect when ball goes out of bounds left/right
    if ball.xcor() > RIGHT_BOUNDARY:
        ball.reset()
        scoreboard.increase_score(LEFT)
    if ball.xcor() < LEFT_BOUNDARY:
        ball.reset()
        scoreboard.increase_score(RIGHT)

    screen.ontimer(main_event, 40)

screen.ontimer(main_event, 40)
screen.exitonclick()
game_over = True
