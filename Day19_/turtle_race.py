# Object having different attributes and performing different functions at the same time is called their
# state (say their color, height etc in Turtle objects)

import random
import turtle as t
t.title("----------Turtle race----------")
screen = t.Screen()
screen.setup(width=500, height=400)  # sizing the window
# displays a popup for us to write a text
user_bet = screen.textinput(title="Make your bet",
                            prompt="Which turtle will win? Enter the colour?")

if user_bet:
    is_race_on = True
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
all_turtles = []

for x in range(6):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.color(colors[x], colors[x])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=(x-2)*30)
    all_turtles.append(new_turtle)


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            # winning conditions and msg
            win_color = turtle.pencolor()
            if win_color == user_bet:
                print(
                    f"Congratulations {win_color} turtle is the winner!!!.You won the bet")
            else:
                print(
                    f"{win_color} won. Either way gambling is a vice and you are bad in this")
            is_race_on = False
            ############################
        random_dist = random.randint(0, 10)
        turtle.fd(random_dist)

screen.exitonclick()
