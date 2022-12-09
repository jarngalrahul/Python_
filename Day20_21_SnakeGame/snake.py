import turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
RIGHT = 0
DOWN = 270


class Snake:
    def __init__(self):
        self.all_segments = []
        self.create_snake()
        self.head = self.all_segments[0]

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)

    def add_segment(self, pos):
        new_segment = turtle.Turtle("square")
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(pos)
        self.all_segments.append(new_segment)

    def extend(self):
        self.add_segment(self.all_segments[-1].position())

    def move(self):
        length = len(self.all_segments)
        for seg_num in range(length-1, 0, -1):
            new_x = self.all_segments[seg_num-1].xcor()
            new_y = self.all_segments[seg_num-1].ycor()
            self.all_segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
