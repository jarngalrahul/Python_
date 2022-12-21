from tkinter import *
import requests


def get_quote():
    # Write your code here.
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    canvas.itemconfig(quote_text, text=f"{data['quote']}")


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

background_img = PhotoImage(file="Day33_API/Kanye-Quotes/background.png")
kanye_img = PhotoImage(file="Day33_API/Kanye-Quotes/kanye.png")

canvas = Canvas(width=300, height=414)
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=(
    "Arial", 20, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)


window.mainloop()
