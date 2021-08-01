# Libraries
import math
from tkinter import *
from math import *

# Constants
ORANGE = "#ff7f50"
RED = "#D83A56"
GREEN = "#009432"
YELLOW = "#F8EFBA"
FONT_NAME = "raleway"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# Reset timer
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0
    check_mark_label.config(text="")
    title_label.config(text="Timer", fg=GREEN)


# Clock timer
def start_timer():
    global reps
    reps += 1
    if reps > 8:
        reps = 0
        start_timer()
    else:
        work_sec = WORK_MIN * 60
        short_break_sec = SHORT_BREAK_MIN * 60
        long_break_sec = LONG_BREAK_MIN * 60
        if reps % 8 == 0:
            title_label.config(text="Break", fg=RED)
            count_down(long_break_sec)
        elif reps % 2 == 0:
            title_label.config(text="Break", fg=ORANGE)
            count_down(short_break_sec)
        else:
            title_label.config(text="Work", fg=GREEN)
            count_down(work_sec)


# Timer countdown
def count_down(count):
    global timer
    count_minute = floor(count / 60)
    count_second = floor(count % 60)
    if count_second < 10:
        count_second = f"0{count_second}"
    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_second}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += "✔"
        check_mark_label.config(text=marks)


# UI setup
# Window object definition
window = Tk()
window.title("Pomodoro Technique Timer")
window.resizable(width=False, height=False)
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas widget
canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
pomodoro_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 110, image=pomodoro_image)
timer_text = canvas.create_text(100, 125, text="00:00", font=(FONT_NAME, 24, "bold"), fill="white")
canvas.grid(row=1, column=1)

# Timer title
title_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(row=0, column=1)

# Start button
start_button = Button(text="START", font=(FONT_NAME, 10, "bold"), fg="white", bg=GREEN, padx=5, command=start_timer)
start_button.grid(row=2, column=0)

# Check mark label
check_mark_label = Label(font=(FONT_NAME, 10, "bold"), fg=ORANGE, bg=YELLOW, pady=20)
check_mark_label.grid(row=2, column=1)

# Reset button
reset_button = Button(text="RESET", font=(FONT_NAME, 10, "bold"), fg="white", bg=GREEN, padx=5, command=reset_timer)
reset_button.grid(row=2, column=2)

# Window on screen
window.mainloop()
