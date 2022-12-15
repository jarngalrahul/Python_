from tkinter import *

# New Window
window = Tk()
window.title("Tkinter widget demo")
window.minsize(width=500, height=500)

# Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.pack()

# Buttons


def action():
    print("Doing something")


btn = Button(text="Click Me", command=action)
btn.pack()

# Entries
entry = Entry(width=30)
entry.insert(index=END, string="Some text")
print(entry.get())
entry.pack()

# text
text = Text(height=5, width=30)
text.focus()
text.insert(END, "Some multi-line text entry.")
print(text.get("1.0", END))
text.pack()


# Spinbox -
def spinbox_used():
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=100, width=5, command=spinbox_used)
spinbox.pack()

# Scale - The function defined is called with the current value


def scale_used(val):
    print(val)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# CheckButton
def checkbuttn_used():
    print(checked_state.get())


# Returns the checked state in 0 or 1
checked_state = IntVar()
checkbutton = Checkbutton(
    text="Is On?", variable=checked_state, command=checkbuttn_used)
checked_state.get()
checkbutton.pack()


# Radio button
def radio_used():
    print(radio_state.get())


# Variable to hold on to which radio button
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option 1", value=1,
                           variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option 2", value=2,
                           variable=radio_state, command=radio_used)
radiobutton3 = Radiobutton(text="Option 3", value=3,
                           variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()
radiobutton3.pack()


# ListBox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Mango", "Orange", "Banana"]
for fruit in fruits:
    listbox.insert(fruits.index(fruit), fruit)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
###########################
window.mainloop()
