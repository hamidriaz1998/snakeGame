from turtle import Turtle

MOVEPOS = [(0, 0), (-20, 0), (-40, 0)]
MOVEDIS = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.createSnake()
        self.head = self.segments[0]

    def createSnake(self):
        for i in MOVEPOS:
            self.addSegment(i)

    def addSegment(self, postion):
        x, y = postion
        newSegment = Turtle("square")
        newSegment.penup()
        newSegment.color("white")
        newSegment.goto(x, y)
        self.segments.append(newSegment)

    def extendSnake(self):
        self.addSegment(self.segments[-1].pos())

    def move(self):
        for segIdx in range(len(self.segments) - 1, 0, -1):
            x, y = self.segments[segIdx - 1].pos()
            self.segments[segIdx].goto(x, y)
        self.head.forward(MOVEDIS)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
