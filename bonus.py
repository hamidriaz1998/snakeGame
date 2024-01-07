from turtle import Turtle
from random import randint as rand

# Specify Screen Borders for random generation of bonus pill
SCREENBORDERS = (-280, 280)


class Bonus(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shapesize(0.5, 0.5)
        self.shape("circle")
        self.color("green")
        self.speed("fastest")
        self.goto(rand(*SCREENBORDERS), rand(*SCREENBORDERS))
