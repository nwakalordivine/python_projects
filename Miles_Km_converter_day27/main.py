import tkinter as tk

window = tk.Tk()
window.title("Miles to Km Converter")
window.minsize(width=270, height=150)
window.config(padx=20, pady=20)

label_1 = tk.Label(text="is equal to", font=("calibri", 15, "normal"))
label_1.grid(column=0, row=1)

label_2 = tk.Label(text="Km", font=("calibri", 15, "normal"))
label_2.grid(column=2, row=1)

label_3 = tk.Label(text="Miles", font=("calibri", 15, "normal"))
label_3.grid(column=2, row=0)


def calculate():
    number = float(inputs.get())
    working = round((number * 1.609), 2)
    answer.config(text=str(working))


answer = tk.Label(text="0", font=("calibri", 15, "normal"))
answer.grid(column=1, row=1)

button = tk.Button(text="calculate", command=calculate)
button.grid(column=1, row=2)

inputs = tk.Entry(width=8)
inputs.insert(tk.END, string="0")
inputs.grid(column=1, row=0)

window.mainloop()
