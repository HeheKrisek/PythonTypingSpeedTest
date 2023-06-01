from tkinter import *
from tkinter import filedialog, messagebox
import random
import datetime

FONT_NAME = "Courier"
COLOR_1 = "#B5F1CC"
COLOR_2 = "#E5FDD1"
COLOR_3 = "#C9F4AA"
COLOR_4 = "PURPLE"

WORDS = ["sin", "expenditure", "formulate", "will", "sniff", "side", "express", "create", "close", "sample", "fine",
         "dialect", "indirect", "method", "jump", "front", "choice", "wage", "insistence", "floor", "ward", "engineer",
         "nun", "carpet", "state", "onion", "twitch", "estate", "wander", "invisible", "hut", "scrap", "lover", "fame",
         "mosque", "crime", "television", "mechanism", "fireplace", "force", "tolerate", "accept", "magnitude",
         "shallow", "describe", "tip", "spend", "growth", "plaintiff", "family"]

def start_timer():
    text_to_type_label_input.pack()
    fillwords()
    test_time = 60
    count_down(test_time)

def count_down(time):
    time_label.config(text=f"Time left: {time} seconds")
    if time > -1:
        window.after(1000, count_down, time-1)

    if time == -1:
        time_label.config(text=f"Time's up!")
        the_end()

def prepare(time=3):
    start_button.pack_forget()
    text_to_type_label_input.pack_forget()
    time_label.config(text=f"Starting in {time}")
    if time > -1:
        window.after(1000, prepare, time - 1)

    if time == 0:
        window.after(1000, prepare, time - 1)
        time_label.config(text="GO!")

    if time == -1:
        start_timer()

def the_end():
    global index
    score = index - 5
    text_to_type_label.config(text=f"The end! Your score is {score} words per minute!")
    window.unbind('<Return>')
    text_to_type_label_input.pack_forget()
    start_button.pack()
    start_button.config(text="Start again")

def fillwords():
    window.bind('<Return>', check2)
    text_to_type_label_input.delete(0, END)
    global wrds
    wrds = []
    for i in range(0, 3):
        for word in WORDS:
            wrd = random.choice(WORDS)
            wrds.append(wrd)

    startwords = str(wrds[0:5])
    clean_startwords = startwords.strip("[]").replace("'", "")
    print(clean_startwords)
    text_to_type_label.config(text=clean_startwords)
    global index
    index = 5


def check2(event):
    global index
    text_to_check = text_to_type_label.cget("text")
    text_to_check.strip("[] ")
    print(text_to_check)
    words_to_check = text_to_check.split(",")
    words_to_check = [word.replace(" ", "") for word in words_to_check]
    print(words_to_check)

    answer = text_to_type_label_input.get()
    if answer in words_to_check:
        words_to_check.remove(answer)
        words_to_check.append(wrds[index])
        print(words_to_check)
        print("dziala")
        newtext = str(words_to_check)
        clean_newtext = newtext.strip("[]").replace("'", "")
        print(clean_newtext)
        text_to_type_label.config(text=clean_newtext)
        index += 1

    text_to_type_label_input.delete(0, END)

# def check(event):
#     global index
#     answer = "'" + text_to_type_label_input.get() + "', "
#     print(answer)
#     if answer in text_to_type_label.cget("text"):
#         newtext = text_to_type_label.cget("text").strip(answer)
#         print(newtext)
#         text_to_type_label.config(text=newtext)
#         text_to_type_label.config(text=text_to_type_label.cget("text")+wrds[index])
#         index += 1
#
#     text_to_type_label_input.delete(0, END)


window = Tk()

window.title("Typing speed test")
window.minsize(750, 600)
window.maxsize(750, 600)
window.config(padx=50, pady=50, bg=COLOR_1)

time_label = Label(text="", font=(FONT_NAME, 10, "bold"), bg=COLOR_1, fg=COLOR_4, pady=25)
time_label.pack()

title_label = Label(text="Test your typing speed!", font=(FONT_NAME, 20, "bold"), bg=COLOR_2, fg=COLOR_4, pady=25)
title_label.pack()

text_to_type_label = Label(text="Words to type will be shown here", font=(FONT_NAME, 15, "bold"), bg=COLOR_2, fg=COLOR_4)
text_to_type_label.pack()

text_to_type_label_input = Entry(window, width=37)
text_to_type_label_input.insert("0", "Type here")
text_to_type_label_input.pack()

start_button = Button(text="Start", highlightthickness=0, command=prepare)
start_button.pack()

window.mainloop()
