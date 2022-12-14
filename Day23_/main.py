# Turtle crossing game
import turtle
import time
from car import Car
from player import Player
from scoreboard import ScoreBoard

screen = turtle.Screen()
screen.title('Turtle Crossing Game')
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score = ScoreBoard()

# Binding moveup function with the up arrow key
screen.listen()
screen.onkeypress(player.move_up, "Up")

# To save car objects
cars = []
game_is_on = True
count = 5
# for changing speed of car objects
spd = 0.1

# main while loop
while game_is_on:
    time.sleep(spd)
    screen.update()
    # checking if player passed the level
    if player.ycor() > 280:
        player.set_pos()
        score.update_level()
        spd *= 0.9
    # making cars and moving them
    if count == 5:
        new_car = Car()
        cars.append(new_car)
        count = 0
    else:
        count += 1
    for car in cars:
        car.move()
        if player.distance(car) < 25:
            score.game_over()
            game_is_on = False
            break


screen.exitonclick()
