import pandas as pd
BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random
number = 0
total = 101
old_number = 0
import csv

try:
    new_data = pd.read_csv("flash-card-project-start/words_to_learn.csv")

except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
    list_of_dictionaries = data.to_dict(orient="records")
else:
    list_of_dictionaries = new_data.to_dict(orient="records")



def generate_word():
    global number
    global total

    number = random.randint(0,total)
    canvas.itemconfig(card, image=front_image)
    generated_word = list_of_dictionaries[number]["French"]
    canvas.itemconfig(Word, text =  generated_word)
    canvas.itemconfig(title, text = "French")
    window.after(3000, flip_card)


def flip_card():
    global number

    canvas.itemconfig(card , image = back_image)
    english_word = list_of_dictionaries[number]["English"]
    canvas.itemconfig(Word, text = english_word)
    canvas.itemconfig(title, text = "English")


def right():
    global number
    global total
    global old_number
    global list_of_dictionaries
    old_number = number
    total -= 1
    number = random.randint(0,total)

    generated_word = list_of_dictionaries[old_number]["French"]

    new_list = [i for i in list_of_dictionaries if  i["French"] != generated_word ]
    new_list2 = new_list.copy()
    keys = new_list2[0].keys()
    data = pandas.DataFrame(new_list)
    data.to_csv("words_to_learn")


    generate_word()
    list_of_dictionaries.pop(old_number)
    print(new_list)
#window
window = Tk()
window.title("Flash card")
window.config(padx = 50 , pady = 50,bg = BACKGROUND_COLOR)


#canvas
canvas = Canvas(width = 800, height = 526, bg = BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row = 0, column = 0 , columnspan= 2)

front_image = PhotoImage(file = "images/card_front.png")
back_image = PhotoImage(file = "images/card_back.png")
card = canvas.create_image(400,263, image = front_image)
Word = canvas.create_text(400,263,text = "Word", font = ("Ariel",60,"bold"))
title = canvas.create_text(400,150, text = "French",font = ("Ariel",40,"italic"))
#right and wrong buttons
right_image = PhotoImage(file="Images/right.png")
wrong_image = PhotoImage(file = "Images/wrong.png")
right_button = Button(image=right_image, highlightthickness=0, command = right)
right_button.grid(row = 1, column = 1)

wrong_button = Button(image = wrong_image, highlightthickness= 0, command = generate_word)
wrong_button.grid(row = 1, column = 0)



print(list_of_dictionaries[1]["French"])
print(list_of_dictionaries)
window.mainloop()