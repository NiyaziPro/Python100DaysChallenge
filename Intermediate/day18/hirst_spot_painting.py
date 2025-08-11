import random
import turtle

import colorgram

# colors = colorgram.extract('image.jpg',30)
#
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.g
#     g = color.rgb.g
#     b = color.rgb.b
#     new_colors = (r,g,b)
#     rgb_colors.append(new_colors)
#
# print(rgb_colors)


turtle.colormode(255)
t = turtle.Turtle()

t.speed("fastest")
t.penup()
t.hideturtle()
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40),
              (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71),
              (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74),
              (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97),
              (176, 192, 209)]

t.setheading(225)
t.forward(300)
t.setheading(0)

num_of_dots = 100

for dot_count in range(1, num_of_dots + 1):
    t.dot(20, random.choice(color_list))
    t.forward(50)

    if dot_count % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)

screen = turtle.Screen()
screen.exitonclick()
