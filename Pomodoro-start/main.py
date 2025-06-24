import tkinter as tk
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = ""


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    reps = 0
    canvas.itemconfig(timer_text, text=f"00:00")
    title.config(text="Timer")
    mark.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        title.config(text="Break", fg=RED)
        countdown(long_break)
    elif reps % 2 == 0:
        title.config(text="Break", fg=PINK)
        countdown(short_break)
    else:
        title.config(text="Work")
        countdown(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    minutes = math.floor(count / 60)
    seconds = round(count % 60)
    if minutes < 10:
        minutes = f"0{minutes}"
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✔"
            mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
my_image = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=my_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = tk.Button(text="Start", bg=YELLOW, highlightbackground=YELLOW, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tk.Button(text="Reset", bg=YELLOW, highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(column=2, row=2)

title = tk.Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, "normal"))
title.grid(column=1, row=0)

mark = tk.Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "normal"))
mark.grid(column=1, row=4)

window.mainloop()
