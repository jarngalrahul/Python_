# Etch a sketch
from turtle import Turtle, Screen
m_oogway = Turtle()
screen = Screen()


def move_fwd():
    m_oogway.fd(10)


def move_back():
    m_oogway.back(10)


def clockwise_rotation():
    m_oogway.right(5)


def anti_clickwise_rot():
    m_oogway.left(5)


def clear_scr():
    m_oogway.clear()
    m_oogway.penup()
    # m_oogway.setpos(0, 0)
    # m_oogway.setheading(0)
    # use the above method or------
    m_oogway.home()
    m_oogway.pendown()


screen.listen()
screen.onkey(key="w", fun=move_fwd)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="d", fun=clockwise_rotation)
screen.onkey(key="a", fun=anti_clickwise_rot)
screen.onkey(key="c", fun=clear_scr)
screen.exitonclick()
