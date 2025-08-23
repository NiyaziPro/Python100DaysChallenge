from turtle import Turtle, Screen

leo = Turtle()
screen = Screen()


# https://docs.python.org/3/library/turtle.html#turtle.listen

def move_forwards():
    leo.forward(10)


def move_backwards():
    leo.backward(10)


def turn_left():
    new_heading = leo.heading() + 10
    leo.setheading(new_heading)


def turn_right():
    new_heading = leo.heading() - 10
    leo.setheading(new_heading)

def clear():
    leo.clear()
    leo.penup()
    leo.home()
    leo.pendown()

screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")
screen.exitonclick()
