# https://docs.python.org/3/library/turtle.html
# https://trinket.io/docs/colors
# https://cs111.wellesley.edu/reference/colors

from turtle import *

# timmy = Turtle()
#
# timmy.shape("turtle")
# timmy.color("green")
# timmy.forward(100)
# timmy.backward(200)
# timmy.right(90)
# timmy.left(180)
# timmy.setheading(0)

# for line in range(4):
#     timmy.forward(100)
#     timmy.left(90)
#
#
# screen = Screen()
# screen.exitonclick()

import heroes as hero

#print(hero.gen())
leo = Turtle()
for i in range(1,11):
    leo.forward(10)
    leo.penup()
    leo.forward(10)
    leo.pendown()

screen = Screen()
screen.exitonclick()