from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color('white')
        self.x = 1
        self.y = 1
        self.speed = 0.1

    def move(self):
        new_x = self.xcor()+10*self.x
        new_y = self.ycor()+10*self.y
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.x *= -1
        self.speed *= 0.9

    def bounce_y(self):
        self.y *= -1
        self.speed *= 0.9

    def reset(self):
        self.goto(0, 0)
        self.x *= -1
        self.speed = 0.1

# bounces on all sides
# def check_pos(self):
#     if self.ycor() == 280:
#         self.y = -1
#     if self.xcor() == 380:
#         self.x = -1
#     if self.ycor() == -280:
#         self.y = 1
#     if self.xcor() == -380:
#         self.x = 1
