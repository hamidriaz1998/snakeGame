from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.printScore()

    def incrementScore(self):
        self.score += 1

    def printScore(self):
        self.reset()
        self.penup()
        self.color("white")
        self.goto(0, 280)
        self.hideturtle()
        self.write(f"Score: {self.score}", align="Center")
