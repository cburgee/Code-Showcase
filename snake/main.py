from turtle import Screen
from snake import Snake
from food import Food
from constants import BOARD_HEIGHT, BOARD_WIDTH, MIN_X, MIN_Y, MAX_X, MAX_Y
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=BOARD_WIDTH, height=BOARD_HEIGHT)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

def main_event():
    screen.update()
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 18:
        food.set_new_pos()
        scoreboard.increase_score()
        snake.extend()

    # Detect Collision with Body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
    # Detect collision with wall
    if (
        snake.head.xcor() > MAX_X
        or snake.head.xcor() < MIN_X
        or snake.head.ycor() > MAX_Y
        or snake.head.ycor() < MIN_Y
    ):
        scoreboard.reset()
        snake.reset()

    screen.ontimer(main_event, 70)


game_is_on = True
screen.ontimer(main_event, 70)
screen.exitonclick()
game_is_on = False
