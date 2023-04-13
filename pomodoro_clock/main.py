from tkinter import *
import math

# Constants given by intructor \/
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
# Constants given by intructor /\
WORK_SEC = 5
SHORT_BREAK_SEC = 5
LONG_BREAK_SEC = 5
reps = 1
timer = None


def start_timer():
    global reps
    if reps == 8:
        count_down(LONG_BREAK_SEC)
        tm_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_SEC)
        tm_label.config(text="Short Break", fg=PINK)
    elif reps % 2 == 1:
        count_down(WORK_SEC)
        tm_label.config(text="Work", fg=GREEN)


def reset_timer():
    global timer
    global reps
    window.after_cancel(timer)
    reps = 1
    chck_label.config(text="")
    tm_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="25:00")


def count_down(count):
    global timer
    global reps
    min = int(count / 60)
    second = count % 60
    if second < 10:
        second = f"0{second}"
    elif second == 0:
        second = "00"
    canvas.itemconfig(timer_text, text=f"{min}:{second}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        if reps < 8:
            reps += 1
            start_timer()
            checks = ""
            work_sessions = math.floor(reps / 2)
            for _ in range(work_sessions):
                checks += "✔"
            chck_label.config(text=checks)


# Window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas
canvas = Canvas(width=204, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato_img)
timer_text = canvas.create_text(
    103, 130, text="25:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(column=1, row=1)


# Timer Label
tm_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 32, "bold"))
tm_label.grid(column=1, row=0)

# Check Mark Label
chck_label = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 12, "normal"))
chck_label.config(pady=20)
chck_label.grid(column=1, row=2)

# Buttons
start_btn = Button(text="Start", command=start_timer)
reset_btn = Button(text="Reset", command=reset_timer)
start_btn.grid(column=0, row=2)
reset_btn.grid(column=2, row=2)

window.mainloop()
