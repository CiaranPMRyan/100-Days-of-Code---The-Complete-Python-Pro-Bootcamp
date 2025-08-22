from tkinter import *
from tkinter.ttk import Combobox
import pandas as pd
import random
import time

BACKGROUND_COLOR = "#B1DDC6"
CAN_X = 800
CAN_Y = 526

FONT_NAME = "arial"

def word_generator():
    """ Picks a random word pairing from the spreadsheet """
    # ---------- Pandas Logic ---------- #

    lang = combo.get() # Gets the string from the dropdown list

    data = pd.read_csv(f"./data/{lang}_words.csv")
    data.to_dict(orient="records")

    pairing = data.iloc[random.randrange(len(data) - 1)]
    foreign_word = pairing[f"{lang}"]
    english_word = pairing["English"]

    canvas.itemconfig(canvas_image, image=front_image)
    canvas.itemconfig(language, text=f"{lang}", fill="black")
    canvas.itemconfig(guess_word, text=pairing[f"{lang}"], fill="black")

    window.after(3000, flip_card, foreign_word, english_word)

def flip_card(word_a, word_b):
    print(word_a)
    print(word_b)
    canvas.itemconfig(canvas_image, image=back_image)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(guess_word, text=f"{word_b}", fill="white")


# ---------- UI SETUP ---------- #

window = Tk()
window.title("Flashy Lingo")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

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


# Buttons #

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=word_generator)
wrong_button.grid(column=0, row=2)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=word_generator)
right_button.grid(column=1, row=2)

word_generator()

window.mainloop()