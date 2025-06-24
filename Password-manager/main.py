import json
from tkinter import *
from random import randint, choice, shuffle
from tkinter import messagebox
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_gen():
    password_entry.delete(0, END)
    # password letters, words and symbols for our password
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_number = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbol = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letter+password_symbol+password_number
    password = password_list
    shuffle(password)
    updated_password = "".join(password)
    password_entry.insert(END, updated_password)
    pyperclip.copy(updated_password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def write_data(new_data):
    with open("data.json", mode='w') as user_data:
        json.dump(new_data, user_data, indent=4)


def save_data():
    website = website_entry.get().title()
    email = email_username_entry.get()
    password_used = password_entry.get()

    data = {
        website: {
            "email": email,
            "password": password_used
        }
    }

    if len(website) == 0 or len(password_used) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")

    else:
        try:
            with open("data.json", mode='r') as user_data:
                json_data = json.load(user_data)
        except FileNotFoundError:
            write_data(data)
        else:
            json_data.update(data)
            write_data(json_data)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
def search_password():
    website = website_entry.get().title()
    try:
        with open("data.json", mode='r') as user_data:
            json_data = json.load(user_data)
    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="This file doesn't exist")
    else:
        if website in json_data:
            web_search = json_data[website]
            messagebox.showinfo(title=web_search, message=f"{website}\nEmail: {web_search['email']}"
                                                          f"\nPassword: {web_search['password']}")
        else:
            messagebox.showwarning(title="Oop", message=f"You have no data on {website}")


window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")

canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_entry = Entry(width=20)
website_entry.focus()
website_entry.grid(column=1, row=1)
email_username_entry = Entry(width=35)
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(END, string="divinenwakalor31@gmail.com")
password_entry = Entry(width=20)
password_entry.grid(column=1, row=3)

generate_password_button = Button(text="Generate Password", width=11, command=password_gen)
generate_password_button.grid(column=2, row=3)
add_password_button = Button(text="Add", width=33, command=save_data)
add_password_button.grid(column=1, row=4, columnspan=2)
search_button = Button(text="Search", width=10, command=search_password)
search_button.grid(column=2, row=1)
window.mainloop()
