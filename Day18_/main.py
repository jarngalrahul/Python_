# extrscting the colors and using them to make million dollar paintings
# importing colors from the given jpg image using colorgram
# import colorgram
import turtle as t
import random
# colors = colorgram.extract("img.jpg", 30)

# rgb_list = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_list.append(new_color)

# print(rgb_list)

# converted the received data to list of tuples
color_list = [(83, 98, 142), (218, 132, 75), (253, 250, 252),
              (220, 223, 79), (152, 159, 177), (89, 111, 98), (155, 166, 159),
              (111, 122, 152), (163, 93, 47), (182, 188, 208), (183, 133, 49),
              (180, 177, 179), (221, 224, 26), (211, 109, 49), (118, 133, 124),
              (185, 195, 188), (226, 182, 160), (52, 62, 86), (195, 189, 192),
              (53, 70, 65), (49, 60, 74), (48, 66, 62), (186, 194, 196),
              (56, 68, 70)]

turtle_sensei = t.Turtle(shape="turtle", visible=False)
screen = t.Screen()

screen.setworldcoordinates(0, 0, 600, 600)

# Not useful in this case sets the opening window size but inside is same
# x = t.window_height()
# y = t.window_width()
# t.Screen().setup(width=200, height=200, startx=0, starty=0)

t.colormode(255)
turtle_sensei.speed('fastest')
turtle_sensei.hideturtle()
turtle_sensei.penup()
for i in range(10):
    turtle_sensei.goto(0, (i+1)*50)
    for _ in range(10):
        turtle_sensei.fd(50)
        turtle_sensei.dot(20, random.choice(color_list))
    turtle_sensei.penup()


screen.exitonclick()
