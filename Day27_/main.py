# Tkinter
import tkinter
# window
window = tkinter.Tk()
window.title("My First GUI program")
window.minsize(width=500, height=500)
window.config(padx=100, pady=200)

# label
my_label = tkinter.Label(text="I'm a label", font=(
    "Arial", 24, "bold"), foreground="pink")
# my_label.pack()
# my_label.place(x=0,y=0)
my_label.grid(column=0, row=0)
my_label.config(padx=20, pady=20)


def demo_btn_fn():
    # Using the next commands we can edit the properties of label
    # my_label['text'] = "New Text"
    new_text = input.get()
    my_label.config(text=new_text, background="red", foreground="yellow")


# Button
button1 = tkinter.Button(text="Click Me", command=demo_btn_fn)
button1.grid(column=1, row=1)
new_btn = tkinter.Button(text="NewButton")
new_btn.grid(row=0, column=2)

# Entry component
input = tkinter.Entry(width=10)
input.grid(column=3, row=2)
window.mainloop()
