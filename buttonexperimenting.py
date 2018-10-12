# Imports
from tkinter import *
from tkinter import ttk
from tkinter import font
import winsound
import time
import calendar
import datetime

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


class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)

        self.master = master

        self.init_window()

    def init_window(self):

        self.master.title("My Experiments")

        self.pack(fill=BOTH, expand=1)

        MainMenu = Menu(self.master)
        self.master.config(menu=MainMenu)

        file = Menu(MainMenu)
        file.add_command(label="Save", command=self.client_exit)
        file.add_command(label="Exit", command=self.client_exit)

        MainMenu.add_cascade(label="File", menu=file)

        edit = Menu(MainMenu)
        edit.add_command(label="Undo")
        MainMenu.add_cascade(label="Edit", menu=edit)

    def client_exit(self):
        exit()


root = Tk()
root.geometry("1200x600")
frame = Frame(root, width=600, height=1100)
frame.configure(background="CadetBlue")
frame.pack()
root.configure(background= 'CadetBlue')
root.bind("<Escape>", quit)
root.after(1000, show_time)
fnt = font.Font(family="Helvetica", size=60, weight="bold")
txt = StringVar()
lbl = ttk.Label(frame, textvariable=txt, font=fnt, foreground="DarkSlateGray", background="DarkGoldenrod")
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)
btn = Button(frame, text="Set Alarm", padx=0.5, pady=0.5)
btn.pack(fill=BOTH, expand=1)
btn.place(relx=0.35, rely=0.3, anchor=NE)
app = Window(root)

root.mainloop()
