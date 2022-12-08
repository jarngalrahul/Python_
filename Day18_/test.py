# importing turtle as an alias
################################
# import turtle as t
# obj = t.Turtle()

# using turtle class
######################
import random
import turtle

turtle_sensei = turtle.Turtle()
turtle_sensei.shape("turtle")
turtle_sensei.color("red", "pink")

# drawing a square
#####################################################
# for _ in range(4):
#     turtle_sensei.forward(100)
#     turtle_sensei.right(90)

# drawing a dashed line
#####################################################
# for i in range(100):
#     if i % 2 == 0:
#         turtle_sensei.penup()
#     else:
#         turtle_sensei.pendown()
#     turtle_sensei.forward(2)


# Making polygons from side 3 upto 10
##############################################################
def random_color():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    clr = [r, g, b]  # or we can make it a tuple
    return clr


# def calc_internal_angle(side):
#     angle = 360/side
#     return angle


# for num_of_side in range(3, 11):
#     angle = calc_internal_angle(num_of_side)
#     clr = random_color()
#     turtle.colormode(255)
#     turtle_sensei.pencolor(clr[0], clr[1], clr[2])
#     for _ in range(num_of_side):
#         turtle_sensei.forward(100)
#         turtle_sensei.right(angle)


# random walk, increasing pensize, inc speed
##################################################
# turtle_sensei.pensize(10)
# angle_choice = [0, 90, 180, 270]
# turtle_sensei.speed(10)
# for _ in range(100):
#     turtle.colormode(255)  # we need to use turtle
#     turtle_sensei.pencolor(random_color())
#     angle = random.choice(angle_choice)
#     turtle_sensei.right(angle)
#     turtle_sensei.fd(30)


# Drawing circles (Spirograph)
####################################################
turtle_sensei.speed('fastest')


def spirograpgh(gap_size):
    for _ in range(int(360/gap_size)):
        turtle.colormode(255)
        turtle_sensei.color(random_color())
        turtle_sensei.circle(150)
        turtle_sensei.setheading(turtle_sensei.heading()+gap_size)


spirograpgh(5)

turtle.Screen().exitonclick()
