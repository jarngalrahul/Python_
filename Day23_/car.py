import turtle
import random
DISTANCE = 10


class Car(turtle.Turtle):
    car_count = 0

    def __init__(self):
        super().__init__()
        Car.car_count += 1
        self.shape('square')
        self.penup()
        self.generating_pos()
        self.shapesize(stretch_wid=1.0, stretch_len=3.0)

    def generating_pos(self):
        turtle.Screen().colormode(255)
        self.random_color()
        self.goto(300, self.new_y())

    def new_y(self):
        quad = random.randint(0, 1)
        if quad == 0:
            return -random.randint(0, 200)
        return random.randint(0, 200)

    def random_color(self):
        x = random.randint(0, 255)
        y = random.randint(0, 255)
        z = random.randint(0, 255)
        self.color((x, y, z))

    def move(self):
        new_x = self.xcor()-DISTANCE
        self.goto(new_x, self.ycor())
        if self.xcor() < -300:
            self.clear()
            Car.car_count -= 1
