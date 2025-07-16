from random import *
from turtle import *

raphael = Turtle()

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "SlateGray"]
directions = [0, 90, 180, 270]
raphael.pensize(15)
raphael.speed("fastest")

for _ in range(200):
    raphael.color(choice(colors))
    raphael.forward(30)
    raphael.setheading(choice(directions))
