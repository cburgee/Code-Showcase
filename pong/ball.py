from turtle import Turtle
from constants import (
    WINDOW_MIDDLE,
    BALL_MOVE_DISTANCE_X,
    BALL_MOVE_DISTANCE_Y,
    UP,
    DOWN,
    LEFT,
    RIGHT,
)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()

    def create_ball(self):
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(WINDOW_MIDDLE)

    def get_direction(self):
        return self.current_x_dir, self.current_y_dir

    def set_direction(self, x_dir=None, y_dir=None):
        if y_dir:
            self.current_y_dir = y_dir
        if x_dir:
            self.current_x_dir = x_dir

    def reverse_direction(self, x=False, y=False):
        if y:
            if self.get_direction()[1] == UP:
                self.set_direction(y_dir=DOWN)
            else:
                self.set_direction(y_dir=UP)
        if x:
            if self.get_direction()[0] == RIGHT:
                self.set_direction(x_dir=LEFT)
            else:
                self.set_direction(x_dir=RIGHT)

    def direction(self):
        MOVE_RIGHT = self.xcor() + BALL_MOVE_DISTANCE_X
        MOVE_LEFT = self.xcor() - BALL_MOVE_DISTANCE_X
        MOVE_UP = self.ycor() + BALL_MOVE_DISTANCE_Y
        MOVE_DOWN = self.ycor() - BALL_MOVE_DISTANCE_Y

        if self.get_direction()[0] == RIGHT:
            new_x = MOVE_RIGHT
        if self.get_direction()[0] == LEFT:
            new_x = MOVE_LEFT
        if self.get_direction()[1] == UP:
            new_y = MOVE_UP
        if self.get_direction()[1] == DOWN:
            new_y = MOVE_DOWN
        return new_x, new_y

    def move(self):
        new_pos = self.direction()
        self.goto(new_pos[0], new_pos[1])

    def bounce_y(self):
        self.reverse_direction(y=True)

    def bounce_x(self):
        self.reverse_direction(x=True)

    def reset(self):
        self.reverse_direction(x=True, y=True)
        self.goto(0, 0)
