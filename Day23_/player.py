from turtle import Turtle
MOVEMENT_DIST = 10
ORIGINAL_POS = (0, -280)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.set_pos()
        self.setheading(90)

    def move_up(self):
        self.fd(MOVEMENT_DIST)

    def set_pos(self):
        self.goto(ORIGINAL_POS)
