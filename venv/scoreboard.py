from turtle import Turtle

FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-240, 250)
        self.write(f"level:{self.score}", align ="center", font = FONT)

    def point(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.penup()
        self.hideturtle()
        self.color("red")
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)
