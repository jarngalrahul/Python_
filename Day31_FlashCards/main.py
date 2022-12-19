from io import BytesIO
from gtts import gTTS
from tkinter import *
from random import randint, choice
import os
import pandas
BACKGROUND_COLOR = "#B1DDC6"
flip_timer = None
current_card = {}


# -------------------------SELECTING THE FILE------------------------------#
path1 = "Day31_FlashCards//data//french_words.csv"
path2 = "Day31_FlashCards//data//words_to_learn.csv"
if os.path.exists(path2):
    try:
        data = pandas.read_csv(filepath_or_buffer=path2)
    except:
        # checking for empty file exception and reinitialising it
        data = pandas.read_csv(filepath_or_buffer=path1)
else:
    data = pandas.read_csv(filepath_or_buffer=path1)
to_learn = data.to_dict(orient="records")
# -----------------------------Flip Card---------------------------#


def change_card():
    global current_card
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


# ---------------------------NEW RANDOM WORD-------------------------#


def random_card():
    global flip_timer, current_card
    if flip_timer != None:
        window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    new_word = current_card["French"]
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=new_word, fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, change_card)

# ------------------------WORDS KNOWN-----------------------#
# TODO:Remove the word from the list if user presses tick


def remove_word():
    to_learn.remove(current_card)
    df = pandas.DataFrame(to_learn)
    df.to_csv(path2, index=False)


# ------------------------UI SETUP-----------------------#
window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flashy")
window.minsize()

# Creating an image with names
card_back_img = PhotoImage(file="Day31_FlashCards//images//card_back.png")
card_front_img = PhotoImage(file="Day31_FlashCards//images//card_front.png")
right_img = PhotoImage(file="Day31_FlashCards//images//right.png")
wrong_img = PhotoImage(file="Day31_FlashCards//images//wrong.png")

# Creating canvas
canvas = Canvas(width=800, height=526,
                bg=BACKGROUND_COLOR, highlightthickness=0)
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(
    400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(
    400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Creating Buttons
wrong_btn = Button(image=wrong_img, highlightthickness=0,
                   pady=50, command=random_card)
wrong_btn.grid(row=1, column=0)
right_btn = Button(image=right_img, highlightthickness=0,
                   pady=50, command=lambda: [random_card(), remove_word()])
right_btn.grid(row=1, column=1)

# Initialising the first tile
random_card()
window.mainloop()
