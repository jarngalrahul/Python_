from tkinter import *
FONT = ("Arial", 18, "normal")
window = Tk()
# window.minsize(height=200, width=400)
window.config(padx=40, pady=30)
window.title("Mile to km Converter")

# Entry
entry = Entry(width=10)
entry.config(border=5)
entry.grid(column=1, row=0)

# Label
label1 = Label(text="Miles", font=FONT)
label1.grid(column=2, row=0)

label2 = Label(text="is equal to", font=FONT)
label2.grid(column=0, row=1)

label3 = Label(text="0", font=FONT)
label3.grid(column=1, row=1)

label4 = Label(text="Km", font=FONT)
label4.grid(column=2, row=1)


# button


def convert():
    result = float(entry.get())*1.6
    label3.config(text=f"{round(result, 2)}", font=FONT)


btn = Button(text="Calculate", command=convert)
btn.grid(column=1, row=2)
window.mainloop()
