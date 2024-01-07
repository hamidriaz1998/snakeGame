from turtle import Screen
from time import sleep
from snake import Snake
from bonus import Bonus
from scoreBoard import ScoreBoard

# Set Screen parameters
screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=600)
screen.tracer(0)
screen.title("Snake")

# Initialize Snake,bonus pill and ScoreBoard objects
snake = Snake()
bonus = Bonus()
scoreBoard = ScoreBoard()

# Listen for keystrokes
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Game loop
isGameOn = True
while isGameOn:
    screen.update()
    sleep(0.1)
    snake.move()

    # Detect collsion with bonus pill
    if snake.head.distance(bonus) < 15:
        bonus.placeBonus()
        snake.addSegment()
        scoreBoard.incrementScore()
        scoreBoard.printScore()

    # Detect wall collsion
    if (
        snake.head.ycor() > 280
        or snake.head.ycor() < -280
        or snake.head.xcor() > 280
        or snake.head.xcor() < -280
    ):
        isGameOn = False
        scoreBoard.gameOver()


screen.exitonclick()
