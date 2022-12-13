# A very rough pong game
# bug --- contact with paddle
from scoreboard import ScoreBoard
from ball import Ball
from Paddle import Paddle
import turtle
import time


screen = turtle.Screen()
screen.title("PONG")
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()
# screen movements
screen.listen()
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(right_paddle) < 50 and ball.xcor() > 330 or ball.distance(left_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()
    # left player gets the point
    if ball.xcor() > 340:
        ball.reset()
        scoreboard.update_lscore()

    # right player gets the point
    if ball.xcor() < -340:
        ball.reset()
        scoreboard.update_rscore()


screen.exitonclick()
