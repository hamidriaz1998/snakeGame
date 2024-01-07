from turtle import Turtle

MOVEPOS = [(0, 0), (-20, 0), (-40, 0)]
MOVEDIS = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.createSnake()
        self.head = self.segments[0]

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
        self.head.forward(MOVEDIS)

    def up(self):
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)

    def left(self):
        self.head.setheading(180)

    def right(self):
        self.head.setheading(0)
