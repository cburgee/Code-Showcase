from turtle import Turtle
import random

from constants import BOARD_WIDTH, BOARD_HEIGHT

FOOD_BOUNDARY_WIDTH = (BOARD_WIDTH / 2) - 20
FOOD_BORDER_HEIGHT = (BOARD_HEIGHT / 2) - 20


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.set_new_pos()

    def set_new_pos(self):
        random_x = random.randint(-FOOD_BOUNDARY_WIDTH, FOOD_BOUNDARY_WIDTH)
        random_y = random.randint(-FOOD_BORDER_HEIGHT, FOOD_BORDER_HEIGHT)
        self.goto(random_x, random_y)
