from turtle import *

# https://docs.python.org/3/library/turtle.html

timmy = Turtle()

# print(type(timmy))
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(50)
# timmy.right(50)
# timmy.forward(50)
# timmy.right(100)
#
#
# my_screen = Screen()
# print(my_screen.canvheight)
#
# my_screen.exitonclick()


from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ["Pokemon Name", "Type"]
table.add_row(["Pikachu", "Electric"])
table.add_row(["Squirtle", "Water"])
table.add_row(["Charmander", "Fire"])
print(table)

# or

table2 = PrettyTable()
table2.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table2.add_column("Type", ["Electric", "Water", "Fire"])

print(table2)

table2.align = "r"
print(table2)