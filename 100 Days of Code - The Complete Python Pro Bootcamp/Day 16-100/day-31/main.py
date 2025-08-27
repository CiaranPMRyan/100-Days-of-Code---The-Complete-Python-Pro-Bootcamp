from tkinter import *
from tkinter.ttk import Combobox
import pandas as pd
import random
import time

BACKGROUND_COLOR = "#B1DDC6"
CAN_X = 800
CAN_Y = 526

FONT_NAME = "arial"

current_card = {}
lang = ""
to_learn = []

def set_language():
    global lang, to_learn
    lang = combo.get()  # Gets the string from the dropdown list

    data = pd.read_csv(f"./data/{lang}_words.csv")
    to_learn = data.to_dict(orient="records")

def word_generator():
    global lang, current_card, to_learn, flip_timer
    window.after_cancel(flip_timer)
    set_language()

    """ Picks a random word pairing from the spreadsheet """
    current_card = random.choice(to_learn)

    canvas.itemconfig(canvas_image, image=front_image)
    canvas.itemconfig(language, text=f"{lang}", fill="black")
    canvas.itemconfig(guess_word, text=current_card[f"{lang}"], fill="black")

    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=back_image)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(guess_word, text=current_card["English"], fill="white")


# ---------- UI SETUP ---------- #

window = Tk()
window.title("Flashy Lingo")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# ---------- Countdown ---------- #

# Flash Card #

canvas = Canvas(width=CAN_X, height=CAN_Y, highlightthickness=0, bg=BACKGROUND_COLOR)
front_image = PhotoImage(file="./images/card_front.png")
back_image = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(CAN_X / 2, CAN_Y / 2, image=front_image)
canvas.grid(row=1, column=0, columnspan=2)

language = canvas.create_text(CAN_X / 2, CAN_Y / 4, text="", fill="black", font=(FONT_NAME, 30, "italic"))
guess_word = canvas.create_text(CAN_X / 2, CAN_Y / 2, text="", fill="black", font=(FONT_NAME, 60, "bold"))

# List Creation #

label = Label(text="Please choose your langauge: ", font=(FONT_NAME, 10, "bold"))
label.config(bg=BACKGROUND_COLOR)
label.grid(row=0, column=0)

combo = Combobox(state="readonly", values=["Dutch", "French", "German"])
combo.current(0) # Sets a default to Dutch so it can pass in something at the start
combo.bind("<<ComboboxSelected>>", lambda _ : word_generator()) # Makes the new option change straight away
combo.grid(row=0, column=1)

print(set_language())

# Buttons #

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=word_generator)
wrong_button.grid(column=0, row=2)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=word_generator)
right_button.grid(column=1, row=2)

word_generator()

window.mainloop()