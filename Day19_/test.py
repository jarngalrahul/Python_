# Instances, States and Higher order functions
# Higher Order functions : A higher order function is a function that works with other functions
from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()


def move_fwds():
    tim.fd(10)


screen.listen()
screen.onkey(key="space", fun=move_fwds)

screen.exitonclick()
