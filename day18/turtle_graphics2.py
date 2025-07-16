import random
from turtle import *

leo = Turtle()
colors = ["CornflowerBlue","DarkOrchid", "blue", "green", "cyan", "red"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        leo.forward(100)
        leo.right(angle)

for shape_side in range(3,11):
    leo.color(random.choice(colors))
    draw_shape(shape_side)

screen = Screen()
screen.exitonclick()