from random import choice
from tkinter import *
from tkinter import messagebox

import pandas

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("./data/english_bg_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(card_title, text="English", fill="black")
    canvas.itemconfig(card_word, text=current_card["English"], fill="black")
    canvas.itemconfig(card_bg, image=front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="Bulgarian", fill="white")
    canvas.itemconfig(card_word, text=current_card["Bulgarian"], fill="white")
    canvas.itemconfig(card_bg, image=back_img)


window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
try:
    front_img = PhotoImage(file="./images/card_front.png")
    back_img = PhotoImage(file="./images/card_back.png")
    card_bg = canvas.create_image(400, 263, image=front_img)
    card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
    card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
except TclError:
    messagebox.showwarning(title="Warning", message="Logo image not found!")

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

try:
    right_image = PhotoImage(file="./images/right.png")
    wrong_image = PhotoImage(file="./images/wrong.png")
except TclError:
    messagebox.showwarning(title="Warning", message="Image not found!")

right_button = Button(image=right_image, highlightthickness=0, cursor="hand2", command=next_card)
wrong_button = Button(image=wrong_image, highlightthickness=0, cursor="hand2", command=next_card)
right_button.grid(column=1, row=1)
wrong_button.grid(column=0, row=1)

next_card()

window.mainloop()
