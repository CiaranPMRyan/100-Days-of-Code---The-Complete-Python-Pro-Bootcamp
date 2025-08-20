from tkinter import *
from xml.dom.xmlbuilder import Options

import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
CAN_X = 800
CAN_Y = 526

FONT_NAME = "arial"

def word_generator():
    """ Picks a random word pairing from the spreadsheet """
    global lang
    pairing = data.iloc[random.randrange(len(data) - 1)]
    foreign_word = pairing[lang]
    english_word = pairing["English"]
    canvas.itemconfig(guess_word, text=pairing[lang])

#print(f"{pairing.English} - {pairing.French}")


# ---------- UI SETUP ---------- #

window = Tk()
window.title("Flashy Lingo")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Flash Card #

canvas = Canvas(width=CAN_X, height=CAN_Y, highlightthickness=0, bg=BACKGROUND_COLOR)
bg_image = PhotoImage(file="./images/card_front.png")
canvas.create_image(CAN_X / 2, CAN_Y / 2, image=bg_image)
canvas.grid(row=0, column=0, columnspan=2)

language = canvas.create_text(CAN_X / 2, CAN_Y / 4, text="", fill="black", font=(FONT_NAME, 30, "italic"))
guess_word = canvas.create_text(CAN_X / 2, CAN_Y / 2, text="", fill="black", font=(FONT_NAME, 60, "bold"))

# List Creation #

lang_list = ["Dutch", "French", "German"] # List to populate the box
lang_sel = StringVar(window)
lang_sel.set(lang_list[0])
lang_sel_dropdown = OptionMenu(window, lang_sel, *lang_list)
lang_sel_dropdown.grid(row=0, column=0)

# ---------- Pandas Logic ---------- #

lang = lang_sel.get()

data = pd.read_csv(f"./data/{lang}_words.csv")
data.to_dict(orient="records")

# Buttons #

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=word_generator)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=word_generator)
right_button.grid(column=1, row=1)

word_generator()

window.mainloop()