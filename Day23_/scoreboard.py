from turtle import Turtle
FONT = ("Calibri", 20, 'normal')
FONT_GAME_OVER = ("Calibri", 40, 'bold')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-250, 270)
        self.level = 0
        self.update_level()

    def update_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align='center', font=FONT)

    def game_over(self):
        self.home()
        self.write("GAME OVER", align='center', font=FONT_GAME_OVER)
