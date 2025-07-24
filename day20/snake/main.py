import time
from turtle import Turtle, Screen

from day20.snake.snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# segment_1 = Turtle(shape="square")
# segment_1.color("white")
#
# segment_2 = Turtle(shape="square")
# segment_2.color("white")
# segment_2.goto(-20, 0)
#
# segment_3 = Turtle(shape="square")
# segment_3.color("white")
# segment_3.goto(-40, 0)

# https://docs.python.org/3.3/library/turtle.html?highlight=turtle#turtle.tracer

snake = Snake()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()


screen.exitonclick()
