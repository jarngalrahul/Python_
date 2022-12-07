# using python packages
from prettytable import PrettyTable
import turtle

turtleObj = turtle.Turtle()
turtle.shape("turtle")
turtle.color("red", "green")

screenObj = turtle.Screen()
for i in range(1, 50):
    turtle.forward(i*2)
    turtle.right(45)
for i in range(1, 40):
    turtle.forward(i*2)
    turtle.right(90)
# default dimensions of turtle screen - 300x300
print(screenObj.canvheight)
screenObj.exitonclick()


table = PrettyTable()
table.field_names = ["Pokemon name", "Type"]
table.add_rows(
    [
        ["Pikachu", "Electric"],
        ["Squirtle", "Water"],
        ["Charmander", "Fire"],
    ]
)
table.align = 'l'
print(table)
