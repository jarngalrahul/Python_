# Snake game
from turtle import Turtle, Screen
from scoreboard import ScoreBoard
from food import Food
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
# turns turtle animation on or off and we
# can also set delays to update drawings
screen.tracer(0)


game_is_on = True
snake = Snake()
food = Food()
score = ScoreBoard()
screen.listen()

screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

while game_is_on:
    screen.update()
    time.sleep(0.05)
    snake.move()

    # Detecting collisions with food, refreshing food's position
    # and extending the snake
    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        score.score_update()

    # detecting collisions with the wall and calling gamw_over
    # method of scoreBoard class
    if snake.head.xcor() > 265 or snake.head.xcor() < -285 or snake.head.ycor() > 270 or snake.head.ycor() < -270:
        game_is_on = False
        score.game_over()

    # detecting collisions with tail or body
    # - if this condition holds true trigger game_over
    for segment in snake.all_segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()


screen.update()
screen.exitonclick()
