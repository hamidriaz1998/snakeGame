from turtle import Turtle

FONT = ("Arial", 14, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.printScore()
        self.goto(0, 280)

    def incrementScore(self):
        self.score += 1

    def printScore(self):
        self.clear()
        self.write(f"Score: {self.score}", align="Center", font=FONT)

    def gameOver(self):
        self.clear()
        self.goto(0, 0)
        self.write("Game over", align="center", font=FONT)
