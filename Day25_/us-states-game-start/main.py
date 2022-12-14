import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S States Game")
image_path = "Day25_/us-states-game-start/blank_states_img.gif"
screen.addshape(image_path)
turtle.shape(image_path)


country_data = pandas.read_csv("Day25_/us-states-game-start/50_states.csv")
countries = country_data['state'].values


guessed_list = []
while len(guessed_list) <= 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_list)}/50 Guess the state", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        break
    if answer_state in countries and answer_state not in guessed_list:
        guessed_list.append(answer_state)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        coords = country_data[country_data['state'] == answer_state]
        print(coords)
        t.goto(float(coords['x']), float(coords['y']))
        t.write(answer_state, align='center', font=('Calibri', 10, 'bold'))


states_left = [x for x in countries if x not in guessed_list]
df = pandas.DataFrame(states_left)
df.to_csv("Day25_/us-states-game-start/states_to_learn.csv")


# Getting the mouse coordinates printed
####################################
# def get_mouse_click(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click)
# turtle.mainloop()
