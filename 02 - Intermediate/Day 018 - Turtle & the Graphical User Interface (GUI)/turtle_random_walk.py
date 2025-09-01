import turtle
from random import *
from turtle import *

raphael = Turtle()
turtle.colormode(255)
def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    random_colors = (r,g,b)
    return random_colors

directions = [0, 90, 180, 270]
raphael.pensize(15)
raphael.speed("fastest")

for _ in range(200):
    raphael.color(random_color())
    raphael.forward(30)
    raphael.setheading(choice(directions))
