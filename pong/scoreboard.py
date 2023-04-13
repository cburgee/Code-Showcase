from turtle import Turtle
from constants import (
    SCOREBOARD_LEFT_POS_X,
    SCOREBOARD_POS_Y,
    SCOREBOARD_RIGHT_POS_X,
    RIGHT,
)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def increase_score(self, player):
        if player == RIGHT:
            self.r_score += 1
        else:
            self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(SCOREBOARD_LEFT_POS_X, SCOREBOARD_POS_Y)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(SCOREBOARD_RIGHT_POS_X, SCOREBOARD_POS_Y)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))
