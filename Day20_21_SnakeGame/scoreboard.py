from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 16, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        self.score = -1
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0, 280)
        self.score_update()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", align=ALIGNMENT, font=FONT)

    def score_update(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT,
                   font=FONT)


# move = False: this means we would not get a trace from origin
# till the arg is printed
