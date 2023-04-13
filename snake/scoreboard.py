import os
from turtle import Turtle
from constants import BOARD_HEIGHT

ALIGNMENT = "center"
FONT = ("Courier", 14, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        if os.path.exists("high_score"):
            with open("high_score", mode="r") as file:
                self.high_score = file.read()
        self.hideturtle()
        self.penup()
        self.color("gray")
        self.goto(0, (BOARD_HEIGHT / 2) - 30)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score} " f" High Score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT,
        )

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
        with open("high_score", mode="w") as file:
            file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
