from tkinter import *
import pandas
from random import choice
import os

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
    to_learn = data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
current_card = {}


def flip_card():
    global current_card
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    try:
        current_card = choice(to_learn)
    except IndexError:
        current_card = {}
        canvas.itemconfig(title, text="You've learned all the words!", fill="black")
        canvas.itemconfig(
            word,
            text="Run Again to Start Again",
            fill="black",
            font=("Arial", 45, "bold"),
        )
        canvas.itemconfig(canvas_image, image=card_front)
        try:
            os.remove("data/words_to_learn.csv")
        except FileNotFoundError:
            pass
        return
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front)
    flip_timer = window.after(3000, flip_card)


def is_known():
    global current_card
    if current_card in to_learn:
        to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)


right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")

right_button = Button(
    image=right_image,
    bg=BACKGROUND_COLOR,
    highlightthickness=0,
    command=is_known,
)
right_button.grid(row=1, column=1)
wrong_button = Button(
    image=wrong_image,
    bg=BACKGROUND_COLOR,
    highlightthickness=0,
    command=next_card,
)
wrong_button.grid(row=1, column=0)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=card_front)
title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

next_card()

window.mainloop()
