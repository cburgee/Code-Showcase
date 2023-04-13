from turtle import Turtle
from constants import (
    START_X_LEFT,
    START_X_RIGHT,
    PADDLE_MOVE_DISTANCE,
    HEADING_DIRECTION,
)


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self, position):
        start_pos = [START_X_RIGHT, 0]
        if position == "left":
            start_pos[0] = START_X_LEFT
        self.shape("square")
        self.setheading(HEADING_DIRECTION)
        self.color("white")
        self.penup()
        self.turtlesize(stretch_wid=1, stretch_len=5)
        self.goto(start_pos[0], start_pos[1])

    def up(self):
        self.forward(PADDLE_MOVE_DISTANCE)

    def down(self):
        self.backward(PADDLE_MOVE_DISTANCE)
