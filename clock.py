##Imports
from tkinter import *
from tkinter import ttk
from tkinter import font
import winsound
import time
import calendar
import datetime

h = 0
m = 0
ap = "AM"


def current_time():

    seconds = calendar.timegm(time.gmtime())
    current_seconds = seconds % 60
    minutes = seconds // 60
    current_minutes = minutes % 60
    hours = minutes // 60
    current_hour = hours % 24
    current_hour = current_hour - 6

    if current_hour >= 12:
        tag="PM"
    else:
        tag="AM"
    timex = "6:05"
    return timex, tag


def quit(*args):

    root.destroy()


def show_time():

    time_dis = current_time()
    txt.set(time_dis)
    root.after(1000, show_time)


root = Tk()
frame = Frame(root, width=600, height=400)
frame.pack()
root.configure(background= 'CadetBlue')
root.bind("<Escape>", quit)
root.after(1000, show_time)
fnt = font.Font(family="Helvetica", size = 60, weight = "bold")
txt = StringVar()
lbl = ttk.Label(root, textvariable = txt, font = fnt, foreground = "DarkSlateGray", background = "DarkGoldenrod")
lbl.place(relx= 0.5, rely = 0.5, anchor = CENTER)
root.mainloop()
