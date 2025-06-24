# import tkinter as tk
#
# window = tk.Tk()
# window.title("My first GUI program")
# window.minsize(width=500, height=300)
# window.config(padx=20, pady=30)
#
# my_label = tk.Label(text="I am a copy Ninja", font=("calibri", 20, "normal"))
# my_label.grid(column=0, row=0)
# my_label["text"] = "testing mic guys"
# my_label.config(text="okay testing's done")
#
#
# def clicked():
#     if inputs.get():
#         my_label.config(text=inputs.get())
#     else:
#         my_label.config(text="Button got click")
#
#
# button = tk.Button(text="Click Me", command=clicked)
# button.grid(column=1, row=1)
#
# new_button = tk.Button(text="Click Me")
# new_button.grid(column=2, row=0)
#
# inputs = tk.Entry(width=10)
# # inputs.insert(tk.END, string="user@mail.com")
# inputs.grid(column=3, row=2)

# text = tk.Text(width=50, height=5)
# text.focus()
# text.insert(tk.END, chars="multiline input")
# print(text.get(1.0, tk.END))
# text.grid(column=1, row=2)

#
# def spin_box():
#     print(spinbox.get())
#
#
# spinbox = tk.Spinbox(from_=0, to=10, width=5, command=spin_box)
# spinbox.pack()
#
#
# def scale_box(value):
#     print(value)
#     return value
#
#
# scale = tk.Scale(from_=0, to=100, command=scale_box)
# scale.pack()
#
#
# def checked_state():
#     print(check_state.get())
#
#
# check_state = tk.IntVar()
# check_button = tk.Checkbutton(text="is_on", variable=check_state, command=checked_state)
# check_state.get()
# check_button.pack()
#
#
# def radio_buttons():
#     print(radio_state.get())
#
#
# radio_state = tk.IntVar()
# radio_button1 = tk.Radiobutton(text="Option1", variable=radio_state, value=0, command=radio_buttons)
# radio_button2 = tk.Radiobutton(text="Option2", variable=radio_state, value=1, command=radio_buttons)
# radio_button3 = tk.Radiobutton(text="Option3", variable=radio_state, value=2, command=radio_buttons)
# radio_state.get()
# radio_button2.pack()
# radio_button1.pack()
# radio_button3.pack()
#
#
# def listbox_used(event):
#     print(list_box.get(list_box.curselection()))
#
#
# list_box = tk.Listbox(height=4)
# fruit = ['Apple', 'Orange', 'Graver', 'Pear']
# for item in fruit:
#     list_box.insert(fruit.index(item), item)
# list_box.bind("<<ListboxSelect>>", listbox_used)
# list_box.pack()

# window.mainloop()
