import json
import random
from tkinter import *
from tkinter import messagebox
import pyperclip
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
special_chars = ['!', '@', '#', '%', '^', '&', '*', '+']
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    choice = []
    choice.extend(random.choices(special_chars, k=2))
    choice.extend(random.choices(letters, k=8))
    choice.extend(random.choices(numbers, k=2))
    random.shuffle(choice)
    password = "".join(choice)
    password_entry.delete(0, END)
    password_entry.insert(0, string=password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_json_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if website == "" or email == "" or password == "":
        messagebox.showinfo(
            title="Oops", message="Please don't leave any feilds empty!")
    else:
        # data = f"{website} | {email} | {password}\n"
        try:
            with open(file="Day29_/data.json", mode="r") as data_file:
                old_data = json.load(data_file)
                # print(type(old_data)) --> <dict>
        except FileNotFoundError:
            with open(file="Day29_/data.json", mode="w") as data_file:
                json.dump(new_json_data, data_file, indent=4)
        else:
            old_data.update(new_json_data)
            with open(file="Day29_/data.json", mode="w") as data_file:
                json.dump(old_data, data_file, indent=4)
        finally:
            password_entry.delete(0, END)
            website_entry.delete(0, END)

# ---------------------------- SEARCH FUNCTIONALITY SETUP ------------------------------- #


def find_password():
    website = website_entry.get()
    try:
        with open("Day29_//data.json") as data_file:
            data = json.load(data_file)
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(
                title="Data", message=f"Email: {email}\nPassword: {password}")
    except FileNotFoundError:
        messagebox.showerror(title="Error!", message="No Data File Found")
    except KeyError:
        messagebox.showerror(
            title="Error!", message=f"No details for website {website} exists")
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.minsize()
window.config(padx=50, pady=50)

lock_img = PhotoImage(file="Day29_/logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

# Labels in the generator
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky='E')
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, sticky='E')
password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky='E')

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=1, sticky='EW')
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky='EW')
email_entry.insert(0, string="rahul@example.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky='EW')

# Buttons
generate_password_btn = Button(
    text="Generate Password", command=generate_password)
generate_password_btn.grid(row=3, column=2, sticky='W')

add_btn = Button(text="Add", width=36, command=add_data)
add_btn.grid(row=4, column=1, columnspan=2, sticky='EW')

search_btn = Button(text="Search", command=find_password)
search_btn.grid(row=1, column=2, sticky='EW')

window.mainloop()
