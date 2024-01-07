from turtle import Turtle

MOVEPOS = [(0, 0), (-20, 0), (-40, 0)]
MOVEDIS = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.createSnake()

    def createSnake(self):
        for i in MOVEPOS:
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(i)
            self.segments.append(segment)

    def move(self):
        for segIdx in range(len(self.segments) - 1, 0, -1):
            x, y = self.segments[segIdx - 1].pos()
            self.segments[segIdx].goto(x, y)
        self.segments[0].forward(MOVEDIS)

    def up(self):
        self.segments[0].setheading(90)

    def down(self):
        self.segments[0].setheading(270)

    def left(self):
        self.segments[0].setheading(180)

    def right(self):
        self.segments[0].setheading(0)
